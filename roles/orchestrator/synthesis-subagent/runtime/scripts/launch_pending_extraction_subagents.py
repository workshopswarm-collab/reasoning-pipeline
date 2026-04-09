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

from common import WORKSPACE_ROOT, relative_to_workspace  # noqa: E402
from status import append_stage_event, locked_status, process_running, set_overall_status, update_request  # noqa: E402

EXECUTOR = SUBAGENT_DIR / "runtime" / "scripts" / "run_reasoning_extract_executor.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch pending extraction executors from synthesis-stage-status.json")
    parser.add_argument("--status-file", required=True)
    parser.add_argument("--timeout-seconds", type=float, default=300.0)
    parser.add_argument("--limit", type=int, default=0, help="Optional max number of pending extractions to launch")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    status_path = Path(args.status_file)
    if not status_path.is_absolute():
        status_path = WORKSPACE_ROOT / status_path

    launched: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []

    with locked_status(status_path) as status:
        requests = status.get("extraction_subagent_requests") or []
        launch_count = 0
        for req in requests:
            persona = req.get("persona") or ""
            label = req.get("label") or ""
            session_key = req.get("target_session_key") or ""
            artifact_path = req.get("artifact_path") or ""
            request_status = req.get("status") or ""
            launched_pid = req.get("launched_pid")

            if request_status == "launched" and launched_pid and process_running(launched_pid):
                skipped.append({"persona": persona, "label": label, "reason": f"already running pid={launched_pid}"})
                continue
            if request_status != "ready":
                skipped.append({"persona": persona, "label": label, "reason": f"status={request_status}"})
                continue
            if not session_key:
                skipped.append({"persona": persona, "label": label, "reason": "missing target_session_key"})
                continue
            if args.limit and launch_count >= args.limit:
                skipped.append({"persona": persona, "label": label, "reason": "limit reached"})
                continue

            cmd = [
                sys.executable,
                str(EXECUTOR),
                "--dispatch-id",
                status["dispatch_id"],
                "--persona",
                persona,
                "--artifact-path",
                artifact_path,
                "--status-file",
                str(status_path),
                "--session-key",
                session_key,
                "--timeout-seconds",
                str(args.timeout_seconds),
                "--pretty",
            ]
            chat_id = req.get("delivery_target_chat_id") or ""
            topic_id = req.get("delivery_target_topic_id") or ""
            start_marker = req.get("visible_start_marker") or ""
            finish_marker = req.get("visible_finish_marker") or ""
            if chat_id and topic_id and start_marker:
                cmd.extend(["--visible-chat-id", str(chat_id), "--visible-topic-id", str(topic_id), "--visible-start-marker", start_marker])
            if chat_id and topic_id and finish_marker:
                if "--visible-chat-id" not in cmd:
                    cmd.extend(["--visible-chat-id", str(chat_id), "--visible-topic-id", str(topic_id)])
                cmd.extend(["--visible-finish-marker", finish_marker])

            log_path = status_path.with_name(f"extraction-launch-{persona}.log")
            log_handle = log_path.open("w")
            proc = subprocess.Popen(cmd, cwd=str(WORKSPACE_ROOT), stdout=log_handle, stderr=subprocess.STDOUT, text=True)
            log_handle.close()

            update_request(status, persona, {
                "status": "launched",
                "launch_log_path": relative_to_workspace(log_path),
                "launched_pid": proc.pid,
            })
            launched.append({
                "persona": persona,
                "label": label,
                "session_key": session_key,
                "artifact_path": artifact_path,
                "delivery_target_chat_id": chat_id,
                "delivery_target_topic_id": topic_id,
                "launch_log_path": relative_to_workspace(log_path),
                "pid": proc.pid,
            })
            launch_count += 1

        if launched:
            set_overall_status(
                status,
                "reasoning_extracts_launched",
                stage="extraction_launch",
                message="Launched pending reasoning-extract executors",
                extra={"launched_personas": [entry["persona"] for entry in launched]},
            )
        elif skipped and not launched:
            append_stage_event(
                status,
                stage="extraction_launch",
                state=status.get("status", "ready_for_reasoning_extracts"),
                message="No extraction executors launched",
                extra={"skipped": skipped},
            )

    summary = {
        "ok": True,
        "status_file": relative_to_workspace(status_path),
        "launched": launched,
        "skipped": skipped,
        "status": None,
    }
    with locked_status(status_path) as status:
        summary["status"] = status.get("status")
    print(json.dumps(summary, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
