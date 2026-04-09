#!/usr/bin/env python3
from __future__ import annotations

from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime, timezone
import fcntl
import subprocess
from pathlib import Path
from typing import Any, Iterator

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]

from common import load_json, write_json  # noqa: E402


def utc_now_z() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def process_running(pid: Any) -> bool:
    try:
        pid_int = int(pid)
    except (TypeError, ValueError):
        return False
    proc = subprocess.run(["ps", "-p", str(pid_int), "-o", "pid="], capture_output=True, text=True)
    return bool(proc.stdout.strip())


@contextmanager
def locked_status(path: Path) -> Iterator[dict[str, Any]]:
    lock_path = Path(f"{path}.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("w") as lock_handle:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
        if path.exists():
            status = load_json(path)
        else:
            status = {}
        yield status
        write_status_file(path, status)
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)


TERMINAL_STATUSES = {
    "reasoning_extracts_failed",
    "extracts_bundle_failed",
    "synthesis_prompt_failed",
    "synthesis_lane_bootstrap_failed",
    "final_synthesis_failed",
    "synthesis_completed",
}


def request_status_counts(status: dict[str, Any]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for req in status.get("extraction_subagent_requests") or []:
        key = str(req.get("status") or "unknown")
        counts[key] = counts.get(key, 0) + 1
    return counts


def synthesis_lane_summary(status: dict[str, Any]) -> dict[str, Any]:
    topic_id = status.get("synthesis_lane_topic_id") or status.get("synthesis_target_topic_id") or ""
    topic_title = status.get("synthesis_lane_topic_title") or status.get("synthesis_target_topic_title") or ""
    session_key = status.get("synthesis_lane_session_key") or status.get("synthesis_target_session_key") or ""
    if not any([topic_id, topic_title, session_key]):
        return {}
    return {
        "topic_id": topic_id,
        "topic_title": topic_title,
        "session_key": session_key,
    }


def update_terminal_summary(status: dict[str, Any]) -> None:
    current_status = str(status.get("status") or "")
    if current_status not in TERMINAL_STATUSES:
        status.pop("terminal_summary", None)
        return
    status["terminal_summary"] = {
        "at": utc_now_z(),
        "status": current_status,
        "request_status_counts": request_status_counts(status),
        "final_artifact_path": status.get("final_artifact_path", ""),
        "final_sidecar_path": status.get("final_sidecar_path", ""),
        "final_decision_handoff_path": status.get("final_decision_handoff_path", ""),
        "synthesis_lane": synthesis_lane_summary(status),
        "last_stage_event": deepcopy(status.get("last_stage_event") or {}),
    }


def append_stage_event(status: dict[str, Any], *, stage: str, state: str, message: str = "", extra: dict[str, Any] | None = None) -> None:
    event = {
        "at": utc_now_z(),
        "stage": stage,
        "state": state,
        "message": message,
        "request_status_counts": request_status_counts(status),
    }
    if extra:
        event.update(extra)
    status.setdefault("stage_events", []).append(event)
    status["last_stage_event"] = deepcopy(event)


def set_overall_status(status: dict[str, Any], value: str, *, stage: str, message: str = "", extra: dict[str, Any] | None = None) -> None:
    status["status"] = value
    append_stage_event(status, stage=stage, state=value, message=message, extra=extra)


def find_request(status: dict[str, Any], persona: str) -> dict[str, Any] | None:
    for req in status.get("extraction_subagent_requests") or []:
        if req.get("persona") == persona:
            return req
    return None


def update_request(status: dict[str, Any], persona: str, patch: dict[str, Any]) -> dict[str, Any]:
    req = find_request(status, persona)
    if req is None:
        raise KeyError(f"persona not found in extraction_subagent_requests: {persona}")
    req.update(patch)
    status["request_status_counts"] = request_status_counts(status)
    return req


def load_status_file(path: Path) -> dict[str, Any]:
    status = load_json(path)
    refresh_request_runtime_state(status)
    return status


def write_status_file(path: Path, status: dict[str, Any]) -> None:
    status["updated_at"] = utc_now_z()
    status["request_status_counts"] = request_status_counts(status)
    status["synthesis_lane"] = synthesis_lane_summary(status)
    update_terminal_summary(status)
    write_json(path, status, pretty=True)


def refresh_request_runtime_state(status: dict[str, Any]) -> None:
    for req in status.get("extraction_subagent_requests") or []:
        pid = req.get("launched_pid")
        if req.get("status") == "launched" and pid and not process_running(pid):
            req["status"] = "ready"
            req["artifact_state"] = req.get("artifact_state") or "missing"
            req.setdefault("artifact_validation_warnings", []).append("previous launched extractor process is no longer running; request returned to ready state")

    final_pid = status.get("final_synthesis_pid")
    if status.get("status") == "final_synthesis_launched" and final_pid and not process_running(final_pid):
        if not all(status.get(key) for key in ["final_artifact_path", "final_sidecar_path", "final_decision_handoff_path"]):
            status["status"] = "final_synthesis_failed"
            status["final_synthesis_failure_reason"] = "final synthesis process is no longer running and final artifacts are absent"
