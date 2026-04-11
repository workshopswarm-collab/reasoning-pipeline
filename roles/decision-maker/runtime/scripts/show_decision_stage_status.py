#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    case_decision_stage_status_path,
    coerce_string,
    load_json,
    relative_to_workspace,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Show normalized Decision-Maker stage status for a case")
    parser.add_argument("--case-key", required=True)
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    status_path = case_decision_stage_status_path(args.case_key)
    if not status_path.exists():
        print(json.dumps({
            "ok": False,
            "case_key": args.case_key,
            "error": "decision stage status not found",
            "expected_path": relative_to_workspace(status_path),
        }, indent=2 if args.pretty else None))
        raise SystemExit(1)

    payload = load_json(status_path)
    summary = {
        "ok": True,
        "case_key": args.case_key,
        "status_path": relative_to_workspace(status_path),
        "status": coerce_string(payload.get("status")),
        "actor": coerce_string(payload.get("actor")),
        "updated_at": coerce_string(payload.get("updated_at")),
        "decision_context_path": coerce_string(payload.get("decision_context_path")),
        "handoff_prompt_path": coerce_string(payload.get("handoff_prompt_path")),
        "packet_json_path": coerce_string(payload.get("packet_json_path")),
        "packet_markdown_path": coerce_string(payload.get("packet_markdown_path")),
        "trade_authorization": coerce_string(payload.get("trade_authorization")),
        "decision_readiness": coerce_string(payload.get("decision_readiness")),
        "recommended_side": coerce_string(payload.get("recommended_side")),
        "target_session": coerce_string(payload.get("target_session")),
        "decision_lane_topic_id": coerce_string(payload.get("decision_lane_topic_id")),
        "decision_lane_topic_title": coerce_string(payload.get("decision_lane_topic_title")),
        "decision_lane_session_key": coerce_string(payload.get("decision_lane_session_key")),
        "decision_receipt_marker_sent_at": coerce_string(payload.get("decision_receipt_marker_sent_at")),
        "decision_analysis_marker_sent_at": coerce_string(payload.get("decision_analysis_marker_sent_at")),
        "decision_completion_marker_sent_at": coerce_string(payload.get("decision_completion_marker_sent_at")),
        "previous_status": coerce_string(payload.get("previous_status")),
        "warnings": payload.get("warnings", []),
    }
    print(json.dumps(summary, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
