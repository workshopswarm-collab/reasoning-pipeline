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
from lib.io import read_json  # noqa: E402
from lib.proposed_driver_occurrence_compiler import (  # noqa: E402
    PACKETS_ROOT,
    STATUS_JSON_PATH,
    build_family_summaries,
    load_packet_rows,
    load_generated_index_payload,
    render_status_markdown,
    write_status_artifacts,
)



def sort_packets_by_support(packets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        packets,
        key=lambda packet: (
            -int(((packet.get('source_summary') or {}).get('source_occurrence_count') or 0)),
            -int(((packet.get('source_summary') or {}).get('distinct_case_count') or 0)),
            -int(((packet.get('source_summary') or {}).get('distinct_persona_count') or 0)),
            str(packet.get('candidate_slug') or ''),
        ),
    )

LATEST_RUN_SQL = r'''
SELECT COALESCE(json_build_object(
  'run_id', run_id,
  'status', status,
  'compiled_packet_count', compiled_packet_count,
  'source_occurrence_count', source_occurrence_count,
  'completed_at', completed_at
), '{}'::json)::text
FROM public.occurrence_compiler_runs
ORDER BY completed_at DESC NULLS LAST, started_at DESC NULLS LAST
LIMIT 1;
'''

PACKET_COUNTS_SQL = r'''
SELECT json_build_object(
  'compiled_row_count', COUNT(*)::int,
  'family_count', COUNT(DISTINCT normalized_family)::int,
  'latest_updated_at', MAX(updated_at)
)::text
FROM public.compiled_causal_proposal_occurrences;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Write a consolidated occurrence-compiler status report')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def main() -> int:
    args = parse_args()
    base_status = read_json(STATUS_JSON_PATH, default={}) or {}
    packets = sort_packets_by_support(load_packet_rows())
    index_payload = load_generated_index_payload()
    resolved_db_url = resolve_db_url(args.db_url)
    warnings = list(base_status.get('warnings') or [])

    db_summary: dict[str, Any] = {}
    latest_run: dict[str, Any] = {}
    if resolved_db_url and table_exists('occurrence_compiler_runs', db_url=resolved_db_url, psql_bin=args.psql):
        payload = exec_sql(args.psql, resolved_db_url, LATEST_RUN_SQL, {})
        if isinstance(payload, dict):
            latest_run = payload
    if resolved_db_url and table_exists('compiled_causal_proposal_occurrences', db_url=resolved_db_url, psql_bin=args.psql):
        payload = exec_sql(args.psql, resolved_db_url, PACKET_COUNTS_SQL, {})
        if isinstance(payload, dict):
            db_summary = payload
    if not resolved_db_url:
        warnings.append('db_url_unavailable')

    status = dict(base_status)
    status.setdefault('type', 'occurrence_compiler_status')
    status['ok'] = bool(base_status.get('ok', True))
    status['packet_root'] = str(base_status.get('packet_root') or PACKETS_ROOT)
    status['candidate_count'] = int(base_status.get('candidate_count') or len(packets))
    status['family_count'] = int(base_status.get('family_count') or len({str(packet.get('normalized_family') or 'unassigned') for packet in packets}))
    status['source_occurrence_count'] = int(base_status.get('source_occurrence_count') or 0)
    status['generated_index_present'] = bool(base_status.get('generated_index_present') or index_payload)
    status['markdown_fallback_occurrence_count'] = int(base_status.get('markdown_fallback_occurrence_count') or ((index_payload.get('source_counts') or {}).get('markdown_fallback_occurrence_count') or 0))
    status['top_families'] = build_family_summaries(packets)[:12] if packets else (base_status.get('top_families') or [])
    status['top_packets'] = [
        {
            'packet_key': packet.get('packet_key'),
            'candidate_slug': packet.get('candidate_slug'),
            'candidate_label': packet.get('candidate_label'),
            'normalized_family': packet.get('normalized_family'),
            'packet_path': f"{status['packet_root']}/{packet.get('candidate_slug')}.json",
            'source_occurrence_count': ((packet.get('source_summary') or {}).get('source_occurrence_count') or 0),
            'distinct_case_count': ((packet.get('source_summary') or {}).get('distinct_case_count') or 0),
            'distinct_persona_count': ((packet.get('source_summary') or {}).get('distinct_persona_count') or 0),
        }
        for packet in packets[:20]
    ] if packets else (base_status.get('top_packets') or [])
    status['db_summary'] = db_summary
    status['latest_run'] = latest_run
    status['warnings'] = sorted({str(item) for item in warnings if str(item).strip()})
    write_status_artifacts(status)
    print(json.dumps(status, indent=2 if args.pretty else None))
    return 0 if status.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
