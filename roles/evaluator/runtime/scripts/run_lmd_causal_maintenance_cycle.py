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
from lib.lmd_causal_runtime import TRIGGER_RETRY_QUEUE_PATH, read_json_lines, write_json_lines  # noqa: E402

RUN_POST_TREATMENT = SCRIPTS_DIR / 'run_post_treatment_causal_feedback_cycle.py'
TRIGGER_POST_TREATMENT = SCRIPTS_DIR / 'trigger_post_treatment_feedback_cycle.py'
BACKFILL_DISPATCH_AUDITS = SCRIPTS_DIR / 'backfill_lmd_causal_dispatch_audits.py'
RECONCILE_RUNTIME = SCRIPTS_DIR / 'reconcile_lmd_causal_runtime.py'
REPORT_RUNTIME_STATUS = SCRIPTS_DIR / 'report_lmd_causal_runtime_status.py'
REPORT_CAUSAL_GOVERNANCE = SCRIPTS_DIR / 'report_causal_governance.py'
REPORT_TRIAL_PACKETS = SCRIPTS_DIR / 'report_proposed_causal_trial_packets.py'
REPORT_SHADOW_VS_LIVE = SCRIPTS_DIR / 'report_shadow_vs_live_proposals.py'
DEFAULT_EXPERIMENT_ID = 'researcher-lmd-v1'
DEFAULT_RECENT_TREATMENT_CASES = 50



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run a backstop LMD/causal maintenance cycle with retry-queue drain and derived reports')
    parser.add_argument('--experiment-id', default=DEFAULT_EXPERIMENT_ID)
    parser.add_argument('--recent-treatment-cases', type=int, default=DEFAULT_RECENT_TREATMENT_CASES)
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--skip-post-treatment', action='store_true')
    parser.add_argument('--skip-retry-queue', action='store_true')
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



def common_db_args(args: argparse.Namespace) -> list[str]:
    out = ['--psql', args.psql]
    if args.db_url:
        out.extend(['--db-url', args.db_url])
    if args.pretty:
        out.append('--pretty')
    return out



def drain_retry_queue(args: argparse.Namespace) -> dict[str, Any]:
    rows = read_json_lines(TRIGGER_RETRY_QUEUE_PATH)
    retained: list[dict[str, Any]] = []
    results: list[dict[str, Any]] = []
    for row in rows:
        command = [
            sys.executable,
            str(TRIGGER_POST_TREATMENT),
            '--case-key', str(row.get('case_key') or ''),
            '--dispatch-id', str(row.get('dispatch_id') or ''),
            '--trigger-source', str(row.get('trigger_source') or 'maintenance_retry_queue'),
            '--repair-missing-logs',
            *common_db_args(args),
        ]
        if args.dry_run:
            command.append('--dry-run')
        result = run_json_command(command)
        results.append(result)
        if not result.get('ok'):
            retained.append(row)
            continue
        payload = result.get('payload') or {}
        if isinstance(payload, dict) and payload.get('ok') is False:
            retained.append(row)
    write_json_lines(TRIGGER_RETRY_QUEUE_PATH, retained)
    return {
        'step': 'drain_retry_queue',
        'ok': True,
        'processed_count': len(rows),
        'remaining_count': len(retained),
        'results': results,
    }



def main() -> int:
    args = parse_args()
    steps: list[dict[str, Any]] = []

    if not args.skip_retry_queue:
        steps.append(drain_retry_queue(args))

    if not args.skip_post_treatment:
        command = [
            sys.executable,
            str(RUN_POST_TREATMENT),
            '--experiment-id', args.experiment_id,
            '--recent-treatment-cases', str(args.recent_treatment_cases),
            '--repair-missing-logs',
            *common_db_args(args),
        ]
        if args.dry_run:
            command.append('--dry-run')
        steps.append({'step': 'run_post_treatment_causal_feedback_cycle', **run_json_command(command)})

    report_scripts = [
        ('backfill_lmd_causal_dispatch_audits', BACKFILL_DISPATCH_AUDITS, ['--experiment-id', args.experiment_id, '--recent-treatment-cases', str(args.recent_treatment_cases)]),
        ('reconcile_lmd_causal_runtime', RECONCILE_RUNTIME, ['--experiment-id', args.experiment_id, '--recent-treatment-cases', str(args.recent_treatment_cases)]),
        ('report_lmd_causal_runtime_status', REPORT_RUNTIME_STATUS, []),
        ('report_causal_governance', REPORT_CAUSAL_GOVERNANCE, []),
        ('report_proposed_causal_trial_packets', REPORT_TRIAL_PACKETS, []),
        ('report_shadow_vs_live_proposals', REPORT_SHADOW_VS_LIVE, []),
    ]
    for step_name, script_path, extra_args in report_scripts:
        command = [sys.executable, str(script_path), *extra_args, *common_db_args(args)]
        steps.append({'step': step_name, **run_json_command(command)})

    output = {
        'ok': all(step.get('ok', False) for step in steps),
        'step_count': len(steps),
        'steps': steps,
    }
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0 if output.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
