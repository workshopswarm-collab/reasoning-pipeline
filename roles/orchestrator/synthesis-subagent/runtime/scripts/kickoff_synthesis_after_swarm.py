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

from common import WORKSPACE_ROOT, load_json, relative_to_workspace, synthesis_subagent_label, telegram_topic_session_key  # noqa: E402
from status import set_overall_status, write_status_file  # noqa: E402

BUILD_BUNDLE = SUBAGENT_DIR / "planner" / "scripts" / "build_synthesis_bundle.py"
BUILD_SIDECAR_BUNDLE = SUBAGENT_DIR / "planner" / "scripts" / "build_sidecar_synthesis_bundle.py"
BUILD_SYNTHESIS_PROMPT = SUBAGENT_DIR / "planner" / "scripts" / "build_synthesis_prompt.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Kick off the synthesis stage after researcher swarm completion")
    parser.add_argument("--dispatch-id", required=True)
    parser.add_argument("--case-key", help="Optional case key to disambiguate bundle lookup")
    parser.add_argument("--build-full", action="store_true", help="If all researcher sidecars are present, also build the sidecar synthesis bundle and final synthesis prompt")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def run_json(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(cmd, cwd=str(WORKSPACE_ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(
            f"command failed ({proc.returncode}): {' '.join(cmd)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
        )
    stdout = proc.stdout.strip()
    return json.loads(stdout) if stdout else {}


def main() -> None:
    args = parse_args()
    cmd = [sys.executable, str(BUILD_BUNDLE), "--dispatch-id", args.dispatch_id]
    if args.case_key:
        cmd.extend(["--case-key", args.case_key])
    if args.pretty:
        cmd.append("--pretty")
    bundle_summary = run_json(cmd)
    bundle_path = WORKSPACE_ROOT / bundle_summary["bundle_path"]
    bundle_payload = load_json(bundle_path)
    question = str(bundle_payload.get("question") or "").strip()

    sidecar_requests = []
    ready_sidecar_personas = []
    pending_sidecar_personas = []
    for persona_entry in bundle_payload.get("persona_findings", []):
        persona = str(persona_entry.get("persona") or "").strip()
        sidecar_path = str(persona_entry.get("reasoning_sidecar_path") or "").strip()
        sidecar_state = "current" if persona_entry.get("reasoning_sidecar_exists") else "missing"
        request = {
            "persona": persona,
            "artifact_path": sidecar_path,
            "status": "completed" if sidecar_state == "current" else "missing",
            "artifact_state": sidecar_state,
        }
        sidecar_requests.append(request)
        if sidecar_state == "current":
            ready_sidecar_personas.append(persona)
        else:
            pending_sidecar_personas.append(persona)

    controller_chat_id = ""
    controller_topic_id = ""
    controller_topic_title = ""
    manifest = bundle_payload.get("manifest") or {}
    bootstrap_state = manifest.get("bootstrap_state") or {}
    controller_topic = bootstrap_state.get("controller_topic") or {}
    controller_chat_id = str(
        bootstrap_state.get("controller_chat_id")
        or bootstrap_state.get("chat_id")
        or manifest.get("controller_chat_id")
        or manifest.get("chat_id")
        or ""
    )
    controller_topic_id = str(
        bootstrap_state.get("controller_topic_id")
        or controller_topic.get("topic_id")
        or manifest.get("controller_topic_id")
        or ""
    )
    controller_topic_title = str(
        bootstrap_state.get("controller_topic_title")
        or controller_topic.get("topic_title")
        or manifest.get("controller_topic_title")
        or ""
    )

    structured_bundle_path = ""
    structured_bundle_artifact_type = ""
    synthesis_prompt_path = ""
    if args.build_full and not pending_sidecar_personas:
        sidecar_summary = run_json([
            sys.executable,
            str(BUILD_SIDECAR_BUNDLE),
            "--bundle-json",
            str(bundle_path),
            *( ["--pretty"] if args.pretty else [] ),
        ])
        structured_bundle_path = sidecar_summary["sidecar_bundle_path"]
        structured_bundle_artifact_type = "sidecar_synthesis_bundle"
        synthesis_summary = run_json([
            sys.executable,
            str(BUILD_SYNTHESIS_PROMPT),
            "--bundle-json",
            str(WORKSPACE_ROOT / structured_bundle_path),
            *( ["--pretty"] if args.pretty else [] ),
        ])
        synthesis_prompt_path = synthesis_summary["prompt_path"]

    status_path = bundle_path.with_name("synthesis-stage-status.json")
    status_payload = {
        "artifact_type": "synthesis_stage_status",
        "dispatch_id": args.dispatch_id,
        "case_key": bundle_summary.get("case_key", ""),
        "bundle_path": relative_to_workspace(bundle_path),
        "reasoning_sidecar_requests": sidecar_requests,
        "ready_sidecar_personas": ready_sidecar_personas,
        "pending_sidecar_personas": pending_sidecar_personas,
        "structured_bundle_path": structured_bundle_path,
        "structured_bundle_artifact_type": structured_bundle_artifact_type,
        "synthesis_prompt_path": synthesis_prompt_path,
        "synthesis_subagent_label": synthesis_subagent_label(args.dispatch_id),
        "synthesis_target_chat_id": controller_chat_id,
        "synthesis_target_topic_id": controller_topic_id,
        "synthesis_target_topic_title": controller_topic_title,
        "synthesis_target_session_key": telegram_topic_session_key(controller_chat_id, controller_topic_id),
        "synthesis_visible_start_marker": f"STARTING SYNTHESIS | market={question} | dispatch_id={args.dispatch_id}",
        "synthesis_visible_finish_marker": f"FINISHED SYNTHESIS | market={question} | dispatch_id={args.dispatch_id}",
    }
    set_overall_status(
        status_payload,
        "ready_for_final_synthesis" if synthesis_prompt_path else "waiting_for_reasoning_sidecars",
        stage="kickoff",
        message="Synthesis kickoff prepared current-stage artifacts",
        extra={
            "ready_sidecar_personas": ready_sidecar_personas,
            "pending_sidecar_personas": pending_sidecar_personas,
            "structured_bundle_artifact_type": structured_bundle_artifact_type,
        },
    )
    write_status_file(status_path, status_payload)

    summary = {
        "ok": True,
        "dispatch_id": args.dispatch_id,
        "case_key": bundle_summary.get("case_key", ""),
        "bundle_path": relative_to_workspace(bundle_path),
        "status_path": relative_to_workspace(status_path),
        "ready_sidecar_personas": ready_sidecar_personas,
        "pending_sidecar_personas": pending_sidecar_personas,
        "structured_bundle_path": structured_bundle_path,
        "structured_bundle_artifact_type": structured_bundle_artifact_type,
        "synthesis_prompt_path": synthesis_prompt_path,
        "synthesis_subagent_label": status_payload["synthesis_subagent_label"],
        "synthesis_target_session_key": status_payload.get("synthesis_target_session_key", ""),
        "status": status_payload["status"],
    }
    print(json.dumps(summary, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
