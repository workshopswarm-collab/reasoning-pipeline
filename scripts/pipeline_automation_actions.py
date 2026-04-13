from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

from automation_runtime_support import AutomationRuntimeError, DEFAULT_SUBPROCESS_TIMEOUT_SECONDS, run_json_subprocess

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

MANUAL_LAUNCH_TIMEOUT_SECONDS = 600.0


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


def launch_decision_maker(case_key: str, *, pretty: bool) -> dict[str, Any]:
    return run_python_script(RUN_DECISION_MAKER, '--case-key', case_key, pretty=pretty)


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
