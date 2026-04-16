#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
WORKSPACE_ROOT = SCRIPT_PATH.parents[4]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.lmd_causal_runtime import TRIGGER_RETRY_QUEUE_PATH, now_iso, read_json_lines, write_json_lines  # noqa: E402

RUN_POST_TREATMENT = SCRIPT_PATH.parent / 'run_post_treatment_causal_feedback_cycle.py'
POST_TREATMENT_REPORT_JSON = WORKSPACE_ROOT / 'qualitative-db' / '60-causal-map' / 'generated' / 'post-treatment-feedback-cycle.json'

COUNT_LMD_SQL = r'''
SELECT COUNT(*)::int AS count
FROM public.lmd_bundle_exposures e
WHERE e.case_key = NULLIF(:'case_key', '')
  AND (NULLIF(:'dispatch_id', '') IS NULL OR e.dispatch_id = NULLIF(:'dispatch_id', ''));
'''

COUNT_TRIAL_SQL = r'''
SELECT COUNT(*)::int AS count
FROM public.proposed_causal_trial_exposures e
WHERE e.case_key = NULLIF(:'case_key', '')
  AND (NULLIF(:'dispatch_id', '') IS NULL OR e.dispatch_id = NULLIF(:'dispatch_id', ''));
'''

COUNT_RESOLVED_SQL = r'''
SELECT COUNT(*)::int AS count
FROM public.learning_case_reviews r
WHERE r.case_key = NULLIF(:'case_key', '')
  AND COALESCE(r.resolution_status, '') = 'resolved';
'''

LATEST_LMD_SQL = r'''
SELECT json_build_object('latest_at', COALESCE(MAX(e.created_at)::text, ''))::text
FROM public.lmd_bundle_exposures e
WHERE e.case_key = NULLIF(:'case_key', '')
  AND (NULLIF(:'dispatch_id', '') IS NULL OR e.dispatch_id = NULLIF(:'dispatch_id', ''));
'''

LATEST_TRIAL_SQL = r'''
SELECT json_build_object('latest_at', COALESCE(MAX(e.created_at)::text, ''))::text
FROM public.proposed_causal_trial_exposures e
WHERE e.case_key = NULLIF(:'case_key', '')
  AND (NULLIF(:'dispatch_id', '') IS NULL OR e.dispatch_id = NULLIF(:'dispatch_id', ''));
'''

LATEST_REVIEW_SQL = r'''
SELECT json_build_object('latest_at', COALESCE(MAX(COALESCE(r.updated_at, r.created_at))::text, ''))::text
FROM public.learning_case_reviews r
WHERE r.case_key = NULLIF(:'case_key', '')
  AND COALESCE(r.resolution_status, '') = 'resolved';
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Conditionally trigger the post-treatment causal feedback cycle for one case/dispatch')
    parser.add_argument('--case-key', required=True)
    parser.add_argument('--dispatch-id', default='')
    parser.add_argument('--trigger-source', default='manual')
    parser.add_argument('--repair-missing-logs', action='store_true')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def coerce_string(value: Any) -> str:
    if value is None:
        return ''
    return str(value).strip()



def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return int(default)



def parse_iso(value: Any) -> datetime | None:
    text = coerce_string(value)
    if not text:
        return None
    if text.endswith('Z'):
        text = text[:-1] + '+00:00'
    try:
        parsed = datetime.fromisoformat(text)
    except Exception:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)



def extract_count(payload: Any) -> int:
    if isinstance(payload, dict):
        return safe_int(payload.get('count'))
    return safe_int(payload)



def extract_text(payload: Any, key: str) -> str:
    if isinstance(payload, dict):
        return coerce_string(payload.get(key))
    return coerce_string(payload)



def query_count(psql_bin: str, db_url: str, sql: str, params: dict[str, str]) -> int:
    return extract_count(exec_sql(psql_bin, db_url, sql, params) or 0)



def query_latest_at(psql_bin: str, db_url: str, sql: str, params: dict[str, str]) -> str | None:
    text = extract_text(exec_sql(psql_bin, db_url, sql, params) or {}, 'latest_at')
    return text or None



def load_existing_report_state(*, case_key: str, dispatch_id: str) -> dict[str, Any]:
    report_path = POST_TREATMENT_REPORT_JSON
    state: dict[str, Any] = {
        'report_path': str(report_path),
        'report_exists': report_path.exists(),
        'report_parse_error': False,
        'report_generated_at': None,
        'case_present': False,
        'dispatch_present': False,
    }
    if not report_path.exists():
        return state
    try:
        report = json.loads(report_path.read_text(encoding='utf-8'))
    except Exception:
        state['report_parse_error'] = True
        return state

    summary = report.get('summary') if isinstance(report, dict) and isinstance(report.get('summary'), dict) else {}
    state['report_generated_at'] = coerce_string(summary.get('generated_at')) or None

    audits = report.get('audits') if isinstance(report, dict) and isinstance(report.get('audits'), list) else []
    dispatch_present = not dispatch_id
    case_present = False
    for audit in audits:
        if not isinstance(audit, dict):
            continue
        if coerce_string(audit.get('case_key')) != case_key:
            continue
        case_present = True
        if not dispatch_id or coerce_string(audit.get('dispatch_id')) == dispatch_id:
            dispatch_present = True
            break
    state['case_present'] = case_present
    state['dispatch_present'] = dispatch_present
    return state



def relevant_state(*, db_url: str, psql_bin: str, case_key: str, dispatch_id: str, force_refresh: bool = False) -> dict[str, Any]:
    resolved_db_url = resolve_db_url(db_url)
    if not resolved_db_url:
        return {'db_available': False, 'should_run': False, 'skip_reason': 'db_url_unavailable'}
    if not table_exists('lmd_bundle_exposures', db_url=resolved_db_url, psql_bin=psql_bin):
        return {
            'db_available': True,
            'should_run': False,
            'missing_tables': ['lmd_bundle_exposures'],
            'skip_reason': 'lmd_bundle_exposures_table_missing',
        }

    missing_tables: list[str] = []
    trial_present = table_exists('proposed_causal_trial_exposures', db_url=resolved_db_url, psql_bin=psql_bin)
    if not trial_present:
        missing_tables.append('proposed_causal_trial_exposures')
    reviews_present = table_exists('learning_case_reviews', db_url=resolved_db_url, psql_bin=psql_bin)
    if not reviews_present:
        missing_tables.append('learning_case_reviews')

    params = {'case_key': case_key, 'dispatch_id': dispatch_id}
    lmd_rows = query_count(psql_bin, resolved_db_url, COUNT_LMD_SQL, params)
    trial_rows = query_count(psql_bin, resolved_db_url, COUNT_TRIAL_SQL, params) if trial_present else 0
    resolved_reviews = query_count(psql_bin, resolved_db_url, COUNT_RESOLVED_SQL, {'case_key': case_key}) if reviews_present else 0

    latest_lmd_exposure_at = query_latest_at(psql_bin, resolved_db_url, LATEST_LMD_SQL, params)
    latest_trial_exposure_at = query_latest_at(psql_bin, resolved_db_url, LATEST_TRIAL_SQL, params) if trial_present else None
    latest_review_update_at = query_latest_at(psql_bin, resolved_db_url, LATEST_REVIEW_SQL, {'case_key': case_key}) if reviews_present else None

    latest_signal_dt = max(
        [stamp for stamp in [parse_iso(latest_lmd_exposure_at), parse_iso(latest_trial_exposure_at), parse_iso(latest_review_update_at)] if stamp is not None],
        default=None,
    )
    latest_signal_at = latest_signal_dt.isoformat() if latest_signal_dt is not None else None

    report_state = load_existing_report_state(case_key=case_key, dispatch_id=dispatch_id)
    report_generated_dt = parse_iso(report_state.get('report_generated_at'))
    report_scope_present = bool(report_state.get('case_present')) and bool(report_state.get('dispatch_present'))
    report_fresh = bool(
        report_generated_dt is not None
        and latest_signal_dt is not None
        and report_generated_dt >= latest_signal_dt
        and report_scope_present
        and not report_state.get('report_parse_error')
    )

    has_relevant_state = bool(lmd_rows > 0 or trial_rows > 0 or resolved_reviews > 0)
    should_run = bool(has_relevant_state and (force_refresh or not report_fresh))
    skip_reason = None
    if not has_relevant_state:
        skip_reason = 'no_relevant_treatment_state'
    elif report_fresh and not force_refresh:
        skip_reason = 'report_already_fresh'

    return {
        'db_available': True,
        'missing_tables': missing_tables,
        'lmd_exposure_rows': lmd_rows,
        'trial_exposure_rows': trial_rows,
        'resolved_reviews': resolved_reviews,
        'latest_lmd_exposure_at': latest_lmd_exposure_at,
        'latest_trial_exposure_at': latest_trial_exposure_at,
        'latest_review_update_at': latest_review_update_at,
        'latest_relevant_signal_at': latest_signal_at,
        'report_state': report_state,
        'report_fresh': report_fresh,
        'force_refresh': bool(force_refresh),
        'should_run': should_run,
        'skip_reason': skip_reason,
    }



def run_cycle(args: argparse.Namespace) -> dict[str, Any]:
    command = [
        sys.executable,
        str(RUN_POST_TREATMENT),
        '--case-key', args.case_key,
        '--psql', args.psql,
    ]
    dispatch_id = coerce_string(args.dispatch_id)
    if dispatch_id:
        command.extend(['--dispatch-id', dispatch_id])
    if args.db_url:
        command.extend(['--db-url', args.db_url])
    if args.repair_missing_logs:
        command.append('--repair-missing-logs')
    if args.dry_run:
        command.append('--dry-run')
    if args.pretty:
        command.append('--pretty')
    proc = subprocess.run(command, text=True, capture_output=True)
    stdout = (proc.stdout or '').strip()
    stderr = (proc.stderr or '').strip()
    if proc.returncode != 0:
        return {
            'ok': False,
            'returncode': proc.returncode,
            'error': stderr or stdout or 'run_post_treatment_causal_feedback_cycle.py failed',
            'command': command,
        }
    payload: Any = None
    if stdout:
        try:
            payload = json.loads(stdout)
        except Exception:
            payload = {'raw_stdout': stdout}
    return {
        'ok': True,
        'returncode': 0,
        'payload': payload,
        'stderr': stderr or None,
        'command': command,
    }



def enqueue_retry(args: argparse.Namespace, *, state: dict[str, Any], cycle: dict[str, Any]) -> dict[str, Any]:
    queue_rows = read_json_lines(TRIGGER_RETRY_QUEUE_PATH)
    key = (coerce_string(args.case_key), coerce_string(args.dispatch_id), coerce_string(args.trigger_source))
    retained: list[dict[str, Any]] = []
    already_present = False
    for row in queue_rows:
        existing_key = (
            coerce_string(row.get('case_key')),
            coerce_string(row.get('dispatch_id')),
            coerce_string(row.get('trigger_source')),
        )
        if existing_key == key:
            already_present = True
            retained.append(row)
            continue
        retained.append(row)
    if not already_present:
        retained.append({
            'queued_at': now_iso(),
            'case_key': coerce_string(args.case_key),
            'dispatch_id': coerce_string(args.dispatch_id),
            'trigger_source': coerce_string(args.trigger_source),
            'repair_missing_logs': bool(args.repair_missing_logs),
            'db_url_present': bool(args.db_url),
            'state': state,
            'cycle_error': cycle.get('error'),
        })
        write_json_lines(TRIGGER_RETRY_QUEUE_PATH, retained)
    return {
        'queue_path': str(TRIGGER_RETRY_QUEUE_PATH),
        'queued': not already_present,
        'already_present': already_present,
        'queue_depth': len(retained),
    }



def main() -> int:
    args = parse_args()
    state = relevant_state(
        db_url=args.db_url,
        psql_bin=args.psql,
        case_key=args.case_key,
        dispatch_id=args.dispatch_id,
        force_refresh=args.repair_missing_logs,
    )
    result: dict[str, Any] = {
        'ok': True,
        'case_key': args.case_key,
        'dispatch_id': coerce_string(args.dispatch_id) or None,
        'trigger_source': args.trigger_source,
        'state': state,
    }
    if not state.get('should_run'):
        result.update({'status': 'skipped', 'reason': state.get('skip_reason') or 'no_relevant_treatment_state'})
    else:
        cycle = run_cycle(args)
        result.update({'status': 'triggered', 'cycle': cycle})
        if not cycle.get('ok'):
            result['ok'] = False
            result['retry_queue'] = enqueue_retry(args, state=state, cycle=cycle)
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0 if result.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
