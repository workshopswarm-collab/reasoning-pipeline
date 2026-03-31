#!/usr/bin/env python3
"""Run the realtime runtime-side orchestration sequence for a dispatch manifest.

This script is the runtime wrapper around the existing pipeline scripts. It is
still intentionally split from actual OpenClaw tool execution:
- Python prepares/normalizes the orchestration sequence
- the TUI/main OpenClaw runtime creates Telegram topics and performs sessions_send into them
- Python builds DB patches and finalizes summaries

The wrapper supports two operational modes:
1. plan-only: emit the exact sequence the OpenClaw runtime should execute
2. replay-results: build DB patch steps + dispatch summary from actual handoff results

This keeps the control plane explicit while fitting the current pipeline.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = BASE_DIR.parent
PIPELINE_DIR = RUNTIME_DIR.parent
WORKSPACE_ROOT = PIPELINE_DIR.parents[2]
DEFAULT_ENV_PATH = WORKSPACE_ROOT / ".env"
RUNTIME_HELPER = BASE_DIR / "runtime_execute_dispatch.py"
UPDATE_RUN = BASE_DIR / "update_research_run.py"


def maybe_load_workspace_env() -> None:
    if os.getenv("PREDQUANT_ORCHESTRATOR_URL"):
        return
    if not DEFAULT_ENV_PATH.exists():
        return
    for raw_line in DEFAULT_ENV_PATH.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Realtime runtime-side orchestration wrapper")
    parser.add_argument("--file", default="-", help="Path to dispatch manifest JSON, or - for stdin")
    parser.add_argument(
        "--existing-map-json",
        help="JSON object keyed by research_run_id with existing runtime state for idempotency",
    )
    parser.add_argument(
        "--handoff-results-json",
        help=(
            "JSON array of actual handoff results keyed by research_run_id, "
            "used to build DB patch commands and finalize summary"
        ),
    )
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
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


def python_json(script: Path, args: list[str], stdin_payload=None) -> dict:
    proc = subprocess.run(
        [sys.executable, str(script), *args],
        input=(json.dumps(stdin_payload) if stdin_payload is not None else None),
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"{script.name} failed")

    stdout = proc.stdout.strip()
    if not stdout:
        raise RuntimeError(f"{script.name} returned empty stdout")

    lines = [line for line in stdout.splitlines() if line.strip()]
    for line in reversed(lines):
        try:
            return json.loads(line)
        except json.JSONDecodeError:
            continue

    return json.loads(stdout)


def build_update_command(patch_payload: dict, db_url: str) -> list[str]:
    cmd = [
        sys.executable,
        str(UPDATE_RUN),
        "--research-run-id", patch_payload["research_run_id"],
        "--status", patch_payload["status"],
        "--workspace-note-path", patch_payload["workspace_note_path"],
        "--notes-json", json.dumps(patch_payload.get("notes", {}), separators=(",", ":")),
    ]
    if patch_payload.get("mark_started"):
        cmd.append("--mark-started")
    if db_url:
        cmd.extend(["--db-url", db_url])
    return cmd


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    try:
        manifest = load_json(args.file)

        validate_result = python_json(RUNTIME_HELPER, ["--action", "validate"], manifest)

        existing_map = json.loads(args.existing_map_json) if args.existing_map_json else {}
        prepare_result = python_json(
            RUNTIME_HELPER,
            [
                "--action", "prepare",
                "--existing-map-json", json.dumps(existing_map, separators=(",", ":")),
            ],
            manifest,
        )

        result = {
            "dispatch_id": manifest["dispatch_id"],
            "validation": validate_result,
            "prepare": prepare_result,
            "runtime_tool_loop_required": True,
            "runtime_tool_loop": [],
            "runtime_tool_phases": [
                {
                    "phase": "bootstrap_topics",
                    "parallel": False,
                    "description": "Create/reuse the controller topic once, then create/reuse persona topics for launchable runs.",
                },
                {
                    "phase": "fan_out_persona_handoffs",
                    "parallel": True,
                    "description": "After topic bootstrap, send visible Telegram kickoff posts and internal persona handoffs in parallel where possible.",
                    "run_count": prepare_result.get("launchable_count", 0),
                },
            ],
        }

        for run in prepare_result["launchable_runs"]:
            result["runtime_tool_loop"].append(
                {
                    "research_run_id": run["research_run_id"],
                    "persona": run["persona"],
                    "step": "telegram_topic_bootstrap_then_sessions_send",
                    "parallel_group": "fan_out_persona_handoffs",
                    "payload_template": run["handoff_payload"],
                    "target": run["target"],
                    "on_success": [
                        "call runtime_execute_dispatch.py --action build-patch with the resolved target_session_key and telegram topic metadata",
                        "apply resulting patch payload via update_research_run.py",
                    ],
                }
            )

        if args.handoff_results_json:
            handoff_results = json.loads(args.handoff_results_json)
            if not isinstance(handoff_results, list):
                raise ValueError("handoff_results_json must decode to an array")

            run_results = []
            patch_steps = []
            for item in handoff_results:
                if not isinstance(item, dict):
                    raise ValueError("each handoff result must be an object")
                research_run_id = item.get("research_run_id")
                persona = item.get("persona")
                status = item.get("status")
                workspace_note_path = item.get("workspace_note_path")
                if not research_run_id or not persona or not status:
                    raise ValueError("each handoff result must include research_run_id, persona, and status")

                if status == "delivered":
                    target_session_key = item.get("target_session_key")
                    if not target_session_key:
                        raise ValueError("delivered handoff result must include target_session_key")
                    patch_payload = python_json(
                        RUNTIME_HELPER,
                        [
                            "--action", "build-patch",
                            "--research-run-id", research_run_id,
                            "--target-session-key", target_session_key,
                            "--delivery-chat-id", item.get("delivery_chat_id") or "",
                            "--delivery-topic-id", item.get("delivery_topic_id") or "",
                            "--delivery-topic-title", item.get("delivery_topic_title") or "",
                            "--controller-topic-id", item.get("controller_topic_id") or "",
                            "--controller-topic-title", item.get("controller_topic_title") or "",
                        ],
                        manifest,
                    )
                    patch_steps.append(
                        {
                            "research_run_id": research_run_id,
                            "persona": persona,
                            "patch_payload": patch_payload,
                            "update_research_run_command": build_update_command(patch_payload, args.db_url),
                        }
                    )

                run_results.append(
                    {
                        "research_run_id": research_run_id,
                        "persona": persona,
                        "status": status,
                        "target_session_key": item.get("target_session_key"),
                        "delivery_chat_id": item.get("delivery_chat_id"),
                        "delivery_topic_id": item.get("delivery_topic_id"),
                        "delivery_topic_title": item.get("delivery_topic_title"),
                        "workspace_note_path": workspace_note_path,
                        "error": item.get("error"),
                    }
                )

            summary = python_json(
                RUNTIME_HELPER,
                [
                    "--action", "finalize-summary",
                    "--run-results-json", json.dumps(run_results, separators=(",", ":")),
                ],
                manifest,
            )
            result["patch_steps"] = patch_steps
            result["summary"] = summary

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
