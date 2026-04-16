#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
ORCHESTRATOR_ROOT = SCRIPT_PATH.parents[4]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.lmd import (  # noqa: E402
    DEFAULT_LMD_EXPERIMENT_ID,
    bundle_candidates,
    bundle_sha256,
    load_bundle,
)
from lib.paths import to_repo_relative  # noqa: E402

CASE_LOOKUP_SQL = r'''
SELECT json_build_object(
  'case_id', id,
  'case_key', case_key
)::text
FROM public.cases
WHERE case_key = :'case_key'
LIMIT 1;
'''

ASSIGNMENT_LOOKUP_SQL = r'''
SELECT json_build_object(
  'experiment_id', experiment_id,
  'arm', arm,
  'generator_version', generator_version,
  'policy_version', policy_version
)::text
FROM public.lmd_experiment_assignments
WHERE case_key = :'case_key'
  AND (NULLIF(:'experiment_id', '') IS NULL OR experiment_id = NULLIF(:'experiment_id', ''))
ORDER BY updated_at DESC NULLS LAST, created_at DESC NULLS LAST, id DESC
LIMIT 1;
'''

INSERT_SQL = r'''
INSERT INTO public.lmd_bundle_exposures (
  case_id,
  case_key,
  dispatch_id,
  research_run_id,
  experiment_id,
  arm,
  generator_version,
  policy_version,
  bundle_path,
  bundle_sha256,
  candidate_id,
  candidate_type,
  candidate_path,
  rank_position,
  retrieval_score,
  was_injected,
  required_check_keys,
  token_cost_estimate,
  notes
)
VALUES (
  NULLIF(:'case_id', '')::uuid,
  :'case_key',
  :'dispatch_id',
  NULLIF(:'research_run_id', ''),
  NULLIF(:'experiment_id', ''),
  NULLIF(:'arm', ''),
  NULLIF(:'generator_version', ''),
  NULLIF(:'policy_version', ''),
  NULLIF(:'bundle_path', ''),
  NULLIF(:'bundle_sha256', ''),
  :'candidate_id',
  :'candidate_type',
  NULLIF(:'candidate_path', ''),
  NULLIF(:'rank_position', '')::int,
  NULLIF(:'retrieval_score', '')::numeric,
  COALESCE(NULLIF(:'was_injected', '')::boolean, true),
  COALESCE(NULLIF(:'required_check_keys_json', ''), '[]')::jsonb,
  NULLIF(:'token_cost_estimate', '')::numeric,
  COALESCE(NULLIF(:'notes_json', ''), '{}')::jsonb
)
ON CONFLICT (dispatch_id, candidate_id, candidate_type) DO UPDATE SET
  case_id = EXCLUDED.case_id,
  case_key = EXCLUDED.case_key,
  research_run_id = EXCLUDED.research_run_id,
  experiment_id = EXCLUDED.experiment_id,
  arm = EXCLUDED.arm,
  generator_version = EXCLUDED.generator_version,
  policy_version = EXCLUDED.policy_version,
  bundle_path = EXCLUDED.bundle_path,
  bundle_sha256 = EXCLUDED.bundle_sha256,
  candidate_path = EXCLUDED.candidate_path,
  rank_position = EXCLUDED.rank_position,
  retrieval_score = EXCLUDED.retrieval_score,
  was_injected = EXCLUDED.was_injected,
  required_check_keys = EXCLUDED.required_check_keys,
  token_cost_estimate = EXCLUDED.token_cost_estimate,
  notes = EXCLUDED.notes
RETURNING json_build_object(
  'dispatch_id', dispatch_id,
  'candidate_id', candidate_id,
  'candidate_type', candidate_type,
  'rank_position', rank_position,
  'retrieval_score', retrieval_score
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Log one LMD bundle exposure set for a dispatch')
    parser.add_argument('--case-key', required=True)
    parser.add_argument('--dispatch-id', required=True)
    parser.add_argument('--research-run-id', default='')
    parser.add_argument('--bundle-path', default='')
    parser.add_argument('--bundle-json', default='')
    parser.add_argument('--experiment-id', default='')
    parser.add_argument('--arm', default='')
    parser.add_argument('--generator-version', default='')
    parser.add_argument('--policy-version', default='')
    parser.add_argument('--notes-json', default='{}')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def resolve_bundle_inputs(bundle_path: str, bundle_json: str) -> tuple[dict[str, Any], str, str]:
    normalized_path = bundle_path
    if bundle_path:
        path = Path(bundle_path)
        if not path.is_absolute():
            path = (ORCHESTRATOR_ROOT / bundle_path).resolve()
        normalized_path = to_repo_relative(path)
        return load_bundle(bundle_path=str(path), bundle_json=bundle_json)
    return load_bundle(bundle_path='', bundle_json=bundle_json)


def main() -> int:
    args = parse_args()
    try:
        user_notes = json.loads(args.notes_json or '{}')
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f'invalid --notes-json: {exc}')
    if not isinstance(user_notes, dict):
        raise SystemExit('--notes-json must decode to an object')

    bundle, resolved_bundle_path, raw_text = resolve_bundle_inputs(args.bundle_path, args.bundle_json)
    stored_bundle_path = ''
    if resolved_bundle_path:
        stored_bundle_path = to_repo_relative(Path(resolved_bundle_path))
    elif args.bundle_path:
        stored_bundle_path = args.bundle_path
    digest = bundle_sha256(raw_text)

    output: dict[str, Any] = {
        'ok': True,
        'case_key': args.case_key,
        'dispatch_id': args.dispatch_id,
        'research_run_id': args.research_run_id or None,
        'bundle_path': stored_bundle_path or None,
        'bundle_sha256': digest or None,
        'bundle_status': bundle.get('status'),
        'lmd_used': bool(bundle.get('lmd_used')),
        'dry_run': args.dry_run,
        'logged_count': 0,
        'candidates': [],
        'warnings': [],
    }

    if not bundle:
        output['warnings'].append('bundle_missing_or_unparseable')
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    if not bundle.get('lmd_used'):
        output['warnings'].append('bundle_not_used')
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    candidates = bundle_candidates(bundle)
    output['candidate_count'] = len(candidates)
    if not candidates:
        output['warnings'].append('bundle_has_no_candidates')
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    resolved_db_url = resolve_db_url(args.db_url)
    exposures_present = table_exists('lmd_bundle_exposures', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    assignments_present = table_exists('lmd_experiment_assignments', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    output['table_present'] = {
        'lmd_bundle_exposures': exposures_present,
        'lmd_experiment_assignments': assignments_present,
    }

    case_id = ''
    if not resolved_db_url:
        output['warnings'].append('db_url_unavailable')
    else:
        case_lookup = exec_sql(args.psql, resolved_db_url, CASE_LOOKUP_SQL, {'case_key': args.case_key}) or {}
        case_id = str(case_lookup.get('case_id') or '')
        output['case_id'] = case_lookup.get('case_id')

    assignment = {}
    if resolved_db_url and assignments_present:
        assignment = exec_sql(
            args.psql,
            resolved_db_url,
            ASSIGNMENT_LOOKUP_SQL,
            {'case_key': args.case_key, 'experiment_id': args.experiment_id},
        ) or {}

    experiment_id = args.experiment_id or assignment.get('experiment_id') or DEFAULT_LMD_EXPERIMENT_ID
    arm = args.arm or assignment.get('arm') or ''
    generator_version = args.generator_version or assignment.get('generator_version') or str(bundle.get('generator_version') or '')
    policy_version = args.policy_version or assignment.get('policy_version') or str(bundle.get('policy_version') or '')
    output['experiment_id'] = experiment_id
    output['arm'] = arm or None
    output['generator_version'] = generator_version or None
    output['policy_version'] = policy_version or None

    if not exposures_present:
        output['warnings'].append('lmd_bundle_exposures_table_missing')

    for candidate in candidates:
        row_notes = {
            **user_notes,
            'bundle_status': bundle.get('status'),
            'lmd_tier': bundle.get('lmd_tier'),
            'query_profile': bundle.get('query_profile') or {},
            'retrieval_policy': bundle.get('retrieval_policy') or {},
            'result_paths': bundle.get('result_paths') or [],
            'candidate_notes': candidate.get('notes') or {},
        }
        db_result = None
        if not args.dry_run and resolved_db_url and exposures_present:
            db_result = exec_sql(
                args.psql,
                resolved_db_url,
                INSERT_SQL,
                {
                    'case_id': case_id,
                    'case_key': args.case_key,
                    'dispatch_id': args.dispatch_id,
                    'research_run_id': args.research_run_id,
                    'experiment_id': experiment_id,
                    'arm': arm,
                    'generator_version': generator_version,
                    'policy_version': policy_version,
                    'bundle_path': stored_bundle_path,
                    'bundle_sha256': digest,
                    'candidate_id': candidate['candidate_id'],
                    'candidate_type': candidate['candidate_type'],
                    'candidate_path': candidate.get('candidate_path') or '',
                    'rank_position': str(candidate.get('rank_position') or ''),
                    'retrieval_score': '' if candidate.get('retrieval_score') is None else str(candidate.get('retrieval_score')),
                    'was_injected': 'true',
                    'required_check_keys_json': json.dumps(candidate.get('required_check_keys') or []),
                    'token_cost_estimate': '' if candidate.get('token_cost_estimate') is None else str(candidate.get('token_cost_estimate')),
                    'notes_json': json.dumps(row_notes),
                },
            )
        output['candidates'].append({
            'candidate_id': candidate['candidate_id'],
            'candidate_type': candidate['candidate_type'],
            'candidate_path': candidate.get('candidate_path') or None,
            'rank_position': candidate.get('rank_position'),
            'retrieval_score': candidate.get('retrieval_score'),
            'idempotency_key': {
                'dispatch_id': args.dispatch_id,
                'candidate_id': candidate['candidate_id'],
                'candidate_type': candidate['candidate_type'],
            },
            'status': 'dry_run' if args.dry_run else ('upserted_by_db' if db_result else 'skipped_db_write'),
            'db_result': db_result,
        })
        output['logged_count'] += 1

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
