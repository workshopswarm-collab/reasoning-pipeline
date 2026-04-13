from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from automation_control import load_control_file, resolve_sequencer_policy
from automation_runtime_support import exclusive_lock
from pipeline_automation_actions import manual_launch_case, manual_launch_market, manual_launch_next, run_light_refresh_update
from pipeline_sequencer_candidates import classify_prepare_failure, decide_refresh_mode, select_refresh_case, select_resumable_case

REFRESH_WATERMARK_PATH = Path(__file__).resolve().parent / '.runtime-state' / 'refresh-watermarks.json'
STAGE_RETRY_REGISTRY_PATH = Path(__file__).resolve().parent / '.runtime-state' / 'stage-launch-retries.json'
REFRESH_RETRIGGER_THRESHOLD = 0.02
DEFER_RETRY_BUDGET = 3
DEFER_RETRY_SLEEP_SECONDS = 10.0
from pipeline_sequencer_periodic import maybe_run_periodic_tasks
from pipeline_sequencer_progress import TERMINAL_PIPELINE_STATUSES, wait_for_case
from pipeline_sequencer_state import (
    active_quarantine_sets,
    heartbeat_base,
    load_quarantine_registry,
    maybe_quarantine_failed_result,
    prune_quarantine_entries,
    save_quarantine_registry,
    update_heartbeat_activity,
    update_heartbeat_for_pass,
    utc_now_iso,
    write_heartbeat,
)


def effective_sequencer_policy(args: Any) -> dict[str, Any]:
    policy = {
        'enabled': True,
        'resume_existing': bool(args.resume_existing),
        'allow_new_case_claims': True,
        'poll_seconds': float(args.poll_seconds),
        'idle_seconds': float(args.idle_seconds),
        'max_case_seconds': float(args.max_case_seconds),
        'control_managed': bool(args.control_managed),
        'control_file': str(Path(args.control_file).expanduser().resolve()),
    }
    if args.control_managed:
        control_path = Path(args.control_file).expanduser().resolve()
        control = load_control_file(control_path)
        control_policy = resolve_sequencer_policy(control)
        policy.update({
            'enabled': bool(control_policy.get('enabled')),
            'resume_existing': bool(control_policy.get('resume_existing')),
            'allow_new_case_claims': bool(control_policy.get('allow_new_case_claims')),
            'poll_seconds': float(control_policy.get('poll_seconds')),
            'idle_seconds': float(control_policy.get('idle_seconds')),
            'max_case_seconds': float(control_policy.get('max_case_seconds')),
            'control_snapshot': control,
            'automation_enabled': bool(control_policy.get('automation_enabled')),
        })
    return policy


DEFERABLE_NONTERMINAL_CASE_ERRORS = {
    'watchdog_reconcile_failed',
    'watchdog_action_failed',
}


def _parse_iso_datetime(value: str) -> datetime | None:
    text = str(value or '').strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text.replace('Z', '+00:00'))
    except ValueError:
        return None


def case_runtime_age_seconds(summary: dict[str, Any]) -> float | None:
    started_at = _parse_iso_datetime(str(summary.get('started_at') or ''))
    if started_at is None:
        return None
    if started_at.tzinfo is None:
        started_at = started_at.replace(tzinfo=timezone.utc)
    return max(0.0, (datetime.now(timezone.utc) - started_at.astimezone(timezone.utc)).total_seconds())


def should_defer_nonterminal_case_result(case_result: dict[str, Any], *, policy: dict[str, Any]) -> bool:
    if bool(case_result.get('ok')):
        return False
    error = str(case_result.get('error') or '').strip()
    if error not in DEFERABLE_NONTERMINAL_CASE_ERRORS:
        return False
    pipeline_summary = case_result.get('pipeline_summary') if isinstance(case_result.get('pipeline_summary'), dict) else {}
    pipeline_status = str(pipeline_summary.get('status') or '').strip()
    if not pipeline_status or pipeline_status in TERMINAL_PIPELINE_STATUSES:
        return False
    age_seconds = case_runtime_age_seconds(pipeline_summary)
    max_case_seconds = float(policy.get('max_case_seconds') or 0.0)
    if age_seconds is not None and max_case_seconds > 0.0 and age_seconds > max_case_seconds:
        return False
    return True


def load_stage_retry_registry(path: Path | None = None) -> dict[str, Any]:
    path = path or STAGE_RETRY_REGISTRY_PATH
    if not path.exists():
        return {'schema_version': 'pipeline-stage-retries/v1', 'entries': {}, 'updated_at': ''}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {'schema_version': 'pipeline-stage-retries/v1', 'entries': {}, 'updated_at': ''}
    if not isinstance(payload, dict):
        return {'schema_version': 'pipeline-stage-retries/v1', 'entries': {}, 'updated_at': ''}
    entries = payload.get('entries') if isinstance(payload.get('entries'), dict) else {}
    return {'schema_version': 'pipeline-stage-retries/v1', 'entries': entries, 'updated_at': str(payload.get('updated_at') or '')}


def save_stage_retry_registry(payload: dict[str, Any], path: Path | None = None) -> None:
    path = path or STAGE_RETRY_REGISTRY_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    payload['updated_at'] = utc_now_iso()
    path.write_text(json.dumps(payload, indent=2) + '\n')


def clear_case_stage_retries(case_key: str, path: Path | None = None) -> None:
    path = path or STAGE_RETRY_REGISTRY_PATH
    normalized_case_key = str(case_key or '').strip()
    if not normalized_case_key:
        return
    payload = load_stage_retry_registry(path)
    entries = payload.get('entries') if isinstance(payload.get('entries'), dict) else {}
    payload['entries'] = {
        key: value for key, value in entries.items()
        if str((value or {}).get('case_key') or '').strip() != normalized_case_key
    }
    save_stage_retry_registry(payload, path)


def stage_retry_identity(case_result: dict[str, Any]) -> dict[str, Any]:
    pipeline_summary = case_result.get('pipeline_summary') if isinstance(case_result.get('pipeline_summary'), dict) else {}
    watchdog_result = case_result.get('watchdog_result') if isinstance(case_result.get('watchdog_result'), dict) else {}
    action_failures = watchdog_result.get('action_failures') if isinstance(watchdog_result.get('action_failures'), list) else []
    first_failure = action_failures[0] if action_failures else {}
    action_name = str((first_failure.get('name') if isinstance(first_failure, dict) else '') or '').strip()
    stage_name = str(pipeline_summary.get('current_stage') or '').strip() or 'unknown'
    case_key = str(pipeline_summary.get('case_key') or case_result.get('case_key') or '').strip()
    return {
        'case_key': case_key,
        'stage': stage_name,
        'action_name': action_name,
        'error': str(case_result.get('error') or '').strip(),
    }


def classify_nonterminal_case_result(case_result: dict[str, Any], *, policy: dict[str, Any]) -> dict[str, Any]:
    if not should_defer_nonterminal_case_result(case_result, policy=policy):
        return {'mode': 'none'}
    identity = stage_retry_identity(case_result)
    payload = load_stage_retry_registry()
    entries = payload.setdefault('entries', {})
    case_key = str(identity.get('case_key') or '').strip()
    stage_name = str(identity.get('stage') or '').strip() or 'unknown'
    action_name = str(identity.get('action_name') or '').strip() or 'unknown_action'
    key = f'{case_key}:{stage_name}:{action_name}'
    entry = entries.get(key) if isinstance(entries.get(key), dict) else {}
    attempts = int(entry.get('attempts') or 0) + 1
    budget = int(policy.get('defer_retry_budget') or DEFER_RETRY_BUDGET)
    pipeline_summary = case_result.get('pipeline_summary') if isinstance(case_result.get('pipeline_summary'), dict) else {}
    age_seconds = case_runtime_age_seconds(pipeline_summary)
    next_entry = {
        'case_key': case_key,
        'stage': stage_name,
        'action_name': action_name,
        'error': str(identity.get('error') or ''),
        'attempts': attempts,
        'first_seen_at': str(entry.get('first_seen_at') or utc_now_iso()),
        'last_seen_at': utc_now_iso(),
        'runtime_age_seconds': age_seconds,
    }
    entries[key] = next_entry
    save_stage_retry_registry(payload)
    if attempts > budget:
        return {
            'mode': 'stuck',
            'retry_entry': next_entry,
            'retry_budget': budget,
        }
    return {
        'mode': 'defer',
        'retry_entry': next_entry,
        'retry_budget': budget,
    }


def assert_sequencer_launch_boundary(*, prepare_result: dict[str, Any], mode: str) -> None:
    payload = prepare_result.get('payload') if isinstance(prepare_result.get('payload'), dict) else {}
    prepared = payload.get('prepare_result') if isinstance(payload.get('prepare_result'), dict) else {}
    case_payload = prepared.get('case') if isinstance(prepared.get('case'), dict) else {}
    case_key = str(case_payload.get('case_key') or case_payload.get('case_id') or '').strip()
    if not case_key:
        raise RuntimeError(f'sequencer launch boundary violation ({mode}): canonical launch path returned no case key')



def recover_case_after_launch_timeout(*, args: Any, policy: dict[str, Any], excluded_case_keys: set[str], excluded_market_ids: set[str], pretty: bool, status_label: str) -> dict[str, Any] | None:
    resumable = select_resumable_case(excluded_case_keys=excluded_case_keys, excluded_market_ids=excluded_market_ids)
    if not resumable:
        return None
    case_key = str(resumable.get('case_key') or '').strip()
    if not case_key:
        return None
    case_result = wait_for_case(
        case_key,
        args=args,
        poll_seconds=float(policy['poll_seconds']),
        max_case_seconds=float(policy['max_case_seconds']),
        pretty=pretty,
    )
    return {
        'ok': bool(case_result.get('ok')),
        'status': status_label,
        'policy': policy,
        'case_key': case_key,
        'case_result': case_result,
        'launch_timeout_recovered': True,
    }



def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')



def load_refresh_watermarks(path: Path = REFRESH_WATERMARK_PATH) -> dict[str, Any]:
    if not path.exists():
        return {'entries': {}, 'updated_at': ''}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {'entries': {}, 'updated_at': ''}
    if not isinstance(payload, dict):
        return {'entries': {}, 'updated_at': ''}
    entries = payload.get('entries') if isinstance(payload.get('entries'), dict) else {}
    return {'entries': entries, 'updated_at': str(payload.get('updated_at') or '')}



def save_refresh_watermarks(payload: dict[str, Any], path: Path = REFRESH_WATERMARK_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload['updated_at'] = utc_now_iso()
    path.write_text(json.dumps(payload, indent=2) + '\n')



def refresh_watermark_key(refresh_payload: dict[str, Any]) -> str:
    market_id = str(refresh_payload.get('market_id') or '').strip()
    contract_id = str(refresh_payload.get('contract_id') or '').strip()
    if market_id and contract_id:
        return f'{market_id}:{contract_id}'
    if market_id:
        return market_id
    return str(refresh_payload.get('case_key') or refresh_payload.get('latest_forecast_case_key') or '').strip()



def should_retrigger_refresh(*, refresh_payload: dict[str, Any], watermark_entry: dict[str, Any] | None) -> bool:
    if not watermark_entry:
        return True
    try:
        current_price = float(refresh_payload.get('current_price'))
        trigger_price = float(watermark_entry.get('trigger_market_price'))
    except Exception:
        return True
    incremental_move = abs(current_price - trigger_price)
    return incremental_move >= REFRESH_RETRIGGER_THRESHOLD



def record_refresh_watermark(*, refresh_payload: dict[str, Any], refresh_plan: dict[str, Any], refresh_case_key: str, light_refresh_result: dict[str, Any] | None = None) -> None:
    key = refresh_watermark_key(refresh_payload)
    if not key:
        return
    payload = load_refresh_watermarks()
    entries = payload.setdefault('entries', {})
    entry = {
        'case_key': refresh_case_key,
        'market_id': str(refresh_payload.get('market_id') or ''),
        'contract_id': str(refresh_payload.get('contract_id') or ''),
        'trigger_market_price': refresh_payload.get('current_price'),
        'trigger_reasoned_price': refresh_payload.get('last_reasoned_price'),
        'trigger_delta': refresh_payload.get('price_delta'),
        'trigger_delta_pct_points': refresh_payload.get('price_delta_pct_points'),
        'refresh_mode': str(refresh_plan.get('mode') or ''),
        'refresh_reasons': refresh_plan.get('reasons') or [],
        'triggered_at': utc_now_iso(),
    }
    if isinstance(light_refresh_result, dict):
        result_payload = light_refresh_result.get('payload') if isinstance(light_refresh_result.get('payload'), dict) else light_refresh_result
        if isinstance(result_payload, dict):
            entry['completed_refresh_id'] = str(result_payload.get('refresh_id') or '')
    entries[key] = entry
    save_refresh_watermarks(payload)



def build_refresh_detected_marker(*, refresh_payload: dict[str, Any], refresh_plan: dict[str, Any]) -> str:
    case_key = str(refresh_payload.get('case_key') or refresh_payload.get('latest_forecast_case_key') or '').strip()
    market_title = str(refresh_payload.get('market_title') or refresh_payload.get('title') or '').strip()
    mode = str(refresh_plan.get('mode') or '').strip() or 'full'
    reasons = ','.join(str(item) for item in (refresh_plan.get('reasons') or []) if str(item).strip())
    delta = refresh_payload.get('price_delta_pct_points')
    if delta is None:
        raw_delta = refresh_payload.get('price_delta')
        try:
            delta = round(float(raw_delta) * 100.0, 3) if raw_delta is not None else ''
        except Exception:
            delta = ''
    return f"MATERIAL CHANGE DETECTED | case={case_key} | market={market_title} | refresh_mode={mode} | delta_pct_points={delta} | reasons={reasons}"



def run_sequencer_pass(
    args: Any,
    policy: dict[str, Any],
    *,
    excluded_case_keys: set[str],
    excluded_market_ids: set[str],
    progress_callback: Any | None = None,
) -> dict[str, Any]:
    if not policy.get('enabled', True):
        return {
            'ok': True,
            'status': 'sequencer_disabled',
            'policy': policy,
        }

    resumable = select_resumable_case(excluded_case_keys=excluded_case_keys, excluded_market_ids=excluded_market_ids) if policy.get('resume_existing') else None
    if resumable:
        case_key = str(resumable.get('case_key') or '').strip()
        if not case_key:
            raise RuntimeError('resumable pipeline status is missing case_key')
        if progress_callback is not None:
            progress_callback(
                phase='resume_existing_case',
                message='Resuming existing in-flight case',
                case_key=case_key,
                market_id=str(resumable.get('market_id') or '').strip(),
                dispatch_id=str(resumable.get('dispatch_id') or '').strip(),
                details={'mode': 'resume_existing'},
            )
        case_result = wait_for_case(
            case_key,
            args=args,
            poll_seconds=float(policy['poll_seconds']),
            max_case_seconds=float(policy['max_case_seconds']),
            pretty=args.pretty,
            progress_callback=progress_callback,
        )
        handling = classify_nonterminal_case_result(case_result, policy=policy)
        if handling.get('mode') == 'defer':
            pipeline_summary = case_result.get('pipeline_summary') if isinstance(case_result.get('pipeline_summary'), dict) else {}
            return {
                'ok': True,
                'status': 'existing_case_deferred',
                'policy': policy,
                'case_key': case_key,
                'case_result': case_result,
                'deferred_error': str(case_result.get('error') or ''),
                'deferred_because_nonterminal': True,
                'deferred_runtime_age_seconds': case_runtime_age_seconds(pipeline_summary),
                'retry_budget': handling.get('retry_budget'),
                'retry_entry': handling.get('retry_entry'),
            }
        if handling.get('mode') == 'stuck':
            return {
                'ok': False,
                'status': 'stage_launch_stuck',
                'policy': policy,
                'case_key': case_key,
                'case_result': case_result,
                'stuck_reason': str(case_result.get('error') or ''),
                'retry_budget': handling.get('retry_budget'),
                'retry_entry': handling.get('retry_entry'),
            }
        return {
            'ok': bool(case_result.get('ok')),
            'status': 'processed_existing_case',
            'policy': policy,
            'case_key': case_key,
            'case_result': case_result,
        }

    refresh_candidate = select_refresh_case(
        pretty=args.pretty,
        excluded_market_ids=excluded_market_ids,
        excluded_case_keys=excluded_case_keys,
    )
    if refresh_candidate.get('ok'):
        refresh_payload = refresh_candidate.get('payload') or {}
        refresh_plan = decide_refresh_mode(refresh_payload)
        refresh_mode = str(refresh_plan.get('mode') or 'light')

        if refresh_mode == 'light':
            watermark_payload = load_refresh_watermarks()
            watermark_entry = watermark_payload.get('entries', {}).get(refresh_watermark_key(refresh_payload))
            if not should_retrigger_refresh(refresh_payload=refresh_payload, watermark_entry=watermark_entry):
                return {
                    'ok': True,
                    'status': 'debounced_light_refresh_candidate',
                    'policy': policy,
                    'refresh_candidate': refresh_candidate,
                    'refresh_plan': refresh_plan,
                    'watermark_entry': watermark_entry,
                    'retrigger_threshold': REFRESH_RETRIGGER_THRESHOLD,
                }
            refresh_case_key = str(refresh_payload.get('case_key') or refresh_payload.get('latest_forecast_case_key') or '').strip()
            if not refresh_case_key:
                return {
                    'ok': False,
                    'status': 'light_refresh_missing_case_key',
                    'policy': policy,
                    'refresh_candidate': refresh_candidate,
                    'refresh_plan': refresh_plan,
                }
            if progress_callback is not None:
                progress_callback(
                    phase='light_refresh',
                    message='Running light refresh for an already-decided case',
                    case_key=refresh_case_key,
                    market_id=str(refresh_payload.get('market_id') or '').strip(),
                    details={
                        'mode': refresh_mode,
                        'reasons': [str(item) for item in (refresh_plan.get('reasons') or []) if str(item).strip()],
                    },
                )
            light_refresh_result = run_light_refresh_update(refresh_case_key, pretty=args.pretty)
            if light_refresh_result.get('ok'):
                record_refresh_watermark(
                    refresh_payload=refresh_payload,
                    refresh_plan=refresh_plan,
                    refresh_case_key=refresh_case_key,
                    light_refresh_result=light_refresh_result,
                )
            return {
                'ok': bool(light_refresh_result.get('ok')),
                'status': 'processed_light_refresh_case',
                'policy': policy,
                'case_key': refresh_case_key,
                'refresh_candidate': refresh_candidate,
                'refresh_plan': refresh_plan,
                'light_refresh_result': light_refresh_result,
            }

        refresh_case_id = str(refresh_payload.get('case_id') or '').strip()
        refresh_case_key = str(refresh_payload.get('case_key') or '').strip()
        refresh_reasons = [str(item) for item in (refresh_plan.get('reasons') or []) if str(item).strip()]
        refresh_price_delta_pct_points = ''
        if refresh_payload.get('price_delta_pct_points') is not None:
            refresh_price_delta_pct_points = str(refresh_payload.get('price_delta_pct_points'))
        elif refresh_payload.get('price_delta') is not None:
            try:
                refresh_price_delta_pct_points = str(round(float(refresh_payload.get('price_delta')) * 100.0, 3))
            except Exception:
                refresh_price_delta_pct_points = ''
        refresh_detected_marker = build_refresh_detected_marker(refresh_payload=refresh_payload, refresh_plan=refresh_plan)
        if progress_callback is not None:
            progress_callback(
                phase='prepare_refresh_launch',
                message='Preparing full-refresh launch for a material-change case',
                case_key=refresh_case_key,
                market_id=str(refresh_payload.get('market_id') or '').strip(),
                details={
                    'mode': refresh_mode,
                    'reasons': refresh_reasons,
                    'price_delta_pct_points': refresh_price_delta_pct_points,
                },
            )
        if refresh_case_id:
            prepared = manual_launch_case(
                refresh_case_id,
                pretty=args.pretty,
                refresh_mode=refresh_mode,
                refresh_reasons=refresh_reasons,
                refresh_price_delta_pct_points=refresh_price_delta_pct_points,
                refresh_detected_marker=refresh_detected_marker,
            )
        else:
            prepared = manual_launch_market(
                str(refresh_payload.get('market_id') or '').strip(),
                pretty=args.pretty,
                refresh_mode=refresh_mode,
                refresh_reasons=refresh_reasons,
                refresh_price_delta_pct_points=refresh_price_delta_pct_points,
                refresh_detected_marker=refresh_detected_marker,
            )
        if not prepared:
            return {
                'ok': False,
                'status': 'prepare_unknown_failure',
                'policy': policy,
                'refresh_candidate': refresh_candidate,
                'refresh_plan': refresh_plan,
            }
        payload = prepared.get('payload') or {}
        if not prepared.get('ok'):
            failure_kind = classify_prepare_failure(prepared)
            if failure_kind == 'prepare_launch_timed_out':
                recovered = recover_case_after_launch_timeout(
                    args=args,
                    policy=policy,
                    excluded_case_keys=excluded_case_keys,
                    excluded_market_ids=excluded_market_ids,
                    pretty=args.pretty,
                    status_label='processed_refresh_case_after_launch_timeout',
                )
                if recovered is not None:
                    recovered.update({
                        'refresh_candidate': refresh_candidate,
                        'refresh_plan': refresh_plan,
                        'prepare_result': prepared,
                    })
                    return recovered
            if failure_kind == 'open_case_failed':
                failure_kind = 'refresh_open_case_failed'
            return {
                'ok': failure_kind in {'idle_pipeline_busy', 'idle_no_eligible_market'},
                'status': failure_kind,
                'policy': policy,
                'refresh_candidate': refresh_candidate,
                'refresh_plan': refresh_plan,
                'prepare_result': prepared,
            }

        assert_sequencer_launch_boundary(prepare_result=prepared, mode='full_refresh')
        prepare_result = payload.get('prepare_result') or {}
        case_payload = prepare_result.get('case') or {}
        case_key = str(case_payload.get('case_key') or refresh_case_key or case_payload.get('case_id') or '').strip()
        if not case_key:
            raise RuntimeError('refresh prepare_and_launch did not return a case_key')

        if progress_callback is not None:
            progress_callback(
                phase='monitor_refresh_case',
                message='Refresh launch completed; monitoring case execution',
                case_key=case_key,
                market_id=str(refresh_payload.get('market_id') or '').strip(),
                dispatch_id=str(case_payload.get('dispatch_id') or '').strip(),
                details={'mode': refresh_mode},
            )
        case_result = wait_for_case(
            case_key,
            args=args,
            poll_seconds=float(policy['poll_seconds']),
            max_case_seconds=float(policy['max_case_seconds']),
            pretty=args.pretty,
            progress_callback=progress_callback,
        )
        handling = classify_nonterminal_case_result(case_result, policy=policy)
        if handling.get('mode') == 'defer':
            pipeline_summary = case_result.get('pipeline_summary') if isinstance(case_result.get('pipeline_summary'), dict) else {}
            return {
                'ok': True,
                'status': 'refresh_case_deferred',
                'policy': policy,
                'case_key': case_key,
                'refresh_candidate': refresh_candidate,
                'refresh_plan': refresh_plan,
                'prepare_result': prepared,
                'case_result': case_result,
                'deferred_error': str(case_result.get('error') or ''),
                'deferred_because_nonterminal': True,
                'deferred_runtime_age_seconds': case_runtime_age_seconds(pipeline_summary),
                'retry_budget': handling.get('retry_budget'),
                'retry_entry': handling.get('retry_entry'),
            }
        if handling.get('mode') == 'stuck':
            return {
                'ok': False,
                'status': 'stage_launch_stuck',
                'policy': policy,
                'case_key': case_key,
                'refresh_candidate': refresh_candidate,
                'refresh_plan': refresh_plan,
                'prepare_result': prepared,
                'case_result': case_result,
                'stuck_reason': str(case_result.get('error') or ''),
                'retry_budget': handling.get('retry_budget'),
                'retry_entry': handling.get('retry_entry'),
            }
        return {
            'ok': bool(case_result.get('ok')),
            'status': 'processed_refresh_case',
            'policy': policy,
            'case_key': case_key,
            'refresh_candidate': refresh_candidate,
            'refresh_plan': refresh_plan,
            'prepare_result': prepared,
            'case_result': case_result,
        }

    if not policy.get('allow_new_case_claims', False):
        return {
            'ok': True,
            'status': 'claims_disabled_idle',
            'policy': policy,
        }

    if progress_callback is not None:
        progress_callback(
            phase='prepare_new_launch',
            message='Preparing launch for the next eligible market',
            details={'mode': 'new_case'},
        )
    prepared = manual_launch_next(pretty=args.pretty)
    if not prepared:
        return {
            'ok': False,
            'status': 'prepare_unknown_failure',
            'policy': policy,
        }

    payload = prepared.get('payload') or {}
    if not prepared.get('ok'):
        failure_kind = classify_prepare_failure(prepared)
        if failure_kind == 'prepare_launch_timed_out':
            recovered = recover_case_after_launch_timeout(
                args=args,
                policy=policy,
                excluded_case_keys=excluded_case_keys,
                excluded_market_ids=excluded_market_ids,
                pretty=args.pretty,
                status_label='processed_new_case_after_launch_timeout',
            )
            if recovered is not None:
                recovered['prepare_result'] = prepared
                return recovered
        idle = failure_kind in {'idle_pipeline_busy', 'idle_no_eligible_market'}
        return {
            'ok': idle,
            'status': failure_kind,
            'policy': policy,
            'prepare_result': prepared,
        }

    assert_sequencer_launch_boundary(prepare_result=prepared, mode='new_case')
    prepare_result = payload.get('prepare_result') or {}
    case_payload = prepare_result.get('case') or {}
    case_key = str(case_payload.get('case_key') or case_payload.get('case_id') or '').strip()
    if not case_key:
        raise RuntimeError('prepare_and_launch did not return a case_key')

    if progress_callback is not None:
        progress_callback(
            phase='monitor_new_case',
            message='New case launched; monitoring pipeline progress',
            case_key=case_key,
            market_id=str(case_payload.get('market_id') or '').strip(),
            dispatch_id=str(case_payload.get('dispatch_id') or '').strip(),
            details={'mode': 'new_case'},
        )
    case_result = wait_for_case(
        case_key,
        args=args,
        poll_seconds=float(policy['poll_seconds']),
        max_case_seconds=float(policy['max_case_seconds']),
        pretty=args.pretty,
        progress_callback=progress_callback,
    )
    handling = classify_nonterminal_case_result(case_result, policy=policy)
    if handling.get('mode') == 'defer':
        pipeline_summary = case_result.get('pipeline_summary') if isinstance(case_result.get('pipeline_summary'), dict) else {}
        return {
            'ok': True,
            'status': 'new_case_deferred',
            'policy': policy,
            'case_key': case_key,
            'prepare_result': prepared,
            'case_result': case_result,
            'deferred_error': str(case_result.get('error') or ''),
            'deferred_because_nonterminal': True,
            'deferred_runtime_age_seconds': case_runtime_age_seconds(pipeline_summary),
            'retry_budget': handling.get('retry_budget'),
            'retry_entry': handling.get('retry_entry'),
        }
    if handling.get('mode') == 'stuck':
        return {
            'ok': False,
            'status': 'stage_launch_stuck',
            'policy': policy,
            'case_key': case_key,
            'prepare_result': prepared,
            'case_result': case_result,
            'stuck_reason': str(case_result.get('error') or ''),
            'retry_budget': handling.get('retry_budget'),
            'retry_entry': handling.get('retry_entry'),
        }
    return {
        'ok': bool(case_result.get('ok')),
        'status': 'processed_new_case',
        'policy': policy,
        'case_key': case_key,
        'prepare_result': prepared,
        'case_result': case_result,
    }


def should_count_processed(result: dict[str, Any]) -> bool:
    return bool(result.get('ok')) and not bool(result.get('soft_failed')) and str(result.get('status') or '') in {
        'processed_existing_case',
        'processed_new_case',
        'processed_refresh_case',
        'processed_light_refresh_case',
    }


def build_single_pass_summary(result: dict[str, Any]) -> dict[str, Any]:
    return {
        'ok': bool(result.get('ok')),
        'processed_cases': 1 if should_count_processed(result) else 0,
        'results': [result],
    }


def build_loop_pass_payload(result: dict[str, Any], processed_cases: int, periodic_tasks: dict[str, Any]) -> dict[str, Any]:
    return {
        'ok': bool(result.get('ok')),
        'processed_cases': processed_cases,
        'periodic_tasks': periodic_tasks,
        'pass_result': result,
    }


def sequencer_sleep_plan(result: dict[str, Any], *, policy: dict[str, Any], args: Any) -> dict[str, Any]:
    deferred = str(result.get('status') or '').endswith('_deferred')
    sleep_seconds = float(min(policy.get('poll_seconds', args.poll_seconds), DEFER_RETRY_SLEEP_SECONDS)) if deferred else float(policy.get('idle_seconds', args.idle_seconds))
    return {
        'deferred': deferred,
        'sleep_seconds': sleep_seconds,
        'heartbeat_state': 'deferred_retry_sleep' if deferred else 'idle_sleep',
    }


def execute_sequencer(args: Any) -> None:
    lock_path = Path(args.lock_file).expanduser().resolve()
    heartbeat_path = Path(args.heartbeat_file).expanduser().resolve()
    heartbeat = heartbeat_base(args)

    def progress_callback(*, phase: str, message: str = '', case_key: str = '', market_id: str = '', dispatch_id: str = '', details: dict[str, Any] | None = None) -> None:
        nonlocal heartbeat
        heartbeat = update_heartbeat_activity(
            heartbeat,
            phase=phase,
            message=message,
            case_key=case_key,
            market_id=market_id,
            dispatch_id=dispatch_id,
            details=details,
        )
        write_heartbeat(heartbeat_path, heartbeat)

    write_heartbeat(heartbeat_path, heartbeat)
    try:
        with exclusive_lock(lock_path, error_message=f'another sequencer instance already holds {lock_path}'):
            heartbeat['state'] = 'running'
            heartbeat['lock_acquired_at'] = utc_now_iso()
            write_heartbeat(heartbeat_path, heartbeat)

            if not args.loop:
                heartbeat['last_loop_started_at'] = utc_now_iso()
                write_heartbeat(heartbeat_path, heartbeat)
                result = run_sequencer_pass(args, effective_sequencer_policy(args), excluded_case_keys=set(), excluded_market_ids=set(), progress_callback=progress_callback)
                heartbeat = update_heartbeat_for_pass(
                    heartbeat,
                    result=result,
                    processed_cases=1 if should_count_processed(result) else 0,
                    periodic_tasks={},
                    excluded_case_keys=set(),
                    excluded_market_ids=set(),
                )
                heartbeat['state'] = 'completed' if result.get('ok') else 'failed'
                write_heartbeat(heartbeat_path, heartbeat)
                summary = build_single_pass_summary(result)
                print(json.dumps(summary, indent=2 if args.pretty else None))
                if not summary['ok']:
                    raise SystemExit(1)
                return

            processed = 0
            last_resolution_sync_ts: float | None = None
            last_brier_snapshot_ts: float | None = None
            quarantine_path = Path(args.quarantine_file).expanduser().resolve()
            while args.max_cases == 0 or processed < args.max_cases:
                policy = effective_sequencer_policy(args)
                now_ts = time.time()
                quarantine_payload = prune_quarantine_entries(load_quarantine_registry(quarantine_path), now_ts=now_ts)
                save_quarantine_registry(quarantine_path, quarantine_payload)
                excluded_case_keys, excluded_market_ids = active_quarantine_sets(quarantine_payload)
                heartbeat['state'] = 'running'
                heartbeat['last_loop_started_at'] = utc_now_iso()
                heartbeat['quarantine_count'] = len(quarantine_payload.get('entries') or [])
                heartbeat['active_quarantines'] = {
                    'case_keys': sorted(excluded_case_keys),
                    'market_ids': sorted(excluded_market_ids),
                }
                write_heartbeat(heartbeat_path, heartbeat)

                periodic_tasks, last_resolution_sync_ts, last_brier_snapshot_ts = maybe_run_periodic_tasks(
                    args=args,
                    now_ts=now_ts,
                    last_resolution_sync_ts=last_resolution_sync_ts,
                    last_brier_snapshot_ts=last_brier_snapshot_ts,
                )
                result = run_sequencer_pass(args, policy, excluded_case_keys=excluded_case_keys, excluded_market_ids=excluded_market_ids, progress_callback=progress_callback)
                quarantine_entry_payload = maybe_quarantine_failed_result(args=args, result=result)
                if quarantine_entry_payload is not None:
                    periodic_tasks['soft_fail_quarantine'] = quarantine_entry_payload
                    result['ok'] = True
                    result['soft_failed'] = True
                if should_count_processed(result):
                    processed += 1
                    resolved_case_key = str(result.get('case_key') or '')
                    if resolved_case_key:
                        clear_case_stage_retries(resolved_case_key)
                heartbeat = update_heartbeat_for_pass(
                    heartbeat,
                    result=result,
                    processed_cases=processed,
                    periodic_tasks=periodic_tasks,
                    excluded_case_keys=excluded_case_keys,
                    excluded_market_ids=excluded_market_ids,
                )
                write_heartbeat(heartbeat_path, heartbeat)
                print(json.dumps(build_loop_pass_payload(result, processed, periodic_tasks), indent=2 if args.pretty else None), flush=True)
                if not result.get('ok'):
                    heartbeat['state'] = 'failed'
                    write_heartbeat(heartbeat_path, heartbeat)
                    raise SystemExit(1)
                if should_count_processed(result):
                    continue
                sleep_plan = sequencer_sleep_plan(result, policy=policy, args=args)
                sleep_seconds = float(sleep_plan['sleep_seconds'])
                heartbeat['state'] = str(sleep_plan['heartbeat_state'])
                heartbeat['last_idle_sleep_started_at'] = utc_now_iso()
                heartbeat['last_idle_sleep_seconds'] = sleep_seconds
                if sleep_plan['deferred']:
                    heartbeat['last_deferred_retry'] = {
                        'at': utc_now_iso(),
                        'status': str(result.get('status') or ''),
                        'case_key': str(result.get('case_key') or ''),
                        'sleep_seconds': sleep_seconds,
                        'retry_budget': result.get('retry_budget'),
                        'retry_entry': result.get('retry_entry'),
                    }
                write_heartbeat(heartbeat_path, heartbeat)
                time.sleep(sleep_seconds)
    except SystemExit:
        raise
    except Exception as exc:
        heartbeat['state'] = 'failed'
        heartbeat['last_hard_failure'] = {
            'at': utc_now_iso(),
            'status': exc.__class__.__name__,
            'message': str(exc),
        }
        write_heartbeat(heartbeat_path, heartbeat)
        raise
    finally:
        if heartbeat.get('state') not in {'failed'}:
            heartbeat['state'] = 'stopped'
        heartbeat['stopped_at'] = utc_now_iso()
        write_heartbeat(heartbeat_path, heartbeat)
