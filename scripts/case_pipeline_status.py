#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
from pathlib import Path
from typing import Any, Iterator

REPO_ROOT = Path(__file__).resolve().parents[1]
CASES_ROOT = REPO_ROOT / "qualitative-db" / "40-research" / "cases"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def case_root(case_key: str) -> Path:
    return CASES_ROOT / case_key


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
    path = pipeline_status_path(case_key)
    now = utc_now_iso()
    with locked_json_file(path) as payload:
        payload.setdefault("artifact_type", "case_pipeline_status")
        payload.setdefault("schema_version", "case-pipeline-status/v1")
        payload.setdefault("case_key", case_key)
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
            payload.setdefault("terminal_summary", {}).update({k: v for k, v in terminal_summary_patch.items() if v is not None})
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
        return dict(payload)


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
