#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
ORCH_ROOT = SCRIPT_PATH.parents[4]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.causal_projection import projection_significance  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.io import read_json  # noqa: E402
from lib.paths import CASE_REVIEWS_ROOT, to_repo_relative  # noqa: E402

SUMMARY_PATH = ORCH_ROOT / 'qualitative-db' / '60-causal-map' / 'generated' / 'significant-projection-backfill-summary.json'

DISTINCT_OCCURRENCE_CASE_KEYS_SQL = r'''
SELECT COALESCE(json_agg(case_key ORDER BY case_key), '[]'::json)::text
FROM (
  SELECT DISTINCT case_key
  FROM public.proposed_causal_candidate_occurrences
  WHERE NULLIF(case_key, '') IS NOT NULL
) t;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Check that proposal-mining inputs match current significance-qualified projections')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def existing_projection_case_keys() -> tuple[list[str], list[str]]:
    projection_case_keys: list[str] = []
    significant_case_keys: list[str] = []
    for case_dir in sorted(CASE_REVIEWS_ROOT.glob('case-*')):
        if not case_dir.is_dir():
            continue
        projection_path = case_dir / 'causal-projection.json'
        if not projection_path.exists():
            continue
        projection_case_keys.append(case_dir.name)
        projection = read_json(projection_path, default={}) or {}
        if bool(projection_significance(projection).get('significant')):
            significant_case_keys.append(case_dir.name)
    return projection_case_keys, significant_case_keys



def summary_case_sets() -> tuple[list[str], list[str]]:
    payload = read_json(SUMMARY_PATH, default={}) or {}
    selected = sorted({str(row.get('case_key') or '').strip() for row in (payload.get('selected_cases') or []) if str(row.get('case_key') or '').strip()})
    skipped = sorted({str(row.get('case_key') or '').strip() for row in (payload.get('skipped_cases') or []) if str(row.get('case_key') or '').strip()})
    return selected, skipped



def occurrence_case_keys(*, db_url: str, psql_bin: str) -> tuple[bool, list[str]]:
    resolved_db_url = resolve_db_url(db_url)
    if not resolved_db_url:
        return False, []
    if not table_exists('proposed_causal_candidate_occurrences', db_url=resolved_db_url, psql_bin=psql_bin):
        return False, []
    payload = exec_sql(psql_bin, resolved_db_url, DISTINCT_OCCURRENCE_CASE_KEYS_SQL, {})
    if isinstance(payload, list):
        return True, sorted({str(item).strip() for item in payload if str(item).strip()})
    return True, []



def main() -> int:
    args = parse_args()
    projection_case_keys, significant_projection_case_keys = existing_projection_case_keys()
    summary_selected_case_keys, summary_skipped_case_keys = summary_case_sets()
    db_checked, occurrence_case_key_rows = occurrence_case_keys(db_url=args.db_url, psql_bin=args.psql)

    mismatches: list[dict[str, Any]] = []
    if summary_selected_case_keys != significant_projection_case_keys:
        mismatches.append(
            {
                'kind': 'summary_selected_vs_significant_projection_files',
                'expected': significant_projection_case_keys,
                'observed': summary_selected_case_keys,
            }
        )
    summary_partition = sorted({*summary_selected_case_keys, *summary_skipped_case_keys})
    if summary_partition and sorted(summary_partition) != sorted({*projection_case_keys, *summary_skipped_case_keys}):
        # This catches the case where the summary omits currently projected files from either selected/skipped buckets.
        missing_from_summary = sorted(set(projection_case_keys) - set(summary_partition))
        if missing_from_summary:
            mismatches.append(
                {
                    'kind': 'projection_files_missing_from_summary',
                    'missing_case_keys': missing_from_summary,
                }
            )
    if db_checked and occurrence_case_key_rows != significant_projection_case_keys:
        mismatches.append(
            {
                'kind': 'proposal_occurrence_case_keys_vs_significant_projection_files',
                'expected': significant_projection_case_keys,
                'observed': occurrence_case_key_rows,
            }
        )

    result = {
        'ok': not mismatches,
        'summary_path': to_repo_relative(SUMMARY_PATH) if SUMMARY_PATH.exists() else None,
        'projection_file_case_keys': projection_case_keys,
        'significant_projection_case_keys': significant_projection_case_keys,
        'summary_selected_case_keys': summary_selected_case_keys,
        'summary_skipped_case_keys': summary_skipped_case_keys,
        'db_checked': db_checked,
        'proposal_occurrence_case_keys': occurrence_case_key_rows,
        'mismatches': mismatches,
    }
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0 if not mismatches else 1


if __name__ == '__main__':
    raise SystemExit(main())
