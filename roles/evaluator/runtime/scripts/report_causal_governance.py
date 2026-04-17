#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.causal_family_policy import load_effective_family_policies  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.io import write_json  # noqa: E402
from lib.lmd_causal_runtime import GOVERNANCE_JSON, coerce_string  # noqa: E402

OUTPUT_JSON = GOVERNANCE_JSON
OUTPUT_MD = OUTPUT_JSON.with_suffix('.md')

MERGE_RECOMMENDATIONS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY proposal_id), '[]'::json)::text
FROM (
  SELECT proposal_id, candidate_type, mechanism_family, lifecycle_stage, promotion_status, merge_candidate_key, merge_recommended, near_live_graph_keys, promotion_blockers
  FROM public.proposed_causal_candidate_stats
  WHERE merge_recommended IS TRUE OR NULLIF(merge_candidate_key, '') IS NOT NULL
) t;
'''

HOLD_NODES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY entity_key), '[]'::json)::text
FROM (
  SELECT 'node'::text AS entity_type, node_key AS entity_key, mechanism_family, lifecycle_stage, status, superseded_by_key
  FROM public.causal_nodes
  WHERE lifecycle_stage = 'hold'
) t;
'''

HOLD_EDGES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY entity_key), '[]'::json)::text
FROM (
  SELECT 'edge'::text AS entity_type, edge_key AS entity_key, mechanism_family, lifecycle_stage, status, superseded_by_key
  FROM public.causal_edges
  WHERE lifecycle_stage = 'hold'
) t;
'''

NODE_STATS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY entity_key), '[]'::json)::text
FROM (
  SELECT node_key AS entity_key, mechanism_family, supporting_case_count, matched_case_count, projected_case_count, contested_case_count, learned_weight, shrunken_uplift, stats_metadata
  FROM public.causal_node_stats
) t;
'''

EDGE_STATS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY entity_key), '[]'::json)::text
FROM (
  SELECT edge_key AS entity_key, supporting_case_count, projected_case_count, contested_case_count, learned_weight, shrunken_uplift, stats_metadata
  FROM public.causal_edge_stats
) t;
'''

OPEN_VIOLATIONS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY entity_type, entity_key), '[]'::json)::text
FROM (
  SELECT entity_type, entity_key, violation_kind, severity
  FROM public.causal_graph_health_violations
  WHERE COALESCE(NULLIF(status, ''), 'open') NOT IN ('resolved', 'closed')
) t;
'''



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate a governance report for live/ proposal causal-map control surfaces')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()



def fetch_rows(psql_bin: str, db_url: str, table_name: str, sql: str) -> list[dict[str, Any]]:
    if not table_exists(table_name, db_url=db_url, psql_bin=psql_bin):
        return []
    rows = exec_sql(psql_bin, db_url, sql, {}) or []
    return rows if isinstance(rows, list) else []



def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return int(default)



def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return float(default)



def support_case_count(row: dict[str, Any]) -> int:
    return max(safe_int(row.get('supporting_case_count')), safe_int(row.get('matched_case_count')), safe_int(row.get('projected_case_count')))



def render_markdown(payload: dict[str, Any]) -> str:
    summary = payload.get('summary') or {}
    lines = [
        '# Causal governance report',
        '',
        '## Summary',
        '',
        f"- generated_at: `{summary.get('generated_at')}`",
        f"- merge_recommendation_count: `{summary.get('merge_recommendation_count')}`",
        f"- hold_item_count: `{summary.get('hold_item_count')}`",
        f"- reactivation_candidate_count: `{summary.get('reactivation_candidate_count')}`",
        f"- recommended_family_quarantine_count: `{summary.get('recommended_family_quarantine_count')}`",
        f"- open_structural_violation_count: `{summary.get('open_structural_violation_count')}`",
        '',
        '## Merge / supersession recommendations',
        '',
    ]
    merges = payload.get('merge_recommendations') or []
    if not merges:
        lines.append('- none')
    else:
        for row in merges[:20]:
            lines.append(f"- `{row.get('proposal_id')}` [{row.get('mechanism_family')}] → `{row.get('merge_candidate_key')}`; stage={row.get('lifecycle_stage')} / status={row.get('promotion_status')}")
    lines.extend(['', '## Hold reactivation candidates', ''])
    reactivations = payload.get('reactivation_candidates') or []
    if not reactivations:
        lines.append('- none')
    else:
        for row in reactivations[:20]:
            lines.append(f"- `{row.get('entity_type')}` `{row.get('entity_key')}` [{row.get('mechanism_family')}] — support={row.get('support_case_count')}; learned_weight={row.get('learned_weight')}; shrunken_uplift={row.get('shrunken_uplift')}")
    lines.extend(['', '## Recommended family quarantines', ''])
    quarantines = payload.get('recommended_family_quarantines') or []
    if not quarantines:
        lines.append('- none')
    else:
        for row in quarantines[:20]:
            lines.append(f"- `{row.get('mechanism_family')}` — reason={row.get('reason')}; hold_count={row.get('hold_count')}; high_severity_open_violations={row.get('high_severity_open_violations')}")
    lines.append('')
    return '\n'.join(lines)



def main() -> int:
    args = parse_args()
    db_url = resolve_db_url(args.db_url)
    family_policies = load_effective_family_policies(db_url=db_url, psql_bin=args.psql)
    merges = fetch_rows(args.psql, db_url, 'proposed_causal_candidate_stats', MERGE_RECOMMENDATIONS_SQL) if db_url else []
    hold_nodes = fetch_rows(args.psql, db_url, 'causal_nodes', HOLD_NODES_SQL) if db_url else []
    hold_edges = fetch_rows(args.psql, db_url, 'causal_edges', HOLD_EDGES_SQL) if db_url else []
    node_stats = fetch_rows(args.psql, db_url, 'causal_node_stats', NODE_STATS_SQL) if db_url else []
    edge_stats = fetch_rows(args.psql, db_url, 'causal_edge_stats', EDGE_STATS_SQL) if db_url else []
    open_violations = fetch_rows(args.psql, db_url, 'causal_graph_health_violations', OPEN_VIOLATIONS_SQL) if db_url else []

    stats_by_key = {coerce_string(row.get('entity_key')): row for row in [*node_stats, *edge_stats] if isinstance(row, dict)}
    open_violation_counts = Counter(coerce_string(row.get('entity_key')) for row in open_violations if isinstance(row, dict))
    high_severity_by_key = Counter(
        coerce_string(row.get('entity_key'))
        for row in open_violations
        if isinstance(row, dict) and coerce_string(row.get('severity')) in {'high', 'critical'}
    )
    structural_open_count = sum(1 for row in open_violations if isinstance(row, dict) and coerce_string(row.get('violation_kind')).startswith('structural_'))

    hold_items = [row for row in [*hold_nodes, *hold_edges] if isinstance(row, dict)]
    reactivation_candidates: list[dict[str, Any]] = []
    hold_counts_by_family = Counter()
    for row in hold_items:
        family = coerce_string(row.get('mechanism_family')) or 'unassigned'
        hold_counts_by_family[family] += 1
        stats = stats_by_key.get(coerce_string(row.get('entity_key'))) or {}
        policy = family_policies.get(family) or family_policies.get('unassigned') or {}
        if open_violation_counts.get(coerce_string(row.get('entity_key')), 0) > 0:
            continue
        if coerce_string(row.get('superseded_by_key')):
            continue
        if support_case_count(stats) < safe_int(policy.get('min_non_intervention_support_cases_for_trial')):
            continue
        if max(safe_float(stats.get('learned_weight')), safe_float(stats.get('shrunken_uplift'))) <= 0:
            continue
        reactivation_candidates.append({
            'entity_type': row.get('entity_type'),
            'entity_key': row.get('entity_key'),
            'mechanism_family': family,
            'support_case_count': support_case_count(stats),
            'learned_weight': stats.get('learned_weight'),
            'shrunken_uplift': stats.get('shrunken_uplift'),
            'notes': 'reactivation_candidate_from_hold',
        })

    family_quarantine_recommendations: list[dict[str, Any]] = []
    high_severity_by_family = Counter()
    for row in open_violations:
        if not isinstance(row, dict):
            continue
        if coerce_string(row.get('severity')) not in {'high', 'critical'}:
            continue
        entity_key = coerce_string(row.get('entity_key'))
        stats = stats_by_key.get(entity_key) or {}
        family = coerce_string(stats.get('mechanism_family')) or 'unassigned'
        high_severity_by_family[family] += 1
    for family, hold_count in sorted(hold_counts_by_family.items()):
        high_severity_count = high_severity_by_family.get(family, 0)
        if hold_count < 2 and high_severity_count == 0:
            continue
        policy = family_policies.get(family) or family_policies.get('unassigned') or {}
        family_quarantine_recommendations.append({
            'mechanism_family': family,
            'hold_count': hold_count,
            'high_severity_open_violations': high_severity_count,
            'policy_enabled': bool(policy.get('enabled', True)),
            'reason': 'repeated_hold_state' if hold_count >= 2 else 'high_severity_open_violations',
        })

    summary = {
        'generated_at': now_iso(),
        'merge_recommendation_count': len(merges),
        'hold_item_count': len(hold_items),
        'reactivation_candidate_count': len(reactivation_candidates),
        'recommended_family_quarantine_count': len(family_quarantine_recommendations),
        'open_structural_violation_count': structural_open_count,
    }
    payload = {
        'summary': summary,
        'merge_recommendations': merges,
        'hold_items': hold_items,
        'reactivation_candidates': reactivation_candidates,
        'recommended_family_quarantines': family_quarantine_recommendations,
        'policy_controls': {
            family: {
                'enabled': bool((policy or {}).get('enabled', True)),
                'notes': (policy or {}).get('notes') or {},
            }
            for family, policy in sorted(family_policies.items())
        },
    }
    if not args.dry_run:
        OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        write_json(OUTPUT_JSON, payload, pretty=True)
        OUTPUT_MD.write_text(render_markdown(payload) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
