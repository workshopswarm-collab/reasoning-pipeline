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
from lib.occurrence_shadow_bridge import BRIDGE_SOURCE, PROPOSAL_SOURCE  # noqa: E402

SCORE_SCRIPT = SCRIPTS_DIR / 'score_proposed_causal_shadow_outcomes.py'
ADVANCE_SCRIPT = SCRIPTS_DIR / 'advance_proposed_causal_candidates.py'
CLAMP_SCRIPT = SCRIPTS_DIR / 'clamp_occurrence_bridge_screening.py'
REPORT_SCRIPT = SCRIPTS_DIR / 'report_occurrence_bridge_shadow_evidence.py'



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run shadow-outcome feedback for occurrence-bridge proposals')
    parser.add_argument('--case-key', default='')
    parser.add_argument('--proposal-id', default='')
    parser.add_argument('--dispatch-id', default='')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--include-already-judged', action='store_true')
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



def main() -> int:
    args = parse_args()
    score_cmd = [
        sys.executable,
        str(SCORE_SCRIPT),
        '--proposal-source', PROPOSAL_SOURCE,
        '--bridge-source', BRIDGE_SOURCE,
        *common_args(args),
    ]
    if args.case_key:
        score_cmd.extend(['--case-key', args.case_key])
    if args.proposal_id:
        score_cmd.extend(['--proposal-id', args.proposal_id])
    if args.dispatch_id:
        score_cmd.extend(['--dispatch-id', args.dispatch_id])
    if not args.include_already_judged:
        score_cmd.append('--only-unjudged')
    if args.dry_run:
        score_cmd.append('--dry-run')

    advance_cmd = [sys.executable, str(ADVANCE_SCRIPT), *common_args(args)]
    if args.dry_run:
        advance_cmd.append('--dry-run')

    clamp_cmd = [sys.executable, str(CLAMP_SCRIPT), *common_args(args)]
    if args.dry_run:
        clamp_cmd.append('--dry-run')

    report_cmd = [sys.executable, str(REPORT_SCRIPT), *common_args(args)]
    if args.dry_run:
        report_cmd.append('--dry-run')

    steps = [
        {'step': 'score_proposed_causal_shadow_outcomes', **run_json_command(score_cmd)},
        {'step': 'advance_proposed_causal_candidates', **run_json_command(advance_cmd)},
        {'step': 'clamp_occurrence_bridge_screening', **run_json_command(clamp_cmd)},
        {'step': 'report_occurrence_bridge_shadow_evidence', **run_json_command(report_cmd)},
    ]

    output = {
        'ok': all(step.get('ok', False) for step in steps),
        'proposal_source': PROPOSAL_SOURCE,
        'bridge_source': BRIDGE_SOURCE,
        'step_count': len(steps),
        'steps': steps,
    }
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0 if output.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
