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

from lib.causal_map import build_edge_record, build_node_record, edge_note_paths, node_note_paths  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402

PROJECTIONS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT case_key, active_nodes, candidate_edges, contested_edges, updated_at
  FROM public.case_causal_projections
  ORDER BY case_key
) t;
'''

UPSERT_NODE_STATS_SQL = r'''
INSERT INTO public.causal_node_stats (
  node_key,
  mechanism_family,
  lifecycle_stage,
  projected_case_count,
  matched_case_count,
  exposure_count,
  injection_count,
  helpful_case_count,
  supporting_case_count,
  contested_case_count,
  raw_uplift,
  shrunken_uplift,
  learned_weight,
  decay_score,
  status,
  status_reason,
  stats_metadata,
  updated_at
)
VALUES (
  :'node_key',
  COALESCE(NULLIF(:'mechanism_family', ''), 'unassigned'),
  COALESCE(NULLIF(:'lifecycle_stage', ''), 'draft'),
  :'projected_case_count'::int,
  :'matched_case_count'::int,
  :'exposure_count'::int,
  :'injection_count'::int,
  :'helpful_case_count'::int,
  :'supporting_case_count'::int,
  :'contested_case_count'::int,
  NULL,
  NULL,
  COALESCE(NULLIF(:'learned_weight', '')::numeric, 0),
  COALESCE(NULLIF(:'decay_score', '')::numeric, 0),
  :'status',
  NULLIF(:'status_reason', ''),
  COALESCE(NULLIF(:'stats_metadata_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (node_key) DO UPDATE SET
  mechanism_family = EXCLUDED.mechanism_family,
  lifecycle_stage = EXCLUDED.lifecycle_stage,
  projected_case_count = EXCLUDED.projected_case_count,
  matched_case_count = EXCLUDED.matched_case_count,
  exposure_count = EXCLUDED.exposure_count,
  injection_count = EXCLUDED.injection_count,
  helpful_case_count = EXCLUDED.helpful_case_count,
  supporting_case_count = EXCLUDED.supporting_case_count,
  contested_case_count = EXCLUDED.contested_case_count,
  status = EXCLUDED.status,
  status_reason = EXCLUDED.status_reason,
  stats_metadata = EXCLUDED.stats_metadata,
  updated_at = NOW()
RETURNING json_build_object('node_key', node_key, 'projected_case_count', projected_case_count)::text;
'''

UPDATE_NODE_SEEN_SQL = r'''
UPDATE public.causal_nodes
SET
  last_seen_at = NULLIF(:'last_seen_at', '')::timestamptz,
  last_matched_at = NULLIF(:'last_matched_at', '')::timestamptz,
  updated_at = NOW()
WHERE node_key = :'node_key'
RETURNING json_build_object('node_key', node_key, 'last_seen_at', last_seen_at, 'last_matched_at', last_matched_at)::text;
'''

UPDATE_EDGE_SEEN_SQL = r'''
UPDATE public.causal_edges
SET
  last_seen_at = NULLIF(:'last_seen_at', '')::timestamptz,
  last_matched_at = NULLIF(:'last_matched_at', '')::timestamptz,
  updated_at = NOW()
WHERE edge_key = :'edge_key'
RETURNING json_build_object('edge_key', edge_key, 'last_seen_at', last_seen_at, 'last_matched_at', last_matched_at)::text;
'''

INSERT_EVENT_SQL = r'''
WITH inserted AS (
  INSERT INTO public.causal_graph_lifecycle_events (
    entity_type,
    entity_key,
    previous_stage,
    new_stage,
    event_kind,
    reason,
    related_entity_key,
    event_metadata
  )
  SELECT
    :'entity_type',
    :'entity_key',
    NULLIF(:'previous_stage', ''),
    :'new_stage',
    :'event_kind',
    NULLIF(:'reason', ''),
    NULLIF(:'related_entity_key', ''),
    COALESCE(NULLIF(:'event_metadata_json', ''), '{}')::jsonb
  WHERE NOT EXISTS (
    SELECT 1
    FROM public.causal_graph_lifecycle_events
    WHERE entity_type = :'entity_type'
      AND entity_key = :'entity_key'
      AND event_kind = :'event_kind'
  )
  RETURNING 1
)
SELECT json_build_object('inserted_count', COUNT(*))::text
FROM inserted;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Backfill baseline lifecycle state for causal nodes and edges')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return []


def max_timestamp(rows: list[dict[str, Any]]) -> str:
    vals = [str(row.get('updated_at') or '').strip() for row in rows if str(row.get('updated_at') or '').strip()]
    return max(vals) if vals else ''


def main() -> int:
    args = parse_args()
    resolved_db_url = resolve_db_url(args.db_url)
    if not resolved_db_url:
        print(json.dumps({'ok': False, 'warning': 'db_url_unavailable'}, indent=2 if args.pretty else None))
        return 1

    required_tables = {
        'causal_nodes': table_exists('causal_nodes', db_url=resolved_db_url, psql_bin=args.psql),
        'causal_edges': table_exists('causal_edges', db_url=resolved_db_url, psql_bin=args.psql),
        'case_causal_projections': table_exists('case_causal_projections', db_url=resolved_db_url, psql_bin=args.psql),
        'causal_node_stats': table_exists('causal_node_stats', db_url=resolved_db_url, psql_bin=args.psql),
        'causal_graph_lifecycle_events': table_exists('causal_graph_lifecycle_events', db_url=resolved_db_url, psql_bin=args.psql),
    }
    missing = [name for name, present in required_tables.items() if not present]
    if missing:
        print(json.dumps({'ok': False, 'missing_tables': missing}, indent=2 if args.pretty else None))
        return 1

    projections = exec_sql(args.psql, resolved_db_url, PROJECTIONS_SQL, {})
    if not isinstance(projections, list):
        projections = []

    nodes = [build_node_record(path) for path in node_note_paths()]
    edges = [build_edge_record(path) for path in edge_note_paths()]

    node_stats_results: list[Any] = []
    node_seen_results: list[Any] = []
    edge_seen_results: list[Any] = []
    lifecycle_event_inserts = 0

    for node in nodes:
        node_key = node['node_key']
        supporting_rows = [row for row in projections if node_key in as_list(row.get('active_nodes'))]
        contested_case_keys = sorted({
            str(row.get('case_key') or '')
            for row in projections
            if any(node_key in edge_key for edge_key in as_list(row.get('contested_edges')))
        })
        last_seen_at = max_timestamp(supporting_rows)
        payload = {
            'node_key': node_key,
            'mechanism_family': node.get('mechanism_family') or 'unassigned',
            'lifecycle_stage': node.get('lifecycle_stage') or 'draft',
            'projected_case_count': str(len({str(row.get('case_key') or '') for row in supporting_rows if row.get('case_key')})),
            'matched_case_count': str(len({str(row.get('case_key') or '') for row in supporting_rows if row.get('case_key')})),
            'exposure_count': '0',
            'injection_count': '0',
            'helpful_case_count': '0',
            'supporting_case_count': str(len({str(row.get('case_key') or '') for row in supporting_rows if row.get('case_key')})),
            'contested_case_count': str(len([key for key in contested_case_keys if key])),
            'learned_weight': '0',
            'decay_score': str(node.get('decay_score') or 0),
            'status': node.get('status') or 'draft',
            'status_reason': 'baseline_backfill_from_case_causal_projections',
            'stats_metadata_json': json.dumps({
                'initialized_by': str(SCRIPT_PATH.relative_to(SCRIPT_PATH.parents[4])),
                'latest_case_keys': sorted({str(row.get('case_key') or '') for row in supporting_rows if row.get('case_key')}),
                'contested_case_keys': [key for key in contested_case_keys if key],
                'baseline_version': 'v1',
            }),
        }
        node_stats_results.append(exec_sql(args.psql, resolved_db_url, UPSERT_NODE_STATS_SQL, payload))
        node_seen_results.append(exec_sql(args.psql, resolved_db_url, UPDATE_NODE_SEEN_SQL, {
            'node_key': node_key,
            'last_seen_at': last_seen_at,
            'last_matched_at': last_seen_at,
        }))
        event_result = exec_sql(args.psql, resolved_db_url, INSERT_EVENT_SQL, {
            'entity_type': 'causal_node',
            'entity_key': node_key,
            'previous_stage': '',
            'new_stage': node.get('lifecycle_stage') or 'draft',
            'event_kind': 'baseline_backfill',
            'reason': 'initialized lifecycle baseline for existing node',
            'related_entity_key': '',
            'event_metadata_json': json.dumps({
                'mechanism_family': node.get('mechanism_family') or 'unassigned',
                'source_kind': node.get('source_kind') or 'unknown',
            }),
        })
        lifecycle_event_inserts += int((event_result or {}).get('inserted_count') or 0)

    for edge in edges:
        edge_key = edge['edge_key']
        supporting_rows = [
            row for row in projections
            if edge_key in as_list(row.get('candidate_edges')) or edge_key in as_list(row.get('contested_edges'))
        ]
        last_seen_at = max_timestamp(supporting_rows)
        edge_seen_results.append(exec_sql(args.psql, resolved_db_url, UPDATE_EDGE_SEEN_SQL, {
            'edge_key': edge_key,
            'last_seen_at': last_seen_at,
            'last_matched_at': last_seen_at,
        }))
        event_result = exec_sql(args.psql, resolved_db_url, INSERT_EVENT_SQL, {
            'entity_type': 'causal_edge',
            'entity_key': edge_key,
            'previous_stage': '',
            'new_stage': edge.get('lifecycle_stage') or 'draft',
            'event_kind': 'baseline_backfill',
            'reason': 'initialized lifecycle baseline for existing edge',
            'related_entity_key': '',
            'event_metadata_json': json.dumps({
                'mechanism_family': edge.get('mechanism_family') or 'unassigned',
                'source_kind': edge.get('source_kind') or 'unknown',
            }),
        })
        lifecycle_event_inserts += int((event_result or {}).get('inserted_count') or 0)

    output = {
        'ok': True,
        'projection_count': len(projections),
        'node_count': len(nodes),
        'edge_count': len(edges),
        'node_stats_upserted': len(node_stats_results),
        'node_seen_updates': len(node_seen_results),
        'edge_seen_updates': len(edge_seen_results),
        'lifecycle_event_inserts': lifecycle_event_inserts,
        'node_stats_results': node_stats_results,
        'node_seen_results': node_seen_results,
        'edge_seen_results': edge_seen_results,
    }
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
