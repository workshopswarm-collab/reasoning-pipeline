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
    append_case_timeline_entry,
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
from status import append_stage_event, locked_status, set_overall_status  # noqa: E402
from validation import validate_decision_packet_payload  # noqa: E402
from reconcile_decision_stage import classify_health, load_json_if_exists  # noqa: E402

REPAIRABLE_HEALTH = {"stale_status", "inconsistent"}
ALREADY_FINAL = {"ready"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Finalize/repair decision-stage status from existing valid artifacts")
    parser.add_argument("--case-key", required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def append_decision_timeline_entry(case_key: str, dispatch_id: str, packet_path: str) -> dict[str, Any]:
    entry = f"- repaired/finalized decision-making `{dispatch_id}` with packet `{packet_path}`."
    unique_token = f"decision-making `{dispatch_id}` with packet `{packet_path}`."
    appended = append_case_timeline_entry(case_key, entry, unique_token=unique_token)
    return {
        "appended": appended,
        "case_key": case_key,
        "dispatch_id": dispatch_id,
        "packet_path": packet_path,
        "entry": entry,
    }


def main() -> None:
    args = parse_args()
    case_key = args.case_key

    synthesis_handoff = case_decision_handoff_path(case_key)
    synthesis_runtime = case_syndicated_runtime_path(case_key)
    synthesis_finding = case_syndicated_finding_path(case_key)
    status_path = case_decision_stage_status_path(case_key)
    packet_json_path = case_decision_packet_json_path(case_key)
    packet_markdown_path = case_decision_packet_markdown_path(case_key)

    status_payload = load_json_if_exists(status_path)
    packet_payload = load_json_if_exists(packet_json_path)
    packet_validation = validate_decision_packet_payload(packet_payload) if packet_payload is not None else {"ok": False, "errors": ["missing packet json"], "warnings": []}
    synthesis_ready = synthesis_handoff.exists() and synthesis_runtime.exists() and synthesis_finding.exists()
    health, problems = classify_health(
        status_payload=status_payload,
        synthesis_ready=synthesis_ready,
        packet_json_exists=packet_json_path.exists(),
        packet_markdown_exists=packet_markdown_path.exists(),
        packet_valid=bool(packet_validation.get("ok")),
    )

    packet_context = (packet_payload or {}).get("context") if isinstance(packet_payload, dict) else {}
    packet_decision = (packet_payload or {}).get("decision") if isinstance(packet_payload, dict) else {}
    dispatch_id = coerce_string((status_payload or {}).get("dispatch_id")) or coerce_string((packet_context or {}).get("dispatch_id"))
    timeline_update = None

    can_finalize = synthesis_ready and packet_json_path.exists() and packet_markdown_path.exists() and bool(packet_validation.get("ok")) and (health in REPAIRABLE_HEALTH or status_payload is None)
    summary = {
        "ok": can_finalize or health in ALREADY_FINAL,
        "case_key": case_key,
        "health": health,
        "problems": problems,
        "apply_requested": args.apply,
        "can_finalize": can_finalize,
        "status_path": relative_to_workspace(status_path),
        "packet_json_path": relative_to_workspace(packet_json_path),
        "packet_markdown_path": relative_to_workspace(packet_markdown_path),
        "warnings": packet_validation.get("warnings", []),
        "notes": [],
    }

    if health in ALREADY_FINAL:
        summary["notes"].append("decision stage already looks finalized and valid")
    elif not can_finalize:
        if not synthesis_ready:
            summary["notes"].append("cannot finalize without synthesis prerequisites")
        if not packet_json_path.exists() or not packet_markdown_path.exists():
            summary["notes"].append("cannot finalize without both packet artifacts")
        if not packet_validation.get("ok"):
            summary["notes"].append("cannot finalize because packet json is invalid")

    if args.apply and can_finalize:
        packet_path_rel = relative_to_workspace(packet_markdown_path)
        if dispatch_id:
            timeline_update = append_decision_timeline_entry(case_key, dispatch_id, packet_path_rel)
        with locked_status(status_path) as status:
            status.setdefault("artifact_type", "decision_stage_status")
            status.setdefault("schema_version", "decision-stage-status/v1")
            status["case_key"] = case_key
            if dispatch_id:
                status["dispatch_id"] = dispatch_id
            status["actor"] = "decision-maker"
            status["packet_json_path"] = relative_to_workspace(packet_json_path)
            status["packet_markdown_path"] = packet_path_rel
            status["trade_authorization"] = coerce_string(packet_decision.get("trade_authorization"))
            status["position_policy"] = coerce_string(packet_decision.get("position_policy"))
            status["decision_readiness"] = coerce_string(packet_decision.get("decision_readiness"))
            status["recommended_side"] = coerce_string(packet_decision.get("side"))
            if timeline_update is not None:
                status["timeline_update"] = timeline_update
            append_stage_event(status, stage="decision_finalize_repair", state="repair_applied", message="Refreshed decision-stage status from existing valid packet artifacts", extra={"previous_health": health})
            set_overall_status(status, "decision_completed", stage="decision_finalize_repair", message="Decision-stage status finalized from existing valid artifacts", extra={"warnings": packet_validation.get("warnings", []), "previous_health": health})
        summary["applied"] = True
        summary["decision_stage_status_path"] = relative_to_workspace(status_path)
        summary["timeline_update"] = timeline_update or {}
        summary["notes"].append("decision-stage status repaired/finalized")
    elif args.apply and health in ALREADY_FINAL:
        summary["applied"] = False
        summary["notes"].append("no mutation applied because the stage already appears finalized")
    else:
        summary["applied"] = False
        if can_finalize:
            summary["notes"].append("run again with --apply to persist the repaired terminal status")

    print(json.dumps(summary, indent=2 if args.pretty else None))
    if args.apply and not can_finalize and health not in ALREADY_FINAL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
