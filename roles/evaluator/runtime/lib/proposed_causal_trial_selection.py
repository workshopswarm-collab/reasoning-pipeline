from __future__ import annotations

from pathlib import Path
from typing import Any

from .io import read_json
from .paths import CAUSAL_MAP_ROOT
from .phase11_retrieval_policy import load_phase11_retrieval_policy, phase11_weight

SUMMARY_PATH = CAUSAL_MAP_ROOT / 'generated' / 'proposed-causal-candidates-summary.json'
MAX_SELECTED_TOTAL = 2
MAX_SELECTED_NODES = 2
MAX_SELECTED_EDGES = 1
MAX_SELECTED_PER_FAMILY = 1
SELECTION_POLICY_VERSION = 'proposed-causal-trial-overlay-v2'



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



def _safe_int(value: Any) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def _safe_float(*values: Any) -> float:
    for value in values:
        if value in (None, ''):
            continue
        try:
            return float(value)
        except Exception:
            continue
    return 0.0


def _current_live_trial_item_count(bundle: dict[str, Any]) -> int:
    causal_context = bundle.get('causal_context') or {}
    count = 0
    for row in (causal_context.get('active_node_metadata') or []):
        if isinstance(row, dict) and str(row.get('lifecycle_stage') or '').strip().lower() == 'trial':
            count += 1
    for row in (causal_context.get('matched_edge_metadata') or []):
        if isinstance(row, dict) and str(row.get('lifecycle_stage') or '').strip().lower() == 'trial':
            count += 1
    return count


def _current_live_family_state(bundle: dict[str, Any]) -> dict[str, dict[str, int]]:
    retrieval_policy = bundle.get('retrieval_policy') or {}
    state = retrieval_policy.get('live_graph_family_state') or {}
    return state if isinstance(state, dict) else {}


def _family_policy_caps(bundle: dict[str, Any]) -> dict[str, dict[str, int]]:
    retrieval_policy = bundle.get('retrieval_policy') or {}
    caps = retrieval_policy.get('live_graph_family_policy_caps') or {}
    return caps if isinstance(caps, dict) else {}


def _family_crowding_penalty(candidate: dict[str, Any], bundle: dict[str, Any]) -> dict[str, Any]:
    family = str(candidate.get('mechanism_family') or 'unassigned').strip() or 'unassigned'
    state = _current_live_family_state(bundle).get(family) or {'trial_total': 0, 'active_nodes': 0, 'active_edges': 0}
    caps = (_family_policy_caps(bundle).get(family) or _family_policy_caps(bundle).get('unassigned') or {})
    current = _safe_int(state.get('trial_total'))
    limit = _safe_int(caps.get('max_trial_candidates'))
    if limit <= 0:
        penalty = 0.45 if current > 0 else 0.0
        ratio = None
    else:
        ratio = round(current / float(limit), 3)
        if ratio > 1.0:
            penalty = round(0.5 + (ratio - 1.0) * 0.25, 3)
        elif ratio >= 1.0:
            penalty = 0.25
        elif ratio >= 0.75:
            penalty = round(0.08 + (ratio - 0.75) * 0.28, 3)
        else:
            penalty = 0.0
    return {'current': current, 'limit': limit, 'ratio': ratio, 'penalty': penalty}


def _dispatch_overlay_caps(bundle: dict[str, Any], limit: int) -> dict[str, int]:
    live_trial_item_count = _current_live_trial_item_count(bundle)
    dynamic_total = max(0, min(max(0, limit), MAX_SELECTED_TOTAL) - (1 if live_trial_item_count > 0 else 0))
    return {
        'requested_limit': max(0, limit),
        'max_selected_total': dynamic_total,
        'max_selected_nodes': MAX_SELECTED_NODES,
        'max_selected_edges': MAX_SELECTED_EDGES,
        'max_selected_per_family': MAX_SELECTED_PER_FAMILY,
        'current_live_trial_item_count': live_trial_item_count,
    }


def _quantile(values: list[float], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * fraction))))
    return float(ordered[idx])


def _build_metric_profile(values: list[float]) -> dict[str, float]:
    clean = sorted(float(value) for value in values if value is not None)
    if not clean:
        return {'count': 0.0, 'p25': 0.0, 'p50': 0.0, 'p90': 0.0, 'max': 0.0}
    return {
        'count': float(len(clean)),
        'p25': _quantile(clean, 0.25),
        'p50': _quantile(clean, 0.50),
        'p90': _quantile(clean, 0.90),
        'max': float(clean[-1]),
    }


def _normalized_reward(value: float, profile: dict[str, float] | None) -> float:
    numeric = float(value)
    if numeric <= 0:
        return 0.0
    profile = profile or {}
    count = _safe_int(profile.get('count'))
    max_value = _safe_float(profile.get('max'))
    if count <= 2:
        fallback = max(1.0, abs(numeric), max_value)
        return round(min(1.5, max(0.0, numeric / fallback)), 3)
    low = max(0.0, _safe_float(profile.get('p25'), profile.get('p50')))
    high = max(low + 1e-6, _safe_float(profile.get('p90'), profile.get('max')))
    if high <= low + 1e-6:
        return round(min(1.5, numeric / max(1.0, abs(numeric), max_value)), 3)
    return round(min(1.5, max(0.0, (numeric - low) / (high - low))), 3)


def _normalized_penalty(value: float, profile: dict[str, float] | None) -> float:
    numeric = float(value)
    if numeric <= 0:
        return 0.0
    profile = profile or {}
    count = _safe_int(profile.get('count'))
    max_value = _safe_float(profile.get('max'))
    if count <= 2:
        fallback = max(1.0, abs(numeric), max_value)
        return round(min(1.5, max(0.0, numeric / fallback)), 3)
    low = max(0.0, _safe_float(profile.get('p50'), profile.get('p25')))
    high = max(low + 1e-6, _safe_float(profile.get('p90'), profile.get('max')))
    if high <= low + 1e-6:
        return round(min(1.5, numeric / max(1.0, abs(numeric), max_value)), 3)
    return round(min(1.5, max(0.0, (numeric - low) / (high - low))), 3)


def _overlay_distribution_profiles(candidates: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    def vals(field: str) -> list[float]:
        out=[]
        for row in candidates:
            value = row.get(field)
            if value in (None, ''):
                continue
            out.append(_safe_float(value))
        return out
    def positive_vals(field: str) -> list[float]:
        return [value for value in vals(field) if value > 0]
    return {
        'shadow_trial_score': _build_metric_profile(positive_vals('shadow_trial_score')),
        'trial_shrunken_utility': _build_metric_profile(positive_vals('trial_shrunken_utility')),
        'trial_helpful_count': _build_metric_profile(vals('trial_helpful_count')),
        'shadow_helpful_count': _build_metric_profile(vals('shadow_helpful_count')),
        'non_intervention_support_case_count': _build_metric_profile(vals('non_intervention_support_case_count')),
        'distinct_case_count': _build_metric_profile(vals('distinct_case_count')),
        'genericity_penalty': _build_metric_profile(vals('genericity_penalty')),
        'shadow_harmful_count': _build_metric_profile(vals('shadow_harmful_count')),
        'trial_harmful_rate': _build_metric_profile(vals('trial_harmful_rate')),
    }


def load_trial_candidates(summary_path: Path = SUMMARY_PATH) -> list[dict[str, Any]]:
    payload = read_json(summary_path, default={}) or {}
    rows: list[dict[str, Any]] = []
    for row in payload.get('proposals') or []:
        if not isinstance(row, dict):
            continue
        if bool(row.get('duplicate_of_live_graph')):
            continue
        if str(row.get('promotion_status') or '') == 'duplicate_of_live_graph':
            continue
        if str(row.get('lifecycle_stage') or '') != 'trial_candidate':
            continue
        if not bool((row.get('trial_readiness') or {}).get('eligible')):
            continue
        if bool(row.get('merge_recommended')):
            continue
        shadow_trial_score = row.get('shadow_trial_score')
        if shadow_trial_score in (None, '') or float(shadow_trial_score) < 0.0:
            continue
        rows.append(row)
    return rows



def _current_required_checks(bundle: dict[str, Any]) -> set[str]:
    checks = []
    for row in ((bundle.get('causal_context') or {}).get('required_checks') or []):
        if isinstance(row, dict):
            key = str(row.get('check_key') or '').strip()
        else:
            key = str(row).strip()
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
        'source_of_truth_class': _to_set([profile.get('source_of_truth_class')] if profile.get('source_of_truth_class') else []),
        'platforms': _to_set([profile.get('platform')] if profile.get('platform') else []),
        'categories': _to_set([profile.get('category')] if profile.get('category') else []),
    }



def _score_candidate(
    candidate: dict[str, Any],
    bundle: dict[str, Any],
    profiles: dict[str, dict[str, float]] | None = None,
    phase11_policy: dict[str, Any] | None = None,
) -> dict[str, Any]:
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

    profiles = profiles or {}
    phase11_policy = phase11_policy or {}
    shadow_trial_score = _safe_float(candidate.get('shadow_trial_score'))
    trial_shrunken_utility = _safe_float(candidate.get('trial_shrunken_utility'))
    trial_harmful_rate = _safe_float(candidate.get('trial_harmful_rate'))
    family_trial_rank = candidate.get('family_trial_rank')
    rank_bonus = 0.0
    if family_trial_rank not in (None, ''):
        try:
            rank_bonus = max(0.0, 4.0 - float(family_trial_rank)) * 0.08
        except Exception:
            rank_bonus = 0.0
    family_crowding = _family_crowding_penalty(candidate, bundle)

    score_breakdown = {
        'active_nodes': 0.65 * len(matched_active_nodes),
        'candidate_edges': 0.6 * len(matched_candidate_edges),
        'contested_edges': 0.45 * len(matched_contested_edges),
        'required_checks': 0.75 * len(matched_required_checks),
        'question_mechanics': 0.35 * len(matched_question_mechanics),
        'source_of_truth_class': 0.35 * len(matched_source_of_truth),
        'platforms': 0.2 * len(matched_platforms),
        'categories': 0.2 * len(matched_categories),
        'shadow_trial_score': round(phase11_weight(phase11_policy, 'overlay', 'shadow_trial_score', default=1.05) * _normalized_reward(shadow_trial_score, profiles.get('shadow_trial_score')), 3),
        'trial_shrunken_utility': round(phase11_weight(phase11_policy, 'overlay', 'trial_shrunken_utility', default=0.95) * _normalized_reward(trial_shrunken_utility, profiles.get('trial_shrunken_utility')), 3),
        'trial_helpful': round(phase11_weight(phase11_policy, 'overlay', 'trial_helpful', default=0.55) * _normalized_reward(_safe_float(candidate.get('trial_helpful_count') or 0), profiles.get('trial_helpful_count')), 3),
        'shadow_helpful': round(phase11_weight(phase11_policy, 'overlay', 'shadow_helpful', default=0.45) * _normalized_reward(_safe_float(candidate.get('shadow_helpful_count') or 0), profiles.get('shadow_helpful_count')), 3),
        'non_intervention_support': round(phase11_weight(phase11_policy, 'overlay', 'non_intervention_support', default=0.55) * _normalized_reward(_safe_float(candidate.get('non_intervention_support_case_count') or 0), profiles.get('non_intervention_support_case_count')), 3),
        'distinct_cases': round(phase11_weight(phase11_policy, 'overlay', 'distinct_cases', default=0.32) * _normalized_reward(_safe_float(candidate.get('distinct_case_count') or 0), profiles.get('distinct_case_count')), 3),
        'rank_bonus': rank_bonus,
        'genericity_penalty': round(-phase11_weight(phase11_policy, 'overlay', 'genericity_penalty', default=0.70) * _normalized_penalty(_safe_float(candidate.get('genericity_penalty') or 0), profiles.get('genericity_penalty')), 3),
        'harmful_shadow_penalty': round(-phase11_weight(phase11_policy, 'overlay', 'harmful_shadow_penalty', default=0.55) * _normalized_penalty(_safe_float(candidate.get('shadow_harmful_count') or 0), profiles.get('shadow_harmful_count')), 3),
        'trial_harmful_rate_penalty': round(-phase11_weight(phase11_policy, 'overlay', 'trial_harmful_rate_penalty', default=0.65) * _normalized_penalty(trial_harmful_rate, profiles.get('trial_harmful_rate')), 3),
        'family_crowding_penalty': round(-phase11_weight(phase11_policy, 'overlay', 'family_crowding_penalty', default=0.90) * _safe_float(family_crowding.get('penalty')), 3),
        'merge_penalty': -phase11_weight(phase11_policy, 'overlay', 'merge_penalty', default=0.75) if bool(candidate.get('merge_recommended')) else 0.0,
    }
    overlay_score = round(sum(score_breakdown.values()), 6)
    preview_selected = overlay_score > 0

    return {
        'proposal_id': str(candidate.get('proposal_id') or ''),
        'proposal_key': str(candidate.get('proposal_key') or ''),
        'candidate_type': str(candidate.get('candidate_type') or ''),
        'mechanism_family': str(candidate.get('mechanism_family') or 'unassigned'),
        'dominant_proposal_source': str(candidate.get('dominant_proposal_source') or ''),
        'promotion_status': str(candidate.get('promotion_status') or ''),
        'lifecycle_stage': str(candidate.get('lifecycle_stage') or ''),
        'overlay_score': overlay_score,
        'preview_selected': preview_selected,
        'preview_only': True,
        'injected': False,
        'overlay_mode': 'preview_only',
        'shadow_trial_score': shadow_trial_score,
        'family_trial_rank': candidate.get('family_trial_rank'),
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
            'shadow_helpful_count': int(candidate.get('shadow_helpful_count') or 0),
            'shadow_harmful_count': int(candidate.get('shadow_harmful_count') or 0),
            'shadow_judged_count': int(candidate.get('shadow_judged_count') or 0),
            'trial_helpful_count': int(candidate.get('trial_helpful_count') or 0),
            'trial_judged_count': int(candidate.get('trial_judged_count') or 0),
            'trial_shrunken_utility': trial_shrunken_utility,
            'trial_harmful_rate': trial_harmful_rate,
            'non_intervention_support_case_count': int(candidate.get('non_intervention_support_case_count') or 0),
            'merge_recommended': bool(candidate.get('merge_recommended')),
            'merge_candidate_key': str(candidate.get('merge_candidate_key') or ''),
            'trial_readiness': candidate.get('trial_readiness') or {},
            'family_policy': candidate.get('family_policy') or {},
            'family_crowding': family_crowding,
        },
    }



def evaluate_trial_candidates(bundle: dict[str, Any], *, limit: int = MAX_SELECTED_TOTAL, summary_path: Path = SUMMARY_PATH, phase11_policy: dict[str, Any] | None = None) -> dict[str, Any]:
    candidates = load_trial_candidates(summary_path)
    distribution_profiles = _overlay_distribution_profiles(candidates)
    phase11_policy = phase11_policy or load_phase11_retrieval_policy()
    results = [_score_candidate(candidate, bundle, distribution_profiles, phase11_policy) for candidate in candidates]
    filtered: list[dict[str, Any]] = []
    skipped_candidates: list[dict[str, Any]] = []
    selection_blocker_counts: dict[str, int] = {}
    for row in results:
        if row['overlay_score'] > 0 and row['preview_selected']:
            filtered.append(row)
            continue
        skipped = {
            **row,
            'selection_blockers': ['non_positive_overlay_score'],
        }
        skipped_candidates.append(skipped)
        selection_blocker_counts['non_positive_overlay_score'] = selection_blocker_counts.get('non_positive_overlay_score', 0) + 1
    filtered.sort(key=lambda row: (-row['overlay_score'], row['candidate_type'], row['proposal_key']))

    caps = _dispatch_overlay_caps(bundle, limit)
    dynamic_total_limit = caps['max_selected_total']
    selected: list[dict[str, Any]] = []
    node_count = 0
    edge_count = 0
    family_counts: dict[str, int] = {}
    for row in filtered:
        family = str(row.get('mechanism_family') or 'unassigned').strip() or 'unassigned'
        blockers: list[str] = []
        if len(selected) >= dynamic_total_limit:
            blockers.append('dispatch_total_cap_reached')
        if row['candidate_type'] == 'node' and node_count >= MAX_SELECTED_NODES:
            blockers.append('dispatch_node_cap_reached')
        if row['candidate_type'] == 'edge' and edge_count >= MAX_SELECTED_EDGES:
            blockers.append('dispatch_edge_cap_reached')
        if family_counts.get(family, 0) >= MAX_SELECTED_PER_FAMILY:
            blockers.append('dispatch_family_cap_reached')
        if blockers:
            skipped_candidates.append({**row, 'selection_blockers': blockers})
            for blocker in blockers:
                selection_blocker_counts[blocker] = selection_blocker_counts.get(blocker, 0) + 1
            continue
        if row['candidate_type'] == 'node':
            node_count += 1
        elif row['candidate_type'] == 'edge':
            edge_count += 1
        family_counts[family] = family_counts.get(family, 0) + 1
        selected.append({**row, 'rank_position': len(selected) + 1})

    return {
        'enabled': True,
        'preview_only': True,
        'overlay_mode': 'preview_only',
        'summary_path': str(summary_path),
        'selection_policy_version': SELECTION_POLICY_VERSION,
        'selection_caps': caps,
        'distribution_profiles': distribution_profiles,
        'phase11_learned_policy': phase11_policy,
        'candidate_count_considered': len(candidates),
        'candidate_count_positive_score': len(filtered),
        'selected_count': len(selected),
        'selection_blocker_counts': dict(sorted(selection_blocker_counts.items())),
        'selected_candidates': selected,
        'skipped_candidates': skipped_candidates,
    }
