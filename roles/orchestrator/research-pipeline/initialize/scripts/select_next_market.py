#!/usr/bin/env python3
"""Select the next market for orchestrator processing.

MVP behavior:
- choose one market at a time
- only consider markets in pipeline_status new/pending_research
- skip markets that already have an open case
- return compact JSON describing the selected market

Uses PREDQUANT_ORCHESTRATOR_URL by default.
"""

import argparse
import json
import os
import subprocess
import sys

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

SQL = r'''
WITH eligible AS (
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
  WHERE m.pipeline_status IN ('new', 'pending_research')
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
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON result")
    return parser.parse_args()


def run_psql(psql_bin: str, db_url: str) -> dict:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")

    proc = subprocess.run(
        [
            psql_bin,
            db_url,
            "-X",
            "-qAt",
            "-v",
            "ON_ERROR_STOP=1",
            "-f",
            "-",
        ],
        input=SQL,
        text=True,
        capture_output=True,
    )

    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")

    stdout = proc.stdout.strip()
    if not stdout:
        raise ValueError("no eligible market found")

    line = stdout.splitlines()[-1]
    return json.loads(line)


def main() -> int:
    args = parse_args()
    try:
        result = run_psql(args.psql, args.db_url)
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
