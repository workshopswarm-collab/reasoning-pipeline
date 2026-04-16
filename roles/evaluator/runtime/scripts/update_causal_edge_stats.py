#!/usr/bin/env python3
from __future__ import annotations

import argparse
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

DEFAULT_EXPERIMENT_ID = 'researcher-lmd-v1'
DEFAULT_SHRINKAGE_K = 5.0

EDGES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT edge_key, status, confidence_mode, confidence_prior
  FROM public.causal_edges
  ORDER BY edge_key
) t;
'''

EVIDENCE_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT edge_key, case_key, support_direction
  FROM public.causal_edge_evidence
) t;
'''

PROJECTIONS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    p.case_key,
    p.active_nodes,
    p.candidate_edges,
    p.contested_edges,
    r.latest_brier_component,
    r.resolution_status
  FROM public.case_causal_projections p
  LEFT JOIN public.learning_case_reviews r
    ON r.case_key = p.case_key
) t;
'''

EDGE_EXPOSURES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    replace(candidate_id, 'edge:', '') AS edge_key,
    e.case_key,
    e.experiment_id,
    r.latest_brier_component
  FROM public.lmd_bundle_exposures e
  JOIN public.learning_case_reviews r
    ON r.case_key = e.case_key
  WHERE e.candidate_type = 'edge'
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
    p.candidate_edges,
    p.contested_edges,
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
INSERT INTO public.causal_edge_stats (
  edge_key,
  exposure_count,
  projected_case_count,
  supporting_case_count,
  contested_case_count,
  treatment_case_count,
  control_case_count,
  treatment_mean_brier,
  control_mean_brier,
  raw_uplift,
  shrunken_uplift,
  genericity_penalty,
  learned_weight,
  status,
  status_reason,
  stats_metadata,
  updated_at
)
VALUES (
  :'edge_key',
  :'exposure_count'::int,
  :'projected_case_count'::int,
  :'supporting_case_count'::int,
  :'contested_case_count'::int,
  :'treatment_case_count'::int,
  :'control_case_count'::int,
  NULLIF(:'treatment_mean_brier', '')::numeric,
  NULLIF(:'control_mean_brier', '')::numeric,
  NULLIF(:'raw_uplift', '')::numeric,
  NULLIF(:'shrunken_uplift', '')::numeric,
  :'genericity_penalty'::numeric,
  :'learned_weight'::numeric,
  :'status',
  NULLIF(:'status_reason', ''),
  COALESCE(NULLIF(:'stats_metadata_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (edge_key) DO UPDATE SET
  exposure_count = EXCLUDED.exposure_count,
  projected_case_count = EXCLUDED.projected_case_count,
  supporting_case_count = EXCLUDED.supporting_case_count,
  contested_case_count = EXCLUDED.contested_case_count,
  treatment_case_count = EXCLUDED.treatment_case_count,
  control_case_count = EXCLUDED.control_case_count,
  treatment_mean_brier = EXCLUDED.treatment_mean_brier,
  control_mean_brier = EXCLUDED.control_mean_brier,
  raw_uplift = EXCLUDED.raw_uplift,
  shrunken_uplift = EXCLUDED.shrunken_uplift,
  genericity_penalty = EXCLUDED.genericity_penalty,
  learned_weight = EXCLUDED.learned_weight,
  status = EXCLUDED.status,
  status_reason = EXCLUDED.status_reason,
  stats_metadata = EXCLUDED.stats_metadata,
  updated_at = NOW()
RETURNING json_build_object(
  'edge_key', edge_key,
  'status', status,
  'learned_weight', learned_weight,
  'exposure_count', exposure_count
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Compute batch causal edge stats from projections, evidence, and LMD exposures')
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


def genericity_penalty(confidence_mode: str, projected_case_count: int, supporting_case_count: int, contested_case_count: int) -> float:
    penalty = 0.06 if confidence_mode == 'hypothesis' else 0.03
    if projected_case_count > supporting_case_count * 2:
        penalty += min(0.08, (projected_case_count - supporting_case_count * 2) * 0.01)
    if contested_case_count > supporting_case_count:
        penalty += 0.04
    return round(penalty, 4)


def learned_weight(confidence_prior: float | None, shrunken_uplift: float | None, genericity: float, supporting_case_count: int, contested_case_count: int) -> float:
    prior_bonus = (confidence_prior or 0.5) - 0.5
    evidence_bonus = supporting_case_count * 0.05 - contested_case_count * 0.06
    uplift_bonus = (shrunken_uplift or 0.0) * 35.0
    weight = prior_bonus + evidence_bonus + uplift_bonus - genericity
    return round(max(-1.0, min(1.0, weight)), 6)


def status_for_edge(weight: float, exposure_count: int, supporting_case_count: int, contested_case_count: int, confidence_mode: str) -> tuple[str, str]:
    if exposure_count == 0 and supporting_case_count == 0:
        return 'draft', 'no_support_or_exposures_yet'
    if exposure_count >= 3 and weight < -0.05:
        return 'retired', 'negative_learned_weight_after_exposure'
    if weight < 0:
        return 'hold', 'negative_or_contested_weight'
    if supporting_case_count >= 1 and confidence_mode == 'reviewed':
        return 'active', 'reviewed_edge_with_support'
    if supporting_case_count >= 2:
        return 'active', 'multi_case_support'
    return 'draft', 'insufficient_support'


def main() -> int:
    args = parse_args()
    resolved_db_url = resolve_db_url(args.db_url)
    table_present = table_exists('causal_edge_stats', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False

    edges = exec_sql(args.psql, resolved_db_url, EDGES_SQL, {}) if resolved_db_url else []
    evidence_rows = exec_sql(args.psql, resolved_db_url, EVIDENCE_SQL, {}) if resolved_db_url else []
    projections = exec_sql(args.psql, resolved_db_url, PROJECTIONS_SQL, {}) if resolved_db_url else []
    exposures = exec_sql(args.psql, resolved_db_url, EDGE_EXPOSURES_SQL, {'experiment_id': args.experiment_id}) if resolved_db_url else []
    control_pool = exec_sql(args.psql, resolved_db_url, CONTROL_POOL_SQL, {'experiment_id': args.experiment_id}) if resolved_db_url else []
    if not isinstance(edges, list):
        edges = []
    if not isinstance(evidence_rows, list):
        evidence_rows = []
    if not isinstance(projections, list):
        projections = []
    if not isinstance(exposures, list):
        exposures = []
    if not isinstance(control_pool, list):
        control_pool = []

    results: list[dict[str, Any]] = []
    persisted_count = 0
    for edge in edges:
        edge_key = str(edge.get('edge_key') or '')
        support_cases = {str(row.get('case_key') or '') for row in evidence_rows if row.get('edge_key') == edge_key and row.get('support_direction') == 'supports' and row.get('case_key')}
        contest_cases = {str(row.get('case_key') or '') for row in evidence_rows if row.get('edge_key') == edge_key and row.get('support_direction') in {'contests', 'weakens'} and row.get('case_key')}
        projected_rows = [row for row in projections if list_contains(row.get('candidate_edges'), edge_key) or list_contains(row.get('contested_edges'), edge_key)]
        projected_case_keys = {str(row.get('case_key') or '') for row in projected_rows if row.get('case_key')}
        treatment_cases = {str(row.get('case_key') or ''): float(row.get('latest_brier_component')) for row in exposures if row.get('edge_key') == edge_key and row.get('latest_brier_component') is not None}
        control_cases = {
            str(row.get('case_key') or ''): float(row.get('latest_brier_component'))
            for row in control_pool
            if (list_contains(row.get('candidate_edges'), edge_key) or list_contains(row.get('contested_edges'), edge_key)) and row.get('latest_brier_component') is not None
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
        genericity = genericity_penalty(str(edge.get('confidence_mode') or ''), len(projected_case_keys), len(support_cases), len(contest_cases))
        weight = learned_weight(float(edge.get('confidence_prior') or 0.5), shrink, genericity, len(support_cases), len(contest_cases))
        status, reason = status_for_edge(weight, len(treatment_cases), len(support_cases), len(contest_cases), str(edge.get('confidence_mode') or ''))
        stats_metadata = {
            'experiment_id': args.experiment_id,
            'shrinkage_k': args.shrinkage_k,
            'projected_case_keys': sorted(projected_case_keys),
            'support_case_keys': sorted(support_cases),
            'contested_case_keys': sorted(contest_cases),
            'treatment_case_keys': sorted(treatment_cases.keys()),
            'control_case_keys': sorted(control_cases.keys()),
            'helpful_case_keys': helpful_case_keys,
            'harmful_case_keys': harmful_case_keys,
            'helpful_case_count': len(helpful_case_keys),
            'harmful_case_count': len(harmful_case_keys),
            'treatment_mean_brier': treatment_mean,
            'control_mean_brier': control_mean,
        }
        record = {
            'edge_key': edge_key,
            'exposure_count': len([row for row in exposures if row.get('edge_key') == edge_key]),
            'projected_case_count': len(projected_case_keys),
            'supporting_case_count': len(support_cases),
            'contested_case_count': len(contest_cases),
            'treatment_case_count': len(treatment_cases),
            'control_case_count': len(control_cases),
            'treatment_mean_brier': treatment_mean,
            'control_mean_brier': control_mean,
            'raw_uplift': raw,
            'shrunken_uplift': shrink,
            'genericity_penalty': genericity,
            'learned_weight': weight,
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
                    'edge_key': edge_key,
                    'exposure_count': str(record['exposure_count']),
                    'projected_case_count': str(record['projected_case_count']),
                    'supporting_case_count': str(record['supporting_case_count']),
                    'contested_case_count': str(record['contested_case_count']),
                    'treatment_case_count': str(record['treatment_case_count']),
                    'control_case_count': str(record['control_case_count']),
                    'treatment_mean_brier': '' if treatment_mean is None else str(round(treatment_mean, 8)),
                    'control_mean_brier': '' if control_mean is None else str(round(control_mean, 8)),
                    'raw_uplift': '' if raw is None else str(round(raw, 8)),
                    'shrunken_uplift': '' if shrink is None else str(round(shrink, 8)),
                    'genericity_penalty': str(genericity),
                    'learned_weight': str(weight),
                    'status': status,
                    'status_reason': reason,
                    'stats_metadata_json': json.dumps(stats_metadata),
                },
            )
            persisted_count += 1
        results.append({'record': record, 'db_result': db_result})

    output: dict[str, Any] = {
        'ok': True,
        'experiment_id': args.experiment_id,
        'edge_count': len(results),
        'persisted_count': persisted_count,
        'table_present': table_present,
        'results': results,
    }
    if not resolved_db_url:
        output['warning'] = 'db_url_unavailable'
    elif not table_present:
        output['warning'] = 'causal_edge_stats table not present; apply roles/evaluator/sql/027_causal_edge_stats.sql'
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
