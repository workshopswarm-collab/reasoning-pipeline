#!/usr/bin/env python3
"""Run the realtime runtime-side orchestration sequence for a dispatch manifest.

This script is the runtime wrapper around the existing pipeline scripts. It is
still intentionally split from actual OpenClaw tool execution:
- Python can prepare/normalize the orchestration sequence
- OpenClaw runtime must perform sessions_spawn
- Python can then build DB patches and finalize summary

The wrapper supports two operational modes:
1. plan-only: emit the exact sequence the OpenClaw runtime should execute
2. replay-results: finalize DB patch steps + dispatch summary from actual spawn results

This keeps the control plane explicit while fitting the current pipeline.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUNTIME_HELPER = BASE_DIR / "runtime_execute_dispatch.py"
UPDATE_RUN = BASE_DIR / "update_research_run.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Realtime runtime-side orchestration wrapper")
    parser.add_argument("--file", default="-", help="Path to dispatch manifest JSON, or - for stdin")
    parser.add_argument(
        "--existing-map-json",
        help="JSON object keyed by research_run_id with existing runtime state for idempotency",
    )
    parser.add_argument(
        "--spawn-results-json",
        help=(
            "JSON array of actual runtime spawn results keyed by research_run_id, "
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
    if db_url:
        cmd.extend(["--db-url", db_url])
    return cmd


def main() -> int:
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
        }

        for run in prepare_result["launchable_runs"]:
            result["runtime_tool_loop"].append(
                {
                    "research_run_id": run["research_run_id"],
                    "persona": run["persona"],
                    "step": "sessions_spawn",
                    "payload": run["spawn_payload"],
                    "on_success": [
                        "call runtime_execute_dispatch.py --action build-patch with returned child_session_key and spawn_run_id",
                        "apply resulting patch payload via update_research_run.py",
                    ],
                }
            )

        if args.spawn_results_json:
            spawn_results = json.loads(args.spawn_results_json)
            if not isinstance(spawn_results, list):
                raise ValueError("spawn_results_json must decode to an array")

            run_results = []
            patch_steps = []
            for item in spawn_results:
                if not isinstance(item, dict):
                    raise ValueError("each spawn result must be an object")
                research_run_id = item.get("research_run_id")
                persona = item.get("persona")
                status = item.get("status")
                workspace_note_path = item.get("workspace_note_path")
                if not research_run_id or not persona or not status:
                    raise ValueError("each spawn result must include research_run_id, persona, and status")

                if status == "launched":
                    child_session_key = item.get("child_session_key")
                    if not child_session_key:
                        raise ValueError("launched spawn result must include child_session_key")
                    patch_payload = python_json(
                        RUNTIME_HELPER,
                        [
                            "--action", "build-patch",
                            "--research-run-id", research_run_id,
                            "--child-session-key", child_session_key,
                            "--spawn-run-id", item.get("spawn_run_id") or "",
                            "--model", item.get("model") or manifest.get("runtime_defaults", {}).get("model") or "",
                            "--thinking", item.get("thinking") or manifest.get("runtime_defaults", {}).get("thinking") or "",
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
                        "child_session_key": item.get("child_session_key"),
                        "spawn_run_id": item.get("spawn_run_id"),
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
