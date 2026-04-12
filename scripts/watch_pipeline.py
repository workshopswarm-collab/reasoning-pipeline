#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fcntl
import json
import os
import subprocess
import sys
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / 'scripts') not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / 'scripts'))

from automation_control import DEFAULT_CONTROL_FILE, load_control_file, resolve_watchdog_policy  # noqa: E402
from case_pipeline_status import list_case_pipeline_statuses, summarize_case_pipeline_status, update_case_pipeline_status  # noqa: E402

RECONCILE_SWARM_STAGE = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / 'scripts' / 'reconcile_swarm_stage.py'
RESUME_SWARM_STAGE = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / 'scripts' / 'resume_swarm_stage.py'
LAUNCH_SYNTHESIS_IF_READY = REPO_ROOT / 'roles' / 'orchestrator' / 'synthesis-subagent' / 'runtime' / 'scripts' / 'launch_synthesis_if_ready.py'
RECONCILE_DECISION_STAGE = REPO_ROOT / 'roles' / 'decision-maker' / 'runtime' / 'scripts' / 'reconcile_decision_stage.py'
FINALIZE_DECISION_STAGE = REPO_ROOT / 'roles' / 'decision-maker' / 'runtime' / 'scripts' / 'finalize_decision_stage.py'
RUN_DECISION_MAKER = REPO_ROOT / 'roles' / 'decision-maker' / 'runtime' / 'scripts' / 'run_decision_maker.py'
DEFAULT_LOCK = REPO_ROOT / 'scripts' / '.runtime-state' / 'pipeline-watchdog.lock'


class WatchdogError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Watch active pipeline cases and conservatively reconcile existing in-flight work')
    parser.add_argument('--poll-seconds', type=float, default=60.0, help='Sleep interval between passes when looping')
    parser.add_argument('--stale-seconds', type=float, default=900.0, help='Staleness threshold forwarded to swarm reconciliation')
    parser.add_argument('--loop', action='store_true', help='Run continuously instead of a single pass')
    parser.add_argument('--apply', action='store_true', help='Allow bounded repair actions on existing in-flight cases')
    parser.add_argument('--allow-resume-swarm', action='store_true', help='When --apply is set, allow same-dispatch swarm recovery')
    parser.add_argument('--allow-launch-synthesis', action='store_true', help='When --apply is set, allow synthesis launch for already-open cases')
    parser.add_argument('--allow-launch-decision', action='store_true', help='When --apply is set, allow Decision-Maker launch for already-open cases')
    parser.add_argument('--allow-finalize-decision', action='store_true', help='When --apply is set, allow decision-stage status finalization from already-valid artifacts')
    parser.add_argument('--allow-finalize-pipeline', action='store_true', help='When --apply is set, allow pipeline-status finalization from already-ready decision artifacts')
    parser.add_argument('--case-key', action='append', default=[], help='Limit monitoring to one or more specific case keys')
    parser.add_argument('--control-managed', action='store_true', help='Load repair/apply policy from the persisted automation control file each pass')
    parser.add_argument('--control-file', default=str(DEFAULT_CONTROL_FILE), help='Automation control file path used with --control-managed')
    parser.add_argument('--lock-file', default=str(DEFAULT_LOCK), help='Process lock to prevent concurrent watchdog loops')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def load_repo_env() -> dict[str, str]:
    env = dict(os.environ)
    for env_name in ['.env', '.env.postgres.local']:
        env_file = REPO_ROOT / env_name
        if not env_file.exists():
            continue
        for raw_line in env_file.read_text().splitlines():
            line = raw_line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            if line.startswith('export '):
                line = line[len('export '):].strip()
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in env:
                env[key] = value
    return env


@contextmanager
def process_lock(path: Path) -> Iterator[None]:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+', encoding='utf-8') as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:  # noqa: PERF203
            raise WatchdogError(f'another watchdog instance already holds {path}') from exc
        try:
            handle.seek(0)
            handle.truncate()
            handle.write(str(os.getpid()))
            handle.flush()
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def run_json_command(cmd: list[str]) -> tuple[int, dict[str, Any], str, str]:
    proc = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True, env=load_repo_env())
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


def load_json_if_exists(path: Path | None) -> dict[str, Any]:
    if path is None or not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def finalize_pipeline(case_key: str, *, decision_payload: dict[str, Any], summary: dict[str, Any]) -> dict[str, Any]:
    outputs = decision_payload.get('outputs') or {}
    packet_path_text = str(outputs.get('packet_json_path') or '').strip()
    packet_payload = load_json_if_exists(REPO_ROOT / packet_path_text) if packet_path_text else {}
    decision_block = packet_payload.get('decision') or {}
    updated = update_case_pipeline_status(
        case_key=case_key,
        dispatch_id=str(summary.get('dispatch_id') or '').strip(),
        market_id=str(summary.get('market_id') or '').strip(),
        market_title=str(summary.get('market_title') or '').strip(),
        status='pipeline_completed',
        current_stage='decision',
        stage_status_patch={
            'swarm': 'completed',
            'synthesis': 'completed',
            'decision': 'completed',
        },
        runner_id='watch_pipeline',
        message='Watchdog finalized pipeline from ready decision artifacts',
        terminal_summary_patch={
            'decision_packet_json': packet_path_text or None,
            'decision_packet_markdown': str(outputs.get('packet_markdown_path') or '').strip() or None,
            'decision_readiness': str(decision_block.get('decision_readiness') or '').strip() or None,
            'recommended_side': str(decision_block.get('side') or '').strip() or None,
            'trade_authorization': str(decision_block.get('trade_authorization') or '').strip() or None,
            'position_policy': str(decision_block.get('position_policy') or '').strip() or None,
        },
    )
    return {'ok': True, 'payload': updated}


def latest_dispatch_dir(case_key: str) -> Path | None:
    analyses_root = REPO_ROOT / 'qualitative-db' / '40-research' / 'cases' / case_key / 'researcher-analyses'
    if not analyses_root.exists():
        return None
    candidates = sorted(analyses_root.glob('*/dispatch-case-*'), key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0] if candidates else None


def synthesis_status_file(case_key: str) -> Path | None:
    dispatch_dir = latest_dispatch_dir(case_key)
    if dispatch_dir is None:
        return None
    path = dispatch_dir / 'synthesis-stage-status.json'
    return path if path.exists() else None


def reconcile_swarm(case_key: str, *, stale_seconds: float, check_only: bool, pretty: bool) -> dict[str, Any]:
    cmd = [sys.executable, str(RECONCILE_SWARM_STAGE), '--case-key', case_key, '--stale-seconds', str(stale_seconds)]
    if check_only:
        cmd.append('--check-only')
    if pretty:
        cmd.append('--pretty')
    code, payload, stdout, stderr = run_json_command(cmd)
    return {'ok': code == 0, 'payload': payload, 'stdout': stdout, 'stderr': stderr, 'returncode': code}


def resume_swarm(case_key: str, *, pretty: bool) -> dict[str, Any]:
    cmd = [sys.executable, str(RESUME_SWARM_STAGE), '--case-key', case_key]
    if pretty:
        cmd.append('--pretty')
    code, payload, stdout, stderr = run_json_command(cmd)
    return {'ok': code == 0, 'payload': payload, 'stdout': stdout, 'stderr': stderr, 'returncode': code}


def launch_synthesis_if_needed(case_key: str, *, pretty: bool) -> dict[str, Any] | None:
    status_file = synthesis_status_file(case_key)
    if status_file is None:
        return None
    cmd = [sys.executable, str(LAUNCH_SYNTHESIS_IF_READY), '--status-file', str(status_file)]
    if pretty:
        cmd.append('--pretty')
    code, payload, stdout, stderr = run_json_command(cmd)
    return {'ok': code == 0, 'payload': payload, 'stdout': stdout, 'stderr': stderr, 'returncode': code}


def reconcile_decision(case_key: str, *, pretty: bool) -> dict[str, Any]:
    cmd = [sys.executable, str(RECONCILE_DECISION_STAGE), '--case-key', case_key]
    if pretty:
        cmd.append('--pretty')
    code, payload, stdout, stderr = run_json_command(cmd)
    return {'ok': code == 0, 'payload': payload, 'stdout': stdout, 'stderr': stderr, 'returncode': code}


def finalize_decision(case_key: str, *, pretty: bool) -> dict[str, Any]:
    cmd = [sys.executable, str(FINALIZE_DECISION_STAGE), '--case-key', case_key, '--apply']
    if pretty:
        cmd.append('--pretty')
    code, payload, stdout, stderr = run_json_command(cmd)
    return {'ok': code == 0, 'payload': payload, 'stdout': stdout, 'stderr': stderr, 'returncode': code}


def launch_decision(case_key: str, *, pretty: bool) -> dict[str, Any]:
    cmd = [sys.executable, str(RUN_DECISION_MAKER), '--case-key', case_key]
    if pretty:
        cmd.append('--pretty')
    code, payload, stdout, stderr = run_json_command(cmd)
    return {'ok': code == 0, 'payload': payload, 'stdout': stdout, 'stderr': stderr, 'returncode': code}


def effective_watchdog_policy(args: argparse.Namespace) -> dict[str, Any]:
    policy = {
        'enabled': True,
        'apply': bool(args.apply),
        'allow_resume_swarm': bool(args.apply and args.allow_resume_swarm),
        'allow_launch_synthesis': bool(args.apply and args.allow_launch_synthesis),
        'allow_launch_decision': bool(args.apply and args.allow_launch_decision),
        'allow_finalize_decision': bool(args.apply and args.allow_finalize_decision),
        'allow_finalize_pipeline': bool(args.apply and args.allow_finalize_pipeline),
        'control_managed': bool(args.control_managed),
        'control_file': str(Path(args.control_file).expanduser().resolve()),
    }
    if args.control_managed:
        control = load_control_file(Path(args.control_file).expanduser().resolve())
        control_policy = resolve_watchdog_policy(control)
        policy.update({
            'enabled': bool(control_policy.get('enabled')),
            'apply': bool(control_policy.get('apply')) or policy['apply'],
            'allow_resume_swarm': bool(control_policy.get('allow_resume_swarm')) or policy['allow_resume_swarm'],
            'allow_launch_synthesis': bool(control_policy.get('allow_launch_synthesis')) or policy['allow_launch_synthesis'],
            'allow_launch_decision': bool(control_policy.get('allow_launch_decision')) or policy['allow_launch_decision'],
            'allow_finalize_decision': bool(control_policy.get('allow_finalize_decision')) or policy['allow_finalize_decision'],
            'allow_finalize_pipeline': bool(control_policy.get('allow_finalize_pipeline')) or policy['allow_finalize_pipeline'],
            'control_snapshot': control,
        })
    return policy


def selected_cases(case_filters: list[str]) -> list[dict[str, Any]]:
    summaries = list_case_pipeline_statuses(include_terminal=False)
    if not case_filters:
        return summaries
    allow = set(case_filters)
    return [summary for summary in summaries if str(summary.get('case_key') or '') in allow]


def watch_case(summary: dict[str, Any], *, args: argparse.Namespace, policy: dict[str, Any]) -> dict[str, Any]:
    case_key = str(summary.get('case_key') or '').strip()
    if not case_key:
        return {'ok': False, 'error': 'missing_case_key', 'case_summary': summary}

    stage_statuses = summary.get('stage_statuses') or {}
    case_result: dict[str, Any] = {
        'case_key': case_key,
        'before': summary,
        'proposed_actions': [],
        'executed_actions': [],
    }

    swarm_result = reconcile_swarm(case_key, stale_seconds=args.stale_seconds, check_only=not policy['apply'], pretty=args.pretty)
    case_result['swarm_reconcile'] = swarm_result
    swarm_payload = swarm_result.get('payload') or {}
    swarm_status = str(swarm_payload.get('status') or '').strip()
    if swarm_status == 'stale':
        case_result['proposed_actions'].append('resume_swarm_same_dispatch')
        if policy['apply'] and policy['allow_resume_swarm']:
            action = resume_swarm(case_key, pretty=args.pretty)
            case_result['executed_actions'].append({'name': 'resume_swarm_same_dispatch', 'result': action})
    elif swarm_status == 'ready_for_synthesis':
        case_result['proposed_actions'].append('launch_synthesis_for_existing_case')
        if policy['apply'] and policy['allow_launch_synthesis']:
            action = resume_swarm(case_key, pretty=args.pretty)
            case_result['executed_actions'].append({'name': 'launch_synthesis_for_existing_case', 'result': action})

    summary_after_swarm = summarize_case_pipeline_status(case_key)
    stage_statuses = summary_after_swarm.get('stage_statuses') or stage_statuses
    synthesis_completed = stage_statuses.get('synthesis') == 'completed' or str(swarm_payload.get('synthesis_status') or '').strip() == 'synthesis_completed'
    decision_pending = stage_statuses.get('decision') in {'pending', ''}

    if not synthesis_completed and decision_pending:
        status_file = synthesis_status_file(case_key)
        if status_file is not None:
            case_result['proposed_actions'].append('check_synthesis_launch_gate')
            if policy['apply'] and policy['allow_launch_synthesis']:
                action = launch_synthesis_if_needed(case_key, pretty=args.pretty)
                case_result['executed_actions'].append({'name': 'check_synthesis_launch_gate', 'result': action})
                summary_after_swarm = summarize_case_pipeline_status(case_key)
                stage_statuses = summary_after_swarm.get('stage_statuses') or stage_statuses
                synthesis_completed = stage_statuses.get('synthesis') == 'completed'
                decision_pending = stage_statuses.get('decision') in {'pending', ''}

    if synthesis_completed or stage_statuses.get('decision') in {'pending', 'in_progress', 'failed'}:
        decision_result = reconcile_decision(case_key, pretty=args.pretty)
        case_result['decision_reconcile'] = decision_result
        decision_payload = decision_result.get('payload') or {}
        decision_health = str(decision_payload.get('health') or '').strip()
        if decision_health == 'ready' and summary_after_swarm.get('status') != 'pipeline_completed':
            case_result['proposed_actions'].append('finalize_pipeline_from_ready_decision')
            if policy['apply'] and policy['allow_finalize_pipeline']:
                action = finalize_pipeline(case_key, decision_payload=decision_payload, summary=summary_after_swarm)
                case_result['executed_actions'].append({'name': 'finalize_pipeline_from_ready_decision', 'result': action})
        if decision_health == 'stale_status':
            case_result['proposed_actions'].append('finalize_decision_status_from_existing_packet')
            if policy['apply'] and policy['allow_finalize_decision']:
                action = finalize_decision(case_key, pretty=args.pretty)
                case_result['executed_actions'].append({'name': 'finalize_decision_status_from_existing_packet', 'result': action})
        elif decision_health == 'not_started' and decision_pending:
            case_result['proposed_actions'].append('launch_decision_for_existing_case')
            if policy['apply'] and policy['allow_launch_decision']:
                action = launch_decision(case_key, pretty=args.pretty)
                case_result['executed_actions'].append({'name': 'launch_decision_for_existing_case', 'result': action})

    case_result['after'] = summarize_case_pipeline_status(case_key)
    case_result['ok'] = True
    return case_result


def watchdog_pass(args: argparse.Namespace) -> dict[str, Any]:
    policy = effective_watchdog_policy(args)
    if not policy.get('enabled', True):
        return {
            'ok': True,
            'mode': {**policy, 'claims_new_cases': False},
            'active_case_count': 0,
            'results': [],
            'status': 'watchdog_disabled_by_control',
        }
    cases = selected_cases(args.case_key)
    results = [watch_case(summary, args=args, policy=policy) for summary in cases]
    return {
        'ok': all(result.get('ok', False) for result in results),
        'mode': {**policy, 'claims_new_cases': False},
        'active_case_count': len(cases),
        'results': results,
    }


def main() -> None:
    args = parse_args()
    lock_path = Path(args.lock_file).expanduser().resolve()
    with process_lock(lock_path):
        if not args.loop:
            summary = watchdog_pass(args)
            print(json.dumps(summary, indent=2 if args.pretty else None))
            if not summary.get('ok'):
                raise SystemExit(1)
            return

        while True:
            summary = watchdog_pass(args)
            print(json.dumps(summary, indent=2 if args.pretty else None), flush=True)
            time.sleep(args.poll_seconds)


if __name__ == '__main__':
    main()
