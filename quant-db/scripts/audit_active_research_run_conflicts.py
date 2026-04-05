#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

SQL = r'''
SELECT COALESCE(json_agg(json_build_object(
  'case_id', x.case_id,
  'case_key', x.case_key,
  'agent_label', x.agent_label,
  'active_attempt_count', x.active_attempt_count,
  'statuses', x.statuses,
  'run_ids', x.run_ids
) ORDER BY x.case_key, x.agent_label), '[]'::json)::text
FROM (
  SELECT
    rr.case_id,
    c.case_key,
    rr.agent_label,
    COUNT(*) AS active_attempt_count,
    json_agg(rr.status ORDER BY rr.created_at, rr.id) AS statuses,
    json_agg(rr.id ORDER BY rr.created_at, rr.id) AS run_ids
  FROM research_runs rr
  JOIN cases c ON c.id = rr.case_id
  WHERE rr.status IN ('queued', 'running')
  GROUP BY rr.case_id, c.case_key, rr.agent_label
  HAVING COUNT(*) > 1
) x;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit active queued/running research-run conflicts before applying uniqueness hardening")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.db_url:
        print("ERROR: --db-url or PREDQUANT_ORCHESTRATOR_URL is required", file=sys.stderr)
        return 1
    proc = subprocess.run([args.psql, args.db_url, '-X', '-qAt', '-v', 'ON_ERROR_STOP=1', '-f', '-'], input=SQL, text=True, capture_output=True)
    if proc.returncode != 0:
        print(f"ERROR: {proc.stderr.strip() or 'psql failed'}", file=sys.stderr)
        return 1
    stdout = proc.stdout.strip()
    payload = json.loads(stdout.splitlines()[-1]) if stdout else []
    result = {'status': 'ok', 'conflict_count': len(payload), 'conflicts': payload}
    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(result, separators=(',', ':'), default=str))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
