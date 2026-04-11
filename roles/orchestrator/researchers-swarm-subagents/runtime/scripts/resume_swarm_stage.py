#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[4]
RECONCILE = SCRIPT_DIR / 'reconcile_swarm_stage.py'
LAUNCH_SWARM = SCRIPT_DIR / 'launch_dispatch_with_stateful_posts.py'
LAUNCH_SYNTHESIS = REPO_ROOT / 'roles' / 'orchestrator' / 'synthesis-subagent' / 'runtime' / 'scripts' / 'launch_synthesis_if_ready.py'
if str(REPO_ROOT / 'scripts') not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / 'scripts'))

from case_pipeline_status import update_case_pipeline_status  # noqa: E402


class ResumeError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Resume a partially completed swarm stage in the same dispatch when possible')
    parser.add_argument('--case-key')
    parser.add_argument('--dispatch-dir')
    parser.add_argument('--stale-seconds', type=float, default=900.0)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def run_json(cmd: list[str]) -> tuple[int, dict[str, Any], str, str]:
    proc = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True)
    payload: dict[str, Any] = {}
    text = (proc.stdout or '').strip()
    if text:
        try:
            parsed = json.loads(text)
            if isinstance(parsed, dict):
                payload = parsed
        except json.JSONDecodeError:
            payload = {}
    return proc.returncode, payload, proc.stdout, proc.stderr


def repo_path(path_text: str) -> Path:
    candidate = Path(path_text)
    if candidate.is_absolute():
        return candidate
    return REPO_ROOT / candidate


def main() -> None:
    args = parse_args()
    if not args.case_key and not args.dispatch_dir:
        raise SystemExit('one of --case-key or --dispatch-dir is required')

    reconcile_cmd = [sys.executable, str(RECONCILE), '--stale-seconds', str(args.stale_seconds)]
    if args.case_key:
        reconcile_cmd.extend(['--case-key', args.case_key])
    if args.dispatch_dir:
        reconcile_cmd.extend(['--dispatch-dir', args.dispatch_dir])
    if args.pretty:
        reconcile_cmd.append('--pretty')
    _, swarm_status, _, _ = run_json(reconcile_cmd)
    if not swarm_status:
        raise ResumeError('failed to reconcile swarm stage')

    case_key = str(swarm_status.get('case_key') or '').strip()
    dispatch_id = str(swarm_status.get('dispatch_id') or '').strip()
    status = str(swarm_status.get('status') or '').strip()
    manifest_path = str(swarm_status.get('manifest_path') or '').strip()
    synthesis_status_path = str(swarm_status.get('synthesis_status_path') or '').strip()

    result: dict[str, Any] = {
        'ok': True,
        'case_key': case_key,
        'dispatch_id': dispatch_id,
        'swarm_status': swarm_status,
        'action': 'none',
    }

    if status == 'completed':
        result['action'] = 'none_needed'
    elif status == 'ready_for_synthesis':
        if not synthesis_status_path:
            raise ResumeError('swarm is ready for synthesis but no synthesis_status_path is available')
        cmd = [sys.executable, str(LAUNCH_SYNTHESIS), '--status-file', str(repo_path(synthesis_status_path))]
        if args.pretty:
            cmd.append('--pretty')
        code, payload, stdout, stderr = run_json(cmd)
        result.update({'action': 'launch_synthesis_if_ready', 'launch_result': payload, 'stdout': stdout, 'stderr': stderr, 'returncode': code})
    elif status == 'stale':
        if not manifest_path:
            raise ResumeError('swarm is stale but no manifest_path is available for same-dispatch resume')
        cmd = [sys.executable, str(LAUNCH_SWARM), '--manifest-path', str(repo_path(manifest_path))]
        if args.pretty:
            cmd.append('--pretty')
        code, payload, stdout, stderr = run_json(cmd)
        result.update({'action': 'relaunch_swarm_same_dispatch', 'launch_result': payload, 'stdout': stdout, 'stderr': stderr, 'returncode': code})
    else:
        result['action'] = 'wait_current_swarm'

    if case_key:
        update_case_pipeline_status(
            case_key=case_key,
            dispatch_id=dispatch_id,
            status='pipeline_in_progress',
            current_stage='swarm' if status in {'in_progress', 'stale'} else 'synthesis',
            runner_id='resume_swarm_stage',
            message=f"Swarm resume helper action: {result['action']}",
        )

    print(json.dumps(result, indent=2 if args.pretty else None))


if __name__ == '__main__':
    main()
