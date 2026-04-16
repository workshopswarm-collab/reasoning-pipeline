#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL  # noqa: E402
from lib.lmd_causal_runtime import audit_path_for_bundle, coerce_string  # noqa: E402
from run_post_treatment_causal_feedback_cycle import load_treatment_cycles  # noqa: E402

WRITE_AUDIT = SCRIPT_PATH.parent / 'write_lmd_causal_dispatch_audit.py'
DEFAULT_EXPERIMENT_ID = 'researcher-lmd-v1'
DEFAULT_RECENT_TREATMENT_CASES = 50



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Backfill compact per-dispatch LMD/causal audit files for recent treatment cycles')
    parser.add_argument('--experiment-id', default=DEFAULT_EXPERIMENT_ID)
    parser.add_argument('--recent-treatment-cases', type=int, default=DEFAULT_RECENT_TREATMENT_CASES)
    parser.add_argument('--case-key', action='append', default=[])
    parser.add_argument('--dispatch-id', action='append', default=[])
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def run_json_command(command: list[str]) -> dict[str, Any]:
    proc = subprocess.run(command, text=True, capture_output=True)
    stdout = (proc.stdout or '').strip()
    stderr = (proc.stderr or '').strip()
    if proc.returncode != 0:
        return {'ok': False, 'command': command, 'returncode': proc.returncode, 'error': stderr or stdout or 'command failed'}
    payload: Any = None
    if stdout:
        try:
            payload = json.loads(stdout)
        except Exception:
            payload = {'raw_stdout': stdout}
    return {'ok': True, 'command': command, 'returncode': 0, 'payload': payload}



def unique(items: list[str]) -> set[str]:
    return {coerce_string(item) for item in items if coerce_string(item)}



def main() -> int:
    args = parse_args()
    cycles = load_treatment_cycles(
        db_url=args.db_url,
        psql_bin=args.psql,
        experiment_id=args.experiment_id,
        case_keys=unique(args.case_key),
        dispatch_ids=unique(args.dispatch_id),
        recent_limit=max(0, int(args.recent_treatment_cases)),
    )
    results: list[dict[str, Any]] = []
    for cycle in cycles:
        bundle_path = coerce_string(cycle.get('bundle_path'))
        if not bundle_path:
            continue
        audit_path = audit_path_for_bundle(bundle_path)
        if audit_path.exists() and not args.dry_run:
            results.append({'case_key': cycle.get('case_key'), 'dispatch_id': cycle.get('dispatch_id'), 'skipped': True, 'reason': 'audit_already_present', 'audit_path': str(audit_path)})
            continue
        command = [
            sys.executable,
            str(WRITE_AUDIT),
            '--bundle-path', bundle_path,
            '--case-key', str(cycle.get('case_key') or ''),
            '--dispatch-id', str(cycle.get('dispatch_id') or ''),
            '--research-run-id', str(cycle.get('research_run_id') or ''),
            '--notes-json', '{}',
            '--shadow-logging-json', '{}',
            '--trial-logging-json', '{}',
            '--lmd-logging-json', '{}',
            '--trigger-json', '{}',
        ]
        if args.pretty:
            command.append('--pretty')
        if args.dry_run:
            results.append({'case_key': cycle.get('case_key'), 'dispatch_id': cycle.get('dispatch_id'), 'audit_path': str(audit_path), 'skipped': True, 'reason': 'dry_run'})
            continue
        result = run_json_command(command)
        result.update({'case_key': cycle.get('case_key'), 'dispatch_id': cycle.get('dispatch_id')})
        results.append(result)

    output = {
        'ok': all(result.get('ok', True) for result in results),
        'audit_result_count': len(results),
        'written_count': sum(1 for result in results if result.get('ok') and not result.get('skipped')),
        'skipped_count': sum(1 for result in results if result.get('skipped')),
        'results': results,
    }
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0 if output.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
