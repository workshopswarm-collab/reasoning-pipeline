#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.io import read_json, write_json  # noqa: E402
from lib.phase11_retrieval_policy import DEFAULT_POLICY, POLICY_PATH, POLICY_VERSION  # noqa: E402

CANDIDATE_STATS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT candidate_id, candidate_type, learned_weight, shrunken_uplift, genericity_penalty, status, status_reason, stats_metadata
  FROM public.lmd_candidate_stats
) t;
'''

NODE_STATS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT node_key, mechanism_family, lifecycle_stage, learned_weight, shrunken_uplift, supporting_case_count, contested_case_count, helpful_case_count, decay_score, status, status_reason, stats_metadata
  FROM public.causal_node_stats
) t;
'''

EDGE_STATS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    s.edge_key,
    e.mechanism_family,
    e.lifecycle_stage,
    s.learned_weight,
    s.shrunken_uplift,
    s.supporting_case_count,
    s.contested_case_count,
    COALESCE(NULLIF(s.stats_metadata->>'helpful_case_count', '')::numeric, 0) AS helpful_case_count,
    COALESCE(e.decay_score, 0) AS decay_score,
    s.genericity_penalty,
    s.status,
    s.status_reason,
    s.stats_metadata
  FROM public.causal_edge_stats s
  LEFT JOIN public.causal_edges e
    ON e.edge_key = s.edge_key
) t;
'''

SUMMARY_PATH = Path(__file__).resolve().parents[4] / 'qualitative-db' / '60-causal-map' / 'generated' / 'proposed-causal-candidates-summary.json'

STATUS_TARGET = {
    'active': 1.0,
    'trial': 0.65,
    'draft': 0.15,
    'hold': -0.55,
    'retired': -1.0,
    'archived': -1.0,
}
PROMOTION_TARGET = {
    'promotion_ready': 1.0,
    'trial_candidate': 0.75,
    'shadow_candidate': 0.35,
    'aggregated': 0.1,
}
SHRINKAGE_K = 8.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Learn Phase 11 retrieval-policy weights from current outcome-derived stats surfaces')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--summary-path', default=str(SUMMARY_PATH))
    parser.add_argument('--output-path', default=str(POLICY_PATH))
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return float(default)



def status_target(status: Any) -> float:
    return STATUS_TARGET.get(str(status or '').strip().lower(), 0.0)



def lifecycle_stage(row: dict[str, Any]) -> str:
    stage = str(row.get('lifecycle_stage') or '').strip().lower()
    if stage:
        return stage
    return str(row.get('status') or '').strip().lower() or 'draft'



def pearson(xs: list[float], ys: list[float]) -> float:
    if len(xs) != len(ys) or len(xs) < 2:
        return 0.0
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    den_x = math.sqrt(sum((x - mean_x) ** 2 for x in xs))
    den_y = math.sqrt(sum((y - mean_y) ** 2 for y in ys))
    if den_x <= 1e-9 or den_y <= 1e-9:
        return 0.0
    return max(-1.0, min(1.0, num / (den_x * den_y)))



def aligned_signal(rows: list[dict[str, Any]], feature_fn, target_fn, *, expected: str) -> dict[str, Any]:
    xs: list[float] = []
    ys: list[float] = []
    for row in rows:
        try:
            x = float(feature_fn(row))
            y = float(target_fn(row))
        except Exception:
            continue
        xs.append(x)
        ys.append(y)
    corr = pearson(xs, ys)
    n = len(xs)
    shrink = n / (n + SHRINKAGE_K) if n > 0 else 0.0
    aligned = max(0.0, corr if expected == 'positive' else -corr)
    return {
        'count': n,
        'correlation': round(corr, 6),
        'aligned_signal': round(aligned, 6),
        'shrinkage': round(shrink, 6),
        'effective_signal': round(aligned * shrink, 6),
    }



def weight_from_signal(default: float, signal: dict[str, Any], *, floor_mult: float = 0.75, ceil_mult: float = 1.45) -> float:
    effective = safe_float(signal.get('effective_signal'))
    multiplier = floor_mult + (ceil_mult - floor_mult) * effective
    return round(default * multiplier, 3)



def stage_bonus_from_rows(default: float, rows: list[dict[str, Any]], stage_name: str) -> tuple[float, dict[str, Any]]:
    targets = [status_target(row.get('status')) for row in rows]
    stage_rows = [row for row in rows if lifecycle_stage(row) == stage_name]
    stage_targets = [status_target(row.get('status')) for row in stage_rows]
    if not targets or not stage_targets:
        return round(default, 3), {'stage': stage_name, 'count': len(stage_targets), 'mean_target': 0.0, 'overall_mean': 0.0}
    overall_mean = sum(targets) / len(targets)
    stage_mean = sum(stage_targets) / len(stage_targets)
    shrink = len(stage_targets) / (len(stage_targets) + SHRINKAGE_K)
    adjusted = default + (stage_mean - overall_mean) * 0.35 * shrink
    return round(adjusted, 3), {
        'stage': stage_name,
        'count': len(stage_targets),
        'mean_target': round(stage_mean, 6),
        'overall_mean': round(overall_mean, 6),
        'shrinkage': round(shrink, 6),
    }



def load_rows(sql: str, *, db_url: str, psql_bin: str, table_name: str) -> tuple[list[dict[str, Any]], bool]:
    if not db_url:
        return [], False
    present = table_exists(table_name, db_url=db_url, psql_bin=psql_bin)
    if not present:
        return [], False
    rows = exec_sql(psql_bin, db_url, sql, {})
    return (rows if isinstance(rows, list) else []), True



def learn_candidate_bonus_weights(candidate_rows: list[dict[str, Any]], policy: dict[str, Any]) -> dict[str, Any]:
    defaults = policy['weights']['candidate_bonus']
    signals = {
        'learned_weight_bonus': aligned_signal(candidate_rows, lambda row: safe_float(row.get('learned_weight')), lambda row: status_target(row.get('status')), expected='positive'),
        'shrunken_uplift_bonus': aligned_signal(candidate_rows, lambda row: safe_float(row.get('shrunken_uplift')), lambda row: status_target(row.get('status')), expected='positive'),
        'genericity_penalty': aligned_signal(candidate_rows, lambda row: safe_float(row.get('genericity_penalty')), lambda row: status_target(row.get('status')), expected='negative'),
    }
    learned = {
        'learned_weight_bonus': weight_from_signal(defaults['learned_weight_bonus'], signals['learned_weight_bonus']),
        'shrunken_uplift_bonus': weight_from_signal(defaults['shrunken_uplift_bonus'], signals['shrunken_uplift_bonus']),
        'genericity_penalty': weight_from_signal(defaults['genericity_penalty'], signals['genericity_penalty']),
        'status_penalty': defaults['status_penalty'],
    }
    return {'weights': learned, 'signals': signals}



def learn_live_graph_weights(rows: list[dict[str, Any]], entity_type: str, policy: dict[str, Any]) -> dict[str, Any]:
    defaults = policy['weights']['live_graph'][entity_type]
    signals = {
        'learned_weight_bonus': aligned_signal(rows, lambda row: max(0.0, safe_float(row.get('learned_weight'))), lambda row: status_target(row.get('status')), expected='positive'),
        'negative_weight_penalty': aligned_signal(rows, lambda row: max(0.0, -safe_float(row.get('learned_weight'))), lambda row: status_target(row.get('status')), expected='negative'),
        'uplift_bonus': aligned_signal(rows, lambda row: max(0.0, safe_float(row.get('shrunken_uplift'))), lambda row: status_target(row.get('status')), expected='positive'),
        'negative_uplift_penalty': aligned_signal(rows, lambda row: max(0.0, -safe_float(row.get('shrunken_uplift'))), lambda row: status_target(row.get('status')), expected='negative'),
        'support_bonus': aligned_signal(rows, lambda row: safe_float(row.get('supporting_case_count')), lambda row: status_target(row.get('status')), expected='positive'),
        'helpful_bonus': aligned_signal(rows, lambda row: safe_float(row.get('helpful_case_count')), lambda row: status_target(row.get('status')), expected='positive'),
        'contestation_penalty': aligned_signal(rows, lambda row: safe_float(row.get('contested_case_count')), lambda row: status_target(row.get('status')), expected='negative'),
        'decay_penalty': aligned_signal(rows, lambda row: safe_float(row.get('decay_score')), lambda row: status_target(row.get('status')), expected='negative'),
    }
    active_bonus, active_meta = stage_bonus_from_rows(defaults['trust_tier_bonus']['active_reviewed'], rows, 'active')
    trial_bonus, trial_meta = stage_bonus_from_rows(defaults['trust_tier_bonus']['trial_experimental'], rows, 'trial')
    review_bonus, review_meta = stage_bonus_from_rows(defaults['trust_tier_bonus']['review_only'], rows, 'draft')
    learned = {
        'learned_weight_bonus': weight_from_signal(defaults['learned_weight_bonus'], signals['learned_weight_bonus']),
        'negative_weight_penalty': weight_from_signal(defaults['negative_weight_penalty'], signals['negative_weight_penalty']),
        'uplift_bonus': weight_from_signal(defaults['uplift_bonus'], signals['uplift_bonus']),
        'negative_uplift_penalty': weight_from_signal(defaults['negative_uplift_penalty'], signals['negative_uplift_penalty']),
        'support_bonus': weight_from_signal(defaults['support_bonus'], signals['support_bonus']),
        'helpful_bonus': weight_from_signal(defaults['helpful_bonus'], signals['helpful_bonus']),
        'contestation_penalty': weight_from_signal(defaults['contestation_penalty'], signals['contestation_penalty']),
        'decay_penalty': weight_from_signal(defaults['decay_penalty'], signals['decay_penalty']),
        'family_crowding_penalty': defaults['family_crowding_penalty'],
        'trust_tier_bonus': {
            'active_reviewed': active_bonus,
            'trial_experimental': trial_bonus,
            'review_only': review_bonus,
        },
        'status_penalty': defaults['status_penalty'],
    }
    return {
        'weights': learned,
        'signals': signals,
        'trust_tier_learning': {
            'active_reviewed': active_meta,
            'trial_experimental': trial_meta,
            'review_only': review_meta,
        },
    }



def learn_overlay_weights(proposals: list[dict[str, Any]], policy: dict[str, Any]) -> dict[str, Any]:
    defaults = policy['weights']['overlay']

    def overlay_target(row: dict[str, Any]) -> float:
        base = 0.0
        base += 1.2 * safe_float(row.get('trial_shrunken_utility'))
        base += 0.9 * safe_float(row.get('shadow_trial_score'))
        base += 0.12 * safe_float(row.get('trial_helpful_count'))
        base += 0.08 * safe_float(row.get('shadow_helpful_count'))
        base += 0.08 * safe_float(row.get('non_intervention_support_case_count'))
        base += PROMOTION_TARGET.get(str(row.get('promotion_status') or '').strip().lower(), 0.0)
        base -= 0.55 * safe_float(row.get('trial_harmful_rate'))
        base -= 0.18 * safe_float(row.get('shadow_harmful_count'))
        base -= 0.15 * safe_float(row.get('genericity_penalty'))
        return base

    signals = {
        'shadow_trial_score': aligned_signal(proposals, lambda row: safe_float(row.get('shadow_trial_score')), overlay_target, expected='positive'),
        'trial_shrunken_utility': aligned_signal(proposals, lambda row: safe_float(row.get('trial_shrunken_utility')), overlay_target, expected='positive'),
        'trial_helpful': aligned_signal(proposals, lambda row: safe_float(row.get('trial_helpful_count')), overlay_target, expected='positive'),
        'shadow_helpful': aligned_signal(proposals, lambda row: safe_float(row.get('shadow_helpful_count')), overlay_target, expected='positive'),
        'non_intervention_support': aligned_signal(proposals, lambda row: safe_float(row.get('non_intervention_support_case_count')), overlay_target, expected='positive'),
        'distinct_cases': aligned_signal(proposals, lambda row: safe_float(row.get('distinct_case_count')), overlay_target, expected='positive'),
        'genericity_penalty': aligned_signal(proposals, lambda row: safe_float(row.get('genericity_penalty')), overlay_target, expected='negative'),
        'harmful_shadow_penalty': aligned_signal(proposals, lambda row: safe_float(row.get('shadow_harmful_count')), overlay_target, expected='negative'),
        'trial_harmful_rate_penalty': aligned_signal(proposals, lambda row: safe_float(row.get('trial_harmful_rate')), overlay_target, expected='negative'),
        'merge_penalty': aligned_signal(proposals, lambda row: 1.0 if bool(row.get('merge_recommended')) else 0.0, overlay_target, expected='negative'),
    }
    learned = {
        'shadow_trial_score': weight_from_signal(defaults['shadow_trial_score'], signals['shadow_trial_score']),
        'trial_shrunken_utility': weight_from_signal(defaults['trial_shrunken_utility'], signals['trial_shrunken_utility']),
        'trial_helpful': weight_from_signal(defaults['trial_helpful'], signals['trial_helpful']),
        'shadow_helpful': weight_from_signal(defaults['shadow_helpful'], signals['shadow_helpful']),
        'non_intervention_support': weight_from_signal(defaults['non_intervention_support'], signals['non_intervention_support']),
        'distinct_cases': weight_from_signal(defaults['distinct_cases'], signals['distinct_cases']),
        'genericity_penalty': weight_from_signal(defaults['genericity_penalty'], signals['genericity_penalty']),
        'harmful_shadow_penalty': weight_from_signal(defaults['harmful_shadow_penalty'], signals['harmful_shadow_penalty']),
        'trial_harmful_rate_penalty': weight_from_signal(defaults['trial_harmful_rate_penalty'], signals['trial_harmful_rate_penalty']),
        'family_crowding_penalty': defaults['family_crowding_penalty'],
        'merge_penalty': weight_from_signal(defaults['merge_penalty'], signals['merge_penalty']),
    }
    return {'weights': learned, 'signals': signals}



def learn_structural_surface_weights(candidate_rows: list[dict[str, Any]], policy: dict[str, Any]) -> dict[str, Any]:
    defaults_intervention = policy['weights']['intervention']
    defaults_aggregate = policy['weights']['aggregate_note']
    intervention_rows = [row for row in candidate_rows if str(row.get('candidate_type') or '').strip() == 'intervention']
    aggregate_rows = [row for row in candidate_rows if str(row.get('candidate_type') or '').strip() == 'aggregate_note']

    intervention_signal = aligned_signal(intervention_rows, lambda row: safe_float(row.get('learned_weight')) + safe_float(row.get('shrunken_uplift')), lambda row: status_target(row.get('status')), expected='positive')
    aggregate_signal = aligned_signal(aggregate_rows, lambda row: safe_float(row.get('learned_weight')) + safe_float(row.get('shrunken_uplift')), lambda row: status_target(row.get('status')), expected='positive')

    def scaled(default: float, signal: dict[str, Any]) -> float:
        return weight_from_signal(default, signal, floor_mult=0.85, ceil_mult=1.25)

    return {
        'intervention': {
            'weights': {
                'required_check_bonus': scaled(defaults_intervention['required_check_bonus'], intervention_signal),
                'mechanic_live_bonus': scaled(defaults_intervention['mechanic_live_bonus'], intervention_signal),
                'source_live_bonus': scaled(defaults_intervention['source_live_bonus'], intervention_signal),
                'workflow_live_bonus': scaled(defaults_intervention['workflow_live_bonus'], intervention_signal),
            },
            'signal': intervention_signal,
        },
        'aggregate_note': {
            'weights': {
                'shared_contested_workflow_edge': scaled(defaults_aggregate['shared_contested_workflow_edge'], aggregate_signal),
                'threshold_workflow_family': scaled(defaults_aggregate['threshold_workflow_family'], aggregate_signal),
                'workflow_live_bonus': scaled(defaults_aggregate['workflow_live_bonus'], aggregate_signal),
                'shared_source_family': scaled(defaults_aggregate['shared_source_family'], aggregate_signal),
                'source_live_bonus': scaled(defaults_aggregate['source_live_bonus'], aggregate_signal),
            },
            'signal': aggregate_signal,
        },
    }



def build_policy(candidate_rows: list[dict[str, Any]], node_rows: list[dict[str, Any]], edge_rows: list[dict[str, Any]], proposals: list[dict[str, Any]]) -> dict[str, Any]:
    policy = copy.deepcopy(DEFAULT_POLICY)
    policy['policy_version'] = POLICY_VERSION
    candidate_bundle = learn_candidate_bonus_weights(candidate_rows, policy)
    node_bundle = learn_live_graph_weights(node_rows, 'node', policy)
    edge_bundle = learn_live_graph_weights(edge_rows, 'edge', policy)
    overlay_bundle = learn_overlay_weights(proposals, policy)
    structural_bundle = learn_structural_surface_weights(candidate_rows, policy)

    policy['weights']['candidate_bonus'] = candidate_bundle['weights']
    policy['weights']['live_graph']['node'] = node_bundle['weights']
    policy['weights']['live_graph']['edge'] = edge_bundle['weights']
    policy['weights']['overlay'] = overlay_bundle['weights']
    policy['weights']['intervention'] = structural_bundle['intervention']['weights']
    policy['weights']['aggregate_note'] = structural_bundle['aggregate_note']['weights']
    policy['learning_metadata'] = {
        'sample_counts': {
            'candidate_rows': len(candidate_rows),
            'node_rows': len(node_rows),
            'edge_rows': len(edge_rows),
            'proposal_rows': len(proposals),
        },
        'signals': {
            'candidate_bonus': candidate_bundle['signals'],
            'live_graph': {
                'node': node_bundle['signals'],
                'edge': edge_bundle['signals'],
                'trust_tier_learning': {
                    'node': node_bundle['trust_tier_learning'],
                    'edge': edge_bundle['trust_tier_learning'],
                },
            },
            'overlay': overlay_bundle['signals'],
            'structural_surfaces': {
                'intervention': structural_bundle['intervention']['signal'],
                'aggregate_note': structural_bundle['aggregate_note']['signal'],
            },
        },
    }
    policy['loaded_from_file'] = False
    return policy



def main() -> int:
    args = parse_args()
    resolved_db_url = resolve_db_url(args.db_url)
    candidate_rows, candidate_present = load_rows(CANDIDATE_STATS_SQL, db_url=resolved_db_url, psql_bin=args.psql, table_name='lmd_candidate_stats')
    node_rows, node_present = load_rows(NODE_STATS_SQL, db_url=resolved_db_url, psql_bin=args.psql, table_name='causal_node_stats')
    edge_rows, edge_present = load_rows(EDGE_STATS_SQL, db_url=resolved_db_url, psql_bin=args.psql, table_name='causal_edge_stats')

    summary_path = Path(args.summary_path)
    summary_payload = read_json(summary_path, default={}) if summary_path.exists() else {}
    proposals = (summary_payload or {}).get('proposals') or []
    if not isinstance(proposals, list):
        proposals = []

    policy = build_policy(candidate_rows, node_rows, edge_rows, proposals)
    policy['source_path'] = str(Path(args.output_path))
    policy['loaded_from_file'] = False
    output = {
        'ok': True,
        'warnings': [
            warning
            for warning, present in [
                ('db_url_unavailable', bool(resolved_db_url)),
                ('lmd_candidate_stats_table_missing', candidate_present),
                ('causal_node_stats_table_missing', node_present),
                ('causal_edge_stats_table_missing', edge_present),
                ('proposal_summary_missing', summary_path.exists()),
            ]
            if not present
        ],
        'policy': policy,
    }

    if not args.dry_run:
        write_json(Path(args.output_path), policy, pretty=True)
        output['written_to'] = str(Path(args.output_path))
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
