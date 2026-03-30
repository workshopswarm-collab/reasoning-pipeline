#!/usr/bin/env python3
"""Prepare the default 5-agent research swarm dispatch plan for one case.

This script owns the Postgres/control-plane half of dispatch:
- load case + market context
- set market pipeline_status=researching
- create one research_runs row per persona
- build persona-specific prompt
- emit an OpenClaw-runtime dispatch manifest for sessions_spawn
- emit the post-spawn DB patch template for each run

It does not call sessions_spawn directly because OpenClaw tools are only available
inside the agent runtime, not from local subprocess Python.

Uses PREDQUANT_ORCHESTRATOR_URL for DB reads/writes.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
DEFAULT_RUNTIME = "subagent"
DEFAULT_PERSONAS = [
    "base-rate",
    "market-implied",
    "variant-view",
    "risk-manager",
    "catalyst-hunter",
]
BASE_DIR = Path(__file__).resolve().parent

CASE_SQL = r'''
WITH input AS (
  SELECT (:'payload'::jsonb) AS j
)
SELECT json_build_object(
  'case_id', c.id,
  'case_key', c.case_key,
  'case_status', c.status,
  'market_id', m.id,
  'platform', m.platform,
  'external_market_id', m.external_market_id,
  'slug', m.slug,
  'title', m.title,
  'description', m.description,
  'category', m.category,
  'market_status', m.status,
  'outcome_type', m.outcome_type,
  'closes_at', m.closes_at,
  'resolves_at', m.resolves_at,
  'metadata', m.metadata,
  'pipeline_status', m.pipeline_status,
  'current_price', m.current_price,
  'last_reasoned_price', m.last_reasoned_price
)::text
FROM cases c
JOIN markets m ON m.id = c.market_id
CROSS JOIN input i
WHERE c.id = NULLIF(i.j->>'case_id', '')::uuid
LIMIT 1;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare the full research swarm dispatch plan for one case")
    parser.add_argument("--case-id", required=True, help="Case UUID")
    parser.add_argument("--personas", nargs="*", default=DEFAULT_PERSONAS, help="Persona list")
    parser.add_argument("--model", help="Optional override model for spawned subagents")
    parser.add_argument("--thinking", help="Optional override thinking for spawned subagents")
    parser.add_argument("--run-timeout-seconds", type=int, default=0, help="Subagent run timeout")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON result")
    return parser.parse_args()


def run_sql(psql_bin: str, db_url: str, payload: dict, sql: str) -> dict:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")
    payload_json = json.dumps(payload, separators=(",", ":"))
    proc = subprocess.run(
        [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1", "-v", f"payload={payload_json}", "-f", "-"],
        input=sql,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    if not stdout:
        raise ValueError("query returned no result")
    return json.loads(stdout.splitlines()[-1])


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

    try:
        return json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{script.name} did not return parseable JSON") from exc


def note_path(case_key: str, slug, persona: str) -> str:
    safe_slug = slug or "market"
    return f"qualitative-db/40-research/agent-findings/{persona}/{case_key}-{safe_slug}.md"


def main() -> int:
    args = parse_args()
    try:
        case_payload = {"case_id": args.case_id}
        case_ctx = run_sql(args.psql, args.db_url, case_payload, CASE_SQL)

        set_status_script = BASE_DIR / "set_market_pipeline_status.py"
        create_run_script = BASE_DIR / "create_research_run.py"
        update_run_script = BASE_DIR / "update_research_run.py"
        build_prompt_script = BASE_DIR / "build_researcher_prompt.py"

        market_state = python_json(
            set_status_script,
            ["--market-id", case_ctx["market_id"], "--pipeline-status", "researching"],
        )

        run_results = []
        for persona in args.personas:
            workspace_note_path = note_path(case_ctx["case_key"], case_ctx.get("slug"), persona)

            create_result = python_json(
                create_run_script,
                [
                    "--case-id", case_ctx["case_id"],
                    "--agent-label", persona,
                    "--run-label", f"{persona}-{case_ctx['case_key']}",
                    "--workspace-note-path", workspace_note_path,
                ],
            )

            prompt_payload = {
                **case_ctx,
                "agent_label": persona,
                "workspace_note_path": workspace_note_path,
            }
            prompt_result = python_json(build_prompt_script, ["--pretty"], prompt_payload)
            prompt_text = prompt_result["prompt"]

            spawn_kwargs = {
                "task": prompt_text,
                "label": f"research-{persona}-{case_ctx['case_key']}",
                "runtime": DEFAULT_RUNTIME,
                "mode": "run",
                "cleanup": "keep",
                "runTimeoutSeconds": args.run_timeout_seconds,
            }
            if args.model:
                spawn_kwargs["model"] = args.model
            if args.thinking:
                spawn_kwargs["thinking"] = args.thinking

            # sessions_spawn is not available from local subprocesses. Emit the exact
            # spawn payload plus a post-spawn DB patch template for the OpenClaw runtime.
            spawn_result = {
                "status": "awaiting_agent_runtime_spawn",
                "spawn_payload": spawn_kwargs,
                "post_spawn_update_template": {
                    "research_run_id": create_result["research_run_id"],
                    "status": "running",
                    "workspace_note_path": workspace_note_path,
                    "notes": {
                        "child_session_key": "<fill from sessions_spawn result>",
                        "spawn_run_id": "<fill from sessions_spawn result if available>",
                    },
                },
            }

            notes = {
                "child_session_key": None,
                "spawn_run_id": None,
                "dispatch_stage": "awaiting_agent_runtime_spawn",
            }
            if args.model:
                notes["model"] = args.model
            if args.thinking:
                notes["thinking"] = args.thinking

            update_result = python_json(
                update_run_script,
                [
                    "--research-run-id", create_result["research_run_id"],
                    "--status", "queued",
                    "--workspace-note-path", workspace_note_path,
                    "--notes-json", json.dumps(notes),
                ],
            )

            run_results.append(
                {
                    "persona": persona,
                    "research_run": update_result,
                    "spawn": spawn_result,
                }
            )

        result = {
            "case_id": case_ctx["case_id"],
            "case_key": case_ctx["case_key"],
            "market_id": case_ctx["market_id"],
            "pipeline_status": market_state["pipeline_status"],
            "dispatch_stage": "awaiting_agent_runtime_spawn",
            "agent_runtime_dispatch_required": True,
            "agent_runtime_steps": [
                "for each run, call sessions_spawn with runs[i].spawn.spawn_payload",
                "capture the returned child session metadata from sessions_spawn",
                "patch the corresponding research_runs row using runs[i].spawn.post_spawn_update_template",
                "set notes.child_session_key and notes.spawn_run_id from the actual spawn result when available",
            ],
            "runs": run_results,
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
