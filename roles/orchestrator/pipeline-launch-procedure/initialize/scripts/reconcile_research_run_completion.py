#!/usr/bin/env python3
"""Reconcile a child-session completion event back into research_runs.

This script is the completion-side companion to the launch helpers.
It resolves the target run by notes.child_session_key and patches:
- status (completed or failed)
- completed_at when successful completion is indicated
- notes.dispatch_stage
- notes.error / notes.completion_summary when provided

Uses PREDQUANT_ORCHESTRATOR_URL by default.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

SQL_LOOKUP = r'''
WITH input AS (
  SELECT (:'payload'::jsonb) AS j
)
SELECT json_build_object(
  'research_run_id', rr.id,
  'case_id', rr.case_id,
  'run_label', rr.run_label,
  'agent_label', rr.agent_label,
  'status', rr.status,
  'workspace_note_path', rr.workspace_note_path,
  'notes', rr.notes,
  'created_at', rr.created_at
)::text
FROM research_runs rr
CROSS JOIN input i
WHERE rr.notes->>'child_session_key' = i.j->>'child_session_key'
ORDER BY rr.created_at DESC
LIMIT 1;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reconcile completion event to research_runs by child_session_key")
    parser.add_argument("--file", default="-", help="Path to input JSON file, or - for stdin")
    parser.add_argument("--child-session-key", help="Child session key from runtime event")
    parser.add_argument("--status", choices=["completed", "failed"], help="Final run status")
    parser.add_argument("--error", help="Optional error text when failed")
    parser.add_argument("--completion-summary", help="Optional completion summary text")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON result")
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
    if args.child_session_key:
        payload["child_session_key"] = args.child_session_key
    if args.status:
        payload["status"] = args.status
    if args.error:
        payload["error"] = args.error
    if args.completion_summary:
        payload["completion_summary"] = args.completion_summary
    if not payload.get("child_session_key"):
        raise ValueError("child_session_key is required")
    if not payload.get("status"):
        raise ValueError("status is required")
    return payload


def run_psql(psql_bin: str, db_url: str, payload: dict, sql: str) -> dict:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")
    payload_json = json.dumps(payload, separators=(",", ":"))
    proc = subprocess.run(
        [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1", "-v", f"payload={payload_json}", "-f", "-"],
        input=sql,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    if not stdout:
        raise ValueError("lookup returned no result")
    return json.loads(stdout.splitlines()[-1])


def python_json(script: Path, args: list[str], stdin_payload=None) -> dict:
    proc = subprocess.run(
        [sys.executable, str(script), *args],
        input=(json.dumps(stdin_payload) if stdin_payload is not None else None),
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"{script.name} failed")
    stdout = proc.stdout.strip()
    if not stdout:
        raise RuntimeError(f"{script.name} returned empty stdout")
    for line in reversed([line for line in stdout.splitlines() if line.strip()]):
        try:
            return json.loads(line)
        except json.JSONDecodeError:
            continue
    return json.loads(stdout)


def main() -> int:
    args = parse_args()
    try:
        payload = build_payload(args)
        lookup = run_psql(args.psql, args.db_url, payload, SQL_LOOKUP)
        update_script = Path(__file__).resolve().parent / "update_research_run.py"
        notes = {
            "dispatch_stage": "completed" if payload["status"] == "completed" else "terminated",
        }
        if payload.get("error"):
            notes["error"] = payload["error"]
        if payload.get("completion_summary"):
            notes["completion_summary"] = payload["completion_summary"]
        update_args = [
            "--research-run-id", lookup["research_run_id"],
            "--status", payload["status"],
            "--workspace-note-path", lookup.get("workspace_note_path") or "",
            "--notes-json", json.dumps(notes, separators=(",", ":")),
            "--db-url", args.db_url,
        ]
        if payload["status"] == "completed":
            update_args.append("--mark-completed")
        result = python_json(update_script, update_args)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    output = {
        "child_session_key": payload["child_session_key"],
        "matched_research_run_id": lookup["research_run_id"],
        "result": result,
    }
    if args.pretty:
        print(json.dumps(output, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(output, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
