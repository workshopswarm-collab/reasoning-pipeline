from __future__ import annotations

from typing import Any

from .io import read_json
from .paths import CAUSAL_MAP_ROOT

FAMILY_POLICY_PATH = CAUSAL_MAP_ROOT / 'family-policies.json'

DEFAULT_POLICY = {
    'description': '',
    'enabled': True,
    'max_shadow_candidates': 6,
    'max_trial_candidates': 2,
    'max_active_nodes': 6,
    'max_active_edges': 4,
    'min_shadow_judged_count_for_trial': 4,
    'min_shadow_helpful_count_for_trial': 1,
    'min_shadow_mean_score_for_trial': 0.5,
    'min_non_intervention_support_cases_for_trial': 2,
    'max_genericity_for_trial': 0.25,
    'max_duplicate_similarity_for_trial': 0.85,
    'max_promotion_ready_candidates': 1,
    'min_trial_judged_count_for_promotion': 2,
    'min_trial_helpful_count_for_promotion': 1,
    'min_trial_shrunken_utility_for_promotion': 0.25,
    'max_trial_harmful_rate_for_promotion': 0.34,
    'max_contest_case_count_for_promotion': 1,
    'max_genericity_for_promotion': 0.22,
    'notes': {},
}

DEFAULT_EXPLORATORY_TRIAL = {
    'enabled': False,
    'max_candidates': 0,
    'require_base_proposal_threshold': False,
    'min_shadow_judged_count': 0,
    'min_shadow_helpful_count': 0,
    'min_non_intervention_support_cases': 1,
    'min_shadow_trial_score': 0.0,
}



def normalize_family_policy(policy: dict[str, Any], *, mechanism_family: str | None = None) -> dict[str, Any]:
    row = dict(DEFAULT_POLICY)
    row.update(policy or {})
    family = str(mechanism_family or row.get('mechanism_family') or '').strip() or 'unassigned'
    row['mechanism_family'] = family
    row['description'] = str(row.get('description') or '').strip()
    row['enabled'] = bool(row.get('enabled', True))
    for key in [
        'max_shadow_candidates',
        'max_trial_candidates',
        'max_active_nodes',
        'max_active_edges',
        'min_shadow_judged_count_for_trial',
        'min_shadow_helpful_count_for_trial',
        'min_non_intervention_support_cases_for_trial',
        'max_promotion_ready_candidates',
        'min_trial_judged_count_for_promotion',
        'min_trial_helpful_count_for_promotion',
        'max_contest_case_count_for_promotion',
    ]:
        row[key] = max(0, int(row.get(key, DEFAULT_POLICY[key]) or 0))
    for key in [
        'min_shadow_mean_score_for_trial',
        'max_genericity_for_trial',
        'max_duplicate_similarity_for_trial',
        'min_trial_shrunken_utility_for_promotion',
        'max_trial_harmful_rate_for_promotion',
        'max_genericity_for_promotion',
    ]:
        row[key] = float(row.get(key, DEFAULT_POLICY[key]) or 0.0)
    notes = row.get('notes') or {}
    row['notes'] = notes if isinstance(notes, dict) else {'raw': notes}
    return row



def load_family_policy_payload() -> dict[str, Any]:
    payload = read_json(FAMILY_POLICY_PATH, default={}) or {}
    if not isinstance(payload, dict):
        return {'schema_version': 'v1', 'policies': []}
    policies = payload.get('policies') or []
    if not isinstance(policies, list):
        policies = []
    return {
        'schema_version': str(payload.get('schema_version') or 'v1'),
        'policies': [policy for policy in policies if isinstance(policy, dict)],
    }



def load_family_policies() -> dict[str, dict[str, Any]]:
    payload = load_family_policy_payload()
    rows: dict[str, dict[str, Any]] = {}
    for policy in payload['policies']:
        normalized = normalize_family_policy(policy)
        rows[normalized['mechanism_family']] = normalized
    if 'unassigned' not in rows:
        rows['unassigned'] = normalize_family_policy({'enabled': False}, mechanism_family='unassigned')
    return rows



def family_policy_for(mechanism_family: str, *, loaded: dict[str, dict[str, Any]] | None = None) -> dict[str, Any]:
    rows = loaded or load_family_policies()
    key = str(mechanism_family or '').strip() or 'unassigned'
    if key in rows:
        return normalize_family_policy(rows[key], mechanism_family=key)
    return normalize_family_policy({}, mechanism_family=key)



def exploratory_trial_for(policy: dict[str, Any] | None) -> dict[str, Any]:
    notes = (policy or {}).get('notes') or {}
    raw = notes.get('exploratory_trial') or {}
    if not isinstance(raw, dict):
        raw = {'enabled': False}
    row = dict(DEFAULT_EXPLORATORY_TRIAL)
    row.update(raw)
    row['enabled'] = bool(row.get('enabled', False))
    row['max_candidates'] = max(0, int(row.get('max_candidates', DEFAULT_EXPLORATORY_TRIAL['max_candidates']) or 0))
    row['require_base_proposal_threshold'] = bool(row.get('require_base_proposal_threshold', DEFAULT_EXPLORATORY_TRIAL['require_base_proposal_threshold']))
    row['min_shadow_judged_count'] = max(0, int(row.get('min_shadow_judged_count', DEFAULT_EXPLORATORY_TRIAL['min_shadow_judged_count']) or 0))
    row['min_shadow_helpful_count'] = max(0, int(row.get('min_shadow_helpful_count', DEFAULT_EXPLORATORY_TRIAL['min_shadow_helpful_count']) or 0))
    row['min_non_intervention_support_cases'] = max(0, int(row.get('min_non_intervention_support_cases', DEFAULT_EXPLORATORY_TRIAL['min_non_intervention_support_cases']) or 0))
    row['min_shadow_trial_score'] = float(row.get('min_shadow_trial_score', DEFAULT_EXPLORATORY_TRIAL['min_shadow_trial_score']) or 0.0)
    return row
