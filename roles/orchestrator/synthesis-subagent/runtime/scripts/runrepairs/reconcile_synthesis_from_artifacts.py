#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR.parent
SUBAGENT_DIR = SCRIPTS_DIR.parents[1]
for path in [SCRIPTS_DIR, SUBAGENT_DIR]:
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    append_case_timeline_entry,
    case_decision_handoff_path_for,
    case_synthesis_markdown_path_for,
    load_json,
    reasoning_extract_prompt_path_for,
    relative_to_workspace,
    runtime_json_path_for,
)
from status import set_overall_status, update_request, write_status_file  # noqa: E402
from validation import validate_reasoning_extract_artifact  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reconcile synthesis stage state from current artifacts")
    parser.add_argument("--status-file", required=True, help="synthesis-stage-status.json path")
    parser.add_argument("--apply", action="store_true", help="Write repaired status back to disk")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def process_running(pid: Any) -> bool:
    try:
        pid_int = int(pid)
    except (TypeError, ValueError):
        return False
    proc = subprocess.run(["ps", "-p", str(pid_int), "-o", "pid="], capture_output=True, text=True)
    return bool(proc.stdout.strip())


def main() -> int:
    args = parse_args()
    status_path = Path(args.status_file).expanduser().resolve()
    status = load_json(status_path)
    jobs_path = WORKSPACE_ROOT / status["jobs_path"]
    jobs_payload = load_json(jobs_path)
    jobs_by_persona = {job["persona"]: job for job in jobs_payload.get("jobs", [])}

    repaired_requests: list[dict[str, Any]] = []
    current_personas: list[str] = []
    pending_personas: list[str] = []
    failed_personas: list[str] = []

    for req in status.get("extraction_subagent_requests") or []:
        persona = req.get("persona") or ""
        job = jobs_by_persona.get(persona)
        if not job:
            failed_personas.append(persona)
            repaired_requests.append({"persona": persona, "state": "missing_job"})
            continue
        extract_path = WORKSPACE_ROOT / req["artifact_path"]
        prompt_path = WORKSPACE_ROOT / reasoning_extract_prompt_path_for(jobs_path, persona)
        if extract_path.exists() and prompt_path.exists():
            validation = validate_reasoning_extract_artifact(load_json(extract_path), job=job, prompt_text=prompt_path.read_text())
            if validation["ok"]:
                state = "current"
                current_personas.append(persona)
                if args.apply:
                    update_request(status, persona, {
                        "status": "completed",
                        "artifact_state": "current",
                        "artifact_validation_errors": [],
                        "artifact_validation_warnings": validation["warnings"],
                    })
            else:
                state = "stale"
                pending_personas.append(persona)
                if args.apply:
                    update_request(status, persona, {
                        "status": "ready",
                        "artifact_state": "stale",
                        "artifact_validation_errors": validation["errors"],
                        "artifact_validation_warnings": validation["warnings"],
                    })
            repaired_requests.append({"persona": persona, "state": state, "errors": validation.get("errors", []), "warnings": validation.get("warnings", [])})
        else:
            pending_personas.append(persona)
            repaired_requests.append({"persona": persona, "state": "missing"})
            if args.apply:
                update_request(status, persona, {
                    "status": "ready",
                    "artifact_state": "missing",
                })

    status_counts = {
        "current": len(current_personas),
        "pending": len(pending_personas),
        "failed": len(failed_personas),
    }

    case_key = status.get("case_key") or ""
    dispatch_artifact_path = status_path.with_name("syndicated-finding.md")
    dispatch_sidecar_path = runtime_json_path_for(dispatch_artifact_path)
    dispatch_handoff_path = status_path.with_name("decision-handoff.md")
    artifact_path = case_synthesis_markdown_path_for(case_key)
    sidecar_path = runtime_json_path_for(artifact_path)
    handoff_path = case_decision_handoff_path_for(case_key)
    final_artifacts_present = artifact_path.exists() and sidecar_path.exists() and handoff_path.exists()

    final_pid = status.get("final_synthesis_pid")
    final_process_running = process_running(final_pid)

    inferred_status = status.get("status", "ready_for_reasoning_extracts")
    if failed_personas:
        inferred_status = "reasoning_extracts_failed"
    elif final_artifacts_present:
        inferred_status = "synthesis_completed"
    elif status.get("status") == "final_synthesis_launched" and final_pid and not final_process_running:
        inferred_status = "final_synthesis_failed"
    elif pending_personas:
        inferred_status = "ready_for_reasoning_extracts"
    else:
        inferred_status = "ready_for_final_synthesis"

    timeline_update = None
    if args.apply and final_artifacts_present:
        dispatch_id = status.get("dispatch_id") or ""
        timeline_artifact_path = dispatch_artifact_path if dispatch_artifact_path.exists() else artifact_path
        artifact_rel = relative_to_workspace(timeline_artifact_path)
        timestamp = datetime.now(timezone.utc).isoformat()
        entry = f"- {timestamp} — completed synthesis `{dispatch_id}` with artifact `{artifact_rel}`."
        unique_token = f"completed synthesis `{dispatch_id}` with artifact `{artifact_rel}`."
        timeline_update = {
            "appended": append_case_timeline_entry(case_key, entry, unique_token=unique_token),
            "case_key": case_key,
            "dispatch_id": dispatch_id,
            "artifact_path": artifact_rel,
            "entry": entry,
        }

    if args.apply:
        status["ready_personas"] = current_personas
        status["pending_personas"] = pending_personas
        status["final_artifact_path"] = relative_to_workspace(dispatch_artifact_path) if dispatch_artifact_path.exists() else status.get("final_artifact_path", "")
        status["final_sidecar_path"] = relative_to_workspace(dispatch_sidecar_path) if dispatch_sidecar_path.exists() else status.get("final_sidecar_path", "")
        status["final_decision_handoff_path"] = relative_to_workspace(dispatch_handoff_path) if dispatch_handoff_path.exists() else status.get("final_decision_handoff_path", "")
        if timeline_update is not None:
            status["timeline_update"] = timeline_update
        if inferred_status == "final_synthesis_failed" and final_pid and not final_process_running:
            status["final_synthesis_failure_reason"] = "final synthesis process is no longer running and final artifacts are absent"
        set_overall_status(status, inferred_status, stage="synthesis_repair", message="Reconciled synthesis stage state from artifacts", extra={"counts": status_counts, "final_artifacts_present": final_artifacts_present, "final_process_running": final_process_running})
        write_status_file(status_path, status)

    out = {
        "status": "applied" if args.apply else "dry_run",
        "status_file": relative_to_workspace(status_path),
        "inferred_status": inferred_status,
        "counts": status_counts,
        "final_artifacts_present": final_artifacts_present,
        "final_synthesis_pid": final_pid,
        "final_process_running": final_process_running,
        "timeline_update": timeline_update,
        "repaired_requests": repaired_requests,
    }
    print(json.dumps(out, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
