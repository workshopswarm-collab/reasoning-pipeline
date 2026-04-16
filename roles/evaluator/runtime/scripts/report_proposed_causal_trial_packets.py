#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.io import write_json  # noqa: E402
from lib.lmd_causal_runtime import TRIAL_PACKETS_JSON, coerce_string, safe_int  # noqa: E402

OUTPUT_JSON = TRIAL_PACKETS_JSON
OUTPUT_MD = OUTPUT_JSON.with_suffix('.md')
OUTPUT_DIR = OUTPUT_JSON.parent / 'trial-packets'

PACKETS_SQL = r'''
WITH trial AS (
  SELECT
    proposal_id,
    COUNT(*)::int AS trial_exposure_count,
    COUNT(*) FILTER (WHERE preview_only IS TRUE)::int AS trial_preview_count,
    COUNT(*) FILTER (WHERE NULLIF(outcome_label, '') IS NOT NULL)::int AS trial_judged_count,
    COUNT(*) FILTER (WHERE COALESCE(outcome_label, '') = 'helpful')::int AS trial_helpful_count,
    COUNT(*) FILTER (WHERE COALESCE(outcome_label, '') = 'harmful')::int AS trial_harmful_count
  FROM public.proposed_causal_trial_exposures
  GROUP BY proposal_id
)
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY proposal_id), '[]'::json)::text
FROM (
  SELECT
    s.proposal_id,
    s.mechanism_family,
    s.lifecycle_stage,
    s.promotion_status,
    s.distinct_case_count,
    s.shadow_match_count,
    s.shadow_positive_count,
    s.merge_recommended,
    s.merge_candidate_key,
    s.near_live_graph_keys,
    s.promotion_blockers,
    COALESCE(t.trial_exposure_count, 0) AS trial_exposure_count,
    COALESCE(t.trial_preview_count, 0) AS trial_preview_count,
    COALESCE(t.trial_judged_count, 0) AS trial_judged_count,
    COALESCE(t.trial_helpful_count, 0) AS trial_helpful_count,
    COALESCE(t.trial_harmful_count, 0) AS trial_harmful_count
  FROM public.proposed_causal_candidate_stats s
  LEFT JOIN trial t USING (proposal_id)
  WHERE s.lifecycle_stage IN ('trial_candidate', 'promotion_ready')
     OR s.shadow_match_count > 0
     OR COALESCE(t.trial_exposure_count, 0) > 0
  ORDER BY COALESCE(t.trial_exposure_count, 0) DESC, s.shadow_match_count DESC, s.proposal_id ASC
) t;
'''



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate structured trial packets for proposal-layer causal candidates')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()



def slugify(value: str) -> str:
    text = re.sub(r'[^A-Za-z0-9]+', '-', coerce_string(value)).strip('-').lower()
    return text or 'proposal'



def packet_from_row(row: dict[str, Any]) -> dict[str, Any]:
    proposal_id = coerce_string(row.get('proposal_id'))
    candidate_type, _, proposal_key = proposal_id.partition(':')
    blockers = row.get('promotion_blockers') if isinstance(row.get('promotion_blockers'), list) else []
    near_live = row.get('near_live_graph_keys') if isinstance(row.get('near_live_graph_keys'), list) else []
    trial_exposure_count = safe_int(row.get('trial_exposure_count'))
    packet = {
        'generated_at': now_iso(),
        'proposal_id': proposal_id,
        'proposal_key': proposal_key or proposal_id,
        'candidate_type': candidate_type or 'unknown',
        'mechanism_family': row.get('mechanism_family') or 'unassigned',
        'lifecycle_stage': row.get('lifecycle_stage'),
        'promotion_status': row.get('promotion_status'),
        'hypothesis': proposal_key.replace('-', ' ') if proposal_key else proposal_id,
        'expected_helpful_context': near_live,
        'expected_failure_mode': blockers[:3],
        'evidence': {
            'distinct_case_count': safe_int(row.get('distinct_case_count')),
            'shadow_match_count': safe_int(row.get('shadow_match_count')),
            'shadow_positive_count': safe_int(row.get('shadow_positive_count')),
            'trial_exposure_count': trial_exposure_count,
            'trial_preview_count': safe_int(row.get('trial_preview_count')),
            'trial_judged_count': safe_int(row.get('trial_judged_count')),
            'trial_helpful_count': safe_int(row.get('trial_helpful_count')),
            'trial_harmful_count': safe_int(row.get('trial_harmful_count')),
        },
        'blockers': blockers,
        'merge_recommended': bool(row.get('merge_recommended', False)),
        'merge_candidate_key': row.get('merge_candidate_key'),
        'notes': {
            'eligibility_signal': 'trial_live' if trial_exposure_count > 0 else ('shadow_only' if safe_int(row.get('shadow_match_count')) > 0 else 'candidate_only'),
        },
    }
    return packet



def render_packet_markdown(packet: dict[str, Any]) -> str:
    evidence = packet.get('evidence') or {}
    lines = [
        f"# Trial packet — {packet.get('proposal_id')}",
        '',
        f"- generated_at: `{packet.get('generated_at')}`",
        f"- mechanism_family: `{packet.get('mechanism_family')}`",
        f"- lifecycle_stage: `{packet.get('lifecycle_stage')}`",
        f"- promotion_status: `{packet.get('promotion_status')}`",
        f"- candidate_type: `{packet.get('candidate_type')}`",
        f"- merge_recommended: `{packet.get('merge_recommended')}`",
        f"- merge_candidate_key: `{packet.get('merge_candidate_key')}`",
        '',
        '## Evidence',
        '',
        f"- distinct_case_count: `{evidence.get('distinct_case_count')}`",
        f"- shadow_match_count: `{evidence.get('shadow_match_count')}`",
        f"- shadow_positive_count: `{evidence.get('shadow_positive_count')}`",
        f"- trial_exposure_count: `{evidence.get('trial_exposure_count')}`",
        f"- trial_preview_count: `{evidence.get('trial_preview_count')}`",
        f"- trial_judged_count: `{evidence.get('trial_judged_count')}`",
        '',
        '## Expected helpful context',
        '',
    ]
    helpful = packet.get('expected_helpful_context') or []
    if helpful:
        for item in helpful:
            lines.append(f"- `{item}`")
    else:
        lines.append('- none surfaced')
    lines.extend(['', '## Blockers / failure modes', ''])
    blockers = packet.get('blockers') or []
    if blockers:
        for item in blockers:
            lines.append(f"- `{item}`")
    else:
        lines.append('- none')
    lines.append('')
    return '\n'.join(lines)



def main() -> int:
    args = parse_args()
    db_url = resolve_db_url(args.db_url)
    rows = []
    if db_url and table_exists('proposed_causal_candidate_stats', db_url=db_url, psql_bin=args.psql):
        result = exec_sql(args.psql, db_url, PACKETS_SQL, {}) or []
        rows = result if isinstance(result, list) else []
    packets = [packet_from_row(row) for row in rows if isinstance(row, dict)]
    if not args.dry_run:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        for packet in packets:
            stem = slugify(coerce_string(packet.get('proposal_id')))
            write_json(OUTPUT_DIR / f'{stem}.json', packet, pretty=True)
            (OUTPUT_DIR / f'{stem}.md').write_text(render_packet_markdown(packet) + '\n', encoding='utf-8')

    payload = {
        'summary': {
            'generated_at': now_iso(),
            'packet_count': len(packets),
            'output_dir': str(OUTPUT_DIR),
        },
        'packets': packets,
    }
    if not args.dry_run:
        OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        write_json(OUTPUT_JSON, payload, pretty=True)
        OUTPUT_MD.write_text(
            '# Proposed causal trial packets\n\n' + '\n'.join(f"- `{packet.get('proposal_id')}` → `trial-packets/{slugify(coerce_string(packet.get('proposal_id')))}.md`" for packet in packets) + ('\n' if packets else '\n- none\n'),
            encoding='utf-8',
        )
    print(json.dumps(payload, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
