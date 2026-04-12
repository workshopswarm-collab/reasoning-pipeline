#!/usr/bin/env python3
"""Reconcile dispatch runs against their assigned primary artifact paths.

Purpose:
- detect stale DB state where a run's assigned agent-finding file exists but the
  corresponding `research_runs` row is still `queued` or `running`
- detect helper-termination failures where artifacts were written but the lane
  was marked `failed` before terminal reconciliation finished
- optionally mark those runs `completed`

This is a safety net for the current Telegram topic-session model when a lane
produces artifacts but fails to complete the DB completion helper path cleanly.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR.parent
LOAD_EXISTING = SCRIPTS_DIR / "internal" / "load_dispatch_existing_state.py"
RECONCILE_COMPLETION = SCRIPTS_DIR / "reconcile_research_run_completion.py"
WORKSPACE_ROOT = BASE_DIR.parents[5]
if str(WORKSPACE_ROOT / 'scripts') not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT / 'scripts'))

from automation_runtime_support import DEFAULT_SUBPROCESS_TIMEOUT_SECONDS, exclusive_lock, load_json_dict, run_json_subprocess  # noqa: E402

HELPER_TERMINATED_AFTER_WRITE_ERROR = "completion helper terminated before finishing after artifacts were written"
REPAIR_LOCK_BYPASS_ENV = 'OPENCLAW_REPAIR_LOCK_HELD'
LOCK_DIR = WORKSPACE_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / '.runtime-state' / 'runrepairs'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reconcile dispatch runs from artifact existence")
    parser.add_argument("--file", "--manifest", dest="manifest", required=True, help="Dispatch manifest JSON path")
    parser.add_argument("--apply", action="store_true", help="Actually mark stale runs completed")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def python_json(script: Path, args: list[str], stdin_payload=None, *, env: dict[str, str] | None = None):
    proc, payload = run_json_subprocess(
        [sys.executable, str(script), *args],
        input_text=(json.dumps(stdin_payload) if stdin_payload is not None else None),
        env=env,
        timeout_seconds=DEFAULT_SUBPROCESS_TIMEOUT_SECONDS,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"{script.name} failed")
    return payload


def dispatch_lock_path(manifest_path: Path) -> Path:
    return LOCK_DIR / f'{manifest_path.stem}.lock'


def validate_manifest_payload(manifest_path: Path) -> dict:
    manifest = load_json_dict(manifest_path, artifact_name='dispatch manifest', required_keys=['runs'])
    runs = manifest.get('runs')
    if not isinstance(runs, list):
        raise RuntimeError(f'dispatch manifest runs must be a list: {manifest_path}')
    for idx, run in enumerate(runs):
        if not isinstance(run, dict):
            raise RuntimeError(f'dispatch manifest run #{idx} must be an object: {manifest_path}')
        if not str(run.get('research_run_id') or '').strip():
            raise RuntimeError(f'dispatch manifest run #{idx} is missing research_run_id: {manifest_path}')
    return manifest


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest).expanduser().resolve()
    with exclusive_lock(
        dispatch_lock_path(manifest_path),
        bypass_env_var=REPAIR_LOCK_BYPASS_ENV,
        error_message=f'another dispatch repair already holds {manifest_path}',
    ):
        env = dict(os.environ)
        env[REPAIR_LOCK_BYPASS_ENV] = '1'
        manifest = validate_manifest_payload(manifest_path)
        existing_map = python_json(LOAD_EXISTING, ["--file", str(manifest_path)], env=env)

        stale = []
        reconciled = []
        for run in manifest.get("runs", []):
            run_id = run["research_run_id"]
            state = existing_map.get(run_id) or {}
            status = state.get("status")
            notes = state.get("notes") or {}
            helper_error = notes.get("error")
            artifact_rel = run.get("workspace_note_path")
            artifact_abs = WORKSPACE_ROOT / artifact_rel if artifact_rel else None
            artifact_exists = bool(artifact_abs and artifact_abs.exists())
            completion_summary = None
            recovery_reason = None
            if artifact_exists and status in {"queued", "running"}:
                completion_summary = "Primary artifact exists at the assigned path; reconciling stale DB state from artifact presence."
                recovery_reason = "stale_nonterminal_state"
            elif artifact_exists and status == "failed" and helper_error == HELPER_TERMINATED_AFTER_WRITE_ERROR:
                completion_summary = (
                    "Primary artifact exists at the assigned path and the failed status records a completion-helper termination after artifacts were written; "
                    "reconciling helper-termination failure from artifact presence."
                )
                recovery_reason = "helper_terminated_after_write"

            if completion_summary is not None:
                entry = {
                    "research_run_id": run_id,
                    "persona": run.get("persona"),
                    "status": status,
                    "workspace_note_path": artifact_rel,
                    "artifact_exists": True,
                    "recovery_reason": recovery_reason,
                }
                stale.append(entry)
                if args.apply:
                    result = python_json(
                        RECONCILE_COMPLETION,
                        [
                            "--research-run-id", run_id,
                            "--status", "completed",
                            "--completion-summary",
                            completion_summary,
                        ],
                        env=env,
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
