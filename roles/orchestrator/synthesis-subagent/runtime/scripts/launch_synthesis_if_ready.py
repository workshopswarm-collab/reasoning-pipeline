#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any
from uuid import uuid4

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import WORKSPACE_ROOT, relative_to_workspace  # noqa: E402
from status import load_status_file, locked_status, process_running, refresh_request_runtime_state, set_overall_status, write_status_file  # noqa: E402

BUILD_SIDECAR_BUNDLE = SUBAGENT_DIR / "planner" / "scripts" / "build_sidecar_synthesis_bundle.py"
BUILD_SYNTHESIS_PROMPT = SUBAGENT_DIR / "planner" / "scripts" / "build_synthesis_prompt.py"
BOOTSTRAP_SYNTHESIS_LANE = SUBAGENT_DIR / "runtime" / "scripts" / "bootstrap_synthesis_telegram_lane.py"
RUN_SYNTHESIS = SUBAGENT_DIR / "runtime" / "scripts" / "run_synthesis_executor.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch final synthesis once all researcher sidecars are ready")
    parser.add_argument("--status-file", required=True)
    parser.add_argument("--timeout-seconds", type=float, default=360.0)
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def run_json(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(cmd, cwd=str(WORKSPACE_ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"command failed: {' '.join(cmd)}")
    stdout = proc.stdout.strip()
    return json.loads(stdout) if stdout else {}


def clear_launch_claim(status: dict[str, Any]) -> None:
    status.pop("final_synthesis_launch_claim_token", None)
    status.pop("final_synthesis_launch_claim_pid", None)
    status.pop("final_synthesis_launch_claimed_at", None)


def claim_final_synthesis_launch(status_path: Path, *, pretty: bool) -> dict[str, Any]:
    claim_pid = os.getpid()
    claim_token = str(uuid4())
    with locked_status(status_path) as status:
        refresh_request_runtime_state(status)

        if status.get("status") == "synthesis_completed":
            return {
                "ok": True,
                "status": status.get("status"),
                "reason": "already_completed",
                "status_file": relative_to_workspace(status_path),
            }

        if status.get("status") == "final_synthesis_launched" and process_running(status.get("final_synthesis_pid")):
            return {
                "ok": True,
                "status": status.get("status"),
                "reason": "already_running",
                "pid": status.get("final_synthesis_pid"),
                "status_file": relative_to_workspace(status_path),
            }

        if status.get("status") == "final_synthesis_launching":
            existing_claim_pid = status.get("final_synthesis_launch_claim_pid")
            if process_running(existing_claim_pid):
                return {
                    "ok": True,
                    "status": status.get("status"),
                    "reason": "already_launching",
                    "claim_pid": existing_claim_pid,
                    "status_file": relative_to_workspace(status_path),
                }
            clear_launch_claim(status)

        status["final_synthesis_launch_claim_token"] = claim_token
        status["final_synthesis_launch_claim_pid"] = claim_pid
        status["final_synthesis_launch_claimed_at"] = status.get("updated_at") or "pending_write"
        set_overall_status(
            status,
            "final_synthesis_launching",
            stage="synthesis_promotion",
            message="Claimed final synthesis launch",
            extra={"launch_claim_pid": claim_pid},
        )
        return {
            "ok": True,
            "status": status.get("status"),
            "reason": "claimed",
            "claim_pid": claim_pid,
            "claim_token": claim_token,
            "status_file": relative_to_workspace(status_path),
        }


def main() -> None:
    args = parse_args()
    status_path = Path(args.status_file)
    if not status_path.is_absolute():
        status_path = WORKSPACE_ROOT / status_path
    status = load_status_file(status_path)

    if status.get("status") == "synthesis_completed":
        print(json.dumps({
            "ok": True,
            "status": status.get("status"),
            "reason": "already_completed",
            "status_file": relative_to_workspace(status_path),
        }, indent=2 if args.pretty else None))
        return
    if status.get("status") == "final_synthesis_launched" and process_running(status.get("final_synthesis_pid")):
        print(json.dumps({
            "ok": True,
            "status": status.get("status"),
            "reason": "already_running",
            "pid": status.get("final_synthesis_pid"),
            "status_file": relative_to_workspace(status_path),
        }, indent=2 if args.pretty else None))
        return

    sidecar_requests = status.get("reasoning_sidecar_requests") or []
    missing_sidecars = [req.get("persona") for req in sidecar_requests if req.get("artifact_path") and not (WORKSPACE_ROOT / req["artifact_path"]).exists()]
    incomplete_sidecars = [req.get("persona") for req in sidecar_requests if req.get("status") not in {"completed", "already_present"}]
    if missing_sidecars or incomplete_sidecars:
        waiting = sorted(set((missing_sidecars or []) + (incomplete_sidecars or [])))
        set_overall_status(status, "waiting_for_reasoning_sidecars", stage="synthesis_promotion", message="Waiting for all researcher sidecars before final synthesis", extra={"waiting_for_personas": waiting})
        write_status_file(status_path, status)
        print(json.dumps({
            "ok": True,
            "status": status.get("status"),
            "waiting_for_personas": waiting,
            "status_file": relative_to_workspace(status_path),
        }, indent=2 if args.pretty else None))
        return

    structured_bundle_path = status.get("structured_bundle_path") or ""
    if not structured_bundle_path:
        try:
            sidecar_summary = run_json([
                sys.executable,
                str(BUILD_SIDECAR_BUNDLE),
                "--bundle-json",
                str(WORKSPACE_ROOT / status["bundle_path"]),
                *( ["--pretty"] if args.pretty else [] ),
            ])
        except Exception as exc:  # noqa: BLE001
            set_overall_status(status, "sidecar_bundle_failed", stage="synthesis_promotion", message="Failed to build sidecar-synthesis bundle", extra={"error": str(exc)})
            write_status_file(status_path, status)
            raise
        structured_bundle_path = sidecar_summary["sidecar_bundle_path"]
        status.update({
            "structured_bundle_path": structured_bundle_path,
            "structured_bundle_artifact_type": "sidecar_synthesis_bundle",
        })

    try:
        prompt_summary = run_json([
            sys.executable,
            str(BUILD_SYNTHESIS_PROMPT),
            "--bundle-json",
            str(WORKSPACE_ROOT / structured_bundle_path),
            *( ["--pretty"] if args.pretty else [] ),
        ])
    except Exception as exc:  # noqa: BLE001
        status.update({
            "structured_bundle_path": structured_bundle_path,
            "structured_bundle_artifact_type": "sidecar_synthesis_bundle",
        })
        set_overall_status(status, "synthesis_prompt_failed", stage="synthesis_promotion", message="Failed to build synthesis prompt", extra={"error": str(exc)})
        write_status_file(status_path, status)
        raise
    synthesis_prompt_path = prompt_summary["prompt_path"]

    claim = claim_final_synthesis_launch(status_path, pretty=args.pretty)
    if claim.get("reason") != "claimed":
        print(json.dumps(claim, indent=2 if args.pretty else None))
        return
    claim_token = claim["claim_token"]

    try:
        with locked_status(status_path) as claimed_status:
            if claimed_status.get("final_synthesis_launch_claim_token") != claim_token:
                print(json.dumps({
                    "ok": True,
                    "status": claimed_status.get("status"),
                    "reason": "claim_lost_before_bootstrap",
                    "status_file": relative_to_workspace(status_path),
                }, indent=2 if args.pretty else None))
                return
            claimed_status.update({
                "structured_bundle_path": structured_bundle_path,
                "structured_bundle_artifact_type": "sidecar_synthesis_bundle",
                "synthesis_prompt_path": synthesis_prompt_path,
            })

        lane_summary = run_json([
            sys.executable,
            str(BOOTSTRAP_SYNTHESIS_LANE),
            "--status-file",
            str(status_path),
            *( ["--pretty"] if args.pretty else [] ),
        ])
        status = load_status_file(status_path)
    except Exception as exc:  # noqa: BLE001
        with locked_status(status_path) as claimed_status:
            if claimed_status.get("final_synthesis_launch_claim_token") == claim_token:
                clear_launch_claim(claimed_status)
                claimed_status.update({
                    "structured_bundle_path": structured_bundle_path,
                    "structured_bundle_artifact_type": "sidecar_synthesis_bundle",
                    "synthesis_prompt_path": synthesis_prompt_path,
                })
                set_overall_status(claimed_status, "synthesis_lane_bootstrap_failed", stage="synthesis_promotion", message="Failed to create or reuse dedicated Telegram synthesis lane", extra={"error": str(exc)})
        raise

    session_key = status.get("synthesis_target_session_key") or ""
    if not session_key:
        with locked_status(status_path) as claimed_status:
            if claimed_status.get("final_synthesis_launch_claim_token") == claim_token:
                clear_launch_claim(claimed_status)
                claimed_status.update({
                    "structured_bundle_path": structured_bundle_path,
                    "structured_bundle_artifact_type": "sidecar_synthesis_bundle",
                    "synthesis_prompt_path": synthesis_prompt_path,
                })
                set_overall_status(claimed_status, "ready_for_final_synthesis", stage="synthesis_promotion", message="Final synthesis is ready but no synthesis target session is configured")
                status = dict(claimed_status)
        print(json.dumps({
            "ok": True,
            "status": status.get("status"),
            "reason": "missing_synthesis_target_session_key",
            "structured_bundle_path": structured_bundle_path,
            "synthesis_prompt_path": synthesis_prompt_path,
            "status_file": relative_to_workspace(status_path),
        }, indent=2 if args.pretty else None))
        return

    cmd = [
        sys.executable,
        str(RUN_SYNTHESIS),
        "--dispatch-id",
        status["dispatch_id"],
        "--bundle-json",
        str(WORKSPACE_ROOT / structured_bundle_path),
        "--status-file",
        str(status_path),
        "--session-key",
        session_key,
        "--timeout-seconds",
        str(args.timeout_seconds),
        "--write-current",
        "--pretty",
    ]
    chat_id = status.get("synthesis_target_chat_id") or ""
    topic_id = status.get("synthesis_target_topic_id") or ""
    if chat_id and topic_id:
        cmd.extend(["--visible-chat-id", str(chat_id), "--visible-topic-id", str(topic_id)])
        if status.get("synthesis_visible_start_marker"):
            cmd.extend(["--visible-start-marker", status["synthesis_visible_start_marker"]])
        if status.get("synthesis_visible_finish_marker"):
            cmd.extend(["--visible-finish-marker", status["synthesis_visible_finish_marker"]])

    log_path = status_path.with_name("final-synthesis-launch.log")
    log_handle = log_path.open("w")
    proc = subprocess.Popen(cmd, cwd=str(WORKSPACE_ROOT), stdout=log_handle, stderr=subprocess.STDOUT, text=True)
    log_handle.close()

    with locked_status(status_path) as status:
        if status.get("final_synthesis_launch_claim_token") != claim_token:
            proc.terminate()
            print(json.dumps({
                "ok": True,
                "status": status.get("status"),
                "reason": "claim_lost_after_spawn",
                "status_file": relative_to_workspace(status_path),
            }, indent=2 if args.pretty else None))
            return
        if status.get("status") == "final_synthesis_launched" and process_running(status.get("final_synthesis_pid")):
            proc.terminate()
            print(json.dumps({
                "ok": True,
                "status": status.get("status"),
                "reason": "already_running_after_race",
                "pid": status.get("final_synthesis_pid"),
                "status_file": relative_to_workspace(status_path),
            }, indent=2 if args.pretty else None))
            return
        clear_launch_claim(status)
        status.update({
            "structured_bundle_path": structured_bundle_path,
            "structured_bundle_artifact_type": "sidecar_synthesis_bundle",
            "synthesis_prompt_path": synthesis_prompt_path,
            "final_synthesis_launch_log_path": relative_to_workspace(log_path),
            "final_synthesis_pid": proc.pid,
        })
        set_overall_status(status, "final_synthesis_launched", stage="synthesis_promotion", message="Launched final synthesis executor", extra={"pid": proc.pid, "launch_log_path": relative_to_workspace(log_path)})

    print(json.dumps({
        "ok": True,
        "status": status.get("status"),
        "dispatch_id": status.get("dispatch_id"),
        "session_key": session_key,
        "structured_bundle_path": structured_bundle_path,
        "synthesis_prompt_path": synthesis_prompt_path,
        "launch_log_path": relative_to_workspace(log_path),
        "pid": proc.pid,
        "lane_summary": lane_summary,
        "status_file": relative_to_workspace(status_path),
    }, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
