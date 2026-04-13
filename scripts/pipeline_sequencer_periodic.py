from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from pipeline_automation_actions import REPO_ROOT, run_python_script, run_resolution_sync

SCORE_BRIER = REPO_ROOT / 'quant-db' / 'scripts' / 'score_brier.py'
DEFAULT_BRIER_OUTPUT_DIR = REPO_ROOT / 'quant-db' / 'reports' / 'brier'


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


def run_brier_snapshot(*, pretty: bool, output_dir: Path) -> dict[str, Any]:
    result = run_python_script(SCORE_BRIER, pretty=pretty)
    if result.get('ok') and result.get('payload'):
        result['persisted_paths'] = persist_brier_snapshot(result['payload'], output_dir=output_dir)
    return result


def maybe_run_periodic_tasks(*, args: Any, now_ts: float, last_resolution_sync_ts: float | None, last_brier_snapshot_ts: float | None) -> tuple[dict[str, Any], float | None, float | None]:
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
