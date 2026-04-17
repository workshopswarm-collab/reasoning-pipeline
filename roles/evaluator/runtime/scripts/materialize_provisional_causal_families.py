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

from lib.causal_family_policy import load_family_policies  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, missing_columns, resolve_db_url, table_exists  # noqa: E402
from lib.proposed_driver_occurrence_compiler import load_packet_rows  # noqa: E402
from lib.provisional_family_registry import (  # noqa: E402
    PROVISIONAL_FAMILY_REGISTRY_JSON_PATH,
    PROVISIONAL_FAMILY_REGISTRY_MD_PATH,
    build_provisional_family_registry,
    write_provisional_family_registry_artifacts,
)

REQUIRED_FAMILY_COLUMNS = [
    'family_label',
    'source_family_slug',
    'family_state',
    'source_lane',
    'seed_candidate_count',
    'distinct_case_count',
    'distinct_persona_count',
    'evidence_mass',
    'lineage_parent_family_key',
    'family_metadata',
    'compiler_metadata',
]

REQUIRED_MEMBER_COLUMNS = [
    'family_key',
    'candidate_slug',
    'packet_key',
    'membership_score',
    'membership_role',
    'member_metadata',
]

UPSERT_FAMILY_SQL = r'''
INSERT INTO public.provisional_causal_families (
  family_key,
  family_label,
  source_family_slug,
  family_state,
  source_lane,
  seed_candidate_count,
  distinct_case_count,
  distinct_persona_count,
  evidence_mass,
  lineage_parent_family_key,
  family_metadata,
  compiler_metadata,
  updated_at,
  last_reinforced_at
)
VALUES (
  :'family_key',
  :'family_label',
  NULLIF(:'source_family_slug', ''),
  :'family_state',
  :'source_lane',
  :'seed_candidate_count'::int,
  :'distinct_case_count'::int,
  :'distinct_persona_count'::int,
  :'evidence_mass'::numeric,
  NULLIF(:'lineage_parent_family_key', ''),
  COALESCE(NULLIF(:'family_metadata_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'compiler_metadata_json', ''), '{}')::jsonb,
  NOW(),
  NOW()
)
ON CONFLICT (family_key) DO UPDATE SET
  family_label = EXCLUDED.family_label,
  source_family_slug = EXCLUDED.source_family_slug,
  family_state = EXCLUDED.family_state,
  source_lane = EXCLUDED.source_lane,
  seed_candidate_count = EXCLUDED.seed_candidate_count,
  distinct_case_count = EXCLUDED.distinct_case_count,
  distinct_persona_count = EXCLUDED.distinct_persona_count,
  evidence_mass = EXCLUDED.evidence_mass,
  lineage_parent_family_key = EXCLUDED.lineage_parent_family_key,
  family_metadata = EXCLUDED.family_metadata,
  compiler_metadata = EXCLUDED.compiler_metadata,
  updated_at = NOW(),
  last_reinforced_at = NOW()
RETURNING json_build_object(
  'family_key', family_key,
  'family_state', family_state,
  'seed_candidate_count', seed_candidate_count,
  'evidence_mass', evidence_mass
)::text;
'''

UPSERT_MEMBER_SQL = r'''
INSERT INTO public.provisional_causal_family_members (
  family_key,
  candidate_slug,
  packet_key,
  membership_score,
  membership_role,
  member_metadata,
  updated_at
)
VALUES (
  :'family_key',
  :'candidate_slug',
  NULLIF(:'packet_key', ''),
  :'membership_score'::numeric,
  :'membership_role',
  COALESCE(NULLIF(:'member_metadata_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (family_key, candidate_slug) DO UPDATE SET
  packet_key = EXCLUDED.packet_key,
  membership_score = EXCLUDED.membership_score,
  membership_role = EXCLUDED.membership_role,
  member_metadata = EXCLUDED.member_metadata,
  updated_at = NOW()
RETURNING json_build_object(
  'family_key', family_key,
  'candidate_slug', candidate_slug,
  'membership_role', membership_role
)::text;
'''

DELETE_STALE_MEMBER_SQL = r'''
WITH keep AS (
  SELECT value::text AS pair
  FROM json_array_elements_text(COALESCE(NULLIF(:'member_pairs_json', ''), '[]')::json)
), deleted AS (
  DELETE FROM public.provisional_causal_family_members AS m
  WHERE (m.family_key || '::' || m.candidate_slug) NOT IN (SELECT pair FROM keep)
  RETURNING 1
)
SELECT json_build_object('deleted_count', COUNT(*)::int)::text
FROM deleted;
'''

DELETE_STALE_FAMILY_SQL = r'''
WITH keep AS (
  SELECT value::text AS family_key
  FROM json_array_elements_text(COALESCE(NULLIF(:'family_keys_json', ''), '[]')::json)
), deleted AS (
  DELETE FROM public.provisional_causal_families AS f
  WHERE f.family_key NOT IN (SELECT family_key FROM keep)
  RETURNING 1
)
SELECT json_build_object('deleted_count', COUNT(*)::int)::text
FROM deleted;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Materialize canonical-bridged provisional causal families from compiled occurrence packets')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def main() -> int:
    args = parse_args()
    packets = load_packet_rows()
    policy_rows = load_family_policies()
    registry = build_provisional_family_registry(packets, loaded_policies=policy_rows)
    write_provisional_family_registry_artifacts(registry)

    resolved_db_url = resolve_db_url(args.db_url)
    family_table_present = table_exists('provisional_causal_families', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    member_table_present = table_exists('provisional_causal_family_members', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    family_missing = missing_columns('provisional_causal_families', REQUIRED_FAMILY_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url and family_table_present else REQUIRED_FAMILY_COLUMNS
    member_missing = missing_columns('provisional_causal_family_members', REQUIRED_MEMBER_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url and member_table_present else REQUIRED_MEMBER_COLUMNS
    if family_table_present and not family_missing:
        family_schema_ready = True
    else:
        family_schema_ready = False
    if member_table_present and not member_missing:
        member_schema_ready = True
    else:
        member_schema_ready = False

    persisted_families: list[dict[str, Any]] = []
    persisted_members: list[dict[str, Any]] = []
    deleted_family_count = 0
    deleted_member_count = 0
    stale_cleanup_skipped = False
    packets_present = bool(packets)

    if packets_present and resolved_db_url and family_schema_ready and member_schema_ready and not args.dry_run:
        for row in registry.get('families') or []:
            persisted_families.append(
                exec_sql(
                    args.psql,
                    resolved_db_url,
                    UPSERT_FAMILY_SQL,
                    {
                        'family_key': str(row.get('family_key') or ''),
                        'family_label': str(row.get('family_label') or ''),
                        'source_family_slug': str(row.get('source_family_slug') or ''),
                        'family_state': str(row.get('family_state') or 'provisional'),
                        'source_lane': str(row.get('source_lane') or 'public.proposed_driver_occurrences'),
                        'seed_candidate_count': str(row.get('candidate_count') or 0),
                        'distinct_case_count': str(row.get('distinct_case_count') or 0),
                        'distinct_persona_count': str(row.get('distinct_persona_count') or 0),
                        'evidence_mass': str(row.get('source_occurrence_count') or 0),
                        'lineage_parent_family_key': str(row.get('lineage_parent_family_key') or ''),
                        'family_metadata_json': json.dumps(
                            {
                                'canonical_family': row.get('canonical_family'),
                                'bridge_status': row.get('bridge_status'),
                                'bridge_confidence_max': row.get('bridge_confidence_max'),
                                'bridge_reasons': row.get('bridge_reasons') or [],
                                'manual_policy_family': row.get('manual_policy_family'),
                                'manual_policy_enabled': row.get('manual_policy_enabled'),
                                'source_family_label': row.get('source_family_label'),
                                'candidate_labels': row.get('candidate_labels') or [],
                                'top_candidates': row.get('top_candidates') or [],
                            }
                        ),
                        'compiler_metadata_json': json.dumps(
                            {
                                'registry_generated_at': registry.get('generated_at'),
                                'score_breakdown_examples': row.get('score_breakdown_examples') or [],
                                'report_json_path': str(PROVISIONAL_FAMILY_REGISTRY_JSON_PATH),
                                'report_md_path': str(PROVISIONAL_FAMILY_REGISTRY_MD_PATH),
                            }
                        ),
                    },
                )
            )
        for row in registry.get('members') or []:
            persisted_members.append(
                exec_sql(
                    args.psql,
                    resolved_db_url,
                    UPSERT_MEMBER_SQL,
                    {
                        'family_key': str(row.get('family_key') or ''),
                        'candidate_slug': str(row.get('candidate_slug') or ''),
                        'packet_key': str(row.get('packet_key') or ''),
                        'membership_score': str(row.get('membership_score') or 0),
                        'membership_role': str(row.get('membership_role') or 'provisional_seed'),
                        'member_metadata_json': json.dumps(row.get('member_metadata') or {}),
                    },
                )
            )
        member_pairs = [f"{row.get('family_key')}::{row.get('candidate_slug')}" for row in (registry.get('members') or [])]
        try:
            deleted_members_payload = exec_sql(
                args.psql,
                resolved_db_url,
                DELETE_STALE_MEMBER_SQL,
                {'member_pairs_json': json.dumps(member_pairs)},
            )
            family_keys = [str(row.get('family_key') or '') for row in (registry.get('families') or [])]
            deleted_families_payload = exec_sql(
                args.psql,
                resolved_db_url,
                DELETE_STALE_FAMILY_SQL,
                {'family_keys_json': json.dumps(family_keys)},
            )
            deleted_member_count = int((deleted_members_payload or {}).get('deleted_count') or 0)
            deleted_family_count = int((deleted_families_payload or {}).get('deleted_count') or 0)
        except Exception:
            deleted_member_count = 0
            deleted_family_count = 0
            stale_cleanup_skipped = True

    output: dict[str, Any] = {
        'ok': True,
        'registry_json_path': str(PROVISIONAL_FAMILY_REGISTRY_JSON_PATH),
        'registry_md_path': str(PROVISIONAL_FAMILY_REGISTRY_MD_PATH),
        'packet_count': len(packets),
        'family_count': int(registry.get('family_count') or 0),
        'member_count': int(registry.get('member_count') or 0),
        'canonical_seed_count': int(registry.get('canonical_seed_count') or 0),
        'provisional_count': int(registry.get('provisional_count') or 0),
        'novel_provisional_count': int(registry.get('novel_provisional_count') or 0),
        'top_canonical_families': (registry.get('canonical_families') or [])[:10],
        'top_families': (registry.get('families') or [])[:15],
        'persisted_family_count': len(persisted_families),
        'persisted_member_count': len(persisted_members),
        'deleted_stale_family_count': deleted_family_count,
        'deleted_stale_member_count': deleted_member_count,
        'stale_cleanup_skipped': stale_cleanup_skipped,
    }
    if not packets_present:
        output['warning'] = 'no_compiled_packets_found; run roles/evaluator/runtime/scripts/run_occurrence_compiler_cycle.py first'
    elif not resolved_db_url:
        output['warning'] = 'db_url_unavailable'
    elif not family_schema_ready or not member_schema_ready:
        output['warning'] = 'provisional family tables missing required schema; apply roles/evaluator/sql/041_provisional_causal_families.sql and roles/evaluator/sql/042_provisional_causal_family_members.sql'
        output['missing_columns'] = {
            'provisional_causal_families': family_missing,
            'provisional_causal_family_members': member_missing,
        }
    elif stale_cleanup_skipped:
        output['warning'] = 'stale_cleanup_skipped_due_to_permissions'

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0 if output.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
