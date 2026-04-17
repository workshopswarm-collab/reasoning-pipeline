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

from lib.db import DEFAULT_PSQL  # noqa: E402

COMPILE_SCRIPT = SCRIPTS_DIR / 'compile_proposed_driver_occurrences_to_causal_packets.py'
UPSERT_SCRIPT = SCRIPTS_DIR / 'upsert_compiled_causal_proposal_occurrences.py'
REPORT_SCRIPT = SCRIPTS_DIR / 'report_occurrence_compiler_status.py'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run the occurrence-backed compiler cycle')
    parser.add_argument('--db-url', default='', help='Optional target DB URL for compiled-packet upsert/report steps')
    parser.add_argument('--source-db-url', default='', help='Optional source-occurrence DB URL for the compile step only')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
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



def common_args(args: argparse.Namespace) -> list[str]:
    out = ['--psql', args.psql]
    if args.db_url:
        out.extend(['--db-url', args.db_url])
    if args.pretty:
        out.append('--pretty')
    return out



def compile_args(args: argparse.Namespace) -> list[str]:
    out = ['--psql', args.psql]
    if args.source_db_url:
        out.extend(['--db-url', args.source_db_url])
    if args.pretty:
        out.append('--pretty')
    return out



def main() -> int:
    args = parse_args()
    steps: list[dict[str, Any]] = []
    compile_command = [sys.executable, str(COMPILE_SCRIPT), *compile_args(args)]
    steps.append({'step': 'compile_proposed_driver_occurrences_to_causal_packets', **run_json_command(compile_command)})

    upsert_command = [sys.executable, str(UPSERT_SCRIPT), *common_args(args)]
    if args.dry_run:
        upsert_command.append('--dry-run')
    steps.append({'step': 'upsert_compiled_causal_proposal_occurrences', **run_json_command(upsert_command)})

    report_command = [sys.executable, str(REPORT_SCRIPT), *common_args(args)]
    steps.append({'step': 'report_occurrence_compiler_status', **run_json_command(report_command)})

    output = {
        'ok': all(step.get('ok', False) for step in steps),
        'step_count': len(steps),
        'steps': steps,
    }
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0 if output.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
