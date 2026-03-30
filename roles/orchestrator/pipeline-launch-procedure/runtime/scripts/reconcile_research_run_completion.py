#!/usr/bin/env python3
"""Reconcile a run completion back into research_runs.

Current behavior:
- resolve by `research_run_id`
- patch status to completed/failed
- set completed_at for successful completion
- store completion summary / error in notes
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
BASE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = BASE_DIR.parent
PIPELINE_DIR = RUNTIME_DIR.parent
WORKSPACE_ROOT = PIPELINE_DIR.parents[2]
DEFAULT_ENV_PATH = WORKSPACE_ROOT / ".env"

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
WHERE rr.id = NULLIF(i.j->>'research_run_id', '')::uuid
ORDER BY rr.created_at DESC
LIMIT 1;
'''


def maybe_load_workspace_env() -> None:
    if os.getenv("PREDQUANT_ORCHESTRATOR_URL"):
        return
    if not DEFAULT_ENV_PATH.exists():
        return
    for raw_line in DEFAULT_ENV_PATH.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reconcile completion event to research_runs")
    parser.add_argument("--file", default="-", help="Path to input JSON file, or - for stdin")
    parser.add_argument("--research-run-id", required=True, help="Primary completion join key for fixed-channel runs")
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
    payload["research_run_id"] = args.research_run_id
    if args.status:
        payload["status"] = args.status
    if args.error:
        payload["error"] = args.error
    if args.completion_summary:
        payload["completion_summary"] = args.completion_summary
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
    maybe_load_workspace_env()
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
        "research_run_id": lookup["research_run_id"],
        "result": result,
    }
    if args.pretty:
        print(json.dumps(output, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(output, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
