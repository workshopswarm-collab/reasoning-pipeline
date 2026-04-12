#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import plistlib
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / 'scripts'
WATCHER_SCRIPT = SCRIPTS_DIR / 'watch_decided_market_prices.py'
RUNTIME_STATE_DIR = SCRIPTS_DIR / '.runtime-state' / 'launchd'
DEFAULT_LABEL = 'ai.openclaw.orchestrator.decided-market-watcher'
DEFAULT_RENDER_PATH = Path(__file__).resolve().parent / f'{DEFAULT_LABEL}.plist'
DEFAULT_AGENT_PATH = Path.home() / 'Library' / 'LaunchAgents' / f'{DEFAULT_LABEL}.plist'
DEFAULT_PATH = '/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'
DEFAULT_ENV_FILE = REPO_ROOT / '.env.postgres.local'
DEFAULT_REPORT_FILE = SCRIPTS_DIR / '.runtime-state' / 'decided-market-watcher-heartbeat.json'
DEFAULT_LOCK_FILE = SCRIPTS_DIR / '.runtime-state' / 'decided-market-watcher.lock'
DEFAULT_PSQL = '/opt/homebrew/opt/postgresql@16/bin/psql'


class LaunchdError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Render/install/status for the decided-market watcher launch agent')
    sub = parser.add_subparsers(dest='command', required=True)

    def add_common(cmd: argparse.ArgumentParser) -> None:
        cmd.add_argument('--label', default=DEFAULT_LABEL)
        cmd.add_argument('--poll-seconds', type=int, default=30)
        cmd.add_argument('--python-bin', default=shutil.which('python3') or sys.executable)
        cmd.add_argument('--stdout-log', default=str(RUNTIME_STATE_DIR / 'decided-market-watcher.stdout.log'))
        cmd.add_argument('--stderr-log', default=str(RUNTIME_STATE_DIR / 'decided-market-watcher.stderr.log'))
        cmd.add_argument('--lock-file', default=str(DEFAULT_LOCK_FILE))
        cmd.add_argument('--report-file', default=str(DEFAULT_REPORT_FILE))
        cmd.add_argument('--env-file', default=str(DEFAULT_ENV_FILE))
        cmd.add_argument('--psql', default=str(DEFAULT_PSQL))
        cmd.add_argument('--min-price-delta', type=float, default=0.05)

    render_cmd = sub.add_parser('render', help='Render the launch agent plist')
    add_common(render_cmd)
    render_cmd.add_argument('--output', default=str(DEFAULT_RENDER_PATH))
    render_cmd.add_argument('--stdout', action='store_true')

    install_cmd = sub.add_parser('install', help='Install the launch agent into ~/Library/LaunchAgents')
    add_common(install_cmd)
    install_cmd.add_argument('--target', default=str(DEFAULT_AGENT_PATH))
    install_cmd.add_argument('--bootstrap', action='store_true')
    install_cmd.add_argument('--kickstart', action='store_true')

    status_cmd = sub.add_parser('status', help='Show staged-file and launchd bootstrap status')
    status_cmd.add_argument('--label', default=DEFAULT_LABEL)
    status_cmd.add_argument('--target', default=str(DEFAULT_AGENT_PATH))

    uninstall_cmd = sub.add_parser('uninstall', help='Remove the installed plist, optionally booting it out first')
    uninstall_cmd.add_argument('--label', default=DEFAULT_LABEL)
    uninstall_cmd.add_argument('--target', default=str(DEFAULT_AGENT_PATH))
    uninstall_cmd.add_argument('--bootout', action='store_true')

    return parser.parse_args()


def launchctl_domain() -> str:
    return f'gui/{os.getuid()}'


def launchctl_label(label: str) -> str:
    return f'{launchctl_domain()}/{label}'


def program_arguments(args: argparse.Namespace) -> list[str]:
    return [
        str(Path(args.python_bin).expanduser().resolve()),
        str(WATCHER_SCRIPT),
        '--env-file', str(Path(args.env_file).expanduser().resolve()),
        '--psql', str(Path(args.psql).expanduser().resolve()),
        '--lock-file', str(Path(args.lock_file).expanduser().resolve()),
        '--report-file', str(Path(args.report_file).expanduser().resolve()),
        '--min-price-delta', str(args.min_price_delta),
        '--apply',
        '--pretty',
    ]


def render_plist_payload(args: argparse.Namespace) -> dict[str, Any]:
    stdout_log = Path(args.stdout_log).expanduser().resolve()
    stderr_log = Path(args.stderr_log).expanduser().resolve()
    return {
        'Label': args.label,
        'ProgramArguments': program_arguments(args),
        'WorkingDirectory': str(REPO_ROOT),
        'RunAtLoad': True,
        'StartInterval': int(args.poll_seconds),
        'StandardOutPath': str(stdout_log),
        'StandardErrorPath': str(stderr_log),
        'ProcessType': 'Background',
        'EnvironmentVariables': {
            'PATH': DEFAULT_PATH,
            'PYTHONUNBUFFERED': '1',
        },
    }


def plist_bytes(payload: dict[str, Any]) -> bytes:
    return plistlib.dumps(payload, fmt=plistlib.FMT_XML, sort_keys=False)


def ensure_parents(args: argparse.Namespace) -> None:
    Path(args.stdout_log).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
    Path(args.stderr_log).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
    Path(args.lock_file).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
    Path(args.report_file).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
    Path(args.env_file).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)


def write_plist(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(plist_bytes(payload))


def run_launchctl(*parts: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(['launchctl', *parts], text=True, capture_output=True)


def status_payload(label: str, target: Path) -> dict[str, Any]:
    proc = run_launchctl('print', launchctl_label(label))
    return {
        'label': label,
        'target': str(target),
        'target_exists': target.exists(),
        'bootstrapped': proc.returncode == 0,
        'launchctl_domain': launchctl_domain(),
        'launchctl_label': launchctl_label(label),
        'launchctl_stdout': proc.stdout.strip(),
        'launchctl_stderr': proc.stderr.strip(),
    }


def cmd_render(args: argparse.Namespace) -> None:
    ensure_parents(args)
    payload = render_plist_payload(args)
    if args.stdout:
        sys.stdout.buffer.write(plist_bytes(payload))
        return
    output = Path(args.output).expanduser().resolve()
    write_plist(output, payload)
    print(output)


def cmd_install(args: argparse.Namespace) -> None:
    ensure_parents(args)
    target = Path(args.target).expanduser().resolve()
    payload = render_plist_payload(args)
    write_plist(target, payload)
    result = {
        'ok': True,
        'label': args.label,
        'target': str(target),
        'bootstrapped': False,
        'kickstarted': False,
        'note': 'plist written only; not active until launchctl bootstrap is run',
    }
    if args.bootstrap:
        proc = run_launchctl('bootstrap', launchctl_domain(), str(target))
        if proc.returncode != 0:
            raise LaunchdError(proc.stderr.strip() or proc.stdout.strip() or 'launchctl bootstrap failed')
        result['bootstrapped'] = True
        if args.kickstart:
            kick = run_launchctl('kickstart', '-k', launchctl_label(args.label))
            if kick.returncode != 0:
                raise LaunchdError(kick.stderr.strip() or kick.stdout.strip() or 'launchctl kickstart failed')
            result['kickstarted'] = True
    print(json.dumps(result, indent=2))


def cmd_status(args: argparse.Namespace) -> None:
    print(json.dumps(status_payload(args.label, Path(args.target).expanduser().resolve()), indent=2))


def cmd_uninstall(args: argparse.Namespace) -> None:
    target = Path(args.target).expanduser().resolve()
    result = {
        'ok': True,
        'label': args.label,
        'target': str(target),
        'booted_out': False,
        'removed': False,
    }
    if args.bootout:
        proc = run_launchctl('bootout', launchctl_domain(), str(target))
        if proc.returncode == 0:
            result['booted_out'] = True
        else:
            result['bootout_error'] = proc.stderr.strip() or proc.stdout.strip()
    if target.exists():
        target.unlink()
        result['removed'] = True
    print(json.dumps(result, indent=2))


def main() -> None:
    args = parse_args()
    if args.command == 'render':
        cmd_render(args)
    elif args.command == 'install':
        cmd_install(args)
    elif args.command == 'status':
        cmd_status(args)
    elif args.command == 'uninstall':
        cmd_uninstall(args)
    else:
        raise SystemExit(f'unknown command: {args.command}')


if __name__ == '__main__':
    main()
