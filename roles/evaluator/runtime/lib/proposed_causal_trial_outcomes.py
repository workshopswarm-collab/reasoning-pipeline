from __future__ import annotations

from typing import Any

from .proposed_causal_shadow_outcomes import (  # reuse deterministic downstream-evidence helpers
    _canonical_support_profile,
    _occurrence_support_profile,
    _projection_overlap_profile,
    load_case_artifacts,
)

JUDGE_VERSION = 'proposed-causal-trial-v1'

OUTCOME_THRESHOLDS = {
    'helpful_min_score': 3.5,
    'neutral_min_score': 1.0,
    'harmful_max_score': -2.5,
}

WEIGHTS = {
    'direct_non_intervention_support': 3.5,
    'direct_mixed_support': 2.5,
    'direct_weak_support': 1.0,
    'direct_contest': -4.5,
    'canonical_exact_support': 1.5,
    'canonical_merge_support': 0.7,
    'required_check_overlap': 1.0,
    'active_node_overlap': 0.3,
    'edge_overlap': 0.45,
    'injected_significant_case_no_signal_penalty': -1.5,
    'injected_reviewed_case_no_signal_penalty': -0.75,
    'merge_ambiguity_penalty': -0.35,
}



def judge_trial_row(
    trial_row: dict[str, Any],
    *,
    occurrence_rows: list[dict[str, Any]] | None = None,
    case_artifacts: dict[str, Any] | None = None,
) -> dict[str, Any]:
    case_key = str(trial_row.get('case_key') or '').strip()
    occurrence_rows = occurrence_rows or []
    case_artifacts = case_artifacts or load_case_artifacts(case_key)

    projection = case_artifacts.get('projection') or {}
    canonical = case_artifacts.get('canonical_suggestions') or {}
    review_exists = bool(case_artifacts.get('review_exists'))
    review_artifacts_present = review_exists or bool(projection) or bool(canonical)
    injected = bool(trial_row.get('injected'))
    preview_only = bool(trial_row.get('preview_only', True))

    occurrence_profile = _occurrence_support_profile(occurrence_rows)
    canonical_profile = _canonical_support_profile(trial_row, canonical)
    projection_profile = _projection_overlap_profile(trial_row, projection)

    positive_breakdown = {
        'direct_non_intervention_support': WEIGHTS['direct_non_intervention_support'] if occurrence_profile['non_intervention_support_count'] > 0 else 0.0,
        'direct_mixed_support': WEIGHTS['direct_mixed_support'] if occurrence_profile['support_count'] > 0 and occurrence_profile['non_intervention_support_count'] <= 0 and occurrence_profile['mixed_support_count'] > 0 else 0.0,
        'direct_weak_support': WEIGHTS['direct_weak_support'] if occurrence_profile['support_count'] > 0 and occurrence_profile['non_intervention_support_count'] <= 0 and occurrence_profile['mixed_support_count'] <= 0 and occurrence_profile['weak_support_count'] > 0 else 0.0,
        'canonical_exact_support': round(min(2, canonical_profile['exact_support_count']) * WEIGHTS['canonical_exact_support'], 6),
        'canonical_merge_support': round(min(2, canonical_profile['merge_support_count']) * WEIGHTS['canonical_merge_support'], 6),
        'required_check_overlap': round(min(2, projection_profile['required_check_overlap_count']) * WEIGHTS['required_check_overlap'], 6),
        'active_node_overlap': round(min(3, projection_profile['active_node_overlap_count']) * WEIGHTS['active_node_overlap'], 6),
        'edge_overlap': round(min(3, projection_profile['edge_overlap_count']) * WEIGHTS['edge_overlap'], 6),
    }

    negative_breakdown = {
        'direct_contest': WEIGHTS['direct_contest'] if occurrence_profile['contest_count'] > 0 else 0.0,
        'merge_ambiguity_penalty': WEIGHTS['merge_ambiguity_penalty'] if bool(((trial_row.get('notes') or {}).get('candidate_notes') or {}).get('merge_recommended')) else 0.0,
        'injected_significant_case_no_signal_penalty': 0.0,
        'injected_reviewed_case_no_signal_penalty': 0.0,
    }

    has_positive_signal = any(value > 0 for value in positive_breakdown.values())
    if injected and review_artifacts_present and not has_positive_signal:
        if projection_profile['projection_significant']:
            negative_breakdown['injected_significant_case_no_signal_penalty'] = WEIGHTS['injected_significant_case_no_signal_penalty']
        else:
            negative_breakdown['injected_reviewed_case_no_signal_penalty'] = WEIGHTS['injected_reviewed_case_no_signal_penalty']

    outcome_score = round(sum(positive_breakdown.values()) + sum(negative_breakdown.values()), 6)
    helpful_gate = (
        injected
        and (
            occurrence_profile['non_intervention_support_count'] > 0
            or (
                occurrence_profile['support_count'] > 0
                and (
                    canonical_profile['exact_support_count'] > 0
                    or (projection_profile['required_check_overlap_count'] + projection_profile['active_node_overlap_count'] + projection_profile['edge_overlap_count']) >= 2
                )
            )
        )
    )

    label = 'unclear'
    if not injected:
        label = 'unclear'
    elif occurrence_profile['contest_count'] > 0 or outcome_score <= OUTCOME_THRESHOLDS['harmful_max_score']:
        label = 'harmful'
    elif review_artifacts_present and outcome_score >= OUTCOME_THRESHOLDS['helpful_min_score'] and helpful_gate:
        label = 'helpful'
    elif review_artifacts_present and outcome_score >= OUTCOME_THRESHOLDS['neutral_min_score']:
        label = 'neutral'
    else:
        label = 'unclear'

    reasons: list[str] = []
    if preview_only and not injected:
        reasons.append('preview_only_not_injected')
    if not review_artifacts_present:
        reasons.append('no_review_artifacts')
    if occurrence_profile['non_intervention_support_count'] > 0:
        reasons.append('same_case_non_intervention_support')
    if occurrence_profile['mixed_support_count'] > 0:
        reasons.append('same_case_mixed_support')
    if occurrence_profile['weak_support_count'] > 0:
        reasons.append('same_case_weak_support')
    if occurrence_profile['contest_count'] > 0:
        reasons.append('same_case_contest')
    if canonical_profile['exact_support_count'] > 0:
        reasons.append('canonical_exact_support')
    if canonical_profile['merge_support_count'] > 0:
        reasons.append('canonical_merge_support')
    if projection_profile['required_check_overlap_count'] > 0:
        reasons.append('required_check_overlap')
    if projection_profile['active_node_overlap_count'] > 0:
        reasons.append('active_node_overlap')
    if projection_profile['edge_overlap_count'] > 0:
        reasons.append('edge_overlap')
    if negative_breakdown['injected_significant_case_no_signal_penalty'] < 0:
        reasons.append('injected_significant_case_no_signal')
    if negative_breakdown['injected_reviewed_case_no_signal_penalty'] < 0:
        reasons.append('injected_reviewed_case_no_signal')
    if negative_breakdown['merge_ambiguity_penalty'] < 0:
        reasons.append('merge_ambiguity_penalty')

    return {
        'outcome_label': label,
        'outcome_score': outcome_score,
        'outcome_favored': True if label == 'helpful' else False,
        'judge_version': JUDGE_VERSION,
        'judged_at': None,
        'outcome_metadata': {
            'thresholds': OUTCOME_THRESHOLDS,
            'weights': WEIGHTS,
            'reasons': reasons,
            'review_artifacts_present': review_artifacts_present,
            'review_exists': review_exists,
            'injected': injected,
            'preview_only': preview_only,
            'occurrence_profile': occurrence_profile,
            'canonical_profile': canonical_profile,
            'projection_profile': projection_profile,
            'positive_breakdown': positive_breakdown,
            'negative_breakdown': negative_breakdown,
            'helpful_gate': helpful_gate,
        },
    }
