#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR.parent
RECONCILE = BASE_DIR / "reconcile_synthesis_from_artifacts.py"
LAUNCH_SYNTHESIS = SCRIPTS_DIR / "launch_synthesis_if_ready.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Finalize synthesis stage after extraction/final-artifact reconciliation")
    parser.add_argument("--status-file", required=True, help="synthesis-stage-status.json path")
    parser.add_argument("--apply", action="store_true", help="Apply reconciliation and advance synthesis when ready")
    parser.add_argument("--pretty", action="store_true")
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
    status_path = Path(args.status_file).expanduser().resolve()
    try:
        reconcile_args = ["--status-file", str(status_path)]
        if args.apply:
            reconcile_args.append("--apply")
        reconcile_result = python_json(RECONCILE, reconcile_args)

        launch_result = None
        launch_error = None
        inferred_status = reconcile_result.get("inferred_status")
        if args.apply and inferred_status == "ready_for_final_synthesis":
            try:
                launch_result = python_json(
                    LAUNCH_SYNTHESIS,
                    ["--status-file", str(status_path)],
                )
            except Exception as exc:  # noqa: BLE001
                launch_error = str(exc)

        out = {
            "status": "applied" if args.apply else "dry_run",
            "status_file": str(status_path),
            "reconcile": reconcile_result,
            "launch_result": launch_result,
            "launch_error": launch_error,
        }
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(out, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(out, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
