#!/usr/bin/env python3
"""Select the next market for orchestrator processing.

MVP behavior:
- choose one market at a time
- by default, refuse to select a new market while the pipeline is already busy with another case
- only consider markets in pipeline_status new/pending_research
- skip markets that already have an open case
- skip markets that are already expired by closes_at/resolves_at
- return compact JSON describing the selected market

Uses PREDQUANT_ORCHESTRATOR_URL by default.
"""

import argparse
import json
import os
import subprocess
import sys

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

BUSY_SQL = r'''
SELECT json_build_object(
  'pipeline_busy', EXISTS (
    SELECT 1
    FROM cases c
    JOIN markets m ON m.id = c.market_id
    WHERE c.status = 'open'
      AND m.pipeline_status = 'researching'
  )
)::text;
'''

SQL = r'''
WITH busy AS (
  SELECT EXISTS (
    SELECT 1
    FROM cases c
    JOIN markets m ON m.id = c.market_id
    WHERE c.status = 'open'
      AND m.pipeline_status = 'researching'
  ) AS pipeline_busy
),
eligible AS (
  SELECT
    m.id,
    m.platform,
    m.external_market_id,
    m.slug,
    m.title,
    m.description,
    m.category,
    m.status,
    m.outcome_type,
    m.closes_at,
    m.resolves_at,
    m.metadata,
    m.pipeline_status,
    m.current_price,
    m.last_reasoned_price,
    m.updated_at
  FROM markets m
  CROSS JOIN busy b
  WHERE (COALESCE(:'allow_when_busy', '') = 'true' OR b.pipeline_busy = false)
    AND m.status = 'open'
    AND m.pipeline_status IN ('new', 'pending_research')
    AND (m.closes_at IS NULL OR m.closes_at > NOW())
    AND (m.resolves_at IS NULL OR m.resolves_at > NOW())
    AND NOT EXISTS (
      SELECT 1
      FROM cases c
      WHERE c.market_id = m.id
        AND c.status = 'open'
    )
),
ranked AS (
  SELECT *
  FROM eligible
  ORDER BY
    CASE pipeline_status
      WHEN 'pending_research' THEN 0
      WHEN 'new' THEN 1
      ELSE 9
    END,
    closes_at ASC NULLS LAST,
    updated_at DESC,
    id ASC
  LIMIT 1
)
SELECT json_build_object(
  'market_id', id,
  'platform', platform,
  'external_market_id', external_market_id,
  'slug', slug,
  'title', title,
  'description', description,
  'category', category,
  'status', status,
  'outcome_type', outcome_type,
  'closes_at', closes_at,
  'resolves_at', resolves_at,
  'metadata', metadata,
  'pipeline_status', pipeline_status,
  'current_price', current_price,
  'last_reasoned_price', last_reasoned_price,
  'updated_at', updated_at
)::text
FROM ranked;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Select the next eligible market for orchestrator processing")
    parser.add_argument("--allow-when-busy", action="store_true", help="Bypass the global sequential-processing gate and select even if another case is already researching")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON result")
    return parser.parse_args()


def run_query(psql_bin: str, db_url: str, sql_text: str, *, allow_when_busy: bool) -> subprocess.CompletedProcess:
    return subprocess.run(
        [
            psql_bin,
            db_url,
            "-X",
            "-qAt",
            "-v",
            "ON_ERROR_STOP=1",
            "-v",
            f"allow_when_busy={'true' if allow_when_busy else 'false'}",
            "-f",
            "-",
        ],
        input=sql_text,
        text=True,
        capture_output=True,
    )


def run_psql(psql_bin: str, db_url: str, *, allow_when_busy: bool) -> dict:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")

    proc = run_query(psql_bin, db_url, SQL, allow_when_busy=allow_when_busy)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")

    stdout = proc.stdout.strip()
    if not stdout:
        busy = run_query(psql_bin, db_url, BUSY_SQL, allow_when_busy=allow_when_busy)
        if busy.returncode == 0 and busy.stdout.strip():
            payload = json.loads(busy.stdout.splitlines()[-1])
            if payload.get("pipeline_busy") and not allow_when_busy:
                raise ValueError("pipeline already busy with an open researching case")
        raise ValueError("no eligible market found")

    line = stdout.splitlines()[-1]
    return json.loads(line)


def main() -> int:
    args = parse_args()
    try:
        result = run_psql(args.psql, args.db_url, allow_when_busy=args.allow_when_busy)
    except Exception as exc:  # noqa: BLE001 - small CLI utility
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(result, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
