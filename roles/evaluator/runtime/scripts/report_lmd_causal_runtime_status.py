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
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.io import write_json  # noqa: E402
from lib.lmd_causal_runtime import (  # noqa: E402
    GOVERNANCE_JSON,
    PHASE11_REPORT_JSON,
    POST_TREATMENT_REPORT_JSON,
    RECONCILIATION_JSON,
    SHADOW_VS_LIVE_JSON,
    STATUS_JSON,
    TRIAL_PACKETS_JSON,
    TRIGGER_RETRY_QUEUE_PATH,
    coerce_string,
    load_audit_rows,
    read_json_lines,
    read_report_generated_at,
)

OUTPUT_JSON = STATUS_JSON
OUTPUT_MD = OUTPUT_JSON.with_suffix('.md')

ASSIGNMENTS_BY_ARM_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY arm), '[]'::json)::text
FROM (
  SELECT arm, COUNT(*)::int AS count
  FROM public.lmd_experiment_assignments
  GROUP BY arm
) t;
'''

EXPOSURES_BY_ARM_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY arm), '[]'::json)::text
FROM (
  SELECT arm, COUNT(*)::int AS count
  FROM public.lmd_bundle_exposures
  GROUP BY arm
) t;
'''

TRIAL_MODES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY overlay_mode), '[]'::json)::text
FROM (
  SELECT overlay_mode, COUNT(*)::int AS count
  FROM public.proposed_causal_trial_exposures
  GROUP BY overlay_mode
) t;
'''

PROPOSAL_FUNNEL_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY lifecycle_stage, promotion_status), '[]'::json)::text
FROM (
  SELECT lifecycle_stage, promotion_status, COUNT(*)::int AS count
  FROM public.proposed_causal_candidate_stats
  GROUP BY lifecycle_stage, promotion_status
) t;
'''

LIVE_NODES_STAGE_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY lifecycle_stage), '[]'::json)::text
FROM (
  SELECT lifecycle_stage, COUNT(*)::int AS count
  FROM public.causal_nodes
  GROUP BY lifecycle_stage
) t;
'''

LIVE_EDGES_STAGE_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY lifecycle_stage), '[]'::json)::text
FROM (
  SELECT lifecycle_stage, COUNT(*)::int AS count
  FROM public.causal_edges
  GROUP BY lifecycle_stage
) t;
'''

OPEN_GRAPH_VIOLATIONS_SQL = r'''
SELECT COUNT(*)::int AS count
FROM public.causal_graph_health_violations
WHERE COALESCE(NULLIF(status, ''), 'open') NOT IN ('resolved', 'closed');
'''

RESOLVED_TREATMENT_CASES_SQL = r'''
SELECT COUNT(DISTINCT e.case_key)::int AS count
FROM public.lmd_bundle_exposures e
JOIN public.learning_case_reviews r USING (case_key)
WHERE e.arm = 'treatment'
  AND COALESCE(r.resolution_status, '') = 'resolved';
'''

CANDIDATE_OUTCOME_LEDGER_SQL = r'''
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
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT
    s.proposal_id,
    s.mechanism_family,
    s.lifecycle_stage,
    s.promotion_status,
    s.distinct_case_count,
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
  ORDER BY COALESCE(t.trial_exposure_count, 0) DESC, s.shadow_match_count DESC, s.proposal_id ASC
  LIMIT 20
) t;
'''



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate a compact runtime status report for the embedded LMD + causal map system')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()



def fetch_json_rows(psql_bin: str, db_url: str, table_name: str, sql: str) -> list[dict[str, Any]]:
    if not table_exists(table_name, db_url=db_url, psql_bin=psql_bin):
        return []
    rows = exec_sql(psql_bin, db_url, sql, {}) or []
    return rows if isinstance(rows, list) else []



def fetch_scalar_count(psql_bin: str, db_url: str, table_name: str, sql: str) -> int:
    if not table_exists(table_name, db_url=db_url, psql_bin=psql_bin):
        return 0
    result = exec_sql(psql_bin, db_url, sql, {}) or 0
    if isinstance(result, dict):
        try:
            return int(result.get('count') or 0)
        except Exception:
            return 0
    try:
        return int(result)
    except Exception:
        return 0



def rows_to_count_map(rows: list[dict[str, Any]], key: str = 'arm') -> dict[str, int]:
    out: dict[str, int] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        out[coerce_string(row.get(key)) or 'unknown'] = int(row.get('count') or 0)
    return out



def audit_counters(audits: list[dict[str, Any]]) -> dict[str, Any]:
    coverage_counts = Counter(str(((audit.get('coverage') or {}).get('classification') or 'unknown')) for audit in audits)
    case_mix_counts = Counter()
    pending = []
    coverage_gaps = []
    control_previews = 0
    for audit in audits:
        if audit.get('counterfactual_treatment_preview'):
            control_previews += 1
        for tag in ((audit.get('case_mix') or {}).get('tags') or []):
            case_mix_counts[str(tag)] += 1
        if str(audit.get('assignment_arm') or '').strip().lower() == 'treatment' and not ((audit.get('runtime') or {}).get('post_treatment_trigger') or {}).get('state', {}).get('resolved_reviews'):
            pending.append({
                'case_key': audit.get('case_key'),
                'dispatch_id': audit.get('dispatch_id'),
                'bundle_status': audit.get('bundle_status'),
                'trial_selected_count': ((audit.get('trial_overlay') or {}).get('selected_count')),
                'trial_injected_count': ((audit.get('trial_overlay') or {}).get('injected_count')),
            })
        if str(((audit.get('coverage') or {}).get('classification') or '')) in {'empty', 'weak'}:
            coverage_gaps.append({
                'case_key': audit.get('case_key'),
                'dispatch_id': audit.get('dispatch_id'),
                'classification': ((audit.get('coverage') or {}).get('classification')),
                'gap_flags': ((audit.get('coverage') or {}).get('gap_flags') or []),
            })
    return {
        'coverage_counts': dict(sorted(coverage_counts.items())),
        'case_mix_counts': dict(sorted(case_mix_counts.items())),
        'pending_treatment_cohort': pending[:20],
        'coverage_gap_cases': coverage_gaps[:20],
        'counterfactual_control_preview_count': control_previews,
    }



def render_markdown(payload: dict[str, Any]) -> str:
    summary = payload.get('summary') or {}
    lines = [
        '# LMD + causal runtime status',
        '',
        '## Summary',
        '',
        f"- generated_at: `{summary.get('generated_at')}`",
        f"- assignments_by_arm: `{summary.get('assignments_by_arm')}`",
        f"- exposures_by_arm: `{summary.get('exposures_by_arm')}`",
        f"- trial_modes: `{summary.get('trial_modes')}`",
        f"- resolved_treatment_case_count: `{summary.get('resolved_treatment_case_count')}`",
        f"- pending_treatment_case_count: `{summary.get('pending_treatment_case_count')}`",
        f"- open_graph_violation_count: `{summary.get('open_graph_violation_count')}`",
        f"- proposal_funnel_total: `{summary.get('proposal_funnel_total')}`",
        f"- coverage_counts: `{summary.get('coverage_counts')}`",
        f"- retry_queue_depth: `{summary.get('retry_queue_depth')}`",
        f"- report_timestamps: `{summary.get('report_timestamps')}`",
        '',
        '## Pending treatment cohort',
        '',
    ]
    pending = payload.get('audit_derived', {}).get('pending_treatment_cohort') or []
    if not pending:
        lines.append('- none')
    else:
        for row in pending[:20]:
            lines.append(f"- `{row.get('case_key')}` / `{row.get('dispatch_id')}` — status={row.get('bundle_status')}; selected={row.get('trial_selected_count')}; injected={row.get('trial_injected_count')}")
    lines.extend(['', '## Coverage gaps', ''])
    gaps = payload.get('audit_derived', {}).get('coverage_gap_cases') or []
    if not gaps:
        lines.append('- none')
    else:
        for row in gaps[:20]:
            lines.append(f"- `{row.get('case_key')}` / `{row.get('dispatch_id')}` — {row.get('classification')}; gaps={', '.join(row.get('gap_flags') or [])}")
    lines.extend(['', '## Candidate outcome ledger (top)', ''])
    for row in (payload.get('candidate_outcome_ledger') or [])[:15]:
        lines.append(
            f"- `{row.get('proposal_id')}` [{row.get('mechanism_family')}] — stage={row.get('lifecycle_stage')}; shadow={row.get('shadow_match_count')}/{row.get('shadow_positive_count')}; trial={row.get('trial_exposure_count')} injected judged={row.get('trial_judged_count')}"
        )
    if not (payload.get('candidate_outcome_ledger') or []):
        lines.append('- none')
    lines.append('')
    return '\n'.join(lines)



def main() -> int:
    args = parse_args()
    db_url = resolve_db_url(args.db_url)
    assignments = fetch_json_rows(args.psql, db_url, 'lmd_experiment_assignments', ASSIGNMENTS_BY_ARM_SQL) if db_url else []
    exposures = fetch_json_rows(args.psql, db_url, 'lmd_bundle_exposures', EXPOSURES_BY_ARM_SQL) if db_url else []
    trial_modes = fetch_json_rows(args.psql, db_url, 'proposed_causal_trial_exposures', TRIAL_MODES_SQL) if db_url else []
    proposal_funnel = fetch_json_rows(args.psql, db_url, 'proposed_causal_candidate_stats', PROPOSAL_FUNNEL_SQL) if db_url else []
    live_nodes = fetch_json_rows(args.psql, db_url, 'causal_nodes', LIVE_NODES_STAGE_SQL) if db_url else []
    live_edges = fetch_json_rows(args.psql, db_url, 'causal_edges', LIVE_EDGES_STAGE_SQL) if db_url else []
    open_graph_violation_count = fetch_scalar_count(args.psql, db_url, 'causal_graph_health_violations', OPEN_GRAPH_VIOLATIONS_SQL) if db_url else 0
    resolved_treatment_case_count = fetch_scalar_count(args.psql, db_url, 'lmd_bundle_exposures', RESOLVED_TREATMENT_CASES_SQL) if db_url else 0
    candidate_outcome_ledger = fetch_json_rows(args.psql, db_url, 'proposed_causal_candidate_stats', CANDIDATE_OUTCOME_LEDGER_SQL) if db_url else []

    audits = load_audit_rows(limit=200)
    audit_derived = audit_counters(audits)
    queue_rows = read_json_lines(TRIGGER_RETRY_QUEUE_PATH)
    report_timestamps = {
        'post_treatment_feedback': read_report_generated_at(POST_TREATMENT_REPORT_JSON),
        'phase11_retrieval_policy_report': read_report_generated_at(PHASE11_REPORT_JSON),
        'reconciliation': read_report_generated_at(RECONCILIATION_JSON),
        'governance': read_report_generated_at(GOVERNANCE_JSON),
        'trial_packets': read_report_generated_at(TRIAL_PACKETS_JSON),
        'shadow_vs_live': read_report_generated_at(SHADOW_VS_LIVE_JSON),
    }

    summary = {
        'generated_at': now_iso(),
        'assignments_by_arm': rows_to_count_map(assignments),
        'exposures_by_arm': rows_to_count_map(exposures),
        'trial_modes': rows_to_count_map(trial_modes, key='overlay_mode'),
        'resolved_treatment_case_count': resolved_treatment_case_count,
        'pending_treatment_case_count': len(audit_derived['pending_treatment_cohort']),
        'proposal_funnel_total': sum(int(row.get('count') or 0) for row in proposal_funnel),
        'proposal_funnel': proposal_funnel,
        'live_nodes_by_stage': rows_to_count_map(live_nodes, key='lifecycle_stage'),
        'live_edges_by_stage': rows_to_count_map(live_edges, key='lifecycle_stage'),
        'open_graph_violation_count': open_graph_violation_count,
        'coverage_counts': audit_derived['coverage_counts'],
        'case_mix_counts': audit_derived['case_mix_counts'],
        'counterfactual_control_preview_count': audit_derived['counterfactual_control_preview_count'],
        'retry_queue_depth': len(queue_rows),
        'report_timestamps': report_timestamps,
    }
    payload = {
        'summary': summary,
        'audit_derived': audit_derived,
        'candidate_outcome_ledger': candidate_outcome_ledger,
    }
    if not args.dry_run:
        OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        write_json(OUTPUT_JSON, payload, pretty=True)
        OUTPUT_MD.write_text(render_markdown(payload) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
