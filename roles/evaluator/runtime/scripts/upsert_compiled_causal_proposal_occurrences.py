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

from lib.db import DEFAULT_PSQL, exec_sql, missing_columns, resolve_db_url, table_exists  # noqa: E402
from lib.proposed_driver_occurrence_compiler import (  # noqa: E402
    COMPILER_VERSION,
    PACKETS_ROOT,
    PROPOSAL_SOURCE,
    STATUS_JSON_PATH,
    load_packet_rows,
)

REQUIRED_RUN_COLUMNS = [
    'run_id',
    'compiler_version',
    'source_root',
    'packet_root',
    'status',
    'source_occurrence_count',
    'grouped_candidate_count',
    'compiled_packet_count',
    'rejected_count',
    'error_count',
    'summary',
    'started_at',
    'completed_at',
]

REQUIRED_PACKET_COLUMNS = [
    'packet_key',
    'proposal_key',
    'candidate_slug',
    'candidate_label',
    'normalized_family',
    'proposal_source',
    'candidate_type',
    'packet_path',
    'packet_hash',
    'compiler_run_id',
    'source_occurrence_count',
    'distinct_case_count',
    'distinct_persona_count',
    'source_mix',
    'compiler_metadata',
]

UPSERT_RUN_SQL = r'''
INSERT INTO public.occurrence_compiler_runs (
  run_id,
  compiler_version,
  source_root,
  packet_root,
  status,
  source_occurrence_count,
  grouped_candidate_count,
  compiled_packet_count,
  rejected_count,
  error_count,
  summary,
  started_at,
  completed_at
)
VALUES (
  :'run_id',
  :'compiler_version',
  :'source_root',
  :'packet_root',
  :'status',
  :'source_occurrence_count'::int,
  :'grouped_candidate_count'::int,
  :'compiled_packet_count'::int,
  :'rejected_count'::int,
  :'error_count'::int,
  COALESCE(NULLIF(:'summary_json', ''), '{}')::jsonb,
  NOW(),
  NOW()
)
ON CONFLICT (run_id) DO UPDATE SET
  compiler_version = EXCLUDED.compiler_version,
  source_root = EXCLUDED.source_root,
  packet_root = EXCLUDED.packet_root,
  status = EXCLUDED.status,
  source_occurrence_count = EXCLUDED.source_occurrence_count,
  grouped_candidate_count = EXCLUDED.grouped_candidate_count,
  compiled_packet_count = EXCLUDED.compiled_packet_count,
  rejected_count = EXCLUDED.rejected_count,
  error_count = EXCLUDED.error_count,
  summary = EXCLUDED.summary,
  completed_at = NOW()
RETURNING json_build_object('run_id', run_id, 'status', status, 'compiled_packet_count', compiled_packet_count)::text;
'''

UPSERT_PACKET_SQL = r'''
INSERT INTO public.compiled_causal_proposal_occurrences (
  packet_key,
  proposal_key,
  candidate_slug,
  candidate_label,
  normalized_family,
  proposal_source,
  candidate_type,
  packet_path,
  packet_hash,
  compiler_run_id,
  source_occurrence_count,
  distinct_case_count,
  distinct_persona_count,
  source_mix,
  compiler_metadata,
  updated_at
)
VALUES (
  :'packet_key',
  :'proposal_key',
  :'candidate_slug',
  :'candidate_label',
  :'normalized_family',
  :'proposal_source',
  :'candidate_type',
  :'packet_path',
  :'packet_hash',
  :'compiler_run_id',
  :'source_occurrence_count'::int,
  :'distinct_case_count'::int,
  :'distinct_persona_count'::int,
  COALESCE(NULLIF(:'source_mix_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'compiler_metadata_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (packet_key) DO UPDATE SET
  proposal_key = EXCLUDED.proposal_key,
  candidate_slug = EXCLUDED.candidate_slug,
  candidate_label = EXCLUDED.candidate_label,
  normalized_family = EXCLUDED.normalized_family,
  proposal_source = EXCLUDED.proposal_source,
  candidate_type = EXCLUDED.candidate_type,
  packet_path = EXCLUDED.packet_path,
  packet_hash = EXCLUDED.packet_hash,
  compiler_run_id = EXCLUDED.compiler_run_id,
  source_occurrence_count = EXCLUDED.source_occurrence_count,
  distinct_case_count = EXCLUDED.distinct_case_count,
  distinct_persona_count = EXCLUDED.distinct_persona_count,
  source_mix = EXCLUDED.source_mix,
  compiler_metadata = EXCLUDED.compiler_metadata,
  updated_at = NOW()
RETURNING json_build_object('packet_key', packet_key, 'candidate_slug', candidate_slug, 'normalized_family', normalized_family)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Upsert occurrence-backed compiled packet metadata into Postgres')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def main() -> int:
    args = parse_args()
    resolved_db_url = resolve_db_url(args.db_url)
    packets = load_packet_rows()
    status_payload = json.loads(STATUS_JSON_PATH.read_text(encoding='utf-8')) if STATUS_JSON_PATH.exists() else {}
    run_id = str(status_payload.get('run_id') or '') or 'occurrence-compiler-manual'
    output: dict[str, Any] = {
        'ok': True,
        'run_id': run_id,
        'packet_count': len(packets),
        'packet_root': str(PACKETS_ROOT),
        'rows': [],
        'warnings': [],
    }

    if not resolved_db_url:
        output['ok'] = False
        output['warnings'].append('db_url_unavailable')
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 1

    run_table_present = table_exists('occurrence_compiler_runs', db_url=resolved_db_url, psql_bin=args.psql)
    packet_table_present = table_exists('compiled_causal_proposal_occurrences', db_url=resolved_db_url, psql_bin=args.psql)
    run_missing = missing_columns('occurrence_compiler_runs', REQUIRED_RUN_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql) if run_table_present else REQUIRED_RUN_COLUMNS
    packet_missing = missing_columns('compiled_causal_proposal_occurrences', REQUIRED_PACKET_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql) if packet_table_present else REQUIRED_PACKET_COLUMNS
    if not run_table_present or run_missing:
        output['ok'] = False
        output['warnings'].append('occurrence_compiler_runs schema unavailable')
        output['missing_columns'] = {'occurrence_compiler_runs': run_missing, 'compiled_causal_proposal_occurrences': packet_missing}
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 1
    if not packet_table_present or packet_missing:
        output['ok'] = False
        output['warnings'].append('compiled_causal_proposal_occurrences schema unavailable')
        output['missing_columns'] = {'compiled_causal_proposal_occurrences': packet_missing}
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 1

    if not args.dry_run:
        run_row = exec_sql(
            args.psql,
            resolved_db_url,
            UPSERT_RUN_SQL,
            {
                'run_id': run_id,
                'compiler_version': str(status_payload.get('compiler_version') or COMPILER_VERSION),
                'source_root': str(status_payload.get('source_lane') or 'public.proposed_driver_occurrences'),
                'packet_root': str(status_payload.get('packet_root') or str(PACKETS_ROOT)),
                'status': 'completed',
                'source_occurrence_count': str(status_payload.get('source_occurrence_count') or 0),
                'grouped_candidate_count': str(status_payload.get('candidate_count') or len(packets)),
                'compiled_packet_count': str(len(packets)),
                'rejected_count': '0',
                'error_count': '0',
                'summary_json': json.dumps({
                    'top_families': status_payload.get('top_families') or [],
                    'warnings': status_payload.get('warnings') or [],
                }),
            },
        )
        output['run_row'] = run_row

    for packet in packets:
        source_summary = packet.get('source_summary') or {}
        compiler_metadata = packet.get('compiler_metadata') or {}
        row_result = None
        if not args.dry_run:
            row_result = exec_sql(
                args.psql,
                resolved_db_url,
                UPSERT_PACKET_SQL,
                {
                    'packet_key': str(packet.get('packet_key') or ''),
                    'proposal_key': str(packet.get('proposal_key') or ''),
                    'candidate_slug': str(packet.get('candidate_slug') or ''),
                    'candidate_label': str(packet.get('candidate_label') or ''),
                    'normalized_family': str(packet.get('normalized_family') or 'unassigned'),
                    'proposal_source': str(packet.get('proposal_source') or PROPOSAL_SOURCE),
                    'candidate_type': str(packet.get('candidate_type') or 'packet'),
                    'packet_path': str(Path(status_payload.get('packet_root') or str(PACKETS_ROOT)) / f"{packet.get('candidate_slug')}.json"),
                    'packet_hash': str(packet.get('packet_hash') or ''),
                    'compiler_run_id': run_id,
                    'source_occurrence_count': str(source_summary.get('source_occurrence_count') or 0),
                    'distinct_case_count': str(source_summary.get('distinct_case_count') or 0),
                    'distinct_persona_count': str(source_summary.get('distinct_persona_count') or 0),
                    'source_mix_json': json.dumps(source_summary.get('source_mix') or {'db': int(source_summary.get('source_occurrence_count') or 0)}),
                    'compiler_metadata_json': json.dumps(compiler_metadata),
                },
            )
        output['rows'].append({'packet_key': packet.get('packet_key'), 'db_result': row_result})

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0 if output.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
