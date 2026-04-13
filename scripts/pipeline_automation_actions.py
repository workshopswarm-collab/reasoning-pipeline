from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from automation_runtime_support import AutomationRuntimeError, DEFAULT_SUBPROCESS_TIMEOUT_SECONDS, run_json_subprocess
from case_pipeline_status import locked_json_file, summarize_case_pipeline_status, update_case_pipeline_status_with_followups as update_case_pipeline_status

REPO_ROOT = Path(__file__).resolve().parents[1]

MANUAL_BATCH_CONTROLLER = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / 'scripts' / 'manual_batch_controller.py'
RECONCILE_SWARM_STAGE = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / 'scripts' / 'reconcile_swarm_stage.py'
RESUME_SWARM_STAGE = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / 'scripts' / 'resume_swarm_stage.py'
LAUNCH_SYNTHESIS_IF_READY = REPO_ROOT / 'roles' / 'orchestrator' / 'synthesis-subagent' / 'runtime' / 'scripts' / 'launch_synthesis_if_ready.py'
RECONCILE_DECISION_STAGE = REPO_ROOT / 'roles' / 'decision-maker' / 'runtime' / 'scripts' / 'reconcile_decision_stage.py'
FINALIZE_DECISION_STAGE = REPO_ROOT / 'roles' / 'decision-maker' / 'runtime' / 'scripts' / 'finalize_decision_stage.py'
RUN_DECISION_MAKER = REPO_ROOT / 'roles' / 'decision-maker' / 'runtime' / 'scripts' / 'run_decision_maker.py'
RUN_LIGHT_REFRESH_UPDATE = REPO_ROOT / 'roles' / 'decision-maker' / 'runtime' / 'scripts' / 'run_light_refresh_update.py'
SYNC_MARKET_RESOLUTIONS = REPO_ROOT / 'quant-db' / 'scripts' / 'sync_polymarket_market_resolutions.py'
DECISION_LAUNCH_LOG_DIR = REPO_ROOT / 'scripts' / '.runtime-state' / 'decision-maker-launches'

MANUAL_LAUNCH_TIMEOUT_SECONDS = 600.0


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


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


def run_json_command(cmd: list[str], *, timeout_seconds: float = DEFAULT_SUBPROCESS_TIMEOUT_SECONDS) -> tuple[int, dict[str, Any], str, str]:
    proc, payload = run_json_subprocess(
        cmd,
        cwd=REPO_ROOT,
        env=load_repo_env(),
        timeout_seconds=timeout_seconds,
    )
    return proc.returncode, payload, proc.stdout, proc.stderr


def run_python_script(script_path: Path, *script_args: str, pretty: bool = False, timeout_seconds: float = DEFAULT_SUBPROCESS_TIMEOUT_SECONDS) -> dict[str, Any]:
    cmd = [sys.executable, str(script_path), *script_args]
    if pretty:
        cmd.append('--pretty')
    try:
        code, payload, stdout, stderr = run_json_command(cmd, timeout_seconds=timeout_seconds)
        return {
            'ok': code == 0,
            'payload': payload,
            'stdout': stdout,
            'stderr': stderr,
            'returncode': code,
        }
    except AutomationRuntimeError as exc:
        return {
            'ok': False,
            'payload': {'status': 'timeout'},
            'stdout': '',
            'stderr': str(exc),
            'returncode': None,
            'error_type': 'timeout',
        }


def load_json_if_exists(path: Path | None) -> dict[str, Any]:
    if path is None or not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


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
    args = ['--case-key', case_key, '--stale-seconds', str(stale_seconds)]
    if check_only:
        args.append('--check-only')
    return run_python_script(RECONCILE_SWARM_STAGE, *args, pretty=pretty)


def resume_swarm(case_key: str, *, pretty: bool) -> dict[str, Any]:
    return run_python_script(RESUME_SWARM_STAGE, '--case-key', case_key, pretty=pretty)


def launch_synthesis_if_needed(case_key: str, *, pretty: bool) -> dict[str, Any] | None:
    status_file = synthesis_status_file(case_key)
    if status_file is None:
        return None
    result = run_python_script(LAUNCH_SYNTHESIS_IF_READY, '--status-file', str(status_file), pretty=pretty)
    result['status_file'] = str(status_file.relative_to(REPO_ROOT))
    return result


def reconcile_decision(case_key: str, *, pretty: bool) -> dict[str, Any]:
    return run_python_script(RECONCILE_DECISION_STAGE, '--case-key', case_key, pretty=pretty)


def finalize_decision(case_key: str, *, pretty: bool) -> dict[str, Any]:
    return run_python_script(FINALIZE_DECISION_STAGE, '--case-key', case_key, '--apply', pretty=pretty)


def record_decision_launch_claim(
    *,
    case_key: str,
    status_path: Path,
    pid: int,
    log_path: Path,
    launch_status: str,
    prepare_payload: dict[str, Any],
) -> None:
    status_path.parent.mkdir(parents=True, exist_ok=True)
    event = {
        'at': utc_now_iso(),
        'stage': 'decision_receipt',
        'state': launch_status,
        'message': 'Decision-Maker launch claimed by automation controller',
        'runner_pid': pid,
        'launch_log_path': str(log_path.relative_to(REPO_ROOT)),
        'decision_context_path': str(prepare_payload.get('decision_context_path') or ''),
        'prompt_path': str(prepare_payload.get('prompt_path') or ''),
    }
    with locked_json_file(status_path) as status:
        status['status'] = 'handoff_sent'
        status['decision_launch_claim'] = {
            'claimed_at': event['at'],
            'runner_pid': pid,
            'launch_log_path': event['launch_log_path'],
            'decision_context_path': event['decision_context_path'],
            'prompt_path': event['prompt_path'],
            'launcher': 'pipeline_automation_actions.launch_decision_maker',
        }
        status.setdefault('stage_events', []).append(event)
        status['last_stage_event'] = dict(event)
        status['updated_at'] = event['at']


def record_decision_launch_immediate_failure(*, status_path: Path, pid: int, log_path: Path, returncode: int) -> None:
    event = {
        'at': utc_now_iso(),
        'stage': 'decision_receipt',
        'state': 'launch_failed_immediately',
        'message': 'Decision-Maker worker subprocess exited immediately after launch claim',
        'runner_pid': pid,
        'launch_log_path': str(log_path.relative_to(REPO_ROOT)),
        'returncode': returncode,
    }
    with locked_json_file(status_path) as status:
        status['status'] = 'handoff_prepared'
        claim = status.get('decision_launch_claim') if isinstance(status.get('decision_launch_claim'), dict) else {}
        claim.update({
            'failed_at': event['at'],
            'runner_pid': pid,
            'launch_log_path': event['launch_log_path'],
            'returncode': returncode,
        })
        status['decision_launch_claim'] = claim
        status.setdefault('stage_events', []).append(event)
        status['last_stage_event'] = dict(event)
        status['updated_at'] = event['at']


def spawn_background_decision_runner(case_key: str, *, prepare_payload: dict[str, Any], pretty: bool) -> dict[str, Any]:
    DECISION_LAUNCH_LOG_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    log_path = DECISION_LAUNCH_LOG_DIR / f'{case_key}-{timestamp}.log'
    cmd = [
        sys.executable,
        str(RUN_DECISION_MAKER),
        '--case-key',
        case_key,
    ]
    decision_context_path = str(prepare_payload.get('decision_context_path') or '').strip()
    prompt_path = str(prepare_payload.get('prompt_path') or '').strip()
    if decision_context_path:
        cmd.extend(['--decision-context-json', decision_context_path])
    if prompt_path:
        cmd.extend(['--prompt-path', prompt_path])
    if pretty:
        cmd.append('--pretty')
    with log_path.open('a', encoding='utf-8') as handle:
        proc = subprocess.Popen(
            cmd,
            cwd=str(REPO_ROOT),
            env=load_repo_env(),
            stdout=handle,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    return {
        'pid': proc.pid,
        'log_path': log_path,
        'cmd': cmd,
        'proc': proc,
    }


def launch_decision_maker(case_key: str, *, pretty: bool) -> dict[str, Any]:
    reconcile = reconcile_decision(case_key, pretty=pretty)
    payload = reconcile.get('payload') if isinstance(reconcile.get('payload'), dict) else {}
    health = str(payload.get('health') or '')
    if reconcile.get('ok') and health == 'ready':
        return {
            'ok': True,
            'launch_status': 'already_completed',
            'decision_health': health,
            'payload': payload,
        }
    if reconcile.get('ok') and health in {'in_progress', 'stale_status'}:
        return {
            'ok': True,
            'launch_status': 'already_running',
            'decision_health': health,
            'payload': payload,
        }
    if not reconcile.get('ok') and health not in {'not_started'}:
        return {
            'ok': False,
            'launch_status': 'terminal_failure',
            'decision_health': health,
            'payload': payload,
            'stderr': reconcile.get('stderr') or '',
            'stdout': reconcile.get('stdout') or '',
            'returncode': reconcile.get('returncode'),
        }

    prepare = run_python_script(RUN_DECISION_MAKER, '--case-key', case_key, '--prepare-only', pretty=pretty)
    prepare_payload = prepare.get('payload') if isinstance(prepare.get('payload'), dict) else {}
    if not prepare.get('ok'):
        return {
            'ok': False,
            'launch_status': 'retryable_transient_failure',
            'decision_health': 'not_started',
            'payload': prepare_payload,
            'stderr': prepare.get('stderr') or '',
            'stdout': prepare.get('stdout') or '',
            'returncode': prepare.get('returncode'),
        }

    spawn = spawn_background_decision_runner(case_key, prepare_payload=prepare_payload, pretty=pretty)
    status_path_value = str(prepare_payload.get('decision_stage_status_path') or '').strip()
    status_path = (REPO_ROOT / status_path_value) if status_path_value else (REPO_ROOT / 'qualitative-db' / '40-research' / 'cases' / case_key / 'decision-maker' / 'artifacts' / 'decision-stage-status.json')
    record_decision_launch_claim(
        case_key=case_key,
        status_path=status_path,
        pid=int(spawn['pid']),
        log_path=spawn['log_path'],
        launch_status='handoff_sent',
        prepare_payload=prepare_payload,
    )
    summary = summarize_case_pipeline_status(case_key)
    update_case_pipeline_status(
        case_key=case_key,
        dispatch_id=str(summary.get('dispatch_id') or '').strip(),
        market_id=str(summary.get('market_id') or '').strip(),
        market_title=str(summary.get('market_title') or '').strip(),
        status='pipeline_in_progress',
        current_stage='decision',
        stage_status_patch={'decision': 'running'},
        runner_id='pipeline_automation_actions.launch_decision_maker',
        message='Decision-Maker launch claimed and worker subprocess started',
    )
    time.sleep(0.5)
    returncode = spawn['proc'].poll()
    if returncode not in (None, 0):
        record_decision_launch_immediate_failure(status_path=status_path, pid=int(spawn['pid']), log_path=spawn['log_path'], returncode=int(returncode))
        return {
            'ok': False,
            'launch_status': 'retryable_transient_failure',
            'decision_health': 'not_started',
            'payload': prepare_payload,
            'runner_pid': int(spawn['pid']),
            'launch_log_path': str(spawn['log_path'].relative_to(REPO_ROOT)),
            'returncode': int(returncode),
        }
    return {
        'ok': True,
        'launch_status': 'started',
        'decision_health': 'not_started',
        'payload': prepare_payload,
        'runner_pid': int(spawn['pid']),
        'launch_log_path': str(spawn['log_path'].relative_to(REPO_ROOT)),
    }


def run_light_refresh_update(case_key: str, *, pretty: bool) -> dict[str, Any]:
    return run_python_script(RUN_LIGHT_REFRESH_UPDATE, '--case-key', case_key, pretty=pretty)


def run_resolution_sync(*, pretty: bool) -> dict[str, Any]:
    return run_python_script(SYNC_MARKET_RESOLUTIONS, pretty=pretty)


def run_manual_batch_controller(command: str, *, pretty: bool, extra_args: list[str] | None = None) -> dict[str, Any]:
    return run_python_script(MANUAL_BATCH_CONTROLLER, command, *(extra_args or []), pretty=pretty, timeout_seconds=MANUAL_LAUNCH_TIMEOUT_SECONDS)


def normalize_manual_launch_result(result: dict[str, Any]) -> dict[str, Any] | None:
    payload = result.get('payload') or {}
    launch_payload = payload.get('launch') if isinstance(payload.get('launch'), dict) else {}
    normalized_payload = launch_payload if launch_payload else payload
    normalized = {
        'ok': bool(result.get('ok')) and str(payload.get('status') or '') == 'ok',
        'payload': normalized_payload,
        'manual_payload': payload,
        'stdout': result.get('stdout') or '',
        'stderr': result.get('stderr') or '',
        'returncode': result.get('returncode'),
        'manual_status': str(payload.get('status') or ''),
    }
    if not normalized['ok'] and not normalized_payload and not payload:
        return None
    return normalized


def manual_launch_next(*, pretty: bool) -> dict[str, Any] | None:
    return normalize_manual_launch_result(run_manual_batch_controller('launch-next', pretty=pretty))


def manual_launch_case(case_id: str, *, pretty: bool, refresh_mode: str = '', refresh_reasons: list[str] | None = None, refresh_price_delta_pct_points: str = '', refresh_detected_marker: str = '') -> dict[str, Any] | None:
    extra_args = ['--case-id', case_id]
    if refresh_mode:
        extra_args.extend(['--refresh-mode', refresh_mode])
    if refresh_reasons:
        extra_args.extend(['--refresh-reasons', ','.join(str(item) for item in refresh_reasons if str(item).strip())])
    if refresh_price_delta_pct_points:
        extra_args.extend(['--refresh-price-delta-pct-points', refresh_price_delta_pct_points])
    if refresh_detected_marker:
        extra_args.extend(['--refresh-detected-marker', refresh_detected_marker])
    return normalize_manual_launch_result(
        run_manual_batch_controller('launch-case', pretty=pretty, extra_args=extra_args)
    )


def manual_launch_market(market_id: str, *, pretty: bool, refresh_mode: str = '', refresh_reasons: list[str] | None = None, refresh_price_delta_pct_points: str = '', refresh_detected_marker: str = '') -> dict[str, Any] | None:
    extra_args = ['--market-id', market_id]
    if refresh_mode:
        extra_args.extend(['--refresh-mode', refresh_mode])
    if refresh_reasons:
        extra_args.extend(['--refresh-reasons', ','.join(str(item) for item in refresh_reasons if str(item).strip())])
    if refresh_price_delta_pct_points:
        extra_args.extend(['--refresh-price-delta-pct-points', refresh_price_delta_pct_points])
    if refresh_detected_marker:
        extra_args.extend(['--refresh-detected-marker', refresh_detected_marker])
    return normalize_manual_launch_result(
        run_manual_batch_controller('launch-market', pretty=pretty, extra_args=extra_args)
    )


def watch_existing_case(summary: dict[str, Any], *, args: Any, policy: dict[str, Any]) -> dict[str, Any]:
    from watch_pipeline import watch_case as _watch_case
    return _watch_case(summary, args=args, policy=policy)
