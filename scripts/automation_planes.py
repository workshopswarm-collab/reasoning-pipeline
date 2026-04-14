#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / 'scripts'
AUTOMATION_CONTROL = SCRIPTS_DIR / 'automation_control.py'
SEQUENCER_HELPER = SCRIPTS_DIR / 'launchd' / 'manage_pipeline_sequencer_launch_agent.py'
WATCHDOG_HELPER = SCRIPTS_DIR / 'launchd' / 'manage_pipeline_watchdog_launch_agent.py'
WATCHER_HELPER = SCRIPTS_DIR / 'launchd' / 'manage_decided_market_watcher_launch_agent.py'
DEFAULT_SEQUENCER_TARGET = Path.home() / 'Library' / 'LaunchAgents' / 'ai.openclaw.orchestrator.pipeline-sequencer.plist'
DEFAULT_WATCHDOG_TARGET = Path.home() / 'Library' / 'LaunchAgents' / 'ai.openclaw.orchestrator.pipeline-watchdog.plist'
DEFAULT_WATCHER_TARGET = Path.home() / 'Library' / 'LaunchAgents' / 'ai.openclaw.orchestrator.decided-market-watcher.plist'
SEQUENCER_HEARTBEAT = SCRIPTS_DIR / '.runtime-state' / 'pipeline-heartbeat.json'
WATCHDOG_HEARTBEAT = SCRIPTS_DIR / '.runtime-state' / 'pipeline-watchdog-heartbeat.json'
WATCHER_HEARTBEAT = SCRIPTS_DIR / '.runtime-state' / 'decided-market-watcher-heartbeat.json'
DEFAULT_SERVICE_STALE_SECONDS = {
    'sequencer': 180.0,
    'watchdog': 180.0,
    'decided_market_watcher': 180.0,
}


def run_json(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(cmd, text=True, capture_output=True, cwd=REPO_ROOT)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"command failed: {' '.join(cmd)}")
    text = proc.stdout.strip()
    return json.loads(text) if text else {}


def automation_control_status() -> dict[str, Any]:
    return run_json([sys.executable, str(AUTOMATION_CONTROL), 'status'])


def plane_status(helper: Path) -> dict[str, Any]:
    return run_json([sys.executable, str(helper), 'status'])


def sequencer_status() -> dict[str, Any]:
    return plane_status(SEQUENCER_HELPER)


def watchdog_status() -> dict[str, Any]:
    return plane_status(WATCHDOG_HELPER)


def watcher_status() -> dict[str, Any]:
    return plane_status(WATCHER_HELPER)


def run_cmd(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, cwd=REPO_ROOT)


def parse_iso_datetime(value: str) -> datetime | None:
    text = str(value or '').strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text.replace('Z', '+00:00'))
    except ValueError:
        return None


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def read_json_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def heartbeat_summary(name: str, path: Path, *, default_max_age_seconds: float) -> dict[str, Any]:
    payload = read_json_file(path)
    updated_at = parse_iso_datetime(str(payload.get('updated_at') or payload.get('completed_at') or payload.get('last_loop_completed_at') or payload.get('started_at') or ''))
    age_seconds = None
    if updated_at is not None:
        if updated_at.tzinfo is None:
            updated_at = updated_at.replace(tzinfo=timezone.utc)
        age_seconds = max(0.0, (now_utc() - updated_at.astimezone(timezone.utc)).total_seconds())
    state = str(payload.get('state') or '').strip()
    max_age_seconds = float(default_max_age_seconds)
    if state in {'idle_sleep', 'deferred_retry_sleep'}:
        try:
            max_age_seconds = max(max_age_seconds, float(payload.get('last_idle_sleep_seconds') or 0.0) * 3.0)
        except Exception:
            pass
    stale = bool(payload) and age_seconds is not None and age_seconds > max_age_seconds
    return {
        'exists': path.exists(),
        'path': str(path),
        'updated_at': updated_at.isoformat().replace('+00:00', 'Z') if updated_at is not None else '',
        'age_seconds': age_seconds,
        'stale': stale,
        'max_age_seconds': max_age_seconds,
        'state': state,
        'payload': payload,
    }


def kickstart_launchd(label: str) -> dict[str, Any]:
    proc = run_cmd(['launchctl', 'kickstart', '-k', label])
    return {
        'ok': proc.returncode == 0,
        'stdout': proc.stdout.strip(),
        'stderr': proc.stderr.strip(),
        'launchctl_label': label,
    }


def set_pipeline_planes(*, enabled: bool) -> dict[str, Any]:
    cmd = [
        sys.executable,
        str(AUTOMATION_CONTROL),
        'set',
        '--automation-enabled', 'true' if enabled else 'false',
        '--watchdog-enabled', 'true' if enabled else 'false',
        '--watchdog-apply', 'true' if enabled else 'false',
        '--allow-resume-swarm', 'true' if enabled else 'false',
        '--allow-launch-synthesis', 'true' if enabled else 'false',
        '--allow-launch-decision', 'true' if enabled else 'false',
        '--allow-finalize-decision', 'true' if enabled else 'false',
        '--allow-finalize-pipeline', 'true' if enabled else 'false',
        '--sequencer-enabled', 'true' if enabled else 'false',
        '--allow-new-case-claims', 'true' if enabled else 'false',
        '--resume-existing', 'true',
    ]
    return run_json(cmd)


def enable_launchd_plane(name: str, helper: Path) -> dict[str, Any]:
    status = plane_status(helper)
    if bool(status.get('bootstrapped')):
        kick = kickstart_launchd(str(status.get('launchctl_label') or ''))
        return {'ok': bool(kick.get('ok')), 'action': 'kickstarted', 'status': status, 'kickstart': kick, 'plane': name}
    result = run_json([sys.executable, str(helper), 'install', '--bootstrap', '--kickstart'])
    result['plane'] = name
    return result


def disable_launchd_plane(name: str, helper: Path) -> dict[str, Any]:
    status = plane_status(helper)
    target_exists = bool(status.get('target_exists'))
    bootstrapped = bool(status.get('bootstrapped'))
    if not target_exists and not bootstrapped:
        return {'ok': True, 'action': 'already_disabled', 'status': status, 'plane': name}
    cmd = [sys.executable, str(helper), 'uninstall']
    if bootstrapped:
        cmd.append('--bootout')
    result = run_json(cmd)
    result['plane'] = name
    return result


def enable_watcher_plane() -> dict[str, Any]:
    return enable_launchd_plane('decided_market_watcher', WATCHER_HELPER)


def disable_watcher_plane() -> dict[str, Any]:
    return disable_launchd_plane('decided_market_watcher', WATCHER_HELPER)


def summarize(control_status: dict[str, Any], planes: dict[str, dict[str, Any]]) -> dict[str, Any]:
    summary = ((control_status.get('summary') or {}) if isinstance(control_status.get('summary'), dict) else {})
    control = ((control_status.get('control') or {}) if isinstance(control_status.get('control'), dict) else {})
    watchdog = ((control.get('watchdog') or {}) if isinstance(control.get('watchdog'), dict) else {})
    sequencer = ((control.get('sequencer') or {}) if isinstance(control.get('sequencer'), dict) else {})
    sequencer_plane = planes.get('sequencer') or {}
    watchdog_plane = planes.get('watchdog') or {}
    watcher_plane = planes.get('decided_market_watcher') or {}
    all_enabled = (
        bool(control.get('automation_enabled'))
        and bool(sequencer.get('enabled'))
        and bool(watchdog.get('enabled'))
        and bool(watchdog.get('apply'))
        and bool(sequencer_plane.get('service', {}).get('bootstrapped'))
        and bool(watchdog_plane.get('service', {}).get('bootstrapped'))
        and bool(watcher_plane.get('service', {}).get('bootstrapped'))
    )
    return {
        'overall_mode': summary.get('overall_mode', ''),
        'sequencer_mode': summary.get('sequencer_mode', ''),
        'watchdog_mode': summary.get('watchdog_mode', ''),
        'sequencer_service_mode': 'active' if bool(sequencer_plane.get('service', {}).get('bootstrapped')) else 'inactive',
        'watchdog_service_mode': 'active' if bool(watchdog_plane.get('service', {}).get('bootstrapped')) else 'inactive',
        'decided_market_watcher_mode': 'active' if bool(watcher_plane.get('service', {}).get('bootstrapped')) else 'inactive',
        'all_planes_enabled': all_enabled,
        'stale_heartbeats': {
            name: bool((plane.get('heartbeat') or {}).get('stale'))
            for name, plane in planes.items()
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Unified control wrapper for sequencer, watchdog, and decided-market watcher planes')
    sub = parser.add_subparsers(dest='command', required=True)
    status = sub.add_parser('status', help='Show unified status for all automation planes')
    status.add_argument('--restart-stale', action='store_true', help='Kickstart launchd services when their heartbeat is stale or missing')
    sub.add_parser('enable-all', help='Enable sequencer + watchdog policy and ensure all launchd-managed planes are running')
    sub.add_parser('disable-all', help='Disable sequencer + watchdog policy and boot out all launchd-managed planes')
    ensure = sub.add_parser('ensure-running', help='Ensure launchd-managed planes are bootstrapped and kickstart stale services')
    ensure.add_argument('--no-restart-stale', dest='restart_stale', action='store_false', help='Do not kickstart services when their heartbeat is stale or missing')
    ensure.set_defaults(restart_stale=True)
    return parser.parse_args()


def collect_plane_states() -> dict[str, dict[str, Any]]:
    return {
        'sequencer': {
            'service': sequencer_status(),
            'heartbeat': heartbeat_summary('sequencer', SEQUENCER_HEARTBEAT, default_max_age_seconds=DEFAULT_SERVICE_STALE_SECONDS['sequencer']),
        },
        'watchdog': {
            'service': watchdog_status(),
            'heartbeat': heartbeat_summary('watchdog', WATCHDOG_HEARTBEAT, default_max_age_seconds=DEFAULT_SERVICE_STALE_SECONDS['watchdog']),
        },
        'decided_market_watcher': {
            'service': watcher_status(),
            'heartbeat': heartbeat_summary('decided_market_watcher', WATCHER_HEARTBEAT, default_max_age_seconds=DEFAULT_SERVICE_STALE_SECONDS['decided_market_watcher']),
        },
    }


def ensure_plane_running(name: str, helper: Path, plane_state: dict[str, Any], *, restart_stale: bool) -> dict[str, Any]:
    service = plane_state.get('service') if isinstance(plane_state.get('service'), dict) else {}
    heartbeat = plane_state.get('heartbeat') if isinstance(plane_state.get('heartbeat'), dict) else {}
    actions: list[dict[str, Any]] = []
    if not bool(service.get('bootstrapped')):
        actions.append(enable_launchd_plane(name, helper))
    elif restart_stale and (not bool(heartbeat.get('exists')) or bool(heartbeat.get('stale'))):
        actions.append({'plane': name, 'action': 'kickstart_for_stale_heartbeat', 'result': kickstart_launchd(str(service.get('launchctl_label') or ''))})
    refreshed = {
        'sequencer': sequencer_status,
        'watchdog': watchdog_status,
        'decided_market_watcher': watcher_status,
    }[name]()
    return {
        'plane': name,
        'actions': actions,
        'service': refreshed,
    }


def cmd_status(*, restart_stale: bool = False) -> None:
    control = automation_control_status()
    planes = collect_plane_states()
    ensure_actions: list[dict[str, Any]] = []
    if restart_stale:
        for name, helper in [('sequencer', SEQUENCER_HELPER), ('watchdog', WATCHDOG_HELPER), ('decided_market_watcher', WATCHER_HELPER)]:
            ensure_actions.append(ensure_plane_running(name, helper, planes[name], restart_stale=True))
        planes = collect_plane_states()
    print(json.dumps({
        'ok': True,
        'control': control,
        'planes': planes,
        'ensure_actions': ensure_actions,
        'summary': summarize(control, planes),
    }, indent=2))


def cmd_ensure_running(*, restart_stale: bool = True) -> None:
    control = automation_control_status()
    planes = collect_plane_states()
    actions = [
        ensure_plane_running('sequencer', SEQUENCER_HELPER, planes['sequencer'], restart_stale=restart_stale),
        ensure_plane_running('watchdog', WATCHDOG_HELPER, planes['watchdog'], restart_stale=restart_stale),
        ensure_plane_running('decided_market_watcher', WATCHER_HELPER, planes['decided_market_watcher'], restart_stale=restart_stale),
    ]
    planes = collect_plane_states()
    print(json.dumps({
        'ok': True,
        'control': control,
        'ensure_actions': actions,
        'planes': planes,
        'summary': summarize(control, planes),
    }, indent=2))


def cmd_enable_all() -> None:
    pipeline = set_pipeline_planes(enabled=True)
    planes = collect_plane_states()
    ensure_actions = [
        ensure_plane_running('sequencer', SEQUENCER_HELPER, planes['sequencer'], restart_stale=True),
        ensure_plane_running('watchdog', WATCHDOG_HELPER, planes['watchdog'], restart_stale=True),
        ensure_plane_running('decided_market_watcher', WATCHER_HELPER, planes['decided_market_watcher'], restart_stale=True),
    ]
    control = automation_control_status()
    planes = collect_plane_states()
    print(json.dumps({
        'ok': True,
        'pipeline': pipeline,
        'ensure_actions': ensure_actions,
        'control': control,
        'planes': planes,
        'summary': summarize(control, planes),
    }, indent=2))


def cmd_disable_all() -> None:
    pipeline = set_pipeline_planes(enabled=False)
    disable_actions = [
        disable_launchd_plane('sequencer', SEQUENCER_HELPER),
        disable_launchd_plane('watchdog', WATCHDOG_HELPER),
        disable_launchd_plane('decided_market_watcher', WATCHER_HELPER),
    ]
    control = automation_control_status()
    planes = collect_plane_states()
    print(json.dumps({
        'ok': True,
        'pipeline': pipeline,
        'disable_actions': disable_actions,
        'control': control,
        'planes': planes,
        'summary': summarize(control, planes),
    }, indent=2))


def main() -> None:
    args = parse_args()
    if args.command == 'status':
        cmd_status(restart_stale=bool(getattr(args, 'restart_stale', False)))
    elif args.command == 'enable-all':
        cmd_enable_all()
    elif args.command == 'disable-all':
        cmd_disable_all()
    elif args.command == 'ensure-running':
        cmd_ensure_running(restart_stale=bool(getattr(args, 'restart_stale', True)))
    else:
        raise SystemExit(f'unknown command: {args.command}')


if __name__ == '__main__':
    main()
