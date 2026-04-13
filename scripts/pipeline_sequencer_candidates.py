from __future__ import annotations

from pathlib import Path
from typing import Any

from case_pipeline_status import list_case_pipeline_statuses
from pipeline_automation_actions import REPO_ROOT, run_python_script

SELECT_REFRESH_CASE = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'planner' / 'scripts' / 'select_refresh_case.py'
FULL_REFRESH_PRICE_DELTA = 0.12
FULL_REFRESH_STALE_HOURS = 12.0
FULL_REFRESH_CLOSE_HOURS = 12.0


def decide_refresh_mode(refresh_payload: dict[str, Any]) -> dict[str, Any]:
    try:
        price_delta = float(refresh_payload.get('price_delta')) if refresh_payload.get('price_delta') not in (None, '') else None
    except Exception:
        price_delta = None
    try:
        hours_since_last_forecast = float(refresh_payload.get('hours_since_last_forecast')) if refresh_payload.get('hours_since_last_forecast') not in (None, '') else None
    except Exception:
        hours_since_last_forecast = None
    try:
        hours_to_close = float(refresh_payload.get('hours_to_close')) if refresh_payload.get('hours_to_close') not in (None, '') else None
    except Exception:
        hours_to_close = None

    reasons: list[str] = []
    if price_delta is not None and price_delta >= FULL_REFRESH_PRICE_DELTA:
        reasons.append('large_price_move')
    if hours_since_last_forecast is not None and hours_since_last_forecast >= FULL_REFRESH_STALE_HOURS:
        reasons.append('stale_forecast')
    if hours_to_close is not None and hours_to_close <= FULL_REFRESH_CLOSE_HOURS:
        reasons.append('near_close')
    if reasons:
        return {'mode': 'full', 'reasons': reasons}
    return {'mode': 'light', 'reasons': ['material_price_move']}


def select_resumable_case(*, excluded_case_keys: set[str], excluded_market_ids: set[str]) -> dict[str, Any] | None:
    active = list_case_pipeline_statuses(include_terminal=False)
    for item in active:
        case_key = str(item.get('case_key') or '').strip()
        market_id = str(item.get('market_id') or '').strip()
        if case_key and case_key in excluded_case_keys:
            continue
        if market_id and market_id in excluded_market_ids:
            continue
        return item
    return None


def select_refresh_case(*, pretty: bool, excluded_market_ids: set[str], excluded_case_keys: set[str]) -> dict[str, Any]:
    args: list[str] = []
    for market_id in sorted(excluded_market_ids):
        args.extend(['--exclude-market-id', market_id])
    for case_key in sorted(excluded_case_keys):
        args.extend(['--exclude-case-key', case_key])
    return run_python_script(SELECT_REFRESH_CASE, *args, pretty=pretty)


def classify_prepare_failure(prepared: dict[str, Any] | None) -> str:
    if prepared is None:
        return 'prepare_unknown_failure'
    manual_status = str(prepared.get('manual_status') or '').strip()
    if manual_status == 'open_case_failed':
        return 'open_case_failed'
    payload = prepared.get('payload') or {}
    combined = '\n'.join([
        manual_status,
        str(payload.get('status') or ''),
        str((payload.get('prepare_result') or {}).get('status') or ''),
        str(prepared.get('stdout') or ''),
        str(prepared.get('stderr') or ''),
        str(payload.get('prepare_stdout') or ''),
        str(payload.get('prepare_stderr') or ''),
    ]).lower()
    if 'pipeline already busy with an open researching case' in combined:
        return 'idle_pipeline_busy'
    if 'no eligible market found' in combined:
        return 'idle_no_eligible_market'
    if 'command timed out after' in combined or 'status\': \'timeout' in combined or 'status": "timeout' in combined:
        return 'prepare_launch_timed_out'
    return 'prepare_launch_failed'
