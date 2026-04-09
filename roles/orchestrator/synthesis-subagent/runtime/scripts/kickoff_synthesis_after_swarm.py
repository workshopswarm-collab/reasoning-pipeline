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

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    extraction_subagent_label,
    load_json,
    relative_to_workspace,
    synthesis_subagent_label,
    telegram_topic_session_key,
)
from status import set_overall_status, write_status_file  # noqa: E402
from validation import validate_reasoning_extract_artifact  # noqa: E402

BUILD_BUNDLE = SUBAGENT_DIR / "planner" / "scripts" / "build_synthesis_bundle.py"
BUILD_JOBS = SUBAGENT_DIR / "planner" / "scripts" / "build_reasoning_extract_jobs.py"
BUILD_EXTRACT_PROMPT = SUBAGENT_DIR / "planner" / "scripts" / "build_reasoning_extract_prompt.py"
BUILD_EXTRACTS_BUNDLE = SUBAGENT_DIR / "planner" / "scripts" / "build_extracts_synthesis_bundle.py"
BUILD_SYNTHESIS_PROMPT = SUBAGENT_DIR / "planner" / "scripts" / "build_synthesis_prompt.py"
LAUNCH_PENDING_EXTRACTORS = SUBAGENT_DIR / "runtime" / "scripts" / "launch_pending_extraction_subagents.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Kick off the synthesis stage after researcher swarm completion")
    parser.add_argument("--dispatch-id", required=True)
    parser.add_argument("--case-key", help="Optional case key to disambiguate bundle lookup")
    parser.add_argument("--build-full-if-extracts-ready", action="store_true", help="If all reasoning extracts already exist, also build the extracts-synthesis bundle and final synthesis prompt")
    parser.add_argument("--launch-extractors", action="store_true", help="Automatically launch pending extraction executors for requests that have target Telegram sessions")
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

    jobs_cmd = [sys.executable, str(BUILD_JOBS), "--bundle-json", str(bundle_path)]
    if args.pretty:
        jobs_cmd.append("--pretty")
    jobs_summary = run_json(jobs_cmd)
    jobs_path = WORKSPACE_ROOT / jobs_summary["jobs_path"]
    jobs_payload = load_json(jobs_path)

    prompt_paths = []
    extraction_requests = []
    pending_personas = []
    ready_personas = []
    for job in jobs_payload.get("jobs", []):
        persona = job["persona"]
        prompt_cmd = [
            sys.executable,
            str(BUILD_EXTRACT_PROMPT),
            "--jobs-json",
            str(jobs_path),
            "--persona",
            persona,
        ]
        if args.pretty:
            prompt_cmd.append("--pretty")
        prompt_summary = run_json(prompt_cmd)
        prompt_path = prompt_summary["prompt_path"]
        prompt_paths.append(prompt_path)
        current_prompt_path = WORKSPACE_ROOT / prompt_path
        extract_path = WORKSPACE_ROOT / job["reasoning_extract_path"]
        artifact_state = "missing"
        artifact_validation_errors: list[str] = []
        artifact_validation_warnings: list[str] = []
        if extract_path.exists():
            artifact_validation = validate_reasoning_extract_artifact(
                load_json(extract_path),
                job=job,
                prompt_text=current_prompt_path.read_text(),
            )
            if artifact_validation["ok"]:
                artifact_state = "current"
            else:
                artifact_state = "stale"
                artifact_validation_errors = artifact_validation["errors"]
                artifact_validation_warnings = artifact_validation["warnings"]
        request = {
            "persona": persona,
            "label": extraction_subagent_label(args.dispatch_id, persona),
            "prompt_path": prompt_path,
            "artifact_path": job["reasoning_extract_path"],
            "support_mode": jobs_payload.get("support_mode", "metadata_and_summaries_only"),
            "target_session_key": job.get("target_session_key") or "",
            "delivery_target_chat_id": job.get("delivery_target_chat_id") or "",
            "delivery_target_topic_id": job.get("delivery_target_topic_id"),
            "delivery_target_topic_title": job.get("delivery_target_topic_title") or "",
            "visible_start_marker": f"STARTING EXTRACTION | market={question} | persona={persona} | dispatch_id={args.dispatch_id} | extract_path={job['reasoning_extract_path']}",
            "visible_finish_marker": f"FINISHED EXTRACTION | market={question} | persona={persona} | dispatch_id={args.dispatch_id} | extract_path={job['reasoning_extract_path']}",
            "research_run_id": job.get("research_run_id") or "",
            "artifact_state": artifact_state,
            "artifact_validation_errors": artifact_validation_errors,
            "artifact_validation_warnings": artifact_validation_warnings,
            "status": "ready" if artifact_state != "current" else "already_present",
        }
        extraction_requests.append(request)
        if artifact_state == "current":
            ready_personas.append(persona)
        else:
            pending_personas.append(persona)

    controller_chat_id = next((job.get("controller_chat_id") for job in jobs_payload.get("jobs", []) if job.get("controller_chat_id")), "")
    controller_topic_id = next((job.get("controller_topic_id") for job in jobs_payload.get("jobs", []) if job.get("controller_topic_id")), "")
    controller_topic_title = next((job.get("controller_topic_title") for job in jobs_payload.get("jobs", []) if job.get("controller_topic_title")), "")

    extracts_bundle_path = ""
    synthesis_prompt_path = ""
    if args.build_full_if_extracts_ready and not pending_personas:
        extracts_cmd = [
            sys.executable,
            str(BUILD_EXTRACTS_BUNDLE),
            "--bundle-json",
            str(bundle_path),
            "--jobs-json",
            str(jobs_path),
        ]
        if args.pretty:
            extracts_cmd.append("--pretty")
        extracts_summary = run_json(extracts_cmd)
        extracts_bundle_path = extracts_summary["extracts_bundle_path"]
        synthesis_cmd = [
            sys.executable,
            str(BUILD_SYNTHESIS_PROMPT),
            "--bundle-json",
            str(WORKSPACE_ROOT / extracts_bundle_path),
        ]
        if args.pretty:
            synthesis_cmd.append("--pretty")
        synthesis_summary = run_json(synthesis_cmd)
        synthesis_prompt_path = synthesis_summary["prompt_path"]

    status_path = bundle_path.with_name("synthesis-stage-status.json")
    status_payload = {
        "artifact_type": "synthesis_stage_status",
        "dispatch_id": args.dispatch_id,
        "case_key": bundle_summary.get("case_key", ""),
        "bundle_path": relative_to_workspace(bundle_path),
        "jobs_path": relative_to_workspace(jobs_path),
        "reasoning_extract_prompt_paths": prompt_paths,
        "extraction_subagent_requests": extraction_requests,
        "ready_personas": ready_personas,
        "pending_personas": pending_personas,
        "extracts_bundle_path": extracts_bundle_path,
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
        "ready_for_final_synthesis" if synthesis_prompt_path else "ready_for_reasoning_extracts",
        stage="kickoff",
        message="Synthesis kickoff prepared current-stage artifacts",
        extra={
            "ready_personas": ready_personas,
            "pending_personas": pending_personas,
        },
    )
    write_status_file(status_path, status_payload)

    launcher_summary = {}
    if args.launch_extractors and pending_personas:
        launcher_proc = subprocess.run(
            [
                sys.executable,
                str(LAUNCH_PENDING_EXTRACTORS),
                "--status-file",
                str(status_path),
                *( ["--pretty"] if args.pretty else [] ),
            ],
            cwd=str(WORKSPACE_ROOT),
            capture_output=True,
            text=True,
            check=False,
        )
        if launcher_proc.returncode == 0 and launcher_proc.stdout.strip():
            launcher_summary = json.loads(launcher_proc.stdout)
            status_payload = load_json(status_path)
            extraction_requests = status_payload.get("extraction_subagent_requests", extraction_requests)
        else:
            launcher_summary = {
                "ok": False,
                "stdout": launcher_proc.stdout,
                "stderr": launcher_proc.stderr,
                "returncode": launcher_proc.returncode,
            }

    summary = {
        "ok": True,
        "dispatch_id": args.dispatch_id,
        "case_key": bundle_summary.get("case_key", ""),
        "bundle_path": relative_to_workspace(bundle_path),
        "jobs_path": relative_to_workspace(jobs_path),
        "status_path": relative_to_workspace(status_path),
        "ready_personas": ready_personas,
        "pending_personas": pending_personas,
        "extraction_subagent_requests": extraction_requests,
        "extracts_bundle_path": extracts_bundle_path,
        "synthesis_prompt_path": synthesis_prompt_path,
        "synthesis_subagent_label": status_payload["synthesis_subagent_label"],
        "synthesis_target_session_key": status_payload.get("synthesis_target_session_key", ""),
        "launcher_summary": launcher_summary,
        "status": status_payload["status"],
    }
    print(json.dumps(summary, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
