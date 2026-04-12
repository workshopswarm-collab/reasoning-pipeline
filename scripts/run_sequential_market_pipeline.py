#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fcntl
import json
import os
import subprocess
import sys
import time
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Any, Iterator

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "scripts"))

from automation_control import DEFAULT_CONTROL_FILE, load_control_file, resolve_sequencer_policy  # noqa: E402
from case_pipeline_status import list_case_pipeline_statuses, pipeline_status_path, summarize_case_pipeline_status, update_case_pipeline_status  # noqa: E402
from watch_pipeline import watch_case as reconcile_existing_case_via_watchdog  # noqa: E402

PREPARE_AND_LAUNCH = REPO_ROOT / "roles" / "orchestrator" / "researchers-swarm-subagents" / "runtime" / "scripts" / "prepare_and_launch_headless_telegram_dispatch.py"
SELECT_REFRESH_CASE = REPO_ROOT / "roles" / "orchestrator" / "researchers-swarm-subagents" / "planner" / "scripts" / "select_refresh_case.py"
OPEN_CASE = REPO_ROOT / "roles" / "orchestrator" / "researchers-swarm-subagents" / "planner" / "scripts" / "open_case.py"
RESUME_SWARM_STAGE = REPO_ROOT / "roles" / "orchestrator" / "researchers-swarm-subagents" / "runtime" / "scripts" / "resume_swarm_stage.py"
LAUNCH_SYNTHESIS_IF_READY = REPO_ROOT / "roles" / "orchestrator" / "synthesis-subagent" / "runtime" / "scripts" / "launch_synthesis_if_ready.py"
RUN_DECISION_MAKER = REPO_ROOT / "roles" / "decision-maker" / "runtime" / "scripts" / "run_decision_maker.py"
RUN_LIGHT_REFRESH_UPDATE = REPO_ROOT / "roles" / "decision-maker" / "runtime" / "scripts" / "run_light_refresh_update.py"
SYNC_MARKET_RESOLUTIONS = REPO_ROOT / "quant-db" / "scripts" / "sync_polymarket_market_resolutions.py"
SCORE_BRIER = REPO_ROOT / "quant-db" / "scripts" / "score_brier.py"
DEFAULT_BRIER_OUTPUT_DIR = REPO_ROOT / "quant-db" / "reports" / "brier"
DEFAULT_HEARTBEAT_FILE = REPO_ROOT / "scripts" / ".runtime-state" / "pipeline-heartbeat.json"
DEFAULT_QUARANTINE_FILE = REPO_ROOT / "scripts" / ".runtime-state" / "pipeline-quarantine.json"
DEFAULT_LOCK = REPO_ROOT / "scripts" / ".runtime-state" / "pipeline-sequencer.lock"
NO_WORK_MARKERS = (
    'no eligible market found',
    'pipeline already busy with an open researching case',
)
FULL_REFRESH_PRICE_DELTA = 0.12
FULL_REFRESH_STALE_HOURS = 12.0
FULL_REFRESH_CLOSE_HOURS = 12.0


class RunnerError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the reasoning pipeline sequentially over available markets")
    parser.add_argument("--max-cases", type=int, default=1, help="Maximum number of markets to process; use 0 to run until no more are available")
    parser.add_argument("--poll-seconds", type=float, default=15.0, help="Polling interval while watching pipeline status")
    parser.add_argument("--idle-seconds", type=float, default=60.0, help="Sleep interval between loop passes when idle/disabled")
    parser.add_argument("--max-case-seconds", type=float, default=7200.0, help="Maximum seconds to wait for one case before failing")
    parser.add_argument("--resume-existing", action="store_true", default=True, help="Resume the most recently updated non-terminal case before claiming a new one")
    parser.add_argument("--no-resume-existing", dest="resume_existing", action="store_false", help="Do not resume an existing non-terminal case")
    parser.add_argument("--loop", action="store_true", help="Run continuously instead of a single pass")
    parser.add_argument("--control-managed", action="store_true", help="Load sequencer behavior from the persisted automation control file each pass")
    parser.add_argument("--control-file", default=str(DEFAULT_CONTROL_FILE), help="Automation control file path used with --control-managed")
    parser.add_argument("--lock-file", default=str(DEFAULT_LOCK), help="Process lock to prevent concurrent sequencer loops")
    parser.add_argument("--resolution-sync-seconds", type=float, default=900.0, help="Cadence for Polymarket resolution sync while looping; set <=0 to disable")
    parser.add_argument("--brier-snapshot-seconds", type=float, default=86400.0, help="Cadence for persisted Brier snapshots while looping; set <=0 to disable")
    parser.add_argument("--brier-output-dir", default=str(DEFAULT_BRIER_OUTPUT_DIR), help="Directory for persisted Brier snapshot JSON files")
    parser.add_argument("--heartbeat-file", default=str(DEFAULT_HEARTBEAT_FILE), help="Sequencer heartbeat/status JSON path")
    parser.add_argument("--quarantine-file", default=str(DEFAULT_QUARANTINE_FILE), help="JSON registry for temporarily quarantined case_keys/market_ids")
    parser.add_argument("--quarantine-seconds", type=float, default=3600.0, help="How long to quarantine a failed case/market before retrying")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def load_repo_env() -> dict[str, str]:
    env = dict(os.environ)
    for env_name in [".env", ".env.postgres.local"]:
        env_file = REPO_ROOT / env_name
        if not env_file.exists():
            continue
        for raw_line in env_file.read_text().splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            if line.startswith("export "):
                line = line[len("export "):].strip()
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in env:
                env[key] = value
    return env


@contextmanager
def process_lock(path: Path) -> Iterator[None]:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+', encoding='utf-8') as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:  # noqa: PERF203
            raise RunnerError(f'another sequencer instance already holds {path}') from exc
        try:
            handle.seek(0)
            handle.truncate()
            handle.write(str(os.getpid()))
            handle.flush()
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def utc_now_iso() -> str:
    return datetime.utcnow().isoformat() + 'Z'


def load_quarantine_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {'schema_version': 'pipeline-quarantine/v1', 'updated_at': '', 'entries': []}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {'schema_version': 'pipeline-quarantine/v1', 'updated_at': '', 'entries': []}
    if not isinstance(payload, dict):
        return {'schema_version': 'pipeline-quarantine/v1', 'updated_at': '', 'entries': []}
    entries = payload.get('entries')
    if not isinstance(entries, list):
        payload['entries'] = []
    payload.setdefault('schema_version', 'pipeline-quarantine/v1')
    payload.setdefault('updated_at', '')
    return payload


def write_runtime_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')


def save_quarantine_registry(path: Path, payload: dict[str, Any]) -> None:
    write_runtime_json(path, payload)


def prune_quarantine_entries(payload: dict[str, Any], *, now_ts: float) -> dict[str, Any]:
    kept: list[dict[str, Any]] = []
    for entry in list(payload.get('entries') or []):
        try:
            release_at = float(entry.get('release_at_ts'))
        except Exception:
            release_at = 0.0
        if release_at > now_ts:
            kept.append(entry)
    payload['entries'] = kept
    payload['updated_at'] = utc_now_iso()
    return payload


def active_quarantine_sets(payload: dict[str, Any]) -> tuple[set[str], set[str]]:
    case_keys: set[str] = set()
    market_ids: set[str] = set()
    for entry in payload.get('entries') or []:
        case_key = str(entry.get('case_key') or '').strip()
        market_id = str(entry.get('market_id') or '').strip()
        if case_key:
            case_keys.add(case_key)
        if market_id:
            market_ids.add(market_id)
    return case_keys, market_ids


def load_heartbeat(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {'schema_version': 'pipeline-heartbeat/v1'}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {'schema_version': 'pipeline-heartbeat/v1'}
    return payload if isinstance(payload, dict) else {'schema_version': 'pipeline-heartbeat/v1'}


def write_heartbeat(path: Path, payload: dict[str, Any]) -> None:
    payload['schema_version'] = 'pipeline-heartbeat/v1'
    payload['updated_at'] = utc_now_iso()
    write_runtime_json(path, payload)


def quarantine_entry(path: Path, *, case_key: str = '', market_id: str = '', reason: str, result: dict[str, Any], quarantine_seconds: float) -> dict[str, Any]:
    payload = prune_quarantine_entries(load_quarantine_registry(path), now_ts=time.time())
    now_ts = time.time()
    entry = {
        'case_key': case_key,
        'market_id': market_id,
        'reason': reason,
        'quarantined_at': utc_now_iso(),
        'quarantined_at_ts': now_ts,
        'release_at_ts': now_ts + float(quarantine_seconds),
        'result_status': str(result.get('status') or ''),
        'result_ok': bool(result.get('ok')),
    }
    payload.setdefault('entries', []).append(entry)
    payload['updated_at'] = utc_now_iso()
    save_quarantine_registry(path, payload)
    return entry


def extract_case_market_refs(result: dict[str, Any]) -> tuple[str, str]:
    case_key = str(result.get('case_key') or '').strip()
    market_id = ''
    for candidate in [
        result.get('market_id'),
        ((result.get('pipeline_summary') or {}) if isinstance(result.get('pipeline_summary'), dict) else {}).get('market_id'),
        ((result.get('refresh_candidate') or {}) if isinstance(result.get('refresh_candidate'), dict) else {}).get('market_id'),
        (((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary') or {}).get('market_id') if isinstance(((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary'), dict) else '',
    ]:
        text = str(candidate or '').strip()
        if text and not market_id:
            market_id = text
    if not case_key:
        for candidate in [
            ((result.get('refresh_candidate') or {}) if isinstance(result.get('refresh_candidate'), dict) else {}).get('case_key'),
            ((result.get('refresh_candidate') or {}) if isinstance(result.get('refresh_candidate'), dict) else {}).get('latest_forecast_case_key'),
            ((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('case_key'),
            (((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary') or {}).get('case_key') if isinstance(((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary'), dict) else '',
        ]:
            text = str(candidate or '').strip()
            if text:
                case_key = text
                break
    return case_key, market_id


def soft_fail_status(result: dict[str, Any]) -> bool:
    status = str(result.get('status') or '')
    return status in {
        'processed_existing_case',
        'processed_new_case',
        'processed_refresh_case',
        'processed_light_refresh_case',
        'refresh_open_case_failed',
        'light_refresh_missing_case_key',
        'prepare_launch_failed',
        'prepare_unknown_failure',
    }


def heartbeat_base(args: argparse.Namespace) -> dict[str, Any]:
    return {
        'runner': 'pipeline-sequencer',
        'pid': os.getpid(),
        'repo_root': str(REPO_ROOT),
        'loop_mode': bool(args.loop),
        'control_managed': bool(args.control_managed),
        'lock_file': str(Path(args.lock_file).expanduser().resolve()),
        'heartbeat_file': str(Path(args.heartbeat_file).expanduser().resolve()),
        'quarantine_file': str(Path(args.quarantine_file).expanduser().resolve()),
        'brier_output_dir': str(Path(args.brier_output_dir).expanduser().resolve()),
        'config': {
            'poll_seconds': float(args.poll_seconds),
            'idle_seconds': float(args.idle_seconds),
            'max_case_seconds': float(args.max_case_seconds),
            'resolution_sync_seconds': float(args.resolution_sync_seconds),
            'brier_snapshot_seconds': float(args.brier_snapshot_seconds),
            'quarantine_seconds': float(args.quarantine_seconds),
        },
        'started_at': utc_now_iso(),
        'state': 'starting',
        'processed_cases_total': 0,
        'quarantine_count': 0,
    }


def periodic_task_brief(task: dict[str, Any]) -> dict[str, Any]:
    payload = task.get('payload') if isinstance(task, dict) else {}
    summary: dict[str, Any] = {
        'ok': bool(task.get('ok')) if isinstance(task, dict) else False,
        'returncode': int(task.get('returncode')) if isinstance(task, dict) and str(task.get('returncode') or '').isdigit() else task.get('returncode') if isinstance(task, dict) else None,
    }
    if isinstance(payload, dict):
        for key in ['candidate_count', 'group_count', 'filters']:
            if key in payload:
                summary[key] = payload.get(key)
    persisted_paths = task.get('persisted_paths') if isinstance(task, dict) else None
    if isinstance(persisted_paths, dict):
        summary['persisted_paths'] = persisted_paths
    stderr = str(task.get('stderr') or '') if isinstance(task, dict) else ''
    if stderr:
        summary['stderr_tail'] = stderr[-500:]
    return summary


def update_heartbeat_for_periodic_tasks(heartbeat: dict[str, Any], periodic_tasks: dict[str, Any]) -> dict[str, Any]:
    if 'resolution_sync' in periodic_tasks:
        heartbeat['last_resolution_sync'] = {
            'attempted_at': utc_now_iso(),
            **periodic_task_brief(periodic_tasks['resolution_sync']),
        }
        if periodic_tasks['resolution_sync'].get('ok'):
            heartbeat['last_resolution_sync']['succeeded_at'] = utc_now_iso()
    if 'brier_snapshot' in periodic_tasks:
        heartbeat['last_brier_snapshot'] = {
            'attempted_at': utc_now_iso(),
            **periodic_task_brief(periodic_tasks['brier_snapshot']),
        }
        if periodic_tasks['brier_snapshot'].get('ok'):
            heartbeat['last_brier_snapshot']['succeeded_at'] = utc_now_iso()
    return heartbeat


def update_heartbeat_for_pass(heartbeat: dict[str, Any], *, result: dict[str, Any], processed_cases: int, periodic_tasks: dict[str, Any], excluded_case_keys: set[str], excluded_market_ids: set[str]) -> dict[str, Any]:
    case_key, market_id = extract_case_market_refs(result)
    heartbeat['state'] = 'running'
    heartbeat['processed_cases_total'] = processed_cases
    heartbeat['last_loop_completed_at'] = utc_now_iso()
    heartbeat['last_pass'] = {
        'status': str(result.get('status') or ''),
        'ok': bool(result.get('ok')),
        'soft_failed': bool(result.get('soft_failed')),
        'case_key': case_key,
        'market_id': market_id,
        'periodic_tasks_ran': sorted(list(periodic_tasks.keys())),
    }
    heartbeat['quarantine_count'] = len(excluded_case_keys) + len(excluded_market_ids)
    heartbeat['active_quarantines'] = {
        'case_keys': sorted(excluded_case_keys),
        'market_ids': sorted(excluded_market_ids),
    }
    if not result.get('ok'):
        heartbeat['last_hard_failure'] = {
            'at': utc_now_iso(),
            'status': str(result.get('status') or result.get('error') or 'unknown_failure'),
            'case_key': case_key,
            'market_id': market_id,
        }
    elif result.get('soft_failed'):
        heartbeat['last_soft_failure'] = {
            'at': utc_now_iso(),
            'status': str(result.get('status') or ''),
            'case_key': case_key,
            'market_id': market_id,
        }
    return update_heartbeat_for_periodic_tasks(heartbeat, periodic_tasks)


def maybe_quarantine_failed_result(*, args: argparse.Namespace, result: dict[str, Any]) -> dict[str, Any] | None:
    if bool(result.get('ok')):
        return None
    if not soft_fail_status(result) and not result.get('refresh_candidate'):
        return None
    case_key, market_id = extract_case_market_refs(result)
    if not case_key and not market_id:
        return None
    reason = str(result.get('status') or result.get('error') or 'soft_fail')
    entry = quarantine_entry(
        Path(args.quarantine_file).expanduser().resolve(),
        case_key=case_key,
        market_id=market_id,
        reason=reason,
        result=result,
        quarantine_seconds=float(args.quarantine_seconds),
    )
    if case_key:
        update_case_pipeline_status(
            case_key=case_key,
            status='pipeline_failed',
            current_stage=str((((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary') or {}).get('current_stage') if isinstance((((result.get('case_result') or {}) if isinstance(result.get('case_result'), dict) else {}).get('pipeline_summary')), dict) else 'decision'),
            runner_id='run_sequential_market_pipeline',
            message='Sequential runner soft-failed and quarantined the case for later retry',
            extra={'quarantine': entry, 'soft_failed_result_status': result.get('status', '')},
            terminal_summary_patch={'failure_reason': reason, 'quarantined': True},
        )
    return entry


def effective_sequencer_policy(args: argparse.Namespace) -> dict[str, Any]:
    policy = {
        'enabled': True,
        'resume_existing': bool(args.resume_existing),
        'allow_new_case_claims': True,
        'poll_seconds': float(args.poll_seconds),
        'idle_seconds': float(args.idle_seconds),
        'max_case_seconds': float(args.max_case_seconds),
        'control_managed': bool(args.control_managed),
        'control_file': str(Path(args.control_file).expanduser().resolve()),
    }
    if args.control_managed:
        control = load_control_file(Path(args.control_file).expanduser().resolve())
        control_policy = resolve_sequencer_policy(control)
        policy.update({
            'enabled': bool(control_policy.get('enabled')),
            'resume_existing': bool(control_policy.get('resume_existing')),
            'allow_new_case_claims': bool(control_policy.get('allow_new_case_claims')),
            'poll_seconds': float(control_policy.get('poll_seconds')),
            'idle_seconds': float(control_policy.get('idle_seconds')),
            'max_case_seconds': float(control_policy.get('max_case_seconds')),
            'control_snapshot': control,
            'automation_enabled': bool(control_policy.get('automation_enabled')),
        })
    return policy


def run_json_command(cmd: list[str]) -> tuple[int, dict[str, Any], str, str]:
    proc = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True, env=load_repo_env())
    payload: dict[str, Any] = {}
    text = (proc.stdout or "").strip()
    if text:
        candidates = [text, text.splitlines()[-1].strip()]
        for candidate in candidates:
            try:
                parsed = json.loads(candidate)
                if isinstance(parsed, dict):
                    payload = parsed
                    break
            except json.JSONDecodeError:
                continue
    return proc.returncode, payload, proc.stdout, proc.stderr


def prepare_and_launch_case(pretty: bool, *, case_id: str = "") -> dict[str, Any] | None:
    cmd = [sys.executable, str(PREPARE_AND_LAUNCH)]
    if case_id:
        cmd.extend(["--case-id", case_id])
    if pretty:
        cmd.append("--pretty")
    code, payload, stdout, stderr = run_json_command(cmd)
    if code != 0:
        if payload:
            return {"ok": False, "payload": payload, "stdout": stdout, "stderr": stderr, "returncode": code}
        return None
    return {"ok": True, "payload": payload, "stdout": stdout, "stderr": stderr, "returncode": code}


def launch_decision_maker(case_key: str, pretty: bool) -> dict[str, Any]:
    cmd = [sys.executable, str(RUN_DECISION_MAKER), "--case-key", case_key]
    if pretty:
        cmd.append("--pretty")
    code, payload, stdout, stderr = run_json_command(cmd)
    return {
        "ok": code == 0,
        "payload": payload,
        "stdout": stdout,
        "stderr": stderr,
        "returncode": code,
    }


def run_light_refresh_update(case_key: str, pretty: bool) -> dict[str, Any]:
    cmd = [sys.executable, str(RUN_LIGHT_REFRESH_UPDATE), "--case-key", case_key]
    if pretty:
        cmd.append("--pretty")
    code, payload, stdout, stderr = run_json_command(cmd)
    return {
        "ok": code == 0,
        "payload": payload,
        "stdout": stdout,
        "stderr": stderr,
        "returncode": code,
    }


def decide_refresh_mode(refresh_payload: dict[str, Any]) -> dict[str, Any]:
    try:
        price_delta = float(refresh_payload.get('price_delta')) if refresh_payload.get('price_delta') not in (None, '') else None
    except Exception:
        price_delta = None
    try:
        hours_since_last_forecast = float(refresh_payload.get('hours_since_last_forecast')) if refresh_payload.get('hours_since_last_forecast') not in (None, '') else None
    except Exception:
        hours_since_last_forecast = None
    try:
        hours_to_close = float(refresh_payload.get('hours_to_close')) if refresh_payload.get('hours_to_close') not in (None, '') else None
    except Exception:
        hours_to_close = None

    reasons: list[str] = []
    if price_delta is not None and price_delta >= FULL_REFRESH_PRICE_DELTA:
        reasons.append('large_price_move')
    if hours_since_last_forecast is not None and hours_since_last_forecast >= FULL_REFRESH_STALE_HOURS:
        reasons.append('stale_forecast')
    if hours_to_close is not None and hours_to_close <= FULL_REFRESH_CLOSE_HOURS:
        reasons.append('near_close')
    if reasons:
        return {'mode': 'full', 'reasons': reasons}
    return {'mode': 'light', 'reasons': ['material_price_move']}


def run_resolution_sync(pretty: bool) -> dict[str, Any]:
    cmd = [sys.executable, str(SYNC_MARKET_RESOLUTIONS)]
    if pretty:
        cmd.append('--pretty')
    code, payload, stdout, stderr = run_json_command(cmd)
    return {
        'ok': code == 0,
        'payload': payload,
        'stdout': stdout,
        'stderr': stderr,
        'returncode': code,
    }


def persist_brier_snapshot(result: dict[str, Any], *, output_dir: Path) -> dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    daily_dir = output_dir / 'daily'
    daily_dir.mkdir(parents=True, exist_ok=True)
    date_key = datetime.now().astimezone().date().isoformat()
    latest_path = output_dir / 'latest.json'
    daily_path = daily_dir / f'{date_key}.json'
    payload = {
        'generated_at': datetime.now().astimezone().isoformat(),
        'date': date_key,
        'metrics': result,
    }
    latest_path.write_text(json.dumps(payload, indent=2) + '\n')
    daily_path.write_text(json.dumps(payload, indent=2) + '\n')
    return {
        'latest_path': str(latest_path.relative_to(REPO_ROOT)),
        'daily_path': str(daily_path.relative_to(REPO_ROOT)),
    }


def run_brier_snapshot(pretty: bool, *, output_dir: Path) -> dict[str, Any]:
    cmd = [sys.executable, str(SCORE_BRIER), '--pretty']
    if not pretty:
        cmd = [sys.executable, str(SCORE_BRIER)]
    code, payload, stdout, stderr = run_json_command(cmd)
    result = {
        'ok': code == 0,
        'payload': payload,
        'stdout': stdout,
        'stderr': stderr,
        'returncode': code,
    }
    if code == 0 and payload:
        result['persisted_paths'] = persist_brier_snapshot(payload, output_dir=output_dir)
    return result


def maybe_run_periodic_tasks(*, args: argparse.Namespace, policy: dict[str, Any], now_ts: float, last_resolution_sync_ts: float | None, last_brier_snapshot_ts: float | None) -> tuple[dict[str, Any], float | None, float | None]:
    tasks: dict[str, Any] = {}
    resolution_cadence = float(args.resolution_sync_seconds)
    if resolution_cadence > 0 and (last_resolution_sync_ts is None or (now_ts - last_resolution_sync_ts) >= resolution_cadence):
        result = run_resolution_sync(pretty=args.pretty)
        tasks['resolution_sync'] = result
        if result.get('ok'):
            last_resolution_sync_ts = now_ts

    brier_cadence = float(args.brier_snapshot_seconds)
    if brier_cadence > 0 and (last_brier_snapshot_ts is None or (now_ts - last_brier_snapshot_ts) >= brier_cadence):
        result = run_brier_snapshot(pretty=args.pretty, output_dir=Path(args.brier_output_dir).expanduser().resolve())
        tasks['brier_snapshot'] = result
        if result.get('ok'):
            last_brier_snapshot_ts = now_ts

    return tasks, last_resolution_sync_ts, last_brier_snapshot_ts


def resume_swarm_stage(case_key: str, pretty: bool) -> dict[str, Any]:
    cmd = [sys.executable, str(RESUME_SWARM_STAGE), '--case-key', case_key]
    if pretty:
        cmd.append('--pretty')
    code, payload, stdout, stderr = run_json_command(cmd)
    return {
        'ok': code == 0,
        'payload': payload,
        'stdout': stdout,
        'stderr': stderr,
        'returncode': code,
    }


def latest_dispatch_dir(case_key: str) -> Path | None:
    analyses_root = REPO_ROOT / "qualitative-db" / "40-research" / "cases" / case_key / "researcher-analyses"
    if not analyses_root.exists():
        return None
    candidates = sorted(analyses_root.glob("*/dispatch-case-*"), key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0] if candidates else None


def synthesis_status_file(case_key: str) -> Path | None:
    dispatch_dir = latest_dispatch_dir(case_key)
    if dispatch_dir is None:
        return None
    path = dispatch_dir / "synthesis-stage-status.json"
    return path if path.exists() else None


def launch_synthesis_if_needed(case_key: str, pretty: bool) -> dict[str, Any] | None:
    status_file = synthesis_status_file(case_key)
    if status_file is None:
        return None
    cmd = [sys.executable, str(LAUNCH_SYNTHESIS_IF_READY), "--status-file", str(status_file)]
    if pretty:
        cmd.append("--pretty")
    code, payload, stdout, stderr = run_json_command(cmd)
    return {
        "ok": code == 0,
        "payload": payload,
        "stdout": stdout,
        "stderr": stderr,
        "returncode": code,
        "status_file": str(status_file.relative_to(REPO_ROOT)),
    }


def wait_for_case(case_key: str, *, poll_seconds: float, max_case_seconds: float, pretty: bool) -> dict[str, Any]:
    path = pipeline_status_path(case_key)
    deadline = time.time() + max_case_seconds
    watchdog_passes = 0
    last_watchdog_result: dict[str, Any] | None = None
    watchdog_args = argparse.Namespace(stale_seconds=900.0, pretty=pretty)
    watchdog_policy = {
        'apply': True,
        'allow_resume_swarm': True,
        'allow_launch_synthesis': True,
        'allow_launch_decision': True,
        'allow_finalize_decision': True,
        'allow_finalize_pipeline': True,
    }

    while time.time() < deadline:
        summary = summarize_case_pipeline_status(case_key)
        status = summary.get('status') or ''

        if pretty:
            print(json.dumps({
                'case_key': case_key,
                'pipeline_status_path': summary.get('path'),
                'status': status,
                'current_stage': summary.get('current_stage'),
                'stage_statuses': summary.get('stage_statuses') or {},
            }, indent=2))

        if status in {'pipeline_completed', 'pipeline_failed', 'pipeline_skipped'}:
            return {
                'ok': status == 'pipeline_completed',
                'case_key': case_key,
                'pipeline_summary': summary,
                'watchdog_passes': watchdog_passes,
                'last_watchdog_result': last_watchdog_result or {},
            }

        last_watchdog_result = reconcile_existing_case_via_watchdog(summary, args=watchdog_args, policy=watchdog_policy)
        watchdog_passes += 1
        if not last_watchdog_result.get('ok', False):
            return {
                'ok': False,
                'case_key': case_key,
                'error': 'watchdog_reconcile_failed',
                'watchdog_result': last_watchdog_result,
                'pipeline_summary': summarize_case_pipeline_status(case_key),
            }

        after = last_watchdog_result.get('after') if isinstance(last_watchdog_result.get('after'), dict) else summarize_case_pipeline_status(case_key)
        after_status = str(after.get('status') or '')
        if after_status in {'pipeline_completed', 'pipeline_failed', 'pipeline_skipped'}:
            return {
                'ok': after_status == 'pipeline_completed',
                'case_key': case_key,
                'pipeline_summary': after,
                'watchdog_passes': watchdog_passes,
                'last_watchdog_result': last_watchdog_result or {},
            }

        time.sleep(poll_seconds)

    return {
        'ok': False,
        'case_key': case_key,
        'error': 'pipeline_timeout',
        'pipeline_summary': summarize_case_pipeline_status(case_key),
        'pipeline_status_path': str(path),
        'watchdog_passes': watchdog_passes,
        'last_watchdog_result': last_watchdog_result or {},
    }


def pick_resumable_case(*, excluded_case_keys: set[str], excluded_market_ids: set[str]) -> dict[str, Any] | None:
    active = list_case_pipeline_statuses(include_terminal=False)
    for item in active:
        case_key = str(item.get('case_key') or '').strip()
        market_id = str(item.get('market_id') or '').strip()
        if case_key and case_key in excluded_case_keys:
            continue
        if market_id and market_id in excluded_market_ids:
            continue
        return item
    return None


def select_refresh_case(pretty: bool, *, excluded_market_ids: set[str], excluded_case_keys: set[str]) -> dict[str, Any] | None:
    cmd = [sys.executable, str(SELECT_REFRESH_CASE)]
    for market_id in sorted(excluded_market_ids):
        cmd.extend(['--exclude-market-id', market_id])
    for case_key in sorted(excluded_case_keys):
        cmd.extend(['--exclude-case-key', case_key])
    if pretty:
        cmd.append("--pretty")
    code, payload, stdout, stderr = run_json_command(cmd)
    if code != 0:
        if payload:
            return {"ok": False, "payload": payload, "stdout": stdout, "stderr": stderr, "returncode": code}
        return {"ok": False, "payload": {}, "stdout": stdout, "stderr": stderr, "returncode": code}
    return {"ok": True, "payload": payload, "stdout": stdout, "stderr": stderr, "returncode": code}


def open_case_for_market(*, market_id: str, pretty: bool) -> dict[str, Any] | None:
    cmd = [sys.executable, str(OPEN_CASE), "--market-id", market_id]
    if pretty:
        cmd.append("--pretty")
    code, payload, stdout, stderr = run_json_command(cmd)
    if code != 0:
        if payload:
            return {"ok": False, "payload": payload, "stdout": stdout, "stderr": stderr, "returncode": code}
        return {"ok": False, "payload": {}, "stdout": stdout, "stderr": stderr, "returncode": code}
    return {"ok": True, "payload": payload, "stdout": stdout, "stderr": stderr, "returncode": code}


def classify_prepare_failure(prepared: dict[str, Any] | None) -> str:
    if prepared is None:
        return 'prepare_unknown_failure'
    payload = prepared.get('payload') or {}
    combined = '\n'.join([
        str(payload.get('status') or ''),
        str((payload.get('prepare_result') or {}).get('status') or ''),
        str(prepared.get('stdout') or ''),
        str(prepared.get('stderr') or ''),
        str(payload.get('prepare_stdout') or ''),
        str(payload.get('prepare_stderr') or ''),
    ]).lower()
    if 'pipeline already busy with an open researching case' in combined:
        return 'idle_pipeline_busy'
    if 'no eligible market found' in combined:
        return 'idle_no_eligible_market'
    return 'prepare_launch_failed'


def run_sequencer_pass(args: argparse.Namespace, policy: dict[str, Any], *, excluded_case_keys: set[str], excluded_market_ids: set[str]) -> dict[str, Any]:
    if not policy.get('enabled', True):
        return {
            'ok': True,
            'status': 'sequencer_disabled',
            'policy': policy,
        }

    resumable = pick_resumable_case(excluded_case_keys=excluded_case_keys, excluded_market_ids=excluded_market_ids) if policy.get('resume_existing') else None
    if resumable:
        case_key = str(resumable.get("case_key") or "").strip()
        if not case_key:
            raise RunnerError("resumable pipeline status is missing case_key")
        update_case_pipeline_status(
            case_key=case_key,
            dispatch_id=str(resumable.get("dispatch_id") or "").strip(),
            market_id=str(resumable.get("market_id") or "").strip(),
            market_title=str(resumable.get("market_title") or "").strip(),
            status=str(resumable.get("status") or "pipeline_in_progress"),
            current_stage=str(resumable.get("current_stage") or "swarm"),
            runner_id="run_sequential_market_pipeline",
            message="Sequential runner resumed existing in-flight case",
        )
        case_result = wait_for_case(
            case_key,
            poll_seconds=float(policy['poll_seconds']),
            max_case_seconds=float(policy['max_case_seconds']),
            pretty=args.pretty,
        )
        return {
            'ok': bool(case_result.get('ok')),
            'status': 'processed_existing_case',
            'policy': policy,
            'case_key': case_key,
            'case_result': case_result,
        }

    refresh_candidate = select_refresh_case(pretty=args.pretty, excluded_market_ids=excluded_market_ids, excluded_case_keys=excluded_case_keys)
    if refresh_candidate and refresh_candidate.get('ok'):
        refresh_payload = refresh_candidate.get('payload') or {}
        refresh_plan = decide_refresh_mode(refresh_payload)
        refresh_mode = str(refresh_plan.get('mode') or 'light')

        if refresh_mode == 'light':
            refresh_case_key = str(refresh_payload.get('case_key') or refresh_payload.get('latest_forecast_case_key') or '').strip()
            if not refresh_case_key:
                return {
                    'ok': False,
                    'status': 'light_refresh_missing_case_key',
                    'policy': policy,
                    'refresh_candidate': refresh_candidate,
                    'refresh_plan': refresh_plan,
                }
            update_case_pipeline_status(
                case_key=refresh_case_key,
                dispatch_id='',
                market_id=str(refresh_payload.get('market_id') or '').strip(),
                market_title=str(refresh_payload.get('title') or '').strip(),
                status='pipeline_started',
                current_stage='decision',
                stage_status_patch={
                    'decision': 'in_progress',
                },
                runner_id='run_sequential_market_pipeline',
                message='Sequential runner launched lightweight prior refresh after material market movement',
                extra={
                    'refresh_candidate': refresh_payload,
                    'refresh_plan': refresh_plan,
                },
            )
            light_refresh_result = run_light_refresh_update(refresh_case_key, pretty=args.pretty)
            return {
                'ok': bool(light_refresh_result.get('ok')),
                'status': 'processed_light_refresh_case',
                'policy': policy,
                'case_key': refresh_case_key,
                'refresh_candidate': refresh_candidate,
                'refresh_plan': refresh_plan,
                'light_refresh_result': light_refresh_result,
            }

        refresh_case_id = str(refresh_payload.get('case_id') or '').strip()
        if not refresh_case_id:
            opened_case = open_case_for_market(market_id=str(refresh_payload.get('market_id') or '').strip(), pretty=args.pretty)
            if not opened_case or not opened_case.get('ok'):
                return {
                    'ok': False,
                    'status': 'refresh_open_case_failed',
                    'policy': policy,
                    'refresh_candidate': refresh_candidate,
                    'refresh_plan': refresh_plan,
                    'open_case_result': opened_case,
                }
            refresh_payload.update(opened_case.get('payload') or {})
            refresh_case_id = str(refresh_payload.get('case_id') or '').strip()
        refresh_case_key = str(refresh_payload.get('case_key') or '').strip()
        prepared = prepare_and_launch_case(pretty=args.pretty, case_id=refresh_case_id)
        if not prepared:
            return {
                'ok': False,
                'status': 'prepare_unknown_failure',
                'policy': policy,
                'refresh_candidate': refresh_candidate,
                'refresh_plan': refresh_plan,
            }
        payload = prepared.get("payload") or {}
        if not prepared.get("ok"):
            failure_kind = classify_prepare_failure(prepared)
            return {
                'ok': failure_kind in {'idle_pipeline_busy', 'idle_no_eligible_market'},
                'status': failure_kind,
                'policy': policy,
                'refresh_candidate': refresh_candidate,
                'refresh_plan': refresh_plan,
                'prepare_result': prepared,
            }

        prepare_result = payload.get("prepare_result") or {}
        case_payload = prepare_result.get("case") or {}
        market_payload = prepare_result.get("market") or {}
        dispatch_payload = prepare_result.get("dispatch") or {}
        case_key = str(case_payload.get("case_key") or refresh_case_key or case_payload.get("case_id") or "").strip()
        if not case_key:
            raise RunnerError("refresh prepare_and_launch did not return a case_key")

        update_case_pipeline_status(
            case_key=case_key,
            dispatch_id=str(dispatch_payload.get("dispatch_id") or "").strip(),
            market_id=str(market_payload.get("market_id") or refresh_payload.get("market_id") or "").strip(),
            market_title=str(market_payload.get("market_title") or refresh_payload.get("title") or "").strip(),
            status="pipeline_started",
            current_stage="swarm",
            stage_status_patch={
                "dispatch": "launched",
                "swarm": "in_progress",
                "synthesis": "pending",
                "decision": "pending",
            },
            runner_id="run_sequential_market_pipeline",
            message="Sequential runner escalated a tracked market to full re-research after material market movement",
            extra={
                'refresh_candidate': refresh_payload,
                'refresh_plan': refresh_plan,
            },
        )

        case_result = wait_for_case(
            case_key,
            poll_seconds=float(policy['poll_seconds']),
            max_case_seconds=float(policy['max_case_seconds']),
            pretty=args.pretty,
        )
        return {
            'ok': bool(case_result.get('ok')),
            'status': 'processed_refresh_case',
            'policy': policy,
            'case_key': case_key,
            'refresh_candidate': refresh_candidate,
            'refresh_plan': refresh_plan,
            'prepare_result': prepared,
            'case_result': case_result,
        }

    if not policy.get('allow_new_case_claims', False):
        return {
            'ok': True,
            'status': 'claims_disabled_idle',
            'policy': policy,
        }

    prepared = prepare_and_launch_case(pretty=args.pretty)
    if not prepared:
        return {
            'ok': False,
            'status': 'prepare_unknown_failure',
            'policy': policy,
        }

    payload = prepared.get("payload") or {}
    if not prepared.get("ok"):
        failure_kind = classify_prepare_failure(prepared)
        idle = failure_kind in {'idle_pipeline_busy', 'idle_no_eligible_market'}
        return {
            'ok': idle,
            'status': failure_kind,
            'policy': policy,
            'prepare_result': prepared,
        }

    prepare_result = payload.get("prepare_result") or {}
    case_payload = prepare_result.get("case") or {}
    market_payload = prepare_result.get("market") or {}
    dispatch_payload = prepare_result.get("dispatch") or {}
    case_key = str(case_payload.get("case_key") or case_payload.get("case_id") or "").strip()
    if not case_key:
        raise RunnerError("prepare_and_launch did not return a case_key")

    update_case_pipeline_status(
        case_key=case_key,
        dispatch_id=str(dispatch_payload.get("dispatch_id") or "").strip(),
        market_id=str(market_payload.get("market_id") or "").strip(),
        market_title=str(market_payload.get("market_title") or "").strip(),
        status="pipeline_started",
        current_stage="swarm",
        stage_status_patch={
            "dispatch": "launched",
            "swarm": "in_progress",
            "synthesis": "pending",
            "decision": "pending",
        },
        runner_id="run_sequential_market_pipeline",
        message="Sequential runner claimed case and is waiting for synthesis completion",
    )

    case_result = wait_for_case(
        case_key,
        poll_seconds=float(policy['poll_seconds']),
        max_case_seconds=float(policy['max_case_seconds']),
        pretty=args.pretty,
    )
    return {
        'ok': bool(case_result.get('ok')),
        'status': 'processed_new_case',
        'policy': policy,
        'case_key': case_key,
        'prepare_result': prepared,
        'case_result': case_result,
    }


def should_count_processed(result: dict[str, Any]) -> bool:
    return bool(result.get('ok')) and not bool(result.get('soft_failed')) and str(result.get('status') or '') in {'processed_existing_case', 'processed_new_case', 'processed_refresh_case', 'processed_light_refresh_case'}


def single_pass_summary(result: dict[str, Any]) -> dict[str, Any]:
    return {
        'ok': bool(result.get('ok')),
        'processed_cases': 1 if should_count_processed(result) else 0,
        'results': [result],
    }


def loop_pass_payload(result: dict[str, Any], processed_cases: int, periodic_tasks: dict[str, Any]) -> dict[str, Any]:
    return {
        'ok': bool(result.get('ok')),
        'processed_cases': processed_cases,
        'periodic_tasks': periodic_tasks,
        'pass_result': result,
    }


def main() -> None:
    args = parse_args()
    lock_path = Path(args.lock_file).expanduser().resolve()
    heartbeat_path = Path(args.heartbeat_file).expanduser().resolve()
    heartbeat = heartbeat_base(args)
    write_heartbeat(heartbeat_path, heartbeat)
    try:
        with process_lock(lock_path):
            heartbeat['state'] = 'running'
            heartbeat['lock_acquired_at'] = utc_now_iso()
            write_heartbeat(heartbeat_path, heartbeat)

            if not args.loop:
                heartbeat['last_loop_started_at'] = utc_now_iso()
                write_heartbeat(heartbeat_path, heartbeat)
                result = run_sequencer_pass(args, effective_sequencer_policy(args), excluded_case_keys=set(), excluded_market_ids=set())
                heartbeat = update_heartbeat_for_pass(heartbeat, result=result, processed_cases=1 if should_count_processed(result) else 0, periodic_tasks={}, excluded_case_keys=set(), excluded_market_ids=set())
                heartbeat['state'] = 'completed' if result.get('ok') else 'failed'
                write_heartbeat(heartbeat_path, heartbeat)
                summary = single_pass_summary(result)
                print(json.dumps(summary, indent=2 if args.pretty else None))
                if not summary['ok']:
                    raise SystemExit(1)
                return

            processed = 0
            last_resolution_sync_ts: float | None = None
            last_brier_snapshot_ts: float | None = None
            quarantine_path = Path(args.quarantine_file).expanduser().resolve()
            while args.max_cases == 0 or processed < args.max_cases:
                policy = effective_sequencer_policy(args)
                now_ts = time.time()
                quarantine_payload = prune_quarantine_entries(load_quarantine_registry(quarantine_path), now_ts=now_ts)
                save_quarantine_registry(quarantine_path, quarantine_payload)
                excluded_case_keys, excluded_market_ids = active_quarantine_sets(quarantine_payload)
                heartbeat['state'] = 'running'
                heartbeat['last_loop_started_at'] = utc_now_iso()
                heartbeat['quarantine_count'] = len(quarantine_payload.get('entries') or [])
                heartbeat['active_quarantines'] = {
                    'case_keys': sorted(excluded_case_keys),
                    'market_ids': sorted(excluded_market_ids),
                }
                write_heartbeat(heartbeat_path, heartbeat)

                periodic_tasks, last_resolution_sync_ts, last_brier_snapshot_ts = maybe_run_periodic_tasks(
                    args=args,
                    policy=policy,
                    now_ts=now_ts,
                    last_resolution_sync_ts=last_resolution_sync_ts,
                    last_brier_snapshot_ts=last_brier_snapshot_ts,
                )
                result = run_sequencer_pass(args, policy, excluded_case_keys=excluded_case_keys, excluded_market_ids=excluded_market_ids)
                quarantine_entry_payload = maybe_quarantine_failed_result(args=args, result=result)
                if quarantine_entry_payload is not None:
                    periodic_tasks['soft_fail_quarantine'] = quarantine_entry_payload
                    result['ok'] = True
                    result['soft_failed'] = True
                if should_count_processed(result):
                    processed += 1
                heartbeat = update_heartbeat_for_pass(heartbeat, result=result, processed_cases=processed, periodic_tasks=periodic_tasks, excluded_case_keys=excluded_case_keys, excluded_market_ids=excluded_market_ids)
                write_heartbeat(heartbeat_path, heartbeat)
                print(json.dumps(loop_pass_payload(result, processed, periodic_tasks), indent=2 if args.pretty else None), flush=True)
                if not result.get('ok'):
                    heartbeat['state'] = 'failed'
                    write_heartbeat(heartbeat_path, heartbeat)
                    raise SystemExit(1)
                if should_count_processed(result):
                    continue
                heartbeat['state'] = 'idle_sleep'
                heartbeat['last_idle_sleep_started_at'] = utc_now_iso()
                heartbeat['last_idle_sleep_seconds'] = float(policy.get('idle_seconds', args.idle_seconds))
                write_heartbeat(heartbeat_path, heartbeat)
                time.sleep(float(policy.get('idle_seconds', args.idle_seconds)))
    except SystemExit:
        raise
    except Exception as exc:
        heartbeat['state'] = 'failed'
        heartbeat['last_hard_failure'] = {
            'at': utc_now_iso(),
            'status': exc.__class__.__name__,
            'message': str(exc),
        }
        write_heartbeat(heartbeat_path, heartbeat)
        raise
    finally:
        if heartbeat.get('state') not in {'failed'}:
            heartbeat['state'] = 'stopped'
        heartbeat['stopped_at'] = utc_now_iso()
        write_heartbeat(heartbeat_path, heartbeat)


if __name__ == "__main__":
    main()
