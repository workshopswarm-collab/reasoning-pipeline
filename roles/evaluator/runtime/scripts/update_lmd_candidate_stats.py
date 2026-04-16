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
from lib.interventions import build_intervention_record, intervention_note_paths  # noqa: E402

DEFAULT_EXPERIMENT_ID = 'researcher-lmd-v1'
DEFAULT_SHRINKAGE_K = 5.0
TOKEN_COST_PENALTIES = {
    'case_review': 0.0008,
    'intervention': 0.0002,
    'aggregate_note': 0.0005,
    'edge': 0.0001,
}

EXPOSURES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    e.candidate_id,
    e.candidate_type,
    e.case_key,
    e.experiment_id,
    e.arm,
    e.candidate_path,
    e.retrieval_score,
    e.required_check_keys,
    e.notes,
    r.latest_brier_component,
    r.error_pattern,
    r.category,
    r.platform
  FROM public.lmd_bundle_exposures e
  JOIN public.learning_case_reviews r
    ON r.case_key = e.case_key
  WHERE r.resolution_status = 'resolved'
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
    r.latest_brier_component,
    r.error_pattern,
    r.category,
    r.platform,
    p.active_nodes,
    p.candidate_edges,
    p.contested_edges,
    p.projection_metadata
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
INSERT INTO public.lmd_candidate_stats (
  candidate_id,
  candidate_type,
  n_exposed,
  distinct_case_count,
  treatment_case_count,
  control_case_count,
  treatment_mean_brier,
  control_mean_brier,
  raw_uplift,
  shrunken_uplift,
  cost_adjusted_uplift,
  genericity_penalty,
  learned_weight,
  status,
  status_reason,
  stats_metadata,
  updated_at
)
VALUES (
  :'candidate_id',
  :'candidate_type',
  :'n_exposed'::int,
  :'distinct_case_count'::int,
  :'treatment_case_count'::int,
  :'control_case_count'::int,
  NULLIF(:'treatment_mean_brier', '')::numeric,
  NULLIF(:'control_mean_brier', '')::numeric,
  NULLIF(:'raw_uplift', '')::numeric,
  NULLIF(:'shrunken_uplift', '')::numeric,
  NULLIF(:'cost_adjusted_uplift', '')::numeric,
  :'genericity_penalty'::numeric,
  :'learned_weight'::numeric,
  :'status',
  NULLIF(:'status_reason', ''),
  COALESCE(NULLIF(:'stats_metadata_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (candidate_id) DO UPDATE SET
  candidate_type = EXCLUDED.candidate_type,
  n_exposed = EXCLUDED.n_exposed,
  distinct_case_count = EXCLUDED.distinct_case_count,
  treatment_case_count = EXCLUDED.treatment_case_count,
  control_case_count = EXCLUDED.control_case_count,
  treatment_mean_brier = EXCLUDED.treatment_mean_brier,
  control_mean_brier = EXCLUDED.control_mean_brier,
  raw_uplift = EXCLUDED.raw_uplift,
  shrunken_uplift = EXCLUDED.shrunken_uplift,
  cost_adjusted_uplift = EXCLUDED.cost_adjusted_uplift,
  genericity_penalty = EXCLUDED.genericity_penalty,
  learned_weight = EXCLUDED.learned_weight,
  status = EXCLUDED.status,
  status_reason = EXCLUDED.status_reason,
  stats_metadata = EXCLUDED.stats_metadata,
  updated_at = NOW()
RETURNING json_build_object(
  'candidate_id', candidate_id,
  'candidate_type', candidate_type,
  'n_exposed', n_exposed,
  'status', status,
  'learned_weight', learned_weight
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Compute batch LMD candidate stats from exposures + resolved outcomes')
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


def overlap(left: list[str], right: list[str]) -> bool:
    left_set = {str(item).strip().lower() for item in left if str(item).strip()}
    right_set = {str(item).strip().lower() for item in right if str(item).strip()}
    return bool(left_set & right_set)


def control_case_context(row: dict[str, Any]) -> dict[str, Any]:
    metadata = row.get('projection_metadata') or {}
    case_context = metadata.get('case_context') or {}
    return {
        'question_mechanics': case_context.get('question_mechanics') or [],
        'source_of_truth_class': case_context.get('source_of_truth_class') or [],
        'active_nodes': row.get('active_nodes') or [],
        'candidate_edges': row.get('candidate_edges') or [],
        'contested_edges': row.get('contested_edges') or [],
        'error_pattern': row.get('error_pattern') or '',
        'category': row.get('category') or '',
        'platform': row.get('platform') or '',
    }


def load_intervention_registry() -> dict[str, dict[str, Any]]:
    return {record['intervention_key']: record for record in (build_intervention_record(path) for path in intervention_note_paths())}


def selector_matches_case(selector: dict[str, Any], control_case: dict[str, Any]) -> bool:
    if not selector:
        return True
    if selector.get('categories') and not overlap(selector.get('categories') or [], [control_case.get('category') or '']):
        return False
    if selector.get('platforms') and not overlap(selector.get('platforms') or [], [control_case.get('platform') or '']):
        return False
    mechanics = selector.get('question_mechanics') or []
    if mechanics and not overlap(mechanics, control_case.get('question_mechanics') or []):
        return False
    source_classes = selector.get('source_of_truth_classes') or selector.get('source_of_truth_class') or []
    if source_classes and not overlap(source_classes, control_case.get('source_of_truth_class') or []):
        return False
    return True


def exposure_matches_control(exposure: dict[str, Any], control: dict[str, Any], intervention_registry: dict[str, dict[str, Any]]) -> bool:
    if exposure.get('experiment_id') and exposure.get('experiment_id') != control.get('experiment_id'):
        return False
    if exposure.get('case_key') == control.get('case_key'):
        return False

    notes = exposure.get('notes') or {}
    query_profile = notes.get('query_profile') or {}
    candidate_notes = notes.get('candidate_notes') or {}
    control_ctx = control_case_context(control)

    query_mechanics = query_profile.get('question_mechanics') or []
    if query_mechanics and not overlap(query_mechanics, control_ctx.get('question_mechanics') or []):
        return False
    source_class = query_profile.get('source_of_truth_class') or ''
    if source_class and not overlap([source_class], control_ctx.get('source_of_truth_class') or []):
        return False

    candidate_type = exposure.get('candidate_type')
    candidate_id = str(exposure.get('candidate_id') or '')
    if candidate_type == 'edge':
        edge_key = candidate_id.split(':', 1)[1] if ':' in candidate_id else candidate_id
        return edge_key in (control_ctx.get('candidate_edges') or []) or edge_key in (control_ctx.get('contested_edges') or [])
    if candidate_type == 'case_review':
        error_pattern = str(candidate_notes.get('error_pattern') or '').strip()
        if error_pattern and error_pattern == str(control_ctx.get('error_pattern') or '').strip():
            return True
        return True
    if candidate_type == 'intervention':
        intervention_key = str(candidate_notes.get('intervention_key') or candidate_id.split(':', 1)[1] if ':' in candidate_id else candidate_id).strip()
        intervention = intervention_registry.get(intervention_key) or {}
        return selector_matches_case(intervention.get('target_selector') or {}, control_ctx)
    if candidate_type == 'aggregate_note':
        path = str(exposure.get('candidate_path') or '').lower()
        if 'workflow-performance' in path:
            return 'verification-caution' in (control_ctx.get('active_nodes') or []) or 'verification-caution__increases__fair-value-discounting-pressure' in (control_ctx.get('contested_edges') or [])
        if 'source-performance' in path:
            return 'settlement-source-specificity' in (control_ctx.get('active_nodes') or []) or 'resolution-surface-ambiguity' in (control_ctx.get('active_nodes') or [])
        return True
    return True


def genericity_penalty_for_candidate(candidate_type: str, exposure_rows: list[dict[str, Any]]) -> float:
    penalty = {
        'case_review': 0.04,
        'intervention': 0.05,
        'aggregate_note': 0.12,
        'edge': 0.07,
    }.get(candidate_type, 0.08)
    if candidate_type == 'case_review':
        errors = {str((row.get('notes') or {}).get('candidate_notes', {}).get('error_pattern') or '').strip() for row in exposure_rows}
        if any(err in {'resolved_case_review_pending', 'settlement_or_path_review_pending'} for err in errors):
            penalty += 0.06
    return round(penalty, 4)


def learned_weight(raw_uplift: float | None, shrunken_uplift: float | None, genericity_penalty: float, distinct_case_count: int, candidate_type: str) -> float:
    base = (shrunken_uplift or 0.0) * 35.0
    support_bonus = math.log1p(max(distinct_case_count, 0)) * 0.08
    type_bias = {'case_review': 0.05, 'intervention': 0.08, 'aggregate_note': 0.02, 'edge': 0.04}.get(candidate_type, 0.03)
    weight = base + support_bonus + type_bias - genericity_penalty
    return round(max(-1.0, min(1.0, weight)), 6)


def status_for_candidate(distinct_case_count: int, cost_adjusted_uplift: float | None, learned_weight_value: float) -> tuple[str, str]:
    if distinct_case_count == 0:
        return 'draft', 'no_exposures'
    if distinct_case_count >= 5 and (cost_adjusted_uplift or 0.0) < -0.002:
        return 'retired', 'sustained_negative_cost_adjusted_uplift'
    if distinct_case_count >= 2 and learned_weight_value >= 0.12 and (cost_adjusted_uplift or 0.0) > 0:
        return 'active', 'positive_shrunken_cost_adjusted_uplift'
    if distinct_case_count >= 2 and learned_weight_value < 0:
        return 'hold', 'negative_or_uncertain_weight'
    return 'draft', 'insufficient_support'


def main() -> int:
    args = parse_args()
    resolved_db_url = resolve_db_url(args.db_url)
    table_present = table_exists('lmd_candidate_stats', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False

    exposures = exec_sql(args.psql, resolved_db_url, EXPOSURES_SQL, {'experiment_id': args.experiment_id}) if resolved_db_url else []
    control_pool = exec_sql(args.psql, resolved_db_url, CONTROL_POOL_SQL, {'experiment_id': args.experiment_id}) if resolved_db_url else []
    if not isinstance(exposures, list):
        exposures = []
    if not isinstance(control_pool, list):
        control_pool = []

    intervention_registry = load_intervention_registry()
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in exposures:
        key = (str(row.get('candidate_id') or ''), str(row.get('candidate_type') or ''))
        grouped.setdefault(key, []).append(row)

    results: list[dict[str, Any]] = []
    persisted_count = 0
    for (candidate_id, candidate_type), rows in sorted(grouped.items()):
        exposed_case_to_brier: dict[str, float] = {}
        for row in rows:
            case_key = str(row.get('case_key') or '')
            brier_raw = row.get('latest_brier_component')
            if not case_key or brier_raw is None:
                continue
            exposed_case_to_brier[case_key] = float(brier_raw)
        treatment_values = list(exposed_case_to_brier.values())
        matched_controls: dict[str, float] = {}
        for control in control_pool:
            if exposure_matches_control(rows[0], control, intervention_registry):
                case_key = str(control.get('case_key') or '')
                brier_raw = control.get('latest_brier_component')
                if case_key and brier_raw is not None:
                    matched_controls[case_key] = float(brier_raw)
        treatment_mean = mean(treatment_values)
        control_mean = mean(list(matched_controls.values()))
        raw = (control_mean - treatment_mean) if treatment_mean is not None and control_mean is not None else None
        shrink = ((len(treatment_values) / (len(treatment_values) + args.shrinkage_k)) * raw) if raw is not None else None
        genericity = genericity_penalty_for_candidate(candidate_type, rows)
        cost_adjusted = (shrink - TOKEN_COST_PENALTIES.get(candidate_type, 0.0003)) if shrink is not None else None
        weight = learned_weight(raw, shrink, genericity, len(exposed_case_to_brier), candidate_type)
        status, reason = status_for_candidate(len(exposed_case_to_brier), cost_adjusted, weight)
        stats_metadata = {
            'experiment_id': args.experiment_id,
            'token_cost_penalty': TOKEN_COST_PENALTIES.get(candidate_type, 0.0003),
            'shrinkage_k': args.shrinkage_k,
            'sample_case_keys': sorted(exposed_case_to_brier.keys()),
            'matched_control_case_keys': sorted(matched_controls.keys()),
        }
        record = {
            'candidate_id': candidate_id,
            'candidate_type': candidate_type,
            'n_exposed': len(rows),
            'distinct_case_count': len(exposed_case_to_brier),
            'treatment_case_count': len(exposed_case_to_brier),
            'control_case_count': len(matched_controls),
            'treatment_mean_brier': treatment_mean,
            'control_mean_brier': control_mean,
            'raw_uplift': raw,
            'shrunken_uplift': shrink,
            'cost_adjusted_uplift': cost_adjusted,
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
                    'candidate_id': candidate_id,
                    'candidate_type': candidate_type,
                    'n_exposed': str(record['n_exposed']),
                    'distinct_case_count': str(record['distinct_case_count']),
                    'treatment_case_count': str(record['treatment_case_count']),
                    'control_case_count': str(record['control_case_count']),
                    'treatment_mean_brier': '' if treatment_mean is None else str(round(treatment_mean, 8)),
                    'control_mean_brier': '' if control_mean is None else str(round(control_mean, 8)),
                    'raw_uplift': '' if raw is None else str(round(raw, 8)),
                    'shrunken_uplift': '' if shrink is None else str(round(shrink, 8)),
                    'cost_adjusted_uplift': '' if cost_adjusted is None else str(round(cost_adjusted, 8)),
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
        'exposure_row_count': len(exposures),
        'control_pool_count': len(control_pool),
        'candidate_count': len(results),
        'persisted_count': persisted_count,
        'table_present': table_present,
        'results': results,
    }
    if not resolved_db_url:
        output['warning'] = 'db_url_unavailable'
    elif not table_present:
        output['warning'] = 'lmd_candidate_stats table not present; apply roles/evaluator/sql/026_lmd_candidate_stats.sql'
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
