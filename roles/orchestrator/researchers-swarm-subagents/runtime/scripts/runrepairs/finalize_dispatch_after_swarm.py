#!/usr/bin/env python3
"""Standard finalization step after a swarm run.

This wrapper runs the artifact-vs-DB reconciler for a dispatch manifest and then
returns a compact post-finalization status summary for the referenced runs.

Use it after the swarm appears finished to clean up stale queued/running rows
whose artifacts were written but whose completion helper did not run, and to
recover helper-termination failures when written artifacts can be reconciled.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR.parent
RECONCILE_FROM_ARTIFACTS = BASE_DIR / "reconcile_dispatch_from_artifacts.py"
LOAD_EXISTING = SCRIPTS_DIR / "internal" / "load_dispatch_existing_state.py"
KICKOFF_SYNTHESIS = SCRIPTS_DIR.parents[2] / "synthesis-subagent" / "runtime" / "scripts" / "kickoff_synthesis_after_swarm.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Finalize a dispatch after swarm completion")
    parser.add_argument("--file", required=True, help="Dispatch manifest JSON path")
    parser.add_argument("--apply", action="store_true", help="Apply artifact reconciliation (default is dry-run summary only)")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def python_json(script: Path, args: list[str]) -> dict:
    proc = subprocess.run([sys.executable, str(script), *args], text=True, capture_output=True)
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
    try:
        reconcile_args = ["--file", str(manifest_path)]
        if args.apply:
            reconcile_args.append("--apply")
        reconcile_result = python_json(RECONCILE_FROM_ARTIFACTS, reconcile_args)
        state_map = python_json(LOAD_EXISTING, ["--file", str(manifest_path)])

        counts = {"queued": 0, "running": 0, "completed": 0, "failed": 0}
        for state in state_map.values():
            status = state.get("status")
            if status in counts:
                counts[status] += 1

        all_terminal = counts["queued"] == 0 and counts["running"] == 0
        all_completed = all_terminal and counts["failed"] == 0 and counts["completed"] > 0
        kickoff_result = None
        kickoff_error = None
        dispatch_id = manifest_path.stem
        if args.apply and all_completed and KICKOFF_SYNTHESIS.exists():
            try:
                kickoff_result = python_json(
                    KICKOFF_SYNTHESIS,
                    ["--dispatch-id", dispatch_id, "--launch-extractors"],
                )
            except Exception as exc:  # noqa: BLE001
                kickoff_error = str(exc)

        result = {
            "status": "applied" if args.apply else "dry_run",
            "manifest_path": str(manifest_path),
            "dispatch_id": dispatch_id,
            "reconcile": reconcile_result,
            "post_finalize_counts": counts,
            "all_terminal": all_terminal,
            "all_completed": all_completed,
            "synthesis_kickoff": kickoff_result,
            "synthesis_kickoff_error": kickoff_error,
        }
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
