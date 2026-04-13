from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from case_pipeline_status import update_case_pipeline_status_with_followups as update_case_pipeline_status
from pipeline_automation_actions import REPO_ROOT


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def write_runtime_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')


def load_quarantine_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {'schema_version': 'pipeline-quarantine/v1', 'updated_at': '', 'entries': []}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {'schema_version': 'pipeline-quarantine/v1', 'updated_at': '', 'entries': []}
    if not isinstance(payload, dict):
        return {'schema_version': 'pipeline-quarantine/v1', 'updated_at': '', 'entries': []}
    entries = payload.get('entries')
    if not isinstance(entries, list):
        payload['entries'] = []
    payload.setdefault('schema_version', 'pipeline-quarantine/v1')
    payload.setdefault('updated_at', '')
    return payload


def save_quarantine_registry(path: Path, payload: dict[str, Any]) -> None:
    write_runtime_json(path, payload)


def prune_quarantine_entries(payload: dict[str, Any], *, now_ts: float) -> dict[str, Any]:
    kept: list[dict[str, Any]] = []
    for entry in list(payload.get('entries') or []):
        try:
            release_at = float(entry.get('release_at_ts'))
        except Exception:
            release_at = 0.0
        if release_at > now_ts:
            kept.append(entry)
    payload['entries'] = kept
    payload['updated_at'] = utc_now_iso()
    return payload


def active_quarantine_sets(payload: dict[str, Any]) -> tuple[set[str], set[str]]:
    case_keys: set[str] = set()
    market_ids: set[str] = set()
    for entry in payload.get('entries') or []:
        case_key = str(entry.get('case_key') or '').strip()
        market_id = str(entry.get('market_id') or '').strip()
        if case_key:
            case_keys.add(case_key)
        if market_id:
            market_ids.add(market_id)
    return case_keys, market_ids


def write_heartbeat(path: Path, payload: dict[str, Any]) -> None:
    payload['schema_version'] = 'pipeline-heartbeat/v1'
    payload['updated_at'] = utc_now_iso()
    write_runtime_json(path, payload)


def update_heartbeat_activity(
    heartbeat: dict[str, Any],
    *,
    phase: str,
    message: str = '',
    case_key: str = '',
    market_id: str = '',
    dispatch_id: str = '',
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    activity: dict[str, Any] = {
        'phase': phase,
        'updated_at': utc_now_iso(),
    }
    if message:
        activity['message'] = message
    if case_key:
        activity['case_key'] = case_key
    if market_id:
        activity['market_id'] = market_id
    if dispatch_id:
        activity['dispatch_id'] = dispatch_id
    if details:
        activity['details'] = details
    heartbeat['state'] = 'running'
    heartbeat['current_activity'] = activity
    return heartbeat


def heartbeat_base(args: Any) -> dict[str, Any]:
    return {
        'runner': 'pipeline-sequencer',
        'pid': os.getpid(),
        'repo_root': str(REPO_ROOT),
        'loop_mode': bool(args.loop),
        'control_managed': bool(args.control_managed),
        'lock_file': str(Path(args.lock_file).expanduser().resolve()),
        'heartbeat_file': str(Path(args.heartbeat_file).expanduser().resolve()),
        'quarantine_file': str(Path(args.quarantine_file).expanduser().resolve()),
        'brier_output_dir': str(Path(args.brier_output_dir).expanduser().resolve()),
        'config': {
            'poll_seconds': float(args.poll_seconds),
            'idle_seconds': float(args.idle_seconds),
            'max_case_seconds': float(args.max_case_seconds),
            'resolution_sync_seconds': float(args.resolution_sync_seconds),
            'brier_snapshot_seconds': float(args.brier_snapshot_seconds),
            'quarantine_seconds': float(args.quarantine_seconds),
        },
        'started_at': utc_now_iso(),
        'state': 'starting',
        'processed_cases_total': 0,
        'quarantine_count': 0,
    }


def extract_case_market_refs(result: dict[str, Any]) -> tuple[str, str]:
    case_key = str(result.get('case_key') or '').strip()
    market_id = ''
    for candidate in [
        result.get('market_id'),
        ((result.get('pipeline_summary') or {}) if isinstance(result.get('pipeline_summary'), dict) else {}).get('market_id'),
        ((result.get('refresh_candidate') or {}) if isinstance(result.get('refresh_candidate'), dict) else {}).get('market_id'),
        (((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary') or {}).get('market_id') if isinstance(((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary'), dict) else '',
    ]:
        text = str(candidate or '').strip()
        if text and not market_id:
            market_id = text
    if not case_key:
        for candidate in [
            ((result.get('refresh_candidate') or {}) if isinstance(result.get('refresh_candidate'), dict) else {}).get('case_key'),
            ((result.get('refresh_candidate') or {}) if isinstance(result.get('refresh_candidate'), dict) else {}).get('latest_forecast_case_key'),
            ((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('case_key'),
            (((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary') or {}).get('case_key') if isinstance(((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary'), dict) else '',
        ]:
            text = str(candidate or '').strip()
            if text:
                case_key = text
                break
    return case_key, market_id


def is_soft_fail_status(result: dict[str, Any]) -> bool:
    status = str(result.get('status') or '')
    return status in {
        'processed_existing_case',
        'processed_new_case',
        'processed_refresh_case',
        'processed_light_refresh_case',
        'refresh_open_case_failed',
        'light_refresh_missing_case_key',
        'prepare_launch_failed',
        'prepare_unknown_failure',
    }


def record_quarantine_entry(path: Path, *, case_key: str = '', market_id: str = '', reason: str, result: dict[str, Any], quarantine_seconds: float) -> dict[str, Any]:
    payload = prune_quarantine_entries(load_quarantine_registry(path), now_ts=time.time())
    now_ts = time.time()
    entry = {
        'case_key': case_key,
        'market_id': market_id,
        'reason': reason,
        'quarantined_at': utc_now_iso(),
        'quarantined_at_ts': now_ts,
        'release_at_ts': now_ts + float(quarantine_seconds),
        'result_status': str(result.get('status') or ''),
        'result_ok': bool(result.get('ok')),
    }
    payload.setdefault('entries', []).append(entry)
    payload['updated_at'] = utc_now_iso()
    save_quarantine_registry(path, payload)
    return entry


def periodic_task_brief(task: dict[str, Any]) -> dict[str, Any]:
    payload = task.get('payload') if isinstance(task, dict) else {}
    summary: dict[str, Any] = {
        'ok': bool(task.get('ok')) if isinstance(task, dict) else False,
        'returncode': int(task.get('returncode')) if isinstance(task, dict) and str(task.get('returncode') or '').isdigit() else task.get('returncode') if isinstance(task, dict) else None,
    }
    if isinstance(payload, dict):
        for key in ['candidate_count', 'group_count', 'filters']:
            if key in payload:
                summary[key] = payload.get(key)
    persisted_paths = task.get('persisted_paths') if isinstance(task, dict) else None
    if isinstance(persisted_paths, dict):
        summary['persisted_paths'] = persisted_paths
    stderr = str(task.get('stderr') or '') if isinstance(task, dict) else ''
    if stderr:
        summary['stderr_tail'] = stderr[-500:]
    return summary


def update_heartbeat_for_periodic_tasks(heartbeat: dict[str, Any], periodic_tasks: dict[str, Any]) -> dict[str, Any]:
    if 'resolution_sync' in periodic_tasks:
        heartbeat['last_resolution_sync'] = {
            'attempted_at': utc_now_iso(),
            **periodic_task_brief(periodic_tasks['resolution_sync']),
        }
        if periodic_tasks['resolution_sync'].get('ok'):
            heartbeat['last_resolution_sync']['succeeded_at'] = utc_now_iso()
    if 'brier_snapshot' in periodic_tasks:
        heartbeat['last_brier_snapshot'] = {
            'attempted_at': utc_now_iso(),
            **periodic_task_brief(periodic_tasks['brier_snapshot']),
        }
        if periodic_tasks['brier_snapshot'].get('ok'):
            heartbeat['last_brier_snapshot']['succeeded_at'] = utc_now_iso()
    return heartbeat


def update_heartbeat_for_pass(heartbeat: dict[str, Any], *, result: dict[str, Any], processed_cases: int, periodic_tasks: dict[str, Any], excluded_case_keys: set[str], excluded_market_ids: set[str]) -> dict[str, Any]:
    case_key, market_id = extract_case_market_refs(result)
    prior_activity = heartbeat.pop('current_activity', None)
    if isinstance(prior_activity, dict) and prior_activity:
        heartbeat['last_activity'] = prior_activity
    heartbeat['state'] = 'running'
    heartbeat['processed_cases_total'] = processed_cases
    heartbeat['last_loop_completed_at'] = utc_now_iso()
    heartbeat['last_pass'] = {
        'status': str(result.get('status') or ''),
        'ok': bool(result.get('ok')),
        'soft_failed': bool(result.get('soft_failed')),
        'case_key': case_key,
        'market_id': market_id,
        'periodic_tasks_ran': sorted(list(periodic_tasks.keys())),
    }
    heartbeat['quarantine_count'] = len(excluded_case_keys) + len(excluded_market_ids)
    heartbeat['active_quarantines'] = {
        'case_keys': sorted(excluded_case_keys),
        'market_ids': sorted(excluded_market_ids),
    }
    if not result.get('ok'):
        heartbeat['last_hard_failure'] = {
            'at': utc_now_iso(),
            'status': str(result.get('status') or result.get('error') or 'unknown_failure'),
            'case_key': case_key,
            'market_id': market_id,
        }
    elif result.get('soft_failed'):
        heartbeat['last_soft_failure'] = {
            'at': utc_now_iso(),
            'status': str(result.get('status') or ''),
            'case_key': case_key,
            'market_id': market_id,
        }
    return update_heartbeat_for_periodic_tasks(heartbeat, periodic_tasks)


def maybe_quarantine_failed_result(*, args: Any, result: dict[str, Any]) -> dict[str, Any] | None:
    if bool(result.get('ok')):
        return None
    if not is_soft_fail_status(result) and not result.get('refresh_candidate'):
        return None
    case_key, market_id = extract_case_market_refs(result)
    if not case_key and not market_id:
        return None
    reason = str(result.get('status') or result.get('error') or 'soft_fail')
    entry = record_quarantine_entry(
        Path(args.quarantine_file).expanduser().resolve(),
        case_key=case_key,
        market_id=market_id,
        reason=reason,
        result=result,
        quarantine_seconds=float(args.quarantine_seconds),
    )
    if case_key:
        update_case_pipeline_status(
            case_key=case_key,
            status='pipeline_failed',
            current_stage=str((((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary') or {}).get('current_stage') if isinstance((((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary')), dict) else 'decision'),
            runner_id='run_sequential_market_pipeline',
            message='Sequential runner soft-failed and quarantined the case for later retry',
            extra={'quarantine': entry, 'soft_failed_result_status': result.get('status', '')},
            terminal_summary_patch={'failure_reason': reason, 'quarantined': True},
        )
    return entry
