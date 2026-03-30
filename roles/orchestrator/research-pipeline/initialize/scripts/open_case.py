#!/usr/bin/env python3
"""Open or fetch an orchestrator case for a market.

MVP behavior:
- accept either market_id or (platform, external_market_id)
- load the market from Postgres
- if an open case already exists for that market, return it
- otherwise create a new case row with generated case_key
- return a small JSON payload

Uses PREDQUANT_ORCHESTRATOR_URL by default.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
DEFAULT_CREATED_BY = "orchestrator"

SQL = r'''
WITH input AS (
  SELECT (:'payload'::jsonb) AS j
),
resolved_market AS (
  SELECT m.id, m.platform, m.external_market_id
  FROM markets m
  CROSS JOIN input i
  WHERE (
    NULLIF(i.j->>'market_id', '') IS NOT NULL
    AND m.id = NULLIF(i.j->>'market_id', '')::uuid
  )
  OR (
    NULLIF(i.j->>'market_id', '') IS NULL
    AND m.platform = i.j->>'platform'
    AND m.external_market_id = i.j->>'external_market_id'
  )
  LIMIT 1
),
existing_case AS (
  SELECT c.id, c.market_id, c.case_key, c.status, c.priority
  FROM cases c
  JOIN resolved_market rm ON rm.id = c.market_id
  WHERE c.status = 'open'
  ORDER BY c.opened_at DESC
  LIMIT 1
),
inserted_case AS (
  INSERT INTO cases (
    market_id,
    case_key,
    status,
    priority,
    created_by,
    orchestration_notes
  )
  SELECT
    rm.id,
    'case-' || to_char(NOW() AT TIME ZONE 'UTC', 'YYYYMMDD') || '-' || substr(replace(gen_random_uuid()::text, '-', ''), 1, 8),
    'open',
    COALESCE(NULLIF(i.j->>'priority', ''), 'normal'),
    COALESCE(NULLIF(i.j->>'created_by', ''), 'orchestrator'),
    COALESCE(i.j->'orchestration_notes', '{}'::jsonb)
  FROM resolved_market rm
  CROSS JOIN input i
  WHERE NOT EXISTS (SELECT 1 FROM existing_case)
  RETURNING id, market_id, case_key, status, priority
),
final_case AS (
  SELECT * FROM existing_case
  UNION ALL
  SELECT * FROM inserted_case
)
SELECT json_build_object(
  'case_id', fc.id,
  'case_key', fc.case_key,
  'market_id', fc.market_id,
  'status', fc.status,
  'priority', fc.priority
)::text
FROM final_case fc
LIMIT 1;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Open or fetch an open case for a market")
    parser.add_argument("--file", default="-", help="Path to input JSON file, or - for stdin")
    parser.add_argument("--market-id", help="Market UUID")
    parser.add_argument("--platform", help="Market platform, e.g. polymarket")
    parser.add_argument("--external-market-id", help="External market identifier")
    parser.add_argument("--priority", default="normal", help="Case priority")
    parser.add_argument("--created-by", default=DEFAULT_CREATED_BY, help="Case creator label")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON result")
    return parser.parse_args()


def load_json(path_str: str):
    if path_str == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path_str).read_text()
    if not raw.strip():
        return {}
    return json.loads(raw)


def build_payload(args: argparse.Namespace) -> dict:
    payload = load_json(args.file)
    if payload and not isinstance(payload, dict):
        raise ValueError("input JSON must be an object")

    payload = dict(payload or {})

    if args.market_id:
        payload["market_id"] = args.market_id
    if args.platform:
        payload["platform"] = args.platform
    if args.external_market_id:
        payload["external_market_id"] = args.external_market_id
    if args.priority:
        payload["priority"] = args.priority
    if args.created_by:
        payload["created_by"] = args.created_by

    has_market_id = bool(payload.get("market_id"))
    has_platform_key = bool(payload.get("platform")) and bool(payload.get("external_market_id"))

    if not has_market_id and not has_platform_key:
        raise ValueError("provide either market_id or both platform and external_market_id")

    return payload


def run_psql(psql_bin: str, db_url: str, payload: dict) -> dict:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")

    payload_json = json.dumps(payload, separators=(",", ":"))

    proc = subprocess.run(
        [
            psql_bin,
            db_url,
            "-X",
            "-qAt",
            "-v",
            "ON_ERROR_STOP=1",
            "-v",
            f"payload={payload_json}",
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
        raise ValueError("market not found or no case returned")

    line = stdout.splitlines()[-1]
    return json.loads(line)


def main() -> int:
    args = parse_args()
    try:
        payload = build_payload(args)
        result = run_psql(args.psql, args.db_url, payload)
    except Exception as exc:  # noqa: BLE001 - small CLI utility
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(json.dumps(result, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
