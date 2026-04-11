#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTROL_FILE = REPO_ROOT / 'scripts' / '.runtime-state' / 'pipeline-automation-control.json'


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


DEFAULT_CONTROL = {
    'artifact_type': 'pipeline_automation_control',
    'schema_version': 'pipeline-automation-control/v1',
    'updated_at': '',
    'automation_enabled': False,
    'watchdog': {
        'enabled': True,
        'apply': False,
        'allow_resume_swarm': False,
        'allow_launch_synthesis': False,
        'allow_launch_decision': False,
        'allow_finalize_decision': False,
        'allow_finalize_pipeline': False,
    },
    'sequencer': {
        'enabled': False,
        'allow_new_case_claims': False,
        'resume_existing': True,
        'poll_seconds': 15.0,
        'idle_seconds': 60.0,
        'max_case_seconds': 7200.0,
    },
}


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = dict(base)
    for key, value in override.items():
        if isinstance(result.get(key), dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def normalize_control_payload(payload: dict[str, Any] | None) -> dict[str, Any]:
    merged = deep_merge(DEFAULT_CONTROL, payload or {})
    merged['artifact_type'] = DEFAULT_CONTROL['artifact_type']
    merged['schema_version'] = DEFAULT_CONTROL['schema_version']
    merged['updated_at'] = str(merged.get('updated_at') or '')
    merged['automation_enabled'] = bool(merged.get('automation_enabled'))

    watchdog = deep_merge(DEFAULT_CONTROL['watchdog'], merged.get('watchdog') or {})
    for key in DEFAULT_CONTROL['watchdog']:
        watchdog[key] = bool(watchdog.get(key))
    merged['watchdog'] = watchdog

    sequencer = deep_merge(DEFAULT_CONTROL['sequencer'], merged.get('sequencer') or {})
    sequencer['enabled'] = bool(sequencer.get('enabled'))
    sequencer['allow_new_case_claims'] = bool(sequencer.get('allow_new_case_claims'))
    sequencer['resume_existing'] = bool(sequencer.get('resume_existing'))
    for key in ['poll_seconds', 'idle_seconds', 'max_case_seconds']:
        try:
            sequencer[key] = float(sequencer.get(key))
        except Exception:
            sequencer[key] = float(DEFAULT_CONTROL['sequencer'][key])
    merged['sequencer'] = sequencer
    return merged


def load_control_file(path: Path = DEFAULT_CONTROL_FILE) -> dict[str, Any]:
    candidate = Path(path)
    if not candidate.exists():
        return normalize_control_payload(None)
    try:
        payload = json.loads(candidate.read_text())
    except Exception:
        payload = {}
    return normalize_control_payload(payload if isinstance(payload, dict) else {})


def write_control_file(payload: dict[str, Any], path: Path = DEFAULT_CONTROL_FILE) -> Path:
    candidate = Path(path)
    candidate.parent.mkdir(parents=True, exist_ok=True)
    normalized = normalize_control_payload(payload)
    normalized['updated_at'] = utc_now_iso()
    candidate.write_text(json.dumps(normalized, indent=2, sort_keys=True) + '\n')
    return candidate


def resolve_watchdog_policy(control: dict[str, Any]) -> dict[str, Any]:
    payload = normalize_control_payload(control)
    watchdog = payload['watchdog']
    enabled = bool(watchdog['enabled'])
    apply_enabled = enabled and bool(watchdog['apply'])
    return {
        'enabled': enabled,
        'apply': apply_enabled,
        'allow_resume_swarm': apply_enabled and bool(watchdog['allow_resume_swarm']),
        'allow_launch_synthesis': apply_enabled and bool(watchdog['allow_launch_synthesis']),
        'allow_launch_decision': apply_enabled and bool(watchdog['allow_launch_decision']),
        'allow_finalize_decision': apply_enabled and bool(watchdog['allow_finalize_decision']),
        'allow_finalize_pipeline': apply_enabled and bool(watchdog['allow_finalize_pipeline']),
    }


def resolve_sequencer_policy(control: dict[str, Any]) -> dict[str, Any]:
    payload = normalize_control_payload(control)
    sequencer = payload['sequencer']
    enabled = bool(sequencer['enabled'])
    return {
        'enabled': enabled,
        'resume_existing': bool(sequencer['resume_existing']),
        'allow_new_case_claims': enabled and bool(payload['automation_enabled']) and bool(sequencer['allow_new_case_claims']),
        'poll_seconds': float(sequencer['poll_seconds']),
        'idle_seconds': float(sequencer['idle_seconds']),
        'max_case_seconds': float(sequencer['max_case_seconds']),
        'automation_enabled': bool(payload['automation_enabled']),
    }


def parse_toggle(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {'1', 'true', 'on', 'yes', 'enabled'}:
        return True
    if normalized in {'0', 'false', 'off', 'no', 'disabled'}:
        return False
    raise ValueError(f'invalid toggle value: {value}')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Manage the persisted pipeline automation control file')
    parser.add_argument('--control-file', default=str(DEFAULT_CONTROL_FILE))
    sub = parser.add_subparsers(dest='command', required=True)

    sub.add_parser('status', help='Show current control-file state and effective policies')
    sub.add_parser('disable-all', help='Disable new market claims, sequencer automation, and watchdog repairs')
    sub.add_parser('enable-sequencer', help='Enable the sequencer and allow new market claims')
    sub.add_parser('disable-sequencer', help='Disable the sequencer and new market claims')
    enable_repairs = sub.add_parser('enable-watchdog-repairs', help='Enable watchdog repair mode')
    enable_repairs.add_argument('--all-actions', action='store_true', help='Enable all currently supported repair actions')
    sub.add_parser('disable-watchdog-repairs', help='Disable watchdog repair mode')

    set_cmd = sub.add_parser('set', help='Patch individual control-file fields')
    set_cmd.add_argument('--automation-enabled')
    set_cmd.add_argument('--watchdog-enabled')
    set_cmd.add_argument('--watchdog-apply')
    set_cmd.add_argument('--allow-resume-swarm')
    set_cmd.add_argument('--allow-launch-synthesis')
    set_cmd.add_argument('--allow-launch-decision')
    set_cmd.add_argument('--allow-finalize-decision')
    set_cmd.add_argument('--allow-finalize-pipeline')
    set_cmd.add_argument('--sequencer-enabled')
    set_cmd.add_argument('--allow-new-case-claims')
    set_cmd.add_argument('--resume-existing')
    set_cmd.add_argument('--poll-seconds', type=float)
    set_cmd.add_argument('--idle-seconds', type=float)
    set_cmd.add_argument('--max-case-seconds', type=float)
    return parser.parse_args()


def cmd_status(path: Path) -> None:
    exists = path.exists()
    control = load_control_file(path)
    payload = {
        'path': str(path),
        'exists': exists,
        'control': control,
        'effective': {
            'watchdog': resolve_watchdog_policy(control),
            'sequencer': resolve_sequencer_policy(control),
        },
    }
    print(json.dumps(payload, indent=2))


def cmd_disable_all(path: Path) -> None:
    control = load_control_file(path)
    control['automation_enabled'] = False
    control['watchdog']['apply'] = False
    control['sequencer']['enabled'] = False
    control['sequencer']['allow_new_case_claims'] = False
    written = write_control_file(control, path)
    cmd_status(written)


def cmd_enable_sequencer(path: Path) -> None:
    control = load_control_file(path)
    control['automation_enabled'] = True
    control['sequencer']['enabled'] = True
    control['sequencer']['allow_new_case_claims'] = True
    written = write_control_file(control, path)
    cmd_status(written)


def cmd_disable_sequencer(path: Path) -> None:
    control = load_control_file(path)
    control['automation_enabled'] = False
    control['sequencer']['enabled'] = False
    control['sequencer']['allow_new_case_claims'] = False
    written = write_control_file(control, path)
    cmd_status(written)


def cmd_enable_watchdog_repairs(path: Path, *, all_actions: bool) -> None:
    control = load_control_file(path)
    control['watchdog']['enabled'] = True
    control['watchdog']['apply'] = True
    if all_actions:
        for key in ['allow_resume_swarm', 'allow_launch_synthesis', 'allow_launch_decision', 'allow_finalize_decision', 'allow_finalize_pipeline']:
            control['watchdog'][key] = True
    written = write_control_file(control, path)
    cmd_status(written)


def cmd_disable_watchdog_repairs(path: Path) -> None:
    control = load_control_file(path)
    control['watchdog']['apply'] = False
    written = write_control_file(control, path)
    cmd_status(written)


def cmd_set(path: Path, args: argparse.Namespace) -> None:
    control = load_control_file(path)
    bool_map = {
        'automation_enabled': 'automation_enabled',
    }
    for attr, key in bool_map.items():
        value = getattr(args, attr)
        if value is not None:
            control[key] = parse_toggle(value)

    watchdog_map = {
        'watchdog_enabled': 'enabled',
        'watchdog_apply': 'apply',
        'allow_resume_swarm': 'allow_resume_swarm',
        'allow_launch_synthesis': 'allow_launch_synthesis',
        'allow_launch_decision': 'allow_launch_decision',
        'allow_finalize_decision': 'allow_finalize_decision',
        'allow_finalize_pipeline': 'allow_finalize_pipeline',
    }
    for attr, key in watchdog_map.items():
        value = getattr(args, attr)
        if value is not None:
            control['watchdog'][key] = parse_toggle(value)

    sequencer_map = {
        'sequencer_enabled': 'enabled',
        'allow_new_case_claims': 'allow_new_case_claims',
        'resume_existing': 'resume_existing',
    }
    for attr, key in sequencer_map.items():
        value = getattr(args, attr)
        if value is not None:
            control['sequencer'][key] = parse_toggle(value)

    for attr in ['poll_seconds', 'idle_seconds', 'max_case_seconds']:
        value = getattr(args, attr)
        if value is not None:
            control['sequencer'][attr] = float(value)

    written = write_control_file(control, path)
    cmd_status(written)


def main() -> None:
    args = parse_args()
    path = Path(args.control_file).expanduser().resolve()
    if args.command == 'status':
        cmd_status(path)
    elif args.command == 'disable-all':
        cmd_disable_all(path)
    elif args.command == 'enable-sequencer':
        cmd_enable_sequencer(path)
    elif args.command == 'disable-sequencer':
        cmd_disable_sequencer(path)
    elif args.command == 'enable-watchdog-repairs':
        cmd_enable_watchdog_repairs(path, all_actions=bool(args.all_actions))
    elif args.command == 'disable-watchdog-repairs':
        cmd_disable_watchdog_repairs(path)
    elif args.command == 'set':
        cmd_set(path, args)
    else:
        raise SystemExit(f'unknown command: {args.command}')


if __name__ == '__main__':
    main()
