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

CASE_LOOKUP_SQL = r'''
SELECT json_build_object(
  'case_id', id,
  'case_key', case_key
)::text
FROM public.cases
WHERE case_key = :'case_key'
LIMIT 1;
'''

INTERVENTION_LOOKUP_SQL = r'''
SELECT json_build_object(
  'intervention_key', intervention_key,
  'path', path,
  'status', status,
  'application_surface', application_surface,
  'change_kind', change_kind
)::text
FROM public.learning_interventions
WHERE intervention_key = NULLIF(:'intervention_key', '')
   OR path = NULLIF(:'path', '')
ORDER BY intervention_key = NULLIF(:'intervention_key', '') DESC
LIMIT 1;
'''

INSERT_SQL = r'''
INSERT INTO public.learning_intervention_applications (
  intervention_key,
  case_id,
  case_key,
  research_run_id,
  application_surface,
  bundle_path,
  dispatch_id,
  notes,
  applied_at
)
VALUES (
  :'intervention_key',
  NULLIF(:'case_id', '')::uuid,
  :'case_key',
  NULLIF(:'research_run_id', ''),
  :'application_surface',
  NULLIF(:'bundle_path', ''),
  NULLIF(:'dispatch_id', ''),
  COALESCE(NULLIF(:'notes_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'applied_at', '')::timestamptz, NOW())
)
ON CONFLICT (intervention_key, research_run_id, application_surface) DO UPDATE SET
  case_id = EXCLUDED.case_id,
  case_key = EXCLUDED.case_key,
  bundle_path = EXCLUDED.bundle_path,
  dispatch_id = EXCLUDED.dispatch_id,
  notes = EXCLUDED.notes,
  applied_at = EXCLUDED.applied_at
RETURNING json_build_object(
  'id', id,
  'intervention_key', intervention_key,
  'case_key', case_key,
  'research_run_id', research_run_id,
  'application_surface', application_surface,
  'bundle_path', bundle_path,
  'applied_at', applied_at
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Log one or more intervention applications for a case')
    parser.add_argument('--case-key', required=True)
    parser.add_argument('--intervention-key', action='append', help='Registered intervention key to log')
    parser.add_argument('--intervention-path', action='append', help='Registered intervention note path to log')
    parser.add_argument('--application-surface', default='', help='Override application surface; defaults to the registered intervention surface')
    parser.add_argument('--bundle-path', default='', help='Related bundle path, e.g. lmd-bundle.json path')
    parser.add_argument('--dispatch-id', default='')
    parser.add_argument('--research-run-id', default='')
    parser.add_argument('--notes-json', default='{}')
    parser.add_argument('--applied-at', default='')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    refs: list[tuple[str, str]] = []
    refs.extend(("intervention_key", value) for value in (args.intervention_key or []) if value)
    refs.extend(("path", value) for value in (args.intervention_path or []) if value)
    if not refs:
        raise SystemExit('Provide at least one --intervention-key or --intervention-path')

    resolved_db_url = resolve_db_url(args.db_url)
    interventions_present = table_exists('learning_interventions', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    applications_present = table_exists('learning_intervention_applications', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False

    output: dict[str, Any] = {
        'ok': True,
        'case_key': args.case_key,
        'research_run_id': args.research_run_id or None,
        'dry_run': args.dry_run,
        'logged_count': 0,
        'applications': [],
        'table_present': {
            'learning_interventions': interventions_present,
            'learning_intervention_applications': applications_present,
        },
    }

    if not resolved_db_url:
        output['warning'] = 'db url unavailable; cannot persist intervention applications'
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    if not interventions_present:
        output['warning'] = 'learning_interventions table not present; apply roles/evaluator/sql/012_learning_interventions.sql and register interventions first'
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    if not applications_present:
        output['warning'] = 'learning_intervention_applications table not present; apply roles/evaluator/sql/013_learning_intervention_applications.sql to enable persistence'
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    case_lookup = exec_sql(args.psql, resolved_db_url, CASE_LOOKUP_SQL, {'case_key': args.case_key})
    case_id = str((case_lookup or {}).get('case_id') or '')
    notes_json = json.dumps(json.loads(args.notes_json or '{}'))

    missing_refs: list[dict[str, str]] = []
    for ref_kind, ref_value in refs:
        lookup = exec_sql(
            args.psql,
            resolved_db_url,
            INTERVENTION_LOOKUP_SQL,
            {
                'intervention_key': ref_value if ref_kind == 'intervention_key' else '',
                'path': ref_value if ref_kind == 'path' else '',
            },
        )
        if not lookup:
            missing_refs.append({'kind': ref_kind, 'value': ref_value})
            continue

        db_result: dict[str, Any] | None = None
        if not args.dry_run:
            db_result = exec_sql(
                args.psql,
                resolved_db_url,
                INSERT_SQL,
                {
                    'intervention_key': lookup['intervention_key'],
                    'case_id': case_id,
                    'case_key': args.case_key,
                    'research_run_id': args.research_run_id,
                    'application_surface': args.application_surface or lookup.get('application_surface') or 'researcher_prompt',
                    'bundle_path': args.bundle_path,
                    'dispatch_id': args.dispatch_id,
                    'notes_json': notes_json,
                    'applied_at': args.applied_at,
                },
            )
        output['applications'].append({
            'lookup': lookup,
            'idempotency_key': {
                'intervention_key': lookup['intervention_key'],
                'research_run_id': args.research_run_id,
                'application_surface': args.application_surface or lookup.get('application_surface') or 'researcher_prompt',
            },
            'status': 'dry_run' if args.dry_run else ('upserted_by_db' if db_result else 'skipped_db_write'),
            'db_result': db_result,
        })
        output['logged_count'] += 1

    if missing_refs:
        output['missing_interventions'] = missing_refs

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
