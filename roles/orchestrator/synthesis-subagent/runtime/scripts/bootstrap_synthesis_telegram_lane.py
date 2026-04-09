#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import relative_to_workspace, telegram_topic_session_key  # noqa: E402
from status import append_stage_event, locked_status, set_overall_status  # noqa: E402

TELEGRAM_TOPIC_CREATE = (
    Path("/Users/agent2/.openclaw/orchestrator")
    / "roles"
    / "orchestrator"
    / "researchers-swarm-subagents"
    / "runtime"
    / "scripts"
    / "internal"
    / "telegram_topic_create.py"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create or reuse a dedicated Telegram synthesis lane for a synthesis stage status file")
    parser.add_argument("--status-file", required=True)
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def parse_created_topic(result: dict[str, Any]) -> tuple[str, str]:
    payload = result.get("payload") or result
    topic_id = (
        payload.get("topicId")
        or payload.get("threadId")
        or payload.get("messageThreadId")
        or (payload.get("thread") or {}).get("id")
        or (payload.get("thread") or {}).get("threadId")
    )
    title = payload.get("name") or payload.get("threadName") or payload.get("title") or ""
    if topic_id is None:
        raise ValueError(f"could not determine created topic id from result: {result}")
    return str(topic_id), str(title)


def run_json(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"command failed: {' '.join(cmd)}")
    out = proc.stdout.strip()
    return json.loads(out.splitlines()[-1]) if out else {}


def main() -> None:
    args = parse_args()
    status_path = Path(args.status_file).expanduser().resolve()

    with locked_status(status_path) as status:
        existing_topic_id = status.get("synthesis_lane_topic_id") or ""
        existing_session_key = status.get("synthesis_lane_session_key") or ""
        if existing_topic_id and existing_session_key:
            append_stage_event(
                status,
                stage="synthesis_lane_bootstrap",
                state="reused",
                message="Reused existing synthesis Telegram lane",
                extra={"topic_id": existing_topic_id, "session_key": existing_session_key},
            )
            print(json.dumps({
                "ok": True,
                "action": "reused",
                "status_file": relative_to_workspace(status_path),
                "topic_id": existing_topic_id,
                "session_key": existing_session_key,
                "topic_title": status.get("synthesis_lane_topic_title", ""),
            }, indent=2 if args.pretty else None))
            return

        chat_id = str(status.get("synthesis_target_chat_id") or "").strip()
        if not chat_id:
            set_overall_status(status, status.get("status", "ready_for_final_synthesis"), stage="synthesis_lane_bootstrap", message="Missing synthesis_target_chat_id; cannot create dedicated synthesis lane")
            raise SystemExit("missing synthesis_target_chat_id")

        case_key = str(status.get("case_key") or "case").strip()
        dispatch_id = str(status.get("dispatch_id") or "dispatch").strip()
        title = f"{case_key} | synthesis | {dispatch_id[-8:]}"

    created = run_json([sys.executable, str(TELEGRAM_TOPIC_CREATE), "--chat-id", chat_id, "--title", title])
    topic_id, created_title = parse_created_topic(created)
    topic_title = created_title or title
    session_key = telegram_topic_session_key(chat_id, topic_id)

    with locked_status(status_path) as status:
        if status.get("synthesis_lane_topic_id") and status.get("synthesis_lane_session_key"):
            append_stage_event(
                status,
                stage="synthesis_lane_bootstrap",
                state="reused",
                message="Another process already created the synthesis Telegram lane",
                extra={
                    "topic_id": status.get("synthesis_lane_topic_id"),
                    "session_key": status.get("synthesis_lane_session_key"),
                },
            )
            print(json.dumps({
                "ok": True,
                "action": "reused-after-race",
                "status_file": relative_to_workspace(status_path),
                "topic_id": status.get("synthesis_lane_topic_id"),
                "session_key": status.get("synthesis_lane_session_key"),
                "topic_title": status.get("synthesis_lane_topic_title", ""),
            }, indent=2 if args.pretty else None))
            return

        status.update({
            "synthesis_lane_topic_id": topic_id,
            "synthesis_lane_topic_title": topic_title,
            "synthesis_lane_session_key": session_key,
            "synthesis_target_topic_id": topic_id,
            "synthesis_target_topic_title": topic_title,
            "synthesis_target_session_key": session_key,
        })
        append_stage_event(
            status,
            stage="synthesis_lane_bootstrap",
            state="created",
            message="Created dedicated Telegram synthesis lane",
            extra={"topic_id": topic_id, "topic_title": topic_title, "session_key": session_key},
        )

    print(json.dumps({
        "ok": True,
        "action": "created",
        "status_file": relative_to_workspace(status_path),
        "chat_id": chat_id,
        "topic_id": topic_id,
        "topic_title": topic_title,
        "session_key": session_key,
    }, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
