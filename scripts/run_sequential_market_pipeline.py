#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / 'scripts') not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / 'scripts'))

from automation_control import DEFAULT_CONTROL_FILE  # noqa: E402
from pipeline_sequencer_periodic import DEFAULT_BRIER_OUTPUT_DIR  # noqa: E402
from pipeline_sequencer_runner import execute_sequencer  # noqa: E402

DEFAULT_HEARTBEAT_FILE = REPO_ROOT / 'scripts' / '.runtime-state' / 'pipeline-heartbeat.json'
DEFAULT_QUARANTINE_FILE = REPO_ROOT / 'scripts' / '.runtime-state' / 'pipeline-quarantine.json'
DEFAULT_LOCK = REPO_ROOT / 'scripts' / '.runtime-state' / 'pipeline-sequencer.lock'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run the reasoning pipeline sequentially over available markets')
    parser.add_argument('--max-cases', type=int, default=1, help='Maximum number of markets to process; use 0 to run until no more are available')
    parser.add_argument('--poll-seconds', type=float, default=15.0, help='Polling interval while watching pipeline status')
    parser.add_argument('--idle-seconds', type=float, default=60.0, help='Sleep interval between loop passes when idle/disabled')
    parser.add_argument('--max-case-seconds', type=float, default=7200.0, help='Maximum seconds to wait for one case before failing')
    parser.add_argument('--resume-existing', action='store_true', default=True, help='Resume the most recently updated non-terminal case before claiming a new one')
    parser.add_argument('--no-resume-existing', dest='resume_existing', action='store_false', help='Do not resume an existing non-terminal case')
    parser.add_argument('--loop', action='store_true', help='Run continuously instead of a single pass')
    parser.add_argument('--control-managed', action='store_true', help='Load sequencer behavior from the persisted automation control file each pass')
    parser.add_argument('--control-file', default=str(DEFAULT_CONTROL_FILE), help='Automation control file path used with --control-managed')
    parser.add_argument('--lock-file', default=str(DEFAULT_LOCK), help='Process lock to prevent concurrent sequencer loops')
    parser.add_argument('--resolution-sync-seconds', type=float, default=900.0, help='Cadence for Polymarket resolution sync while looping; set <=0 to disable')
    parser.add_argument('--brier-snapshot-seconds', type=float, default=86400.0, help='Cadence for persisted Brier snapshots while looping; set <=0 to disable')
    parser.add_argument('--brier-output-dir', default=str(DEFAULT_BRIER_OUTPUT_DIR), help='Directory for persisted Brier snapshot JSON files')
    parser.add_argument('--heartbeat-file', default=str(DEFAULT_HEARTBEAT_FILE), help='Sequencer heartbeat/status JSON path')
    parser.add_argument('--quarantine-file', default=str(DEFAULT_QUARANTINE_FILE), help='JSON registry for temporarily quarantined case_keys/market_ids')
    parser.add_argument('--quarantine-seconds', type=float, default=3600.0, help='How long to quarantine a failed case/market before retrying')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def main() -> None:
    execute_sequencer(parse_args())


if __name__ == '__main__':
    main()
