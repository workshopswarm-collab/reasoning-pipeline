from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

try:
    from .io import read_json
except ImportError:  # pragma: no cover - planner scripts import via runtime-root sys.path
    from lib.io import read_json

POLICY_VERSION = 'phase11-learned-policy-v1'
POLICY_PATH = Path(__file__).resolve().parents[4] / 'qualitative-db' / '60-causal-map' / 'generated' / 'phase11-retrieval-policy.json'

DEFAULT_POLICY: dict[str, Any] = {
    'policy_version': POLICY_VERSION,
    'loaded_from_file': False,
    'source_path': str(POLICY_PATH),
    'weights': {
        'candidate_bonus': {
            'learned_weight_bonus': 0.95,
            'shrunken_uplift_bonus': 0.70,
            'genericity_penalty': 0.35,
            'status_penalty': 0.18,
        },
        'live_graph': {
            'node': {
                'learned_weight_bonus': 1.25,
                'negative_weight_penalty': 1.35,
                'uplift_bonus': 1.10,
                'negative_uplift_penalty': 1.15,
                'support_bonus': 0.70,
                'helpful_bonus': 0.45,
                'contestation_penalty': 0.80,
                'decay_penalty': 0.70,
                'family_crowding_penalty': 0.90,
                'trust_tier_bonus': {
                    'active_reviewed': 0.45,
                    'trial_experimental': 0.12,
                    'review_only': -0.18,
                },
                'status_penalty': {
                    'hold_or_draft': 0.28,
                    'retired_or_archived': 0.45,
                },
            },
            'edge': {
                'learned_weight_bonus': 1.25,
                'negative_weight_penalty': 1.35,
                'uplift_bonus': 1.10,
                'negative_uplift_penalty': 1.15,
                'support_bonus': 0.70,
                'helpful_bonus': 0.45,
                'contestation_penalty': 0.80,
                'decay_penalty': 0.70,
                'family_crowding_penalty': 0.90,
                'trust_tier_bonus': {
                    'active_reviewed': 0.45,
                    'trial_experimental': 0.12,
                    'review_only': -0.18,
                },
                'status_penalty': {
                    'hold_or_draft': 0.28,
                    'retired_or_archived': 0.45,
                },
            },
        },
        'intervention': {
            'required_check_bonus': 0.45,
            'mechanic_live_bonus': 0.55,
            'source_live_bonus': 0.75,
            'workflow_live_bonus': 0.60,
        },
        'aggregate_note': {
            'shared_contested_workflow_edge': 0.85,
            'threshold_workflow_family': 0.55,
            'workflow_live_bonus': 0.80,
            'shared_source_family': 0.90,
            'source_live_bonus': 0.85,
        },
        'overlay': {
            'shadow_trial_score': 1.05,
            'trial_shrunken_utility': 0.95,
            'trial_helpful': 0.55,
            'shadow_helpful': 0.45,
            'non_intervention_support': 0.55,
            'distinct_cases': 0.32,
            'genericity_penalty': 0.70,
            'harmful_shadow_penalty': 0.55,
            'trial_harmful_rate_penalty': 0.65,
            'family_crowding_penalty': 0.90,
            'merge_penalty': 0.75,
        },
    },
}


def _deep_merge(base: Any, override: Any) -> Any:
    if isinstance(base, dict) and isinstance(override, dict):
        merged = {key: copy.deepcopy(value) for key, value in base.items()}
        for key, value in override.items():
            if key in merged:
                merged[key] = _deep_merge(merged[key], value)
            else:
                merged[key] = copy.deepcopy(value)
        return merged
    return copy.deepcopy(override)



def load_phase11_retrieval_policy(path: Path | None = None) -> dict[str, Any]:
    target = path or POLICY_PATH
    policy = copy.deepcopy(DEFAULT_POLICY)
    policy['source_path'] = str(target)
    data = read_json(target, default={}) if target.exists() else {}
    if isinstance(data, dict) and data:
        policy = _deep_merge(policy, data)
        policy['loaded_from_file'] = True
        policy['source_path'] = str(target)
    return policy



def phase11_weight(policy: dict[str, Any] | None, *path: str, default: float = 0.0) -> float:
    current: Any = (policy or {}).get('weights') or {}
    for part in path:
        if not isinstance(current, dict) or part not in current:
            return float(default)
        current = current[part]
    try:
        return float(current)
    except Exception:
        return float(default)
