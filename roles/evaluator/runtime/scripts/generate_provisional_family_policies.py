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

from lib.causal_family_policy import load_family_policies  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, missing_columns, resolve_db_url, table_exists  # noqa: E402
from lib.provisional_family_autopolicy import (  # noqa: E402
    FAMILY_AUTOPOLICY_REPORT_JSON_PATH,
    FAMILY_AUTOPOLICY_REPORT_MD_PATH,
    POLICY_SOURCE,
    PROVISIONAL_FAMILY_POLICIES_PATH,
    build_generated_provisional_family_policies,
    load_provisional_family_registry_payload,
    write_generated_provisional_family_policy_artifacts,
)

REQUIRED_COLUMNS = [
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
    'policy_source',
    'policy_generated_at',
    'family_state',
    'health_score',
    'evidence_mass',
    'quarantine_until',
    'decay_half_life_days',
    'policy_notes',
]

UPSERT_SQL = r'''
INSERT INTO public.causal_family_policies (
  mechanism_family,
  description,
  enabled,
  max_shadow_candidates,
  max_trial_candidates,
  max_active_nodes,
  max_active_edges,
  min_shadow_judged_count_for_trial,
  min_shadow_helpful_count_for_trial,
  min_shadow_mean_score_for_trial,
  min_non_intervention_support_cases_for_trial,
  max_genericity_for_trial,
  max_duplicate_similarity_for_trial,
  max_promotion_ready_candidates,
  min_trial_judged_count_for_promotion,
  min_trial_helpful_count_for_promotion,
  min_trial_shrunken_utility_for_promotion,
  max_trial_harmful_rate_for_promotion,
  max_contest_case_count_for_promotion,
  max_genericity_for_promotion,
  notes,
  policy_source,
  policy_generated_at,
  family_state,
  health_score,
  evidence_mass,
  quarantine_until,
  decay_half_life_days,
  policy_notes,
  updated_at
)
VALUES (
  :'mechanism_family',
  NULLIF(:'description', ''),
  COALESCE(NULLIF(:'enabled', '')::boolean, true),
  :'max_shadow_candidates'::int,
  :'max_trial_candidates'::int,
  :'max_active_nodes'::int,
  :'max_active_edges'::int,
  :'min_shadow_judged_count_for_trial'::int,
  :'min_shadow_helpful_count_for_trial'::int,
  :'min_shadow_mean_score_for_trial'::numeric,
  :'min_non_intervention_support_cases_for_trial'::int,
  :'max_genericity_for_trial'::numeric,
  :'max_duplicate_similarity_for_trial'::numeric,
  :'max_promotion_ready_candidates'::int,
  :'min_trial_judged_count_for_promotion'::int,
  :'min_trial_helpful_count_for_promotion'::int,
  :'min_trial_shrunken_utility_for_promotion'::numeric,
  :'max_trial_harmful_rate_for_promotion'::numeric,
  :'max_contest_case_count_for_promotion'::int,
  :'max_genericity_for_promotion'::numeric,
  COALESCE(NULLIF(:'notes_json', ''), '{}')::jsonb,
  :'policy_source',
  NULLIF(:'policy_generated_at', '')::timestamptz,
  :'family_state',
  :'health_score'::numeric,
  :'evidence_mass'::numeric,
  NULLIF(:'quarantine_until', '')::timestamptz,
  :'decay_half_life_days'::int,
  COALESCE(NULLIF(:'policy_notes_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (mechanism_family) DO UPDATE SET
  description = EXCLUDED.description,
  enabled = EXCLUDED.enabled,
  max_shadow_candidates = EXCLUDED.max_shadow_candidates,
  max_trial_candidates = EXCLUDED.max_trial_candidates,
  max_active_nodes = EXCLUDED.max_active_nodes,
  max_active_edges = EXCLUDED.max_active_edges,
  min_shadow_judged_count_for_trial = EXCLUDED.min_shadow_judged_count_for_trial,
  min_shadow_helpful_count_for_trial = EXCLUDED.min_shadow_helpful_count_for_trial,
  min_shadow_mean_score_for_trial = EXCLUDED.min_shadow_mean_score_for_trial,
  min_non_intervention_support_cases_for_trial = EXCLUDED.min_non_intervention_support_cases_for_trial,
  max_genericity_for_trial = EXCLUDED.max_genericity_for_trial,
  max_duplicate_similarity_for_trial = EXCLUDED.max_duplicate_similarity_for_trial,
  max_promotion_ready_candidates = EXCLUDED.max_promotion_ready_candidates,
  min_trial_judged_count_for_promotion = EXCLUDED.min_trial_judged_count_for_promotion,
  min_trial_helpful_count_for_promotion = EXCLUDED.min_trial_helpful_count_for_promotion,
  min_trial_shrunken_utility_for_promotion = EXCLUDED.min_trial_shrunken_utility_for_promotion,
  max_trial_harmful_rate_for_promotion = EXCLUDED.max_trial_harmful_rate_for_promotion,
  max_contest_case_count_for_promotion = EXCLUDED.max_contest_case_count_for_promotion,
  max_genericity_for_promotion = EXCLUDED.max_genericity_for_promotion,
  notes = EXCLUDED.notes,
  policy_source = EXCLUDED.policy_source,
  policy_generated_at = EXCLUDED.policy_generated_at,
  family_state = EXCLUDED.family_state,
  health_score = EXCLUDED.health_score,
  evidence_mass = EXCLUDED.evidence_mass,
  quarantine_until = EXCLUDED.quarantine_until,
  decay_half_life_days = EXCLUDED.decay_half_life_days,
  policy_notes = EXCLUDED.policy_notes,
  updated_at = NOW()
RETURNING json_build_object(
  'mechanism_family', mechanism_family,
  'enabled', enabled,
  'max_shadow_candidates', max_shadow_candidates,
  'policy_source', policy_source,
  'family_state', family_state,
  'health_score', health_score
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate and persist shadow-first provisional family autopolicy rows')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def main() -> int:
    args = parse_args()
    registry_payload = load_provisional_family_registry_payload()
    base_policies = load_family_policies()
    payload = build_generated_provisional_family_policies(registry_payload, base_policies=base_policies)
    write_generated_provisional_family_policy_artifacts(payload)

    resolved_db_url = resolve_db_url(args.db_url)
    table_present = table_exists('causal_family_policies', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    schema_missing: list[str] = []
    if resolved_db_url and table_present:
        schema_missing = missing_columns('causal_family_policies', REQUIRED_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql)
        if schema_missing:
            table_present = False

    persisted: list[dict[str, Any]] = []
    if resolved_db_url and table_present and not args.dry_run:
        for row in payload.get('policies') or []:
            if not isinstance(row, dict):
                continue
            persisted.append(
                exec_sql(
                    args.psql,
                    resolved_db_url,
                    UPSERT_SQL,
                    {
                        'mechanism_family': str(row.get('mechanism_family') or ''),
                        'description': str(row.get('description') or ''),
                        'enabled': 'true' if row.get('enabled', True) else 'false',
                        'max_shadow_candidates': str(row.get('max_shadow_candidates') or 0),
                        'max_trial_candidates': str(row.get('max_trial_candidates') or 0),
                        'max_active_nodes': str(row.get('max_active_nodes') or 0),
                        'max_active_edges': str(row.get('max_active_edges') or 0),
                        'min_shadow_judged_count_for_trial': str(row.get('min_shadow_judged_count_for_trial') or 0),
                        'min_shadow_helpful_count_for_trial': str(row.get('min_shadow_helpful_count_for_trial') or 0),
                        'min_shadow_mean_score_for_trial': str(row.get('min_shadow_mean_score_for_trial') or 0),
                        'min_non_intervention_support_cases_for_trial': str(row.get('min_non_intervention_support_cases_for_trial') or 0),
                        'max_genericity_for_trial': str(row.get('max_genericity_for_trial') or 0),
                        'max_duplicate_similarity_for_trial': str(row.get('max_duplicate_similarity_for_trial') or 0),
                        'max_promotion_ready_candidates': str(row.get('max_promotion_ready_candidates') or 0),
                        'min_trial_judged_count_for_promotion': str(row.get('min_trial_judged_count_for_promotion') or 0),
                        'min_trial_helpful_count_for_promotion': str(row.get('min_trial_helpful_count_for_promotion') or 0),
                        'min_trial_shrunken_utility_for_promotion': str(row.get('min_trial_shrunken_utility_for_promotion') or 0),
                        'max_trial_harmful_rate_for_promotion': str(row.get('max_trial_harmful_rate_for_promotion') or 0),
                        'max_contest_case_count_for_promotion': str(row.get('max_contest_case_count_for_promotion') or 0),
                        'max_genericity_for_promotion': str(row.get('max_genericity_for_promotion') or 0),
                        'notes_json': json.dumps(row.get('notes') or {}),
                        'policy_source': str(row.get('policy_source') or POLICY_SOURCE),
                        'policy_generated_at': str(row.get('policy_generated_at') or ''),
                        'family_state': str(row.get('family_state') or 'provisional'),
                        'health_score': str(row.get('health_score') or 0),
                        'evidence_mass': str(row.get('evidence_mass') or 0),
                        'quarantine_until': str(row.get('quarantine_until') or ''),
                        'decay_half_life_days': str(row.get('decay_half_life_days') or 30),
                        'policy_notes_json': json.dumps(row.get('policy_notes') or {}),
                    },
                )
            )

    output: dict[str, Any] = {
        'ok': True,
        'registry_path': str(PROVISIONAL_FAMILY_POLICIES_PATH.parent / 'generated' / 'provisional-family-registry.json'),
        'generated_policy_path': str(PROVISIONAL_FAMILY_POLICIES_PATH),
        'autopolicy_report_json_path': str(FAMILY_AUTOPOLICY_REPORT_JSON_PATH),
        'autopolicy_report_md_path': str(FAMILY_AUTOPOLICY_REPORT_MD_PATH),
        'policy_source': POLICY_SOURCE,
        'policy_count': int(payload.get('policy_count') or 0),
        'enabled_policy_count': int(payload.get('enabled_policy_count') or 0),
        'disabled_policy_count': int(payload.get('disabled_policy_count') or 0),
        'skipped_canonical_seed_count': int(payload.get('skipped_canonical_seed_count') or 0),
        'top_policies': (payload.get('policies') or [])[:15],
        'persisted_policy_count': len(persisted),
    }
    if not registry_payload:
        output['warning'] = 'provisional_family_registry_missing_or_invalid; run roles/evaluator/runtime/scripts/materialize_provisional_causal_families.py first'
    elif not resolved_db_url:
        output['warning'] = 'db_url_unavailable'
    elif schema_missing:
        output['warning'] = 'causal_family_policies missing required autopolicy columns; apply roles/evaluator/sql/044_extend_causal_family_policies_for_autopolicy.sql'
        output['missing_columns'] = {'causal_family_policies': schema_missing}
    elif not table_present:
        output['warning'] = 'causal_family_policies table missing; apply roles/evaluator/sql/035_causal_family_policies.sql'

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0 if output.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
