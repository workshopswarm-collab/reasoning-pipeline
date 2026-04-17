#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
ORCH_ROOT = SCRIPT_PATH.parents[4]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, missing_columns, resolve_db_url, table_exists  # noqa: E402
from lib.proposed_causal_shadow_outcomes import judge_shadow_row  # noqa: E402

REQUIRED_SHADOW_COLUMNS = [
    'outcome_label',
    'outcome_score',
    'outcome_favored',
    'judged_at',
    'judge_version',
    'outcome_metadata',
]

SHADOW_ROWS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY created_at, id), '[]'::json)::text
FROM (
  SELECT *
  FROM public.proposed_causal_shadow_matches
) t;
'''

OCCURRENCE_ROWS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY updated_at, id), '[]'::json)::text
FROM (
  SELECT *
  FROM public.proposed_causal_candidate_occurrences
) t;
'''

UPDATE_SQL = r'''
UPDATE public.proposed_causal_shadow_matches
SET
  outcome_label = NULLIF(:'outcome_label', ''),
  outcome_score = NULLIF(:'outcome_score', '')::numeric,
  outcome_favored = CASE
    WHEN NULLIF(:'outcome_favored', '') IS NULL THEN NULL
    ELSE NULLIF(:'outcome_favored', '')::boolean
  END,
  judged_at = NULLIF(:'judged_at', '')::timestamptz,
  judge_version = NULLIF(:'judge_version', ''),
  outcome_metadata = COALESCE(NULLIF(:'outcome_metadata_json', ''), '{}')::jsonb
WHERE id = NULLIF(:'row_id', '')::bigint
RETURNING json_build_object(
  'id', id,
  'proposal_id', proposal_id,
  'outcome_label', outcome_label,
  'outcome_score', outcome_score
)::text;
'''



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Deterministically score proposed-causal shadow matches as helpful / neutral / harmful / unclear')
    parser.add_argument('--case-key', default='')
    parser.add_argument('--proposal-id', default='')
    parser.add_argument('--dispatch-id', default='')
    parser.add_argument('--proposal-source', default='')
    parser.add_argument('--bridge-source', default='')
    parser.add_argument('--only-unjudged', action='store_true')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def occurrence_rows_match_filters(occurrence_rows: list[dict[str, Any]], args: argparse.Namespace) -> bool:
    if args.proposal_source:
        if not any(str(row.get('proposal_source') or '').strip() == args.proposal_source for row in occurrence_rows if isinstance(row, dict)):
            return False
    if args.bridge_source:
        def bridge_source_for(row: dict[str, Any]) -> str:
            metadata = row.get('proposal_metadata') or {}
            if not isinstance(metadata, dict):
                return ''
            return str(metadata.get('bridge_source') or '').strip()
        if not any(bridge_source_for(row) == args.bridge_source for row in occurrence_rows if isinstance(row, dict)):
            return False
    return True



def matches_filters(row: dict[str, Any], args: argparse.Namespace, occurrence_rows: list[dict[str, Any]]) -> bool:
    if args.case_key and str(row.get('case_key') or '').strip() != args.case_key:
        return False
    if args.proposal_id and str(row.get('proposal_id') or '').strip() != args.proposal_id:
        return False
    if args.dispatch_id and str(row.get('dispatch_id') or '').strip() != args.dispatch_id:
        return False
    if args.only_unjudged and str(row.get('outcome_label') or '').strip():
        return False
    if not occurrence_rows_match_filters(occurrence_rows, args):
        return False
    return True



def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()



def main() -> int:
    args = parse_args()
    resolved_db_url = resolve_db_url(args.db_url)
    shadow_present = table_exists('proposed_causal_shadow_matches', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    occurrence_present = table_exists('proposed_causal_candidate_occurrences', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    shadow_missing: list[str] = []
    if resolved_db_url and shadow_present:
        shadow_missing = missing_columns('proposed_causal_shadow_matches', REQUIRED_SHADOW_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql)
        if shadow_missing:
            shadow_present = False

    shadow_rows = exec_sql(args.psql, resolved_db_url, SHADOW_ROWS_SQL, {}) if resolved_db_url and shadow_present else []
    occurrence_rows = exec_sql(args.psql, resolved_db_url, OCCURRENCE_ROWS_SQL, {}) if resolved_db_url and occurrence_present else []
    if not isinstance(shadow_rows, list):
        shadow_rows = []
    if not isinstance(occurrence_rows, list):
        occurrence_rows = []

    occurrence_by_case_and_proposal: dict[tuple[str, str], list[dict[str, Any]]] = {}
    occurrence_by_proposal: dict[str, list[dict[str, Any]]] = {}
    for row in occurrence_rows:
        proposal_id = str(row.get('proposal_id') or '').strip()
        case_key = str(row.get('case_key') or '').strip()
        if proposal_id:
            occurrence_by_proposal.setdefault(proposal_id, []).append(row)
        key = (case_key, proposal_id)
        occurrence_by_case_and_proposal.setdefault(key, []).append(row)

    case_artifact_cache: dict[str, dict[str, Any]] = {}
    updated_rows: list[dict[str, Any]] = []
    persisted_count = 0
    label_counts: Counter[str] = Counter()

    for row in shadow_rows:
        if not isinstance(row, dict):
            continue
        case_key = str(row.get('case_key') or '').strip()
        proposal_id = str(row.get('proposal_id') or '').strip()
        linked_occurrences = occurrence_by_case_and_proposal.get((case_key, proposal_id), [])
        occurrence_scope = 'same_case'
        if not linked_occurrences:
            fallback_occurrences = occurrence_by_proposal.get(proposal_id, [])
            if fallback_occurrences:
                linked_occurrences = fallback_occurrences
                occurrence_scope = 'cross_case'
        if not matches_filters(row, args, linked_occurrences):
            continue
        if case_key not in case_artifact_cache:
            from lib.proposed_causal_shadow_outcomes import load_case_artifacts  # noqa: PLC0415,E402
            case_artifact_cache[case_key] = load_case_artifacts(case_key)
        judgment = judge_shadow_row(
            row,
            occurrence_rows=linked_occurrences,
            case_artifacts=case_artifact_cache[case_key],
            occurrence_scope=occurrence_scope,
        )
        judged_at = now_iso()
        record = {
            'row_id': str(row.get('id') or ''),
            'proposal_id': proposal_id,
            'case_key': case_key,
            'dispatch_id': str(row.get('dispatch_id') or '').strip(),
            'outcome_label': judgment['outcome_label'],
            'outcome_score': judgment['outcome_score'],
            'outcome_favored': judgment['outcome_favored'],
            'judge_version': judgment['judge_version'],
            'judged_at': judged_at,
            'outcome_metadata': judgment['outcome_metadata'],
            'db_result': None,
        }
        if resolved_db_url and shadow_present and not args.dry_run:
            record['db_result'] = exec_sql(
                args.psql,
                resolved_db_url,
                UPDATE_SQL,
                {
                    'row_id': record['row_id'],
                    'outcome_label': record['outcome_label'],
                    'outcome_score': str(record['outcome_score']),
                    'outcome_favored': 'true' if record['outcome_favored'] else 'false',
                    'judge_version': record['judge_version'],
                    'judged_at': judged_at,
                    'outcome_metadata_json': json.dumps(record['outcome_metadata']),
                },
            )
            persisted_count += 1
        updated_rows.append(record)
        label_counts[record['outcome_label']] += 1

    output: dict[str, Any] = {
        'ok': True,
        'row_count': len(updated_rows),
        'persisted_count': persisted_count,
        'filters': {
            'case_key': args.case_key,
            'proposal_id': args.proposal_id,
            'dispatch_id': args.dispatch_id,
            'proposal_source': args.proposal_source,
            'bridge_source': args.bridge_source,
            'only_unjudged': bool(args.only_unjudged),
        },
        'label_counts': dict(sorted(label_counts.items())),
        'table_present': {
            'proposed_causal_shadow_matches': shadow_present,
            'proposed_causal_candidate_occurrences': occurrence_present,
        },
        'rows': updated_rows,
    }
    if not resolved_db_url:
        output['warning'] = 'db_url_unavailable'
    elif shadow_missing:
        output['warning'] = 'proposed_causal_shadow_matches table missing outcome-label columns; apply roles/evaluator/sql/034_proposed_causal_shadow_outcome_labels.sql'
        output['missing_columns'] = {'proposed_causal_shadow_matches': shadow_missing}
    elif not shadow_present:
        output['warning'] = 'proposed_causal_shadow_matches table missing; apply roles/evaluator/sql/031_proposed_causal_shadow_matches.sql and roles/evaluator/sql/034_proposed_causal_shadow_outcome_labels.sql'
    elif not occurrence_present:
        output['warning'] = 'proposed_causal_candidate_occurrences table missing; apply roles/evaluator/sql/024_proposed_causal_candidate_occurrences.sql'
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
