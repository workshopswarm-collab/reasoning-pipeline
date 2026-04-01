#!/usr/bin/env python3
"""Reconcile dispatch runs against their assigned primary artifact paths.

Purpose:
- detect stale DB state where a run's assigned agent-finding file exists but the
  corresponding `research_runs` row is still `queued` or `running`
- optionally mark those runs `completed`

This is a safety net for the current Telegram topic-session model when a lane
produces artifacts but fails to call the DB completion helper.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR.parent
LOAD_EXISTING = SCRIPTS_DIR / "internal" / "load_dispatch_existing_state.py"
RECONCILE_COMPLETION = SCRIPTS_DIR / "reconcile_research_run_completion.py"
WORKSPACE_ROOT = BASE_DIR.parents[5]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reconcile dispatch runs from artifact existence")
    parser.add_argument("--file", required=True, help="Dispatch manifest JSON path")
    parser.add_argument("--apply", action="store_true", help="Actually mark stale runs completed")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def python_json(script: Path, args: list[str], stdin_payload=None):
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
        return {}
    for line in reversed([line for line in stdout.splitlines() if line.strip()]):
        try:
            return json.loads(line)
        except json.JSONDecodeError:
            continue
    return json.loads(stdout)


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.file).expanduser().resolve()
    manifest = json.loads(manifest_path.read_text())
    existing_map = python_json(LOAD_EXISTING, ["--file", str(manifest_path)])

    stale = []
    reconciled = []
    for run in manifest.get("runs", []):
        run_id = run["research_run_id"]
        state = existing_map.get(run_id) or {}
        status = state.get("status")
        artifact_rel = run.get("workspace_note_path")
        artifact_abs = WORKSPACE_ROOT / artifact_rel if artifact_rel else None
        artifact_exists = bool(artifact_abs and artifact_abs.exists())
        if artifact_exists and status in {"queued", "running"}:
            entry = {
                "research_run_id": run_id,
                "persona": run.get("persona"),
                "status": status,
                "workspace_note_path": artifact_rel,
                "artifact_exists": True,
            }
            stale.append(entry)
            if args.apply:
                result = python_json(
                    RECONCILE_COMPLETION,
                    [
                        "--research-run-id", run_id,
                        "--status", "completed",
                        "--completion-summary",
                        "Primary artifact exists at the assigned path; reconciling stale DB state from artifact presence.",
                    ],
                )
                reconciled.append({**entry, "result": result})

    out = {
        "status": "applied" if args.apply else "dry_run",
        "manifest_path": str(manifest_path),
        "stale_count": len(stale),
        "stale": stale,
        "reconciled": reconciled,
    }
    if args.pretty:
        print(json.dumps(out, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(out, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
