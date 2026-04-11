#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    case_decision_handoff_path,
    case_decision_packet_json_path,
    case_decision_packet_markdown_path,
    case_decision_stage_status_path,
    case_syndicated_finding_path,
    case_syndicated_runtime_path,
    coerce_string,
    load_json,
    relative_to_workspace,
)
from validation import validate_decision_packet_payload  # noqa: E402


TERMINAL_OK = {"decision_completed"}
TERMINAL_FAIL = {"decision_failed"}
PREPARED_OR_RUNNING = {
    "decision_ready_for_receipt",
    "decision_analysis_running",
    "handoff_prepared",
    "handoff_sent",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reconcile Decision-Maker stage state for a case")
    parser.add_argument("--case-key", required=True)
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def load_json_if_exists(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    payload = load_json(path)
    return payload if isinstance(payload, dict) else None


def classify_health(*, status_payload: dict[str, Any] | None, synthesis_ready: bool, packet_json_exists: bool, packet_markdown_exists: bool, packet_valid: bool) -> tuple[str, list[str]]:
    problems: list[str] = []
    status_value = coerce_string((status_payload or {}).get("status"))

    if not synthesis_ready:
        problems.append("missing synthesis prerequisites")
        return "blocked", problems

    if status_payload is None:
        if packet_json_exists or packet_markdown_exists:
            problems.append("decision artifacts exist without decision-stage status")
            return "inconsistent", problems
        problems.append("decision stage has not started")
        return "not_started", problems

    if status_value in TERMINAL_FAIL:
        problems.append("decision stage is in failed status")
        return "failed", problems

    if status_value in TERMINAL_OK:
        if not packet_json_exists:
            problems.append("decision completed but packet json is missing")
            return "inconsistent", problems
        if not packet_markdown_exists:
            problems.append("decision completed but packet markdown is missing")
            return "inconsistent", problems
        if not packet_valid:
            problems.append("decision completed but packet json is invalid")
            return "inconsistent", problems
        return "ready", problems

    if status_value in PREPARED_OR_RUNNING:
        if packet_json_exists and packet_markdown_exists and packet_valid:
            problems.append("packet artifacts exist while status is still non-terminal")
            return "stale_status", problems
        return "in_progress", problems

    if packet_json_exists or packet_markdown_exists:
        problems.append("decision artifacts exist but status is not recognized")
        return "inconsistent", problems

    problems.append("decision stage status is present but not recognized")
    return "unknown", problems


def main() -> None:
    args = parse_args()
    case_key = args.case_key

    synthesis_handoff = case_decision_handoff_path(case_key)
    synthesis_runtime = case_syndicated_runtime_path(case_key)
    synthesis_finding = case_syndicated_finding_path(case_key)
    decision_status = case_decision_stage_status_path(case_key)
    packet_json = case_decision_packet_json_path(case_key)
    packet_md = case_decision_packet_markdown_path(case_key)

    status_payload = load_json_if_exists(decision_status)
    packet_payload = load_json_if_exists(packet_json)

    packet_validation = validate_decision_packet_payload(packet_payload) if packet_payload is not None else {"ok": False, "errors": ["missing packet json"], "warnings": []}

    verification_mode_path = None
    selected_input_bundle_path = None
    targeted_verification_pack_path = None
    prompt_path = None
    if isinstance(status_payload, dict):
        verification_mode_value = coerce_string(status_payload.get("verification_mode_path"))
        selected_bundle_value = coerce_string(status_payload.get("selected_input_bundle_path"))
        targeted_pack_value = coerce_string(status_payload.get("targeted_verification_pack_path"))
        prompt_value = coerce_string(status_payload.get("decision_prompt_path"))
        if verification_mode_value:
            verification_mode_path = WORKSPACE_ROOT / verification_mode_value
        if selected_bundle_value:
            selected_input_bundle_path = WORKSPACE_ROOT / selected_bundle_value
        if targeted_pack_value:
            targeted_verification_pack_path = WORKSPACE_ROOT / targeted_pack_value
        if prompt_value:
            prompt_path = WORKSPACE_ROOT / prompt_value

    synthesis_ready = synthesis_handoff.exists() and synthesis_runtime.exists() and synthesis_finding.exists()
    health, problems = classify_health(
        status_payload=status_payload,
        synthesis_ready=synthesis_ready,
        packet_json_exists=packet_json.exists(),
        packet_markdown_exists=packet_md.exists(),
        packet_valid=bool(packet_validation.get("ok")),
    )

    stage_events = (status_payload or {}).get("stage_events") if isinstance((status_payload or {}).get("stage_events"), list) else []
    last_event = stage_events[-1] if stage_events else {}

    summary = {
        "ok": health in {"ready", "in_progress", "not_started", "stale_status"},
        "case_key": case_key,
        "health": health,
        "problems": problems,
        "status": {
            "exists": decision_status.exists(),
            "path": relative_to_workspace(decision_status),
            "status": coerce_string((status_payload or {}).get("status")),
            "actor": coerce_string((status_payload or {}).get("actor")),
            "updated_at": coerce_string((status_payload or {}).get("updated_at")),
            "last_stage": coerce_string(last_event.get("stage")),
            "last_state": coerce_string(last_event.get("state")),
            "last_message": coerce_string(last_event.get("message")),
        },
        "inputs": {
            "decision_handoff_exists": synthesis_handoff.exists(),
            "decision_handoff_path": relative_to_workspace(synthesis_handoff),
            "syndicated_runtime_exists": synthesis_runtime.exists(),
            "syndicated_runtime_path": relative_to_workspace(synthesis_runtime),
            "syndicated_finding_exists": synthesis_finding.exists(),
            "syndicated_finding_path": relative_to_workspace(synthesis_finding),
            "verification_mode_exists": bool(verification_mode_path and verification_mode_path.exists()),
            "verification_mode_path": relative_to_workspace(verification_mode_path) if verification_mode_path else "",
            "selected_input_bundle_exists": bool(selected_input_bundle_path and selected_input_bundle_path.exists()),
            "selected_input_bundle_path": relative_to_workspace(selected_input_bundle_path) if selected_input_bundle_path else "",
            "targeted_verification_pack_exists": bool(targeted_verification_pack_path and targeted_verification_pack_path.exists()),
            "targeted_verification_pack_path": relative_to_workspace(targeted_verification_pack_path) if targeted_verification_pack_path else "",
            "decision_prompt_exists": bool(prompt_path and prompt_path.exists()),
            "decision_prompt_path": relative_to_workspace(prompt_path) if prompt_path else "",
        },
        "outputs": {
            "packet_json_exists": packet_json.exists(),
            "packet_json_path": relative_to_workspace(packet_json),
            "packet_json_valid": bool(packet_validation.get("ok")),
            "packet_json_errors": packet_validation.get("errors", []),
            "packet_json_warnings": packet_validation.get("warnings", []),
            "packet_markdown_exists": packet_md.exists(),
            "packet_markdown_path": relative_to_workspace(packet_md),
        },
        "recommended_actions": [],
    }

    actions: list[str] = []
    if health == "not_started":
        actions.append("run the Decision-Maker stage for this case")
    if health == "blocked":
        actions.append("regenerate synthesis artifacts before starting Decision-Maker")
    if health == "in_progress":
        actions.append("wait or inspect the decision-maker session if this remains in progress unexpectedly")
    if health == "stale_status":
        actions.append("refresh decision-stage status to reflect the completed packet artifacts")
        actions.append("run finalize_decision_stage.py --case-key <case> --apply to repair the terminal status")
    if health == "failed":
        actions.append("inspect decision-stage status, prompt, and session activity before retrying")
    if health == "inconsistent":
        actions.append("repair or regenerate missing/invalid artifacts before trusting the decision stage")
        if packet_json.exists() and packet_md.exists() and packet_validation.get("ok"):
            actions.append("run finalize_decision_stage.py --case-key <case> --apply if the artifacts are already the intended terminal outputs")
    if packet_json.exists() and not packet_validation.get("ok"):
        actions.append("fix packet generation or validation issues before using the decision output")
    if summary["inputs"]["selected_input_bundle_exists"] is False and summary["status"]["exists"]:
        actions.append("rebuild the selected-input bundle and prompt for this case")
    summary["recommended_actions"] = actions

    print(json.dumps(summary, indent=2 if args.pretty else None))
    if health in {"failed", "blocked", "inconsistent", "unknown"}:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
