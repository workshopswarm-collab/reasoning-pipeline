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

from lib.causal_map import build_edge_record, build_node_record, edge_note_paths, node_note_paths  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.io import parse_frontmatter, read_json, read_text, strip_frontmatter, write_json  # noqa: E402
from lib.paths import to_repo_relative  # noqa: E402
from scripts.upsert_causal_edges import persist_record as persist_edge_record  # noqa: E402
from scripts.upsert_causal_nodes import persist_record as persist_node_record  # noqa: E402

EVENT_COLUMNS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY ordinal_position), '[]'::json)::text
FROM (
  SELECT column_name, data_type, ordinal_position
  FROM information_schema.columns
  WHERE table_schema = 'public'
    AND table_name = 'causal_graph_lifecycle_events'
) t;
'''

SCRIPT_NAME = SCRIPT_PATH.name
TARGET_STAGE = 'trial'
TARGET_STATUS = 'active'
TARGET_EVIDENCE_STATUS = 'experimental_trial'
EVENT_TYPE = 'advanced_to_trial'

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    yaml = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Explicitly elevate live causal-graph draft items into trial recall')
    parser.add_argument('--node-key', action='append', default=[])
    parser.add_argument('--edge-key', action='append', default=[])
    parser.add_argument('--proposal-id', action='append', default=[])
    parser.add_argument('--proposal-key', action='append', default=[])
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--skip-db-refresh', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def unique(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        value = str(item or '').strip()
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def lifecycle_stage(record: dict[str, Any]) -> str:
    stage = str(record.get('lifecycle_stage') or '').strip().lower()
    if stage:
        return stage
    status = str(record.get('status') or '').strip().lower()
    if status in {'draft', 'trial', 'active', 'hold', 'retired', 'archived'}:
        return status
    return 'draft'


def frontmatter_text(frontmatter: dict[str, Any]) -> str:
    if yaml is not None:
        return yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()

    def render_scalar(value: Any) -> str:
        if value is None:
            return '""'
        if isinstance(value, bool):
            return 'true' if value else 'false'
        if isinstance(value, (int, float)):
            return str(value)
        text = str(value)
        if not text or any(ch in text for ch in [':', '#', '[', ']', '{', '}', '\n']) or text.lower() in {'true', 'false', 'null', 'yes', 'no'}:
            return json.dumps(text)
        return text

    lines: list[str] = []
    for key, value in frontmatter.items():
        if isinstance(value, list):
            lines.append(f'{key}:')
            for item in value:
                lines.append(f'  - {render_scalar(item)}')
            continue
        lines.append(f'{key}: {render_scalar(value)}')
    return '\n'.join(lines)


def render_note(frontmatter: dict[str, Any], body: str) -> str:
    rendered_body = body.lstrip('\n')
    return f"---\n{frontmatter_text(frontmatter)}\n---\n\n{rendered_body}" if rendered_body else f"---\n{frontmatter_text(frontmatter)}\n---\n"


def candidate_identity(record: dict[str, Any], entity_type: str) -> str:
    return str(record.get('node_key') if entity_type == 'node' else record.get('edge_key') or '').strip()


def record_matches(
    record: dict[str, Any],
    *,
    entity_type: str,
    node_keys: set[str],
    edge_keys: set[str],
    proposal_ids: set[str],
    proposal_keys: set[str],
) -> bool:
    frontmatter = record.get('note_frontmatter') or {}
    key = candidate_identity(record, entity_type)
    proposal_id = str(frontmatter.get('proposal_id') or '').strip()
    proposal_key = str(frontmatter.get('proposal_key') or '').strip()
    if entity_type == 'node' and key in node_keys:
        return True
    if entity_type == 'edge' and key in edge_keys:
        return True
    if proposal_id and proposal_id in proposal_ids:
        return True
    if proposal_key and proposal_key in proposal_keys:
        return True
    if key and key in proposal_keys:
        return True
    return False


def selected_entries(args: argparse.Namespace) -> list[dict[str, Any]]:
    node_keys = set(unique(args.node_key or []))
    edge_keys = set(unique(args.edge_key or []))
    proposal_ids = set(unique(args.proposal_id or []))
    proposal_keys = set(unique(args.proposal_key or []))
    if not any([node_keys, edge_keys, proposal_ids, proposal_keys]):
        raise SystemExit('Provide at least one selector: --node-key, --edge-key, --proposal-id, or --proposal-key')

    entries: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for note_path in node_note_paths():
        record = build_node_record(note_path)
        if not record_matches(record, entity_type='node', node_keys=node_keys, edge_keys=edge_keys, proposal_ids=proposal_ids, proposal_keys=proposal_keys):
            continue
        key = candidate_identity(record, 'node')
        pair = ('node', key)
        if pair in seen:
            continue
        seen.add(pair)
        entries.append({'entity_type': 'node', 'note_path': note_path, 'record': record})
    for note_path in edge_note_paths():
        record = build_edge_record(note_path)
        if not record_matches(record, entity_type='edge', node_keys=node_keys, edge_keys=edge_keys, proposal_ids=proposal_ids, proposal_keys=proposal_keys):
            continue
        key = candidate_identity(record, 'edge')
        pair = ('edge', key)
        if pair in seen:
            continue
        seen.add(pair)
        entries.append({'entity_type': 'edge', 'note_path': note_path, 'record': record})
    return entries


def transition_preview(entry: dict[str, Any], transitioned_at: str) -> dict[str, Any]:
    record = entry['record']
    entity_type = entry['entity_type']
    frontmatter = record.get('note_frontmatter') or {}
    return {
        'entity_type': entity_type,
        'entity_key': candidate_identity(record, entity_type),
        'path': to_repo_relative(entry['note_path']),
        'proposal_id': frontmatter.get('proposal_id') or None,
        'proposal_key': frontmatter.get('proposal_key') or None,
        'from_stage': lifecycle_stage(record),
        'to_stage': TARGET_STAGE,
        'from_status': record.get('status'),
        'to_status': TARGET_STATUS,
        'transitioned_at': transitioned_at,
    }


def apply_transition(entry: dict[str, Any], *, transitioned_at: str, dry_run: bool) -> dict[str, Any]:
    record = entry['record']
    entity_type = entry['entity_type']
    note_path = Path(entry['note_path'])
    sidecar_path = note_path.with_suffix('.json')
    current_stage = lifecycle_stage(record)
    preview = transition_preview(entry, transitioned_at)

    if current_stage != 'draft':
        preview['status'] = 'skipped'
        preview['reason'] = f'current lifecycle_stage is {current_stage}, not draft'
        return preview

    note_text = read_text(note_path)
    frontmatter = parse_frontmatter(note_text)
    sidecar = read_json(sidecar_path, default={}) or {}
    frontmatter['status'] = TARGET_STATUS
    frontmatter['lifecycle_stage'] = TARGET_STAGE
    frontmatter['lifecycle_stage_updated_at'] = transitioned_at
    frontmatter['lifecycle_stage_updated_by'] = SCRIPT_NAME
    frontmatter['lifecycle_transition'] = f'draft->{TARGET_STAGE}'
    if str(frontmatter.get('evidence_status') or '').strip() == 'experimental_draft':
        frontmatter['evidence_status'] = TARGET_EVIDENCE_STATUS

    sidecar['lifecycle_stage'] = TARGET_STAGE
    sidecar['status'] = TARGET_STATUS
    sidecar['last_stage_transition'] = {
        'event_type': EVENT_TYPE,
        'event_source': SCRIPT_NAME,
        'from_stage': 'draft',
        'to_stage': TARGET_STAGE,
        'occurred_at': transitioned_at,
    }
    sidecar['last_stage_transition_at'] = transitioned_at
    sidecar['lifecycle_stage_updated_at'] = transitioned_at
    sidecar['lifecycle_stage_updated_by'] = SCRIPT_NAME
    if str(sidecar.get('evidence_status') or '').strip() == 'experimental_draft':
        sidecar['evidence_status'] = TARGET_EVIDENCE_STATUS

    if dry_run:
        preview['status'] = 'dry_run'
        return preview

    note_path.write_text(render_note(frontmatter, strip_frontmatter(note_text)), encoding='utf-8')
    write_json(sidecar_path, sidecar, pretty=True)
    updated_record = build_node_record(note_path) if entity_type == 'node' else build_edge_record(note_path)
    preview['status'] = 'updated'
    preview['updated_record'] = {
        'status': updated_record.get('status'),
        'lifecycle_stage': updated_record.get('lifecycle_stage'),
        'path': updated_record.get('path'),
    }
    entry['record'] = updated_record
    return preview


def fetch_event_columns(*, db_url: str, psql_bin: str) -> list[dict[str, Any]]:
    if not db_url or not table_exists('causal_graph_lifecycle_events', db_url=db_url, psql_bin=psql_bin):
        return []
    rows = exec_sql(psql_bin, db_url, EVENT_COLUMNS_SQL, {})
    return rows if isinstance(rows, list) else []


def maybe_log_lifecycle_event(
    *,
    entry: dict[str, Any],
    transitioned_at: str,
    db_url: str,
    psql_bin: str,
    dry_run: bool,
) -> dict[str, Any] | None:
    resolved_db_url = resolve_db_url(db_url)
    columns = fetch_event_columns(db_url=resolved_db_url, psql_bin=psql_bin)
    if not columns:
        return None

    record = entry['record']
    entity_type = entry['entity_type']
    note_path = Path(entry['note_path'])
    frontmatter = record.get('note_frontmatter') or {}
    metadata = {
        'proposal_id': frontmatter.get('proposal_id'),
        'proposal_key': frontmatter.get('proposal_key'),
        'entity_type': entity_type,
        'entity_key': candidate_identity(record, entity_type),
        'mechanism_family': record.get('mechanism_family'),
        'source_kind': record.get('source_kind'),
        'note_path': to_repo_relative(note_path),
    }
    scalar_values: dict[str, Any] = {
        'entity_type': entity_type,
        'entity_key': candidate_identity(record, entity_type),
        'event_type': EVENT_TYPE,
        'event_source': SCRIPT_NAME,
        'from_stage': 'draft',
        'to_stage': TARGET_STAGE,
        'old_stage': 'draft',
        'new_stage': TARGET_STAGE,
        'reason': 'explicitly elevated from live graph draft into trial recall',
        'created_at': transitioned_at,
        'occurred_at': transitioned_at,
        'recorded_at': transitioned_at,
        'mechanism_family': record.get('mechanism_family'),
        'proposal_id': frontmatter.get('proposal_id'),
        'proposal_key': frontmatter.get('proposal_key'),
        'source_kind': record.get('source_kind'),
        'note_path': to_repo_relative(note_path),
    }
    json_values = {
        'metadata': metadata,
        'event_metadata': metadata,
        'details': metadata,
        'notes': metadata,
        'payload': metadata,
    }

    insert_columns: list[str] = []
    value_sql: list[str] = []
    params: dict[str, Any] = {}
    for column in columns:
        name = str(column.get('column_name') or '')
        data_type = str(column.get('data_type') or '')
        if not name or name == 'id':
            continue
        if name in json_values and 'json' in data_type:
            insert_columns.append(name)
            param_name = f'{name}_json'
            value_sql.append(f"COALESCE(NULLIF(:'{param_name}', ''), '{{}}')::jsonb")
            params[param_name] = json.dumps(json_values[name])
            continue
        if name in scalar_values:
            insert_columns.append(name)
            value_sql.append(f":'{name}'")
            value = scalar_values[name]
            params[name] = '' if value is None else str(value)

    if not insert_columns:
        return None

    if dry_run:
        return {
            'dry_run': True,
            'entity_key': candidate_identity(record, entity_type),
            'event_type': EVENT_TYPE,
            'columns': insert_columns,
        }

    sql = (
        f"INSERT INTO public.causal_graph_lifecycle_events ({', '.join(insert_columns)}) "
        f"VALUES ({', '.join(value_sql)}) "
        "RETURNING json_build_object('event_type', event_type, 'entity_key', entity_key)::text;"
    )
    return exec_sql(psql_bin, resolved_db_url, sql, params)


def maybe_refresh_db(*, entry: dict[str, Any], db_url: str, psql_bin: str, skip: bool, dry_run: bool) -> dict[str, Any] | None:
    if skip or not db_url:
        return None
    record = entry['record']
    entity_type = entry['entity_type']
    if dry_run:
        return {
            'dry_run': True,
            'entity_type': entity_type,
            'entity_key': candidate_identity(record, entity_type),
            'db_refresh': True,
        }
    if entity_type == 'node':
        return persist_node_record(record, db_url=db_url, psql_bin=psql_bin)
    return persist_edge_record(record, db_url=db_url, psql_bin=psql_bin)


def main() -> int:
    args = parse_args()
    transitioned_at = now_iso()
    entries = selected_entries(args)
    if not entries:
        payload = {'status': 'no_matches', 'updated': [], 'skipped': [], 'counts': {'matched': 0, 'updated': 0, 'skipped': 0}}
        print(json.dumps(payload, indent=2 if args.pretty else None))
        return 0

    updated: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    event_results: list[dict[str, Any]] = []
    db_refresh_results: list[dict[str, Any]] = []

    for entry in entries:
        result = apply_transition(entry, transitioned_at=transitioned_at, dry_run=args.dry_run)
        if result.get('status') in {'updated', 'dry_run'}:
            updated.append(result)
            event_row = maybe_log_lifecycle_event(
                entry=entry,
                transitioned_at=transitioned_at,
                db_url=args.db_url,
                psql_bin=args.psql,
                dry_run=args.dry_run,
            )
            if event_row is not None:
                event_results.append({'entity_key': result.get('entity_key'), 'event': event_row})
            db_row = maybe_refresh_db(
                entry=entry,
                db_url=args.db_url,
                psql_bin=args.psql,
                skip=args.skip_db_refresh,
                dry_run=args.dry_run,
            )
            if db_row is not None:
                db_refresh_results.append({'entity_key': result.get('entity_key'), 'db_refresh': db_row})
        else:
            skipped.append(result)

    payload = {
        'status': 'dry_run' if args.dry_run else 'ok',
        'transition': 'draft->trial',
        'updated': updated,
        'skipped': skipped,
        'lifecycle_events': event_results,
        'db_refreshes': db_refresh_results,
        'counts': {
            'matched': len(entries),
            'updated': len(updated),
            'skipped': len(skipped),
        },
    }
    print(json.dumps(payload, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
