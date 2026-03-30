#!/usr/bin/env python3
"""Set markets.pipeline_status for one market.

Uses PREDQUANT_ORCHESTRATOR_URL by default.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

SQL = r'''
WITH input AS (
  SELECT (:'payload'::jsonb) AS j
),
updated AS (
  UPDATE markets m
  SET pipeline_status = (SELECT NULLIF(j->>'pipeline_status', '')::processing_status FROM input)
  FROM input i
  WHERE m.id = NULLIF(i.j->>'market_id', '')::uuid
  RETURNING m.id, m.platform, m.external_market_id, m.title, m.pipeline_status, m.current_price, m.last_reasoned_price, m.updated_at
)
SELECT json_build_object(
  'market_id', id,
  'platform', platform,
  'external_market_id', external_market_id,
  'title', title,
  'pipeline_status', pipeline_status,
  'current_price', current_price,
  'last_reasoned_price', last_reasoned_price,
  'updated_at', updated_at
)::text
FROM updated;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Set one market pipeline status")
    parser.add_argument("--file", default="-", help="Path to input JSON file, or - for stdin")
    parser.add_argument("--market-id", help="markets UUID")
    parser.add_argument("--pipeline-status", help="New pipeline status")
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
    if args.pipeline_status:
        payload["pipeline_status"] = args.pipeline_status

    if not payload.get("market_id"):
        raise ValueError("market_id is required")
    if not payload.get("pipeline_status"):
        raise ValueError("pipeline_status is required")

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
        raise ValueError("market not found or not updated")

    return json.loads(stdout.splitlines()[-1])


def main() -> int:
    args = parse_args()
    try:
        payload = build_payload(args)
        result = run_psql(args.psql, args.db_url, payload)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(result, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
