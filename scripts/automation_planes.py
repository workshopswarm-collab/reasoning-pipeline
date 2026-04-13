#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / 'scripts'
AUTOMATION_CONTROL = SCRIPTS_DIR / 'automation_control.py'
WATCHER_HELPER = SCRIPTS_DIR / 'launchd' / 'manage_decided_market_watcher_launch_agent.py'
DEFAULT_WATCHER_TARGET = Path.home() / 'Library' / 'LaunchAgents' / 'ai.openclaw.orchestrator.decided-market-watcher.plist'


def run_json(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(cmd, text=True, capture_output=True, cwd=REPO_ROOT)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"command failed: {' '.join(cmd)}")
    text = proc.stdout.strip()
    return json.loads(text) if text else {}


def automation_control_status() -> dict[str, Any]:
    return run_json([sys.executable, str(AUTOMATION_CONTROL), 'status'])


def watcher_status() -> dict[str, Any]:
    return run_json([sys.executable, str(WATCHER_HELPER), 'status'])


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


def enable_watcher_plane() -> dict[str, Any]:
    status = watcher_status()
    if bool(status.get('bootstrapped')):
        return {'ok': True, 'action': 'already_bootstrapped', 'status': status}
    return run_json([sys.executable, str(WATCHER_HELPER), 'install', '--bootstrap', '--kickstart'])


def disable_watcher_plane() -> dict[str, Any]:
    status = watcher_status()
    target_exists = bool(status.get('target_exists'))
    bootstrapped = bool(status.get('bootstrapped'))
    if not target_exists and not bootstrapped:
        return {'ok': True, 'action': 'already_disabled', 'status': status}
    cmd = [sys.executable, str(WATCHER_HELPER), 'uninstall']
    if bootstrapped:
        cmd.append('--bootout')
    return run_json(cmd)


def summarize(control_status: dict[str, Any], watcher: dict[str, Any]) -> dict[str, Any]:
    summary = ((control_status.get('summary') or {}) if isinstance(control_status.get('summary'), dict) else {})
    control = ((control_status.get('control') or {}) if isinstance(control_status.get('control'), dict) else {})
    watchdog = ((control.get('watchdog') or {}) if isinstance(control.get('watchdog'), dict) else {})
    sequencer = ((control.get('sequencer') or {}) if isinstance(control.get('sequencer'), dict) else {})
    all_enabled = bool(control.get('automation_enabled')) and bool(sequencer.get('enabled')) and bool(watchdog.get('enabled')) and bool(watchdog.get('apply')) and bool(watcher.get('bootstrapped'))
    return {
        'overall_mode': summary.get('overall_mode', ''),
        'sequencer_mode': summary.get('sequencer_mode', ''),
        'watchdog_mode': summary.get('watchdog_mode', ''),
        'decided_market_watcher_mode': 'active' if bool(watcher.get('bootstrapped')) else 'inactive',
        'all_planes_enabled': all_enabled,
        'watcher_launchctl_label': watcher.get('launchctl_label', ''),
        'watcher_target_exists': bool(watcher.get('target_exists')),
        'watcher_bootstrapped': bool(watcher.get('bootstrapped')),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Unified control wrapper for sequencer, watchdog, and decided-market watcher planes')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('status', help='Show unified status for all automation planes')
    sub.add_parser('enable-all', help='Enable sequencer + watchdog policy and bootstrap the decided-market watcher')
    sub.add_parser('disable-all', help='Disable sequencer + watchdog policy and boot out the decided-market watcher')
    return parser.parse_args()


def cmd_status() -> None:
    control = automation_control_status()
    watcher = watcher_status()
    print(json.dumps({
        'ok': True,
        'control': control,
        'decided_market_watcher': watcher,
        'summary': summarize(control, watcher),
    }, indent=2))


def cmd_enable_all() -> None:
    pipeline = set_pipeline_planes(enabled=True)
    watcher_action = enable_watcher_plane()
    control = automation_control_status()
    watcher = watcher_status()
    print(json.dumps({
        'ok': True,
        'pipeline': pipeline,
        'decided_market_watcher_action': watcher_action,
        'control': control,
        'decided_market_watcher': watcher,
        'summary': summarize(control, watcher),
    }, indent=2))


def cmd_disable_all() -> None:
    pipeline = set_pipeline_planes(enabled=False)
    watcher_action = disable_watcher_plane()
    control = automation_control_status()
    watcher = watcher_status()
    print(json.dumps({
        'ok': True,
        'pipeline': pipeline,
        'decided_market_watcher_action': watcher_action,
        'control': control,
        'decided_market_watcher': watcher,
        'summary': summarize(control, watcher),
    }, indent=2))


def main() -> None:
    args = parse_args()
    if args.command == 'status':
        cmd_status()
    elif args.command == 'enable-all':
        cmd_enable_all()
    elif args.command == 'disable-all':
        cmd_disable_all()
    else:
        raise SystemExit(f'unknown command: {args.command}')


if __name__ == '__main__':
    main()
