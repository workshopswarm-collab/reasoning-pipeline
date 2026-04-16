#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.io import read_json, write_json  # noqa: E402
from lib.lmd_causal_runtime import (  # noqa: E402
    audit_path_for_bundle,
    bundle_path_to_repo_relative,
    case_mix_from_query_profile,
    coerce_string,
    coverage_metrics_from_bundle,
    now_iso,
    resolve_repo_path,
    sha256_jsonable,
    summarize_logging_result,
)
from lib.paths import to_repo_relative  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Write a compact per-dispatch LMD/causal audit artifact beside an LMD bundle')
    parser.add_argument('--bundle-path', required=True)
    parser.add_argument('--case-key', default='')
    parser.add_argument('--dispatch-id', default='')
    parser.add_argument('--research-run-id', default='')
    parser.add_argument('--notes-json', default='{}')
    parser.add_argument('--shadow-logging-json', default='{}')
    parser.add_argument('--trial-logging-json', default='{}')
    parser.add_argument('--lmd-logging-json', default='{}')
    parser.add_argument('--trigger-json', default='{}')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def parse_json_arg(text: str, *, field: str) -> dict[str, Any]:
    try:
        payload = json.loads(text or '{}')
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f'invalid {field}: {exc}')
    if not isinstance(payload, dict):
        raise SystemExit(f'{field} must decode to an object')
    return payload



def minimal_case_review(row: dict[str, Any]) -> dict[str, Any]:
    return {
        'case_key': row.get('case_key'),
        'review_path': row.get('review_path'),
        'retrieval_score': row.get('retrieval_score'),
        'matched_active_nodes': row.get('matched_active_nodes') or [],
        'matched_candidate_edges': row.get('matched_candidate_edges') or [],
        'why': row.get('why'),
    }



def minimal_intervention(row: dict[str, Any]) -> dict[str, Any]:
    return {
        'intervention_key': row.get('intervention_key'),
        'path': row.get('path'),
        'retrieval_score': row.get('retrieval_score'),
        'required_checks': row.get('required_checks') or [],
        'matched_question_mechanics': row.get('matched_question_mechanics') or [],
        'matched_source_of_truth_class': row.get('matched_source_of_truth_class') or [],
        'why': row.get('why'),
    }



def minimal_aggregate_note(row: dict[str, Any]) -> dict[str, Any]:
    return {
        'path': row.get('path'),
        'retrieval_score': row.get('retrieval_score'),
        'candidate_kind': row.get('candidate_kind'),
        'why': row.get('why'),
    }



def minimal_selected_candidate(row: dict[str, Any]) -> dict[str, Any]:
    return {
        'proposal_id': row.get('proposal_id'),
        'proposal_key': row.get('proposal_key'),
        'candidate_type': row.get('candidate_type'),
        'mechanism_family': row.get('mechanism_family'),
        'eligibility_mode': row.get('eligibility_mode'),
        'overlay_score': row.get('overlay_score'),
        'shadow_trial_score': row.get('shadow_trial_score'),
        'preview_only': bool(row.get('preview_only', True)),
        'injected': bool(row.get('injected', False)),
        'matched_active_nodes': row.get('matched_active_nodes') or [],
        'matched_candidate_edges': row.get('matched_candidate_edges') or [],
        'matched_required_checks': row.get('matched_required_checks') or [],
        'selection_blockers': row.get('selection_blockers') or [],
        'merge_recommended': bool(row.get('merge_recommended', False)),
        'merge_candidate_key': row.get('merge_candidate_key'),
    }



def minimal_skipped_candidate(row: dict[str, Any]) -> dict[str, Any]:
    return {
        'proposal_id': row.get('proposal_id'),
        'proposal_key': row.get('proposal_key'),
        'candidate_type': row.get('candidate_type'),
        'mechanism_family': row.get('mechanism_family'),
        'overlay_score': row.get('overlay_score'),
        'selection_blockers': row.get('selection_blockers') or [],
        'promotion_status': row.get('promotion_status'),
        'lifecycle_stage': row.get('lifecycle_stage'),
    }



def summarize_trial_overlay(bundle: dict[str, Any]) -> dict[str, Any]:
    overlay = bundle.get('trial_overlay') if isinstance(bundle.get('trial_overlay'), dict) else {}
    selected = [row for row in (overlay.get('selected_candidates') or []) if isinstance(row, dict)]
    skipped = [row for row in (overlay.get('skipped_candidates') or []) if isinstance(row, dict)]
    return {
        'enabled': bool(overlay.get('enabled', False)),
        'used': bool(overlay.get('used', False)),
        'preview_only': bool(overlay.get('preview_only', True)),
        'overlay_mode': overlay.get('overlay_mode'),
        'candidate_count_considered': int(overlay.get('candidate_count_considered') or 0),
        'candidate_count_positive_score': int(overlay.get('candidate_count_positive_score') or 0),
        'selected_count': len(selected),
        'injected_count': len([row for row in selected if bool(row.get('injected'))]),
        'selection_blocker_counts': overlay.get('selection_blocker_counts') or {},
        'selected_candidates': [minimal_selected_candidate(row) for row in selected],
        'skipped_candidates_preview': [minimal_skipped_candidate(row) for row in skipped[:12]],
        'experimental_candidate_ids': [coerce_string(row.get('proposal_id') or row.get('proposal_key')) for row in selected if coerce_string(row.get('proposal_id') or row.get('proposal_key'))],
    }



def summarize_shadow(bundle: dict[str, Any]) -> dict[str, Any]:
    shadow = bundle.get('shadow_evaluation') if isinstance(bundle.get('shadow_evaluation'), dict) else {}
    matches = [row for row in (shadow.get('top_matches') or []) if isinstance(row, dict)]
    return {
        'enabled': bool(shadow.get('enabled', False)),
        'proposal_count_considered': int(shadow.get('proposal_count_considered') or 0),
        'match_count': len(matches),
        'would_inject_count': len([row for row in matches if bool(row.get('would_inject'))]),
        'top_matches': [
            {
                'proposal_id': row.get('proposal_id'),
                'proposal_key': row.get('proposal_key'),
                'candidate_type': row.get('candidate_type'),
                'mechanism_family': row.get('mechanism_family'),
                'retrieval_score': row.get('retrieval_score'),
                'would_inject': bool(row.get('would_inject', False)),
                'matched_active_nodes': row.get('matched_active_nodes') or [],
                'matched_required_checks': row.get('matched_required_checks') or [],
            }
            for row in matches[:12]
        ],
    }



def main() -> int:
    args = parse_args()
    notes = parse_json_arg(args.notes_json, field='--notes-json')
    shadow_logging = parse_json_arg(args.shadow_logging_json, field='--shadow-logging-json')
    trial_logging = parse_json_arg(args.trial_logging_json, field='--trial-logging-json')
    lmd_logging = parse_json_arg(args.lmd_logging_json, field='--lmd-logging-json')
    trigger = parse_json_arg(args.trigger_json, field='--trigger-json')

    bundle_path = resolve_repo_path(args.bundle_path)
    bundle = read_json(bundle_path, default={}) or {}
    if not isinstance(bundle, dict):
        bundle = {}
    audit_path = audit_path_for_bundle(bundle_path)
    existing = read_json(audit_path, default={}) or {}
    if not isinstance(existing, dict):
        existing = {}

    results = bundle.get('results') if isinstance(bundle.get('results'), dict) else {}
    query_profile = bundle.get('query_profile') if isinstance(bundle.get('query_profile'), dict) else {}
    coverage = coverage_metrics_from_bundle(bundle)
    trial_overlay = summarize_trial_overlay(bundle)
    shadow_summary = summarize_shadow(bundle)
    case_key = coerce_string(args.case_key or bundle.get('case_key') or (existing.get('case_key') if isinstance(existing, dict) else ''))
    dispatch_id = coerce_string(args.dispatch_id or (existing.get('dispatch_id') if isinstance(existing, dict) else ''))
    research_run_id = coerce_string(args.research_run_id or (existing.get('research_run_id') if isinstance(existing, dict) else ''))

    audit = {
        'schema_version': 'v1',
        'generated_at': now_iso(),
        'case_key': case_key or None,
        'dispatch_id': dispatch_id or None,
        'research_run_id': research_run_id or None,
        'bundle_path': bundle_path_to_repo_relative(bundle_path),
        'audit_path': to_repo_relative(audit_path),
        'bundle_status': bundle.get('status'),
        'assignment_arm': bundle.get('assignment_arm'),
        'lmd_used': bool(bundle.get('lmd_used', False)),
        'usage_mode': bundle.get('usage_mode'),
        'lmd_tier': bundle.get('lmd_tier'),
        'control_preview': str(bundle.get('assignment_arm') or '').strip().lower() == 'control',
        'counterfactual_treatment_preview': str(bundle.get('assignment_arm') or '').strip().lower() == 'control' and bool(bundle.get('status') == 'control_preview'),
        'query_profile': query_profile,
        'case_mix': bundle.get('case_mix') or case_mix_from_query_profile(query_profile),
        'support_gate': ((bundle.get('debug') or {}).get('support_gate') or {}),
        'coverage': coverage,
        'provenance': bundle.get('provenance') or {},
        'retrieval': {
            'case_reviews': [minimal_case_review(row) for row in (results.get('case_reviews') or []) if isinstance(row, dict)],
            'active_interventions': [minimal_intervention(row) for row in (results.get('active_interventions') or []) if isinstance(row, dict)],
            'aggregate_notes': [minimal_aggregate_note(row) for row in (results.get('aggregate_notes') or []) if isinstance(row, dict)],
            'required_checks': results.get('required_checks') or [],
            'negative_checks': results.get('negative_checks') or [],
            'result_paths': bundle.get('result_paths') or [],
        },
        'shadow_evaluation': shadow_summary,
        'trial_overlay': trial_overlay,
        'logging': {
            'shadow': summarize_logging_result(shadow_logging),
            'trial': summarize_logging_result(trial_logging),
            'lmd': summarize_logging_result(lmd_logging),
        },
        'runtime': {
            'runtime_surface': notes.get('runtime_surface'),
            'persona': notes.get('persona') or notes.get('trigger_persona'),
            'dispatch_gate_status': notes.get('dispatch_gate_status') or {},
            'post_treatment_trigger': trigger or {},
        },
    }
    audit['audit_hash'] = sha256_jsonable({
        'case_key': audit['case_key'],
        'dispatch_id': audit['dispatch_id'],
        'bundle_path': audit['bundle_path'],
        'bundle_status': audit['bundle_status'],
        'assignment_arm': audit['assignment_arm'],
        'coverage': audit['coverage'],
        'trial_overlay': audit['trial_overlay'],
        'shadow_evaluation': audit['shadow_evaluation'],
        'logging': audit['logging'],
        'provenance': audit['provenance'],
    })

    audit_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(audit_path, audit, pretty=True)
    output = {
        'ok': True,
        'bundle_path': audit['bundle_path'],
        'audit_path': audit['audit_path'],
        'coverage_classification': coverage.get('classification'),
        'trial_selected_count': trial_overlay.get('selected_count'),
        'control_preview': audit.get('control_preview'),
    }
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
