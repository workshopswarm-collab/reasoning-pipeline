#!/usr/bin/env python3
from __future__ import annotations

"""Prepare the default research swarm dispatch plan for one case.

This script owns the Postgres/control-plane half of dispatch:
- load case + market context
- set market pipeline_status=researching
- create one research_runs row per persona
- build persona-specific prompt
- emit an OpenClaw-runtime dispatch manifest for Telegram topic-routed handoff
- emit the post-handoff DB patch skeleton for each run

The current intended runtime target is a fresh set of Telegram forum topics:
- one controller topic per case
- one fresh persona topic per persona per case

This planner emits logical topic targets. Runtime later creates those topics,
resolves topic session keys, and delivers the kickoff messages.

It does not call runtime tools directly because OpenClaw tools are only
available inside the agent runtime, not from local subprocess Python.

Uses PREDQUANT_ORCHESTRATOR_URL for DB reads/writes.
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
DEFAULT_RUNTIME = "telegram-fresh-topic-session"
DEFAULT_RUNTIME_LABEL = "openclaw-telegram-forum-topic"
DEFAULT_RUNTIME_SURFACE = "telegram-forum-topic"
DEFAULT_MODEL = "openai-codex/gpt-5.4"
DEFAULT_THINKING = "medium"
DEFAULT_PERSONAS = [
    "base-rate",
    "market-implied",
    "variant-view",
    "risk-manager",
    "catalyst-hunter",
]
BASE_DIR = Path(__file__).resolve().parent
PIPELINE_DIR = BASE_DIR.parent.parent
RUNTIME_DIR = PIPELINE_DIR / "runtime"
RUNTIME_SCRIPTS_DIR = RUNTIME_DIR / "scripts"
TELEGRAM_RUNTIME_CONFIG_PATH = RUNTIME_DIR / "telegram-runtime-config.json"

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
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model for spawned researcher sessions")
    parser.add_argument("--thinking", default=DEFAULT_THINKING, help="Thinking level for spawned researcher sessions")
    parser.add_argument("--run-timeout-seconds", type=int, default=0, help="Researcher runtime timeout")
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


def make_dispatch_id(case_key: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"dispatch-{case_key}-{ts}"


def load_telegram_runtime_config() -> dict:
    if not TELEGRAM_RUNTIME_CONFIG_PATH.exists():
        raise FileNotFoundError(f"telegram runtime config not found: {TELEGRAM_RUNTIME_CONFIG_PATH}")
    data = json.loads(TELEGRAM_RUNTIME_CONFIG_PATH.read_text())
    research_group = data.get("research_group") or {}
    templates = research_group.get("topic_title_templates") or {}
    if not research_group.get("chat_id"):
        raise ValueError("telegram runtime config missing research_group.chat_id")
    if not templates.get("controller"):
        raise ValueError("telegram runtime config missing controller topic title template")
    if not templates.get("persona"):
        raise ValueError("telegram runtime config missing persona topic title template")
    configured_personas = set(data.get("personas") or DEFAULT_PERSONAS)
    missing = [persona for persona in DEFAULT_PERSONAS if persona not in configured_personas]
    if missing:
        raise ValueError(f"telegram runtime config missing personas: {', '.join(missing)}")
    return data


def build_topic_title(template: str, *, case_key: str, persona: str | None = None) -> str:
    return template.format(case_key=case_key, persona=persona or "controller")


def build_visible_markers(*, research_run_id: str, persona: str, market_title: str, workspace_note_path: str) -> tuple[str, str]:
    start_marker = f"STARTING RESEARCH | market={market_title} | persona={persona} | research_run_id={research_run_id}"
    finish_marker = f"FINISHED RESEARCH | market={market_title} | persona={persona} | research_run_id={research_run_id} | agent_finding_path={workspace_note_path}"
    return start_marker, finish_marker


def build_topic_handoff_message(*, research_run_id: str, persona: str, case_key: str, topic_title: str, controller_topic_title: str, market_title: str, workspace_note_path: str, prompt_text: str, start_marker: str, finish_marker: str) -> str:
    return "\n".join(
        [
            f"Research run assignment for `{research_run_id}`.",
            "",
            "You are operating in a fresh Telegram persona topic for this run.",
            f"- persona: {persona}",
            f"- case_key: {case_key}",
            f"- market_title: {market_title}",
            f"- persona_topic: {topic_title}",
            f"- controller_topic: {controller_topic_title}",
            f"- research_run_id: {research_run_id}",
            f"- primary_agent_finding_path: {workspace_note_path}",
            "",
            "Treat this message as the canonical assignment for this run.",
            "Treat this topic as self-contained for this run except for the qualitative/quantitative databases and the prompt below.",
            "Use the prompt below as authoritative for the work to perform.",
            "",
            "Required visible topic updates:",
            "1. As soon as you begin, post this exact format as a visible topic message:",
            f"   {start_marker}",
            "2. After your primary agent-finding is written, post this exact format as a visible topic message:",
            f"   {finish_marker}",
            "3. After posting the finished message, update the run to completed using the runtime DB helper (or failed if blocked).",
            "",
            "BEGIN_PROMPT",
            prompt_text,
            "END_PROMPT",
        ]
    )


def main() -> int:
    args = parse_args()
    try:
        case_payload = {"case_id": args.case_id}
        case_ctx = run_sql(args.psql, args.db_url, case_payload, CASE_SQL)

        set_status_script = BASE_DIR / "set_market_pipeline_status.py"
        create_run_script = BASE_DIR / "create_research_run.py"
        update_run_script = RUNTIME_SCRIPTS_DIR / "update_research_run.py"
        build_prompt_script = BASE_DIR / "build_researcher_prompt.py"

        market_state = python_json(
            set_status_script,
            ["--market-id", case_ctx["market_id"], "--pipeline-status", "researching"],
        )

        dispatch_id = make_dispatch_id(case_ctx["case_key"])
        created_at = datetime.now(timezone.utc).isoformat()
        telegram_runtime = load_telegram_runtime_config()
        research_group = telegram_runtime["research_group"]
        controller_topic_title = build_topic_title(
            research_group["topic_title_templates"]["controller"],
            case_key=case_ctx["case_key"],
        )

        runs = []
        for persona in args.personas:
            workspace_note_path = note_path(case_ctx["case_key"], case_ctx.get("slug"), persona)
            source_note_directory = "qualitative-db/40-research/source-notes/by-market"
            source_note_prefix = f"{case_ctx['case_key']}-{persona}"
            assumption_note_path = f"qualitative-db/40-research/assumption-notes/{case_ctx['case_key']}-{persona}-assumptions.md"
            evidence_map_path = f"qualitative-db/40-research/evidence-maps/{case_ctx['case_key']}-{persona}-evidence-map.md"
            persona_topic_title = build_topic_title(
                research_group["topic_title_templates"]["persona"],
                case_key=case_ctx["case_key"],
                persona=persona,
            )

            create_result = python_json(
                create_run_script,
                [
                    "--case-id", case_ctx["case_id"],
                    "--agent-label", persona,
                    "--run-label", f"{persona}-{case_ctx['case_key']}",
                    "--workspace-note-path", workspace_note_path,
                    "--runtime", DEFAULT_RUNTIME_LABEL,
                ],
            )

            prompt_payload = {
                **case_ctx,
                "agent_label": persona,
                "workspace_note_path": workspace_note_path,
                "source_note_dir": source_note_directory,
                "source_note_prefix": source_note_prefix,
                "assumption_note_path": assumption_note_path,
                "evidence_map_path": evidence_map_path,
            }
            prompt_result = python_json(build_prompt_script, ["--pretty"], prompt_payload)
            prompt_text = prompt_result["prompt"]

            start_marker, finish_marker = build_visible_markers(
                research_run_id=create_result["research_run_id"],
                persona=persona,
                market_title=case_ctx["title"],
                workspace_note_path=workspace_note_path,
            )

            handoff_message = build_topic_handoff_message(
                research_run_id=create_result["research_run_id"],
                persona=persona,
                case_key=case_ctx["case_key"],
                topic_title=persona_topic_title,
                controller_topic_title=controller_topic_title,
                market_title=case_ctx["title"],
                workspace_note_path=workspace_note_path,
                prompt_text=prompt_text,
                start_marker=start_marker,
                finish_marker=finish_marker,
            )

            logical_target = {
                "kind": "telegram_forum_topic",
                "chat_id": research_group["chat_id"],
                "topic_title": persona_topic_title,
                "controller_topic_title": controller_topic_title,
                "persona": persona,
            }

            handoff_payload = {
                "chatId": research_group["chat_id"],
                "topicTitle": persona_topic_title,
                "message": handoff_message,
                "timeoutSeconds": 20,
            }

            post_handoff_update_template = {
                "research_run_id": create_result["research_run_id"],
                "status": "running",
                "mark_started": True,
                "workspace_note_path": workspace_note_path,
                "notes": {
                    "delivery_target_chat_id": research_group["chat_id"],
                    "delivery_target_topic_title": persona_topic_title,
                    "controller_chat_id": research_group["chat_id"],
                    "controller_topic_title": controller_topic_title,
                    "dispatch_id": dispatch_id,
                    "dispatch_stage": "persona_topic_running",
                    "runtime_surface": DEFAULT_RUNTIME_SURFACE,
                    "expected_start_marker": start_marker,
                    "expected_finish_marker": finish_marker,
                    "model": args.model,
                    "thinking": args.thinking,
                },
            }

            notes = {
                "delivery_target_chat_id": research_group["chat_id"],
                "delivery_target_topic_title": persona_topic_title,
                "controller_chat_id": research_group["chat_id"],
                "controller_topic_title": controller_topic_title,
                "dispatch_id": dispatch_id,
                "dispatch_stage": "awaiting_topic_creation",
                "runtime_surface": DEFAULT_RUNTIME_SURFACE,
                "expected_start_marker": start_marker,
                "expected_finish_marker": finish_marker,
                "model": args.model,
                "thinking": args.thinking,
            }

            update_result = python_json(
                update_run_script,
                [
                    "--research-run-id", create_result["research_run_id"],
                    "--status", "queued",
                    "--workspace-note-path", workspace_note_path,
                    "--notes-json", json.dumps(notes),
                ],
            )

            runs.append(
                {
                    "research_run_id": create_result["research_run_id"],
                    "persona": persona,
                    "run_label": f"{persona}-{case_ctx['case_key']}",
                    "workspace_note_path": workspace_note_path,
                    "expected_auxiliary_paths": {
                        "source_note_directory": source_note_directory,
                        "source_note_prefix": source_note_prefix,
                        "assumption_note_path": assumption_note_path,
                        "evidence_map_path": evidence_map_path,
                    },
                    "research_run": update_result,
                    "handoff": {
                        "status": "awaiting_topic_creation",
                        "target": logical_target,
                        "handoff_payload": handoff_payload,
                        "post_handoff_update_template": post_handoff_update_template,
                    },
                }
            )

        result = {
            "dispatch_id": dispatch_id,
            "created_at": created_at,
            "planner": {
                "script": "roles/orchestrator/pipeline-launch-procedure/planner/scripts/dispatch_case_research.py",
                "version": None,
            },
            "case": {
                "case_id": case_ctx["case_id"],
                "case_key": case_ctx["case_key"],
                "status": case_ctx["case_status"],
            },
            "market": {
                "market_id": case_ctx["market_id"],
                "platform": case_ctx["platform"],
                "external_market_id": case_ctx["external_market_id"],
                "slug": case_ctx.get("slug"),
                "title": case_ctx["title"],
                "description": case_ctx.get("description"),
                "current_price": case_ctx.get("current_price"),
                "closes_at": case_ctx.get("closes_at"),
                "resolves_at": case_ctx.get("resolves_at"),
            },
            "runtime_defaults": {
                "runtime": DEFAULT_RUNTIME,
                "runtime_label": DEFAULT_RUNTIME_LABEL,
                "runtime_surface": DEFAULT_RUNTIME_SURFACE,
                "chat_id": research_group["chat_id"],
                "controller_topic_title": controller_topic_title,
                "model": args.model,
                "thinking": args.thinking,
            },
            "pipeline_status": market_state["pipeline_status"],
            "dispatch_stage": "awaiting_topic_creation",
            "agent_runtime_dispatch_required": True,
            "agent_runtime_steps": [
                "validate manifest before launch",
                "for each run, check idempotency against current research_runs status and prior telegram topic metadata",
                "create the controller topic once for the dispatch and create one fresh persona topic per queued run",
                "resolve each created topic to a telegram topic session key",
                "for each eligible run, call sessions_send with the run handoff message after injecting the resolved topic session key",
                "after each successful handoff, build a filled DB patch from runs[i].handoff.post_handoff_update_template",
                "patch the corresponding research_runs row using update_research_run.py so status becomes running only after topic creation and persona-topic handoff succeed",
                "if some runs launch and others fail, return delivered_partial and retry only failed queued runs later without creating duplicate topics",
            ],
            "runs": runs,
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
