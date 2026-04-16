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

from lib.causal_map import build_node_record, node_note_paths  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, missing_columns, resolve_db_url, table_exists  # noqa: E402
from lib.paths import CAUSAL_NODES_ROOT  # noqa: E402

REQUIRED_COLUMNS = [
    'mechanism_family',
    'source_kind',
    'lifecycle_stage',
    'promotion_score',
    'last_seen_at',
    'last_matched_at',
    'last_injected_at',
    'last_helpful_at',
    'decay_score',
    'demotion_reason',
    'superseded_by_key',
]

UPSERT_SQL = r'''
INSERT INTO public.causal_nodes (
  node_key,
  path,
  node_label,
  node_type,
  status,
  mechanism_family,
  source_kind,
  lifecycle_stage,
  promotion_score,
  description,
  contexts,
  tags,
  linked_paths,
  note_frontmatter,
  sidecar_path,
  last_seen_at,
  last_matched_at,
  last_injected_at,
  last_helpful_at,
  decay_score,
  demotion_reason,
  superseded_by_key,
  updated_at
)
VALUES (
  :'node_key',
  :'path',
  :'node_label',
  :'node_type',
  :'status',
  COALESCE(NULLIF(:'mechanism_family', ''), 'unassigned'),
  COALESCE(NULLIF(:'source_kind', ''), 'unknown'),
  COALESCE(NULLIF(:'lifecycle_stage', ''), 'draft'),
  COALESCE(NULLIF(:'promotion_score', '')::numeric, 0),
  NULLIF(:'description', ''),
  COALESCE(NULLIF(:'contexts_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'tags_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'linked_paths_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'note_frontmatter_json', ''), '{}')::jsonb,
  NULLIF(:'sidecar_path', ''),
  NULLIF(:'last_seen_at', '')::timestamptz,
  NULLIF(:'last_matched_at', '')::timestamptz,
  NULLIF(:'last_injected_at', '')::timestamptz,
  NULLIF(:'last_helpful_at', '')::timestamptz,
  COALESCE(NULLIF(:'decay_score', '')::numeric, 0),
  NULLIF(:'demotion_reason', ''),
  NULLIF(:'superseded_by_key', ''),
  NOW()
)
ON CONFLICT (node_key) DO UPDATE SET
  path = EXCLUDED.path,
  node_label = EXCLUDED.node_label,
  node_type = EXCLUDED.node_type,
  status = EXCLUDED.status,
  mechanism_family = EXCLUDED.mechanism_family,
  source_kind = EXCLUDED.source_kind,
  lifecycle_stage = EXCLUDED.lifecycle_stage,
  promotion_score = EXCLUDED.promotion_score,
  description = EXCLUDED.description,
  contexts = EXCLUDED.contexts,
  tags = EXCLUDED.tags,
  linked_paths = EXCLUDED.linked_paths,
  note_frontmatter = EXCLUDED.note_frontmatter,
  sidecar_path = EXCLUDED.sidecar_path,
  last_seen_at = EXCLUDED.last_seen_at,
  last_matched_at = EXCLUDED.last_matched_at,
  last_injected_at = EXCLUDED.last_injected_at,
  last_helpful_at = EXCLUDED.last_helpful_at,
  decay_score = EXCLUDED.decay_score,
  demotion_reason = EXCLUDED.demotion_reason,
  superseded_by_key = EXCLUDED.superseded_by_key,
  updated_at = NOW()
RETURNING json_build_object(
  'node_key', node_key,
  'status', status,
  'node_type', node_type,
  'mechanism_family', mechanism_family,
  'lifecycle_stage', lifecycle_stage
)::text;
'''


def persist_record(record: dict[str, Any], *, db_url: str = '', psql_bin: str = DEFAULT_PSQL) -> dict[str, Any]:
    resolved_db_url = resolve_db_url(db_url)
    table_present = table_exists('causal_nodes', db_url=resolved_db_url, psql_bin=psql_bin) if resolved_db_url else False
    result: dict[str, Any] = {
        'persisted': False,
        'table_present': table_present,
    }
    if resolved_db_url and table_present:
        missing = missing_columns('causal_nodes', REQUIRED_COLUMNS, db_url=resolved_db_url, psql_bin=psql_bin)
        if missing:
            result['warning'] = 'causal_nodes table is missing lifecycle columns; apply roles/evaluator/sql/028_causal_graph_lifecycle_columns.sql first'
            result['missing_columns'] = missing
            return result
        payload = exec_sql(
            psql_bin,
            resolved_db_url,
            UPSERT_SQL,
            {
                'node_key': record['node_key'],
                'path': record['path'],
                'node_label': record['node_label'],
                'node_type': record['node_type'],
                'status': record['status'],
                'mechanism_family': record.get('mechanism_family') or '',
                'source_kind': record.get('source_kind') or '',
                'lifecycle_stage': record.get('lifecycle_stage') or '',
                'promotion_score': '' if record.get('promotion_score') in (None, '') else str(record.get('promotion_score')),
                'description': record.get('description') or '',
                'contexts_json': json.dumps(record.get('contexts') or {}),
                'tags_json': json.dumps(record.get('tags') or []),
                'linked_paths_json': json.dumps(record.get('linked_paths') or {}),
                'note_frontmatter_json': json.dumps(record.get('note_frontmatter') or {}),
                'sidecar_path': record.get('sidecar_path') or '',
                'last_seen_at': record.get('last_seen_at') or '',
                'last_matched_at': record.get('last_matched_at') or '',
                'last_injected_at': record.get('last_injected_at') or '',
                'last_helpful_at': record.get('last_helpful_at') or '',
                'decay_score': '' if record.get('decay_score') in (None, '') else str(record.get('decay_score')),
                'demotion_reason': record.get('demotion_reason') or '',
                'superseded_by_key': record.get('superseded_by_key') or '',
            },
        )
        result['persisted'] = True
        result['db_result'] = payload
    elif resolved_db_url and not table_present:
        result['warning'] = 'causal_nodes table not present; apply roles/evaluator/sql/020_causal_nodes.sql and roles/evaluator/sql/028_causal_graph_lifecycle_columns.sql to enable persistence'
    else:
        result['warning'] = 'db url unavailable; emitting causal node records only'
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Upsert causal node records from qualitative-db/60-causal-map/nodes')
    parser.add_argument('--path', action='append', help='Specific node note path(s) to register')
    parser.add_argument('--root', default=str(CAUSAL_NODES_ROOT), help='Causal node root to scan when --path is omitted')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    note_paths = [Path(raw) for raw in (args.path or [])]
    if not note_paths:
        note_paths = node_note_paths(Path(args.root))

    records = [build_node_record(path) for path in note_paths if path.exists()]
    persisted_count = 0
    results: list[dict[str, Any]] = []
    warnings: list[str] = []
    for record in records:
        persist_result = persist_record(record, db_url=args.db_url, psql_bin=args.psql)
        if persist_result.get('persisted'):
            persisted_count += 1
        warning = persist_result.get('warning')
        if isinstance(warning, str) and warning not in warnings:
            warnings.append(warning)
        results.append({'record': record, **persist_result})

    output: dict[str, Any] = {
        'ok': True,
        'note_count': len(note_paths),
        'registered_count': len(records),
        'persisted_count': persisted_count,
        'results': results,
    }
    if warnings:
        output['warnings'] = warnings

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
