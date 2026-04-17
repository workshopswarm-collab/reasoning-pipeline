from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

from .causal_family_policy import family_policy_for, load_family_policies, normalize_family_policy
from .io import read_json, write_json
from .paths import CAUSAL_MAP_ROOT, ensure_parent

PROVISIONAL_FAMILY_POLICIES_PATH = CAUSAL_MAP_ROOT / 'provisional-family-policies.generated.json'
FAMILY_AUTOPOLICY_REPORT_JSON_PATH = CAUSAL_MAP_ROOT / 'generated' / 'family-autopolicy-report.json'
FAMILY_AUTOPOLICY_REPORT_MD_PATH = CAUSAL_MAP_ROOT / 'generated' / 'family-autopolicy-report.md'
PROVISIONAL_FAMILY_REGISTRY_JSON_PATH = CAUSAL_MAP_ROOT / 'generated' / 'provisional-family-registry.json'

POLICY_SOURCE = 'generated_provisional_shadow'
IMPOSSIBLE_INT = 999
IMPOSSIBLE_FLOAT = 999.0



def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))



def sort_families_by_support(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        rows,
        key=lambda row: (
            -int(row.get('source_occurrence_count') or 0),
            -int(row.get('distinct_case_count') or 0),
            str(row.get('family_key') or ''),
        ),
    )



def compute_health_score(row: dict[str, Any]) -> float:
    occurrence_score = min(1.0, float(row.get('source_occurrence_count') or 0) / 60.0)
    case_score = min(1.0, float(row.get('distinct_case_count') or 0) / 12.0)
    persona_score = min(1.0, float(row.get('distinct_persona_count') or 0) / 4.0)
    candidate_score = min(1.0, float(row.get('candidate_count') or 0) / 10.0)
    score = 0.45 * occurrence_score + 0.30 * case_score + 0.15 * persona_score + 0.10 * candidate_score
    if str(row.get('canonical_family') or 'unassigned') == 'unassigned':
        score -= 0.15
    if str(row.get('bridge_status') or '') == 'mapped_provisional':
        score += 0.05
    return round(clamp(score, 0.0, 1.0), 4)



def shadow_enablement(row: dict[str, Any], *, base_policy: dict[str, Any]) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    occurrences = int(row.get('source_occurrence_count') or 0)
    cases = int(row.get('distinct_case_count') or 0)
    personas = int(row.get('distinct_persona_count') or 0)
    canonical_family = str(row.get('canonical_family') or 'unassigned')
    if canonical_family == 'unassigned':
        candidate_count = int(row.get('candidate_count') or 0)
        if occurrences < 20:
            reasons.append('novel_occurrence_mass_below_minimum')
        if cases < 4:
            reasons.append('novel_case_breadth_below_minimum')
        if personas < 2:
            reasons.append('novel_persona_breadth_below_minimum')
        if candidate_count < 2:
            reasons.append('novel_candidate_count_below_minimum')
    else:
        if not bool(base_policy.get('enabled', True)):
            reasons.append('parent_policy_disabled')
            return False, reasons
        if occurrences < 3:
            reasons.append('mapped_occurrence_mass_below_minimum')
        if cases < 1:
            reasons.append('mapped_case_breadth_below_minimum')
    return len(reasons) == 0, reasons



def shadow_budget(row: dict[str, Any], *, base_policy: dict[str, Any], enabled: bool) -> int:
    if not enabled:
        return 0
    occurrences = int(row.get('source_occurrence_count') or 0)
    cases = int(row.get('distinct_case_count') or 0)
    candidates = max(1, int(row.get('candidate_count') or 0))
    canonical_family = str(row.get('canonical_family') or 'unassigned')
    budget = 1
    if occurrences >= 15 or cases >= 4:
        budget = 2
    if occurrences >= 50 or cases >= 10:
        budget = 3
    if canonical_family == 'unassigned':
        budget = min(budget, 1)
        base_cap = max(1, int(base_policy.get('max_shadow_candidates') or 0))
    else:
        base_cap = max(0, int(base_policy.get('max_shadow_candidates') or 0))
    budget = min(budget, candidates, base_cap)
    return max(0, budget)



def make_shadow_only_notes(base_policy: dict[str, Any], row: dict[str, Any], *, enabled: bool, shadow_budget_value: int, disabled_reasons: list[str]) -> dict[str, Any]:
    notes = deepcopy((base_policy.get('notes') or {}))
    notes['exploratory_trial'] = {
        'enabled': False,
        'max_candidates': 0,
        'require_base_proposal_threshold': False,
        'min_shadow_judged_count': IMPOSSIBLE_INT,
        'min_shadow_helpful_count': IMPOSSIBLE_INT,
        'min_non_intervention_support_cases': IMPOSSIBLE_INT,
        'min_shadow_trial_score': IMPOSSIBLE_FLOAT,
        'autopolicy_disabled': True,
    }
    notes['generated_autopolicy'] = {
        'mode': 'shadow_only',
        'policy_source': POLICY_SOURCE,
        'canonical_family': row.get('canonical_family'),
        'lineage_parent_family_key': row.get('lineage_parent_family_key'),
        'bridge_status': row.get('bridge_status'),
        'bridge_confidence_max': row.get('bridge_confidence_max'),
        'manual_policy_family': row.get('manual_policy_family'),
        'manual_policy_enabled': row.get('manual_policy_enabled'),
        'shadow_enabled': enabled,
        'max_shadow_candidates': shadow_budget_value,
        'disabled_reasons': disabled_reasons,
    }
    return notes



def build_generated_policy_row(row: dict[str, Any], *, base_policies: dict[str, dict[str, Any]] | None = None, generated_at: str = '') -> dict[str, Any]:
    manual_rows = base_policies or load_family_policies()
    canonical_family = str(row.get('canonical_family') or 'unassigned') or 'unassigned'
    base_policy = family_policy_for(canonical_family, loaded=manual_rows)
    enabled, disabled_reasons = shadow_enablement(row, base_policy=base_policy)
    shadow_budget_value = shadow_budget(row, base_policy=base_policy, enabled=enabled)
    if enabled and shadow_budget_value <= 0:
        enabled = False
        disabled_reasons = [*disabled_reasons, 'zero_shadow_budget_after_clamp']
    health_score = compute_health_score(row)
    notes = make_shadow_only_notes(base_policy, row, enabled=enabled, shadow_budget_value=shadow_budget_value, disabled_reasons=disabled_reasons)
    policy = normalize_family_policy(
        {
            **base_policy,
            'mechanism_family': str(row.get('family_key') or ''),
            'description': f"Generated provisional shadow-only policy for {row.get('family_label') or row.get('family_key')}",
            'enabled': enabled,
            'max_shadow_candidates': shadow_budget_value,
            'max_trial_candidates': 0,
            'min_shadow_judged_count_for_trial': IMPOSSIBLE_INT,
            'min_shadow_helpful_count_for_trial': IMPOSSIBLE_INT,
            'min_shadow_mean_score_for_trial': IMPOSSIBLE_FLOAT,
            'min_non_intervention_support_cases_for_trial': IMPOSSIBLE_INT,
            'max_promotion_ready_candidates': 0,
            'min_trial_judged_count_for_promotion': IMPOSSIBLE_INT,
            'min_trial_helpful_count_for_promotion': IMPOSSIBLE_INT,
            'min_trial_shrunken_utility_for_promotion': IMPOSSIBLE_FLOAT,
            'max_trial_harmful_rate_for_promotion': 0.0,
            'max_contest_case_count_for_promotion': 0,
            'notes': notes,
            'policy_source': POLICY_SOURCE,
            'policy_generated_at': generated_at or '',
            'family_state': str(row.get('family_state') or 'provisional'),
            'health_score': health_score,
            'evidence_mass': float(row.get('source_occurrence_count') or 0),
            'quarantine_until': '',
            'decay_half_life_days': 45 if canonical_family != 'unassigned' else 30,
            'policy_notes': {
                'canonical_family': canonical_family,
                'lineage_parent_family_key': row.get('lineage_parent_family_key'),
                'source_family_slug': row.get('source_family_slug'),
                'bridge_status': row.get('bridge_status'),
                'bridge_confidence_max': row.get('bridge_confidence_max'),
                'bridge_reasons': row.get('bridge_reasons') or [],
                'manual_policy_family': row.get('manual_policy_family'),
                'manual_policy_enabled': row.get('manual_policy_enabled'),
                'candidate_count': row.get('candidate_count'),
                'source_occurrence_count': row.get('source_occurrence_count'),
                'distinct_case_count': row.get('distinct_case_count'),
                'distinct_persona_count': row.get('distinct_persona_count'),
                'shadow_only': True,
                'disabled_reasons': disabled_reasons,
            },
        }
    )
    policy['policy_notes']['generated_shadow_budget'] = shadow_budget_value
    return policy



def build_generated_provisional_family_policies(
    registry_payload: dict[str, Any],
    *,
    base_policies: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    manual_rows = base_policies or load_family_policies()
    families = sort_families_by_support([row for row in (registry_payload.get('families') or []) if isinstance(row, dict)])
    generated_rows: list[dict[str, Any]] = []
    skipped_canonical_seed_rows: list[dict[str, Any]] = []
    for row in families:
        family_key = str(row.get('family_key') or '')
        if not family_key:
            continue
        if family_key == str(row.get('canonical_family') or ''):
            skipped_canonical_seed_rows.append(
                {
                    'family_key': family_key,
                    'canonical_family': row.get('canonical_family'),
                    'reason': 'canonical_seed_uses_manual_prior',
                    'candidate_count': row.get('candidate_count'),
                    'source_occurrence_count': row.get('source_occurrence_count'),
                }
            )
            continue
        generated_rows.append(
            build_generated_policy_row(row, base_policies=manual_rows, generated_at=str(registry_payload.get('generated_at') or ''))
        )
    enabled_count = sum(1 for row in generated_rows if row.get('enabled'))
    disabled_count = len(generated_rows) - enabled_count
    canonical_parent_counts: dict[str, int] = {}
    for row in generated_rows:
        family = str((row.get('policy_notes') or {}).get('canonical_family') or 'unassigned')
        canonical_parent_counts[family] = canonical_parent_counts.get(family, 0) + 1
    return {
        'type': 'generated_provisional_family_policies',
        'generated_at': str(registry_payload.get('generated_at') or ''),
        'policy_source': POLICY_SOURCE,
        'registry_path': str(PROVISIONAL_FAMILY_REGISTRY_JSON_PATH),
        'policy_count': len(generated_rows),
        'enabled_policy_count': enabled_count,
        'disabled_policy_count': disabled_count,
        'skipped_canonical_seed_count': len(skipped_canonical_seed_rows),
        'canonical_parent_counts': canonical_parent_counts,
        'policies': generated_rows,
        'skipped_canonical_seeds': skipped_canonical_seed_rows,
    }



def load_provisional_family_registry_payload() -> dict[str, Any]:
    payload = read_json(PROVISIONAL_FAMILY_REGISTRY_JSON_PATH, default={}) or {}
    if not isinstance(payload, dict):
        return {}
    return payload



def render_family_autopolicy_markdown(payload: dict[str, Any]) -> str:
    lines = [
        '---',
        'type: family_autopolicy_report',
        f"generated_at: {payload.get('generated_at')}",
        f"policy_source: {payload.get('policy_source')}",
        '---',
        '',
        '# Generated provisional family autopolicy',
        '',
        '## Summary',
        f"- policy_count: `{payload.get('policy_count')}`",
        f"- enabled_policy_count: `{payload.get('enabled_policy_count')}`",
        f"- disabled_policy_count: `{payload.get('disabled_policy_count')}`",
        f"- skipped_canonical_seed_count: `{payload.get('skipped_canonical_seed_count')}`",
        '',
        '## Canonical parent counts',
    ]
    counts = payload.get('canonical_parent_counts') or {}
    if not counts:
        lines.append('- none')
    else:
        for family, count in sorted(counts.items(), key=lambda item: (-int(item[1]), item[0])):
            lines.append(f"- `{family}`: `{count}`")
    lines.extend(['', '## Top generated policies'])
    policies = sort_families_by_support(payload.get('policies') or [])
    if not policies:
        lines.append('- none')
    else:
        for row in policies[:20]:
            policy_notes = row.get('policy_notes') or {}
            lines.append(
                f"- `{row.get('mechanism_family')}` -> canonical `{policy_notes.get('canonical_family')}` "
                f"(enabled: `{row.get('enabled')}`, shadow_budget: `{row.get('max_shadow_candidates')}`, "
                f"health_score: `{row.get('health_score')}`, evidence_mass: `{row.get('evidence_mass')}`)"
            )
            disabled_reasons = policy_notes.get('disabled_reasons') or []
            if disabled_reasons:
                lines.append(f"  - disabled_reasons: {', '.join(disabled_reasons)}")
    lines.append('')
    return '\n'.join(lines)



def write_generated_provisional_family_policy_artifacts(payload: dict[str, Any]) -> None:
    write_json(ensure_parent(PROVISIONAL_FAMILY_POLICIES_PATH), payload)
    write_json(ensure_parent(FAMILY_AUTOPOLICY_REPORT_JSON_PATH), payload)
    ensure_parent(FAMILY_AUTOPOLICY_REPORT_MD_PATH).write_text(
        render_family_autopolicy_markdown(payload),
        encoding='utf-8',
    )
