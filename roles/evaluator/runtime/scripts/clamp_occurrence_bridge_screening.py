#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.occurrence_shadow_bridge import BRIDGE_SOURCE, PROPOSAL_SOURCE  # noqa: E402

SELECT_SQL = r'''
WITH judged AS (
  SELECT
    proposal_id,
    COUNT(*) FILTER (WHERE NULLIF(outcome_label, '') IS NOT NULL)::int AS shadow_judged_count
  FROM public.proposed_causal_shadow_matches
  GROUP BY proposal_id
)
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY shadow_match_count DESC, proposal_key), '[]'::json)::text
FROM (
  SELECT
    stats.proposal_id,
    stats.proposal_key,
    stats.mechanism_family,
    stats.lifecycle_stage,
    stats.promotion_status,
    stats.shadow_match_count,
    COALESCE(judged.shadow_judged_count, 0) AS shadow_judged_count,
    stats.shadow_positive_count,
    stats.promotion_score
  FROM public.proposed_causal_candidate_stats stats
  LEFT JOIN judged USING (proposal_id)
  WHERE stats.dominant_proposal_source = :'proposal_source'
    AND COALESCE(stats.shadow_positive_count, 0) <= 0
) t;
'''

CLAMP_SQL = r'''
WITH judged AS (
  SELECT
    proposal_id,
    COUNT(*) FILTER (WHERE NULLIF(outcome_label, '') IS NOT NULL)::int AS shadow_judged_count
  FROM public.proposed_causal_shadow_matches
  GROUP BY proposal_id
), candidates AS (
  SELECT
    stats.proposal_id,
    COALESCE(judged.shadow_judged_count, 0) AS shadow_judged_count,
    CASE
      WHEN COALESCE(stats.shadow_match_count, 0) > 0
       AND COALESCE(judged.shadow_judged_count, 0) > 0
       AND COALESCE(stats.shadow_positive_count, 0) <= 0
      THEN 'aggregated'
      ELSE stats.lifecycle_stage
    END AS next_lifecycle_stage
  FROM public.proposed_causal_candidate_stats stats
  LEFT JOIN judged USING (proposal_id)
  WHERE stats.dominant_proposal_source = :'proposal_source'
    AND COALESCE(stats.shadow_positive_count, 0) <= 0
), updated AS (
  UPDATE public.proposed_causal_candidate_stats stats
  SET promotion_status = 'not_trial_candidate',
      promotion_score = 0.0,
      lifecycle_stage = candidates.next_lifecycle_stage,
      stage_entered_at = CASE
        WHEN stats.lifecycle_stage IS DISTINCT FROM candidates.next_lifecycle_stage
        THEN NOW()
        ELSE stats.stage_entered_at
      END
  FROM candidates
  WHERE stats.proposal_id = candidates.proposal_id
  RETURNING json_build_object(
    'proposal_id', stats.proposal_id,
    'proposal_key', stats.proposal_key,
    'mechanism_family', stats.mechanism_family,
    'lifecycle_stage', stats.lifecycle_stage,
    'promotion_status', stats.promotion_status,
    'shadow_match_count', stats.shadow_match_count,
    'shadow_judged_count', candidates.shadow_judged_count,
    'shadow_positive_count', stats.shadow_positive_count,
    'promotion_score', stats.promotion_score
  ) AS row_json
)
SELECT COALESCE(json_agg(row_json), '[]'::json)::text
FROM updated;
'''


def clamped_lifecycle_stage(record: Mapping[str, Any]) -> str:
    lifecycle_stage = str(record.get('lifecycle_stage') or 'aggregated')
    shadow_match_count = int(record.get('shadow_match_count') or 0)
    shadow_judged_count = int(record.get('shadow_judged_count') or 0)
    shadow_positive_count = int(record.get('shadow_positive_count') or 0)
    if shadow_match_count > 0 and shadow_judged_count > 0 and shadow_positive_count <= 0:
        return 'aggregated'
    return lifecycle_stage


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Clamp occurrence-bridge proposal maturity until positive judged shadow evidence exists')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def main() -> int:
    args = parse_args()
    db_url = resolve_db_url(args.db_url)
    output: dict[str, Any] = {
        'ok': True,
        'proposal_source': PROPOSAL_SOURCE,
        'bridge_source': BRIDGE_SOURCE,
        'clamped_rows': [],
    }
    if not db_url:
        output['warning'] = 'db_url_unavailable'
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0
    if not table_exists('proposed_causal_candidate_stats', db_url=db_url, psql_bin=args.psql):
        output['warning'] = 'proposed_causal_candidate_stats table missing'
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0
    if not table_exists('proposed_causal_shadow_matches', db_url=db_url, psql_bin=args.psql):
        output['warning'] = 'proposed_causal_shadow_matches table missing'
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    rows = exec_sql(args.psql, db_url, SELECT_SQL, {'proposal_source': PROPOSAL_SOURCE}) or []
    if not isinstance(rows, list):
        rows = []
    normalized_rows: list[dict[str, Any]] = []
    for raw_row in rows:
        if not isinstance(raw_row, dict):
            continue
        row = dict(raw_row)
        row['clamped_lifecycle_stage'] = clamped_lifecycle_stage(row)
        normalized_rows.append(row)
    output['candidate_count'] = len(normalized_rows)
    output['sample'] = normalized_rows[:25]

    if not args.dry_run:
        clamped_rows = exec_sql(args.psql, db_url, CLAMP_SQL, {'proposal_source': PROPOSAL_SOURCE}) or []
        output['clamped_rows'] = clamped_rows if isinstance(clamped_rows, list) else []
    output['clamped_count'] = len(output['clamped_rows']) if not args.dry_run else len(normalized_rows)
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
