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

from lib.db import DEFAULT_PSQL  # noqa: E402
from lib.io import write_json  # noqa: E402
from lib.lmd_causal_runtime import (  # noqa: E402
    POST_TREATMENT_REPORT_JSON,
    RECONCILIATION_JSON,
    TRIGGER_RETRY_QUEUE_PATH,
    audit_path_for_bundle,
    coerce_string,
    read_json_lines,
    read_report_generated_at,
    safe_int,
)
from run_post_treatment_causal_feedback_cycle import build_cycle_audit, load_treatment_cycles, parse_iso  # noqa: E402

OUTPUT_JSON = RECONCILIATION_JSON
OUTPUT_MD = OUTPUT_JSON.with_suffix('.md')
DEFAULT_EXPERIMENT_ID = 'researcher-lmd-v1'
DEFAULT_RECENT_TREATMENT_CASES = 50



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Reconcile recent LMD/causal runtime state against bundles, exposure logs, and freshness artifacts')
    parser.add_argument('--experiment-id', default=DEFAULT_EXPERIMENT_ID)
    parser.add_argument('--recent-treatment-cases', type=int, default=DEFAULT_RECENT_TREATMENT_CASES)
    parser.add_argument('--case-key', action='append', default=[])
    parser.add_argument('--dispatch-id', action='append', default=[])
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()



def unique(items: list[str]) -> set[str]:
    return {coerce_string(item) for item in items if coerce_string(item)}



def latest_signal_at(audits: list[dict[str, Any]]) -> str | None:
    candidates = []
    for audit in audits:
        for key in ['last_exposure_at', 'trial_last_exposure_at', 'review_updated_at']:
            parsed = parse_iso(audit.get(key))
            if parsed is not None:
                candidates.append(parsed)
    if not candidates:
        return None
    return max(candidates).isoformat()



def render_markdown(payload: dict[str, Any]) -> str:
    summary = payload.get('summary') or {}
    cycles = payload.get('cycles') or []
    queue = payload.get('retry_queue') or []
    lines = [
        '# LMD / causal runtime reconciliation',
        '',
        '## Summary',
        '',
        f"- generated_at: `{summary.get('generated_at')}`",
        f"- cycle_count: `{summary.get('cycle_count')}`",
        f"- cycles_with_warnings_count: `{summary.get('cycles_with_warnings_count')}`",
        f"- unresolved_cycle_count: `{summary.get('unresolved_cycle_count')}`",
        f"- missing_bundle_count: `{summary.get('missing_bundle_count')}`",
        f"- missing_audit_file_count: `{summary.get('missing_audit_file_count')}`",
        f"- lmd_row_mismatch_count: `{summary.get('lmd_row_mismatch_count')}`",
        f"- trial_row_mismatch_count: `{summary.get('trial_row_mismatch_count')}`",
        f"- retry_queue_depth: `{summary.get('retry_queue_depth')}`",
        f"- post_treatment_report_generated_at: `{summary.get('post_treatment_report_generated_at')}`",
        f"- latest_relevant_signal_at: `{summary.get('latest_relevant_signal_at')}`",
        f"- post_treatment_report_stale: `{summary.get('post_treatment_report_stale')}`",
        '',
        '## Warning cycles',
        '',
    ]
    warning_cycles = [row for row in cycles if row.get('warnings')]
    if not warning_cycles:
        lines.append('- none')
    else:
        for row in warning_cycles[:20]:
            lines.append(
                f"- `{row.get('case_key')}` / `{row.get('dispatch_id')}` — warnings={', '.join(row.get('warnings') or [])}; bundle_found={row.get('bundle_found')}; audit_file_present={row.get('audit_file_present')}"
            )
    lines.extend(['', '## Pending retry queue', ''])
    if not queue:
        lines.append('- empty')
    else:
        for row in queue[:20]:
            lines.append(
                f"- `{row.get('case_key')}` / `{row.get('dispatch_id')}` — source={row.get('trigger_source')}; queued_at={row.get('queued_at')}; error={row.get('cycle_error')}"
            )
    lines.append('')
    return '\n'.join(lines)



def main() -> int:
    args = parse_args()
    cycles = load_treatment_cycles(
        db_url=args.db_url,
        psql_bin=args.psql,
        experiment_id=args.experiment_id,
        case_keys=unique(args.case_key),
        dispatch_ids=unique(args.dispatch_id),
        recent_limit=max(0, int(args.recent_treatment_cases)),
    )
    audits = [build_cycle_audit(cycle) for cycle in cycles]
    for audit in audits:
        bundle_path = coerce_string(audit.get('bundle_path'))
        audit_path = audit_path_for_bundle(bundle_path) if bundle_path else None
        audit['audit_file_path'] = str(audit_path) if audit_path is not None else None
        audit['audit_file_present'] = bool(audit_path and audit_path.exists())

    queue_rows = read_json_lines(TRIGGER_RETRY_QUEUE_PATH)
    latest_signal = latest_signal_at(audits)
    report_generated_at = read_report_generated_at(POST_TREATMENT_REPORT_JSON)
    report_generated_dt = parse_iso(report_generated_at)
    latest_signal_dt = parse_iso(latest_signal)
    report_stale = bool(report_generated_dt and latest_signal_dt and report_generated_dt < latest_signal_dt)

    summary = {
        'generated_at': now_iso(),
        'cycle_count': len(audits),
        'cycles_with_warnings_count': sum(1 for audit in audits if audit.get('warnings')),
        'unresolved_cycle_count': sum(1 for audit in audits if audit.get('resolution_status') != 'resolved'),
        'missing_bundle_count': sum(1 for audit in audits if not audit.get('bundle_found')),
        'missing_audit_file_count': sum(1 for audit in audits if not audit.get('audit_file_present')),
        'lmd_row_mismatch_count': sum(1 for audit in audits if 'lmd_exposure_row_count_mismatch' in (audit.get('warnings') or [])),
        'trial_row_mismatch_count': sum(
            1
            for audit in audits
            if 'trial_exposure_row_count_mismatch' in (audit.get('warnings') or []) or 'trial_injected_row_count_mismatch' in (audit.get('warnings') or [])
        ),
        'retry_queue_depth': len(queue_rows),
        'post_treatment_report_generated_at': report_generated_at,
        'latest_relevant_signal_at': latest_signal,
        'post_treatment_report_stale': report_stale,
    }
    payload = {
        'summary': summary,
        'cycles': audits,
        'retry_queue': queue_rows,
    }
    if not args.dry_run:
        OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        write_json(OUTPUT_JSON, payload, pretty=True)
        OUTPUT_MD.write_text(render_markdown(payload) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
