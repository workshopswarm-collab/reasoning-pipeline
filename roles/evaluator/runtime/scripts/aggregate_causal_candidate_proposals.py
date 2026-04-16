#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
ORCH_ROOT = SCRIPT_PATH.parents[4]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.causal_family_policy import exploratory_trial_for, family_policy_for, load_family_policies  # noqa: E402
from lib.causal_map import build_edge_record, build_node_record, edge_note_paths, node_note_paths  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, missing_columns, resolve_db_url, table_exists  # noqa: E402
from lib.io import write_json  # noqa: E402
from lib.proposed_causal_metadata import (  # noqa: E402
    collect_nearby_keys,
    context_breadth_counts,
    context_distribution,
    dominant_proposal_source,
    proposal_source_mix,
    support_case_breakdown,
)

GENERATED_ROOT = ORCH_ROOT / 'qualitative-db' / '60-causal-map' / 'generated'
SUMMARY_PATH = GENERATED_ROOT / 'proposed-causal-candidates-summary.json'
INDEX_PATH = GENERATED_ROOT / 'proposed-causal-candidates-index.md'

REQUIRED_OCCURRENCE_COLUMNS = [
    'updated_at',
    'mechanism_family',
    'proposal_source',
    'evidence_channels',
    'intervention_dependency',
    'normalized_cluster_key',
    'context_snapshot',
]
REQUIRED_STATS_COLUMNS = [
    'lifecycle_stage',
    'first_seen_at',
    'last_seen_at',
    'proposal_source_mix',
    'dominant_proposal_source',
    'evidence_channel_counts',
    'shadow_match_count',
    'shadow_positive_count',
    'stage_entered_at',
    'promotion_blockers',
    'mechanism_family',
    'normalized_cluster_key',
    'non_intervention_support_case_count',
    'intervention_only_support_case_count',
    'draft_intervention_support_case_count',
    'active_intervention_support_case_count',
    'heuristic_only_support_case_count',
    'review_text_support_case_count',
    'signal_packet_support_case_count',
    'frontmatter_support_case_count',
    'near_duplicate_keys',
    'near_live_graph_keys',
    'max_duplicate_similarity',
    'merge_candidate_key',
    'merge_recommended',
    'distinct_platform_count',
    'distinct_category_count',
    'distinct_question_mechanics_count',
    'distinct_source_of_truth_class_count',
    'distinct_domain_count',
    'context_distribution',
]
REQUIRED_SHADOW_COLUMNS = [
    'outcome_label',
    'outcome_score',
    'outcome_favored',
    'judged_at',
    'judge_version',
    'outcome_metadata',
]
REQUIRED_FAMILY_POLICY_COLUMNS = [
    'description',
    'enabled',
    'max_shadow_candidates',
    'max_trial_candidates',
    'max_active_nodes',
    'max_active_edges',
    'min_shadow_judged_count_for_trial',
    'min_shadow_helpful_count_for_trial',
    'min_shadow_mean_score_for_trial',
    'min_non_intervention_support_cases_for_trial',
    'max_genericity_for_trial',
    'max_duplicate_similarity_for_trial',
    'max_promotion_ready_candidates',
    'min_trial_judged_count_for_promotion',
    'min_trial_helpful_count_for_promotion',
    'min_trial_shrunken_utility_for_promotion',
    'max_trial_harmful_rate_for_promotion',
    'max_contest_case_count_for_promotion',
    'max_genericity_for_promotion',
    'notes',
]
REQUIRED_TRIAL_EXPOSURE_COLUMNS = [
    'preview_only',
    'injected',
    'outcome_label',
    'outcome_score',
    'outcome_favored',
    'judged_at',
    'judge_version',
    'outcome_metadata',
]

OCCURRENCES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT *
  FROM public.proposed_causal_candidate_occurrences
  ORDER BY proposal_id, case_key
) t;
'''

LEGACY_SHADOW_COUNTS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    proposal_id,
    COUNT(*)::int AS shadow_match_count,
    COUNT(*) FILTER (
      WHERE COALESCE(NULLIF(notes->>'outcome_favored', ''), 'false')::boolean = true
    )::int AS shadow_positive_count,
    0::int AS shadow_helpful_count,
    0::int AS shadow_neutral_count,
    0::int AS shadow_harmful_count,
    0::int AS shadow_unclear_count,
    0::int AS shadow_judged_count,
    0::numeric AS shadow_score_sum,
    NULL::numeric AS shadow_mean_score
  FROM public.proposed_causal_shadow_matches
  GROUP BY proposal_id
) t;
'''

SHADOW_COUNTS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    proposal_id,
    COUNT(*)::int AS shadow_match_count,
    COUNT(*) FILTER (
      WHERE outcome_label = 'helpful' OR outcome_favored IS TRUE
    )::int AS shadow_positive_count,
    COUNT(*) FILTER (
      WHERE outcome_label = 'helpful' OR outcome_favored IS TRUE
    )::int AS shadow_helpful_count,
    COUNT(*) FILTER (
      WHERE outcome_label = 'neutral'
    )::int AS shadow_neutral_count,
    COUNT(*) FILTER (
      WHERE outcome_label = 'harmful'
    )::int AS shadow_harmful_count,
    COUNT(*) FILTER (
      WHERE outcome_label = 'unclear'
    )::int AS shadow_unclear_count,
    COUNT(*) FILTER (
      WHERE NULLIF(outcome_label, '') IS NOT NULL
    )::int AS shadow_judged_count,
    COALESCE(SUM(COALESCE(outcome_score, 0)), 0)::numeric AS shadow_score_sum,
    AVG(outcome_score)::numeric AS shadow_mean_score
  FROM public.proposed_causal_shadow_matches
  GROUP BY proposal_id
) t;
'''

FAMILY_POLICIES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY mechanism_family), '[]'::json)::text
FROM (
  SELECT *
  FROM public.causal_family_policies
) t;
'''

LEGACY_TRIAL_COUNTS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    proposal_id,
    COUNT(*) FILTER (WHERE injected IS TRUE)::int AS trial_exposure_count,
    COUNT(*) FILTER (WHERE preview_only IS TRUE)::int AS trial_preview_count,
    0::int AS trial_helpful_count,
    0::int AS trial_neutral_count,
    0::int AS trial_harmful_count,
    0::int AS trial_unclear_count,
    0::int AS trial_judged_count,
    0::numeric AS trial_score_sum,
    NULL::numeric AS trial_mean_score
  FROM public.proposed_causal_trial_exposures
  GROUP BY proposal_id
) t;
'''

TRIAL_COUNTS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    proposal_id,
    COUNT(*) FILTER (WHERE injected IS TRUE)::int AS trial_exposure_count,
    COUNT(*) FILTER (WHERE preview_only IS TRUE)::int AS trial_preview_count,
    COUNT(*) FILTER (WHERE injected IS TRUE AND (outcome_label = 'helpful' OR outcome_favored IS TRUE))::int AS trial_helpful_count,
    COUNT(*) FILTER (WHERE injected IS TRUE AND outcome_label = 'neutral')::int AS trial_neutral_count,
    COUNT(*) FILTER (WHERE injected IS TRUE AND outcome_label = 'harmful')::int AS trial_harmful_count,
    COUNT(*) FILTER (WHERE injected IS TRUE AND outcome_label = 'unclear')::int AS trial_unclear_count,
    COUNT(*) FILTER (WHERE injected IS TRUE AND NULLIF(outcome_label, '') IS NOT NULL)::int AS trial_judged_count,
    COALESCE(SUM(CASE WHEN injected IS TRUE THEN COALESCE(outcome_score, 0) ELSE 0 END), 0)::numeric AS trial_score_sum,
    AVG(CASE WHEN injected IS TRUE THEN outcome_score ELSE NULL END)::numeric AS trial_mean_score
  FROM public.proposed_causal_trial_exposures
  GROUP BY proposal_id
) t;
'''

OPEN_HEALTH_VIOLATIONS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    entity_key,
    COUNT(*)::int AS open_violation_count
  FROM public.causal_graph_health_violations
  WHERE COALESCE(NULLIF(status, ''), 'open') NOT IN ('resolved', 'closed')
  GROUP BY entity_key
) t;
'''

DELETE_STALE_SQL = r'''
DELETE FROM public.proposed_causal_candidate_stats
WHERE proposal_id NOT IN (
  SELECT DISTINCT proposal_id
  FROM public.proposed_causal_candidate_occurrences
);
'''

UPSERT_SQL = r'''
INSERT INTO public.proposed_causal_candidate_stats (
  proposal_id,
  proposal_key,
  candidate_type,
  candidate_label,
  mechanism_family,
  normalized_cluster_key,
  source_node_key,
  target_node_key,
  node_type,
  effect_sign,
  occurrence_count,
  distinct_case_count,
  support_case_count,
  contest_case_count,
  non_intervention_support_case_count,
  intervention_only_support_case_count,
  draft_intervention_support_case_count,
  active_intervention_support_case_count,
  heuristic_only_support_case_count,
  review_text_support_case_count,
  signal_packet_support_case_count,
  frontmatter_support_case_count,
  duplicate_of_live_graph,
  genericity_penalty,
  promotion_score,
  promotion_status,
  promotion_reason,
  lifecycle_stage,
  first_seen_at,
  last_seen_at,
  proposal_source_mix,
  dominant_proposal_source,
  evidence_channel_counts,
  shadow_match_count,
  shadow_positive_count,
  stage_entered_at,
  promotion_blockers,
  near_duplicate_keys,
  near_live_graph_keys,
  max_duplicate_similarity,
  merge_candidate_key,
  merge_recommended,
  distinct_platform_count,
  distinct_category_count,
  distinct_question_mechanics_count,
  distinct_source_of_truth_class_count,
  distinct_domain_count,
  context_distribution,
  supporting_case_keys,
  threshold_profile,
  stats_metadata,
  updated_at
)
VALUES (
  :'proposal_id',
  :'proposal_key',
  :'candidate_type',
  :'candidate_label',
  COALESCE(NULLIF(:'mechanism_family', ''), 'unassigned'),
  NULLIF(:'normalized_cluster_key', ''),
  NULLIF(:'source_node_key', ''),
  NULLIF(:'target_node_key', ''),
  NULLIF(:'node_type', ''),
  NULLIF(:'effect_sign', ''),
  :'occurrence_count'::int,
  :'distinct_case_count'::int,
  :'support_case_count'::int,
  :'contest_case_count'::int,
  :'non_intervention_support_case_count'::int,
  :'intervention_only_support_case_count'::int,
  :'draft_intervention_support_case_count'::int,
  :'active_intervention_support_case_count'::int,
  :'heuristic_only_support_case_count'::int,
  :'review_text_support_case_count'::int,
  :'signal_packet_support_case_count'::int,
  :'frontmatter_support_case_count'::int,
  COALESCE(NULLIF(:'duplicate_of_live_graph', '')::boolean, false),
  :'genericity_penalty'::numeric,
  :'promotion_score'::numeric,
  :'promotion_status',
  NULLIF(:'promotion_reason', ''),
  :'lifecycle_stage',
  NULLIF(:'first_seen_at', '')::timestamptz,
  NULLIF(:'last_seen_at', '')::timestamptz,
  COALESCE(NULLIF(:'proposal_source_mix_json', ''), '{}')::jsonb,
  NULLIF(:'dominant_proposal_source', ''),
  COALESCE(NULLIF(:'evidence_channel_counts_json', ''), '{}')::jsonb,
  :'shadow_match_count'::int,
  :'shadow_positive_count'::int,
  COALESCE(NULLIF(:'stage_entered_at', '')::timestamptz, NOW()),
  COALESCE(NULLIF(:'promotion_blockers_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'near_duplicate_keys_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'near_live_graph_keys_json', ''), '[]')::jsonb,
  NULLIF(:'max_duplicate_similarity', '')::numeric,
  NULLIF(:'merge_candidate_key', ''),
  COALESCE(NULLIF(:'merge_recommended', '')::boolean, false),
  :'distinct_platform_count'::int,
  :'distinct_category_count'::int,
  :'distinct_question_mechanics_count'::int,
  :'distinct_source_of_truth_class_count'::int,
  :'distinct_domain_count'::int,
  COALESCE(NULLIF(:'context_distribution_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'supporting_case_keys_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'threshold_profile_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'stats_metadata_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (proposal_id) DO UPDATE SET
  proposal_key = EXCLUDED.proposal_key,
  candidate_type = EXCLUDED.candidate_type,
  candidate_label = EXCLUDED.candidate_label,
  mechanism_family = EXCLUDED.mechanism_family,
  normalized_cluster_key = EXCLUDED.normalized_cluster_key,
  source_node_key = EXCLUDED.source_node_key,
  target_node_key = EXCLUDED.target_node_key,
  node_type = EXCLUDED.node_type,
  effect_sign = EXCLUDED.effect_sign,
  occurrence_count = EXCLUDED.occurrence_count,
  distinct_case_count = EXCLUDED.distinct_case_count,
  support_case_count = EXCLUDED.support_case_count,
  contest_case_count = EXCLUDED.contest_case_count,
  non_intervention_support_case_count = EXCLUDED.non_intervention_support_case_count,
  intervention_only_support_case_count = EXCLUDED.intervention_only_support_case_count,
  draft_intervention_support_case_count = EXCLUDED.draft_intervention_support_case_count,
  active_intervention_support_case_count = EXCLUDED.active_intervention_support_case_count,
  heuristic_only_support_case_count = EXCLUDED.heuristic_only_support_case_count,
  review_text_support_case_count = EXCLUDED.review_text_support_case_count,
  signal_packet_support_case_count = EXCLUDED.signal_packet_support_case_count,
  frontmatter_support_case_count = EXCLUDED.frontmatter_support_case_count,
  duplicate_of_live_graph = EXCLUDED.duplicate_of_live_graph,
  genericity_penalty = EXCLUDED.genericity_penalty,
  promotion_score = EXCLUDED.promotion_score,
  promotion_status = EXCLUDED.promotion_status,
  promotion_reason = EXCLUDED.promotion_reason,
  lifecycle_stage = EXCLUDED.lifecycle_stage,
  first_seen_at = COALESCE(LEAST(public.proposed_causal_candidate_stats.first_seen_at, EXCLUDED.first_seen_at), public.proposed_causal_candidate_stats.first_seen_at, EXCLUDED.first_seen_at),
  last_seen_at = EXCLUDED.last_seen_at,
  proposal_source_mix = EXCLUDED.proposal_source_mix,
  dominant_proposal_source = EXCLUDED.dominant_proposal_source,
  evidence_channel_counts = EXCLUDED.evidence_channel_counts,
  shadow_match_count = EXCLUDED.shadow_match_count,
  shadow_positive_count = EXCLUDED.shadow_positive_count,
  stage_entered_at = CASE
    WHEN public.proposed_causal_candidate_stats.lifecycle_stage IS DISTINCT FROM EXCLUDED.lifecycle_stage THEN NOW()
    ELSE COALESCE(public.proposed_causal_candidate_stats.stage_entered_at, EXCLUDED.stage_entered_at, NOW())
  END,
  promotion_blockers = EXCLUDED.promotion_blockers,
  near_duplicate_keys = EXCLUDED.near_duplicate_keys,
  near_live_graph_keys = EXCLUDED.near_live_graph_keys,
  max_duplicate_similarity = EXCLUDED.max_duplicate_similarity,
  merge_candidate_key = EXCLUDED.merge_candidate_key,
  merge_recommended = EXCLUDED.merge_recommended,
  distinct_platform_count = EXCLUDED.distinct_platform_count,
  distinct_category_count = EXCLUDED.distinct_category_count,
  distinct_question_mechanics_count = EXCLUDED.distinct_question_mechanics_count,
  distinct_source_of_truth_class_count = EXCLUDED.distinct_source_of_truth_class_count,
  distinct_domain_count = EXCLUDED.distinct_domain_count,
  context_distribution = EXCLUDED.context_distribution,
  supporting_case_keys = EXCLUDED.supporting_case_keys,
  threshold_profile = EXCLUDED.threshold_profile,
  stats_metadata = EXCLUDED.stats_metadata,
  updated_at = NOW()
RETURNING json_build_object(
  'proposal_id', proposal_id,
  'candidate_type', candidate_type,
  'promotion_status', promotion_status,
  'lifecycle_stage', lifecycle_stage,
  'promotion_score', promotion_score
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Aggregate mined causal candidate occurrences into proposal stats')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0



def min_timestamp(rows: list[dict[str, Any]], *keys: str) -> str:
    values: list[str] = []
    for row in rows:
        for key in keys:
            value = str(row.get(key) or '').strip()
            if value:
                values.append(value)
                break
    return min(values) if values else ''



def max_timestamp(rows: list[dict[str, Any]], *keys: str) -> str:
    values: list[str] = []
    for row in rows:
        for key in keys:
            value = str(row.get(key) or '').strip()
            if value:
                values.append(value)
                break
    return max(values) if values else ''



def evidence_channel_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for row in rows:
        raw = row.get('evidence_channels') or []
        if isinstance(raw, list):
            for item in raw:
                text = str(item).strip()
                if text:
                    counts[text] += 1
    return dict(sorted(counts.items()))



def intervention_dependency_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for row in rows:
        dependency = str(row.get('intervention_dependency') or '').strip() or 'none'
        counts[dependency] += 1
    return dict(sorted(counts.items()))



def load_live_graph() -> tuple[dict[str, str], dict[str, str]]:
    node_labels = {record['node_key']: record['node_label'] for record in (build_node_record(path) for path in node_note_paths())}
    edge_labels = {record['edge_key']: record['edge_label'] for record in (build_edge_record(path) for path in edge_note_paths())}
    return node_labels, edge_labels



def load_live_family_state() -> dict[str, dict[str, Any]]:
    state: dict[str, dict[str, Any]] = {}

    def ensure(family: str) -> dict[str, Any]:
        return state.setdefault(
            family,
            {
                'live_nodes': {'total': 0, 'by_stage': {}},
                'live_edges': {'total': 0, 'by_stage': {}},
            },
        )

    for path in node_note_paths():
        record = build_node_record(path)
        family = str(record.get('mechanism_family') or 'unassigned')
        stage = str(record.get('lifecycle_stage') or 'draft')
        row = ensure(family)
        row['live_nodes']['total'] += 1
        row['live_nodes']['by_stage'][stage] = int(row['live_nodes']['by_stage'].get(stage) or 0) + 1

    for path in edge_note_paths():
        record = build_edge_record(path)
        family = str(record.get('mechanism_family') or 'unassigned')
        stage = str(record.get('lifecycle_stage') or 'draft')
        row = ensure(family)
        row['live_edges']['total'] += 1
        row['live_edges']['by_stage'][stage] = int(row['live_edges']['by_stage'].get(stage) or 0) + 1

    return state



SHADOW_TRIAL_PRIOR_SAMPLE_SIZE = 4.0
TRIAL_UTILITY_PRIOR_SAMPLE_SIZE = 6.0



def shadow_trial_score(record: dict[str, Any]) -> float | None:
    judged_count = int(record.get('shadow_judged_count') or 0)
    score_sum = float(record.get('shadow_score_sum') or 0.0)
    if judged_count <= 0 and SHADOW_TRIAL_PRIOR_SAMPLE_SIZE <= 0:
        return None
    denominator = judged_count + SHADOW_TRIAL_PRIOR_SAMPLE_SIZE
    if denominator <= 0:
        return None
    return round(score_sum / denominator, 6)



def shadow_label_balance(record: dict[str, Any]) -> int:
    return int(record.get('shadow_helpful_count') or 0) - int(record.get('shadow_harmful_count') or 0)



def trial_shrunken_utility(record: dict[str, Any]) -> float | None:
    exposure_count = int(record.get('trial_exposure_count') or 0)
    score_sum = float(record.get('trial_score_sum') or 0.0)
    if exposure_count <= 0 and TRIAL_UTILITY_PRIOR_SAMPLE_SIZE <= 0:
        return None
    denominator = exposure_count + TRIAL_UTILITY_PRIOR_SAMPLE_SIZE
    if denominator <= 0:
        return None
    return round(score_sum / denominator, 6)



def trial_label_balance(record: dict[str, Any]) -> int:
    return int(record.get('trial_helpful_count') or 0) - int(record.get('trial_harmful_count') or 0)



def trial_harmful_rate(record: dict[str, Any]) -> float | None:
    exposure_count = int(record.get('trial_exposure_count') or 0)
    if exposure_count <= 0:
        return None
    return round(float(record.get('trial_harmful_count') or 0) / exposure_count, 6)



def promotion_ready_sort_key(record: dict[str, Any]) -> tuple[Any, ...]:
    shrunken_utility = record.get('trial_shrunken_utility')
    normalized_utility = float(shrunken_utility) if shrunken_utility not in (None, '') else -999.0
    harmful_rate = trial_harmful_rate(record)
    normalized_harmful_rate = float(harmful_rate) if harmful_rate not in (None, '') else 999.0
    return (
        -normalized_utility,
        -int(record.get('trial_helpful_count') or 0),
        normalized_harmful_rate,
        int(record.get('contest_case_count') or 0),
        float(record.get('genericity_penalty') or 0.0),
        -float(record.get('promotion_score') or 0.0),
        str(record.get('proposal_id') or ''),
    )



def trial_priority_sort_key(record: dict[str, Any]) -> tuple[Any, ...]:
    trial_score = record.get('shadow_trial_score')
    normalized_trial_score = float(trial_score) if trial_score not in (None, '') else -999.0
    return (
        -int(record.get('shadow_helpful_count') or 0),
        -normalized_trial_score,
        -shadow_label_balance(record),
        -int(record.get('shadow_judged_count') or 0),
        -int(record.get('non_intervention_support_case_count') or 0),
        -float(record.get('promotion_score') or 0.0),
        float(record.get('genericity_penalty') or 0.0),
        str(record.get('proposal_id') or ''),
    )



def base_lifecycle_stage_for_record(record: dict[str, Any]) -> str:
    if record['duplicate_of_live_graph']:
        return 'duplicate_of_live_graph'
    if record['occurrence_count'] <= 0:
        return 'observed'
    if int(record.get('shadow_match_count') or 0) > 0:
        return 'shadow_candidate'
    return 'aggregated'



def non_budget_trial_blockers_for_record(record: dict[str, Any], policy: dict[str, Any], *, within_shadow_budget: bool) -> list[str]:
    blockers: list[str] = []
    max_duplicate_similarity = record.get('max_duplicate_similarity')
    if not bool(policy.get('enabled', True)):
        blockers.append('family_policy_disabled')
    if str(record.get('promotion_status') or '') not in {'proposed', 'draft_recommendation'}:
        blockers.append('below_base_proposal_threshold')
    if row_duplicate := bool(record.get('duplicate_of_live_graph')):
        if row_duplicate:
            blockers.append('duplicate_of_live_graph')
    if str(record.get('mechanism_family') or 'unassigned') == 'unassigned':
        blockers.append('unassigned_mechanism_family')
    if row_merge := bool(record.get('merge_recommended')):
        if row_merge:
            blockers.append('merge_recommended')
    if int(record.get('shadow_match_count') or 0) <= 0:
        blockers.append('no_shadow_matches')
    if not within_shadow_budget:
        blockers.append('outside_family_shadow_budget')
    if int(record.get('shadow_judged_count') or 0) < int(policy.get('min_shadow_judged_count_for_trial') or 0):
        blockers.append('below_family_min_shadow_judged_count')
    if int(record.get('shadow_helpful_count') or 0) < int(policy.get('min_shadow_helpful_count_for_trial') or 0):
        blockers.append('below_family_min_shadow_helpful_count')
    trial_score = record.get('shadow_trial_score')
    if trial_score in (None, ''):
        blockers.append('no_shadow_trial_score')
    elif float(trial_score) < float(policy.get('min_shadow_mean_score_for_trial') or 0.0):
        blockers.append('below_family_min_shadow_mean_score')
    if int(record.get('non_intervention_support_case_count') or 0) < int(policy.get('min_non_intervention_support_cases_for_trial') or 0):
        blockers.append('below_family_min_non_intervention_support_cases')
    if float(record.get('genericity_penalty') or 0.0) > float(policy.get('max_genericity_for_trial') or 0.0):
        blockers.append('genericity_above_family_trial_limit')
    if max_duplicate_similarity not in (None, '') and float(max_duplicate_similarity) > float(policy.get('max_duplicate_similarity_for_trial') or 0.0):
        blockers.append('duplicate_similarity_above_family_trial_limit')
    return sorted(dict.fromkeys(blockers))



def trial_gate_details_for_record(
    record: dict[str, Any],
    policy: dict[str, Any],
    *,
    within_shadow_budget: bool,
    open_violation_count: int = 0,
) -> dict[str, dict[str, Any]]:
    shadow_trial_score_value = record.get('shadow_trial_score')
    current_shadow_trial_score = None if shadow_trial_score_value in (None, '') else float(shadow_trial_score_value)
    max_duplicate_similarity = record.get('max_duplicate_similarity')
    current_duplicate_similarity = None if max_duplicate_similarity in (None, '') else float(max_duplicate_similarity)
    return {
        'family_policy_enabled': {
            'passed': bool(policy.get('enabled', True)),
        },
        'base_proposal_threshold': {
            'passed': str(record.get('promotion_status') or '') in {'proposed', 'draft_recommendation'},
            'current': str(record.get('promotion_status') or ''),
            'required_any_of': ['proposed', 'draft_recommendation'],
        },
        'duplicate_of_live_graph': {
            'passed': not bool(record.get('duplicate_of_live_graph')),
            'current': bool(record.get('duplicate_of_live_graph')),
        },
        'mechanism_family_assignment': {
            'passed': str(record.get('mechanism_family') or 'unassigned') != 'unassigned',
            'current': str(record.get('mechanism_family') or 'unassigned'),
        },
        'merge_recommended': {
            'passed': not bool(record.get('merge_recommended')),
            'current': bool(record.get('merge_recommended')),
        },
        'shadow_matches': {
            'passed': int(record.get('shadow_match_count') or 0) > 0,
            'current': int(record.get('shadow_match_count') or 0),
            'minimum': 1,
        },
        'family_shadow_budget': {
            'passed': within_shadow_budget,
            'current': bool(within_shadow_budget),
        },
        'shadow_judged_count': {
            'passed': int(record.get('shadow_judged_count') or 0) >= int(policy.get('min_shadow_judged_count_for_trial') or 0),
            'current': int(record.get('shadow_judged_count') or 0),
            'minimum': int(policy.get('min_shadow_judged_count_for_trial') or 0),
        },
        'shadow_helpful_count': {
            'passed': int(record.get('shadow_helpful_count') or 0) >= int(policy.get('min_shadow_helpful_count_for_trial') or 0),
            'current': int(record.get('shadow_helpful_count') or 0),
            'minimum': int(policy.get('min_shadow_helpful_count_for_trial') or 0),
        },
        'shadow_trial_score': {
            'passed': current_shadow_trial_score is not None and current_shadow_trial_score >= float(policy.get('min_shadow_mean_score_for_trial') or 0.0),
            'current': current_shadow_trial_score,
            'minimum': float(policy.get('min_shadow_mean_score_for_trial') or 0.0),
        },
        'non_intervention_support_case_count': {
            'passed': int(record.get('non_intervention_support_case_count') or 0) >= int(policy.get('min_non_intervention_support_cases_for_trial') or 0),
            'current': int(record.get('non_intervention_support_case_count') or 0),
            'minimum': int(policy.get('min_non_intervention_support_cases_for_trial') or 0),
        },
        'genericity_penalty': {
            'passed': float(record.get('genericity_penalty') or 0.0) <= float(policy.get('max_genericity_for_trial') or 0.0),
            'current': float(record.get('genericity_penalty') or 0.0),
            'maximum': float(policy.get('max_genericity_for_trial') or 0.0),
        },
        'duplicate_similarity': {
            'passed': current_duplicate_similarity is None or current_duplicate_similarity <= float(policy.get('max_duplicate_similarity_for_trial') or 0.0),
            'current': current_duplicate_similarity,
            'maximum': float(policy.get('max_duplicate_similarity_for_trial') or 0.0),
        },
        'open_health_violations': {
            'passed': int(open_violation_count or 0) <= 0,
            'current': int(open_violation_count or 0),
            'maximum': 0,
        },
    }



def exploratory_trial_blockers_for_record(
    record: dict[str, Any],
    policy: dict[str, Any],
    exploratory: dict[str, Any],
    *,
    within_shadow_budget: bool,
    open_violation_count: int,
) -> list[str]:
    blockers: list[str] = []
    if not bool(exploratory.get('enabled')) or int(exploratory.get('max_candidates') or 0) <= 0:
        return ['exploratory_trial_disabled']
    if not bool(policy.get('enabled', True)):
        blockers.append('family_policy_disabled')
    if bool(exploratory.get('require_base_proposal_threshold')) and str(record.get('promotion_status') or '') not in {'proposed', 'draft_recommendation'}:
        blockers.append('below_base_proposal_threshold')
    if bool(record.get('duplicate_of_live_graph')):
        blockers.append('duplicate_of_live_graph')
    if str(record.get('mechanism_family') or 'unassigned') == 'unassigned':
        blockers.append('unassigned_mechanism_family')
    if bool(record.get('merge_recommended')):
        blockers.append('merge_recommended')
    if int(record.get('shadow_match_count') or 0) <= 0:
        blockers.append('no_shadow_matches')
    if not within_shadow_budget:
        blockers.append('outside_family_shadow_budget')
    if int(record.get('shadow_judged_count') or 0) < int(exploratory.get('min_shadow_judged_count') or 0):
        blockers.append('below_exploratory_min_shadow_judged_count')
    if int(record.get('shadow_helpful_count') or 0) < int(exploratory.get('min_shadow_helpful_count') or 0):
        blockers.append('below_exploratory_min_shadow_helpful_count')
    trial_score = record.get('shadow_trial_score')
    if trial_score in (None, ''):
        blockers.append('no_shadow_trial_score')
    elif float(trial_score) < float(exploratory.get('min_shadow_trial_score') or 0.0):
        blockers.append('below_exploratory_min_shadow_trial_score')
    if int(record.get('non_intervention_support_case_count') or 0) < int(exploratory.get('min_non_intervention_support_cases') or 0):
        blockers.append('below_exploratory_min_non_intervention_support_cases')
    if float(record.get('genericity_penalty') or 0.0) > float(policy.get('max_genericity_for_trial') or 0.0):
        blockers.append('genericity_above_family_trial_limit')
    max_duplicate_similarity = record.get('max_duplicate_similarity')
    if max_duplicate_similarity not in (None, '') and float(max_duplicate_similarity) > float(policy.get('max_duplicate_similarity_for_trial') or 0.0):
        blockers.append('duplicate_similarity_above_family_trial_limit')
    if int(open_violation_count or 0) > 0:
        blockers.append('open_health_violations')
    return sorted(dict.fromkeys(blockers))



def attach_family_policy_state(
    proposals: list[dict[str, Any]],
    *,
    family_policy_rows: dict[str, dict[str, Any]],
    live_family_state: dict[str, dict[str, Any]],
    open_health_violations_by_key: dict[str, int],
) -> dict[str, dict[str, Any]]:
    proposals_by_family: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in proposals:
        family = str(record.get('mechanism_family') or 'unassigned')
        proposals_by_family[family].append(record)

    family_summary: dict[str, dict[str, Any]] = {}
    all_families = sorted({*family_policy_rows.keys(), *live_family_state.keys(), *proposals_by_family.keys()})
    for family in all_families:
        policy = family_policy_for(family, loaded=family_policy_rows)
        rows = proposals_by_family.get(family, [])
        live_state = live_family_state.get(family) or {
            'live_nodes': {'total': 0, 'by_stage': {}},
            'live_edges': {'total': 0, 'by_stage': {}},
        }
        shadow_rows = [row for row in rows if int(row.get('shadow_match_count') or 0) > 0]
        for row in rows:
            row['shadow_trial_score'] = shadow_trial_score(row)
            row['shadow_label_balance'] = shadow_label_balance(row)
            row['trial_shrunken_utility'] = trial_shrunken_utility(row)
            row['trial_label_balance'] = trial_label_balance(row)
            row['trial_harmful_rate'] = trial_harmful_rate(row)

        ranked_shadow_rows = sorted(shadow_rows, key=trial_priority_sort_key)
        shadow_budget = int(policy.get('max_shadow_candidates') or 0)
        max_trial_candidates = int(policy.get('max_trial_candidates') or 0)
        max_promotion_ready_candidates = int(policy.get('max_promotion_ready_candidates') or 0)
        exploratory_trial = exploratory_trial_for(policy)
        shadow_rank_map = {row['proposal_id']: index + 1 for index, row in enumerate(ranked_shadow_rows)}

        open_violation_count_by_proposal: dict[str, int] = {}
        for row in rows:
            pid = row['proposal_id']
            proposal_key = str(row.get('proposal_key') or '').strip()
            open_violation_count_by_proposal[pid] = int(open_health_violations_by_key.get(pid, 0) or 0) + int(open_health_violations_by_key.get(proposal_key, 0) or 0)

        trial_gate_details_by_proposal: dict[str, dict[str, Any]] = {}
        base_trial_blockers_by_proposal: dict[str, list[str]] = {}
        exploratory_trial_blockers_by_proposal: dict[str, list[str]] = {}
        for row in rows:
            pid = row['proposal_id']
            shadow_rank = shadow_rank_map.get(pid)
            within_shadow_budget = bool(shadow_rank is not None and shadow_rank <= shadow_budget)
            open_violation_count = open_violation_count_by_proposal.get(pid, 0)
            trial_gate_details_by_proposal[pid] = trial_gate_details_for_record(
                row,
                policy,
                within_shadow_budget=within_shadow_budget,
                open_violation_count=open_violation_count,
            )
            base_trial_blockers_by_proposal[pid] = non_budget_trial_blockers_for_record(row, policy, within_shadow_budget=within_shadow_budget)
            exploratory_trial_blockers_by_proposal[pid] = exploratory_trial_blockers_for_record(
                row,
                policy,
                exploratory_trial,
                within_shadow_budget=within_shadow_budget,
                open_violation_count=open_violation_count,
            )

        prelim_trial_rows = [row for row in rows if not base_trial_blockers_by_proposal.get(row['proposal_id'])]
        ranked_trial_rows = sorted(prelim_trial_rows, key=trial_priority_sort_key)
        trial_rank_map = {row['proposal_id']: index + 1 for index, row in enumerate(ranked_trial_rows)}

        trial_state_by_proposal: dict[str, dict[str, Any]] = {}
        final_trial_candidates = 0
        for row in rows:
            pid = row['proposal_id']
            trial_rank = trial_rank_map.get(pid)
            trial_blockers = list(base_trial_blockers_by_proposal.get(pid) or [])
            if trial_rank is None and not trial_blockers and max_trial_candidates <= 0:
                trial_blockers.append('outside_family_trial_budget')
            elif trial_rank is not None and trial_rank > max_trial_candidates:
                trial_blockers.append('outside_family_trial_budget')
            within_trial_budget = bool(trial_rank is not None and trial_rank <= max_trial_candidates)
            standard_eligible = not trial_blockers and within_trial_budget
            if standard_eligible:
                final_trial_candidates += 1
            trial_state_by_proposal[pid] = {
                'trial_rank': trial_rank,
                'within_trial_budget': within_trial_budget,
                'standard_trial_blockers': sorted(dict.fromkeys(trial_blockers)),
                'trial_blockers': sorted(dict.fromkeys(trial_blockers)),
                'standard_eligible': standard_eligible,
                'exploratory_eligible': False,
                'eligible': standard_eligible,
                'eligibility_mode': 'standard' if standard_eligible else 'blocked',
                'exploratory_rank': None,
                'within_exploratory_budget': False,
                'exploratory_trial_blockers': exploratory_trial_blockers_by_proposal.get(pid) or [],
            }

        exploratory_prelim_rows = [
            row
            for row in rows
            if not trial_state_by_proposal.get(row['proposal_id'], {}).get('standard_eligible')
            and not exploratory_trial_blockers_by_proposal.get(row['proposal_id'])
        ]
        ranked_exploratory_rows = sorted(exploratory_prelim_rows, key=trial_priority_sort_key)
        exploratory_rank_map = {row['proposal_id']: index + 1 for index, row in enumerate(ranked_exploratory_rows)}
        exploratory_max_candidates = int(exploratory_trial.get('max_candidates') or 0)
        final_exploratory_trial_candidates = 0
        for row in rows:
            pid = row['proposal_id']
            exploratory_rank = exploratory_rank_map.get(pid)
            exploratory_blockers = list(exploratory_trial_blockers_by_proposal.get(pid) or [])
            if exploratory_rank is None and not exploratory_blockers and exploratory_max_candidates <= 0:
                exploratory_blockers.append('outside_exploratory_trial_budget')
            elif exploratory_rank is not None and exploratory_rank > exploratory_max_candidates:
                exploratory_blockers.append('outside_exploratory_trial_budget')
            within_exploratory_budget = bool(exploratory_rank is not None and exploratory_rank <= exploratory_max_candidates)
            exploratory_eligible = not exploratory_blockers and within_exploratory_budget
            if exploratory_eligible:
                final_exploratory_trial_candidates += 1
            state = trial_state_by_proposal[pid]
            state['exploratory_rank'] = exploratory_rank
            state['within_exploratory_budget'] = within_exploratory_budget
            state['exploratory_trial_blockers'] = sorted(dict.fromkeys(exploratory_blockers))
            state['exploratory_eligible'] = exploratory_eligible
            if not state['standard_eligible'] and exploratory_eligible:
                state['eligible'] = True
                state['eligibility_mode'] = 'exploratory'
                state['trial_blockers'] = []

        eligible_trial_rows = [row for row in rows if trial_state_by_proposal.get(row['proposal_id'], {}).get('eligible')]
        ranked_promotion_rows = sorted(eligible_trial_rows, key=promotion_ready_sort_key)
        promotion_rank_map = {row['proposal_id']: index + 1 for index, row in enumerate(ranked_promotion_rows)}

        promotion_state_by_proposal: dict[str, dict[str, Any]] = {}
        final_promotion_ready_candidates = 0
        for row in rows:
            pid = row['proposal_id']
            proposal_key = str(row.get('proposal_key') or '').strip()
            promotion_rank = promotion_rank_map.get(pid)
            promotion_blockers: list[str] = []
            trial_state = trial_state_by_proposal.get(pid) or {}
            if not bool(trial_state.get('eligible')):
                promotion_blockers.append('not_trial_candidate')
            if not bool(policy.get('enabled', True)):
                promotion_blockers.append('family_policy_disabled')
            if bool(row.get('duplicate_of_live_graph')):
                promotion_blockers.append('duplicate_of_live_graph')
            if bool(row.get('merge_recommended')):
                promotion_blockers.append('merge_recommended')
            if int(row.get('trial_judged_count') or 0) < int(policy.get('min_trial_judged_count_for_promotion') or 0):
                promotion_blockers.append('below_family_min_trial_judged_count')
            if int(row.get('trial_helpful_count') or 0) < int(policy.get('min_trial_helpful_count_for_promotion') or 0):
                promotion_blockers.append('below_family_min_trial_helpful_count')
            shrunken_utility = row.get('trial_shrunken_utility')
            if shrunken_utility in (None, ''):
                promotion_blockers.append('no_trial_shrunken_utility')
            elif float(shrunken_utility) < float(policy.get('min_trial_shrunken_utility_for_promotion') or 0.0):
                promotion_blockers.append('below_family_min_trial_shrunken_utility')
            harmful_rate = row.get('trial_harmful_rate')
            if harmful_rate not in (None, '') and float(harmful_rate) > float(policy.get('max_trial_harmful_rate_for_promotion') or 0.0):
                promotion_blockers.append('harmful_trial_rate_too_high')
            if int(row.get('contest_case_count') or 0) > int(policy.get('max_contest_case_count_for_promotion') or 0):
                promotion_blockers.append('contest_case_count_above_family_limit')
            if float(row.get('genericity_penalty') or 0.0) > float(policy.get('max_genericity_for_promotion') or 0.0):
                promotion_blockers.append('genericity_above_family_promotion_limit')
            open_violation_count = int(open_violation_count_by_proposal.get(pid, 0) or 0)
            if open_violation_count > 0:
                promotion_blockers.append('open_health_violations')
            if promotion_rank is None and not promotion_blockers and max_promotion_ready_candidates <= 0:
                promotion_blockers.append('outside_family_promotion_budget')
            elif promotion_rank is not None and promotion_rank > max_promotion_ready_candidates:
                promotion_blockers.append('family_slot_taken_by_stronger_sibling')
            within_promotion_budget = bool(promotion_rank is not None and promotion_rank <= max_promotion_ready_candidates)
            eligible = not promotion_blockers and within_promotion_budget
            if eligible:
                final_promotion_ready_candidates += 1
            promotion_state_by_proposal[pid] = {
                'promotion_rank': promotion_rank,
                'within_promotion_budget': within_promotion_budget,
                'promotion_blockers': sorted(dict.fromkeys(promotion_blockers)),
                'eligible': eligible,
                'open_violation_count': open_violation_count,
            }

        stage_counts: Counter[str] = Counter()
        standard_trial_blocker_counts: Counter[str] = Counter()
        exploratory_trial_blocker_counts: Counter[str] = Counter()
        available_trial_slots = max(max_trial_candidates - final_trial_candidates, 0)
        available_exploratory_trial_slots = max(exploratory_max_candidates - final_exploratory_trial_candidates, 0)
        available_promotion_ready_slots = max(max_promotion_ready_candidates - final_promotion_ready_candidates, 0)
        for row in rows:
            pid = row['proposal_id']
            shadow_rank = shadow_rank_map.get(pid)
            within_shadow_budget = bool(shadow_rank is not None and shadow_rank <= shadow_budget)
            trial_state = trial_state_by_proposal[pid]
            promotion_state = promotion_state_by_proposal[pid]
            standard_trial_blocker_counts.update(trial_state.get('standard_trial_blockers') or [])
            exploratory_trial_blocker_counts.update([
                blocker
                for blocker in (trial_state.get('exploratory_trial_blockers') or [])
                if blocker != 'exploratory_trial_disabled'
            ])
            if promotion_state['eligible']:
                prospective_stage = 'promotion_ready'
            elif trial_state['eligible']:
                prospective_stage = 'trial_candidate'
            else:
                prospective_stage = base_lifecycle_stage_for_record(row)
            stage_counts[prospective_stage] += 1

            row['family_policy'] = dict(policy)
            row['family_shadow_rank'] = shadow_rank
            row['family_trial_rank'] = trial_state['trial_rank']
            row['family_promotion_ready_rank'] = promotion_state['promotion_rank']
            row['within_family_shadow_budget'] = within_shadow_budget
            row['within_family_trial_budget'] = trial_state['within_trial_budget']
            row['within_family_promotion_ready_budget'] = promotion_state['within_promotion_budget']
            row['trial_readiness'] = {
                'eligible': trial_state['eligible'],
                'eligibility_mode': trial_state.get('eligibility_mode') or 'blocked',
                'blockers': trial_state['trial_blockers'],
                'standard_blockers': trial_state.get('standard_trial_blockers') or [],
                'exploratory_blockers': trial_state.get('exploratory_trial_blockers') or [],
                'blocker_details': trial_gate_details_by_proposal.get(pid) or {},
                'available_trial_slots': available_trial_slots,
                'available_exploratory_trial_slots': available_exploratory_trial_slots,
                'existing_trial_candidates': final_trial_candidates,
                'existing_exploratory_trial_candidates': final_exploratory_trial_candidates,
                'family_trial_rank': trial_state['trial_rank'],
                'family_shadow_rank': shadow_rank,
                'family_exploratory_trial_rank': trial_state.get('exploratory_rank'),
                'within_exploratory_trial_budget': trial_state.get('within_exploratory_budget'),
                'exploratory_trial_policy': dict(exploratory_trial),
                'shadow_trial_score': row.get('shadow_trial_score'),
                'shadow_label_balance': row.get('shadow_label_balance'),
                'prospective_stage': 'trial_candidate' if trial_state['eligible'] else prospective_stage,
            }
            row['promotion_readiness'] = {
                'eligible': promotion_state['eligible'],
                'blockers': promotion_state['promotion_blockers'],
                'available_promotion_ready_slots': available_promotion_ready_slots,
                'existing_promotion_ready_candidates': final_promotion_ready_candidates,
                'family_promotion_ready_rank': promotion_state['promotion_rank'],
                'trial_shrunken_utility': row.get('trial_shrunken_utility'),
                'trial_harmful_rate': row.get('trial_harmful_rate'),
                'trial_label_balance': row.get('trial_label_balance'),
                'open_violation_count': promotion_state['open_violation_count'],
                'prospective_stage': prospective_stage,
            }
            row['stats_metadata']['family_policy'] = {
                'mechanism_family': family,
                'max_shadow_candidates': int(policy.get('max_shadow_candidates') or 0),
                'max_trial_candidates': max_trial_candidates,
                'max_promotion_ready_candidates': max_promotion_ready_candidates,
                'max_active_nodes': int(policy.get('max_active_nodes') or 0),
                'max_active_edges': int(policy.get('max_active_edges') or 0),
                'enabled': bool(policy.get('enabled', True)),
            }
            row['stats_metadata']['shadow_trial_metrics'] = {
                'trial_score': row.get('shadow_trial_score'),
                'label_balance': row.get('shadow_label_balance'),
                'prior_sample_size': SHADOW_TRIAL_PRIOR_SAMPLE_SIZE,
            }
            row['stats_metadata']['trial_metrics'] = {
                'exposure_count': int(row.get('trial_exposure_count') or 0),
                'preview_count': int(row.get('trial_preview_count') or 0),
                'helpful_count': int(row.get('trial_helpful_count') or 0),
                'neutral_count': int(row.get('trial_neutral_count') or 0),
                'harmful_count': int(row.get('trial_harmful_count') or 0),
                'unclear_count': int(row.get('trial_unclear_count') or 0),
                'judged_count': int(row.get('trial_judged_count') or 0),
                'score_sum': float(row.get('trial_score_sum') or 0.0),
                'mean_score': row.get('trial_mean_score'),
                'shrunken_utility': row.get('trial_shrunken_utility'),
                'label_balance': row.get('trial_label_balance'),
                'harmful_rate': row.get('trial_harmful_rate'),
                'prior_sample_size': TRIAL_UTILITY_PRIOR_SAMPLE_SIZE,
            }
            row['stats_metadata']['family_trial_readiness'] = row['trial_readiness']
            row['stats_metadata']['family_promotion_readiness'] = row['promotion_readiness']

        family_summary[family] = {
            'policy': dict(policy),
            'proposal_counts': {
                'total': len(rows),
                'shadow_candidates': len(shadow_rows),
                'trial_candidates': final_trial_candidates + final_exploratory_trial_candidates,
                'standard_trial_candidates': final_trial_candidates,
                'exploratory_trial_candidates': final_exploratory_trial_candidates,
                'promotion_ready_candidates': final_promotion_ready_candidates,
                'by_stage': dict(sorted(stage_counts.items())),
            },
            'live_state': live_state,
            'available_trial_slots': available_trial_slots,
            'available_exploratory_trial_slots': available_exploratory_trial_slots,
            'available_promotion_ready_slots': available_promotion_ready_slots,
            'shadow_budget': shadow_budget,
            'trial_gate_blocker_counts': dict(sorted(standard_trial_blocker_counts.items())),
            'exploratory_trial_gate_blocker_counts': dict(sorted(exploratory_trial_blocker_counts.items())),
            'exploratory_trial_policy': dict(exploratory_trial),
        }

    return family_summary


def promotion_for_record(record: dict[str, Any]) -> tuple[str, str]:
    threshold = record['threshold_profile']
    cases = record['distinct_case_count']
    supports = record['non_intervention_support_case_count']
    contests = record['contest_case_count']
    genericity = record['genericity_penalty']
    if record['duplicate_of_live_graph']:
        return 'duplicate_of_live_graph', 'proposal_key_already_exists_in_live_graph'
    if record['candidate_type'] == 'node':
        if cases >= threshold.get('draft_min_cases', 999) and supports >= threshold.get('draft_min_support_cases', 999) and genericity <= threshold.get('max_genericity_for_draft', 0.25):
            return 'draft_recommendation', 'meets_node_draft_threshold_with_non_intervention_support'
        if cases >= threshold.get('proposed_min_cases', 999) and supports >= 1 and genericity <= threshold.get('max_genericity_for_proposed', 0.35):
            return 'proposed', 'meets_node_proposed_threshold_with_non_intervention_support'
        return 'insufficient_support', 'below_node_threshold_after_support_filter'
    ratio = (supports / max(contests, 1)) if contests else float('inf')
    if cases >= threshold.get('draft_min_cases', 999) and supports >= threshold.get('draft_min_support_cases', 999) and ratio >= threshold.get('min_support_to_contest_ratio', 2.0) and genericity <= threshold.get('max_genericity_for_draft', 0.25):
        return 'draft_recommendation', 'meets_edge_draft_threshold_with_non_intervention_support'
    if cases >= threshold.get('proposed_min_cases', 999) and supports >= 1 and genericity <= threshold.get('max_genericity_for_proposed', 0.35):
        return 'proposed', 'meets_edge_proposed_threshold_with_non_intervention_support'
    return 'insufficient_support', 'below_edge_threshold_after_support_filter'



def lifecycle_stage_for_record(record: dict[str, Any]) -> str:
    promotion_readiness = record.get('promotion_readiness') or {}
    if bool(promotion_readiness.get('eligible')):
        return 'promotion_ready'
    trial_readiness = record.get('trial_readiness') or {}
    if bool(trial_readiness.get('eligible')):
        return 'trial_candidate'
    return base_lifecycle_stage_for_record(record)



def promotion_blockers_for_record(record: dict[str, Any]) -> list[str]:
    threshold = record['threshold_profile'] or {}
    blockers: list[str] = []
    cases = int(record.get('distinct_case_count') or 0)
    supports = int(record.get('non_intervention_support_case_count') or 0)
    contests = int(record.get('contest_case_count') or 0)
    genericity = float(record.get('genericity_penalty') or 0.0)

    if record.get('duplicate_of_live_graph'):
        blockers.append('duplicate_of_live_graph')
        return blockers
    if str(record.get('mechanism_family') or 'unassigned') == 'unassigned':
        blockers.append('unassigned_mechanism_family')
    if record.get('merge_recommended'):
        blockers.append('merge_recommended')
    if int(record.get('non_intervention_support_case_count') or 0) <= 0:
        blockers.append('no_non_intervention_support')
    if int(record.get('heuristic_only_support_case_count') or 0) >= int(record.get('support_case_count') or 0) and int(record.get('support_case_count') or 0) > 0:
        blockers.append('heuristic_only_support')
    if int(record.get('intervention_only_support_case_count') or 0) >= int(record.get('support_case_count') or 0) and int(record.get('support_case_count') or 0) > 0:
        blockers.append('intervention_only_support')
    if int(record.get('draft_intervention_support_case_count') or 0) > 0 and supports <= 0:
        blockers.append('draft_intervention_dependent')

    proposed_min_cases = int(threshold.get('proposed_min_cases', 0) or 0)
    if proposed_min_cases and cases < proposed_min_cases:
        blockers.append('below_proposed_min_cases')

    max_genericity_for_proposed = float(threshold.get('max_genericity_for_proposed', 999) or 999)
    if genericity > max_genericity_for_proposed:
        blockers.append('genericity_above_proposed_limit')

    if record.get('candidate_type') == 'node':
        draft_min_cases = int(threshold.get('draft_min_cases', 0) or 0)
        draft_min_support_cases = int(threshold.get('draft_min_support_cases', 0) or 0)
        max_genericity_for_draft = float(threshold.get('max_genericity_for_draft', 999) or 999)
        if cases < draft_min_cases:
            blockers.append('below_draft_min_cases')
        if supports < draft_min_support_cases:
            blockers.append('below_draft_non_intervention_support_cases')
        if genericity > max_genericity_for_draft:
            blockers.append('genericity_above_draft_limit')
        return sorted(dict.fromkeys(blockers))

    proposed_min_support_cases = 1
    if proposed_min_support_cases and supports < proposed_min_support_cases:
        blockers.append('below_proposed_non_intervention_support_cases')

    draft_min_cases = int(threshold.get('draft_min_cases', 0) or 0)
    draft_min_support_cases = int(threshold.get('draft_min_support_cases', 0) or 0)
    min_ratio = float(threshold.get('min_support_to_contest_ratio', 0) or 0)
    ratio = (supports / max(contests, 1)) if contests else float('inf')
    max_genericity_for_draft = float(threshold.get('max_genericity_for_draft', 999) or 999)
    if cases < draft_min_cases:
        blockers.append('below_draft_min_cases')
    if supports < draft_min_support_cases:
        blockers.append('below_draft_non_intervention_support_cases')
    if ratio < min_ratio:
        blockers.append('support_to_contest_ratio_too_low')
    if genericity > max_genericity_for_draft:
        blockers.append('genericity_above_draft_limit')
    return sorted(dict.fromkeys(blockers))



def promotion_score(record: dict[str, Any]) -> float:
    cases = record['distinct_case_count']
    non_intervention_supports = record['non_intervention_support_case_count']
    contests = record['contest_case_count']
    duplicate_penalty = 1.5 if record['duplicate_of_live_graph'] else 0.0
    merge_penalty = 1.0 if record.get('merge_recommended') else 0.0
    heuristic_penalty = 0.35 * int(record.get('heuristic_only_support_case_count') or 0)
    intervention_only_penalty = 0.45 * int(record.get('intervention_only_support_case_count') or 0)
    context_bonus = 0.08 * (
        int(record.get('distinct_platform_count') or 0)
        + int(record.get('distinct_category_count') or 0)
        + int(record.get('distinct_question_mechanics_count') or 0)
        + int(record.get('distinct_source_of_truth_class_count') or 0)
        + int(record.get('distinct_domain_count') or 0)
    )
    score = (
        math.log1p(cases) * 0.55
        + non_intervention_supports * 0.55
        - contests * 0.45
        - float(record['genericity_penalty'])
        - duplicate_penalty
        - merge_penalty
        - heuristic_penalty
        - intervention_only_penalty
        + context_bonus
    )
    return round(score, 6)



def build_markdown(summary: dict[str, Any]) -> str:
    lines = [
        '# Proposed causal candidates',
        '',
        f"- occurrence_count: {summary['occurrence_count']}",
        f"- proposal_count: {summary['proposal_count']}",
        '',
    ]
    family_summaries = summary.get('family_summaries') or {}
    if family_summaries:
        lines.append('## Family policy summary')
        lines.append('')
        for family in sorted(family_summaries):
            row = family_summaries[family]
            policy = row.get('policy') or {}
            proposal_counts = row.get('proposal_counts') or {}
            live_state = row.get('live_state') or {}
            lines.append(f"### `{family}`")
            exploratory_policy = row.get('exploratory_trial_policy') or {}
            lines.append(
                f"- enabled: `{policy.get('enabled')}` | shadow_budget: `{policy.get('max_shadow_candidates')}` | "
                f"trial_budget: `{policy.get('max_trial_candidates')}` | available_trial_slots: `{row.get('available_trial_slots')}` | "
                f"exploratory_trial_enabled: `{exploratory_policy.get('enabled')}` | exploratory_trial_budget: `{exploratory_policy.get('max_candidates')}` | available_exploratory_trial_slots: `{row.get('available_exploratory_trial_slots')}` | "
                f"promotion_ready_budget: `{policy.get('max_promotion_ready_candidates')}` | available_promotion_ready_slots: `{row.get('available_promotion_ready_slots')}`"
            )
            lines.append(
                f"- proposals: total `{proposal_counts.get('total', 0)}` | shadow `{proposal_counts.get('shadow_candidates', 0)}` | "
                f"trial `{proposal_counts.get('trial_candidates', 0)}` (standard `{proposal_counts.get('standard_trial_candidates', 0)}` / exploratory `{proposal_counts.get('exploratory_trial_candidates', 0)}`) | promotion_ready `{proposal_counts.get('promotion_ready_candidates', 0)}`"
            )
            lines.append(
                f"- live_nodes: total `{((live_state.get('live_nodes') or {}).get('total') or 0)}` | "
                f"live_edges: total `{((live_state.get('live_edges') or {}).get('total') or 0)}`"
            )
            trial_gate_blocker_counts = row.get('trial_gate_blocker_counts') or {}
            if trial_gate_blocker_counts:
                lines.append(f"- trial_gate_blocker_counts: `{json.dumps(trial_gate_blocker_counts, sort_keys=True)}`")
            exploratory_gate_blocker_counts = row.get('exploratory_trial_gate_blocker_counts') or {}
            if exploratory_gate_blocker_counts:
                lines.append(f"- exploratory_trial_gate_blocker_counts: `{json.dumps(exploratory_gate_blocker_counts, sort_keys=True)}`")
            lines.append('')
    for candidate_type in ['node', 'edge']:
        rows = [row for row in summary['proposals'] if row['candidate_type'] == candidate_type]
        lines.append(f"## {candidate_type.title()} proposals")
        lines.append('')
        if not rows:
            lines.append('- None')
            lines.append('')
            continue
        for row in rows:
            lines.append(f"### `{row['proposal_key']}`")
            lines.append(f"- status: `{row['promotion_status']}` | lifecycle_stage: `{row['lifecycle_stage']}` | family: `{row.get('mechanism_family')}`")
            lines.append(f"- score: `{row['promotion_score']}` | dominant_source: `{row.get('dominant_proposal_source') or ''}`")
            lines.append(f"- cases: `{row['distinct_case_count']}` | non_intervention_supports: `{row['non_intervention_support_case_count']}` | contests: `{row['contest_case_count']}`")
            lines.append(f"- intervention_only_supports: `{row['intervention_only_support_case_count']}` | heuristic_only_supports: `{row['heuristic_only_support_case_count']}`")
            if row.get('source_node_key') or row.get('target_node_key'):
                lines.append(f"- edge: `{row.get('source_node_key') or ''}` -> `{row.get('target_node_key') or ''}`")
            if row.get('merge_recommended'):
                lines.append(f"- merge_candidate_key: `{row.get('merge_candidate_key') or ''}` | max_duplicate_similarity: `{row.get('max_duplicate_similarity')}`")
            lines.append(f"- reason: {row['promotion_reason']}")
            lines.append(f"- first_seen_at: `{row.get('first_seen_at') or ''}` | last_seen_at: `{row.get('last_seen_at') or ''}`")
            lines.append(
                f"- shadow: `{row.get('shadow_match_count', 0)}` matches | "
                f"helpful `{row.get('shadow_helpful_count', row.get('shadow_positive_count', 0))}` | "
                f"neutral `{row.get('shadow_neutral_count', 0)}` | "
                f"harmful `{row.get('shadow_harmful_count', 0)}` | "
                f"unclear `{row.get('shadow_unclear_count', 0)}`"
            )
            lines.append(
                f"- trial: exposures `{row.get('trial_exposure_count', 0)}` | helpful `{row.get('trial_helpful_count', 0)}` | "
                f"neutral `{row.get('trial_neutral_count', 0)}` | harmful `{row.get('trial_harmful_count', 0)}` | "
                f"unclear `{row.get('trial_unclear_count', 0)}`"
            )
            lines.append(
                f"- family_trial_rank: `{row.get('family_trial_rank')}` | within_family_trial_budget: `{row.get('within_family_trial_budget')}` | "
                f"trial_eligible: `{((row.get('trial_readiness') or {}).get('eligible'))}` | trial_eligibility_mode: `{((row.get('trial_readiness') or {}).get('eligibility_mode'))}` | exploratory_trial_rank: `{((row.get('trial_readiness') or {}).get('family_exploratory_trial_rank'))}`"
            )
            lines.append(
                f"- family_promotion_ready_rank: `{row.get('family_promotion_ready_rank')}` | within_family_promotion_ready_budget: `{row.get('within_family_promotion_ready_budget')}` | "
                f"promotion_ready_eligible: `{((row.get('promotion_readiness') or {}).get('eligible'))}`"
            )
            lines.append(
                f"- shadow_trial_score: `{row.get('shadow_trial_score')}` | shadow_label_balance: `{row.get('shadow_label_balance')}` | "
                f"trial_shrunken_utility: `{row.get('trial_shrunken_utility')}` | trial_label_balance: `{row.get('trial_label_balance')}` | "
                f"trial_harmful_rate: `{row.get('trial_harmful_rate')}`"
            )
            lines.append(f"- supporting_case_keys: {', '.join(row['supporting_case_keys']) if row['supporting_case_keys'] else '[]'}")
            if row.get('promotion_blockers'):
                lines.append(f"- blockers: {', '.join(row['promotion_blockers'])}")
            trial_blockers = (row.get('trial_readiness') or {}).get('blockers') or []
            if trial_blockers:
                lines.append(f"- trial_blockers: {', '.join(trial_blockers)}")
            standard_trial_blockers = (row.get('trial_readiness') or {}).get('standard_blockers') or []
            if standard_trial_blockers and standard_trial_blockers != trial_blockers:
                lines.append(f"- standard_trial_blockers: {', '.join(standard_trial_blockers)}")
            exploratory_trial_blockers = (row.get('trial_readiness') or {}).get('exploratory_blockers') or []
            if exploratory_trial_blockers:
                lines.append(f"- exploratory_trial_blockers: {', '.join(exploratory_trial_blockers)}")
            blocker_details = (row.get('trial_readiness') or {}).get('blocker_details') or {}
            if blocker_details:
                lines.append(f"- trial_gate_details: `{json.dumps(blocker_details, sort_keys=True)}`")
            promotion_blockers = (row.get('promotion_readiness') or {}).get('blockers') or []
            if promotion_blockers:
                lines.append(f"- promotion_ready_blockers: {', '.join(promotion_blockers)}")
            lines.append('')
    return '\n'.join(lines) + '\n'



def main() -> int:
    args = parse_args()
    resolved_db_url = resolve_db_url(args.db_url)
    configured_family_policies = load_family_policies()
    table_present = table_exists('proposed_causal_candidate_stats', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    occurrences_present = table_exists('proposed_causal_candidate_occurrences', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    shadow_present = table_exists('proposed_causal_shadow_matches', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    trial_exposure_present = table_exists('proposed_causal_trial_exposures', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    family_policy_table_present = table_exists('causal_family_policies', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    stats_schema_missing: list[str] = []
    occurrences_schema_missing: list[str] = []
    shadow_schema_missing: list[str] = []
    trial_exposure_schema_missing: list[str] = []
    family_policy_schema_missing: list[str] = []
    if resolved_db_url and table_present:
        stats_schema_missing = missing_columns('proposed_causal_candidate_stats', REQUIRED_STATS_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql)
        if stats_schema_missing:
            table_present = False
    if resolved_db_url and occurrences_present:
        occurrences_schema_missing = missing_columns('proposed_causal_candidate_occurrences', REQUIRED_OCCURRENCE_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql)
        if occurrences_schema_missing:
            occurrences_present = False
    if resolved_db_url and shadow_present:
        shadow_schema_missing = missing_columns('proposed_causal_shadow_matches', REQUIRED_SHADOW_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql)
    if resolved_db_url and trial_exposure_present:
        trial_exposure_schema_missing = missing_columns('proposed_causal_trial_exposures', REQUIRED_TRIAL_EXPOSURE_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql)
    if resolved_db_url and family_policy_table_present:
        family_policy_schema_missing = missing_columns('causal_family_policies', REQUIRED_FAMILY_POLICY_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql)

    node_labels, edge_labels = load_live_graph()
    live_family_state = load_live_family_state()
    occurrences = exec_sql(args.psql, resolved_db_url, OCCURRENCES_SQL, {}) if resolved_db_url and occurrences_present else []
    if not isinstance(occurrences, list):
        occurrences = []

    shadow_sql = SHADOW_COUNTS_SQL if shadow_present and not shadow_schema_missing else LEGACY_SHADOW_COUNTS_SQL
    shadow_rows = exec_sql(args.psql, resolved_db_url, shadow_sql, {}) if resolved_db_url and shadow_present else []
    if not isinstance(shadow_rows, list):
        shadow_rows = []
    shadow_by_proposal = {str(row.get('proposal_id') or ''): row for row in shadow_rows if str(row.get('proposal_id') or '').strip()}

    trial_sql = TRIAL_COUNTS_SQL if trial_exposure_present and not trial_exposure_schema_missing else LEGACY_TRIAL_COUNTS_SQL
    trial_rows = exec_sql(args.psql, resolved_db_url, trial_sql, {}) if resolved_db_url and trial_exposure_present else []
    if not isinstance(trial_rows, list):
        trial_rows = []
    trial_by_proposal = {str(row.get('proposal_id') or ''): row for row in trial_rows if str(row.get('proposal_id') or '').strip()}

    family_policy_rows = dict(configured_family_policies)
    if resolved_db_url and family_policy_table_present and not family_policy_schema_missing:
        db_family_policies = exec_sql(args.psql, resolved_db_url, FAMILY_POLICIES_SQL, {})
        if isinstance(db_family_policies, list):
            for row in db_family_policies:
                if not isinstance(row, dict):
                    continue
                family = str(row.get('mechanism_family') or '').strip()
                if not family:
                    continue
                family_policy_rows[family] = family_policy_for(family, loaded={family: row})

    open_health_violations_by_key: dict[str, int] = {}
    health_present = table_exists('causal_graph_health_violations', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    if resolved_db_url and health_present:
        health_rows = exec_sql(args.psql, resolved_db_url, OPEN_HEALTH_VIOLATIONS_SQL, {})
        if isinstance(health_rows, list):
            open_health_violations_by_key = {
                str(row.get('entity_key') or ''): int(row.get('open_violation_count') or 0)
                for row in health_rows
                if isinstance(row, dict) and str(row.get('entity_key') or '').strip()
            }

    grouped: dict[str, list[dict[str, Any]]] = {}
    by_type_keys: dict[str, list[str]] = {'node': [], 'edge': []}
    for row in occurrences:
        pid = str(row.get('proposal_id') or '')
        if not pid:
            continue
        grouped.setdefault(pid, []).append(row)
        ctype = str(row.get('candidate_type') or '')
        pkey = str(row.get('proposal_key') or '')
        if ctype in by_type_keys and pkey and pkey not in by_type_keys[ctype]:
            by_type_keys[ctype].append(pkey)

    proposals: list[dict[str, Any]] = []
    persisted_count = 0
    if resolved_db_url and table_present and occurrences_present and not args.dry_run:
        exec_sql(args.psql, resolved_db_url, DELETE_STALE_SQL, {})

    for pid, rows in sorted(grouped.items()):
        first = rows[0]
        candidate_type = str(first.get('candidate_type') or '')
        proposal_key = str(first.get('proposal_key') or '')
        supporting_case_keys = sorted({str(row.get('case_key') or '') for row in rows if row.get('support_direction') == 'supports' and row.get('case_key')})
        contest_case_keys = sorted({str(row.get('case_key') or '') for row in rows if row.get('support_direction') in {'contests', 'weakens'} and row.get('case_key')})
        live_labels = node_labels if candidate_type == 'node' else edge_labels
        duplicate = proposal_key in live_labels
        near_duplicate_keys, near_live_graph_keys, max_duplicate_similarity, merge_candidate_key, merge_recommended = collect_nearby_keys(
            proposal_key=proposal_key,
            candidate_label=str(first.get('candidate_label') or ''),
            proposal_keys=by_type_keys.get(candidate_type, []),
            live_keys=sorted(live_labels.keys()),
            live_labels=live_labels,
        )
        shadow = shadow_by_proposal.get(pid) or {}
        trial = trial_by_proposal.get(pid) or {}
        support_breakdown = support_case_breakdown(rows)
        ctx_distribution = context_distribution(rows)
        ctx_breadth = context_breadth_counts(rows)
        record = {
            'proposal_id': pid,
            'proposal_key': proposal_key,
            'candidate_type': candidate_type,
            'candidate_label': str(first.get('candidate_label') or ''),
            'mechanism_family': str(first.get('mechanism_family') or 'unassigned'),
            'normalized_cluster_key': str(first.get('normalized_cluster_key') or ''),
            'source_node_key': str(first.get('source_node_key') or ''),
            'target_node_key': str(first.get('target_node_key') or ''),
            'node_type': str(first.get('node_type') or ''),
            'effect_sign': str(first.get('effect_sign') or ''),
            'occurrence_count': len(rows),
            'distinct_case_count': len({str(row.get('case_key') or '') for row in rows if row.get('case_key')}),
            'support_case_count': len(supporting_case_keys),
            'contest_case_count': len(contest_case_keys),
            'duplicate_of_live_graph': duplicate,
            'genericity_penalty': round(mean([float(row.get('genericity_penalty') or 0.0) for row in rows]), 4),
            'supporting_case_keys': supporting_case_keys,
            'threshold_profile': first.get('threshold_profile') or {},
            'first_seen_at': min_timestamp(rows, 'created_at', 'updated_at'),
            'last_seen_at': max_timestamp(rows, 'updated_at', 'created_at'),
            'proposal_source_mix': proposal_source_mix(rows),
            'dominant_proposal_source': dominant_proposal_source(rows),
            'evidence_channel_counts': evidence_channel_counts(rows),
            'shadow_match_count': int(shadow.get('shadow_match_count') or 0),
            'shadow_positive_count': int(shadow.get('shadow_positive_count') or 0),
            'shadow_helpful_count': int(shadow.get('shadow_helpful_count') or 0),
            'shadow_neutral_count': int(shadow.get('shadow_neutral_count') or 0),
            'shadow_harmful_count': int(shadow.get('shadow_harmful_count') or 0),
            'shadow_unclear_count': int(shadow.get('shadow_unclear_count') or 0),
            'shadow_judged_count': int(shadow.get('shadow_judged_count') or 0),
            'shadow_score_sum': float(shadow.get('shadow_score_sum') or 0.0),
            'shadow_mean_score': None if shadow.get('shadow_mean_score') in (None, '') else float(shadow.get('shadow_mean_score') or 0.0),
            'trial_exposure_count': int(trial.get('trial_exposure_count') or 0),
            'trial_preview_count': int(trial.get('trial_preview_count') or 0),
            'trial_helpful_count': int(trial.get('trial_helpful_count') or 0),
            'trial_neutral_count': int(trial.get('trial_neutral_count') or 0),
            'trial_harmful_count': int(trial.get('trial_harmful_count') or 0),
            'trial_unclear_count': int(trial.get('trial_unclear_count') or 0),
            'trial_judged_count': int(trial.get('trial_judged_count') or 0),
            'trial_score_sum': float(trial.get('trial_score_sum') or 0.0),
            'trial_mean_score': None if trial.get('trial_mean_score') in (None, '') else float(trial.get('trial_mean_score') or 0.0),
            'near_duplicate_keys': near_duplicate_keys,
            'near_live_graph_keys': near_live_graph_keys,
            'max_duplicate_similarity': max_duplicate_similarity,
            'merge_candidate_key': merge_candidate_key,
            'merge_recommended': merge_recommended,
            'context_distribution': ctx_distribution,
            'stats_metadata': {
                'supporting_case_keys': supporting_case_keys,
                'contested_case_keys': contest_case_keys,
                'occurrence_reasons': sorted({str(row.get('occurrence_reason') or '') for row in rows if row.get('occurrence_reason')}),
                'latest_projection_paths': sorted({str(row.get('projection_path') or '') for row in rows if row.get('projection_path')}),
                'intervention_dependency_counts': intervention_dependency_counts(rows),
                'observed_active_nodes': sorted({str(item).strip() for row in rows for item in ((row.get('trigger_snapshot') or {}).get('active_nodes') or []) if str(item).strip()}),
                'observed_candidate_edges': sorted({str(item).strip() for row in rows for item in ((row.get('trigger_snapshot') or {}).get('candidate_edges') or []) if str(item).strip()}),
                'observed_contested_edges': sorted({str(item).strip() for row in rows for item in ((row.get('trigger_snapshot') or {}).get('contested_edges') or []) if str(item).strip()}),
                'observed_required_checks': sorted({str(item).strip() for row in rows for item in ((row.get('trigger_snapshot') or {}).get('required_checks') or []) if str(item).strip()}),
                'observed_source_sections': sorted({str(item).strip() for row in rows for item in ((row.get('trigger_snapshot') or {}).get('source_sections') or []) if str(item).strip()}),
                'shadow_outcome_counts': {
                    'helpful': int(shadow.get('shadow_helpful_count') or 0),
                    'neutral': int(shadow.get('shadow_neutral_count') or 0),
                    'harmful': int(shadow.get('shadow_harmful_count') or 0),
                    'unclear': int(shadow.get('shadow_unclear_count') or 0),
                    'judged': int(shadow.get('shadow_judged_count') or 0),
                },
                'shadow_score_sum': float(shadow.get('shadow_score_sum') or 0.0),
                'shadow_mean_score': None if shadow.get('shadow_mean_score') in (None, '') else float(shadow.get('shadow_mean_score') or 0.0),
            },
        }
        record.update(support_breakdown)
        record.update(ctx_breadth)
        record['trial_shrunken_utility'] = trial_shrunken_utility(record)
        record['trial_label_balance'] = trial_label_balance(record)
        record['promotion_score'] = promotion_score(record)
        record['promotion_status'], record['promotion_reason'] = promotion_for_record(record)
        record['lifecycle_stage'] = base_lifecycle_stage_for_record(record)
        record['promotion_blockers'] = promotion_blockers_for_record(record)
        record['stage_entered_at'] = record['last_seen_at'] or record['first_seen_at']
        proposals.append({**record, 'db_result': None})

    family_summaries = attach_family_policy_state(
        proposals,
        family_policy_rows=family_policy_rows,
        live_family_state=live_family_state,
        open_health_violations_by_key=open_health_violations_by_key,
    )

    for record in proposals:
        record['lifecycle_stage'] = lifecycle_stage_for_record(record)
        record['stats_metadata']['advancement'] = {
            'lifecycle_stage': record['lifecycle_stage'],
            'trial_readiness': record.get('trial_readiness') or {},
            'promotion_readiness': record.get('promotion_readiness') or {},
            'shadow_trial_score': record.get('shadow_trial_score'),
            'shadow_label_balance': record.get('shadow_label_balance'),
            'trial_shrunken_utility': record.get('trial_shrunken_utility'),
            'trial_label_balance': record.get('trial_label_balance'),
            'trial_harmful_rate': record.get('trial_harmful_rate'),
        }
        if resolved_db_url and table_present and not args.dry_run:
            record['db_result'] = exec_sql(
                args.psql,
                resolved_db_url,
                UPSERT_SQL,
                {
                    'proposal_id': record['proposal_id'],
                    'proposal_key': record['proposal_key'],
                    'candidate_type': record['candidate_type'],
                    'candidate_label': record['candidate_label'],
                    'mechanism_family': record['mechanism_family'],
                    'normalized_cluster_key': record.get('normalized_cluster_key') or '',
                    'source_node_key': record['source_node_key'],
                    'target_node_key': record['target_node_key'],
                    'node_type': record['node_type'],
                    'effect_sign': record['effect_sign'],
                    'occurrence_count': str(record['occurrence_count']),
                    'distinct_case_count': str(record['distinct_case_count']),
                    'support_case_count': str(record['support_case_count']),
                    'contest_case_count': str(record['contest_case_count']),
                    'non_intervention_support_case_count': str(record['non_intervention_support_case_count']),
                    'intervention_only_support_case_count': str(record['intervention_only_support_case_count']),
                    'draft_intervention_support_case_count': str(record['draft_intervention_support_case_count']),
                    'active_intervention_support_case_count': str(record['active_intervention_support_case_count']),
                    'heuristic_only_support_case_count': str(record['heuristic_only_support_case_count']),
                    'review_text_support_case_count': str(record['review_text_support_case_count']),
                    'signal_packet_support_case_count': str(record['signal_packet_support_case_count']),
                    'frontmatter_support_case_count': str(record['frontmatter_support_case_count']),
                    'duplicate_of_live_graph': 'true' if record['duplicate_of_live_graph'] else 'false',
                    'genericity_penalty': str(record['genericity_penalty']),
                    'promotion_score': str(record['promotion_score']),
                    'promotion_status': record['promotion_status'],
                    'promotion_reason': record['promotion_reason'],
                    'lifecycle_stage': record['lifecycle_stage'],
                    'first_seen_at': record['first_seen_at'],
                    'last_seen_at': record['last_seen_at'],
                    'proposal_source_mix_json': json.dumps(record['proposal_source_mix']),
                    'dominant_proposal_source': record.get('dominant_proposal_source') or '',
                    'evidence_channel_counts_json': json.dumps(record['evidence_channel_counts']),
                    'shadow_match_count': str(record['shadow_match_count']),
                    'shadow_positive_count': str(record['shadow_positive_count']),
                    'stage_entered_at': record['stage_entered_at'],
                    'promotion_blockers_json': json.dumps(record['promotion_blockers']),
                    'near_duplicate_keys_json': json.dumps(record['near_duplicate_keys']),
                    'near_live_graph_keys_json': json.dumps(record['near_live_graph_keys']),
                    'max_duplicate_similarity': '' if record.get('max_duplicate_similarity') in (None, '') else str(record['max_duplicate_similarity']),
                    'merge_candidate_key': record.get('merge_candidate_key') or '',
                    'merge_recommended': 'true' if record.get('merge_recommended') else 'false',
                    'distinct_platform_count': str(record['distinct_platform_count']),
                    'distinct_category_count': str(record['distinct_category_count']),
                    'distinct_question_mechanics_count': str(record['distinct_question_mechanics_count']),
                    'distinct_source_of_truth_class_count': str(record['distinct_source_of_truth_class_count']),
                    'distinct_domain_count': str(record['distinct_domain_count']),
                    'context_distribution_json': json.dumps(record['context_distribution']),
                    'supporting_case_keys_json': json.dumps(record['supporting_case_keys']),
                    'threshold_profile_json': json.dumps(record['threshold_profile']),
                    'stats_metadata_json': json.dumps(record['stats_metadata']),
                },
            )
            persisted_count += 1

    proposals.sort(key=lambda row: (-row['promotion_score'], row['candidate_type'], row['proposal_key']))
    summary = {
        'occurrence_count': len(occurrences),
        'proposal_count': len(proposals),
        'proposal_status_counts': {
            status: sum(1 for row in proposals if row['promotion_status'] == status)
            for status in sorted({row['promotion_status'] for row in proposals})
        },
        'proposal_stage_counts': {
            stage: sum(1 for row in proposals if row['lifecycle_stage'] == stage)
            for stage in sorted({row['lifecycle_stage'] for row in proposals})
        },
        'family_summaries': family_summaries,
        'proposals': proposals,
    }
    generated_write = {'status': 'skipped_missing_schema'}
    if occurrences_present and not occurrences_schema_missing:
        GENERATED_ROOT.mkdir(parents=True, exist_ok=True)
        write_json(SUMMARY_PATH, summary, pretty=True)
        INDEX_PATH.write_text(build_markdown(summary), encoding='utf-8')
        generated_write = {'status': 'written'}

    output: dict[str, Any] = {
        'ok': True,
        'occurrence_count': len(occurrences),
        'proposal_count': len(proposals),
        'persisted_count': persisted_count,
        'table_present': {
            'proposed_causal_candidate_occurrences': occurrences_present,
            'proposed_causal_candidate_stats': table_present,
            'proposed_causal_shadow_matches': shadow_present,
            'proposed_causal_trial_exposures': trial_exposure_present,
            'causal_family_policies': family_policy_table_present,
        },
        'generated_write': generated_write,
        'summary_path': str(SUMMARY_PATH.relative_to(ORCH_ROOT)),
        'index_path': str(INDEX_PATH.relative_to(ORCH_ROOT)),
        'proposals': proposals,
    }
    if not resolved_db_url:
        output['warning'] = 'db_url_unavailable'
    elif occurrences_schema_missing:
        output['warning'] = 'proposed_causal_candidate_occurrences table is missing enriched evidence columns; apply roles/evaluator/sql/033_proposed_causal_candidate_evidence_metadata.sql'
        output['missing_columns'] = {'proposed_causal_candidate_occurrences': occurrences_schema_missing}
    elif stats_schema_missing:
        output['warning'] = 'proposed_causal_candidate_stats table is missing enriched evidence columns; apply roles/evaluator/sql/033_proposed_causal_candidate_evidence_metadata.sql'
        output['missing_columns'] = {'proposed_causal_candidate_stats': stats_schema_missing}
    elif not occurrences_present:
        output['warning'] = 'proposed_causal_candidate_occurrences table missing; apply roles/evaluator/sql/024_proposed_causal_candidate_occurrences.sql and roles/evaluator/sql/033_proposed_causal_candidate_evidence_metadata.sql'
    elif not table_present:
        output['warning'] = 'proposed_causal_candidate_stats table missing; apply roles/evaluator/sql/025_proposed_causal_candidate_stats.sql and roles/evaluator/sql/033_proposed_causal_candidate_evidence_metadata.sql'
    elif shadow_schema_missing:
        output['warning'] = 'proposed_causal_shadow_matches table missing outcome-label columns; apply roles/evaluator/sql/034_proposed_causal_shadow_outcome_labels.sql'
        output['missing_columns'] = {'proposed_causal_shadow_matches': shadow_schema_missing}
    elif trial_exposure_schema_missing:
        output['warning'] = 'proposed_causal_trial_exposures table missing outcome-label columns; apply roles/evaluator/sql/037_proposed_causal_trial_outcome_labels.sql'
        output['missing_columns'] = {'proposed_causal_trial_exposures': trial_exposure_schema_missing}
    elif family_policy_schema_missing:
        output['warning'] = 'causal_family_policies table missing required columns; apply roles/evaluator/sql/035_causal_family_policies.sql'
        output['missing_columns'] = {'causal_family_policies': family_policy_schema_missing}
    elif not family_policy_table_present:
        output['warning'] = 'causal_family_policies table missing; apply roles/evaluator/sql/035_causal_family_policies.sql and seed via roles/evaluator/runtime/scripts/upsert_causal_family_policies.py'
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
