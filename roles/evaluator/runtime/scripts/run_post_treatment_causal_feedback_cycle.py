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
from lib.io import read_json, write_json  # noqa: E402
from lib.lmd import bundle_candidates  # noqa: E402

DEFAULT_EXPERIMENT_ID = 'researcher-lmd-v1'
GENERATED_ROOT = WORKSPACE_ROOT / 'qualitative-db' / '60-causal-map' / 'generated'
DEFAULT_JSON_OUT = GENERATED_ROOT / 'post-treatment-feedback-cycle.json'
DEFAULT_MD_OUT = GENERATED_ROOT / 'post-treatment-feedback-cycle.md'

LOG_LMD_EXPOSURES = SCRIPT_PATH.parent / 'log_lmd_bundle_exposure.py'
LOG_TRIAL_EXPOSURES = SCRIPT_PATH.parent / 'log_proposed_causal_trial_exposure.py'
SCORE_TRIAL_OUTCOMES = SCRIPT_PATH.parent / 'score_proposed_causal_trial_outcomes.py'
ADVANCE_PROPOSALS = SCRIPT_PATH.parent / 'advance_proposed_causal_candidates.py'
UPDATE_LMD_CANDIDATES = SCRIPT_PATH.parent / 'update_lmd_candidate_stats.py'
RUN_LIVE_GRAPH_CYCLE = SCRIPT_PATH.parent / 'run_live_causal_graph_cycle.py'
LEARN_PHASE11_POLICY = SCRIPT_PATH.parent / 'learn_phase11_retrieval_policy.py'
REPORT_PHASE11_POLICY = SCRIPT_PATH.parent / 'report_phase11_retrieval_policy.py'
BACKFILL_DISPATCH_AUDITS = SCRIPT_PATH.parent / 'backfill_lmd_causal_dispatch_audits.py'
RECONCILE_RUNTIME = SCRIPT_PATH.parent / 'reconcile_lmd_causal_runtime.py'
REPORT_RUNTIME_STATUS = SCRIPT_PATH.parent / 'report_lmd_causal_runtime_status.py'
REPORT_CAUSAL_GOVERNANCE = SCRIPT_PATH.parent / 'report_causal_governance.py'
REPORT_TRIAL_PACKETS = SCRIPT_PATH.parent / 'report_proposed_causal_trial_packets.py'
REPORT_SHADOW_VS_LIVE = SCRIPT_PATH.parent / 'report_shadow_vs_live_proposals.py'

TREATMENT_CYCLES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY last_exposure_at DESC), '[]'::json)::text
FROM (
  SELECT
    e.case_key,
    e.dispatch_id,
    COALESCE(MAX(NULLIF(e.research_run_id, '')), '') AS research_run_id,
    COALESCE(MAX(NULLIF(e.experiment_id, '')), '') AS experiment_id,
    COALESCE(MAX(NULLIF(e.arm, '')), '') AS arm,
    COALESCE(MAX(NULLIF(e.generator_version, '')), '') AS generator_version,
    COALESCE(MAX(NULLIF(e.policy_version, '')), '') AS policy_version,
    COALESCE(MAX(NULLIF(e.bundle_path, '')), '') AS bundle_path,
    COUNT(*)::int AS lmd_exposure_rows,
    COUNT(DISTINCT e.candidate_id)::int AS lmd_distinct_candidate_rows,
    MIN(e.created_at) AS first_exposure_at,
    MAX(e.created_at) AS last_exposure_at,
    MAX(r.resolution_status) AS resolution_status,
    MAX(r.latest_brier_component) AS latest_brier_component,
    MAX(COALESCE(r.updated_at, r.created_at)) AS review_updated_at
  FROM public.lmd_bundle_exposures e
  LEFT JOIN public.learning_case_reviews r
    ON r.case_key = e.case_key
  WHERE COALESCE(NULLIF(e.arm, ''), '') = 'treatment'
    AND (NULLIF(:'experiment_id', '') IS NULL OR e.experiment_id = NULLIF(:'experiment_id', ''))
  GROUP BY e.case_key, e.dispatch_id
) t;
'''

TRIAL_COUNTS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    case_key,
    dispatch_id,
    COUNT(*)::int AS trial_rows,
    COUNT(*) FILTER (WHERE injected IS TRUE)::int AS trial_injected_rows,
    COUNT(*) FILTER (WHERE preview_only IS TRUE)::int AS trial_preview_rows,
    COUNT(*) FILTER (WHERE NULLIF(outcome_label, '') IS NOT NULL)::int AS trial_judged_rows,
    MAX(created_at) AS trial_last_exposure_at
  FROM public.proposed_causal_trial_exposures
  GROUP BY case_key, dispatch_id
) t;
'''



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Audit and run the causal-map post-treatment feedback cycle for recent treatment-arm LMD cases')
    parser.add_argument('--case-key', action='append', default=[])
    parser.add_argument('--dispatch-id', action='append', default=[])
    parser.add_argument('--recent-treatment-cases', type=int, default=5)
    parser.add_argument('--experiment-id', default=DEFAULT_EXPERIMENT_ID)
    parser.add_argument('--repair-missing-logs', action='store_true')
    parser.add_argument('--report-max-cases', type=int, default=5)
    parser.add_argument('--json-out', default=str(DEFAULT_JSON_OUT))
    parser.add_argument('--md-out', default=str(DEFAULT_MD_OUT))
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()



def coerce_string(value: Any) -> str:
    if value is None:
        return ''
    return str(value).strip()



def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return int(default)



def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return float(default)



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



def relative_to_workspace(path: Path) -> str:
    try:
        return str(path.relative_to(WORKSPACE_ROOT))
    except ValueError:
        return str(path)



def resolve_path(path_str: str) -> Path:
    path = Path(path_str)
    if not path.is_absolute():
        path = (WORKSPACE_ROOT / path_str).resolve()
    return path



def load_treatment_cycles(*, db_url: str, psql_bin: str, experiment_id: str, case_keys: set[str], dispatch_ids: set[str], recent_limit: int) -> list[dict[str, Any]]:
    resolved_db_url = resolve_db_url(db_url)
    if not resolved_db_url:
        return []
    if not table_exists('lmd_bundle_exposures', db_url=resolved_db_url, psql_bin=psql_bin):
        return []

    cycles = exec_sql(psql_bin, resolved_db_url, TREATMENT_CYCLES_SQL, {'experiment_id': experiment_id}) or []
    if not isinstance(cycles, list):
        cycles = []

    trial_map: dict[tuple[str, str], dict[str, Any]] = {}
    if table_exists('proposed_causal_trial_exposures', db_url=resolved_db_url, psql_bin=psql_bin):
        trial_rows = exec_sql(psql_bin, resolved_db_url, TRIAL_COUNTS_SQL, {}) or []
        if isinstance(trial_rows, list):
            for row in trial_rows:
                if not isinstance(row, dict):
                    continue
                key = (coerce_string(row.get('case_key')), coerce_string(row.get('dispatch_id')))
                trial_map[key] = row

    filtered: list[dict[str, Any]] = []
    for row in cycles:
        if not isinstance(row, dict):
            continue
        case_key = coerce_string(row.get('case_key'))
        dispatch_id = coerce_string(row.get('dispatch_id'))
        if case_keys and case_key not in case_keys:
            continue
        if dispatch_ids and dispatch_id not in dispatch_ids:
            continue
        trial_row = trial_map.get((case_key, dispatch_id), {})
        filtered.append({
            **row,
            'trial_rows': safe_int(trial_row.get('trial_rows')),
            'trial_injected_rows': safe_int(trial_row.get('trial_injected_rows')),
            'trial_preview_rows': safe_int(trial_row.get('trial_preview_rows')),
            'trial_judged_rows': safe_int(trial_row.get('trial_judged_rows')),
            'trial_last_exposure_at': trial_row.get('trial_last_exposure_at'),
        })

    filtered.sort(key=lambda item: coerce_string(item.get('last_exposure_at')), reverse=True)
    if not case_keys and not dispatch_ids:
        filtered = filtered[: max(0, int(recent_limit))]
    return filtered



def load_bundle_details(bundle_path_str: str) -> dict[str, Any]:
    if not bundle_path_str:
        return {
            'bundle_found': False,
            'bundle_path': None,
            'bundle': {},
            'expected_lmd_rows': 0,
            'expected_trial_rows': 0,
            'expected_trial_injected_rows': 0,
            'selected_candidate_ids': [],
        }
    path = resolve_path(bundle_path_str)
    bundle = read_json(path, default={}) if path.exists() else {}
    if not isinstance(bundle, dict):
        bundle = {}
    overlay = bundle.get('trial_overlay') if isinstance(bundle.get('trial_overlay'), dict) else {}
    selected = [row for row in (overlay.get('selected_candidates') or []) if isinstance(row, dict)]
    candidates = bundle_candidates(bundle) if bundle else []
    return {
        'bundle_found': path.exists() and bool(bundle),
        'bundle_path': path,
        'bundle': bundle,
        'expected_lmd_rows': len(candidates) if bool(bundle.get('lmd_used')) else 0,
        'expected_trial_rows': len(selected),
        'expected_trial_injected_rows': len([row for row in selected if bool(row.get('injected'))]),
        'selected_candidate_ids': [coerce_string(row.get('proposal_id') or row.get('proposal_key')) for row in selected if coerce_string(row.get('proposal_id') or row.get('proposal_key'))],
    }



def build_cycle_audit(cycle: dict[str, Any]) -> dict[str, Any]:
    bundle_info = load_bundle_details(coerce_string(cycle.get('bundle_path')))
    bundle = bundle_info['bundle'] or {}
    overlay = bundle.get('trial_overlay') if isinstance(bundle.get('trial_overlay'), dict) else {}
    lmd_used = bool(bundle.get('lmd_used'))
    resolution_status = coerce_string(cycle.get('resolution_status'))
    latest_brier_component = cycle.get('latest_brier_component')
    actual_lmd_rows = safe_int(cycle.get('lmd_exposure_rows'))
    actual_trial_rows = safe_int(cycle.get('trial_rows'))
    actual_trial_injected_rows = safe_int(cycle.get('trial_injected_rows'))
    expected_lmd_rows = safe_int(bundle_info.get('expected_lmd_rows'))
    expected_trial_rows = safe_int(bundle_info.get('expected_trial_rows'))
    expected_trial_injected_rows = safe_int(bundle_info.get('expected_trial_injected_rows'))

    warnings: list[str] = []
    if not bundle_info['bundle_found']:
        warnings.append('bundle_missing')
    if lmd_used and actual_lmd_rows != expected_lmd_rows:
        warnings.append('lmd_exposure_row_count_mismatch')
    if actual_trial_rows != expected_trial_rows:
        warnings.append('trial_exposure_row_count_mismatch')
    if actual_trial_injected_rows != expected_trial_injected_rows:
        warnings.append('trial_injected_row_count_mismatch')
    if resolution_status != 'resolved':
        warnings.append('case_not_resolved_yet')
    if resolution_status == 'resolved' and latest_brier_component is None:
        warnings.append('resolved_case_missing_latest_brier_component')

    ready_for_outcome_learning = resolution_status == 'resolved' and latest_brier_component is not None and actual_lmd_rows > 0
    ready_for_trial_outcome_learning = ready_for_outcome_learning and actual_trial_injected_rows > 0
    return {
        'case_key': coerce_string(cycle.get('case_key')),
        'dispatch_id': coerce_string(cycle.get('dispatch_id')),
        'research_run_id': coerce_string(cycle.get('research_run_id')),
        'experiment_id': coerce_string(cycle.get('experiment_id')),
        'arm': coerce_string(cycle.get('arm')),
        'generator_version': coerce_string(cycle.get('generator_version')),
        'policy_version': coerce_string(cycle.get('policy_version')),
        'bundle_path': relative_to_workspace(bundle_info['bundle_path']) if bundle_info.get('bundle_path') else coerce_string(cycle.get('bundle_path')),
        'first_exposure_at': cycle.get('first_exposure_at'),
        'last_exposure_at': cycle.get('last_exposure_at'),
        'trial_last_exposure_at': cycle.get('trial_last_exposure_at'),
        'review_updated_at': cycle.get('review_updated_at'),
        'bundle_found': bool(bundle_info['bundle_found']),
        'bundle_status': bundle.get('status'),
        'lmd_used': lmd_used,
        'trial_overlay_enabled': bool(overlay.get('enabled', False)),
        'trial_overlay_mode': overlay.get('overlay_mode'),
        'trial_overlay_preview_only': bool(overlay.get('preview_only', True)),
        'selected_trial_candidate_ids': bundle_info.get('selected_candidate_ids') or [],
        'expected_lmd_rows': expected_lmd_rows,
        'actual_lmd_rows': actual_lmd_rows,
        'expected_trial_rows': expected_trial_rows,
        'actual_trial_rows': actual_trial_rows,
        'expected_trial_injected_rows': expected_trial_injected_rows,
        'actual_trial_injected_rows': actual_trial_injected_rows,
        'actual_trial_judged_rows': safe_int(cycle.get('trial_judged_rows')),
        'resolution_status': resolution_status or None,
        'latest_brier_component': latest_brier_component,
        'lmd_logging_complete': (actual_lmd_rows == expected_lmd_rows) if lmd_used else (actual_lmd_rows == 0),
        'trial_logging_complete': actual_trial_rows == expected_trial_rows and actual_trial_injected_rows == expected_trial_injected_rows,
        'ready_for_outcome_learning': ready_for_outcome_learning,
        'ready_for_trial_outcome_learning': ready_for_trial_outcome_learning,
        'warnings': warnings,
    }



def run_json_command(command: list[str]) -> dict[str, Any]:
    proc = subprocess.run(command, text=True, capture_output=True)
    stdout = (proc.stdout or '').strip()
    stderr = (proc.stderr or '').strip()
    if proc.returncode != 0:
        return {
            'ok': False,
            'command': command,
            'returncode': proc.returncode,
            'error': stderr or stdout or 'command failed',
        }
    payload: Any = None
    if stdout:
        try:
            payload = json.loads(stdout)
        except Exception:
            payload = {'raw_stdout': stdout}
    return {
        'ok': True,
        'command': command,
        'returncode': proc.returncode,
        'payload': payload,
        'stderr': stderr or None,
    }



def maybe_repair_logs(audit: dict[str, Any], args: argparse.Namespace) -> list[dict[str, Any]]:
    repairs: list[dict[str, Any]] = []
    bundle_path = coerce_string(audit.get('bundle_path'))
    if not args.repair_missing_logs or not audit.get('bundle_found') or not bundle_path:
        return repairs

    if audit.get('lmd_used') and safe_int(audit.get('actual_lmd_rows')) < safe_int(audit.get('expected_lmd_rows')):
        command = [
            sys.executable,
            str(LOG_LMD_EXPOSURES),
            '--case-key', coerce_string(audit.get('case_key')),
            '--dispatch-id', coerce_string(audit.get('dispatch_id')),
            '--research-run-id', coerce_string(audit.get('research_run_id')),
            '--bundle-path', bundle_path,
            '--experiment-id', coerce_string(audit.get('experiment_id')),
            '--arm', coerce_string(audit.get('arm')),
            '--generator-version', coerce_string(audit.get('generator_version')),
            '--policy-version', coerce_string(audit.get('policy_version')),
            '--notes-json', json.dumps({'repair_source': 'run_post_treatment_causal_feedback_cycle'}, separators=(',', ':')),
            '--psql', args.psql,
        ]
        if args.db_url:
            command.extend(['--db-url', args.db_url])
        if args.dry_run:
            command.append('--dry-run')
        repairs.append({'kind': 'lmd_bundle_exposures', **run_json_command(command)})

    if safe_int(audit.get('actual_trial_rows')) < safe_int(audit.get('expected_trial_rows')):
        command = [
            sys.executable,
            str(LOG_TRIAL_EXPOSURES),
            '--case-key', coerce_string(audit.get('case_key')),
            '--dispatch-id', coerce_string(audit.get('dispatch_id')),
            '--research-run-id', coerce_string(audit.get('research_run_id')),
            '--bundle-path', bundle_path,
            '--experiment-id', coerce_string(audit.get('experiment_id')),
            '--experiment-arm', coerce_string(audit.get('arm')),
            '--notes-json', json.dumps({'repair_source': 'run_post_treatment_causal_feedback_cycle'}, separators=(',', ':')),
            '--psql', args.psql,
        ]
        if args.db_url:
            command.extend(['--db-url', args.db_url])
        if args.dry_run:
            command.append('--dry-run')
        repairs.append({'kind': 'proposed_causal_trial_exposures', **run_json_command(command)})
    return repairs



def run_refresh_step(script_path: Path, *, args: argparse.Namespace, extra_args: list[str] | None = None) -> dict[str, Any]:
    command = [sys.executable, str(script_path), '--psql', args.psql]
    if args.db_url:
        command.extend(['--db-url', args.db_url])
    if extra_args:
        command.extend(extra_args)
    if args.dry_run:
        command.append('--dry-run')
    if args.pretty:
        command.append('--pretty')
    result = run_json_command(command)
    result['step'] = script_path.name
    return result



def run_trial_outcome_scoring(audits: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for audit in audits:
        if not audit.get('ready_for_trial_outcome_learning'):
            results.append({
                'step': SCORE_TRIAL_OUTCOMES.name,
                'case_key': audit.get('case_key'),
                'skipped': True,
                'reason': 'case_not_ready_for_trial_outcome_learning',
            })
            continue
        command = [
            sys.executable,
            str(SCORE_TRIAL_OUTCOMES),
            '--case-key', coerce_string(audit.get('case_key')),
            '--psql', args.psql,
        ]
        if args.db_url:
            command.extend(['--db-url', args.db_url])
        if args.dry_run:
            command.append('--dry-run')
        if args.pretty:
            command.append('--pretty')
        result = run_json_command(command)
        result['step'] = SCORE_TRIAL_OUTCOMES.name
        result['case_key'] = audit.get('case_key')
        results.append(result)
    return results



def extract_live_graph_cycle_summary(refresh_steps: list[dict[str, Any]]) -> dict[str, Any]:
    step = next((item for item in refresh_steps if item.get('step') == RUN_LIVE_GRAPH_CYCLE.name), None)
    if not isinstance(step, dict) or not step.get('ok'):
        return {}
    payload = step.get('payload') or {}
    summaries = payload.get('summaries') if isinstance(payload, dict) else []
    summary_map = {
        coerce_string(item.get('step')): item
        for item in (summaries or [])
        if isinstance(item, dict) and coerce_string(item.get('step'))
    }
    scan_summary = summary_map.get('scan_causal_graph_health') or {}
    repair_summary = summary_map.get('repair_causal_graph') or {}
    controller_summary = summary_map.get('advance_live_causal_graph_items') or {}
    post_repair_summary = repair_summary.get('post_repair_projection') if isinstance(repair_summary, dict) else {}
    return {
        'live_graph_cycle_ok': True,
        'live_graph_pre_repair_violation_count': safe_int(scan_summary.get('violation_count')),
        'live_graph_violation_count': safe_int((post_repair_summary or {}).get('violation_count', scan_summary.get('violation_count'))),
        'live_graph_repair_count': safe_int(repair_summary.get('repair_count')),
        'live_graph_recommended_count': safe_int(controller_summary.get('recommended_count')),
        'live_graph_blocked_count': safe_int(controller_summary.get('blocked_count')),
    }



def build_summary(*, audits: list[dict[str, Any]], repairs: list[dict[str, Any]], refresh_steps: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    case_count = len(audits)
    resolved_count = sum(1 for audit in audits if audit.get('resolution_status') == 'resolved')
    ready_count = sum(1 for audit in audits if audit.get('ready_for_outcome_learning'))
    ready_trial_count = sum(1 for audit in audits if audit.get('ready_for_trial_outcome_learning'))
    lmd_complete = sum(1 for audit in audits if audit.get('lmd_logging_complete'))
    trial_complete = sum(1 for audit in audits if audit.get('trial_logging_complete'))
    cases_with_any_warning = sum(1 for audit in audits if audit.get('warnings'))
    step_errors = [step for step in refresh_steps if not step.get('ok', True) and not step.get('skipped')]
    repair_errors = [item for item in repairs if not item.get('ok', True)]

    generated_at = utc_now_iso()
    generated_dt = parse_iso(generated_at)
    latest_lmd_candidates = [stamp for stamp in (parse_iso(audit.get('last_exposure_at')) for audit in audits) if stamp is not None]
    latest_trial_candidates = [stamp for stamp in (parse_iso(audit.get('trial_last_exposure_at')) for audit in audits) if stamp is not None]
    latest_review_candidates = [stamp for stamp in (parse_iso(audit.get('review_updated_at')) for audit in audits) if stamp is not None]
    latest_lmd_dt = max(latest_lmd_candidates, default=None)
    latest_trial_dt = max(latest_trial_candidates, default=None)
    latest_review_dt = max(latest_review_candidates, default=None)
    latest_signal_dt = max((stamp for stamp in [latest_lmd_dt, latest_trial_dt, latest_review_dt] if stamp is not None), default=None)
    latest_signal_age_seconds = None
    if generated_dt is not None and latest_signal_dt is not None:
        latest_signal_age_seconds = round(max(0.0, (generated_dt - latest_signal_dt).total_seconds()), 3)

    summary = {
        'generated_at': generated_at,
        'experiment_id': args.experiment_id,
        'cycle_count': case_count,
        'resolved_cycle_count': resolved_count,
        'ready_for_outcome_learning_count': ready_count,
        'ready_for_trial_outcome_learning_count': ready_trial_count,
        'lmd_logging_complete_count': lmd_complete,
        'trial_logging_complete_count': trial_complete,
        'cases_with_warnings_count': cases_with_any_warning,
        'repair_attempt_count': len(repairs),
        'repair_error_count': len(repair_errors),
        'refresh_step_count': len(refresh_steps),
        'refresh_error_count': len(step_errors),
        'retuning_ready': bool(ready_count > 0),
        'proposal_retuning_ready': bool(ready_trial_count > 0),
        'latest_lmd_exposure_at': latest_lmd_dt.isoformat() if latest_lmd_dt is not None else None,
        'latest_trial_exposure_at': latest_trial_dt.isoformat() if latest_trial_dt is not None else None,
        'latest_review_update_at': latest_review_dt.isoformat() if latest_review_dt is not None else None,
        'latest_relevant_signal_at': latest_signal_dt.isoformat() if latest_signal_dt is not None else None,
        'latest_relevant_signal_age_seconds': latest_signal_age_seconds,
    }
    summary.update(extract_live_graph_cycle_summary(refresh_steps))
    return summary



def render_markdown(report: dict[str, Any]) -> str:
    summary = report.get('summary') or {}
    lines = [
        '# Post-treatment causal feedback cycle',
        '',
        f"- generated_at: `{summary.get('generated_at')}`",
        f"- experiment_id: `{summary.get('experiment_id')}`",
        f"- cycle_count: `{summary.get('cycle_count')}`",
        f"- resolved_cycle_count: `{summary.get('resolved_cycle_count')}`",
        f"- ready_for_outcome_learning_count: `{summary.get('ready_for_outcome_learning_count')}`",
        f"- ready_for_trial_outcome_learning_count: `{summary.get('ready_for_trial_outcome_learning_count')}`",
        f"- lmd_logging_complete_count: `{summary.get('lmd_logging_complete_count')}` / `{summary.get('cycle_count')}`",
        f"- trial_logging_complete_count: `{summary.get('trial_logging_complete_count')}` / `{summary.get('cycle_count')}`",
        f"- latest_lmd_exposure_at: `{summary.get('latest_lmd_exposure_at')}`",
        f"- latest_trial_exposure_at: `{summary.get('latest_trial_exposure_at')}`",
        f"- latest_review_update_at: `{summary.get('latest_review_update_at')}`",
        f"- latest_relevant_signal_at: `{summary.get('latest_relevant_signal_at')}`",
        f"- latest_relevant_signal_age_seconds: `{summary.get('latest_relevant_signal_age_seconds')}`",
        f"- retuning_ready: `{summary.get('retuning_ready')}`",
        f"- proposal_retuning_ready: `{summary.get('proposal_retuning_ready')}`",
        f"- live_graph_pre_repair_violation_count: `{summary.get('live_graph_pre_repair_violation_count')}`",
        f"- live_graph_violation_count: `{summary.get('live_graph_violation_count')}`",
        f"- live_graph_repair_count: `{summary.get('live_graph_repair_count')}`",
        f"- live_graph_recommended_count: `{summary.get('live_graph_recommended_count')}`",
        f"- live_graph_blocked_count: `{summary.get('live_graph_blocked_count')}`",
        '',
        '## Audited treatment cycles',
    ]
    for audit in report.get('audits') or []:
        lines.extend([
            '',
            f"### {audit.get('case_key')} / {audit.get('dispatch_id')}",
            f"- resolution_status: `{audit.get('resolution_status')}`",
            f"- latest_brier_component: `{audit.get('latest_brier_component')}`",
            f"- bundle_status: `{audit.get('bundle_status')}`",
            f"- lmd_used: `{audit.get('lmd_used')}`",
            f"- lmd_rows: expected `{audit.get('expected_lmd_rows')}` actual `{audit.get('actual_lmd_rows')}` complete=`{audit.get('lmd_logging_complete')}`",
            f"- trial_rows: expected `{audit.get('expected_trial_rows')}` actual `{audit.get('actual_trial_rows')}` complete=`{audit.get('trial_logging_complete')}`",
            f"- trial_injected_rows: expected `{audit.get('expected_trial_injected_rows')}` actual `{audit.get('actual_trial_injected_rows')}`",
            f"- ready_for_outcome_learning: `{audit.get('ready_for_outcome_learning')}`",
            f"- ready_for_trial_outcome_learning: `{audit.get('ready_for_trial_outcome_learning')}`",
        ])
        warnings = list(audit.get('warnings') or [])
        if warnings:
            lines.append('- warnings:')
            for warning in warnings:
                lines.append(f'  - `{warning}`')

    lines.extend(['', '## Repair actions'])
    for item in report.get('repairs') or []:
        label = item.get('kind') or 'repair'
        if item.get('skipped'):
            lines.append(f'- `{label}` skipped: `{item.get("reason")}`')
            continue
        lines.append(f'- `{label}` ok=`{item.get("ok")}`')
        if item.get('error'):
            lines.append(f'  - error: `{item.get("error")}`')

    lines.extend(['', '## Refresh steps'])
    for step in report.get('refresh_steps') or []:
        if step.get('skipped'):
            lines.append(f'- `{step.get("step")}` / `{step.get("case_key")}` skipped: `{step.get("reason")}`')
            continue
        lines.append(f'- `{step.get("step")}` ok=`{step.get("ok")}`')
        if step.get('error'):
            lines.append(f'  - error: `{step.get("error")}`')
    return '\n'.join(lines).rstrip() + '\n'



def main() -> int:
    args = parse_args()
    case_keys = {coerce_string(item) for item in args.case_key if coerce_string(item)}
    dispatch_ids = {coerce_string(item) for item in args.dispatch_id if coerce_string(item)}

    audits = [
        build_cycle_audit(cycle)
        for cycle in load_treatment_cycles(
            db_url=args.db_url,
            psql_bin=args.psql,
            experiment_id=args.experiment_id,
            case_keys=case_keys,
            dispatch_ids=dispatch_ids,
            recent_limit=args.recent_treatment_cases,
        )
    ]

    repairs: list[dict[str, Any]] = []
    if args.repair_missing_logs:
        for audit in audits:
            repairs.extend(maybe_repair_logs(audit, args))
        audits = [
            build_cycle_audit(cycle)
            for cycle in load_treatment_cycles(
                db_url=args.db_url,
                psql_bin=args.psql,
                experiment_id=args.experiment_id,
                case_keys=case_keys,
                dispatch_ids=dispatch_ids,
                recent_limit=args.recent_treatment_cases,
            )
        ]

    refresh_steps: list[dict[str, Any]] = []
    refresh_steps.extend(run_trial_outcome_scoring(audits, args))
    refresh_steps.append(run_refresh_step(ADVANCE_PROPOSALS, args=args))
    refresh_steps.append(run_refresh_step(UPDATE_LMD_CANDIDATES, args=args, extra_args=['--experiment-id', args.experiment_id]))
    live_graph_extra_args = ['--experiment-id', args.experiment_id]
    if not args.dry_run:
        live_graph_extra_args.append('--repair-apply')
    refresh_steps.append(run_refresh_step(RUN_LIVE_GRAPH_CYCLE, args=args, extra_args=live_graph_extra_args))
    refresh_steps.append(run_refresh_step(LEARN_PHASE11_POLICY, args=args))

    report_case_keys = [coerce_string(audit.get('case_key')) for audit in audits[: max(0, int(args.report_max_cases))] if coerce_string(audit.get('case_key'))]
    report_extra_args: list[str] = []
    for case_key in report_case_keys:
        report_extra_args.extend(['--case-key', case_key])
    refresh_steps.append(run_refresh_step(REPORT_PHASE11_POLICY, args=args, extra_args=report_extra_args))
    refresh_steps.append(run_refresh_step(BACKFILL_DISPATCH_AUDITS, args=args, extra_args=['--experiment-id', args.experiment_id, '--recent-treatment-cases', str(max(0, int(args.recent_treatment_cases)))]))
    refresh_steps.append(run_refresh_step(RECONCILE_RUNTIME, args=args, extra_args=['--experiment-id', args.experiment_id, '--recent-treatment-cases', str(max(0, int(args.recent_treatment_cases)))]))
    refresh_steps.append(run_refresh_step(REPORT_RUNTIME_STATUS, args=args))
    refresh_steps.append(run_refresh_step(REPORT_CAUSAL_GOVERNANCE, args=args))
    refresh_steps.append(run_refresh_step(REPORT_TRIAL_PACKETS, args=args))
    refresh_steps.append(run_refresh_step(REPORT_SHADOW_VS_LIVE, args=args))

    report = {
        'summary': build_summary(audits=audits, repairs=repairs, refresh_steps=refresh_steps, args=args),
        'audits': audits,
        'repairs': repairs,
        'refresh_steps': refresh_steps,
    }
    markdown = render_markdown(report)

    json_out = resolve_path(args.json_out)
    md_out = resolve_path(args.md_out)
    if not args.dry_run:
        json_out.parent.mkdir(parents=True, exist_ok=True)
        md_out.parent.mkdir(parents=True, exist_ok=True)
        write_json(json_out, report, pretty=True)
        md_out.write_text(markdown, encoding='utf-8')

    output = {
        'ok': True,
        'summary': report['summary'],
        'json_out': relative_to_workspace(json_out),
        'md_out': relative_to_workspace(md_out),
        'audited_cases': [
            {
                'case_key': audit.get('case_key'),
                'dispatch_id': audit.get('dispatch_id'),
                'resolution_status': audit.get('resolution_status'),
                'lmd_logging_complete': audit.get('lmd_logging_complete'),
                'trial_logging_complete': audit.get('trial_logging_complete'),
                'ready_for_outcome_learning': audit.get('ready_for_outcome_learning'),
                'ready_for_trial_outcome_learning': audit.get('ready_for_trial_outcome_learning'),
                'warnings': audit.get('warnings') or [],
            }
            for audit in audits
        ],
    }
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
