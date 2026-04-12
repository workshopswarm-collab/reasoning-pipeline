#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
from pathlib import Path
from typing import Any, Iterator

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / 'scripts') not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / 'scripts'))

from automation_runtime_support import DEFAULT_SUBPROCESS_TIMEOUT_SECONDS, parse_json_output, run_subprocess, tail_text  # noqa: E402

CASES_ROOT = REPO_ROOT / "qualitative-db" / "40-research" / "cases"
POST_CASE_TERMINAL_TOPIC_MARKER = REPO_ROOT / "scripts" / "post_case_terminal_topic_marker.py"
MATERIALIZE_CASE_SWARM_ARTIFACTS = REPO_ROOT / "scripts" / "materialize_case_swarm_artifacts.py"
CANONICAL_CASE_KEY_RE = re.compile(r'(case-\d{8}-[a-f0-9]{8})')
HELPER_TIMEOUT_SECONDS = DEFAULT_SUBPROCESS_TIMEOUT_SECONDS


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def case_root(case_key: str) -> Path:
    return CASES_ROOT / case_key


def canonicalize_case_key(case_key: str, *, dispatch_id: str = "") -> str:
    text = str(case_key or "").strip()
    if text.startswith('case-'):
        return text
    match = CANONICAL_CASE_KEY_RE.search(str(dispatch_id or ''))
    if match:
        return match.group(1)
    return text


def pipeline_status_path(case_key: str) -> Path:
    return case_root(case_key) / "pipeline-status.json"


def load_json_if_exists(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


@contextmanager
def locked_json_file(path: Path) -> Iterator[dict[str, Any]]:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_RDWR | os.O_CREAT, 0o644)
    with os.fdopen(fd, "r+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            raw = handle.read()
            try:
                payload = json.loads(raw) if raw.strip() else {}
            except Exception:
                payload = {}
            if not isinstance(payload, dict):
                payload = {}
            yield payload
            handle.seek(0)
            handle.truncate()
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def _default_stage_statuses() -> dict[str, str]:
    return {
        "dispatch": "pending",
        "swarm": "pending",
        "synthesis": "pending",
        "decision": "pending",
    }


def record_helper_status(case_key: str, helper_name: str, result: dict[str, Any]) -> None:
    path = pipeline_status_path(case_key)
    if not path.exists():
        return
    with locked_json_file(path) as payload:
        helper_status = payload.setdefault('helper_status', {})
        helper_status[helper_name] = result


def maybe_materialize_case_swarm_artifacts(snapshot: dict[str, Any]) -> dict[str, Any]:
    case_key = str(snapshot.get('case_key') or '').strip()
    if not MATERIALIZE_CASE_SWARM_ARTIFACTS.exists():
        return {
            'helper': 'materialize_case_swarm_artifacts',
            'attempted_at': utc_now_iso(),
            'ok': False,
            'reason': 'script_missing',
        }
    cmd = [sys.executable, str(MATERIALIZE_CASE_SWARM_ARTIFACTS), '--case-key', case_key]
    try:
        proc = run_subprocess(
            cmd,
            cwd=REPO_ROOT,
            timeout_seconds=HELPER_TIMEOUT_SECONDS,
        )
        payload = parse_json_output(proc.stdout or '')
        result = {
            'helper': 'materialize_case_swarm_artifacts',
            'attempted_at': utc_now_iso(),
            'ok': proc.returncode == 0,
            'returncode': proc.returncode,
        }
        if payload:
            result['payload'] = payload
        if proc.returncode != 0:
            result['stdout_tail'] = tail_text(proc.stdout)
            result['stderr_tail'] = tail_text(proc.stderr)
        return result
    except Exception as exc:  # noqa: BLE001
        return {
            'helper': 'materialize_case_swarm_artifacts',
            'attempted_at': utc_now_iso(),
            'ok': False,
            'error': str(exc),
        }


def maybe_post_terminal_topic_marker(snapshot: dict[str, Any]) -> dict[str, Any]:
    status = str(snapshot.get('status') or '')
    terminal_summary = snapshot.get('terminal_summary') if isinstance(snapshot.get('terminal_summary'), dict) else {}
    if status not in {'pipeline_completed', 'pipeline_failed', 'pipeline_skipped'}:
        return {
            'helper': 'post_case_terminal_topic_marker',
            'attempted_at': utc_now_iso(),
            'ok': True,
            'noop': True,
            'reason': f'status_not_terminal:{status}',
        }
    if terminal_summary.get('topic_terminal_marker_posted_at'):
        return {
            'helper': 'post_case_terminal_topic_marker',
            'attempted_at': utc_now_iso(),
            'ok': True,
            'noop': True,
            'reason': 'already_posted',
        }
    if not POST_CASE_TERMINAL_TOPIC_MARKER.exists():
        return {
            'helper': 'post_case_terminal_topic_marker',
            'attempted_at': utc_now_iso(),
            'ok': False,
            'reason': 'script_missing',
        }
    cmd = [sys.executable, str(POST_CASE_TERMINAL_TOPIC_MARKER), '--case-key', str(snapshot.get('case_key') or '')]
    try:
        proc = run_subprocess(
            cmd,
            cwd=REPO_ROOT,
            timeout_seconds=HELPER_TIMEOUT_SECONDS,
        )
        payload = parse_json_output(proc.stdout or '')
        result = {
            'helper': 'post_case_terminal_topic_marker',
            'attempted_at': utc_now_iso(),
            'ok': proc.returncode == 0,
            'returncode': proc.returncode,
        }
        if payload:
            result['payload'] = payload
        if proc.returncode != 0:
            result['stdout_tail'] = tail_text(proc.stdout)
            result['stderr_tail'] = tail_text(proc.stderr)
        return result
    except Exception as exc:  # noqa: BLE001
        return {
            'helper': 'post_case_terminal_topic_marker',
            'attempted_at': utc_now_iso(),
            'ok': False,
            'error': str(exc),
        }


def _normalize_terminal_payload(payload: dict[str, Any]) -> None:
    status = str(payload.get("status") or "").strip()
    stage_statuses = payload.setdefault("stage_statuses", _default_stage_statuses())
    terminal_summary = payload.setdefault("terminal_summary", {})
    if status == "pipeline_completed":
        for stage_name in ("dispatch", "swarm", "synthesis", "decision"):
            stage_statuses[stage_name] = "completed"
        for stale_key in ("failure_reason", "failed_stage", "quarantined"):
            terminal_summary.pop(stale_key, None)
    elif status == "pipeline_skipped":
        for stale_key in ("failure_reason", "failed_stage", "quarantined"):
            terminal_summary.pop(stale_key, None)


def update_case_pipeline_status(
    *,
    case_key: str,
    dispatch_id: str = "",
    market_id: str = "",
    market_title: str = "",
    status: str | None = None,
    current_stage: str | None = None,
    stage_status_patch: dict[str, str] | None = None,
    runner_id: str = "",
    batch_run_id: str = "",
    message: str = "",
    extra: dict[str, Any] | None = None,
    terminal_summary_patch: dict[str, Any] | None = None,
) -> dict[str, Any]:
    normalized_case_key = canonicalize_case_key(case_key, dispatch_id=dispatch_id)
    path = pipeline_status_path(normalized_case_key)
    now = utc_now_iso()
    with locked_json_file(path) as payload:
        payload.setdefault("artifact_type", "case_pipeline_status")
        payload.setdefault("schema_version", "case-pipeline-status/v1")
        payload["case_key"] = normalized_case_key
        payload.setdefault("stage_statuses", _default_stage_statuses())
        payload.setdefault("timeline", [])
        payload.setdefault("terminal_summary", {})
        payload.setdefault("started_at", now)
        payload["updated_at"] = now
        if dispatch_id:
            payload["dispatch_id"] = dispatch_id
        if market_id:
            payload["market_id"] = market_id
        if market_title:
            payload["market_title"] = market_title
        if runner_id:
            payload["runner_id"] = runner_id
        if batch_run_id:
            payload["batch_run_id"] = batch_run_id
        if status:
            payload["status"] = status
            if status in {"pipeline_completed", "pipeline_failed", "pipeline_skipped"}:
                payload["completed_at"] = now
        else:
            payload.setdefault("status", "pipeline_started")
        if current_stage:
            payload["current_stage"] = current_stage
        else:
            payload.setdefault("current_stage", "dispatch")
        if stage_status_patch:
            stage_statuses = payload.setdefault("stage_statuses", _default_stage_statuses())
            for key, value in stage_status_patch.items():
                if value:
                    stage_statuses[key] = value
        if terminal_summary_patch:
            terminal_summary = payload.setdefault("terminal_summary", {})
            for key, value in terminal_summary_patch.items():
                if value is None:
                    terminal_summary.pop(key, None)
                else:
                    terminal_summary[key] = value
        _normalize_terminal_payload(payload)
        if message or extra:
            entry = {
                "at": now,
                "status": payload.get("status", ""),
                "current_stage": payload.get("current_stage", ""),
            }
            if message:
                entry["message"] = message
            if extra:
                entry.update(extra)
            timeline = payload.setdefault("timeline", [])
            timeline.append(entry)
            payload["last_event"] = entry
        snapshot = dict(payload)
    materialize_result = maybe_materialize_case_swarm_artifacts(snapshot)
    terminal_marker_result = maybe_post_terminal_topic_marker(snapshot)
    record_helper_status(normalized_case_key, 'materialize_case_swarm_artifacts', materialize_result)
    record_helper_status(normalized_case_key, 'post_case_terminal_topic_marker', terminal_marker_result)
    snapshot['helper_status'] = {
        'materialize_case_swarm_artifacts': materialize_result,
        'post_case_terminal_topic_marker': terminal_marker_result,
    }
    return snapshot


def summarize_case_pipeline_status(case_key: str) -> dict[str, Any]:
    path = pipeline_status_path(case_key)
    payload = load_json_if_exists(path)
    return {
        "exists": path.exists(),
        "path": str(path.relative_to(REPO_ROOT)) if path.exists() else str(path.relative_to(REPO_ROOT)),
        "case_key": case_key,
        "status": payload.get("status", ""),
        "current_stage": payload.get("current_stage", ""),
        "stage_statuses": payload.get("stage_statuses", {}),
        "dispatch_id": payload.get("dispatch_id", ""),
        "market_id": payload.get("market_id", ""),
        "market_title": payload.get("market_title", ""),
        "started_at": payload.get("started_at", ""),
        "updated_at": payload.get("updated_at", ""),
        "completed_at": payload.get("completed_at", ""),
        "terminal_summary": payload.get("terminal_summary", {}),
        "helper_status": payload.get("helper_status", {}),
        "last_event": payload.get("last_event", {}),
    }


def list_case_pipeline_statuses(*, include_terminal: bool = False) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for path in sorted(CASES_ROOT.glob('case-*/pipeline-status.json')):
        case_key = path.parent.name
        summary = summarize_case_pipeline_status(case_key)
        if not include_terminal and summary.get("status") in {"pipeline_completed", "pipeline_failed", "pipeline_skipped"}:
            continue
        summaries.append(summary)
    summaries.sort(key=lambda item: item.get("updated_at", ""), reverse=True)
    return summaries


def first_active_nonterminal_case() -> dict[str, Any]:
    active = list_case_pipeline_statuses(include_terminal=False)
    return active[0] if active else {}


def first_blocking_case_without_completed_decision_packet() -> dict[str, Any]:
    for summary in list_case_pipeline_statuses(include_terminal=True):
        terminal_summary = summary.get("terminal_summary") if isinstance(summary.get("terminal_summary"), dict) else {}
        status = str(summary.get("status") or "").strip()
        if status != "pipeline_completed":
            return summary
        if not str(terminal_summary.get("decision_packet_markdown") or "").strip():
            return summary
    return {}
