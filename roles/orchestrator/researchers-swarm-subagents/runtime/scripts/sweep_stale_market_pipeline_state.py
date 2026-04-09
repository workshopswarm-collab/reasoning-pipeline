#!/usr/bin/env python3
from __future__ import annotations

"""Preview and repair stale market-level pipeline state.

Repairs covered:
- expired open markets stuck in pipeline_status new/pending_research -> closed
- orphan researching markets with no open case:
  - expired -> closed
  - still not expired -> needs_intervention
"""

import argparse
import json
import os
import subprocess
import sys
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

PREVIEW_SQL = r'''
WITH expired_candidates AS (
  SELECT
    m.id AS market_id,
    m.title,
    m.status,
    m.pipeline_status,
    m.closes_at,
    m.resolves_at,
    m.updated_at,
    'closed'::text AS suggested_pipeline_status
  FROM markets m
  WHERE m.status = 'open'
    AND m.pipeline_status IN ('new', 'pending_research')
    AND (
      (m.closes_at IS NOT NULL AND m.closes_at <= NOW())
      OR (m.resolves_at IS NOT NULL AND m.resolves_at <= NOW())
    )
),
orphan_researching AS (
  SELECT
    m.id AS market_id,
    m.title,
    m.status,
    m.pipeline_status,
    m.closes_at,
    m.resolves_at,
    m.updated_at,
    CASE
      WHEN (m.closes_at IS NOT NULL AND m.closes_at <= NOW())
        OR (m.resolves_at IS NOT NULL AND m.resolves_at <= NOW())
      THEN 'closed'
      ELSE 'needs_intervention'
    END AS suggested_pipeline_status
  FROM markets m
  WHERE m.pipeline_status = 'researching'
    AND NOT EXISTS (
      SELECT 1
      FROM cases c
      WHERE c.market_id = m.id
        AND c.status = 'open'
    )
)
SELECT json_build_object(
  'expired_open_unactionable_markets', COALESCE((
    SELECT json_agg(row_to_json(x) ORDER BY x.closes_at DESC NULLS LAST, x.updated_at DESC NULLS LAST)
    FROM expired_candidates x
  ), '[]'::json),
  'orphan_researching_markets', COALESCE((
    SELECT json_agg(row_to_json(x) ORDER BY x.updated_at DESC NULLS LAST)
    FROM orphan_researching x
  ), '[]'::json)
)::text;
'''

APPLY_EXPIRED_SQL = r'''
WITH updated AS (
  UPDATE markets m
  SET pipeline_status = 'closed'::processing_status,
      updated_at = NOW()
  WHERE m.status = 'open'
    AND m.pipeline_status IN ('new', 'pending_research')
    AND (
      (m.closes_at IS NOT NULL AND m.closes_at <= NOW())
      OR (m.resolves_at IS NOT NULL AND m.resolves_at <= NOW())
    )
  RETURNING m.id AS market_id, m.title, m.pipeline_status, m.closes_at, m.resolves_at
)
SELECT json_build_object(
  'updated_count', COUNT(*),
  'updated_markets', COALESCE(json_agg(row_to_json(updated) ORDER BY closes_at DESC NULLS LAST), '[]'::json)
)::text
FROM updated;
'''

APPLY_ORPHAN_SQL = r'''
WITH updated AS (
  UPDATE markets m
  SET pipeline_status = CASE
        WHEN (m.closes_at IS NOT NULL AND m.closes_at <= NOW())
          OR (m.resolves_at IS NOT NULL AND m.resolves_at <= NOW())
        THEN 'closed'::processing_status
        ELSE 'needs_intervention'::processing_status
      END,
      updated_at = NOW()
  WHERE m.pipeline_status = 'researching'
    AND NOT EXISTS (
      SELECT 1
      FROM cases c
      WHERE c.market_id = m.id
        AND c.status = 'open'
    )
  RETURNING m.id AS market_id, m.title, m.pipeline_status, m.closes_at, m.resolves_at
)
SELECT json_build_object(
  'updated_count', COUNT(*),
  'updated_markets', COALESCE(json_agg(row_to_json(updated) ORDER BY closes_at DESC NULLS LAST), '[]'::json)
)::text
FROM updated;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Preview/repair stale market pipeline state")
    parser.add_argument("--apply", action="store_true", help="Apply the suggested market-state repairs")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def exec_sql(psql_bin: str, db_url: str, sql: str) -> dict[str, Any]:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")
    proc = subprocess.run([psql_bin, db_url, '-X', '-qAt', '-v', 'ON_ERROR_STOP=1', '-f', '-'], input=sql, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'psql failed')
    stdout = proc.stdout.strip()
    return json.loads(stdout.splitlines()[-1]) if stdout else {}


def main() -> int:
    args = parse_args()
    try:
        preview = exec_sql(args.psql, args.db_url, PREVIEW_SQL)
        expired_result = None
        orphan_result = None
        if args.apply:
            expired_result = exec_sql(args.psql, args.db_url, APPLY_EXPIRED_SQL)
            orphan_result = exec_sql(args.psql, args.db_url, APPLY_ORPHAN_SQL)
            preview = exec_sql(args.psql, args.db_url, PREVIEW_SQL)
        result = {
            'status': 'ok',
            'preview': preview,
            'expired_apply_result': expired_result,
            'orphan_apply_result': orphan_result,
        }
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(result, separators=(',', ':'), default=str))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
