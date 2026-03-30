#!/usr/bin/env python3
"""Prepare a headless TUI -> Discord fixed-channel dispatch handoff bundle.

This wrapper does the planner/control-plane work locally and emits a reusable
bundle that a TUI-side OpenClaw session can execute with `sessions_send` into
fixed Discord persona channels.

Supported modes:
1. Prepare from an existing manifest (`--manifest-path`)
2. Prepare from an existing case (`--case-id`)
3. Select next market -> open case -> emit manifest (default when no case/manifest is supplied)
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
BASE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = BASE_DIR.parent
PIPELINE_DIR = RUNTIME_DIR.parent
PLANNER_SCRIPTS_DIR = PIPELINE_DIR / "planner" / "scripts"
DEFAULT_MANIFEST_DIR = RUNTIME_DIR / "dispatch-manifests"
DEFAULT_MODEL = "openai-codex/gpt-5.4"
DEFAULT_THINKING = "medium"
DEFAULT_PERSONAS = [
    "base-rate",
    "market-implied",
    "variant-view",
    "risk-manager",
    "catalyst-hunter",
]

SELECT_NEXT_MARKET = PLANNER_SCRIPTS_DIR / "select_next_market.py"
OPEN_CASE = PLANNER_SCRIPTS_DIR / "open_case.py"
DISPATCH_CASE_RESEARCH = PLANNER_SCRIPTS_DIR / "dispatch_case_research.py"
RUN_DISPATCH_RUNTIME = BASE_DIR / "run_dispatch_runtime.py"
LOAD_DISPATCH_EXISTING_STATE = BASE_DIR / "load_dispatch_existing_state.py"
FINALIZE_DISPATCH_AFTER_SWARM = BASE_DIR / "finalize_dispatch_after_swarm.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare a headless TUI -> Discord fixed-channel dispatch bundle")
    parser.add_argument("--manifest-path", help="Use an existing dispatch manifest path instead of preparing a new one")
    parser.add_argument("--case-id", help="Existing case UUID to dispatch")
    parser.add_argument("--market-id", help="Existing market UUID to open/fetch case for")
    parser.add_argument("--personas", nargs="*", default=DEFAULT_PERSONAS, help="Persona list when preparing a new dispatch")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model hint recorded in run metadata")
    parser.add_argument("--thinking", default=DEFAULT_THINKING, help="Thinking hint recorded in run metadata")
    parser.add_argument("--run-timeout-seconds", type=int, default=0, help="Retained for compatibility; not used by fixed channels")
    parser.add_argument("--manifest-dir", default=str(DEFAULT_MANIFEST_DIR), help="Directory where prepared manifests should be written")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def python_json(script: Path, args: list[str], stdin_payload: dict[str, Any] | None = None) -> dict[str, Any]:
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

    try:
        return json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{script.name} did not return parseable JSON") from exc


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def persist_manifest(manifest_dir: Path, manifest: dict[str, Any]) -> Path:
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = manifest_dir / f"{manifest['dispatch_id']}.json"
    write_json(manifest_path, manifest)
    return manifest_path


def prepare_manifest(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, Any], Path, dict[str, Any] | None]:
    selection = None
    manifest_dir = Path(args.manifest_dir).expanduser().resolve()
    if args.manifest_path:
        source_manifest_path = Path(args.manifest_path).expanduser().resolve()
        if not source_manifest_path.exists():
            raise FileNotFoundError(f"manifest not found: {source_manifest_path}")
        manifest = load_json(source_manifest_path)
        manifest_path = persist_manifest(manifest_dir, manifest)
    else:
        if args.case_id:
            case = {"case_id": args.case_id}
        else:
            if args.market_id:
                selection = {"market_id": args.market_id}
            else:
                selection = python_json(SELECT_NEXT_MARKET, ["--db-url", args.db_url, "--psql", args.psql])
            case = python_json(
                OPEN_CASE,
                ["--db-url", args.db_url, "--psql", args.psql, "--market-id", selection["market_id"]],
            )

        manifest = python_json(
            DISPATCH_CASE_RESEARCH,
            [
                "--case-id", case["case_id"],
                "--db-url", args.db_url,
                "--psql", args.psql,
                "--model", args.model,
                "--thinking", args.thinking,
                "--run-timeout-seconds", str(args.run_timeout_seconds),
                *( ["--personas", *args.personas] if args.personas else []),
            ],
        )
        manifest_path = persist_manifest(manifest_dir, manifest)

    existing_map = python_json(LOAD_DISPATCH_EXISTING_STATE, ["--file", str(manifest_path), "--db-url", args.db_url])
    prepare_preview = python_json(
        RUN_DISPATCH_RUNTIME,
        [
            "--file", str(manifest_path),
            "--db-url", args.db_url,
            "--existing-map-json", json.dumps(existing_map, separators=(",", ":")),
        ],
    )
    return manifest, prepare_preview, manifest_path, selection


def build_next_tool_steps(prepare_result: dict) -> list[dict[str, Any]]:
    steps = []
    for run in prepare_result.get("launchable_runs", []):
        payload = dict(run["handoff_payload"])
        payload.setdefault("timeoutSeconds", 20)
        steps.append(
            {
                "research_run_id": run["research_run_id"],
                "persona": run["persona"],
                "channel_name": run["target"]["channel_name"],
                "channel_id": run["target"]["channel_id"],
                "tool": "sessions_send",
                **payload,
            }
        )
    return steps


def main() -> int:
    args = parse_args()
    try:
        if not args.db_url:
            raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")

        manifest, runtime_preview, manifest_path, selection = prepare_manifest(args)
        next_tool_steps = build_next_tool_steps(runtime_preview["prepare"])

        result = {
            "status": "ready_for_fixed_channel_handoff",
            "selection": selection,
            "case": manifest["case"],
            "market": {
                "market_id": manifest["market"]["market_id"],
                "title": manifest["market"]["title"],
                "slug": manifest["market"].get("slug"),
                "current_price": manifest["market"].get("current_price"),
                "closes_at": manifest["market"].get("closes_at"),
                "resolves_at": manifest["market"].get("resolves_at"),
            },
            "dispatch": {
                "dispatch_id": manifest["dispatch_id"],
                "manifest_path": str(manifest_path),
                "dispatch_stage": manifest.get("dispatch_stage"),
                "runtime_surface": manifest.get("runtime_defaults", {}).get("runtime_surface"),
                "run_count": len(manifest.get("runs", [])),
                "launchable_count": runtime_preview["prepare"]["launchable_count"],
                "personas": [run["persona"] for run in manifest.get("runs", [])],
            },
            "runtime_preview": {
                "validation": runtime_preview["validation"],
                "prepare": {
                    "status": runtime_preview["prepare"]["status"],
                    "launchable_count": runtime_preview["prepare"]["launchable_count"],
                    "skipped_count": runtime_preview["prepare"]["skipped_count"],
                },
            },
            "next_tool_steps": next_tool_steps,
            "manual_finalize_backstop_step": {
                "tool": "exec",
                "description": "Optional repair step if automatic terminal finalization is missed or you want an explicit post-run audit",
                "command": f"set -a; source /Users/agent2/.openclaw/workspace/.env; set +a; python3 {FINALIZE_DISPATCH_AFTER_SWARM} --file {manifest_path} --apply --pretty"
            }
        }
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
