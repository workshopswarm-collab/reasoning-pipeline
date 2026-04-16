#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
ORCH_ROOT = SCRIPT_PATH.parents[4]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

try:  # optional; JSON frontmatter fallback remains valid YAML 1.2
    import yaml  # type: ignore
except Exception:  # noqa: BLE001
    yaml = None

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.io import read_json  # noqa: E402
from lib.paths import CAUSAL_MAP_ROOT, to_repo_relative  # noqa: E402

SUMMARY_PATH = CAUSAL_MAP_ROOT / 'generated' / 'proposed-causal-candidates-summary.json'
ADVANCE_SCRIPT = SCRIPT_PATH.parent / 'advance_proposed_causal_candidates.py'
EVENT_COLUMNS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY ordinal_position), '[]'::json)::text
FROM (
  SELECT column_name, data_type, ordinal_position
  FROM information_schema.columns
  WHERE table_schema = 'public'
    AND table_name = 'causal_graph_lifecycle_events'
) t;
'''



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Materialize promotion_ready proposals into live graph draft notes')
    parser.add_argument('--proposal-id', action='append', default=[])
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--no-refresh', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()



def load_summary() -> dict[str, Any]:
    return read_json(SUMMARY_PATH, default={}) or {}



def selected_proposals(summary: dict[str, Any], proposal_ids: list[str]) -> list[dict[str, Any]]:
    wanted = {str(item).strip() for item in proposal_ids if str(item).strip()}
    rows: list[dict[str, Any]] = []
    for row in summary.get('proposals') or []:
        if not isinstance(row, dict):
            continue
        if str(row.get('lifecycle_stage') or '') != 'promotion_ready':
            continue
        if wanted and str(row.get('proposal_id') or '').strip() not in wanted:
            continue
        rows.append(row)
    return rows



def note_path_for(row: dict[str, Any]) -> Path:
    proposal_key = str(row.get('proposal_key') or '').strip()
    candidate_type = str(row.get('candidate_type') or '').strip()
    if candidate_type == 'node':
        return CAUSAL_MAP_ROOT / 'nodes' / f'{proposal_key}.md'
    if candidate_type == 'edge':
        return CAUSAL_MAP_ROOT / 'edges' / f'{proposal_key}.md'
    raise ValueError(f'unsupported candidate_type: {candidate_type!r}')



def _frontmatter_text(frontmatter: dict[str, Any]) -> str:
    if yaml is not None:
        return yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    return json.dumps(frontmatter, indent=2, sort_keys=False)



def render_note(row: dict[str, Any], *, materialized_at: str) -> str:
    candidate_type = str(row.get('candidate_type') or '').strip()
    proposal_id = str(row.get('proposal_id') or '').strip()
    proposal_key = str(row.get('proposal_key') or '').strip()
    label = str(row.get('candidate_label') or proposal_key).strip()
    mechanism_family = str(row.get('mechanism_family') or 'unassigned').strip()
    supporting_case_keys = list(row.get('supporting_case_keys') or [])
    stats_metadata = row.get('stats_metadata') or {}
    trial_readiness = row.get('trial_readiness') or {}
    promotion_readiness = row.get('promotion_readiness') or {}

    frontmatter: dict[str, Any] = {
        'type': 'causal_node' if candidate_type == 'node' else 'causal_edge',
        'status': 'active',
        'source_kind': 'promoted_candidate',
        'mechanism_family': mechanism_family,
        'lifecycle_stage': 'draft',
        'evidence_status': 'experimental_draft',
        'proposal_id': proposal_id,
        'proposal_key': proposal_key,
        'materialized_at': materialized_at,
        'materialized_by': 'materialize_promoted_causal_candidates.py',
        'supporting_case_keys': supporting_case_keys,
    }
    if candidate_type == 'node':
        frontmatter.update(
            {
                'node_key': proposal_key,
                'node_label': label,
                'node_type': str(row.get('node_type') or 'derived').strip(),
            }
        )
    else:
        frontmatter.update(
            {
                'edge_key': proposal_key,
                'edge_label': label,
                'source_node_key': str(row.get('source_node_key') or '').strip(),
                'target_node_key': str(row.get('target_node_key') or '').strip(),
                'effect_sign': str(row.get('effect_sign') or 'conditions').strip(),
            }
        )

    body_lines = [
        f'# {label}',
        '',
        'This is a live-graph `draft` item materialized from a `promotion_ready` proposal candidate.',
        'It exists for explicit review and later live-graph trial/active advancement; it is not default canon by virtue of materialization alone.',
        '',
        '## Promotion provenance',
        '',
        f'- proposal_id: `{proposal_id}`',
        f'- proposal_key: `{proposal_key}`',
        f'- candidate_type: `{candidate_type}`',
        f'- mechanism_family: `{mechanism_family}`',
        f'- materialized_at: `{materialized_at}`',
        f'- promotion_reason: `{row.get("promotion_reason")}`',
        f'- family_promotion_ready_rank: `{row.get("family_promotion_ready_rank")}`',
        '',
        '## Evidence summary',
        '',
        f'- supporting_case_keys: {", ".join(str(item) for item in supporting_case_keys) if supporting_case_keys else "[]"}',
        f'- distinct_case_count: `{row.get("distinct_case_count")}`',
        f'- non_intervention_support_case_count: `{row.get("non_intervention_support_case_count")}`',
        f'- contest_case_count: `{row.get("contest_case_count")}`',
        f'- shadow_helpful_count: `{row.get("shadow_helpful_count")}`',
        f'- shadow_trial_score: `{row.get("shadow_trial_score")}`',
        f'- trial_exposure_count: `{row.get("trial_exposure_count")}`',
        f'- trial_helpful_count: `{row.get("trial_helpful_count")}`',
        f'- trial_shrunken_utility: `{row.get("trial_shrunken_utility")}`',
        f'- trial_harmful_rate: `{row.get("trial_harmful_rate")}`',
        '',
        '## Advancement state at materialization',
        '',
        f'- trial_readiness: `{json.dumps(trial_readiness, sort_keys=True)}`',
        f'- promotion_readiness: `{json.dumps(promotion_readiness, sort_keys=True)}`',
        '',
        '## Candidate provenance snapshot',
        '',
        '```json',
        json.dumps(
            {
                'proposal_id': proposal_id,
                'proposal_key': proposal_key,
                'mechanism_family': mechanism_family,
                'supporting_case_keys': supporting_case_keys,
                'promotion_score': row.get('promotion_score'),
                'promotion_status': row.get('promotion_status'),
                'promotion_reason': row.get('promotion_reason'),
                'trial_metrics': (stats_metadata.get('trial_metrics') or {}),
                'family_policy': (stats_metadata.get('family_policy') or {}),
            },
            indent=2,
            sort_keys=True,
        ),
        '```',
        '',
    ]
    return f"---\n{_frontmatter_text(frontmatter)}\n---\n\n" + "\n".join(body_lines)



def fetch_event_columns(*, db_url: str, psql_bin: str) -> list[dict[str, Any]]:
    if not db_url:
        return []
    if not table_exists('causal_graph_lifecycle_events', db_url=db_url, psql_bin=psql_bin):
        return []
    rows = exec_sql(psql_bin, db_url, EVENT_COLUMNS_SQL, {})
    return rows if isinstance(rows, list) else []



def maybe_log_lifecycle_event(*, row: dict[str, Any], note_path: Path, materialized_at: str, db_url: str, psql_bin: str, dry_run: bool) -> dict[str, Any] | None:
    columns = fetch_event_columns(db_url=db_url, psql_bin=psql_bin)
    if not columns:
        return None

    metadata = {
        'proposal_id': row.get('proposal_id'),
        'proposal_key': row.get('proposal_key'),
        'candidate_type': row.get('candidate_type'),
        'mechanism_family': row.get('mechanism_family'),
        'note_path': to_repo_relative(note_path),
        'supporting_case_keys': row.get('supporting_case_keys') or [],
        'trial_metrics': {
            'trial_exposure_count': row.get('trial_exposure_count'),
            'trial_helpful_count': row.get('trial_helpful_count'),
            'trial_shrunken_utility': row.get('trial_shrunken_utility'),
        },
    }
    scalar_values: dict[str, Any] = {
        'entity_type': row.get('candidate_type'),
        'entity_key': row.get('proposal_key'),
        'event_type': 'materialized_to_draft',
        'event_source': 'materialize_promoted_causal_candidates.py',
        'from_stage': 'promotion_ready',
        'to_stage': 'draft',
        'old_stage': 'promotion_ready',
        'new_stage': 'draft',
        'reason': 'promotion_ready candidate materialized into live graph draft',
        'created_at': materialized_at,
        'occurred_at': materialized_at,
        'recorded_at': materialized_at,
        'mechanism_family': row.get('mechanism_family'),
        'proposal_id': row.get('proposal_id'),
        'proposal_key': row.get('proposal_key'),
        'source_kind': 'promoted_candidate',
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
            value = scalar_values[name]
            insert_columns.append(name)
            value_sql.append(f":'{name}'")
            params[name] = '' if value is None else str(value)

    if not insert_columns:
        return None

    sql = (
        f"INSERT INTO public.causal_graph_lifecycle_events ({', '.join(insert_columns)}) "
        f"VALUES ({', '.join(value_sql)}) "
        "RETURNING json_build_object('event_type', event_type, 'entity_key', entity_key)::text;"
    )
    if dry_run:
        return {
            'dry_run': True,
            'columns': insert_columns,
            'entity_key': row.get('proposal_key'),
            'event_type': 'materialized_to_draft',
        }
    return exec_sql(psql_bin, db_url, sql, params)



def refresh_candidate_state(*, args: argparse.Namespace) -> dict[str, Any] | None:
    if args.no_refresh or args.dry_run:
        return None
    cmd = [sys.executable, str(ADVANCE_SCRIPT), '--psql', args.psql]
    if args.db_url:
        cmd.extend(['--db-url', args.db_url])
    proc = subprocess.run(cmd, cwd=str(ORCH_ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.strip() or proc.stdout.strip() or 'advance_proposed_causal_candidates.py failed after materialization')
    try:
        return json.loads(proc.stdout)
    except Exception:  # noqa: BLE001
        return {'raw': proc.stdout}



def main() -> int:
    args = parse_args()
    summary = load_summary()
    rows = selected_proposals(summary, args.proposal_id)
    resolved_db_url = resolve_db_url(args.db_url)
    materialized_at = now_iso()

    results: list[dict[str, Any]] = []
    for row in rows:
        note_path = note_path_for(row)
        if note_path.exists():
            results.append(
                {
                    'proposal_id': row.get('proposal_id'),
                    'proposal_key': row.get('proposal_key'),
                    'status': 'skipped_existing',
                    'note_path': to_repo_relative(note_path),
                }
            )
            continue
        content = render_note(row, materialized_at=materialized_at)
        if not args.dry_run:
            note_path.parent.mkdir(parents=True, exist_ok=True)
            note_path.write_text(content, encoding='utf-8')
        event_result = maybe_log_lifecycle_event(
            row=row,
            note_path=note_path,
            materialized_at=materialized_at,
            db_url=resolved_db_url,
            psql_bin=args.psql,
            dry_run=args.dry_run,
        )
        results.append(
            {
                'proposal_id': row.get('proposal_id'),
                'proposal_key': row.get('proposal_key'),
                'candidate_type': row.get('candidate_type'),
                'status': 'materialized',
                'note_path': to_repo_relative(note_path),
                'event_result': event_result,
            }
        )

    refresh_result = refresh_candidate_state(args=args)
    output = {
        'ok': True,
        'dry_run': args.dry_run,
        'proposal_count': len(rows),
        'materialized_count': sum(1 for row in results if row.get('status') == 'materialized'),
        'skipped_existing_count': sum(1 for row in results if row.get('status') == 'skipped_existing'),
        'results': results,
        'refresh_result': refresh_result,
    }
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
