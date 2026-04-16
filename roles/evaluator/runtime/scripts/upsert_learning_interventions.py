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

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.interventions import build_intervention_record, intervention_note_paths  # noqa: E402
from lib.paths import INTERVENTIONS_ROOT  # noqa: E402

UPSERT_SQL = r'''
INSERT INTO public.learning_interventions (
  intervention_key,
  path,
  intervention_label,
  status,
  application_surface,
  change_kind,
  target_selector,
  change_payload,
  hypothesis,
  evidence_paths,
  metric_definition,
  retrieval_tags,
  note_frontmatter,
  activated_at,
  ended_at,
  updated_at
)
VALUES (
  :'intervention_key',
  :'path',
  :'intervention_label',
  :'status',
  :'application_surface',
  :'change_kind',
  COALESCE(NULLIF(:'target_selector_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'change_payload_json', ''), '{}')::jsonb,
  NULLIF(:'hypothesis', ''),
  COALESCE(NULLIF(:'evidence_paths_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'metric_definition_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'retrieval_tags_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'note_frontmatter_json', ''), '{}')::jsonb,
  NULLIF(:'activated_at', '')::timestamptz,
  NULLIF(:'ended_at', '')::timestamptz,
  NOW()
)
ON CONFLICT (intervention_key) DO UPDATE SET
  path = EXCLUDED.path,
  intervention_label = EXCLUDED.intervention_label,
  status = EXCLUDED.status,
  application_surface = EXCLUDED.application_surface,
  change_kind = EXCLUDED.change_kind,
  target_selector = EXCLUDED.target_selector,
  change_payload = EXCLUDED.change_payload,
  hypothesis = EXCLUDED.hypothesis,
  evidence_paths = EXCLUDED.evidence_paths,
  metric_definition = EXCLUDED.metric_definition,
  retrieval_tags = EXCLUDED.retrieval_tags,
  note_frontmatter = EXCLUDED.note_frontmatter,
  activated_at = EXCLUDED.activated_at,
  ended_at = EXCLUDED.ended_at,
  updated_at = NOW()
RETURNING json_build_object(
  'intervention_key', intervention_key,
  'status', status,
  'application_surface', application_surface,
  'change_kind', change_kind
)::text;
'''


def persist_record(record: dict[str, Any], *, db_url: str = '', psql_bin: str = DEFAULT_PSQL) -> dict[str, Any]:
    resolved_db_url = resolve_db_url(db_url)
    table_present = table_exists('learning_interventions', db_url=resolved_db_url, psql_bin=psql_bin) if resolved_db_url else False
    result: dict[str, Any] = {
        'persisted': False,
        'table_present': table_present,
    }
    if resolved_db_url and table_present:
        payload = exec_sql(
            psql_bin,
            resolved_db_url,
            UPSERT_SQL,
            {
                'intervention_key': record['intervention_key'],
                'path': record['path'],
                'intervention_label': record['intervention_label'],
                'status': record['status'],
                'application_surface': record['application_surface'],
                'change_kind': record['change_kind'],
                'target_selector_json': json.dumps(record['target_selector']),
                'change_payload_json': json.dumps(record['change_payload']),
                'hypothesis': record['hypothesis'] or '',
                'evidence_paths_json': json.dumps(record['evidence_paths']),
                'metric_definition_json': json.dumps(record['metric_definition']),
                'retrieval_tags_json': json.dumps(record['retrieval_tags']),
                'note_frontmatter_json': json.dumps(record['note_frontmatter']),
                'activated_at': record['activated_at'] or '',
                'ended_at': record['ended_at'] or '',
            },
        )
        result['persisted'] = True
        result['db_result'] = payload
    elif resolved_db_url and not table_present:
        result['warning'] = 'learning_interventions table not present; apply roles/evaluator/sql/012_learning_interventions.sql to enable persistence'
    else:
        result['warning'] = 'db url unavailable; emitting registry records only'
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Upsert evaluator intervention registry entries from intervention-tracking markdown notes')
    parser.add_argument('--path', action='append', help='Specific intervention note path(s) to register')
    parser.add_argument('--root', default=str(INTERVENTIONS_ROOT), help='Intervention-tracking root to scan when --path is omitted')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    note_paths = [Path(raw) for raw in (args.path or [])]
    if not note_paths:
        note_paths = intervention_note_paths(Path(args.root))

    records = [build_intervention_record(path) for path in note_paths if path.exists()]
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
        results.append({
            'record': record,
            **persist_result,
        })

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
