#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.case_artifacts import discover_case_artifacts  # noqa: E402
from lib.io import extract_timeline_events, iso_sort_key, write_json  # noqa: E402
from lib.paths import ensure_parent, to_repo_relative  # noqa: E402


def infer_event_type(summary: str) -> str:
    lower = summary.lower()
    if "prepared analysis" in lower:
        return "research_dispatch_prepared"
    if "completed synthesis" in lower:
        return "synthesis_completed"
    if "decision-making" in lower:
        return "decision_completed"
    if "refresh" in lower:
        return "refresh_event"
    return "case_event"


def build_timeline(case_key: str) -> dict[str, Any]:
    artifacts = discover_case_artifacts(case_key)
    events: list[dict[str, Any]] = []
    warnings: list[str] = []

    timeline_text = artifacts.get("timeline_text") or ""
    for item in extract_timeline_events(timeline_text):
        events.append({
            "ts": item.get("ts"),
            "event_type": infer_event_type(item.get("summary", "")),
            "observed": True,
            "summary": item.get("summary"),
            "source_paths": [to_repo_relative(artifacts["timeline_path"])] if artifacts.get("timeline_path") and artifacts["timeline_path"].exists() else [],
            "metadata": {},
        })

    decision_packet = artifacts.get("decision_packet_json") or {}
    if decision_packet:
        generated_at = decision_packet.get("generated_at")
        if generated_at and not any(e["ts"] == generated_at and e["event_type"] == "decision_completed" for e in events):
            events.append({
                "ts": generated_at,
                "event_type": "decision_completed",
                "observed": True,
                "summary": "decision packet generated",
                "source_paths": [to_repo_relative(artifacts["decision_packet_json_path"])],
                "metadata": {
                    "trade_authorization": (decision_packet.get("decision") or {}).get("trade_authorization"),
                    "side": (decision_packet.get("decision") or {}).get("side"),
                },
            })

    synthesis_runtime = artifacts.get("synthesis_runtime") or {}
    synthesis_ts = synthesis_runtime.get("market_snapshot_time")
    if synthesis_ts and not any(e["ts"] == synthesis_ts and e["event_type"] == "synthesis_completed" for e in events):
        events.append({
            "ts": synthesis_ts,
            "event_type": "synthesis_completed",
            "observed": True,
            "summary": "synthesis runtime artifact written",
            "source_paths": [to_repo_relative(artifacts["synthesis_runtime_path"])],
            "metadata": {
                "dispatch_id": synthesis_runtime.get("dispatch_id"),
                "synthesis_status": synthesis_runtime.get("synthesis_status"),
            },
        })

    swarm_current = artifacts.get("swarm_current") or {}
    if swarm_current:
        bullets = swarm_current.get("bullet_map") or {}
        if bullets.get("completed_persona_count"):
            events.append({
                "ts": None,
                "event_type": "research_completion_state",
                "observed": True,
                "summary": f"research swarm reported {bullets.get('completed_persona_count')} completed personas",
                "source_paths": [to_repo_relative(swarm_current["path"])],
                "metadata": {
                    "completed_persona_count": bullets.get("completed_persona_count"),
                    "expected_persona_count": bullets.get("expected_persona_count"),
                    "pipeline_status": bullets.get("pipeline_status"),
                },
            })

    if not events:
        warnings.append("no_case_events_detected")

    ordered = sorted(events, key=lambda item: (iso_sort_key(item.get("ts")), item.get("event_type") or ""))
    return {
        "artifact_type": "case_event_timeline",
        "schema_version": "v1",
        "case_key": case_key,
        "event_count": len(ordered),
        "events": ordered,
        "warnings": warnings,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a structured evaluator event timeline for one case")
    parser.add_argument("--case-key", required=True)
    parser.add_argument("--out")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data = build_timeline(args.case_key)
    if args.out:
        out_path = ensure_parent(Path(args.out))
        write_json(out_path, data, pretty=True if args.pretty or True else False)
    else:
        import json
        print(json.dumps(data, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
