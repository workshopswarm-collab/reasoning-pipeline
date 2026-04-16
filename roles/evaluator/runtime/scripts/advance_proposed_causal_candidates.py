#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402

AGGREGATE_SCRIPT = SCRIPT_PATH.parent / 'aggregate_causal_candidate_proposals.py'

STATS_ROWS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY proposal_id), '[]'::json)::text
FROM (
  SELECT proposal_id, lifecycle_stage, promotion_status, stage_entered_at
  FROM public.proposed_causal_candidate_stats
) t;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run deterministic proposal advancement and report lifecycle-stage transitions')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def load_stats_snapshot(*, db_url: str, psql_bin: str) -> dict[str, dict[str, Any]]:
    resolved_db_url = resolve_db_url(db_url)
    if not resolved_db_url:
        return {}
    if not table_exists('proposed_causal_candidate_stats', db_url=resolved_db_url, psql_bin=psql_bin):
        return {}
    rows = exec_sql(psql_bin, resolved_db_url, STATS_ROWS_SQL, {})
    if not isinstance(rows, list):
        return {}
    return {str(row.get('proposal_id') or ''): row for row in rows if isinstance(row, dict) and str(row.get('proposal_id') or '').strip()}



def main() -> int:
    args = parse_args()
    before = load_stats_snapshot(db_url=args.db_url, psql_bin=args.psql)

    cmd = [sys.executable, str(AGGREGATE_SCRIPT), '--psql', args.psql]
    if args.db_url:
        cmd.extend(['--db-url', args.db_url])
    if args.dry_run:
        cmd.append('--dry-run')
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.strip() or proc.stdout.strip() or 'aggregate_causal_candidate_proposals.py failed')
    try:
        payload = json.loads(proc.stdout)
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f'failed to parse aggregate output: {exc}')

    proposals = payload.get('proposals') or []
    after_map = {str(row.get('proposal_id') or ''): row for row in proposals if isinstance(row, dict) and str(row.get('proposal_id') or '').strip()}

    transitions: list[dict[str, Any]] = []
    for proposal_id, row in sorted(after_map.items()):
        before_row = before.get(proposal_id) or {}
        before_stage = str(before_row.get('lifecycle_stage') or '').strip() or None
        after_stage = str(row.get('lifecycle_stage') or '').strip() or None
        before_status = str(before_row.get('promotion_status') or '').strip() or None
        after_status = str(row.get('promotion_status') or '').strip() or None
        if before_stage != after_stage or before_status != after_status:
            transitions.append(
                {
                    'proposal_id': proposal_id,
                    'proposal_key': row.get('proposal_key'),
                    'before_stage': before_stage,
                    'after_stage': after_stage,
                    'before_status': before_status,
                    'after_status': after_status,
                    'trial_readiness': row.get('trial_readiness') or {},
                    'promotion_readiness': row.get('promotion_readiness') or {},
                }
            )

    output = {
        'ok': True,
        'dry_run': args.dry_run,
        'proposal_count': len(proposals),
        'proposal_stage_counts': dict(Counter(str(row.get('lifecycle_stage') or 'unknown') for row in proposals)),
        'trial_candidate_ids': [row.get('proposal_id') for row in proposals if str(row.get('lifecycle_stage') or '') == 'trial_candidate'],
        'promotion_ready_ids': [row.get('proposal_id') for row in proposals if str(row.get('lifecycle_stage') or '') == 'promotion_ready'],
        'trial_eligible_ids': [row.get('proposal_id') for row in proposals if bool((row.get('trial_readiness') or {}).get('eligible'))],
        'promotion_ready_eligible_ids': [row.get('proposal_id') for row in proposals if bool((row.get('promotion_readiness') or {}).get('eligible'))],
        'transition_count': len(transitions),
        'transitions': transitions,
        'summary_path': payload.get('summary_path'),
        'index_path': payload.get('index_path'),
    }
    if payload.get('warning'):
        output['warning'] = payload['warning']
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
