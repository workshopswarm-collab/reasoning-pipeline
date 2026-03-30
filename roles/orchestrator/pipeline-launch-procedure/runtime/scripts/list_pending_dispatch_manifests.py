#!/usr/bin/env python3
"""List dispatch manifests that still need fixed-channel launch work.

This is a lightweight helper for the current TUI/runtime handoff loop.
It scans the manifest directory, looks up the referenced research_runs rows, and
classifies each manifest into one of:
- pending_launch   : at least one run is still queued and has not been handed off
- inflight         : no queued launchable runs remain, but some runs are running
- terminal         : all runs are terminal (completed/failed)
- unknown          : manifest/runtime state could not be classified cleanly

Default output returns only manifests with pending launch work.
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
RUNTIME_DIR = BASE_DIR.parent
PIPELINE_DIR = RUNTIME_DIR.parent
WORKSPACE_ROOT = PIPELINE_DIR.parents[2]
DEFAULT_MANIFEST_DIR = RUNTIME_DIR / "dispatch-manifests"
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
    rr.case_id,
    rr.run_label,
    rr.agent_label,
    rr.status,
    rr.started_at,
    rr.completed_at,
    rr.created_at,
    rr.notes,
    COALESCE(rr.notes->>'delivery_target_session_key', '') AS delivery_target_session_key,
    COALESCE(rr.notes->>'dispatch_stage', '') AS dispatch_stage
  FROM research_runs rr
  JOIN run_ids r ON r.research_run_id = rr.id
)
SELECT COALESCE(json_agg(json_build_object(
  'research_run_id', id,
  'case_id', case_id,
  'run_label', run_label,
  'agent_label', agent_label,
  'status', status,
  'started_at', started_at,
  'completed_at', completed_at,
  'created_at', created_at,
  'dispatch_stage', dispatch_stage,
  'delivery_target_session_key', NULLIF(delivery_target_session_key, ''),
  'notes', notes
) ORDER BY created_at), '[]'::json)::text
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
    parser = argparse.ArgumentParser(description="List dispatch manifests that still need launch work")
    parser.add_argument("--manifest-dir", default=str(DEFAULT_MANIFEST_DIR), help="Dispatch manifest directory")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument(
        "--include",
        default="pending_launch",
        help="Comma-separated classes to include (pending_launch,inflight,terminal,unknown,all)",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def run_psql(psql_bin: str, db_url: str, payload: dict[str, Any]) -> list[dict[str, Any]]:
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
        return []
    return json.loads(stdout.splitlines()[-1])


def classify_manifest(run_rows: list[dict[str, Any]]) -> tuple[str, dict[str, int]]:
    counts = {
        "queued": 0,
        "running": 0,
        "completed": 0,
        "failed": 0,
        "with_delivery_target": 0,
        "without_delivery_target": 0,
    }
    for row in run_rows:
        status = row.get("status") or ""
        if status in counts:
            counts[status] += 1
        delivery_target = row.get("delivery_target_session_key")
        if delivery_target:
            counts["with_delivery_target"] += 1
        else:
            counts["without_delivery_target"] += 1

    launchable = [
        row for row in run_rows
        if row.get("status") == "queued"
    ]
    running = [row for row in run_rows if row.get("status") == "running"]
    terminal = [row for row in run_rows if row.get("status") in {"completed", "failed"}]

    if launchable:
        return "pending_launch", counts
    if running:
        return "inflight", counts
    if run_rows and len(terminal) == len(run_rows):
        return "terminal", counts
    return "unknown", counts


def load_manifest(path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text())
        if isinstance(data, dict):
            return data
    except Exception:
        return None
    return None


def include_class(kind: str, include_raw: str) -> bool:
    tokens = {token.strip() for token in include_raw.split(",") if token.strip()}
    if not tokens or "pending_launch" in tokens:
        tokens = tokens or {"pending_launch"}
    if "all" in tokens:
        return True
    return kind in tokens


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    manifest_dir = Path(args.manifest_dir).expanduser().resolve()
    manifest_dir.mkdir(parents=True, exist_ok=True)

    manifests = []
    for path in sorted(manifest_dir.glob("*.json")):
        manifest = load_manifest(path)
        if not manifest:
            continue
        runs = manifest.get("runs") or []
        run_ids = [run.get("research_run_id") for run in runs if run.get("research_run_id")]
        if not run_ids:
            continue
        run_rows = run_psql(args.psql, args.db_url, {"research_run_ids": run_ids})
        kind, counts = classify_manifest(run_rows)
        if not include_class(kind, args.include):
            continue
        manifests.append({
            "dispatch_id": manifest.get("dispatch_id"),
            "manifest_path": str(path),
            "case_id": (manifest.get("case") or {}).get("case_id"),
            "case_key": (manifest.get("case") or {}).get("case_key"),
            "market_title": (manifest.get("market") or {}).get("title"),
            "created_at": manifest.get("created_at"),
            "classification": kind,
            "counts": counts,
            "run_rows": run_rows,
        })

    result = {
        "status": "ok",
        "manifest_dir": str(manifest_dir),
        "include": args.include,
        "count": len(manifests),
        "manifests": manifests,
    }
    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(result, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
