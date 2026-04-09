#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import relative_to_workspace  # noqa: E402
from status import load_status_file  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Show a compact synthesis stage status summary")
    parser.add_argument("--status-file", required=True)
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.status_file).expanduser().resolve()
    status = load_status_file(path)
    out = {
        "status_file": relative_to_workspace(path),
        "status": status.get("status"),
        "updated_at": status.get("updated_at"),
        "request_status_counts": status.get("request_status_counts"),
        "ready_personas": status.get("ready_personas"),
        "pending_personas": status.get("pending_personas"),
        "synthesis_lane": status.get("synthesis_lane"),
        "last_stage_event": status.get("last_stage_event"),
        "terminal_summary": status.get("terminal_summary"),
        "final_artifact_path": status.get("final_artifact_path", ""),
        "final_sidecar_path": status.get("final_sidecar_path", ""),
        "final_decision_handoff_path": status.get("final_decision_handoff_path", ""),
    }
    print(json.dumps(out, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
