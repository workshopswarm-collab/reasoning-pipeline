#!/usr/bin/env python3
"""Runtime-side dispatch helper for the research swarm.

This script keeps the OpenClaw runtime boundary thin and deterministic.
It does not call OpenClaw tools itself; instead it:
- validates a planner-emitted dispatch manifest
- builds a Telegram topic bootstrap / handoff plan with idempotency guidance
- builds filled post-handoff DB patch payloads from resolved topic/session metadata
- finalizes a launch summary from per-run outcomes

Intended pipeline fit:
- dispatch_case_research.py -> emits manifest for fresh Telegram forum topics
- OpenClaw runtime in TUI/main -> calls this internal helper with action=prepare
- OpenClaw runtime in TUI/main -> creates controller/persona topics and resolves topic session keys
- OpenClaw runtime in TUI/main -> materializes each topic session and delivers via `sessions.send`
- OpenClaw runtime in TUI/main -> calls this internal helper with action=build-patch per successful handoff
- OpenClaw runtime in TUI/main -> patches DB via update_research_run.py
- OpenClaw runtime in TUI/main -> calls this internal helper with action=finalize-summary
"""

import argparse
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Optional

VALID_PERSONAS = {
    "base-rate",
    "market-implied",
    "variant-view",
    "risk-manager",
    "catalyst-hunter",
}

STATUS_DELIVERED = "delivered"
STATUS_SKIPPED = "skipped_existing"
STATUS_FAILED = "failed"
RUN_STATUS_QUEUED = "queued"
RUN_STATUS_RUNNING = "running"
RUN_STATUS_COMPLETED = "completed"
RUN_STATUS_FAILED = "failed"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Runtime-side dispatch helper")
    parser.add_argument("--file", default="-", help="Path to manifest JSON, or - for stdin")
    parser.add_argument(
        "--action",
        choices=["validate", "prepare", "build-patch", "finalize-summary"],
        default="validate",
    )
    parser.add_argument("--research-run-id", help="research_run_id for build-patch")
    parser.add_argument("--target-session-key", help="Resolved Telegram topic session key for build-patch")
    parser.add_argument("--delivery-chat-id", help="Resolved Telegram chat id for build-patch")
    parser.add_argument("--delivery-topic-id", help="Resolved Telegram topic id for build-patch")
    parser.add_argument("--delivery-topic-title", help="Resolved Telegram topic title for build-patch")
    parser.add_argument("--controller-topic-id", help="Resolved controller topic id for build-patch")
    parser.add_argument("--controller-topic-title", help="Resolved controller topic title for build-patch")
    parser.add_argument(
        "--existing-map-json",
        help=(
            "JSON object keyed by research_run_id with existing runtime state, e.g. "
            "{\"<id>\": {\"status\": \"running\", \"delivery_target_session_key\": \"...\"}}"
        ),
    )
    parser.add_argument("--run-results-json", help="JSON array of per-run result objects for finalize-summary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def load_json(path_str: str):
    if path_str == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path_str).read_text()
    if not raw.strip():
        raise ValueError("input JSON is empty")
    return json.loads(raw)


def require(obj: dict, key: str):
    value = obj.get(key)
    if value is None or value == "":
        raise ValueError(f"missing required field: {key}")
    return value


def validate_manifest(manifest: dict) -> dict:
    require(manifest, "dispatch_id")
    require(manifest, "created_at")
    case = require(manifest, "case")
    market = require(manifest, "market")
    runtime_defaults = require(manifest, "runtime_defaults")
    runs = require(manifest, "runs")

    if not isinstance(case, dict):
        raise ValueError("case must be an object")
    if not isinstance(market, dict):
        raise ValueError("market must be an object")
    if not isinstance(runtime_defaults, dict):
        raise ValueError("runtime_defaults must be an object")
    if not isinstance(runs, list) or not runs:
        raise ValueError("runs must be a non-empty array")

    require(case, "case_id")
    require(case, "case_key")
    require(market, "market_id")
    require(runtime_defaults, "runtime")

    normalized_runs = []
    for run in runs:
        if not isinstance(run, dict):
            raise ValueError("each run must be an object")
        require(run, "research_run_id")
        persona = require(run, "persona")
        if persona not in VALID_PERSONAS:
            raise ValueError(f"unsupported persona: {persona}")
        require(run, "run_label")
        require(run, "workspace_note_path")
        handoff = require(run, "handoff")
        if not isinstance(handoff, dict):
            raise ValueError("run.handoff must be an object")
        target = require(handoff, "target")
        handoff_payload = require(handoff, "handoff_payload")
        patch_template = require(handoff, "post_handoff_update_template")
        if not isinstance(target, dict):
            raise ValueError("handoff.target must be an object")
        if not isinstance(handoff_payload, dict):
            raise ValueError("handoff_payload must be an object")
        if not isinstance(patch_template, dict):
            raise ValueError("post_handoff_update_template must be an object")
        target_kind = require(target, "kind")
        if target_kind != "telegram_forum_topic":
            raise ValueError(f"unsupported handoff target kind: {target_kind}")
        require(target, "chat_id")
        require(target, "topic_title")
        require(target, "controller_topic_title")
        require(handoff_payload, "chatId")
        require(handoff_payload, "topicTitle")
        require(handoff_payload, "message")
        require(patch_template, "research_run_id")
        require(patch_template, "status")
        require(patch_template, "workspace_note_path")
        notes = require(patch_template, "notes")
        if not isinstance(notes, dict):
            raise ValueError("post_handoff_update_template.notes must be an object")
        normalized_runs.append(run)

    return {
        "dispatch_id": manifest["dispatch_id"],
        "case_id": case["case_id"],
        "market_id": market["market_id"],
        "run_count": len(normalized_runs),
        "personas": [r["persona"] for r in normalized_runs],
        "status": "valid",
    }


def prepare_launch_plan(manifest: dict, existing_map: Optional[dict] = None) -> dict:
    validate_manifest(manifest)
    existing_map = existing_map or {}

    launchable_runs = []
    skipped_runs = []
    for run in manifest["runs"]:
        research_run_id = run["research_run_id"]
        existing = existing_map.get(research_run_id) or {}
        existing_status = existing.get("status")
        delivery_target_session_key = existing.get("delivery_target_session_key")
        if existing_status and existing_status != RUN_STATUS_QUEUED:
            skipped_runs.append(
                {
                    "research_run_id": research_run_id,
                    "persona": run["persona"],
                    "status": STATUS_SKIPPED,
                    "reason": f"existing status is {existing_status}",
                    "delivery_target_session_key": delivery_target_session_key,
                    "workspace_note_path": run["workspace_note_path"],
                }
            )
            continue

        launchable_runs.append(
            {
                "research_run_id": research_run_id,
                "persona": run["persona"],
                "run_label": run["run_label"],
                "workspace_note_path": run["workspace_note_path"],
                "target": run["handoff"]["target"],
                "handoff_payload": run["handoff"]["handoff_payload"],
                "post_handoff_update_template": run["handoff"]["post_handoff_update_template"],
            }
        )

    return {
        "dispatch_id": manifest["dispatch_id"],
        "case_id": manifest["case"]["case_id"],
        "market_id": manifest["market"]["market_id"],
        "status": "prepared",
        "launchable_count": len(launchable_runs),
        "skipped_count": len(skipped_runs),
        "launchable_runs": launchable_runs,
        "skipped_runs": skipped_runs,
        "operator_instructions": [
            "create the controller topic once for this dispatch and one fresh persona topic per launchable run",
            "resolve each created persona topic to its canonical Telegram topic session key before delivery",
            "materialize the topic session and deliver the internal assignment via sessions.send",
            "after topic bootstrap, fan out the resolved persona launch steps in parallel where possible rather than sending them strictly one by one",
            "treat the queued->running patch as the canonical start transition; update_research_run.py emits the visible STARTING marker from stored delivery metadata",
            "after each successful handoff, build a patch payload with action=build-patch using the resolved session/topic metadata",
            "apply that patch via update_research_run.py",
            "if some handoffs fail and some succeed, keep successful handoffs, record failures, and treat overall dispatch as delivered_partial",
            "on retry, rerun prepare with fresh existing_map_json so non-queued runs are skipped and existing topics are reused",
        ],
    }


def build_patch(
    manifest: dict,
    research_run_id: str,
    target_session_key: str,
    *,
    delivery_chat_id: Optional[str] = None,
    delivery_topic_id: Optional[str] = None,
    delivery_topic_title: Optional[str] = None,
    controller_topic_id: Optional[str] = None,
    controller_topic_title: Optional[str] = None,
) -> dict:
    validate_manifest(manifest)
    for run in manifest["runs"]:
        if run["research_run_id"] == research_run_id:
            patch = deepcopy(run["handoff"]["post_handoff_update_template"])
            notes = patch.setdefault("notes", {})
            patch["status"] = RUN_STATUS_RUNNING
            patch["mark_started"] = True
            notes["delivery_target_session_key"] = target_session_key
            if delivery_chat_id:
                notes["delivery_target_chat_id"] = delivery_chat_id
            if delivery_topic_id:
                notes["delivery_target_topic_id"] = delivery_topic_id
            if delivery_topic_title:
                notes["delivery_target_topic_title"] = delivery_topic_title
            if controller_topic_id:
                notes["controller_topic_id"] = controller_topic_id
            if controller_topic_title:
                notes["controller_topic_title"] = controller_topic_title
            notes["dispatch_id"] = manifest["dispatch_id"]
            notes["dispatch_stage"] = "persona_topic_running"
            return patch
    raise ValueError(f"research_run_id not found in manifest: {research_run_id}")


def finalize_summary(manifest: dict, run_results: list[dict]) -> dict:
    validate_manifest(manifest)
    delivered_count = sum(1 for r in run_results if r.get("status") == STATUS_DELIVERED)
    skipped_count = sum(1 for r in run_results if r.get("status") == STATUS_SKIPPED)
    failed_count = sum(1 for r in run_results if r.get("status") == STATUS_FAILED)

    if delivered_count > 0 and failed_count == 0:
        overall_status = "delivered_all"
    elif delivered_count > 0 and failed_count > 0:
        overall_status = "delivered_partial"
    elif delivered_count == 0 and failed_count > 0:
        overall_status = "delivery_failed"
    elif skipped_count == len(run_results) and run_results:
        overall_status = "skipped_all"
    else:
        overall_status = "delivery_failed"

    return {
        "dispatch_id": manifest["dispatch_id"],
        "case_id": manifest["case"]["case_id"],
        "market_id": manifest["market"]["market_id"],
        "status": overall_status,
        "delivered_count": delivered_count,
        "skipped_count": skipped_count,
        "failed_count": failed_count,
        "runs": run_results,
        "retry_guidance": (
            "retry only failed runs by rerunning prepare/finalize with fresh existing_map_json; non-queued runs should be skipped"
            if overall_status == "delivered_partial"
            else None
        ),
    }


def main() -> int:
    args = parse_args()
    try:
        manifest = load_json(args.file)
        if args.action == "validate":
            result = validate_manifest(manifest)
        elif args.action == "prepare":
            existing_map = json.loads(args.existing_map_json) if args.existing_map_json else {}
            result = prepare_launch_plan(manifest, existing_map=existing_map)
        elif args.action == "build-patch":
            if not args.research_run_id:
                raise ValueError("--research-run-id is required for build-patch")
            if not args.target_session_key:
                raise ValueError("--target-session-key is required for build-patch")
            result = build_patch(
                manifest,
                args.research_run_id,
                args.target_session_key,
                delivery_chat_id=args.delivery_chat_id,
                delivery_topic_id=args.delivery_topic_id,
                delivery_topic_title=args.delivery_topic_title,
                controller_topic_id=args.controller_topic_id,
                controller_topic_title=args.controller_topic_title,
            )
        else:
            if not args.run_results_json:
                raise ValueError("--run-results-json is required for finalize-summary")
            run_results = json.loads(args.run_results_json)
            if not isinstance(run_results, list):
                raise ValueError("run_results_json must decode to an array")
            result = finalize_summary(manifest, run_results)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(result, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
