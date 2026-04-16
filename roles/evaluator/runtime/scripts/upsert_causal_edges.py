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

from lib.causal_map import build_edge_record, edge_note_paths  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, missing_columns, resolve_db_url, table_exists  # noqa: E402
from lib.paths import CAUSAL_EDGES_ROOT  # noqa: E402

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
INSERT INTO public.causal_edges (
  edge_key,
  path,
  edge_label,
  source_node_key,
  target_node_key,
  effect_sign,
  status,
  mechanism_family,
  source_kind,
  lifecycle_stage,
  confidence_mode,
  confidence_prior,
  promotion_score,
  description,
  contexts,
  linked_intervention_keys,
  evidence_paths,
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
  :'edge_key',
  :'path',
  :'edge_label',
  :'source_node_key',
  :'target_node_key',
  :'effect_sign',
  :'status',
  COALESCE(NULLIF(:'mechanism_family', ''), 'unassigned'),
  COALESCE(NULLIF(:'source_kind', ''), 'unknown'),
  COALESCE(NULLIF(:'lifecycle_stage', ''), 'draft'),
  :'confidence_mode',
  NULLIF(:'confidence_prior', '')::numeric,
  COALESCE(NULLIF(:'promotion_score', '')::numeric, 0),
  NULLIF(:'description', ''),
  COALESCE(NULLIF(:'contexts_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'linked_intervention_keys_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'evidence_paths_json', ''), '[]')::jsonb,
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
ON CONFLICT (edge_key) DO UPDATE SET
  path = EXCLUDED.path,
  edge_label = EXCLUDED.edge_label,
  source_node_key = EXCLUDED.source_node_key,
  target_node_key = EXCLUDED.target_node_key,
  effect_sign = EXCLUDED.effect_sign,
  status = EXCLUDED.status,
  mechanism_family = EXCLUDED.mechanism_family,
  source_kind = EXCLUDED.source_kind,
  lifecycle_stage = EXCLUDED.lifecycle_stage,
  confidence_mode = EXCLUDED.confidence_mode,
  confidence_prior = EXCLUDED.confidence_prior,
  promotion_score = EXCLUDED.promotion_score,
  description = EXCLUDED.description,
  contexts = EXCLUDED.contexts,
  linked_intervention_keys = EXCLUDED.linked_intervention_keys,
  evidence_paths = EXCLUDED.evidence_paths,
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
  'edge_key', edge_key,
  'status', status,
  'source_node_key', source_node_key,
  'target_node_key', target_node_key,
  'mechanism_family', mechanism_family,
  'lifecycle_stage', lifecycle_stage
)::text;
'''

DELETE_EVIDENCE_SQL = r'''
WITH deleted AS (
  DELETE FROM public.causal_edge_evidence
  WHERE edge_key = :'edge_key'
  RETURNING 1
)
SELECT json_build_object('deleted_count', COUNT(*))::text
FROM deleted;
'''

INSERT_EVIDENCE_SQL = r'''
WITH input AS (
  SELECT COALESCE(NULLIF(:'rows_json', ''), '[]')::jsonb AS rows
),
inserted AS (
  INSERT INTO public.causal_edge_evidence (
    edge_key,
    case_key,
    review_path,
    signal_kind,
    signal_key,
    evidence_path,
    support_direction,
    confidence,
    notes
  )
  SELECT
    :'edge_key',
    NULLIF(item->>'case_key', ''),
    NULLIF(item->>'review_path', ''),
    NULLIF(item->>'signal_kind', ''),
    NULLIF(item->>'signal_key', ''),
    NULLIF(item->>'evidence_path', ''),
    COALESCE(NULLIF(item->>'support_direction', ''), 'supports'),
    NULLIF(item->>'confidence', '')::numeric,
    COALESCE(item->'notes', '{}'::jsonb)
  FROM input, jsonb_array_elements(input.rows) AS item
  RETURNING 1
)
SELECT json_build_object('inserted_count', COUNT(*))::text
FROM inserted;
'''


def persist_record(record: dict[str, Any], *, db_url: str = '', psql_bin: str = DEFAULT_PSQL) -> dict[str, Any]:
    resolved_db_url = resolve_db_url(db_url)
    edges_present = table_exists('causal_edges', db_url=resolved_db_url, psql_bin=psql_bin) if resolved_db_url else False
    evidence_present = table_exists('causal_edge_evidence', db_url=resolved_db_url, psql_bin=psql_bin) if resolved_db_url else False
    result: dict[str, Any] = {
        'persisted': False,
        'table_present': {
            'causal_edges': edges_present,
            'causal_edge_evidence': evidence_present,
        },
    }
    if resolved_db_url and edges_present:
        missing = missing_columns('causal_edges', REQUIRED_COLUMNS, db_url=resolved_db_url, psql_bin=psql_bin)
        if missing:
            result['warning'] = 'causal_edges table is missing lifecycle columns; apply roles/evaluator/sql/028_causal_graph_lifecycle_columns.sql first'
            result['missing_columns'] = missing
            return result
        payload = exec_sql(
            psql_bin,
            resolved_db_url,
            UPSERT_SQL,
            {
                'edge_key': record['edge_key'],
                'path': record['path'],
                'edge_label': record['edge_label'],
                'source_node_key': record['source_node_key'],
                'target_node_key': record['target_node_key'],
                'effect_sign': record['effect_sign'],
                'status': record['status'],
                'mechanism_family': record.get('mechanism_family') or '',
                'source_kind': record.get('source_kind') or '',
                'lifecycle_stage': record.get('lifecycle_stage') or '',
                'confidence_mode': record['confidence_mode'],
                'confidence_prior': '' if record.get('confidence_prior') in (None, '') else str(record.get('confidence_prior')),
                'promotion_score': '' if record.get('promotion_score') in (None, '') else str(record.get('promotion_score')),
                'description': record.get('description') or '',
                'contexts_json': json.dumps(record.get('contexts') or {}),
                'linked_intervention_keys_json': json.dumps(record.get('linked_intervention_keys') or []),
                'evidence_paths_json': json.dumps(record.get('evidence_paths') or []),
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
        if evidence_present:
            result['evidence_refresh'] = {
                'deleted': exec_sql(psql_bin, resolved_db_url, DELETE_EVIDENCE_SQL, {'edge_key': record['edge_key']}),
                'inserted': exec_sql(
                    psql_bin,
                    resolved_db_url,
                    INSERT_EVIDENCE_SQL,
                    {
                        'edge_key': record['edge_key'],
                        'rows_json': json.dumps(record.get('evidence_rows') or []),
                    },
                ),
            }
        else:
            result['warning'] = 'causal_edge_evidence table not present; apply roles/evaluator/sql/022_causal_edge_evidence.sql to enable evidence persistence'
    elif resolved_db_url and not edges_present:
        result['warning'] = 'causal_edges table not present; apply roles/evaluator/sql/021_causal_edges.sql and roles/evaluator/sql/028_causal_graph_lifecycle_columns.sql to enable persistence'
    else:
        result['warning'] = 'db url unavailable; emitting causal edge records only'
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Upsert causal edge records from qualitative-db/60-causal-map/edges')
    parser.add_argument('--path', action='append', help='Specific edge note path(s) to register')
    parser.add_argument('--root', default=str(CAUSAL_EDGES_ROOT), help='Causal edge root to scan when --path is omitted')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    note_paths = [Path(raw) for raw in (args.path or [])]
    if not note_paths:
        note_paths = edge_note_paths(Path(args.root))

    records = [build_edge_record(path) for path in note_paths if path.exists()]
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
