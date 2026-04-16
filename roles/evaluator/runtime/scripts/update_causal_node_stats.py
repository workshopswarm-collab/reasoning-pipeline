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

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402

DEFAULT_EXPERIMENT_ID = 'researcher-lmd-v1'
DEFAULT_SHRINKAGE_K = 5.0

NODES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT node_key, status, lifecycle_stage, mechanism_family, source_kind, promotion_score, decay_score
  FROM public.causal_nodes
  ORDER BY node_key
) t;
'''

PROJECTIONS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    p.case_key,
    p.active_nodes,
    p.contested_edges,
    r.latest_brier_component,
    r.resolution_status
  FROM public.case_causal_projections p
  LEFT JOIN public.learning_case_reviews r
    ON r.case_key = p.case_key
) t;
'''

NODE_EXPOSURES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    replace(candidate_id, 'node:', '') AS node_key,
    e.case_key,
    e.experiment_id,
    r.latest_brier_component
  FROM public.lmd_bundle_exposures e
  JOIN public.learning_case_reviews r
    ON r.case_key = e.case_key
  WHERE e.candidate_type = 'node'
    AND r.resolution_status = 'resolved'
    AND r.latest_brier_component IS NOT NULL
    AND (NULLIF(:'experiment_id', '') IS NULL OR e.experiment_id = NULLIF(:'experiment_id', ''))
) t;
'''

CONTROL_POOL_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    a.case_key,
    a.experiment_id,
    p.active_nodes,
    r.latest_brier_component
  FROM public.lmd_experiment_assignments a
  JOIN public.learning_case_reviews r
    ON r.case_key = a.case_key
  LEFT JOIN public.case_causal_projections p
    ON p.case_key = a.case_key
  WHERE a.arm = 'control'
    AND r.resolution_status = 'resolved'
    AND r.latest_brier_component IS NOT NULL
    AND (NULLIF(:'experiment_id', '') IS NULL OR a.experiment_id = NULLIF(:'experiment_id', ''))
) t;
'''

UPSERT_SQL = r'''
INSERT INTO public.causal_node_stats (
  node_key,
  mechanism_family,
  lifecycle_stage,
  projected_case_count,
  matched_case_count,
  exposure_count,
  injection_count,
  helpful_case_count,
  supporting_case_count,
  contested_case_count,
  raw_uplift,
  shrunken_uplift,
  learned_weight,
  decay_score,
  status,
  status_reason,
  stats_metadata,
  updated_at
)
VALUES (
  :'node_key',
  COALESCE(NULLIF(:'mechanism_family', ''), 'unassigned'),
  COALESCE(NULLIF(:'lifecycle_stage', ''), 'draft'),
  :'projected_case_count'::int,
  :'matched_case_count'::int,
  :'exposure_count'::int,
  :'injection_count'::int,
  :'helpful_case_count'::int,
  :'supporting_case_count'::int,
  :'contested_case_count'::int,
  NULLIF(:'raw_uplift', '')::numeric,
  NULLIF(:'shrunken_uplift', '')::numeric,
  :'learned_weight'::numeric,
  :'decay_score'::numeric,
  :'status',
  NULLIF(:'status_reason', ''),
  COALESCE(NULLIF(:'stats_metadata_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (node_key) DO UPDATE SET
  mechanism_family = EXCLUDED.mechanism_family,
  lifecycle_stage = EXCLUDED.lifecycle_stage,
  projected_case_count = EXCLUDED.projected_case_count,
  matched_case_count = EXCLUDED.matched_case_count,
  exposure_count = EXCLUDED.exposure_count,
  injection_count = EXCLUDED.injection_count,
  helpful_case_count = EXCLUDED.helpful_case_count,
  supporting_case_count = EXCLUDED.supporting_case_count,
  contested_case_count = EXCLUDED.contested_case_count,
  raw_uplift = EXCLUDED.raw_uplift,
  shrunken_uplift = EXCLUDED.shrunken_uplift,
  learned_weight = EXCLUDED.learned_weight,
  decay_score = EXCLUDED.decay_score,
  status = EXCLUDED.status,
  status_reason = EXCLUDED.status_reason,
  stats_metadata = EXCLUDED.stats_metadata,
  updated_at = NOW()
RETURNING json_build_object(
  'node_key', node_key,
  'status', status,
  'learned_weight', learned_weight,
  'exposure_count', exposure_count
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Compute batch causal node stats from projections and node-level LMD exposures')
    parser.add_argument('--experiment-id', default=DEFAULT_EXPERIMENT_ID)
    parser.add_argument('--shrinkage-k', type=float, default=DEFAULT_SHRINKAGE_K)
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def mean(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)



def list_contains(values: list[str] | None, needle: str) -> bool:
    return needle in {str(item).strip() for item in (values or []) if str(item).strip()}



def edge_contains_node(edge_key: str, node_key: str) -> bool:
    parts = str(edge_key or '').split('__')
    if len(parts) >= 3:
        return node_key in {parts[0], parts[2]}
    return node_key in {str(edge_key or '').strip()}



def contested_node(values: list[str] | None, node_key: str) -> bool:
    return any(edge_contains_node(str(item or ''), node_key) for item in (values or []))



def genericity_penalty(source_kind: str, projected_case_count: int, supporting_case_count: int, contested_case_count: int, decay_score: float) -> float:
    penalty = 0.06 if source_kind == 'promoted_candidate' else 0.03
    if projected_case_count > supporting_case_count * 2:
        penalty += min(0.08, (projected_case_count - supporting_case_count * 2) * 0.01)
    if contested_case_count > supporting_case_count:
        penalty += 0.04
    if decay_score > 0.5:
        penalty += min(0.12, (decay_score - 0.5) * 0.2)
    return round(penalty, 4)



def learned_weight(shrunken_uplift: float | None, genericity: float, supporting_case_count: int, contested_case_count: int, helpful_case_count: int, promotion_score: float) -> float:
    evidence_bonus = supporting_case_count * 0.05 + helpful_case_count * 0.03 - contested_case_count * 0.06
    uplift_bonus = (shrunken_uplift or 0.0) * 35.0
    prior_bonus = max(-0.15, min(0.15, promotion_score * 0.15))
    weight = prior_bonus + evidence_bonus + uplift_bonus - genericity
    return round(max(-1.0, min(1.0, weight)), 6)



def status_for_node(weight: float, exposure_count: int, supporting_case_count: int, contested_case_count: int, lifecycle_stage: str) -> tuple[str, str]:
    if exposure_count == 0 and supporting_case_count == 0:
        return 'draft', 'no_support_or_exposures_yet'
    if exposure_count >= 3 and weight < -0.05:
        return 'retired', 'negative_learned_weight_after_exposure'
    if weight < 0 or contested_case_count > supporting_case_count:
        return 'hold', 'negative_or_contested_weight'
    if lifecycle_stage == 'trial' and exposure_count >= 1 and weight >= 0:
        return 'active', 'trial_node_with_nonnegative_weight'
    if supporting_case_count >= 1:
        return 'active', 'matched_node_with_support'
    return 'draft', 'insufficient_support'



def main() -> int:
    args = parse_args()
    resolved_db_url = resolve_db_url(args.db_url)
    table_present = table_exists('causal_node_stats', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False

    nodes = exec_sql(args.psql, resolved_db_url, NODES_SQL, {}) if resolved_db_url else []
    projections = exec_sql(args.psql, resolved_db_url, PROJECTIONS_SQL, {}) if resolved_db_url else []
    exposures = exec_sql(args.psql, resolved_db_url, NODE_EXPOSURES_SQL, {'experiment_id': args.experiment_id}) if resolved_db_url else []
    control_pool = exec_sql(args.psql, resolved_db_url, CONTROL_POOL_SQL, {'experiment_id': args.experiment_id}) if resolved_db_url else []
    if not isinstance(nodes, list):
        nodes = []
    if not isinstance(projections, list):
        projections = []
    if not isinstance(exposures, list):
        exposures = []
    if not isinstance(control_pool, list):
        control_pool = []

    results: list[dict[str, Any]] = []
    persisted_count = 0
    for node in nodes:
        node_key = str(node.get('node_key') or '')
        if not node_key:
            continue
        projected_rows = [row for row in projections if list_contains(row.get('active_nodes'), node_key)]
        projected_case_keys = {str(row.get('case_key') or '') for row in projected_rows if row.get('case_key')}
        contest_case_keys = {
            str(row.get('case_key') or '')
            for row in projections
            if row.get('case_key') and contested_node(row.get('contested_edges'), node_key)
        }
        treatment_cases = {
            str(row.get('case_key') or ''): float(row.get('latest_brier_component'))
            for row in exposures
            if row.get('node_key') == node_key and row.get('latest_brier_component') is not None
        }
        control_cases = {
            str(row.get('case_key') or ''): float(row.get('latest_brier_component'))
            for row in control_pool
            if list_contains(row.get('active_nodes'), node_key) and row.get('latest_brier_component') is not None
        }
        treatment_mean = mean(list(treatment_cases.values()))
        control_mean = mean(list(control_cases.values()))
        raw = (control_mean - treatment_mean) if treatment_mean is not None and control_mean is not None else None
        shrink = ((len(treatment_cases) / (len(treatment_cases) + args.shrinkage_k)) * raw) if raw is not None else None
        helpful_case_keys = sorted([
            case_key for case_key, score in treatment_cases.items()
            if control_mean is not None and score <= control_mean
        ])
        harmful_case_keys = sorted([
            case_key for case_key, score in treatment_cases.items()
            if control_mean is not None and score > control_mean
        ])
        genericity = genericity_penalty(
            str(node.get('source_kind') or ''),
            len(projected_case_keys),
            len(projected_case_keys),
            len([key for key in contest_case_keys if key]),
            float(node.get('decay_score') or 0.0),
        )
        weight = learned_weight(
            shrink,
            genericity,
            len(projected_case_keys),
            len([key for key in contest_case_keys if key]),
            len(helpful_case_keys),
            float(node.get('promotion_score') or 0.0),
        )
        status, reason = status_for_node(
            weight,
            len(treatment_cases),
            len(projected_case_keys),
            len([key for key in contest_case_keys if key]),
            str(node.get('lifecycle_stage') or ''),
        )
        stats_metadata = {
            'experiment_id': args.experiment_id,
            'shrinkage_k': args.shrinkage_k,
            'projected_case_keys': sorted(projected_case_keys),
            'contested_case_keys': sorted([key for key in contest_case_keys if key]),
            'treatment_case_keys': sorted(treatment_cases.keys()),
            'control_case_keys': sorted(control_cases.keys()),
            'helpful_case_keys': helpful_case_keys,
            'harmful_case_keys': harmful_case_keys,
            'helpful_case_count': len(helpful_case_keys),
            'harmful_case_count': len(harmful_case_keys),
            'treatment_mean_brier': treatment_mean,
            'control_mean_brier': control_mean,
            'genericity_penalty': genericity,
        }
        row = {
            'node_key': node_key,
            'mechanism_family': str(node.get('mechanism_family') or 'unassigned'),
            'lifecycle_stage': str(node.get('lifecycle_stage') or 'draft'),
            'projected_case_count': len(projected_case_keys),
            'matched_case_count': len(projected_case_keys),
            'exposure_count': len(treatment_cases),
            'injection_count': len(treatment_cases),
            'helpful_case_count': len(helpful_case_keys),
            'supporting_case_count': len(projected_case_keys),
            'contested_case_count': len([key for key in contest_case_keys if key]),
            'raw_uplift': raw,
            'shrunken_uplift': shrink,
            'learned_weight': weight,
            'decay_score': float(node.get('decay_score') or 0.0),
            'status': status,
            'status_reason': reason,
            'stats_metadata': stats_metadata,
        }
        db_result = None
        if resolved_db_url and table_present and not args.dry_run:
            db_result = exec_sql(
                args.psql,
                resolved_db_url,
                UPSERT_SQL,
                {
                    'node_key': row['node_key'],
                    'mechanism_family': row['mechanism_family'],
                    'lifecycle_stage': row['lifecycle_stage'],
                    'projected_case_count': str(row['projected_case_count']),
                    'matched_case_count': str(row['matched_case_count']),
                    'exposure_count': str(row['exposure_count']),
                    'injection_count': str(row['injection_count']),
                    'helpful_case_count': str(row['helpful_case_count']),
                    'supporting_case_count': str(row['supporting_case_count']),
                    'contested_case_count': str(row['contested_case_count']),
                    'raw_uplift': '' if row['raw_uplift'] is None else str(round(float(row['raw_uplift']), 6)),
                    'shrunken_uplift': '' if row['shrunken_uplift'] is None else str(round(float(row['shrunken_uplift']), 6)),
                    'learned_weight': str(row['learned_weight']),
                    'decay_score': str(row['decay_score']),
                    'status': row['status'],
                    'status_reason': row['status_reason'],
                    'stats_metadata_json': json.dumps(row['stats_metadata']),
                },
            )
            persisted_count += 1
        results.append({'row': row, 'db_result': db_result})

    output: dict[str, Any] = {
        'ok': True,
        'experiment_id': args.experiment_id,
        'table_present': table_present,
        'node_count': len(nodes),
        'persisted_count': persisted_count,
        'dry_run': args.dry_run,
        'rows': results,
    }
    if not resolved_db_url:
        output['warning'] = 'db_url_unavailable'
    elif not table_present:
        output['warning'] = 'causal_node_stats table not present; apply roles/evaluator/sql/029_causal_node_stats.sql'

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
