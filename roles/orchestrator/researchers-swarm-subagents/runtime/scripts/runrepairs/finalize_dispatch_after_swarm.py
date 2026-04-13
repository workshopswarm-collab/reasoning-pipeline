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
import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR.parent
WORKSPACE_ROOT = BASE_DIR.parents[5]
if str(WORKSPACE_ROOT / 'scripts') not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT / 'scripts'))

from automation_runtime_support import DEFAULT_SUBPROCESS_TIMEOUT_SECONDS, exclusive_lock, load_json_dict, run_json_subprocess  # noqa: E402

RESEARCH_CASES_ROOT = WORKSPACE_ROOT / "qualitative-db" / "40-research" / "cases"
RECONCILE_FROM_ARTIFACTS = BASE_DIR / "reconcile_dispatch_from_artifacts.py"
LOAD_EXISTING = SCRIPTS_DIR / "internal" / "load_dispatch_existing_state.py"
KICKOFF_SYNTHESIS = SCRIPTS_DIR.parents[2] / "synthesis-subagent" / "runtime" / "scripts" / "kickoff_synthesis_after_swarm.py"
LAUNCH_SYNTHESIS_IF_READY = SCRIPTS_DIR.parents[2] / "synthesis-subagent" / "runtime" / "scripts" / "launch_synthesis_if_ready.py"
REPAIR_LOCK_BYPASS_ENV = 'OPENCLAW_REPAIR_LOCK_HELD'
LOCK_DIR = WORKSPACE_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / '.runtime-state' / 'runrepairs'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Finalize a dispatch after swarm completion")
    parser.add_argument("--file", "--manifest", dest="manifest", required=True, help="Dispatch manifest JSON path")
    parser.add_argument("--apply", action="store_true", help="Apply artifact reconciliation (default is dry-run summary only)")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
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


def load_json(path: Path) -> dict:
    return load_json_dict(path, artifact_name='json artifact')


def dispatch_lock_path(manifest_path: Path) -> Path:
    return LOCK_DIR / f'{manifest_path.stem}.lock'


def validate_manifest_payload(manifest_path: Path) -> dict:
    manifest = load_json_dict(manifest_path, artifact_name='dispatch manifest', required_keys=['runs'])
    runs = manifest.get('runs')
    if not isinstance(runs, list):
        raise RuntimeError(f'dispatch manifest runs must be a list: {manifest_path}')
    return manifest


def write_manifest(path: Path, manifest: dict) -> None:
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def send_visible_telegram_message(*, chat_id: str, topic_id: str, message: str) -> dict:
    proc = subprocess.run(
        [
            'openclaw', 'message', 'send',
            '--channel', 'telegram',
            '--target', str(chat_id),
            '--thread-id', str(topic_id),
            '--message', message,
            '--json',
        ],
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or 'telegram visible send failed')
    text = proc.stdout.strip()
    return json.loads(text.splitlines()[-1]) if text else {}


def locate_status_file(*, case_key: str, dispatch_id: str) -> Path | None:
    if not case_key:
        return None
    matches = sorted((RESEARCH_CASES_ROOT / case_key / "researcher-analyses").glob(f"*/{dispatch_id}/synthesis-stage-status.json"))
    return matches[-1] if matches else None


def synthesis_already_terminal(status_path: Path | None) -> bool:
    if status_path is None:
        return False

    if status_path.exists():
        try:
            payload = load_json(status_path)
        except Exception:
            payload = {}
        terminal_summary = payload.get("terminal_summary") or {}
        terminal_status = str(
            terminal_summary.get("status")
            or (payload.get("last_stage_event") or {}).get("state")
            or payload.get("status")
            or ""
        ).strip()
        if terminal_status in {"synthesis_completed", "final_synthesis_completed"}:
            return True
        final_artifact_path = str(terminal_summary.get("final_artifact_path") or "").strip()
        if final_artifact_path and (WORKSPACE_ROOT / final_artifact_path).exists():
            return True

    dispatch_dir = status_path.parent
    artifact_candidates = [
        dispatch_dir / "syndicated-finding.md",
        dispatch_dir / "syndicated-finding.runtime.json",
        dispatch_dir / "decision-handoff.md",
    ]
    return all(path.exists() for path in artifact_candidates)


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest).expanduser().resolve()
    try:
        with exclusive_lock(
            dispatch_lock_path(manifest_path),
            bypass_env_var=REPAIR_LOCK_BYPASS_ENV,
            error_message=f'another dispatch finalizer already holds {manifest_path}',
        ):
            env = dict(os.environ)
            env[REPAIR_LOCK_BYPASS_ENV] = '1'
            reconcile_args = ["--file", str(manifest_path)]
            if args.apply:
                reconcile_args.append("--apply")
            reconcile_result = python_json(RECONCILE_FROM_ARTIFACTS, reconcile_args, env=env)
            state_map = python_json(LOAD_EXISTING, ["--file", str(manifest_path)], env=env)

            counts = {"queued": 0, "running": 0, "completed": 0, "failed": 0, "superseded": 0, "cancelled": 0, "skipped": 0}
            for state in state_map.values():
                status = state.get("status")
                if status in counts:
                    counts[status] += 1

            terminal_count = counts["completed"] + counts["failed"] + counts["superseded"] + counts["cancelled"] + counts["skipped"]
            all_terminal = counts["queued"] == 0 and counts["running"] == 0 and terminal_count == len(state_map)
            all_completed = all_terminal and counts["failed"] == 0 and counts["completed"] > 0
            kickoff_result = None
            kickoff_error = None
            synthesis_launch = None
            synthesis_launch_error = None
            refresh_finish_result = None
            refresh_finish_error = None
            dispatch_id = manifest_path.stem
            manifest = validate_manifest_payload(manifest_path)
            case_key = ((manifest.get("case") or {}).get("case_key") or "").strip()
            existing_status_path = locate_status_file(case_key=case_key, dispatch_id=dispatch_id)
            synthesis_terminal_before_finalize = synthesis_already_terminal(existing_status_path)
            if args.apply and all_completed:
                runtime_defaults = manifest.get('runtime_defaults') if isinstance(manifest.get('runtime_defaults'), dict) else {}
                bootstrap_state = manifest.get('bootstrap_state') if isinstance(manifest.get('bootstrap_state'), dict) else {}
                controller_topic = bootstrap_state.get('controller_topic') if isinstance(bootstrap_state.get('controller_topic'), dict) else {}
                refresh_finish_marker = str(runtime_defaults.get('refresh_finish_marker') or '').strip()
                refresh_finish_sent_at = str((bootstrap_state.get('refresh_finish_marker_sent_at') or '')).strip()
                if refresh_finish_marker and not refresh_finish_sent_at and bootstrap_state.get('chat_id') and controller_topic.get('topic_id'):
                    try:
                        refresh_finish_result = send_visible_telegram_message(
                            chat_id=str(bootstrap_state.get('chat_id')),
                            topic_id=str(controller_topic.get('topic_id')),
                            message=refresh_finish_marker,
                        )
                        bootstrap_state['refresh_finish_marker_sent_at'] = str(refresh_finish_result.get('sentAt') or 'sent')
                        manifest['bootstrap_state'] = bootstrap_state
                        write_manifest(manifest_path, manifest)
                    except Exception as exc:  # noqa: BLE001
                        refresh_finish_error = str(exc)
            if args.apply and all_completed and not synthesis_terminal_before_finalize and KICKOFF_SYNTHESIS.exists():
                try:
                    kickoff_args = ["--dispatch-id", dispatch_id, "--build-full"]
                    if case_key:
                        kickoff_args.extend(["--case-key", case_key])
                    kickoff_result = python_json(KICKOFF_SYNTHESIS, kickoff_args, env=env)
                    status_path = str((kickoff_result or {}).get("status_path") or "").strip()
                    if status_path and LAUNCH_SYNTHESIS_IF_READY.exists():
                        synthesis_launch = python_json(
                            LAUNCH_SYNTHESIS_IF_READY,
                            ["--status-file", status_path],
                            env=env,
                        )
                except Exception as exc:  # noqa: BLE001
                    if kickoff_result is None:
                        kickoff_error = str(exc)
                    else:
                        synthesis_launch_error = str(exc)

            result = {
                "status": "applied" if args.apply else "dry_run",
                "manifest_path": str(manifest_path),
                "dispatch_id": dispatch_id,
                "reconcile": reconcile_result,
                "post_finalize_counts": counts,
                "all_terminal": all_terminal,
                "all_completed": all_completed,
                "existing_status_path": str(existing_status_path) if existing_status_path else None,
                "synthesis_terminal_before_finalize": synthesis_terminal_before_finalize,
                "refresh_finish_result": refresh_finish_result,
                "refresh_finish_error": refresh_finish_error,
                "synthesis_kickoff": kickoff_result,
                "synthesis_kickoff_error": kickoff_error,
                "synthesis_launch": synthesis_launch,
                "synthesis_launch_error": synthesis_launch_error,
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
