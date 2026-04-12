#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import plistlib
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / 'scripts'
HEALTHCHECK_SCRIPT = SCRIPTS_DIR / 'check_pipeline_health.py'
RUNTIME_STATE_DIR = SCRIPTS_DIR / '.runtime-state' / 'launchd'
DEFAULT_LABEL = 'ai.openclaw.orchestrator.pipeline-healthcheck'
DEFAULT_RENDER_PATH = Path(__file__).resolve().parent / f'{DEFAULT_LABEL}.plist'
DEFAULT_AGENT_PATH = Path.home() / 'Library' / 'LaunchAgents' / f'{DEFAULT_LABEL}.plist'
DEFAULT_PATH = '/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'
DEFAULT_HEARTBEAT_FILE = SCRIPTS_DIR / '.runtime-state' / 'pipeline-heartbeat.json'
DEFAULT_QUARANTINE_FILE = SCRIPTS_DIR / '.runtime-state' / 'pipeline-quarantine.json'
DEFAULT_REPORT_FILE = SCRIPTS_DIR / '.runtime-state' / 'pipeline-health-report.json'
DEFAULT_ARTIFACT_CONTRACT_ROOT = REPO_ROOT / 'qualitative-db' / '40-research' / 'cases'
DEFAULT_ARTIFACT_CONTRACT_REPORT_FILE = SCRIPTS_DIR / '.runtime-state' / 'pipeline-artifact-contract-report.json'
DEFAULT_DECIDED_MARKET_WATCHER_HEARTBEAT_FILE = SCRIPTS_DIR / '.runtime-state' / 'decided-market-watcher-heartbeat.json'
DEFAULT_MARKET_CHECKER_ENV_FILE = REPO_ROOT / '.env.postgres.local'
DEFAULT_MARKET_CHECKER_PSQL = '/opt/homebrew/opt/postgresql@16/bin/psql'


class LaunchdError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Render/install/status for the pipeline health-check launch agent')
    sub = parser.add_subparsers(dest='command', required=True)

    def add_common_render_flags(cmd: argparse.ArgumentParser) -> None:
        cmd.add_argument('--label', default=DEFAULT_LABEL)
        cmd.add_argument('--interval-seconds', type=int, default=300, help='launchd StartInterval seconds')
        cmd.add_argument('--python-bin', default=shutil.which('python3') or sys.executable, help='Absolute python3 path used by launchd')
        cmd.add_argument('--stdout-log', default=str(RUNTIME_STATE_DIR / 'pipeline-healthcheck.stdout.log'))
        cmd.add_argument('--stderr-log', default=str(RUNTIME_STATE_DIR / 'pipeline-healthcheck.stderr.log'))
        cmd.add_argument('--heartbeat-file', default=str(DEFAULT_HEARTBEAT_FILE))
        cmd.add_argument('--quarantine-file', default=str(DEFAULT_QUARANTINE_FILE))
        cmd.add_argument('--report-file', default=str(DEFAULT_REPORT_FILE))
        cmd.add_argument('--artifact-contract-root', default=str(DEFAULT_ARTIFACT_CONTRACT_ROOT))
        cmd.add_argument('--artifact-contract-report-file', default=str(DEFAULT_ARTIFACT_CONTRACT_REPORT_FILE))
        cmd.add_argument('--skip-artifact-contract-check', action='store_true')
        cmd.add_argument('--decided-market-watcher-heartbeat-file', default=str(DEFAULT_DECIDED_MARKET_WATCHER_HEARTBEAT_FILE))
        cmd.add_argument('--max-decided-market-watcher-age-seconds', type=float, default=120.0)
        cmd.add_argument('--skip-decided-market-watcher-check', action='store_true')
        cmd.add_argument('--market-checker-env-file', default=str(DEFAULT_MARKET_CHECKER_ENV_FILE))
        cmd.add_argument('--market-checker-psql', default=str(DEFAULT_MARKET_CHECKER_PSQL))
        cmd.add_argument('--max-market-snapshot-age-seconds', type=float, default=3600.0)
        cmd.add_argument('--skip-market-checker-check', action='store_true')
        cmd.add_argument('--max-heartbeat-age-seconds', type=float, default=1800.0)
        cmd.add_argument('--max-resolution-sync-age-seconds', type=float, default=5400.0)
        cmd.add_argument('--max-brier-age-seconds', type=float, default=172800.0)
        cmd.add_argument('--max-quarantine-count', type=int, default=10)

    render_cmd = sub.add_parser('render', help='Render the launch agent plist into the repo (or another path)')
    add_common_render_flags(render_cmd)
    render_cmd.add_argument('--output', default=str(DEFAULT_RENDER_PATH))
    render_cmd.add_argument('--stdout', action='store_true', help='Print plist to stdout instead of writing a file')

    install_cmd = sub.add_parser('install', help='Install the rendered plist into ~/Library/LaunchAgents')
    add_common_render_flags(install_cmd)
    install_cmd.add_argument('--target', default=str(DEFAULT_AGENT_PATH))
    install_cmd.add_argument('--bootstrap', action='store_true', help='After writing, bootstrap the agent into launchd')
    install_cmd.add_argument('--kickstart', action='store_true', help='Kickstart the job after bootstrap')

    status_cmd = sub.add_parser('status', help='Show staged-file and launchd bootstrap status')
    status_cmd.add_argument('--label', default=DEFAULT_LABEL)
    status_cmd.add_argument('--target', default=str(DEFAULT_AGENT_PATH))

    uninstall_cmd = sub.add_parser('uninstall', help='Remove the installed plist, optionally booting it out first')
    uninstall_cmd.add_argument('--label', default=DEFAULT_LABEL)
    uninstall_cmd.add_argument('--target', default=str(DEFAULT_AGENT_PATH))
    uninstall_cmd.add_argument('--bootout', action='store_true', help='Call launchctl bootout before removing the plist')

    return parser.parse_args()


def launchctl_domain() -> str:
    return f'gui/{os.getuid()}'


def launchctl_label(label: str) -> str:
    return f'{launchctl_domain()}/{label}'


def healthcheck_program_arguments(args: argparse.Namespace) -> list[str]:
    program = [
        str(Path(args.python_bin).expanduser().resolve()),
        str(HEALTHCHECK_SCRIPT),
        '--heartbeat-file', str(Path(args.heartbeat_file).expanduser().resolve()),
        '--quarantine-file', str(Path(args.quarantine_file).expanduser().resolve()),
        '--report-file', str(Path(args.report_file).expanduser().resolve()),
        '--artifact-contract-root', str(Path(args.artifact_contract_root).expanduser().resolve()),
        '--artifact-contract-report-file', str(Path(args.artifact_contract_report_file).expanduser().resolve()),
        '--decided-market-watcher-heartbeat-file', str(Path(args.decided_market_watcher_heartbeat_file).expanduser().resolve()),
        '--max-decided-market-watcher-age-seconds', str(args.max_decided_market_watcher_age_seconds),
        '--market-checker-env-file', str(Path(args.market_checker_env_file).expanduser().resolve()),
        '--market-checker-psql', str(Path(args.market_checker_psql).expanduser().resolve()),
        '--max-market-snapshot-age-seconds', str(args.max_market_snapshot_age_seconds),
        '--max-heartbeat-age-seconds', str(args.max_heartbeat_age_seconds),
        '--max-resolution-sync-age-seconds', str(args.max_resolution_sync_age_seconds),
        '--max-brier-age-seconds', str(args.max_brier_age_seconds),
        '--max-quarantine-count', str(args.max_quarantine_count),
        '--pretty',
    ]
    if args.skip_artifact_contract_check:
        program.append('--skip-artifact-contract-check')
    if args.skip_decided_market_watcher_check:
        program.append('--skip-decided-market-watcher-check')
    if args.skip_market_checker_check:
        program.append('--skip-market-checker-check')
    return program


def render_plist_payload(args: argparse.Namespace) -> dict[str, Any]:
    stdout_log = Path(args.stdout_log).expanduser().resolve()
    stderr_log = Path(args.stderr_log).expanduser().resolve()
    return {
        'Label': args.label,
        'ProgramArguments': healthcheck_program_arguments(args),
        'WorkingDirectory': str(REPO_ROOT),
        'RunAtLoad': True,
        'StartInterval': int(args.interval_seconds),
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


def ensure_parent_dirs(args: argparse.Namespace) -> None:
    Path(args.stdout_log).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
    Path(args.stderr_log).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
    Path(args.heartbeat_file).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
    Path(args.quarantine_file).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
    Path(args.report_file).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
    Path(args.artifact_contract_root).expanduser().resolve().mkdir(parents=True, exist_ok=True)
    Path(args.artifact_contract_report_file).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
    Path(args.decided_market_watcher_heartbeat_file).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
    Path(args.market_checker_env_file).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)


def write_plist(path: Path, payload: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(plist_bytes(payload))
    return path


def run_launchctl(*parts: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(['launchctl', *parts], text=True, capture_output=True)


def status_payload(label: str, target: Path) -> dict[str, Any]:
    proc = run_launchctl('print', launchctl_label(label))
    bootstrapped = proc.returncode == 0
    return {
        'label': label,
        'target': str(target),
        'target_exists': target.exists(),
        'bootstrapped': bootstrapped,
        'launchctl_domain': launchctl_domain(),
        'launchctl_label': launchctl_label(label),
        'launchctl_stdout': proc.stdout.strip(),
        'launchctl_stderr': proc.stderr.strip(),
    }


def cmd_render(args: argparse.Namespace) -> None:
    ensure_parent_dirs(args)
    payload = render_plist_payload(args)
    if args.stdout:
        sys.stdout.buffer.write(plist_bytes(payload))
        return
    output = Path(args.output).expanduser().resolve()
    write_plist(output, payload)
    print(output)


def cmd_install(args: argparse.Namespace) -> None:
    ensure_parent_dirs(args)
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
    print(json_dump(result))


def cmd_status(args: argparse.Namespace) -> None:
    payload = status_payload(args.label, Path(args.target).expanduser().resolve())
    print(json_dump(payload))


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
    print(json_dump(result))


def json_dump(payload: dict[str, Any]) -> str:
    import json
    return json.dumps(payload, indent=2)


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
