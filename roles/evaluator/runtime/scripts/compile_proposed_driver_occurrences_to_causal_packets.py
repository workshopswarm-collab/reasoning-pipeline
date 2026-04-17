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

from lib.db import DEFAULT_PSQL, missing_columns, table_exists  # noqa: E402
from lib.proposed_driver_occurrence_compiler import (  # noqa: E402
    REQUIRED_OCCURRENCE_COLUMNS,
    build_status_payload,
    compile_occurrence_packets,
    load_active_occurrence_rows,
    load_generated_index_payload,
    resolve_occurrence_source_db_url,
    write_packet_artifacts,
    write_status_artifacts,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Compile proposed-driver occurrence rows into occurrence-backed causal packet artifacts')
    parser.add_argument('--db-url', default='', help='Optional source-occurrence DB URL; defaults to the orchestrator DB URL when available')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def main() -> int:
    args = parse_args()
    resolved_db_url = resolve_occurrence_source_db_url(args.db_url)
    warnings: list[str] = []

    if not resolved_db_url:
        status: dict[str, Any] = {
            'type': 'occurrence_compiler_status',
            'ok': False,
            'warnings': ['db_url_unavailable'],
        }
        write_status_artifacts(status)
        print(json.dumps(status, indent=2 if args.pretty else None))
        return 1

    table_present = table_exists('proposed_driver_occurrences', db_url=resolved_db_url, psql_bin=args.psql)
    schema_missing: list[str] = []
    if table_present:
        schema_missing = missing_columns('proposed_driver_occurrences', REQUIRED_OCCURRENCE_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql)
        if schema_missing:
            table_present = False
    if not table_present:
        warning = 'proposed_driver_occurrences table missing required schema'
        warnings.append(warning)
        status = {
            'type': 'occurrence_compiler_status',
            'ok': False,
            'warnings': warnings,
            'missing_columns': {'proposed_driver_occurrences': schema_missing},
        }
        write_status_artifacts(status)
        print(json.dumps(status, indent=2 if args.pretty else None))
        return 1

    rows = load_active_occurrence_rows(args.psql, resolved_db_url)
    index_payload = load_generated_index_payload()
    packets = compile_occurrence_packets(rows, index_payload)
    write_outcomes = write_packet_artifacts(packets)
    status = build_status_payload(rows=rows, packets=packets, write_outcomes=write_outcomes, index_payload=index_payload, warnings=warnings)
    write_status_artifacts(status)
    print(json.dumps(status, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
