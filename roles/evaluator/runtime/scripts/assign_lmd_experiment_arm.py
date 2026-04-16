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
from lib.lmd import (  # noqa: E402
    DEFAULT_LMD_EXPERIMENT_ID,
    DEFAULT_LMD_GENERATOR_VERSION,
    DEFAULT_LMD_POLICY_VERSION,
    DEFAULT_TREATMENT_RATIO,
    choose_arm,
)

CASE_LOOKUP_SQL = r'''
SELECT json_build_object(
  'case_id', id,
  'case_key', case_key
)::text
FROM public.cases
WHERE case_key = :'case_key'
LIMIT 1;
'''

UPSERT_SQL = r'''
INSERT INTO public.lmd_experiment_assignments (
  case_id,
  case_key,
  experiment_id,
  arm,
  generator_version,
  policy_version,
  assignment_unit,
  assignment_hash,
  assignment_fraction,
  treatment_ratio,
  notes,
  updated_at
)
VALUES (
  NULLIF(:'case_id', '')::uuid,
  :'case_key',
  :'experiment_id',
  :'arm',
  :'generator_version',
  :'policy_version',
  :'assignment_unit',
  :'assignment_hash',
  :'assignment_fraction'::numeric,
  :'treatment_ratio'::numeric,
  COALESCE(NULLIF(:'notes_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (case_key, experiment_id) DO UPDATE SET
  case_id = EXCLUDED.case_id,
  arm = EXCLUDED.arm,
  generator_version = EXCLUDED.generator_version,
  policy_version = EXCLUDED.policy_version,
  assignment_unit = EXCLUDED.assignment_unit,
  assignment_hash = EXCLUDED.assignment_hash,
  assignment_fraction = EXCLUDED.assignment_fraction,
  treatment_ratio = EXCLUDED.treatment_ratio,
  notes = EXCLUDED.notes,
  updated_at = NOW()
RETURNING json_build_object(
  'case_key', case_key,
  'experiment_id', experiment_id,
  'arm', arm,
  'generator_version', generator_version,
  'policy_version', policy_version,
  'assignment_fraction', assignment_fraction,
  'treatment_ratio', treatment_ratio
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Assign a deterministic LMD experiment arm for one case')
    parser.add_argument('--case-key', required=True)
    parser.add_argument('--experiment-id', default=DEFAULT_LMD_EXPERIMENT_ID)
    parser.add_argument('--generator-version', default=DEFAULT_LMD_GENERATOR_VERSION)
    parser.add_argument('--policy-version', default=DEFAULT_LMD_POLICY_VERSION)
    parser.add_argument('--treatment-ratio', type=float, default=DEFAULT_TREATMENT_RATIO)
    parser.add_argument('--notes-json', default='{}')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        notes = json.loads(args.notes_json or '{}')
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f'invalid --notes-json: {exc}')
    if not isinstance(notes, dict):
        raise SystemExit('--notes-json must decode to an object')

    assignment = choose_arm(
        experiment_id=args.experiment_id,
        case_key=args.case_key,
        treatment_ratio=args.treatment_ratio,
    )
    output: dict[str, Any] = {
        'ok': True,
        'case_key': args.case_key,
        'experiment_id': assignment['experiment_id'],
        'arm': assignment['arm'],
        'generator_version': args.generator_version,
        'policy_version': args.policy_version,
        'assignment_unit': assignment['assignment_unit'],
        'assignment_hash': assignment['assignment_hash'],
        'assignment_fraction': assignment['assignment_fraction'],
        'treatment_ratio': assignment['treatment_ratio'],
        'persisted': False,
        'dry_run': args.dry_run,
    }

    resolved_db_url = resolve_db_url(args.db_url)
    table_present = table_exists('lmd_experiment_assignments', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    output['table_present'] = table_present

    if not resolved_db_url:
        output['warning'] = 'db url unavailable; returning deterministic assignment only'
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    case_lookup = exec_sql(args.psql, resolved_db_url, CASE_LOOKUP_SQL, {'case_key': args.case_key}) or {}
    output['case_id'] = case_lookup.get('case_id')

    if not table_present:
        output['warning'] = 'lmd_experiment_assignments table not present; apply roles/evaluator/sql/014_lmd_experiment_assignments.sql to enable persistence'
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    if args.dry_run:
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    db_result = exec_sql(
        args.psql,
        resolved_db_url,
        UPSERT_SQL,
        {
            'case_id': str(case_lookup.get('case_id') or ''),
            'case_key': args.case_key,
            'experiment_id': assignment['experiment_id'],
            'arm': assignment['arm'],
            'generator_version': args.generator_version,
            'policy_version': args.policy_version,
            'assignment_unit': assignment['assignment_unit'],
            'assignment_hash': assignment['assignment_hash'],
            'assignment_fraction': str(assignment['assignment_fraction']),
            'treatment_ratio': str(assignment['treatment_ratio']),
            'notes_json': json.dumps(notes),
        },
    )
    output['persisted'] = True
    output['db_result'] = db_result
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
