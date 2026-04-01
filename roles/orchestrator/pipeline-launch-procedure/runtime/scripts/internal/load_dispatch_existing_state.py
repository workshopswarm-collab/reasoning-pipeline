#!/usr/bin/env python3
"""Load current DB state for all research_runs referenced by a dispatch manifest.

This helper makes the TUI/runtime handoff loop idempotent by returning a map
keyed by research_run_id with the current run status and relevant delivery
metadata.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR.parent
RUNTIME_DIR = SCRIPTS_DIR.parent
PIPELINE_DIR = RUNTIME_DIR.parent
WORKSPACE_ROOT = PIPELINE_DIR.parents[2]
DEFAULT_ENV_PATH = WORKSPACE_ROOT / ".env"

SQL = r'''
WITH input AS (
  SELECT (:'payload'::jsonb) AS j
),
run_ids AS (
  SELECT value::uuid AS research_run_id
  FROM input i, jsonb_array_elements_text(i.j->'research_run_ids') AS value
),
selected AS (
  SELECT
    rr.id,
    rr.status,
    rr.started_at,
    rr.completed_at,
    rr.workspace_note_path,
    rr.notes,
    COALESCE(rr.notes->>'dispatch_stage', '') AS dispatch_stage,
    COALESCE(rr.notes->>'delivery_target_session_key', '') AS delivery_target_session_key,
    COALESCE(rr.notes->>'delivery_target_chat_id', '') AS delivery_target_chat_id,
    COALESCE(rr.notes->>'delivery_target_topic_id', '') AS delivery_target_topic_id,
    COALESCE(rr.notes->>'delivery_target_topic_title', '') AS delivery_target_topic_title,
    COALESCE(rr.notes->>'controller_topic_id', '') AS controller_topic_id,
    COALESCE(rr.notes->>'controller_topic_title', '') AS controller_topic_title
  FROM research_runs rr
  JOIN run_ids r ON r.research_run_id = rr.id
)
SELECT COALESCE(json_object_agg(id::text, json_build_object(
  'status', status,
  'started_at', started_at,
  'completed_at', completed_at,
  'workspace_note_path', workspace_note_path,
  'dispatch_stage', NULLIF(dispatch_stage, ''),
  'delivery_target_session_key', NULLIF(delivery_target_session_key, ''),
  'delivery_target_chat_id', NULLIF(delivery_target_chat_id, ''),
  'delivery_target_topic_id', NULLIF(delivery_target_topic_id, ''),
  'delivery_target_topic_title', NULLIF(delivery_target_topic_title, ''),
  'controller_topic_id', NULLIF(controller_topic_id, ''),
  'controller_topic_title', NULLIF(controller_topic_title, ''),
  'notes', notes
)), '{}'::json)::text
FROM selected;
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
    parser = argparse.ArgumentParser(description="Load current DB state for manifest runs")
    parser.add_argument("--file", default="-", help="Path to dispatch manifest JSON, or - for stdin")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def load_json(path_str: str):
    if path_str == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path_str).read_text()
    if not raw.strip():
        raise ValueError("input JSON is empty")
    return json.loads(raw)


def run_psql(psql_bin: str, db_url: str, payload: dict[str, Any]) -> dict[str, Any]:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")
    payload_json = json.dumps(payload, separators=(",", ":"))
    proc = subprocess.run(
        [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1", "-v", f"payload={payload_json}", "-f", "-"],
        input=SQL,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    if not stdout:
        return {}
    return json.loads(stdout.splitlines()[-1])


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    try:
        manifest = load_json(args.file)
        run_ids = [run.get("research_run_id") for run in (manifest.get("runs") or []) if run.get("research_run_id")]
        result = run_psql(args.psql, args.db_url, {"research_run_ids": run_ids}) if run_ids else {}
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
