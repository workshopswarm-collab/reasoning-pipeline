#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
ALLOWED_STATUSES = {"unresolved", "resolved", "canceled", "disputed", "error"}

UPSERT_SQL = r'''
INSERT INTO public.market_resolutions (
  market_id,
  contract_id,
  platform,
  resolution_status,
  resolved_outcome,
  resolved_value,
  resolved_ts,
  resolution_source,
  resolution_notes,
  updated_at
)
VALUES (
  :'market_id',
  :'contract_id',
  :'platform',
  :'resolution_status',
  NULLIF(:'resolved_outcome', ''),
  NULLIF(:'resolved_value', '')::numeric,
  NULLIF(:'resolved_ts', '')::timestamptz,
  NULLIF(:'resolution_source', ''),
  NULLIF(:'resolution_notes', ''),
  NOW()
)
ON CONFLICT (market_id, contract_id)
DO UPDATE SET
  platform = EXCLUDED.platform,
  resolution_status = EXCLUDED.resolution_status,
  resolved_outcome = EXCLUDED.resolved_outcome,
  resolved_value = EXCLUDED.resolved_value,
  resolved_ts = EXCLUDED.resolved_ts,
  resolution_source = EXCLUDED.resolution_source,
  resolution_notes = EXCLUDED.resolution_notes,
  updated_at = NOW()
RETURNING json_build_object(
  'market_id', market_id,
  'contract_id', contract_id,
  'platform', platform,
  'resolution_status', resolution_status,
  'resolved_outcome', resolved_outcome,
  'resolved_value', resolved_value,
  'resolved_ts', resolved_ts,
  'resolution_source', resolution_source,
  'resolution_notes', resolution_notes
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manual upsert helper for public.market_resolutions")
    parser.add_argument("--market-id", required=True)
    parser.add_argument("--contract-id", required=True)
    parser.add_argument("--platform", default="polymarket")
    parser.add_argument("--resolution-status", required=True, choices=sorted(ALLOWED_STATUSES))
    parser.add_argument("--resolved-outcome", default="")
    parser.add_argument("--resolved-value", default="")
    parser.add_argument("--resolved-ts", default="")
    parser.add_argument("--resolution-source", default="")
    parser.add_argument("--resolution-notes", default="")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL") or os.getenv("PREDQUANT_ADMIN_URL", ""))
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL))
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def normalize_outcome(value: str) -> str:
    return value.strip().lower()


def normalize_value(value: str) -> str:
    raw = value.strip()
    if not raw:
        return ""
    num = float(raw)
    if num < 0 or num > 1:
        raise ValueError("--resolved-value must be between 0 and 1")
    return f"{num:.5f}"


def infer_resolved_value(status: str, outcome: str, provided_value: str) -> str:
    if provided_value:
        return provided_value
    if status != "resolved":
        return ""
    if outcome == "yes":
        return "1.00000"
    if outcome == "no":
        return "0.00000"
    return ""


def validate_args(args: argparse.Namespace) -> dict[str, str]:
    outcome = normalize_outcome(args.resolved_outcome)
    value = normalize_value(args.resolved_value)
    inferred_value = infer_resolved_value(args.resolution_status, outcome, value)

    if args.resolution_status == "resolved" and not (outcome or inferred_value):
        raise ValueError("resolved rows require --resolved-outcome and/or --resolved-value")

    if args.resolution_status != "resolved" and args.resolved_ts and args.resolution_status not in {"canceled", "disputed", "error", "unresolved"}:
        raise ValueError("unexpected resolution status")

    return {
        "market_id": args.market_id.strip(),
        "contract_id": args.contract_id.strip(),
        "platform": args.platform.strip().lower() or "polymarket",
        "resolution_status": args.resolution_status,
        "resolved_outcome": outcome,
        "resolved_value": inferred_value,
        "resolved_ts": args.resolved_ts.strip(),
        "resolution_source": args.resolution_source.strip(),
        "resolution_notes": args.resolution_notes.strip(),
    }


def exec_sql(psql_bin: str, db_url: str, sql: str, variables: dict[str, str]) -> dict[str, Any] | None:
    if not db_url:
        raise ValueError("--db-url, PREDQUANT_ORCHESTRATOR_URL, or PREDQUANT_ADMIN_URL is required")
    cmd = [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1"]
    for key, value in variables.items():
        cmd.extend(["-v", f"{key}={value}"])
    cmd.extend(["-f", "-"])
    proc = subprocess.run(cmd, input=sql, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    if not stdout:
        return None
    return json.loads(stdout.splitlines()[-1])


def main() -> int:
    args = parse_args()
    record = validate_args(args)
    persisted = exec_sql(args.psql, args.db_url, UPSERT_SQL, record) or {}
    print(json.dumps({
        "ok": True,
        "persisted": persisted,
        "record": record,
    }, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
