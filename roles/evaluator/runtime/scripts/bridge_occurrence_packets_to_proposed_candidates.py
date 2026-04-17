#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
SCRIPTS_DIR = SCRIPT_PATH.parent
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, missing_columns, resolve_db_url, table_exists  # noqa: E402
from lib.occurrence_shadow_bridge import BRIDGE_SOURCE, PROPOSAL_SOURCE, build_shadow_bridge_rows  # noqa: E402

AGGREGATE_SCRIPT = SCRIPTS_DIR / 'aggregate_causal_candidate_proposals.py'
CLAMP_SCRIPT = SCRIPTS_DIR / 'clamp_occurrence_bridge_screening.py'

REQUIRED_COLUMNS = [
    'updated_at',
    'mechanism_family',
    'proposal_source',
    'evidence_channels',
    'intervention_dependency',
    'normalized_cluster_key',
    'context_snapshot',
]

DELETE_STALE_SQL = r'''
WITH keep AS (
  SELECT value::text AS pair
  FROM json_array_elements_text(COALESCE(NULLIF(:'keep_pairs_json', ''), '[]')::json)
), deleted AS (
  DELETE FROM public.proposed_causal_candidate_occurrences
  WHERE proposal_source = :'proposal_source'
    AND COALESCE(proposal_metadata->>'bridge_source', '') = :'bridge_source'
    AND (
      jsonb_array_length(COALESCE(NULLIF(:'keep_pairs_json', ''), '[]')::jsonb) = 0
      OR (proposal_id || '::' || case_key) NOT IN (SELECT pair FROM keep)
    )
  RETURNING 1
)
SELECT json_build_object('deleted_count', COUNT(*)::int)::text
FROM deleted;
'''

UPSERT_SQL = r'''
INSERT INTO public.proposed_causal_candidate_occurrences (
  proposal_id,
  proposal_key,
  candidate_type,
  candidate_label,
  mechanism_family,
  proposal_source,
  case_key,
  review_path,
  projection_path,
  source_node_key,
  target_node_key,
  node_type,
  effect_sign,
  support_direction,
  occurrence_reason,
  evidence_excerpt,
  genericity_penalty,
  evidence_channels,
  intervention_dependency,
  normalized_cluster_key,
  context_snapshot,
  trigger_snapshot,
  threshold_profile,
  proposal_metadata,
  updated_at
)
VALUES (
  :'proposal_id',
  :'proposal_key',
  :'candidate_type',
  :'candidate_label',
  COALESCE(NULLIF(:'mechanism_family', ''), 'unassigned'),
  COALESCE(NULLIF(:'proposal_source', ''), 'rule_projection'),
  :'case_key',
  :'review_path',
  :'projection_path',
  NULLIF(:'source_node_key', ''),
  NULLIF(:'target_node_key', ''),
  NULLIF(:'node_type', ''),
  NULLIF(:'effect_sign', ''),
  :'support_direction',
  NULLIF(:'occurrence_reason', ''),
  NULLIF(:'evidence_excerpt', ''),
  :'genericity_penalty'::numeric,
  COALESCE(NULLIF(:'evidence_channels_json', ''), '[]')::jsonb,
  :'intervention_dependency',
  NULLIF(:'normalized_cluster_key', ''),
  COALESCE(NULLIF(:'context_snapshot_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'trigger_snapshot_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'threshold_profile_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'proposal_metadata_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (proposal_id, case_key) DO UPDATE SET
  proposal_key = EXCLUDED.proposal_key,
  candidate_type = EXCLUDED.candidate_type,
  candidate_label = EXCLUDED.candidate_label,
  mechanism_family = EXCLUDED.mechanism_family,
  proposal_source = EXCLUDED.proposal_source,
  review_path = EXCLUDED.review_path,
  projection_path = EXCLUDED.projection_path,
  source_node_key = EXCLUDED.source_node_key,
  target_node_key = EXCLUDED.target_node_key,
  node_type = EXCLUDED.node_type,
  effect_sign = EXCLUDED.effect_sign,
  support_direction = EXCLUDED.support_direction,
  occurrence_reason = EXCLUDED.occurrence_reason,
  evidence_excerpt = EXCLUDED.evidence_excerpt,
  genericity_penalty = EXCLUDED.genericity_penalty,
  evidence_channels = EXCLUDED.evidence_channels,
  intervention_dependency = EXCLUDED.intervention_dependency,
  normalized_cluster_key = EXCLUDED.normalized_cluster_key,
  context_snapshot = EXCLUDED.context_snapshot,
  trigger_snapshot = EXCLUDED.trigger_snapshot,
  threshold_profile = EXCLUDED.threshold_profile,
  proposal_metadata = EXCLUDED.proposal_metadata,
  updated_at = NOW()
RETURNING json_build_object(
  'proposal_id', proposal_id,
  'case_key', case_key,
  'mechanism_family', mechanism_family,
  'candidate_type', candidate_type,
  'proposal_source', proposal_source
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Bridge enabled occurrence-backed provisional families into proposed causal candidate occurrences and refresh aggregation')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--skip-aggregate', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def run_json_command(command: list[str]) -> dict[str, Any]:
    proc = subprocess.run(command, text=True, capture_output=True)
    stdout = (proc.stdout or '').strip()
    stderr = (proc.stderr or '').strip()
    if proc.returncode != 0:
        return {
            'ok': False,
            'command': command,
            'returncode': proc.returncode,
            'error': stderr or stdout or 'command failed',
        }
    payload: Any = None
    if stdout:
        try:
            payload = json.loads(stdout)
        except Exception:
            payload = {'raw_stdout': stdout}
    return {'ok': True, 'command': command, 'payload': payload, 'returncode': 0}



def main() -> int:
    args = parse_args()
    rows_payload = build_shadow_bridge_rows()
    rows = rows_payload.get('rows') or []
    resolved_db_url = resolve_db_url(args.db_url)
    table_present = table_exists('proposed_causal_candidate_occurrences', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    schema_missing: list[str] = []
    if resolved_db_url and table_present:
        schema_missing = missing_columns('proposed_causal_candidate_occurrences', REQUIRED_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql)
        if schema_missing:
            table_present = False

    persisted_count = 0
    deleted_count = 0
    if resolved_db_url and table_present and not args.dry_run:
        keep_pairs = [f"{row.get('proposal_id')}::{row.get('case_key')}" for row in rows]
        delete_payload = exec_sql(
            args.psql,
            resolved_db_url,
            DELETE_STALE_SQL,
            {
                'keep_pairs_json': json.dumps(keep_pairs),
                'proposal_source': PROPOSAL_SOURCE,
                'bridge_source': BRIDGE_SOURCE,
            },
        )
        deleted_count = int((delete_payload or {}).get('deleted_count') or 0)
        for row in rows:
            exec_sql(
                args.psql,
                resolved_db_url,
                UPSERT_SQL,
                {
                    'proposal_id': str(row.get('proposal_id') or ''),
                    'proposal_key': str(row.get('proposal_key') or ''),
                    'candidate_type': str(row.get('candidate_type') or ''),
                    'candidate_label': str(row.get('candidate_label') or ''),
                    'mechanism_family': str(row.get('mechanism_family') or ''),
                    'proposal_source': str(row.get('proposal_source') or PROPOSAL_SOURCE),
                    'case_key': str(row.get('case_key') or ''),
                    'review_path': str(row.get('review_path') or ''),
                    'projection_path': str(row.get('projection_path') or ''),
                    'source_node_key': str(row.get('source_node_key') or ''),
                    'target_node_key': str(row.get('target_node_key') or ''),
                    'node_type': str(row.get('node_type') or ''),
                    'effect_sign': str(row.get('effect_sign') or ''),
                    'support_direction': str(row.get('support_direction') or 'supports'),
                    'occurrence_reason': str(row.get('occurrence_reason') or ''),
                    'evidence_excerpt': str(row.get('evidence_excerpt') or ''),
                    'genericity_penalty': str(row.get('genericity_penalty') or 0),
                    'evidence_channels_json': json.dumps(row.get('evidence_channels') or []),
                    'intervention_dependency': str(row.get('intervention_dependency') or 'none'),
                    'normalized_cluster_key': str(row.get('normalized_cluster_key') or ''),
                    'context_snapshot_json': json.dumps(row.get('context_snapshot') or {}),
                    'trigger_snapshot_json': json.dumps(row.get('trigger_snapshot') or {}),
                    'threshold_profile_json': json.dumps(row.get('threshold_profile') or {}),
                    'proposal_metadata_json': json.dumps(row.get('proposal_metadata') or {}),
                },
            )
            persisted_count += 1

    aggregate_result: dict[str, Any] | None = None
    clamp_result: dict[str, Any] | None = None
    if not args.skip_aggregate and not args.dry_run:
        command = [sys.executable, str(AGGREGATE_SCRIPT), '--psql', args.psql]
        if args.db_url:
            command.extend(['--db-url', args.db_url])
        if args.pretty:
            command.append('--pretty')
        aggregate_result = run_json_command(command)

        if aggregate_result.get('ok'):
            clamp_command = [sys.executable, str(CLAMP_SCRIPT), '--psql', args.psql]
            if args.db_url:
                clamp_command.extend(['--db-url', args.db_url])
            if args.pretty:
                clamp_command.append('--pretty')
            clamp_result = run_json_command(clamp_command)
        else:
            clamp_result = {'ok': False, 'skipped': True, 'reason': 'aggregate_failed'}

    output: dict[str, Any] = {
        'ok': True,
        'bridge_source': BRIDGE_SOURCE,
        'proposal_source': PROPOSAL_SOURCE,
        'row_count': int(rows_payload.get('row_count') or len(rows)),
        'enabled_family_count': int(rows_payload.get('enabled_family_count') or 0),
        'bridged_family_counts': rows_payload.get('bridged_family_counts') or {},
        'skipped_count': len(rows_payload.get('skipped') or []),
        'skipped_sample': (rows_payload.get('skipped') or [])[:25],
        'persisted_count': persisted_count,
        'deleted_stale_count': deleted_count,
        'aggregate_result': aggregate_result,
        'clamp_result': clamp_result,
    }
    if not resolved_db_url:
        output['warning'] = 'db_url_unavailable'
    elif schema_missing:
        output['warning'] = 'proposed_causal_candidate_occurrences missing required columns; apply roles/evaluator/sql/024_proposed_causal_candidate_occurrences.sql and roles/evaluator/sql/033_proposed_causal_candidate_evidence_metadata.sql'
        output['missing_columns'] = {'proposed_causal_candidate_occurrences': schema_missing}
    elif not table_present:
        output['warning'] = 'proposed_causal_candidate_occurrences table missing'
    elif args.dry_run:
        output['warning'] = 'dry_run_skipped_db_upsert_and_aggregate'
    elif args.skip_aggregate:
        output['warning'] = 'aggregate_skipped'

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0 if output.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
