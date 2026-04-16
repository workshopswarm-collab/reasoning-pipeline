from __future__ import annotations

from pathlib import Path
from typing import Any

from .io import read_json
from .paths import CAUSAL_MAP_ROOT

SUMMARY_PATH = CAUSAL_MAP_ROOT / 'generated' / 'proposed-causal-candidates-summary.json'



def _to_set(values: Any) -> set[str]:
    if isinstance(values, list):
        return {str(item).strip() for item in values if str(item).strip()}
    return set()



def _distribution_keys(dist: Any, key: str) -> set[str]:
    if not isinstance(dist, dict):
        return set()
    bucket = dist.get(key) or {}
    if isinstance(bucket, dict):
        return {str(item).strip() for item in bucket.keys() if str(item).strip()}
    return set()



def load_shadow_candidates(summary_path: Path = SUMMARY_PATH) -> list[dict[str, Any]]:
    payload = read_json(summary_path, default={}) or {}
    rows: list[dict[str, Any]] = []
    for row in payload.get('proposals') or []:
        if not isinstance(row, dict):
            continue
        if bool(row.get('duplicate_of_live_graph')):
            continue
        if str(row.get('promotion_status') or '') == 'duplicate_of_live_graph':
            continue
        rows.append(row)
    return rows



def _current_required_checks(bundle: dict[str, Any]) -> set[str]:
    checks = []
    for row in ((bundle.get('causal_context') or {}).get('required_checks') or []):
        if isinstance(row, dict):
            key = str(row.get('check_key') or '').strip()
            if key:
                checks.append(key)
    return set(checks)



def _current_context(bundle: dict[str, Any]) -> dict[str, set[str]]:
    profile = bundle.get('query_profile') or {}
    causal_context = bundle.get('causal_context') or {}
    return {
        'active_nodes': _to_set(causal_context.get('active_nodes')),
        'candidate_edges': _to_set(causal_context.get('matched_edges')),
        'contested_edges': _to_set(causal_context.get('contested_edges')),
        'required_checks': _current_required_checks(bundle),
        'question_mechanics': _to_set(profile.get('question_mechanics')),
        'source_of_truth_class': _to_set(profile.get('source_of_truth_class')),
        'platforms': _to_set([profile.get('platform')] if profile.get('platform') else []),
        'categories': _to_set([profile.get('category')] if profile.get('category') else []),
    }



def _score_candidate(candidate: dict[str, Any], bundle: dict[str, Any]) -> dict[str, Any]:
    current = _current_context(bundle)
    stats_metadata = candidate.get('stats_metadata') or {}
    observed_active_nodes = _to_set(stats_metadata.get('observed_active_nodes'))
    observed_candidate_edges = _to_set(stats_metadata.get('observed_candidate_edges'))
    observed_contested_edges = _to_set(stats_metadata.get('observed_contested_edges'))
    observed_required_checks = _to_set(stats_metadata.get('observed_required_checks'))
    context_distribution = candidate.get('context_distribution') or {}

    matched_active_nodes = sorted(current['active_nodes'] & (observed_active_nodes | {str(candidate.get('source_node_key') or '').strip(), str(candidate.get('target_node_key') or '').strip()}))
    matched_candidate_edges = sorted(current['candidate_edges'] & observed_candidate_edges)
    matched_contested_edges = sorted(current['contested_edges'] & observed_contested_edges)
    matched_required_checks = sorted(current['required_checks'] & observed_required_checks)
    matched_question_mechanics = sorted(current['question_mechanics'] & _distribution_keys(context_distribution, 'question_mechanics'))
    matched_source_of_truth = sorted(current['source_of_truth_class'] & _distribution_keys(context_distribution, 'source_of_truth_class'))
    matched_platforms = sorted(current['platforms'] & _distribution_keys(context_distribution, 'platforms'))
    matched_categories = sorted(current['categories'] & _distribution_keys(context_distribution, 'categories'))

    score_breakdown = {
        'active_nodes': 0.65 * len(matched_active_nodes),
        'candidate_edges': 0.6 * len(matched_candidate_edges),
        'contested_edges': 0.5 * len(matched_contested_edges),
        'required_checks': 0.75 * len(matched_required_checks),
        'question_mechanics': 0.35 * len(matched_question_mechanics),
        'source_of_truth_class': 0.35 * len(matched_source_of_truth),
        'platforms': 0.2 * len(matched_platforms),
        'categories': 0.2 * len(matched_categories),
        'non_intervention_support': 0.18 * float(candidate.get('non_intervention_support_case_count') or 0),
        'distinct_cases': 0.08 * float(candidate.get('distinct_case_count') or 0),
        'shadow_positive': 0.08 * float(candidate.get('shadow_positive_count') or 0),
        'genericity_penalty': -1.0 * float(candidate.get('genericity_penalty') or 0),
        'merge_penalty': -0.5 if bool(candidate.get('merge_recommended')) else 0.0,
        'intervention_only_penalty': -0.22 * float(candidate.get('intervention_only_support_case_count') or 0),
        'heuristic_only_penalty': -0.15 * float(candidate.get('heuristic_only_support_case_count') or 0),
    }
    retrieval_score = round(sum(score_breakdown.values()), 6)
    would_inject = retrieval_score >= 1.0 and not bool(candidate.get('merge_recommended'))

    return {
        'proposal_id': str(candidate.get('proposal_id') or ''),
        'proposal_key': str(candidate.get('proposal_key') or ''),
        'candidate_type': str(candidate.get('candidate_type') or ''),
        'mechanism_family': str(candidate.get('mechanism_family') or 'unassigned'),
        'dominant_proposal_source': str(candidate.get('dominant_proposal_source') or ''),
        'promotion_status': str(candidate.get('promotion_status') or ''),
        'lifecycle_stage': str(candidate.get('lifecycle_stage') or ''),
        'retrieval_score': retrieval_score,
        'would_inject': would_inject,
        'matched_active_nodes': matched_active_nodes,
        'matched_candidate_edges': matched_candidate_edges,
        'matched_contested_edges': matched_contested_edges,
        'matched_required_checks': matched_required_checks,
        'matched_question_mechanics': matched_question_mechanics,
        'matched_source_of_truth_class': matched_source_of_truth,
        'matched_platforms': matched_platforms,
        'matched_categories': matched_categories,
        'score_breakdown': score_breakdown,
        'notes': {
            'non_intervention_support_case_count': int(candidate.get('non_intervention_support_case_count') or 0),
            'intervention_only_support_case_count': int(candidate.get('intervention_only_support_case_count') or 0),
            'heuristic_only_support_case_count': int(candidate.get('heuristic_only_support_case_count') or 0),
            'merge_recommended': bool(candidate.get('merge_recommended')),
            'merge_candidate_key': str(candidate.get('merge_candidate_key') or ''),
        },
    }



def evaluate_shadow_candidates(bundle: dict[str, Any], *, limit: int = 5, summary_path: Path = SUMMARY_PATH) -> dict[str, Any]:
    candidates = load_shadow_candidates(summary_path)
    results = [_score_candidate(candidate, bundle) for candidate in candidates]
    filtered = [row for row in results if row['retrieval_score'] > 0]
    filtered.sort(key=lambda row: (-row['retrieval_score'], row['candidate_type'], row['proposal_key']))
    top = []
    for index, row in enumerate(filtered[: max(0, limit)], start=1):
        top.append({**row, 'rank_position': index})
    return {
        'enabled': True,
        'summary_path': str(summary_path),
        'proposal_count_considered': len(candidates),
        'match_count': len(top),
        'top_matches': top,
    }
