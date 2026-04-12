#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from case_artifact_contract_audit import DEFAULT_CASES_ROOT, DEFAULT_REPORT_FILE as DEFAULT_ARTIFACT_CONTRACT_REPORT_FILE, evaluate_case_artifact_contract

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HEARTBEAT_FILE = REPO_ROOT / 'scripts' / '.runtime-state' / 'pipeline-heartbeat.json'
DEFAULT_QUARANTINE_FILE = REPO_ROOT / 'scripts' / '.runtime-state' / 'pipeline-quarantine.json'
DEFAULT_REPORT_FILE = REPO_ROOT / 'scripts' / '.runtime-state' / 'pipeline-health-report.json'
DEFAULT_DECIDED_MARKET_WATCHER_HEARTBEAT_FILE = REPO_ROOT / 'scripts' / '.runtime-state' / 'decided-market-watcher-heartbeat.json'
DEFAULT_DB_ENV_FILE = REPO_ROOT / '.env.postgres.local'
DEFAULT_PSQL_BIN = '/opt/homebrew/opt/postgresql@16/bin/psql'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Check sequencer heartbeat / health state')
    parser.add_argument('--heartbeat-file', default=str(DEFAULT_HEARTBEAT_FILE))
    parser.add_argument('--quarantine-file', default=str(DEFAULT_QUARANTINE_FILE))
    parser.add_argument('--report-file', default=str(DEFAULT_REPORT_FILE))
    parser.add_argument('--max-heartbeat-age-seconds', type=float, default=1800.0)
    parser.add_argument('--max-resolution-sync-age-seconds', type=float, default=5400.0)
    parser.add_argument('--max-brier-age-seconds', type=float, default=172800.0)
    parser.add_argument('--max-quarantine-count', type=int, default=10)
    parser.add_argument('--artifact-contract-root', default=str(DEFAULT_CASES_ROOT))
    parser.add_argument('--artifact-contract-report-file', default=str(DEFAULT_ARTIFACT_CONTRACT_REPORT_FILE))
    parser.add_argument('--skip-artifact-contract-check', action='store_true')
    parser.add_argument('--decided-market-watcher-heartbeat-file', default=str(DEFAULT_DECIDED_MARKET_WATCHER_HEARTBEAT_FILE))
    parser.add_argument('--max-decided-market-watcher-age-seconds', type=float, default=120.0)
    parser.add_argument('--skip-decided-market-watcher-check', action='store_true')
    parser.add_argument('--market-checker-env-file', default=str(DEFAULT_DB_ENV_FILE))
    parser.add_argument('--market-checker-db-url', default=os.getenv('PREDQUANT_ADMIN_URL', ''))
    parser.add_argument('--market-checker-psql', default=os.getenv('PSQL_BIN', DEFAULT_PSQL_BIN))
    parser.add_argument('--max-market-snapshot-age-seconds', type=float, default=3600.0)
    parser.add_argument('--skip-market-checker-check', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def load_json_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def write_json_file(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')


def load_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    env: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        if line.startswith('export '):
            line = line[len('export '):].strip()
        key, value = line.split('=', 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def resolve_market_checker_db_url(args: argparse.Namespace) -> str:
    direct = str(args.market_checker_db_url or '').strip()
    if direct:
        return direct
    env_file = Path(args.market_checker_env_file).expanduser().resolve()
    env = load_env_file(env_file)
    return str(env.get('PREDQUANT_ADMIN_URL') or env.get('PREDQUANT_ORCHESTRATOR_URL') or '')


def query_market_checker_status(*, psql_bin: str, db_url: str) -> dict[str, Any]:
    sql = r'''
WITH open_markets AS (
  SELECT m.id, m.updated_at
  FROM public.markets m
  WHERE m.platform = 'polymarket'
    AND m.status = 'open'
), latest_snapshots AS (
  SELECT
    MAX(ms.observed_at) AS latest_snapshot_at,
    COUNT(*) AS snapshot_rows,
    COUNT(DISTINCT ms.market_id) AS snapped_open_market_count
  FROM public.market_snapshots ms
  JOIN open_markets om ON om.id = ms.market_id
), market_state AS (
  SELECT
    COUNT(*) AS open_market_count,
    MAX(updated_at) AS latest_market_update_at
  FROM open_markets
)
SELECT json_build_object(
  'open_market_count', COALESCE((SELECT open_market_count FROM market_state), 0),
  'latest_snapshot_at', (SELECT latest_snapshot_at FROM latest_snapshots),
  'latest_market_update_at', (SELECT latest_market_update_at FROM market_state),
  'snapshot_rows_for_open_markets', COALESCE((SELECT snapshot_rows FROM latest_snapshots), 0),
  'snapped_open_market_count', COALESCE((SELECT snapped_open_market_count FROM latest_snapshots), 0)
)::text;
'''
    proc = subprocess.run(
        [psql_bin, db_url, '-X', '-qAt', '-v', 'ON_ERROR_STOP=1', '-f', '-'],
        input=sql,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'psql failed')
    stdout = proc.stdout.strip()
    return json.loads(stdout.splitlines()[-1]) if stdout else {}


def parse_iso(value: Any) -> datetime | None:
    text = str(value or '').strip()
    if not text:
        return None
    text = text.replace('Z', '+00:00')
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def age_seconds(value: Any, *, now: datetime) -> float | None:
    dt = parse_iso(value)
    if dt is None:
        return None
    return max(0.0, (now - dt).total_seconds())


def add_issue(issues: list[dict[str, Any]], *, level: str, code: str, message: str, **extra: Any) -> None:
    issue = {'level': level, 'code': code, 'message': message}
    issue.update(extra)
    issues.append(issue)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    now = datetime.now(timezone.utc)
    heartbeat_path = Path(args.heartbeat_file).expanduser().resolve()
    quarantine_path = Path(args.quarantine_file).expanduser().resolve()
    report_path = Path(args.report_file).expanduser().resolve()
    artifact_contract_root = Path(args.artifact_contract_root).expanduser().resolve()
    artifact_contract_report_path = Path(args.artifact_contract_report_file).expanduser().resolve()
    decided_market_watcher_heartbeat_path = Path(args.decided_market_watcher_heartbeat_file).expanduser().resolve()
    market_checker_env_file = Path(args.market_checker_env_file).expanduser().resolve()
    market_checker_db_url = resolve_market_checker_db_url(args)

    heartbeat = load_json_file(heartbeat_path)
    quarantine = load_json_file(quarantine_path)
    quarantine_entries = quarantine.get('entries') if isinstance(quarantine.get('entries'), list) else []
    issues: list[dict[str, Any]] = []

    if not heartbeat:
        add_issue(issues, level='error', code='missing_heartbeat', message='Sequencer heartbeat file is missing or unreadable', path=str(heartbeat_path))
    else:
        state = str(heartbeat.get('state') or '')
        if state == 'failed':
            add_issue(issues, level='error', code='sequencer_failed', message='Sequencer heartbeat reports failed state', state=state, last_hard_failure=heartbeat.get('last_hard_failure'))

        last_activity_age = age_seconds(heartbeat.get('last_loop_completed_at') or heartbeat.get('last_loop_started_at'), now=now)
        if heartbeat.get('loop_mode'):
            if last_activity_age is None:
                add_issue(issues, level='error', code='missing_loop_activity', message='Loop heartbeat is missing last loop timestamps')
            elif last_activity_age > float(args.max_heartbeat_age_seconds):
                add_issue(issues, level='error', code='stale_loop', message='Sequencer loop heartbeat is stale', age_seconds=round(last_activity_age, 1), max_age_seconds=float(args.max_heartbeat_age_seconds))

        resolution_cfg = (((heartbeat.get('config') or {}) if isinstance(heartbeat.get('config'), dict) else {})).get('resolution_sync_seconds')
        last_resolution_sync = heartbeat.get('last_resolution_sync') if isinstance(heartbeat.get('last_resolution_sync'), dict) else {}
        if resolution_cfg not in (None, '', 0, 0.0):
            sync_age = age_seconds(last_resolution_sync.get('succeeded_at') or last_resolution_sync.get('attempted_at'), now=now)
            if sync_age is None:
                add_issue(issues, level='warn', code='missing_resolution_sync', message='No recorded resolution sync yet', cadence_seconds=resolution_cfg)
            elif sync_age > float(args.max_resolution_sync_age_seconds):
                add_issue(issues, level='error', code='stale_resolution_sync', message='Resolution sync appears stale', age_seconds=round(sync_age, 1), max_age_seconds=float(args.max_resolution_sync_age_seconds), last_resolution_sync=last_resolution_sync)
            elif last_resolution_sync.get('ok') is False:
                add_issue(issues, level='warn', code='last_resolution_sync_failed', message='Most recent resolution sync failed', last_resolution_sync=last_resolution_sync)

        brier_cfg = (((heartbeat.get('config') or {}) if isinstance(heartbeat.get('config'), dict) else {})).get('brier_snapshot_seconds')
        last_brier_snapshot = heartbeat.get('last_brier_snapshot') if isinstance(heartbeat.get('last_brier_snapshot'), dict) else {}
        if brier_cfg not in (None, '', 0, 0.0):
            brier_age = age_seconds(last_brier_snapshot.get('succeeded_at') or last_brier_snapshot.get('attempted_at'), now=now)
            if brier_age is None:
                add_issue(issues, level='warn', code='missing_brier_snapshot', message='No recorded Brier snapshot yet', cadence_seconds=brier_cfg)
            elif brier_age > float(args.max_brier_age_seconds):
                add_issue(issues, level='warn', code='stale_brier_snapshot', message='Brier snapshot appears stale', age_seconds=round(brier_age, 1), max_age_seconds=float(args.max_brier_age_seconds), last_brier_snapshot=last_brier_snapshot)
            elif last_brier_snapshot.get('ok') is False:
                add_issue(issues, level='warn', code='last_brier_snapshot_failed', message='Most recent Brier snapshot failed', last_brier_snapshot=last_brier_snapshot)

    quarantine_count = len(quarantine_entries)
    if quarantine_count > int(args.max_quarantine_count):
        add_issue(issues, level='warn', code='quarantine_buildup', message='Quarantine entry count is above threshold', quarantine_count=quarantine_count, max_quarantine_count=int(args.max_quarantine_count))

    artifact_contract_report: dict[str, Any] = {}
    if not args.skip_artifact_contract_check:
        artifact_contract_report = evaluate_case_artifact_contract(
            artifact_contract_root,
            report_file=artifact_contract_report_path,
        )
        for artifact_issue in artifact_contract_report.get('issues', []):
            level = str(artifact_issue.get('level') or 'warn')
            if level not in {'warn', 'error'}:
                level = 'warn'
            add_issue(
                issues,
                level=level,
                code=f"artifact_contract_{artifact_issue.get('code')}",
                message=str(artifact_issue.get('message') or 'Case artifact contract issue detected'),
                artifact_issue=artifact_issue,
            )

    decided_market_watcher_report: dict[str, Any] = {}
    if not args.skip_decided_market_watcher_check:
        decided_market_watcher_report = load_json_file(decided_market_watcher_heartbeat_path)
        watcher_age = age_seconds(decided_market_watcher_report.get('completed_at') or decided_market_watcher_report.get('started_at'), now=now)
        decided_market_watcher_report['age_seconds'] = round(watcher_age, 1) if watcher_age is not None else None
        if not decided_market_watcher_report:
            add_issue(
                issues,
                level='warn',
                code='missing_decided_market_watcher_heartbeat',
                message='Decided-market watcher heartbeat file is missing',
                decided_market_watcher_heartbeat_file=str(decided_market_watcher_heartbeat_path),
            )
        elif not decided_market_watcher_report.get('ok', False):
            add_issue(
                issues,
                level='error',
                code='decided_market_watcher_failed',
                message='Decided-market watcher reported a failed run',
                decided_market_watcher=decided_market_watcher_report,
            )
        elif watcher_age is not None and watcher_age > float(args.max_decided_market_watcher_age_seconds):
            add_issue(
                issues,
                level='error',
                code='stale_decided_market_watcher',
                message='Decided-market watcher heartbeat is stale',
                age_seconds=round(watcher_age, 1),
                max_age_seconds=float(args.max_decided_market_watcher_age_seconds),
                decided_market_watcher=decided_market_watcher_report,
            )

    market_checker_report: dict[str, Any] = {}
    if not args.skip_market_checker_check:
        if not market_checker_db_url:
            add_issue(
                issues,
                level='warn',
                code='market_checker_db_unconfigured',
                message='Market checker freshness check could not resolve a Postgres URL',
                env_file=str(market_checker_env_file),
            )
        else:
            try:
                market_checker_report = query_market_checker_status(
                    psql_bin=str(args.market_checker_psql),
                    db_url=market_checker_db_url,
                )
            except Exception as exc:  # noqa: BLE001
                add_issue(
                    issues,
                    level='warn',
                    code='market_checker_query_failed',
                    message='Market checker freshness query failed',
                    error=str(exc),
                )
            else:
                open_market_count = int(market_checker_report.get('open_market_count') or 0)
                latest_snapshot_age = age_seconds(market_checker_report.get('latest_snapshot_at'), now=now)
                market_checker_report['latest_snapshot_age_seconds'] = round(latest_snapshot_age, 1) if latest_snapshot_age is not None else None
                if open_market_count > 0 and latest_snapshot_age is None:
                    add_issue(
                        issues,
                        level='error',
                        code='missing_market_snapshots',
                        message='No market snapshot timestamp found for open polymarket markets',
                        market_checker=market_checker_report,
                    )
                elif latest_snapshot_age is not None and latest_snapshot_age > float(args.max_market_snapshot_age_seconds):
                    add_issue(
                        issues,
                        level='error',
                        code='stale_market_checker',
                        message='Market snapshot feed appears stale',
                        age_seconds=round(latest_snapshot_age, 1),
                        max_age_seconds=float(args.max_market_snapshot_age_seconds),
                        market_checker=market_checker_report,
                    )
                elif open_market_count == 0:
                    add_issue(
                        issues,
                        level='warn',
                        code='no_open_polymarket_markets',
                        message='Market checker found no open polymarket markets to monitor',
                        market_checker=market_checker_report,
                    )

    if any(issue['level'] == 'error' for issue in issues):
        status = 'error'
        exit_code = 2
    elif issues:
        status = 'warn'
        exit_code = 1
    else:
        status = 'ok'
        exit_code = 0

    report = {
        'status': status,
        'exit_code': exit_code,
        'checked_at': now.isoformat().replace('+00:00', 'Z'),
        'heartbeat_file': str(heartbeat_path),
        'quarantine_file': str(quarantine_path),
        'report_file': str(report_path),
        'artifact_contract_root': str(artifact_contract_root),
        'artifact_contract_report_file': str(artifact_contract_report_path),
        'decided_market_watcher_heartbeat_file': str(decided_market_watcher_heartbeat_path),
        'market_checker_env_file': str(market_checker_env_file),
        'market_checker_psql': str(args.market_checker_psql),
        'heartbeat': {
            'state': heartbeat.get('state'),
            'pid': heartbeat.get('pid'),
            'started_at': heartbeat.get('started_at'),
            'last_loop_started_at': heartbeat.get('last_loop_started_at'),
            'last_loop_completed_at': heartbeat.get('last_loop_completed_at'),
            'processed_cases_total': heartbeat.get('processed_cases_total'),
            'last_pass': heartbeat.get('last_pass', {}),
            'last_resolution_sync': heartbeat.get('last_resolution_sync', {}),
            'last_brier_snapshot': heartbeat.get('last_brier_snapshot', {}),
        },
        'quarantine_count': quarantine_count,
        'artifact_contract': artifact_contract_report,
        'decided_market_watcher': decided_market_watcher_report,
        'market_checker': market_checker_report,
        'issues': issues,
    }
    write_json_file(report_path, report)
    return report


def main() -> int:
    args = parse_args()
    report = evaluate(args)
    print(json.dumps(report, indent=2 if args.pretty else None))
    return int(report.get('exit_code', 2))


if __name__ == '__main__':
    raise SystemExit(main())
