#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR.parent
WORKSPACE_ROOT = BASE_DIR.parents[5]
if str(WORKSPACE_ROOT / 'scripts') not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT / 'scripts'))

from automation_runtime_support import DEFAULT_SUBPROCESS_TIMEOUT_SECONDS, exclusive_lock, load_json_dict, run_json_subprocess  # noqa: E402

RECONCILE = BASE_DIR / "reconcile_synthesis_from_artifacts.py"
LAUNCH_SYNTHESIS = SCRIPTS_DIR / "launch_synthesis_if_ready.py"
REPAIR_LOCK_BYPASS_ENV = 'OPENCLAW_REPAIR_LOCK_HELD'
LOCK_DIR = WORKSPACE_ROOT / 'roles' / 'orchestrator' / 'synthesis-subagent' / 'runtime' / '.runtime-state' / 'runrepairs'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Finalize synthesis stage after extraction/final-artifact reconciliation")
    parser.add_argument("--status-file", required=True, help="synthesis-stage-status.json path")
    parser.add_argument("--apply", action="store_true", help="Apply reconciliation and advance synthesis when ready")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def python_json(script: Path, args: list[str], *, env: dict[str, str] | None = None) -> dict:
    proc, payload = run_json_subprocess(
        [sys.executable, str(script), *args],
        env=env,
        timeout_seconds=DEFAULT_SUBPROCESS_TIMEOUT_SECONDS,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"{script.name} failed")
    return payload


def status_lock_path(status_path: Path) -> Path:
    return LOCK_DIR / f'{status_path.parent.name}.lock'


def validate_status_payload(status_path: Path) -> dict:
    return load_json_dict(status_path, artifact_name='synthesis status file', required_keys=['bundle_path'])


def main() -> int:
    args = parse_args()
    status_path = Path(args.status_file).expanduser().resolve()
    try:
        with exclusive_lock(
            status_lock_path(status_path),
            bypass_env_var=REPAIR_LOCK_BYPASS_ENV,
            error_message=f'another synthesis finalizer already holds {status_path}',
        ):
            env = dict(os.environ)
            env[REPAIR_LOCK_BYPASS_ENV] = '1'
            validate_status_payload(status_path)
            reconcile_args = ["--status-file", str(status_path)]
            if args.apply:
                reconcile_args.append("--apply")
            reconcile_result = python_json(RECONCILE, reconcile_args, env=env)

            launch_result = None
            launch_error = None
            inferred_status = reconcile_result.get("inferred_status")
            if args.apply and inferred_status == "ready_for_final_synthesis":
                try:
                    launch_result = python_json(
                        LAUNCH_SYNTHESIS,
                        ["--status-file", str(status_path)],
                        env=env,
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
