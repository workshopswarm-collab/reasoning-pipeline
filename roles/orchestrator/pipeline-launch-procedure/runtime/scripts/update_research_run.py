#!/usr/bin/env python3
from __future__ import annotations

"""Patch one research_runs row.

Supports updating:
- status
- started_at (set automatically when --mark-started is used)
- completed_at (set automatically when --mark-completed is used)
- workspace_note_path
- notes (merged into existing notes)

Uses PREDQUANT_ORCHESTRATOR_URL by default.
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
AUTO_FINALIZER = BASE_DIR / "auto_finalize_case_after_terminal_run.py"
TERMINAL_STATUSES = {"completed", "failed"}

SQL = r'''
WITH input AS (
  SELECT (:'payload'::jsonb) AS j
),
updated AS (
  UPDATE research_runs rr
  SET
    status = COALESCE(NULLIF(i.j->>'status', ''), rr.status),
    started_at = CASE
      WHEN COALESCE((i.j->>'mark_started')::boolean, false) THEN COALESCE(rr.started_at, NOW())
      ELSE rr.started_at
    END,
    completed_at = CASE
      WHEN COALESCE((i.j->>'mark_completed')::boolean, false) THEN NOW()
      ELSE rr.completed_at
    END,
    workspace_note_path = COALESCE(NULLIF(i.j->>'workspace_note_path', ''), rr.workspace_note_path),
    notes = COALESCE(rr.notes, '{}'::jsonb) || COALESCE(i.j->'notes', '{}'::jsonb)
  FROM input i
  WHERE rr.id = NULLIF(i.j->>'research_run_id', '')::uuid
  RETURNING rr.id, rr.case_id, rr.run_label, rr.agent_label, rr.runtime, rr.status, rr.started_at, rr.completed_at, rr.workspace_note_path, rr.notes, rr.created_at
)
SELECT json_build_object(
  'research_run_id', id,
  'case_id', case_id,
  'run_label', run_label,
  'agent_label', agent_label,
  'runtime', runtime,
  'status', status,
  'started_at', started_at,
  'completed_at', completed_at,
  'workspace_note_path', workspace_note_path,
  'notes', notes,
  'created_at', created_at
)::text
FROM updated;
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
    parser = argparse.ArgumentParser(description="Patch one research run")
    parser.add_argument("--file", default="-", help="Path to input JSON file, or - for stdin")
    parser.add_argument("--research-run-id", help="research_runs UUID")
    parser.add_argument("--status", help="New run status")
    parser.add_argument("--workspace-note-path", help="Primary qualitative artifact path")
    parser.add_argument("--notes-json", help="JSON object merged into notes")
    parser.add_argument("--mark-started", action="store_true", help="Set started_at = NOW() if not already set")
    parser.add_argument("--mark-completed", action="store_true", help="Set completed_at = NOW()")
    parser.add_argument("--skip-auto-finalize", action="store_true", help="Do not attempt automatic case/market finalization after terminal updates")
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

    if args.research_run_id:
        payload["research_run_id"] = args.research_run_id
    if args.status:
        payload["status"] = args.status
    if args.workspace_note_path:
        payload["workspace_note_path"] = args.workspace_note_path
    if args.notes_json:
        payload["notes"] = json.loads(args.notes_json)
    if args.mark_started:
        payload["mark_started"] = True
    if args.mark_completed:
        payload["mark_completed"] = True

    if not payload.get("research_run_id"):
        raise ValueError("research_run_id is required")

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
        raise ValueError("research run not found or not updated")

    return json.loads(stdout.splitlines()[-1])


def parse_json_lines(raw: str) -> dict:
    stdout = (raw or "").strip()
    if not stdout:
        return {}
    for line in reversed([line for line in stdout.splitlines() if line.strip()]):
        try:
            return json.loads(line)
        except json.JSONDecodeError:
            continue
    return json.loads(stdout)


def maybe_auto_finalize(args: argparse.Namespace, result: dict) -> dict | None:
    if args.skip_auto_finalize or os.getenv("ORCHESTRATOR_SKIP_AUTO_FINALIZE") == "1":
        return None
    if result.get("status") not in TERMINAL_STATUSES:
        return None
    research_run_id = result.get("research_run_id")
    if not research_run_id:
        return None

    proc = subprocess.run(
        [
            sys.executable,
            str(AUTO_FINALIZER),
            "--research-run-id",
            research_run_id,
            "--db-url",
            args.db_url,
        ],
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        return {
            "status": "error",
            "error": proc.stderr.strip() or proc.stdout.strip() or f"{AUTO_FINALIZER.name} failed",
        }
    parsed = parse_json_lines(proc.stdout)
    parsed.setdefault("status", "ok")
    return parsed


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    try:
        payload = build_payload(args)
        result = run_psql(args.psql, args.db_url, payload)
        auto_finalize = maybe_auto_finalize(args, result)
        if auto_finalize is not None:
            result["auto_finalize"] = auto_finalize
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
