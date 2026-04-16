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

from lib.causal_family_policy import FAMILY_POLICY_PATH, load_family_policy_payload, normalize_family_policy  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, missing_columns, resolve_db_url, table_exists  # noqa: E402
from lib.paths import to_repo_relative  # noqa: E402

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
  updated_at = NOW()
RETURNING json_build_object(
  'mechanism_family', mechanism_family,
  'enabled', enabled,
  'max_shadow_candidates', max_shadow_candidates,
  'max_trial_candidates', max_trial_candidates,
  'max_promotion_ready_candidates', max_promotion_ready_candidates
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Upsert configured causal-family policy rows into Postgres')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def main() -> int:
    args = parse_args()
    payload = load_family_policy_payload()
    policy_rows = [normalize_family_policy(row) for row in payload.get('policies') or []]

    resolved_db_url = resolve_db_url(args.db_url)
    table_present = table_exists('causal_family_policies', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    schema_missing: list[str] = []
    if resolved_db_url and table_present:
        schema_missing = missing_columns('causal_family_policies', REQUIRED_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql)
        if schema_missing:
            table_present = False

    persisted: list[dict[str, Any]] = []
    for row in policy_rows:
        db_result = None
        if resolved_db_url and table_present and not args.dry_run:
            db_result = exec_sql(
                args.psql,
                resolved_db_url,
                UPSERT_SQL,
                {
                    'mechanism_family': row['mechanism_family'],
                    'description': row.get('description') or '',
                    'enabled': 'true' if row.get('enabled', True) else 'false',
                    'max_shadow_candidates': str(row['max_shadow_candidates']),
                    'max_trial_candidates': str(row['max_trial_candidates']),
                    'max_active_nodes': str(row['max_active_nodes']),
                    'max_active_edges': str(row['max_active_edges']),
                    'min_shadow_judged_count_for_trial': str(row['min_shadow_judged_count_for_trial']),
                    'min_shadow_helpful_count_for_trial': str(row['min_shadow_helpful_count_for_trial']),
                    'min_shadow_mean_score_for_trial': str(row['min_shadow_mean_score_for_trial']),
                    'min_non_intervention_support_cases_for_trial': str(row['min_non_intervention_support_cases_for_trial']),
                    'max_genericity_for_trial': str(row['max_genericity_for_trial']),
                    'max_duplicate_similarity_for_trial': str(row['max_duplicate_similarity_for_trial']),
                    'max_promotion_ready_candidates': str(row['max_promotion_ready_candidates']),
                    'min_trial_judged_count_for_promotion': str(row['min_trial_judged_count_for_promotion']),
                    'min_trial_helpful_count_for_promotion': str(row['min_trial_helpful_count_for_promotion']),
                    'min_trial_shrunken_utility_for_promotion': str(row['min_trial_shrunken_utility_for_promotion']),
                    'max_trial_harmful_rate_for_promotion': str(row['max_trial_harmful_rate_for_promotion']),
                    'max_contest_case_count_for_promotion': str(row['max_contest_case_count_for_promotion']),
                    'max_genericity_for_promotion': str(row['max_genericity_for_promotion']),
                    'notes_json': json.dumps(row.get('notes') or {}),
                },
            )
        persisted.append({'mechanism_family': row['mechanism_family'], 'db_result': db_result, 'policy': row})

    output: dict[str, Any] = {
        'ok': True,
        'policy_path': to_repo_relative(FAMILY_POLICY_PATH),
        'policy_count': len(policy_rows),
        'table_present': table_present,
        'rows': persisted,
    }
    if not resolved_db_url:
        output['warning'] = 'db_url_unavailable'
    elif schema_missing:
        output['warning'] = 'causal_family_policies table missing required columns; apply roles/evaluator/sql/035_causal_family_policies.sql'
        output['missing_columns'] = {'causal_family_policies': schema_missing}
    elif not table_present:
        output['warning'] = 'causal_family_policies table missing; apply roles/evaluator/sql/035_causal_family_policies.sql'

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
