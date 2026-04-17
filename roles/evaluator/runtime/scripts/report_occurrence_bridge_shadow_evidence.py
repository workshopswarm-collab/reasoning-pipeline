#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
ORCH_ROOT = SCRIPT_PATH.parents[4]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.io import write_json  # noqa: E402
from lib.occurrence_shadow_bridge import BRIDGE_SOURCE, PROPOSAL_SOURCE  # noqa: E402

OUTPUT_JSON = ORCH_ROOT / 'qualitative-db' / '60-causal-map' / 'generated' / 'occurrence-bridge-shadow-evidence.json'
OUTPUT_MD = OUTPUT_JSON.with_suffix('.md')

REPORT_SQL = r'''
WITH bridge AS (
  SELECT DISTINCT
    o.proposal_id,
    o.proposal_key,
    o.candidate_label,
    o.mechanism_family
  FROM public.proposed_causal_candidate_occurrences o
  WHERE o.proposal_source = :'proposal_source'
    AND COALESCE(o.proposal_metadata->>'bridge_source', '') = :'bridge_source'
),
shadow AS (
  SELECT
    s.proposal_id,
    COUNT(*)::int AS shadow_match_count,
    COUNT(*) FILTER (WHERE NULLIF(s.outcome_label, '') IS NOT NULL)::int AS shadow_judged_count,
    COUNT(*) FILTER (WHERE s.outcome_label = 'helpful' OR s.outcome_favored IS TRUE)::int AS shadow_helpful_count,
    COUNT(*) FILTER (WHERE s.outcome_label = 'harmful')::int AS shadow_harmful_count,
    COUNT(*) FILTER (WHERE s.outcome_label = 'neutral')::int AS shadow_neutral_count,
    COUNT(*) FILTER (WHERE s.outcome_label = 'unclear')::int AS shadow_unclear_count,
    COALESCE(SUM(COALESCE(s.outcome_score, 0)), 0)::numeric AS shadow_score_sum,
    AVG(s.outcome_score)::numeric AS shadow_mean_score,
    COUNT(DISTINCT s.dispatch_id)::int AS distinct_dispatch_count,
    COUNT(DISTINCT s.case_key)::int AS distinct_shadow_case_count,
    MAX(s.judged_at) AS last_judged_at
  FROM public.proposed_causal_shadow_matches s
  JOIN bridge b USING (proposal_id)
  GROUP BY s.proposal_id
)
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY COALESCE(shadow_judged_count, 0) DESC, COALESCE(shadow_match_count, 0) DESC, proposal_id ASC), '[]'::json)::text
FROM (
  SELECT
    b.proposal_id,
    COALESCE(stats.proposal_key, b.proposal_key) AS proposal_key,
    COALESCE(stats.candidate_label, b.candidate_label) AS candidate_label,
    COALESCE(stats.mechanism_family, b.mechanism_family) AS mechanism_family,
    stats.lifecycle_stage,
    stats.promotion_status,
    stats.dominant_proposal_source,
    stats.proposal_source_mix,
    stats.promotion_score,
    stats.distinct_case_count,
    stats.non_intervention_support_case_count,
    stats.merge_recommended,
    stats.merge_candidate_key,
    stats.promotion_blockers,
    COALESCE(shadow.shadow_match_count, 0) AS shadow_match_count,
    COALESCE(shadow.shadow_judged_count, 0) AS shadow_judged_count,
    COALESCE(shadow.shadow_helpful_count, 0) AS shadow_helpful_count,
    COALESCE(shadow.shadow_harmful_count, 0) AS shadow_harmful_count,
    COALESCE(shadow.shadow_neutral_count, 0) AS shadow_neutral_count,
    COALESCE(shadow.shadow_unclear_count, 0) AS shadow_unclear_count,
    COALESCE(shadow.shadow_score_sum, 0) AS shadow_score_sum,
    shadow.shadow_mean_score,
    COALESCE(shadow.distinct_dispatch_count, 0) AS distinct_dispatch_count,
    COALESCE(shadow.distinct_shadow_case_count, 0) AS distinct_shadow_case_count,
    shadow.last_judged_at
  FROM bridge b
  LEFT JOIN public.proposed_causal_candidate_stats stats USING (proposal_id)
  LEFT JOIN shadow USING (proposal_id)
) t;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Report shadow-evidence health for occurrence-bridge proposals')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--include-mixed-source', action='store_true', help='include mixed-source bridge participants in the main reported rows')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')



def sort_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        rows,
        key=lambda row: (
            -int(row.get('shadow_judged_count') or 0),
            -int(row.get('shadow_match_count') or 0),
            -float(row.get('promotion_score') or 0),
            str(row.get('proposal_key') or ''),
        ),
    )



def bridge_membership(record: Mapping[str, Any]) -> str:
    dominant_source = str(record.get('dominant_proposal_source') or '').strip()
    if dominant_source == PROPOSAL_SOURCE:
        return 'bridge_dominant'
    raw_mix = record.get('proposal_source_mix')
    mix = raw_mix if isinstance(raw_mix, dict) else {}
    try:
        bridge_count = int(mix.get(PROPOSAL_SOURCE) or 0)
    except Exception:
        bridge_count = 0
    if bridge_count > 0:
        return 'bridge_participant'
    return 'bridge_unclassified'



def screening_state(record: Mapping[str, Any]) -> str:
    if int(record.get('shadow_positive_count') or 0) > 0:
        return 'positive_shadow_validated'
    if int(record.get('shadow_judged_count') or 0) > 0:
        return 'judged_but_not_positive'
    if int(record.get('shadow_match_count') or 0) > 0:
        return 'pending_positive_shadow_validation'
    return 'no_shadow_matches'



def render_markdown(payload: dict[str, Any]) -> str:
    summary = payload.get('summary') or {}
    lines = [
        '# Occurrence-bridge shadow evidence',
        '',
        '## Summary',
        '',
        f"- generated_at: `{summary.get('generated_at')}`",
        f"- proposal_count: `{summary.get('proposal_count')}`",
        f"- bridge_linked_proposal_count: `{summary.get('bridge_linked_proposal_count')}`",
        f"- suppressed_bridge_participant_count: `{summary.get('suppressed_bridge_participant_count')}`",
        f"- judged_proposal_count: `{summary.get('judged_proposal_count')}`",
        f"- shadow_match_count: `{summary.get('shadow_match_count')}`",
        f"- shadow_judged_count: `{summary.get('shadow_judged_count')}`",
        f"- shadow_helpful_count: `{summary.get('shadow_helpful_count')}`",
        f"- shadow_harmful_count: `{summary.get('shadow_harmful_count')}`",
        f"- bridge_membership_counts: `{summary.get('bridge_membership_counts')}`",
        f"- lifecycle_stage_counts: `{summary.get('lifecycle_stage_counts')}`",
        f"- screening_state_counts: `{summary.get('screening_state_counts')}`",
        '',
        '## Proposals',
        '',
    ]
    rows = payload.get('rows') or []
    if not rows:
        lines.append('- none')
    else:
        for row in rows[:40]:
            lines.append(
                f"- `{row.get('proposal_key')}` [{row.get('mechanism_family')}] — bridge=`{row.get('bridge_membership')}`; stage=`{row.get('lifecycle_stage')}`; promotion=`{row.get('promotion_status')}`; screening=`{row.get('screening_state')}`; shadow={row.get('shadow_match_count')}/{row.get('shadow_judged_count')}; helpful=`{row.get('shadow_helpful_count')}`; harmful=`{row.get('shadow_harmful_count')}`; mean=`{row.get('shadow_mean_score')}`"
            )
            blockers = row.get('promotion_blockers') or []
            if blockers:
                lines.append(f"  - blockers: {', '.join(blockers[:6])}")
    suppressed_rows = payload.get('suppressed_rows') or []
    if suppressed_rows:
        lines.extend([
            '',
            '## Suppressed mixed-source bridge participants',
            '',
        ])
        for row in suppressed_rows[:20]:
            lines.append(
                f"- `{row.get('proposal_key')}` — dominant=`{row.get('dominant_proposal_source')}`; bridge=`{row.get('bridge_membership')}`; stage=`{row.get('lifecycle_stage')}`; promotion=`{row.get('promotion_status')}`"
            )
    lines.append('')
    return '\n'.join(lines)



def main() -> int:
    args = parse_args()
    db_url = resolve_db_url(args.db_url)
    rows: list[dict[str, Any]] = []
    warning: str | None = None
    if not db_url:
        warning = 'db_url_unavailable'
    elif not table_exists('proposed_causal_candidate_occurrences', db_url=db_url, psql_bin=args.psql):
        warning = 'proposed_causal_candidate_occurrences table missing'
    elif not table_exists('proposed_causal_shadow_matches', db_url=db_url, psql_bin=args.psql):
        warning = 'proposed_causal_shadow_matches table missing'
    elif not table_exists('proposed_causal_candidate_stats', db_url=db_url, psql_bin=args.psql):
        warning = 'proposed_causal_candidate_stats table missing'
    else:
        result = exec_sql(
            args.psql,
            db_url,
            REPORT_SQL,
            {'proposal_source': PROPOSAL_SOURCE, 'bridge_source': BRIDGE_SOURCE},
        ) or []
        rows = result if isinstance(result, list) else []

    normalized = []
    for raw_row in sort_rows([row for row in rows if isinstance(row, dict)]):
        row = dict(raw_row)
        row['bridge_membership'] = bridge_membership(row)
        row['screening_state'] = screening_state(row)
        normalized.append(row)

    reported_rows = normalized if args.include_mixed_source else [
        row for row in normalized if row.get('bridge_membership') == 'bridge_dominant'
    ]
    suppressed_rows = [] if args.include_mixed_source else [
        row for row in normalized if row.get('bridge_membership') == 'bridge_participant'
    ]

    lifecycle_stage_counts: dict[str, int] = {}
    screening_state_counts: dict[str, int] = {}
    bridge_membership_counts: dict[str, int] = {}
    shadow_match_count = 0
    shadow_judged_count = 0
    shadow_helpful_count = 0
    shadow_harmful_count = 0
    for row in reported_rows:
        lifecycle = str(row.get('lifecycle_stage') or 'unknown')
        lifecycle_stage_counts[lifecycle] = lifecycle_stage_counts.get(lifecycle, 0) + 1
        membership = str(row.get('bridge_membership') or 'bridge_unclassified')
        bridge_membership_counts[membership] = bridge_membership_counts.get(membership, 0) + 1
        shadow_match_count += int(row.get('shadow_match_count') or 0)
        shadow_judged_count += int(row.get('shadow_judged_count') or 0)
        shadow_helpful_count += int(row.get('shadow_helpful_count') or 0)
        shadow_harmful_count += int(row.get('shadow_harmful_count') or 0)
        current_screening_state = str(row.get('screening_state') or 'unknown')
        screening_state_counts[current_screening_state] = screening_state_counts.get(current_screening_state, 0) + 1

    all_bridge_membership_counts: dict[str, int] = {}
    for row in normalized:
        membership = str(row.get('bridge_membership') or 'bridge_unclassified')
        all_bridge_membership_counts[membership] = all_bridge_membership_counts.get(membership, 0) + 1

    payload = {
        'summary': {
            'generated_at': now_iso(),
            'proposal_source': PROPOSAL_SOURCE,
            'bridge_source': BRIDGE_SOURCE,
            'proposal_count': len(reported_rows),
            'bridge_linked_proposal_count': len(normalized),
            'suppressed_bridge_participant_count': len(suppressed_rows),
            'judged_proposal_count': sum(1 for row in reported_rows if int(row.get('shadow_judged_count') or 0) > 0),
            'shadow_match_count': shadow_match_count,
            'shadow_judged_count': shadow_judged_count,
            'shadow_helpful_count': shadow_helpful_count,
            'shadow_harmful_count': shadow_harmful_count,
            'bridge_membership_counts': all_bridge_membership_counts,
            'reported_bridge_membership_counts': bridge_membership_counts,
            'lifecycle_stage_counts': lifecycle_stage_counts,
            'screening_state_counts': screening_state_counts,
        },
        'rows': reported_rows,
        'suppressed_rows': suppressed_rows[:25],
    }
    if warning:
        payload['warning'] = warning
    if not args.dry_run:
        OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        write_json(OUTPUT_JSON, payload, pretty=True)
        OUTPUT_MD.write_text(render_markdown(payload) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
