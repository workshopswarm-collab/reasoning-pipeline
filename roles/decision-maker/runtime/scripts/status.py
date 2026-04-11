#!/usr/bin/env python3
from __future__ import annotations

from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime, timezone
import fcntl
from pathlib import Path
from typing import Any, Iterator

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]

from common import load_json, write_json  # noqa: E402


TERMINAL_STATUSES = {
    "decision_completed",
    "decision_failed",
}


def utc_now_z() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


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


def decision_lane_summary(status: dict[str, Any]) -> dict[str, Any]:
    topic_id = status.get("decision_lane_topic_id") or status.get("decision_target_topic_id") or ""
    topic_title = status.get("decision_lane_topic_title") or status.get("decision_target_topic_title") or ""
    session_key = status.get("decision_lane_session_key") or status.get("decision_target_session_key") or ""
    if not any([topic_id, topic_title, session_key]):
        return {}
    return {
        "topic_id": topic_id,
        "topic_title": topic_title,
        "session_key": session_key,
    }


def append_stage_event(status: dict[str, Any], *, stage: str, state: str, message: str = "", extra: dict[str, Any] | None = None) -> None:
    event = {
        "at": utc_now_z(),
        "stage": stage,
        "state": state,
        "message": message,
    }
    if extra:
        event.update(extra)
    status.setdefault("stage_events", []).append(event)
    status["last_stage_event"] = deepcopy(event)


def set_overall_status(status: dict[str, Any], value: str, *, stage: str, message: str = "", extra: dict[str, Any] | None = None) -> None:
    status["status"] = value
    append_stage_event(status, stage=stage, state=value, message=message, extra=extra)


def update_terminal_summary(status: dict[str, Any]) -> None:
    current_status = str(status.get("status") or "")
    if current_status not in TERMINAL_STATUSES:
        status.pop("terminal_summary", None)
        return
    status["terminal_summary"] = {
        "at": utc_now_z(),
        "status": current_status,
        "decision_lane": decision_lane_summary(status),
        "packet_json_path": status.get("packet_json_path", ""),
        "packet_markdown_path": status.get("packet_markdown_path", ""),
        "trade_authorization": status.get("trade_authorization", ""),
        "decision_readiness": status.get("decision_readiness", ""),
        "last_stage_event": deepcopy(status.get("last_stage_event") or {}),
    }


def write_status_file(path: Path, status: dict[str, Any]) -> None:
    status["updated_at"] = utc_now_z()
    status["decision_lane"] = decision_lane_summary(status)
    update_terminal_summary(status)
    write_json(path, status, pretty=True)
