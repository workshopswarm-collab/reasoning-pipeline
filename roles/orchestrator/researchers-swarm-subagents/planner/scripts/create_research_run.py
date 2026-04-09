#!/usr/bin/env python3
"""Create one research_runs row for a case.

MVP behavior:
- accept case_id
- require agent_label
- optionally accept run_label, runtime, workspace_note_path, notes
- insert a queued run with started_at unset until runtime launch actually succeeds
- return compact JSON

Uses PREDQUANT_ORCHESTRATOR_URL by default.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
DEFAULT_RUNTIME = "openclaw-telegram-forum-topic"

SQL = r'''
WITH input AS (
  SELECT (:'payload'::jsonb) AS j
),
resolved_case AS (
  SELECT c.id
  FROM cases c
  CROSS JOIN input i
  WHERE c.id = NULLIF(i.j->>'case_id', '')::uuid
  LIMIT 1
),
inserted_run AS (
  INSERT INTO research_runs (
    case_id,
    run_label,
    agent_label,
    runtime,
    status,
    started_at,
    workspace_note_path,
    notes
  )
  SELECT
    rc.id,
    NULLIF(i.j->>'run_label', ''),
    i.j->>'agent_label',
    COALESCE(NULLIF(i.j->>'runtime', ''), 'openclaw-telegram-forum-topic'),
    COALESCE(NULLIF(i.j->>'status', ''), 'queued'),
    NULL,
    NULLIF(i.j->>'workspace_note_path', ''),
    COALESCE(i.j->'notes', '{}'::jsonb)
  FROM resolved_case rc
  CROSS JOIN input i
  RETURNING id, case_id, run_label, agent_label, runtime, status, started_at, workspace_note_path, notes, created_at
)
SELECT json_build_object(
  'research_run_id', id,
  'case_id', case_id,
  'run_label', run_label,
  'agent_label', agent_label,
  'runtime', runtime,
  'status', status,
  'started_at', started_at,
  'workspace_note_path', workspace_note_path,
  'notes', notes,
  'created_at', created_at
)::text
FROM inserted_run;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create one research run for a case")
    parser.add_argument("--file", default="-", help="Path to input JSON file, or - for stdin")
    parser.add_argument("--case-id", help="Case UUID")
    parser.add_argument("--agent-label", help="Research persona / agent label")
    parser.add_argument("--run-label", help="Optional run label")
    parser.add_argument("--runtime", default=DEFAULT_RUNTIME, help="Runtime label")
    parser.add_argument("--workspace-note-path", help="Primary qualitative artifact path")
    parser.add_argument("--notes-json", help="JSON object merged into notes")
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

    if args.case_id:
        payload["case_id"] = args.case_id
    if args.agent_label:
        payload["agent_label"] = args.agent_label
    if args.run_label:
        payload["run_label"] = args.run_label
    if args.runtime:
        payload["runtime"] = args.runtime
    if args.workspace_note_path:
        payload["workspace_note_path"] = args.workspace_note_path
    if args.notes_json:
        payload["notes"] = json.loads(args.notes_json)

    if not payload.get("case_id"):
        raise ValueError("case_id is required")
    if not payload.get("agent_label"):
        raise ValueError("agent_label is required")

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
        raise ValueError("case not found or research run not created")

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
