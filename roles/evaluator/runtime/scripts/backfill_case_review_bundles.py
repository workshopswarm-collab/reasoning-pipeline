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

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url  # noqa: E402
from lib.paths import case_review_dir  # noqa: E402
from materialize_case_review_bundle import materialize_case_review_bundle  # noqa: E402

SQL = r'''
WITH candidates AS (
  SELECT DISTINCT
    c.case_key,
    c.status,
    c.opened_at,
    c.closed_at,
    CASE WHEN lcr.case_key IS NULL THEN false ELSE true END AS already_indexed
  FROM public.cases c
  JOIN public.forecast_decisions_with_resolution f ON f.market_id::text = c.market_id::text
  LEFT JOIN public.learning_case_reviews lcr ON lcr.case_key = c.case_key
  WHERE f.resolution_status = 'resolved'
)
SELECT json_build_object(
  'cases', COALESCE(
    (
      SELECT json_agg(row_to_json(x) ORDER BY COALESCE(x.closed_at, x.opened_at) DESC, x.case_key DESC)
      FROM (
        SELECT *
        FROM candidates
        WHERE (CASE WHEN :'include_indexed' = 'true' THEN true ELSE NOT already_indexed END)
        ORDER BY COALESCE(closed_at, opened_at) DESC, case_key DESC
        LIMIT NULLIF(:'limit', '')::int
      ) x
    ),
    '[]'::json
  )
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Backfill evaluator case-review bundles for resolved/closed cases')
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--include-indexed', action='store_true')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--contract-id', default='yes')
    parser.add_argument('--agent-review', action='store_true')
    parser.add_argument('--memory-upgrade', action='store_true')
    parser.add_argument('--causal-projection', action='store_true')
    parser.add_argument('--session-key', default='agent:evaluator:main')
    parser.add_argument('--agent-id')
    parser.add_argument('--timeout-seconds', type=float, default=480.0)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    db_url = resolve_db_url(args.db_url)
    payload = exec_sql(
        args.psql,
        db_url,
        SQL,
        {
            'include_indexed': 'true' if args.include_indexed else 'false',
            'limit': str(args.limit),
        },
    )
    rows = payload.get('cases') or []
    results: list[dict[str, Any]] = []
    for row in rows:
        case_key = row.get('case_key')
        if not case_key:
            continue
        result = materialize_case_review_bundle(
            case_key,
            contract_id=args.contract_id,
            db_url=db_url,
            psql_bin=args.psql,
            agent_review=args.agent_review,
            memory_upgrade=args.memory_upgrade,
            causal_projection=args.causal_projection,
            session_key=args.session_key,
            agent_id=args.agent_id,
            timeout_seconds=args.timeout_seconds,
        )
        result['already_indexed_before'] = bool(row.get('already_indexed'))
        result['bundle_dir'] = str(case_review_dir(case_key))
        results.append(result)

    output = {
        'ok': True,
        'selected_count': len(rows),
        'materialized_count': len(results),
        'results': results,
    }
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
