#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
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
    relative_to_workspace,
    runtime_json_path_for,
)
from status import set_overall_status, update_request, write_status_file  # noqa: E402
from validation import validate_reasoning_sidecar_artifact  # noqa: E402


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
    import subprocess
    proc = subprocess.run(["ps", "-p", str(pid_int), "-o", "pid="], capture_output=True, text=True)
    return bool(proc.stdout.strip())


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    args = parse_args()
    status_path = Path(args.status_file).expanduser().resolve()
    status = load_json(status_path)
    bundle_path = WORKSPACE_ROOT / status["bundle_path"]
    bundle = load_json(bundle_path)
    persona_entries = {str(entry.get("persona") or ""): entry for entry in bundle.get("persona_findings", [])}

    repaired_requests: list[dict[str, Any]] = []
    current_personas: list[str] = []
    pending_personas: list[str] = []
    failed_personas: list[str] = []

    for req in status.get("reasoning_sidecar_requests") or []:
        persona = str(req.get("persona") or "")
        entry = persona_entries.get(persona)
        if not entry:
            failed_personas.append(persona)
            repaired_requests.append({"persona": persona, "state": "missing_bundle_persona"})
            continue
        sidecar_path = WORKSPACE_ROOT / req["artifact_path"]
        finding_path_rel = str(entry.get("path") or "")
        finding_path = WORKSPACE_ROOT / finding_path_rel
        if sidecar_path.exists() and finding_path.exists():
            try:
                payload = load_json(sidecar_path)
                persona_text = finding_path.read_text()
                validation = validate_reasoning_sidecar_artifact(
                    payload,
                    persona_finding_path=finding_path_rel,
                    source_persona_sha256=sha256_text(persona_text),
                    persona=persona,
                )
            except Exception as exc:  # noqa: BLE001
                validation = {"ok": False, "errors": [str(exc)], "warnings": []}
            if validation["ok"]:
                state = "current"
                current_personas.append(persona)
                if args.apply:
                    update_request(status, persona, {
                        "status": "completed",
                        "artifact_state": "current",
                        "artifact_validation_errors": [],
                        "artifact_validation_warnings": validation.get("warnings", []),
                    })
            else:
                state = "invalid"
                pending_personas.append(persona)
                if args.apply:
                    update_request(status, persona, {
                        "status": "missing",
                        "artifact_state": "invalid",
                        "artifact_validation_errors": validation.get("errors", []),
                        "artifact_validation_warnings": validation.get("warnings", []),
                    })
            repaired_requests.append({"persona": persona, "state": state, "errors": validation.get("errors", []), "warnings": validation.get("warnings", [])})
        else:
            pending_personas.append(persona)
            repaired_requests.append({"persona": persona, "state": "missing"})
            if args.apply:
                update_request(status, persona, {
                    "status": "missing",
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

    inferred_status = status.get("status", "waiting_for_reasoning_sidecars")
    if final_artifacts_present:
        inferred_status = "synthesis_completed"
    elif status.get("status") == "final_synthesis_launched" and final_pid and not final_process_running:
        inferred_status = "final_synthesis_failed"
    elif pending_personas or failed_personas:
        inferred_status = "waiting_for_reasoning_sidecars"
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
        status["ready_sidecar_personas"] = current_personas
        status["pending_sidecar_personas"] = pending_personas
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
