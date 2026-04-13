#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from case_artifact_contract_audit import DEFAULT_CASES_ROOT, DEFAULT_REPORT_FILE, evaluate_case_artifact_contract


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Check canonical case artifact contract / case_key drift')
    parser.add_argument('--cases-root', default=str(DEFAULT_CASES_ROOT))
    parser.add_argument('--report-file', default=str(DEFAULT_REPORT_FILE))
    parser.add_argument('--no-report-file', action='store_true', help='Do not write the machine-readable report file')
    parser.add_argument('--pretty', action='store_true')
    parser.add_argument('--strict-warnings', action='store_true', help='Return exit code 1 when warnings are present even if there are no errors')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report_file = None if args.no_report_file else Path(args.report_file).expanduser().resolve()
    report = evaluate_case_artifact_contract(Path(args.cases_root).expanduser().resolve(), report_file=report_file)
    print(json.dumps(report, indent=2 if args.pretty else None))
    exit_code = int(report.get('exit_code', 2))
    if args.strict_warnings and report.get('status') == 'warn' and exit_code == 1:
        return 1
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
