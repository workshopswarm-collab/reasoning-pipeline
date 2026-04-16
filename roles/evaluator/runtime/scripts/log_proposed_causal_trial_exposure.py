#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.io import read_json  # noqa: E402
from lib.paths import ORCHESTRATOR_ROOT, to_repo_relative  # noqa: E402

LOOKUP_SQL = r'''
SELECT json_build_object('id', id)::text
FROM public.proposed_causal_trial_exposures
WHERE dispatch_id = NULLIF(:'dispatch_id', '')
  AND proposal_id = :'proposal_id'
  AND candidate_type = :'candidate_type'
ORDER BY id DESC
LIMIT 1;
'''

UPDATE_SQL = r'''
UPDATE public.proposed_causal_trial_exposures
SET
  proposal_key = :'proposal_key',
  mechanism_family = NULLIF(:'mechanism_family', ''),
  case_key = :'case_key',
  research_run_id = NULLIF(:'research_run_id', ''),
  experiment_id = NULLIF(:'experiment_id', ''),
  experiment_arm = NULLIF(:'experiment_arm', ''),
  trial_rank = NULLIF(:'trial_rank', '')::int,
  shadow_trial_score = NULLIF(:'shadow_trial_score', '')::numeric,
  family_trial_rank = NULLIF(:'family_trial_rank', '')::int,
  overlay_score = NULLIF(:'overlay_score', '')::numeric,
  preview_only = COALESCE(NULLIF(:'preview_only', '')::boolean, true),
  injected = COALESCE(NULLIF(:'injected', '')::boolean, false),
  overlay_mode = COALESCE(NULLIF(:'overlay_mode', ''), 'preview_only'),
  matched_active_nodes = COALESCE(NULLIF(:'matched_active_nodes_json', ''), '[]')::jsonb,
  matched_candidate_edges = COALESCE(NULLIF(:'matched_candidate_edges_json', ''), '[]')::jsonb,
  matched_required_checks = COALESCE(NULLIF(:'matched_required_checks_json', ''), '[]')::jsonb,
  notes = COALESCE(NULLIF(:'notes_json', ''), '{}')::jsonb
WHERE id = NULLIF(:'row_id', '')::bigint
RETURNING json_build_object('proposal_id', proposal_id, 'trial_rank', trial_rank, 'action', 'updated')::text;
'''

INSERT_SQL = r'''
INSERT INTO public.proposed_causal_trial_exposures (
  proposal_id,
  proposal_key,
  candidate_type,
  mechanism_family,
  case_key,
  dispatch_id,
  research_run_id,
  experiment_id,
  experiment_arm,
  trial_rank,
  shadow_trial_score,
  family_trial_rank,
  overlay_score,
  preview_only,
  injected,
  overlay_mode,
  matched_active_nodes,
  matched_candidate_edges,
  matched_required_checks,
  notes
)
VALUES (
  :'proposal_id',
  :'proposal_key',
  :'candidate_type',
  COALESCE(NULLIF(:'mechanism_family', ''), 'unassigned'),
  :'case_key',
  NULLIF(:'dispatch_id', ''),
  NULLIF(:'research_run_id', ''),
  NULLIF(:'experiment_id', ''),
  NULLIF(:'experiment_arm', ''),
  NULLIF(:'trial_rank', '')::int,
  NULLIF(:'shadow_trial_score', '')::numeric,
  NULLIF(:'family_trial_rank', '')::int,
  NULLIF(:'overlay_score', '')::numeric,
  COALESCE(NULLIF(:'preview_only', '')::boolean, true),
  COALESCE(NULLIF(:'injected', '')::boolean, false),
  COALESCE(NULLIF(:'overlay_mode', ''), 'preview_only'),
  COALESCE(NULLIF(:'matched_active_nodes_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'matched_candidate_edges_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'matched_required_checks_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'notes_json', ''), '{}')::jsonb
)
RETURNING json_build_object('proposal_id', proposal_id, 'trial_rank', trial_rank, 'action', 'inserted')::text;
'''

CASE_KEY_RE = re.compile(r'\b(case-[a-zA-Z0-9]+)\b')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Log preview-only proposed causal trial exposures from an LMD bundle')
    parser.add_argument('--bundle-path', required=True)
    parser.add_argument('--case-key', default='')
    parser.add_argument('--dispatch-id', default='')
    parser.add_argument('--research-run-id', default='')
    parser.add_argument('--experiment-id', default='')
    parser.add_argument('--experiment-arm', default='')
    parser.add_argument('--notes-json', default='{}')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    return parser.parse_args()



def resolve_bundle_path(bundle_path: str) -> Path:
    path = Path(bundle_path)
    if not path.is_absolute():
        path = (ORCHESTRATOR_ROOT / bundle_path).resolve()
    return path



def _case_key_from_text(text: str) -> str:
    match = CASE_KEY_RE.search(text or '')
    return match.group(1) if match else ''



def case_key_from_bundle(bundle: dict[str, Any], *, bundle_path: Path, cli_case_key: str = '') -> str:
    case_key = str(cli_case_key or '').strip()
    if case_key:
        return case_key
    direct = str(bundle.get('case_key') or '').strip()
    if direct:
        return direct
    case_context = bundle.get('case_context') or {}
    for key in ['case_key', 'market_id', 'question_id']:
        value = str(case_context.get(key) or '').strip()
        if value.startswith('case-'):
            return value
    for value in [str(bundle_path), to_repo_relative(bundle_path)]:
        inferred = _case_key_from_text(value)
        if inferred:
            return inferred
    for item in bundle.get('result_paths') or []:
        inferred = _case_key_from_text(str(item))
        if inferred:
            return inferred
    return ''



def row_params(*, row: dict[str, Any], bundle: dict[str, Any], case_key: str, args: argparse.Namespace, user_notes: dict[str, Any]) -> dict[str, Any]:
    row_notes = {
        **user_notes,
        'bundle_status': bundle.get('status'),
        'lmd_used': bool(bundle.get('lmd_used')),
        'usage_mode': bundle.get('usage_mode'),
        'lmd_tier': bundle.get('lmd_tier'),
        'query_profile': bundle.get('query_profile') or {},
        'retrieval_policy': bundle.get('retrieval_policy') or {},
        'result_paths': bundle.get('result_paths') or [],
        'selection_policy_version': ((bundle.get('trial_overlay') or {}).get('selection_policy_version')),
        'selection_caps': ((bundle.get('trial_overlay') or {}).get('selection_caps') or {}),
        'candidate_notes': row.get('notes') or {},
        'score_breakdown': row.get('score_breakdown') or {},
        'matched_question_mechanics': row.get('matched_question_mechanics') or [],
        'matched_source_of_truth_class': row.get('matched_source_of_truth_class') or [],
        'matched_platforms': row.get('matched_platforms') or [],
        'matched_categories': row.get('matched_categories') or [],
    }
    return {
        'proposal_id': row.get('proposal_id') or f"{row.get('candidate_type')}:{row.get('proposal_key')}",
        'proposal_key': row.get('proposal_key') or '',
        'candidate_type': row.get('candidate_type') or '',
        'mechanism_family': row.get('mechanism_family') or '',
        'case_key': case_key,
        'dispatch_id': args.dispatch_id,
        'research_run_id': args.research_run_id,
        'experiment_id': args.experiment_id,
        'experiment_arm': args.experiment_arm,
        'trial_rank': '' if row.get('rank_position') in (None, '') else str(row.get('rank_position')),
        'shadow_trial_score': '' if row.get('shadow_trial_score') in (None, '') else str(row.get('shadow_trial_score')),
        'family_trial_rank': '' if row.get('family_trial_rank') in (None, '') else str(row.get('family_trial_rank')),
        'overlay_score': '' if row.get('overlay_score') in (None, '') else str(row.get('overlay_score')),
        'preview_only': 'true' if row.get('preview_only', True) else 'false',
        'injected': 'true' if row.get('injected') else 'false',
        'overlay_mode': row.get('overlay_mode') or 'preview_only',
        'matched_active_nodes_json': json.dumps(row.get('matched_active_nodes') or []),
        'matched_candidate_edges_json': json.dumps((row.get('matched_candidate_edges') or []) + (row.get('matched_contested_edges') or [])),
        'matched_required_checks_json': json.dumps(row.get('matched_required_checks') or []),
        'notes_json': json.dumps(row_notes),
    }



def main() -> int:
    args = parse_args()
    try:
        user_notes = json.loads(args.notes_json or '{}')
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f'invalid --notes-json: {exc}')
    if not isinstance(user_notes, dict):
        raise SystemExit('--notes-json must decode to an object')

    bundle_path = resolve_bundle_path(args.bundle_path)
    stored_bundle_path = to_repo_relative(bundle_path)
    bundle = read_json(bundle_path, default={}) or {}
    overlay = bundle.get('trial_overlay') or {}
    selected = overlay.get('selected_candidates') or []
    case_key = case_key_from_bundle(bundle, bundle_path=bundle_path, cli_case_key=args.case_key)

    output: dict[str, Any] = {
        'ok': True,
        'bundle_path': stored_bundle_path,
        'case_key': case_key or None,
        'dispatch_id': args.dispatch_id or None,
        'research_run_id': args.research_run_id or None,
        'experiment_id': args.experiment_id or None,
        'experiment_arm': args.experiment_arm or None,
        'dry_run': args.dry_run,
        'trial_overlay_enabled': bool(overlay.get('enabled', False)),
        'preview_only': bool(overlay.get('preview_only', True)),
        'candidate_count_considered': int(overlay.get('candidate_count_considered') or 0),
        'selected_count': len(selected),
        'logged_count': 0,
        'inserted_count': 0,
        'updated_count': 0,
        'warnings': [],
        'rows': [],
    }

    if not bundle:
        output['warnings'].append('bundle_missing_or_unparseable')
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0
    if not overlay:
        output['warnings'].append('trial_overlay_missing')
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0
    if not selected:
        output['warnings'].append('trial_overlay_has_no_selected_candidates')
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0
    if not case_key:
        output['warnings'].append('case_key_unresolved')
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    resolved_db_url = resolve_db_url(args.db_url)
    table_present = table_exists('proposed_causal_trial_exposures', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    output['table_present'] = {'proposed_causal_trial_exposures': table_present}

    if not resolved_db_url:
        output['warnings'].append('db_url_unavailable')
    elif not table_present:
        output['warnings'].append('proposed_causal_trial_exposures_table_missing')

    for row in selected:
        if not isinstance(row, dict):
            continue
        params = row_params(row=row, bundle=bundle, case_key=case_key, args=args, user_notes=user_notes)
        db_result = None
        row_status = 'skipped_db_write'
        if not args.dry_run and resolved_db_url and table_present:
            existing_row = {}
            if args.dispatch_id:
                existing_row = exec_sql(
                    args.psql,
                    resolved_db_url,
                    LOOKUP_SQL,
                    {
                        'dispatch_id': args.dispatch_id,
                        'proposal_id': params['proposal_id'],
                        'candidate_type': params['candidate_type'],
                    },
                ) or {}
            row_id = str(existing_row.get('id') or '').strip()
            if row_id:
                db_result = exec_sql(
                    args.psql,
                    resolved_db_url,
                    UPDATE_SQL,
                    {**params, 'row_id': row_id},
                )
                row_status = 'updated_existing_row'
                output['updated_count'] += 1
            else:
                db_result = exec_sql(args.psql, resolved_db_url, INSERT_SQL, params)
                row_status = 'inserted_new_row'
                output['inserted_count'] += 1
        elif args.dry_run:
            row_status = 'dry_run'
        output['rows'].append(
            {
                'proposal_id': params['proposal_id'],
                'proposal_key': params['proposal_key'],
                'candidate_type': params['candidate_type'],
                'trial_rank': row.get('rank_position'),
                'family_trial_rank': row.get('family_trial_rank'),
                'overlay_score': row.get('overlay_score'),
                'preview_only': bool(row.get('preview_only', True)),
                'injected': bool(row.get('injected', False)),
                'idempotency_key': {
                    'dispatch_id': params['dispatch_id'],
                    'proposal_id': params['proposal_id'],
                    'candidate_type': params['candidate_type'],
                },
                'status': row_status,
                'db_result': db_result,
            }
        )
        output['logged_count'] += 1

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
