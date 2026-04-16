#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
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
from lib.lmd_causal_runtime import SHADOW_VS_LIVE_JSON, coerce_string, safe_int  # noqa: E402

OUTPUT_JSON = SHADOW_VS_LIVE_JSON
OUTPUT_MD = OUTPUT_JSON.with_suffix('.md')

REPORT_SQL = r'''
WITH trial AS (
  SELECT
    proposal_id,
    COUNT(*)::int AS trial_exposure_count,
    COUNT(*) FILTER (WHERE preview_only IS TRUE)::int AS trial_preview_count,
    COUNT(*) FILTER (WHERE injected IS TRUE)::int AS trial_injected_count,
    COUNT(*) FILTER (WHERE COALESCE(outcome_label, '') = 'helpful')::int AS trial_helpful_count,
    COUNT(*) FILTER (WHERE COALESCE(outcome_label, '') = 'harmful')::int AS trial_harmful_count,
    COUNT(*) FILTER (WHERE NULLIF(outcome_label, '') IS NOT NULL)::int AS trial_judged_count
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
    s.shadow_match_count,
    s.shadow_positive_count,
    COALESCE(t.trial_exposure_count, 0) AS trial_exposure_count,
    COALESCE(t.trial_preview_count, 0) AS trial_preview_count,
    COALESCE(t.trial_injected_count, 0) AS trial_injected_count,
    COALESCE(t.trial_helpful_count, 0) AS trial_helpful_count,
    COALESCE(t.trial_harmful_count, 0) AS trial_harmful_count,
    COALESCE(t.trial_judged_count, 0) AS trial_judged_count,
    s.merge_recommended,
    s.merge_candidate_key
  FROM public.proposed_causal_candidate_stats s
  LEFT JOIN trial t USING (proposal_id)
  WHERE s.shadow_match_count > 0
     OR COALESCE(t.trial_exposure_count, 0) > 0
  ORDER BY COALESCE(t.trial_exposure_count, 0) DESC, s.shadow_match_count DESC, s.proposal_id ASC
) t;
'''



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Compare proposal-layer shadow support against live trial exposure state')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()



def classify_row(row: dict[str, Any]) -> str:
    trial_injected = safe_int(row.get('trial_injected_count'))
    trial_preview = safe_int(row.get('trial_preview_count'))
    shadow_positive = safe_int(row.get('shadow_positive_count'))
    if trial_injected > 0:
        return 'trial_injected'
    if trial_preview > 0:
        return 'trial_preview_only'
    if shadow_positive > 0:
        return 'shadow_positive_only'
    return 'shadow_only'



def render_markdown(payload: dict[str, Any]) -> str:
    summary = payload.get('summary') or {}
    lines = [
        '# Proposed causal shadow vs live',
        '',
        '## Summary',
        '',
        f"- generated_at: `{summary.get('generated_at')}`",
        f"- proposal_count: `{summary.get('proposal_count')}`",
        f"- mode_counts: `{summary.get('mode_counts')}`",
        '',
        '## Proposals',
        '',
    ]
    for row in payload.get('rows') or []:
        lines.append(
            f"- `{row.get('proposal_id')}` [{row.get('mechanism_family')}] — mode={row.get('comparison_mode')}; shadow={row.get('shadow_match_count')}/{row.get('shadow_positive_count')}; preview={row.get('trial_preview_count')}; injected={row.get('trial_injected_count')}; judged={row.get('trial_judged_count')}"
        )
    if not (payload.get('rows') or []):
        lines.append('- none')
    lines.append('')
    return '\n'.join(lines)



def main() -> int:
    args = parse_args()
    db_url = resolve_db_url(args.db_url)
    rows = []
    if db_url and table_exists('proposed_causal_candidate_stats', db_url=db_url, psql_bin=args.psql):
        result = exec_sql(args.psql, db_url, REPORT_SQL, {}) or []
        rows = result if isinstance(result, list) else []
    normalized = []
    mode_counts: dict[str, int] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        mode = classify_row(row)
        mode_counts[mode] = mode_counts.get(mode, 0) + 1
        normalized.append({
            **row,
            'comparison_mode': mode,
        })
    payload = {
        'summary': {
            'generated_at': now_iso(),
            'proposal_count': len(normalized),
            'mode_counts': mode_counts,
        },
        'rows': normalized,
    }
    if not args.dry_run:
        OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        write_json(OUTPUT_JSON, payload, pretty=True)
        OUTPUT_MD.write_text(render_markdown(payload) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
