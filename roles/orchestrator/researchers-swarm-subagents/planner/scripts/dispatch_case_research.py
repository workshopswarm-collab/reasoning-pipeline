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

The current intended runtime target is a persistent set of Telegram forum topics:
- one controller topic per case
- one persona topic per persona per case
- reruns should reuse those case/persona lanes whenever prior lane metadata exists

This planner emits logical topic targets. Runtime later reuses or creates those topics,
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
DEFAULT_RUNTIME = "telegram-persistent-topic-session"
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
WORKSPACE_ROOT = BASE_DIR.parents[4]

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

CASE_RUN_STATE_SQL = r'''
WITH input AS (
  SELECT (:'payload'::jsonb) AS j
),
target_case AS (
  SELECT
    c.id,
    COALESCE(c.orchestration_notes->>'active_dispatch_id', '') AS active_dispatch_id
  FROM cases c
  CROSS JOIN input i
  WHERE c.id = NULLIF(i.j->>'case_id', '')::uuid
  LIMIT 1
)
SELECT json_build_object(
  'case_id', tc.id,
  'active_dispatch_id', NULLIF(tc.active_dispatch_id, ''),
  'runs', COALESCE((
    SELECT json_agg(json_build_object(
      'research_run_id', rr.id,
      'agent_label', rr.agent_label,
      'status', rr.status,
      'created_at', rr.created_at,
      'started_at', rr.started_at,
      'completed_at', rr.completed_at,
      'workspace_note_path', rr.workspace_note_path,
      'notes', COALESCE(rr.notes, '{}'::jsonb)
    ) ORDER BY rr.created_at DESC, rr.id DESC)
    FROM research_runs rr
    WHERE rr.case_id = tc.id
  ), '[]'::json)
)::text
FROM target_case tc;
'''

SUPERSEDE_STALE_QUEUED_SQL = r'''
WITH input AS (
  SELECT (:'payload'::jsonb) AS j
),
updated AS (
  UPDATE research_runs rr
  SET
    status = 'superseded',
    notes = COALESCE(rr.notes, '{}'::jsonb) || jsonb_build_object(
      'dispatch_stage', 'superseded_before_rerun',
      'superseded_at', NOW(),
      'superseded_by_dispatch_id', NULLIF(i.j->>'dispatch_id', ''),
      'superseded_reason', 'new_dispatch_preflight',
      'superseded_from_status', rr.status
    )
  FROM input i
  WHERE rr.case_id = NULLIF(i.j->>'case_id', '')::uuid
    AND rr.status = 'queued'
  RETURNING rr.id, rr.agent_label, rr.status
)
SELECT json_build_object(
  'superseded_count', COUNT(*),
  'research_run_ids', COALESCE(json_agg(id), '[]'::json),
  'agent_labels', COALESCE(json_agg(agent_label), '[]'::json)
)::text
FROM updated;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare the full research swarm dispatch plan for one case")
    parser.add_argument("--case-id", required=True, help="Case UUID")
    parser.add_argument("--personas", nargs="*", default=DEFAULT_PERSONAS, help="Persona list")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model for spawned researcher sessions")
    parser.add_argument("--thinking", default=DEFAULT_THINKING, help="Thinking level for spawned researcher sessions")
    parser.add_argument("--run-timeout-seconds", type=int, default=0, help="Researcher runtime timeout")
    parser.add_argument("--allow-closed-case-rerun", action="store_true", help="Permit dispatch preparation against a closed historical case")
    parser.add_argument("--dry-run", action="store_true", help="Compute the dispatch/rerun plan without writing DB state or creating attempt rows")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--refresh-mode", default="", help="Optional explicit refresh mode metadata")
    parser.add_argument("--refresh-reasons", default="", help="Optional comma-separated explicit refresh reasons")
    parser.add_argument("--refresh-price-delta-pct-points", default="", help="Optional explicit refresh price delta in percentage points")
    parser.add_argument("--refresh-detected-marker", default="", help="Optional explicit controller-lane material-change marker")
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
            parsed = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return parsed

    try:
        parsed = json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{script.name} did not return parseable JSON") from exc
    if not isinstance(parsed, dict):
        raise RuntimeError(f"{script.name} returned JSON but not an object")
    return parsed


def analysis_date(created_at: str) -> str:
    return created_at[:10]


def case_root(case_key: str) -> Path:
    return Path("qualitative-db/40-research/cases") / case_key


def analysis_root(case_key: str, created_at: str, dispatch_id: str) -> Path:
    return case_root(case_key) / "researcher-analyses" / analysis_date(created_at) / dispatch_id


def note_path(case_key: str, created_at: str, dispatch_id: str, persona: str) -> str:
    return str(analysis_root(case_key, created_at, dispatch_id) / "personas" / f"{persona}.md")


def sidecar_path(case_key: str, created_at: str, dispatch_id: str, persona: str) -> str:
    return str(analysis_root(case_key, created_at, dispatch_id) / "personas" / f"{persona}.sidecar.json")


def summary_path(case_key: str, created_at: str, dispatch_id: str) -> str:
    return str(analysis_root(case_key, created_at, dispatch_id) / "summary.md")


def assumption_note_path(case_key: str, created_at: str, dispatch_id: str, persona: str) -> str:
    return str(analysis_root(case_key, created_at, dispatch_id) / "assumptions" / f"{persona}.md")


def evidence_map_path(case_key: str, created_at: str, dispatch_id: str, persona: str) -> str:
    return str(analysis_root(case_key, created_at, dispatch_id) / "evidence" / f"{persona}.md")


def source_note_directory(case_key: str) -> str:
    return str(case_root(case_key) / "researcher-source-notes")


def source_note_prefix(created_at: str, persona: str) -> str:
    return f"{analysis_date(created_at)}-{persona}"


def case_file_path(case_key: str) -> str:
    return str(case_root(case_key) / "case.md")


def current_file_path(case_key: str) -> str:
    return str(case_root(case_key) / "researcher-swarm-current.md")


def timeline_file_path(case_key: str) -> str:
    return str(case_root(case_key) / "timeline.md")


def render_case_md(case_ctx: dict) -> str:
    lines = [
        "---",
        "type: research_case",
        f"case_key: {case_ctx.get('case_key')}",
        f"case_id: {case_ctx.get('case_id')}",
        f"market_id: {case_ctx.get('market_id')}",
        f"platform: {case_ctx.get('platform')}",
        f"external_market_id: {case_ctx.get('external_market_id')}",
        f"slug: {case_ctx.get('slug')}",
        "status: active",
        "generated_by: orchestrator",
        "---",
        "",
        f"# {case_ctx.get('title')}",
        "",
        "## Case identity",
        f"- case_key: `{case_ctx.get('case_key')}`",
        f"- case_id: `{case_ctx.get('case_id')}`",
        f"- market_id: `{case_ctx.get('market_id')}`",
        f"- platform: `{case_ctx.get('platform')}`",
        f"- external_market_id: `{case_ctx.get('external_market_id')}`",
        f"- slug: `{case_ctx.get('slug')}`",
        "",
        "## Market context",
        f"- current_price: `{case_ctx.get('current_price')}`",
        f"- closes_at: `{case_ctx.get('closes_at')}`",
        f"- resolves_at: `{case_ctx.get('resolves_at')}`",
        "",
        "## Description",
        case_ctx.get('description') or "",
        "",
        "## Case surfaces",
        "- `researcher-swarm-current.md` = latest/current researcher swarm pointers",
        "- `timeline.md` = programmatic lifecycle summary",
        "- `researcher-source-notes/` = case-level source provenance across researcher analyses",
        "- `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` = append-only researcher analysis generations",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def render_current_md(case_ctx: dict, *, created_at: str, dispatch_id: str, summary_note_path: str, persona_paths: dict[str, str], difficulty_profile: dict) -> str:
    lines = [
        "---",
        "type: researcher_swarm_current",
        f"case_key: {case_ctx.get('case_key')}",
        f"dispatch_id: {dispatch_id}",
        f"analysis_date: {analysis_date(created_at)}",
        f"updated_at: {created_at}",
        "generated_by: orchestrator",
        "---",
        "",
        f"# Researcher swarm current — {case_ctx.get('case_key')}",
        "",
        f"- latest_dispatch_id: `{dispatch_id}`",
        f"- latest_analysis_date: `{analysis_date(created_at)}`",
        f"- latest_summary: `{summary_note_path}`",
        f"- current_price: `{case_ctx.get('current_price')}`",
        f"- difficulty_class: `{difficulty_profile.get('difficulty_class')}`",
        f"- resolution_risk: `{difficulty_profile.get('resolution_risk')}`",
        "",
        "## Latest persona findings",
    ]
    for persona, path in persona_paths.items():
        lines.append(f"- `{persona}` -> `{path}`")
    lines.extend([
        "",
        "## Notes",
        "- This file is a generated latest-view surface for the researcher swarm state for this case.",
        "- Canonical per-analysis history lives under `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...`.",
        "",
    ])
    return "\n".join(lines).rstrip() + "\n"


def update_timeline_md(path: Path, *, created_at: str, dispatch_id: str, case_key: str, summary_note_path: str, dry_run: bool) -> None:
    header = "---\ntype: research_case_timeline\ncase_key: {case_key}\ngenerated_by: orchestrator\n---\n\n# Timeline\n\n".format(case_key=case_key)
    entry = f"- {created_at} — prepared analysis `{dispatch_id}` with summary `{summary_note_path}`.\n"
    if dry_run:
        return
    if path.exists():
        text = path.read_text()
        if dispatch_id in text:
            return
        path.write_text(text.rstrip() + "\n" + entry)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(header + entry)


def render_summary_md(case_ctx: dict, *, created_at: str, dispatch_id: str, persona_paths: dict[str, str], assumption_paths: dict[str, str], evidence_paths: dict[str, str], difficulty_profile: dict) -> str:
    lines = [
        "---",
        "type: research_analysis_summary",
        f"case_key: {case_ctx.get('case_key')}",
        f"dispatch_id: {dispatch_id}",
        f"analysis_date: {analysis_date(created_at)}",
        f"generated_at: {created_at}",
        "generated_by: orchestrator",
        "---",
        "",
        f"# Analysis summary — {dispatch_id}",
        "",
        "## Analysis context",
        f"- case_key: `{case_ctx.get('case_key')}`",
        f"- title: {case_ctx.get('title')}",
        f"- current_price_at_dispatch: `{case_ctx.get('current_price')}`",
        f"- difficulty_class: `{difficulty_profile.get('difficulty_class')}`",
        f"- resolution_risk: `{difficulty_profile.get('resolution_risk')}`",
        f"- evidence_floor: `{difficulty_profile.get('evidence_floor')}`",
        "",
        "## Persona findings",
    ]
    for persona, path in persona_paths.items():
        lines.append(f"- `{persona}` -> `{path}`")
    lines.extend([
        "",
        "## Supporting artifacts",
    ])
    for persona, path in assumption_paths.items():
        lines.append(f"- assumption `{persona}` -> `{path}`")
    for persona, path in evidence_paths.items():
        lines.append(f"- evidence `{persona}` -> `{path}`")
    lines.extend([
        "",
        "## Notes",
        "- This summary is generated at dispatch-preparation time and can later be enriched by Orchestrator-side consolidation or review workflows.",
        "",
    ])
    return "\n".join(lines).rstrip() + "\n"


def write_case_analysis_scaffolds(case_ctx: dict, *, created_at: str, dispatch_id: str, persona_paths: dict[str, str], assumption_paths: dict[str, str], evidence_paths: dict[str, str], difficulty_profile: dict, dry_run: bool) -> dict:
    case_dir = case_root(case_ctx['case_key'])
    analysis_dir = analysis_root(case_ctx['case_key'], created_at, dispatch_id)
    summary_note_path = summary_path(case_ctx['case_key'], created_at, dispatch_id)
    scaffolds = {
        'case_root': str(case_dir),
        'analysis_root': str(analysis_dir),
        'case_md': case_file_path(case_ctx['case_key']),
        'current_md': current_file_path(case_ctx['case_key']),
        'timeline_md': timeline_file_path(case_ctx['case_key']),
        'summary_md': summary_note_path,
        'qmd_bundle_json': str(analysis_dir / 'qmd-bundle.json'),
    }
    if dry_run:
        scaffolds['status'] = 'dry_run'
        return scaffolds

    case_dir.mkdir(parents=True, exist_ok=True)
    analysis_dir.mkdir(parents=True, exist_ok=True)
    (analysis_dir / 'personas').mkdir(parents=True, exist_ok=True)
    (analysis_dir / 'assumptions').mkdir(parents=True, exist_ok=True)
    (analysis_dir / 'evidence').mkdir(parents=True, exist_ok=True)
    (case_dir / 'researcher-source-notes').mkdir(parents=True, exist_ok=True)

    case_md_path = case_dir / 'case.md'
    if not case_md_path.exists():
        case_md_path.write_text(render_case_md(case_ctx))

    researcher_swarm_current_path = case_dir / 'researcher-swarm-current.md'
    researcher_swarm_current_path.write_text(
        render_current_md(
            case_ctx,
            created_at=created_at,
            dispatch_id=dispatch_id,
            summary_note_path=summary_note_path,
            persona_paths=persona_paths,
            difficulty_profile=difficulty_profile,
        )
    )
    update_timeline_md(case_dir / 'timeline.md', created_at=created_at, dispatch_id=dispatch_id, case_key=case_ctx['case_key'], summary_note_path=summary_note_path, dry_run=dry_run)
    (analysis_dir / 'summary.md').write_text(
        render_summary_md(
            case_ctx,
            created_at=created_at,
            dispatch_id=dispatch_id,
            persona_paths=persona_paths,
            assumption_paths=assumption_paths,
            evidence_paths=evidence_paths,
            difficulty_profile=difficulty_profile,
        )
    )

    scaffolds['compatibility_results'] = {'status': 'disabled'}
    scaffolds['status'] = 'written'
    return scaffolds


def make_dispatch_id(case_key: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"dispatch-{case_key}-{ts}"


def make_dry_run_research_run_id(case_key: str, persona: str) -> str:
    return f"dryrun-{case_key}-{persona}"


def build_lane_fingerprint(case_ctx: dict) -> dict:
    return {
        "case_id": case_ctx.get("case_id"),
        "market_id": case_ctx.get("market_id"),
        "platform": case_ctx.get("platform"),
        "external_market_id": case_ctx.get("external_market_id"),
        "outcome_type": case_ctx.get("outcome_type"),
    }


def latest_lane_seed(existing_runs: list[dict], persona: str) -> dict:
    for row in existing_runs:
        if row.get("agent_label") != persona:
            continue
        notes = row.get("notes") or {}
        if any(
            notes.get(key)
            for key in [
                "delivery_target_topic_id",
                "delivery_target_session_key",
                "controller_topic_id",
            ]
        ):
            return {
                "source_research_run_id": row.get("research_run_id"),
                "source_dispatch_id": notes.get("dispatch_id"),
                "delivery_target_chat_id": notes.get("delivery_target_chat_id"),
                "delivery_target_topic_id": notes.get("delivery_target_topic_id"),
                "delivery_target_session_key": notes.get("delivery_target_session_key"),
                "delivery_target_topic_title": notes.get("delivery_target_topic_title"),
                "controller_chat_id": notes.get("controller_chat_id"),
                "controller_topic_id": notes.get("controller_topic_id"),
                "controller_topic_title": notes.get("controller_topic_title"),
                "lane_fingerprint": notes.get("lane_fingerprint") or {},
            }
    return {}


def lane_fingerprint_mismatch(case_ctx: dict, lane_seed: dict) -> dict:
    expected = build_lane_fingerprint(case_ctx)
    actual = lane_seed.get("lane_fingerprint") or {}
    if not actual:
        return {"mismatch": True, "missing_fingerprint": True, "expected": expected, "actual": actual, "fields": ["lane_fingerprint"]}
    fields = [key for key, value in expected.items() if actual.get(key) != value]
    return {"mismatch": bool(fields), "missing_fingerprint": False, "expected": expected, "actual": actual, "fields": fields}


def active_running_conflicts(existing_runs: list[dict]) -> list[dict]:
    return [row for row in existing_runs if row.get("status") == "running"]


def queued_stale_runs(existing_runs: list[dict]) -> list[dict]:
    return [row for row in existing_runs if row.get("status") == "queued"]


def collect_rerun_metadata(*, case_id: str, market_id: str, existing_runs: list[dict], active_dispatch_id: str | None = None) -> dict:
    prior_dispatches = []
    seen = set()
    for row in existing_runs:
        notes = row.get("notes") or {}
        dispatch = notes.get("dispatch_id")
        if dispatch and dispatch not in seen:
            seen.add(dispatch)
            prior_dispatches.append(dispatch)
    run_kind = "rerun" if prior_dispatches else "novel"
    rerun_scope = "same_case" if run_kind == "rerun" else None
    return {
        "run_kind": run_kind,
        "rerun_scope": rerun_scope,
        "prior_dispatch_count": len(prior_dispatches),
        "prior_case_count": 0,
        "prior_dispatch_ids": prior_dispatches,
        "active_dispatch_id_before_prepare": active_dispatch_id or None,
    }


def generate_qmd_bundle(*, args: argparse.Namespace, case_ctx: dict, difficulty_profile: dict, rerun_context: dict) -> dict:
    script = BASE_DIR / "generate_qmd_bundle.py"
    fallback = {
        "status": "not_run",
        "qmd_used": False,
        "qmd_tier": "tier0",
        "query_profile": {
            "run_kind": rerun_context.get("run_kind"),
            "rerun_scope": rerun_context.get("rerun_scope"),
            "prior_dispatch_count": rerun_context.get("prior_dispatch_count", 0),
            "prior_case_count": rerun_context.get("prior_case_count", 0),
            "difficulty_class": difficulty_profile.get("difficulty_class"),
            "source_of_truth_class": difficulty_profile.get("source_of_truth_class"),
            "suppress_same_case": True,
            "suppress_same_market": rerun_context.get("run_kind") == "rerun" or rerun_context.get("prior_dispatch_count", 0) > 0 or rerun_context.get("prior_case_count", 0) > 0,
        },
        "results": {"similar_cases": [], "entity_notes": [], "driver_notes": []},
        "result_paths": [],
    }
    if not script.exists():
        fallback["status"] = "generator_missing"
        return fallback
    try:
        bundle = python_json(
            script,
            [
                "--pretty",
                "--case-key", case_ctx["case_key"],
                "--market-id", case_ctx["market_id"],
                "--title", case_ctx["title"],
                "--description", case_ctx.get("description") or "",
                "--category", case_ctx.get("category") or "",
                "--platform", case_ctx.get("platform") or "",
                "--run-kind", rerun_context.get("run_kind") or "novel",
                "--rerun-scope", rerun_context.get("rerun_scope") or "",
                "--prior-dispatch-count", str(rerun_context.get("prior_dispatch_count", 0)),
                "--prior-case-count", str(rerun_context.get("prior_case_count", 0)),
                "--difficulty-class", difficulty_profile.get("difficulty_class") or "",
                "--source-of-truth-class", difficulty_profile.get("source_of_truth_class") or "",
                "--focus-hints-json", json.dumps(difficulty_profile.get("focus_hints") or []),
                "--db-url", args.db_url,
                "--psql", args.psql,
            ],
        )
    except Exception as exc:  # noqa: BLE001
        fallback["status"] = "generator_error"
        fallback["error"] = str(exc)
        return fallback
    if not isinstance(bundle, dict):
        fallback["status"] = "generator_invalid"
        return fallback
    bundle.setdefault("status", "ok")
    bundle.setdefault("results", {"similar_cases": [], "entity_notes": [], "driver_notes": []})
    bundle.setdefault("result_paths", [])
    return bundle


def write_qmd_bundle(path_str: str, bundle: dict, *, dry_run: bool) -> dict:
    if dry_run:
        return {"status": "dry_run", "path": path_str}
    path = Path(path_str)
    if not path.is_absolute():
        path = (WORKSPACE_ROOT / path_str).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(bundle, indent=2, sort_keys=True))
    return {"status": "written", "path": str(path.relative_to(WORKSPACE_ROOT))}


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


def is_refresh_dispatch_mode(value: str) -> bool:
    return str(value or '').strip().lower() in {'refresh', 'full_refresh', 'full'}


def build_refresh_controller_markers(*, case_key: str, market_title: str, dispatch_id: str, refresh_mode: str, refresh_reasons: list[str] | None = None) -> tuple[str, str]:
    normalized_mode = str(refresh_mode or '').strip().lower()
    if not is_refresh_dispatch_mode(normalized_mode):
        return '', ''
    reasons = ','.join(str(item) for item in (refresh_reasons or []) if str(item).strip())
    start_marker = f"STARTING FULL REFRESH | case={case_key} | market={market_title} | dispatch_id={dispatch_id} | refresh_mode={normalized_mode} | reasons={reasons}"
    finish_marker = f"FINISHED FULL REFRESH SWARM | case={case_key} | dispatch_id={dispatch_id} | next_stage=synthesis"
    return start_marker, finish_marker


def build_topic_handoff_message(*, research_run_id: str, persona: str, case_key: str, topic_title: str, controller_topic_title: str, market_title: str, workspace_note_path: str, reasoning_sidecar_path: str, prompt_text: str, start_marker: str, finish_marker: str) -> str:
    completion_cmd = (
        "python3 roles/orchestrator/researchers-swarm-subagents/runtime/scripts/"
        f"reconcile_research_run_completion.py --research-run-id {research_run_id} --status completed"
    )
    failure_cmd = (
        "python3 roles/orchestrator/researchers-swarm-subagents/runtime/scripts/"
        f"reconcile_research_run_completion.py --research-run-id {research_run_id} --status failed --error "
        '"<brief reason>"'
    )
    return "\n".join(
        [
            f"Research run assignment for `{research_run_id}`.",
            f"- persona: {persona}",
            f"- case_key: {case_key}",
            f"- market_title: {market_title}",
            f"- persona_topic: {topic_title}",
            f"- controller_topic: {controller_topic_title}",
            f"- primary_agent_finding_path: {workspace_note_path}",
            f"- reasoning_sidecar_path: {reasoning_sidecar_path}",
            "",
            "Use this topic as the self-contained runtime workspace for this run.",
            "Do not branch into unrelated old case artifacts or extra non-material research once you can defend a directional view.",
            "Apply the materiality stop rule from the prompt below and finish decisively when it is met.",
            "",
            "Visible topic updates:",
            f"- runtime posts kickoff automatically: {start_marker}",
            "- you may post sparse progress updates only at meaningful milestones or roughly once every 10 minutes max while still active",
            f"- runtime posts the completion marker automatically after successful completion: {finish_marker}",
            "",
            "Terminal state helper (run this via the exec tool from the workspace root):",
            f"- on success: `{completion_cmd}`",
            f"- if blocked/failed: `{failure_cmd}`",
            "- the helper auto-updates research_runs, stamps completed_at for successful completion, and posts the visible FINISHED marker from stored delivery metadata",
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
        classify_difficulty_script = BASE_DIR / "classify_research_difficulty.py"
        update_case_notes_script = BASE_DIR / "update_case_orchestration_notes.py"

        if case_ctx.get("case_status") == "closed" and not args.allow_closed_case_rerun:
            raise ValueError("case is closed; refusing rerun unless --allow-closed-case-rerun is set")

        difficulty_result = python_json(classify_difficulty_script, ["--pretty", "--mode", "hybrid"], case_ctx)
        difficulty_profile = difficulty_result.get("difficulty_profile") or {}
        heuristic_summary = difficulty_result.get("heuristic_summary") or {}
        model_summary = difficulty_result.get("model_summary") or {}
        created_at = datetime.now(timezone.utc).isoformat()
        dispatch_id = make_dispatch_id(case_ctx["case_key"])

        case_run_state = run_sql(args.psql, args.db_url, {"case_id": case_ctx["case_id"]}, CASE_RUN_STATE_SQL)
        existing_runs = case_run_state.get("runs") or []
        running_conflicts = active_running_conflicts(existing_runs)
        if running_conflicts:
            conflict_dispatches = sorted({
                (row.get("notes") or {}).get("dispatch_id")
                for row in running_conflicts
                if (row.get("notes") or {}).get("dispatch_id")
            })
            raise ValueError(
                "case already has running research runs; rerun blocked until the active swarm is reconciled"
                + (f" (dispatches: {', '.join(conflict_dispatches)})" if conflict_dispatches else "")
            )

        superseded_runs = {}
        stale_queued = queued_stale_runs(existing_runs)
        if stale_queued:
            if args.dry_run:
                superseded_runs = {
                    "status": "dry_run",
                    "superseded_count": len(stale_queued),
                    "research_run_ids": [row.get("research_run_id") for row in stale_queued],
                    "agent_labels": [row.get("agent_label") for row in stale_queued],
                    "would_supersede_by_dispatch_id": dispatch_id,
                }
            else:
                superseded_runs = run_sql(
                    args.psql,
                    args.db_url,
                    {"case_id": case_ctx["case_id"], "dispatch_id": dispatch_id},
                    SUPERSEDE_STALE_QUEUED_SQL,
                )
                existing_runs = [row for row in existing_runs if row.get("status") != "queued"]

        rerun_context = collect_rerun_metadata(
            case_id=case_ctx["case_id"],
            market_id=case_ctx["market_id"],
            existing_runs=existing_runs,
            active_dispatch_id=case_run_state.get("active_dispatch_id"),
        )

        lane_fingerprint = build_lane_fingerprint(case_ctx)

        difficulty_notes_payload = {
            "case_id": case_ctx["case_id"],
            "orchestration_notes": {
                "active_dispatch_id": dispatch_id,
                "lane_policy": "persistent_case_topics",
                "difficulty_profile": {
                    "difficulty_class": difficulty_profile.get("difficulty_class"),
                    "resolution_risk": difficulty_profile.get("resolution_risk"),
                    "evidence_floor": difficulty_profile.get("evidence_floor"),
                    "extra_verification_required": difficulty_profile.get("extra_verification_required"),
                    "source_of_truth_class": difficulty_profile.get("source_of_truth_class"),
                    "focus_hints": difficulty_profile.get("focus_hints") or [],
                },
                "rerun_context": rerun_context,
                "difficulty_meta": {
                    "classifier_source": difficulty_profile.get("classifier_source"),
                    "classifier_model": difficulty_profile.get("classifier_model"),
                    "classifier_version": difficulty_profile.get("classifier_version"),
                    "model_used": model_summary.get("used"),
                    "model_confidence": model_summary.get("model_confidence"),
                    "heuristic_confidence": heuristic_summary.get("heuristic_confidence"),
                    "fallback_reason": model_summary.get("fallback_reason"),
                    "classified_at": created_at,
                },
            },
        }
        if args.dry_run:
            case_notes_result = {
                "status": "dry_run",
                "would_update_case_id": case_ctx["case_id"],
                "would_merge_orchestration_notes": difficulty_notes_payload["orchestration_notes"],
            }
            market_state = {
                "status": "dry_run",
                "market_id": case_ctx["market_id"],
                "pipeline_status": "researching",
                "would_set_pipeline_status": "researching",
            }
        else:
            case_notes_result = python_json(update_case_notes_script, ["--pretty"], difficulty_notes_payload)
            market_state = python_json(
                set_status_script,
                ["--market-id", case_ctx["market_id"], "--pipeline-status", "researching"],
            )

        telegram_runtime = load_telegram_runtime_config()
        research_group = telegram_runtime["research_group"]
        controller_topic_title = build_topic_title(
            research_group["topic_title_templates"]["controller"],
            case_key=case_ctx["case_key"],
        )

        refresh_mode = str(args.refresh_mode or rerun_context.get('run_kind') or '').strip().lower()
        refresh_reasons = [item.strip() for item in str(args.refresh_reasons or '').split(',') if item.strip()]
        if not refresh_reasons and is_refresh_dispatch_mode(refresh_mode):
            refresh_reasons = ['material_move_reanalysis']
        refresh_controller_start_marker, refresh_controller_finish_marker = build_refresh_controller_markers(
            case_key=case_ctx['case_key'],
            market_title=case_ctx['title'],
            dispatch_id=dispatch_id,
            refresh_mode=refresh_mode or 'fresh',
            refresh_reasons=refresh_reasons,
        )
        refresh_detected_marker = str(args.refresh_detected_marker or '').strip()
        if not refresh_detected_marker and is_refresh_dispatch_mode(refresh_mode):
            delta_text = str(args.refresh_price_delta_pct_points or '').strip()
            reasons_text = ','.join(refresh_reasons)
            refresh_detected_marker = f"MATERIAL CHANGE DETECTED | case={case_ctx['case_key']} | market={case_ctx['title']} | refresh_mode={refresh_mode or 'full'} | delta_pct_points={delta_text} | reasons={reasons_text}"

        persona_paths = {
            persona: note_path(case_ctx["case_key"], created_at, dispatch_id, persona)
            for persona in args.personas
        }
        sidecar_paths = {
            persona: sidecar_path(case_ctx["case_key"], created_at, dispatch_id, persona)
            for persona in args.personas
        }
        assumption_paths = {
            persona: assumption_note_path(case_ctx["case_key"], created_at, dispatch_id, persona)
            for persona in args.personas
        }
        evidence_paths = {
            persona: evidence_map_path(case_ctx["case_key"], created_at, dispatch_id, persona)
            for persona in args.personas
        }
        qmd_bundle_path = str(analysis_root(case_ctx["case_key"], created_at, dispatch_id) / "qmd-bundle.json")
        qmd_bundle = generate_qmd_bundle(
            args=args,
            case_ctx=case_ctx,
            difficulty_profile=difficulty_profile,
            rerun_context=rerun_context,
        )
        qmd_bundle_write = write_qmd_bundle(qmd_bundle_path, qmd_bundle, dry_run=args.dry_run)
        scaffold_result = write_case_analysis_scaffolds(
            case_ctx,
            created_at=created_at,
            dispatch_id=dispatch_id,
            persona_paths=persona_paths,
            assumption_paths=assumption_paths,
            evidence_paths=evidence_paths,
            difficulty_profile=difficulty_profile,
            dry_run=args.dry_run,
        )

        runs = []
        for persona in args.personas:
            workspace_note_path = persona_paths[persona]
            reasoning_sidecar_path = sidecar_paths[persona]
            source_note_dir = source_note_directory(case_ctx["case_key"])
            source_note_prefix_value = source_note_prefix(created_at, persona)
            assumption_note_path_value = assumption_paths[persona]
            evidence_map_path_value = evidence_paths[persona]
            persona_topic_title = build_topic_title(
                research_group["topic_title_templates"]["persona"],
                case_key=case_ctx["case_key"],
                persona=persona,
            )
            lane_seed = latest_lane_seed(existing_runs, persona)
            lane_check = lane_fingerprint_mismatch(case_ctx, lane_seed) if lane_seed else None
            if lane_check and lane_check.get("mismatch"):
                if lane_check.get("missing_fingerprint"):
                    lane_seed = {}
                else:
                    raise ValueError(
                        f"lane fingerprint mismatch for persona '{persona}'; refusing topic reuse across mismatched market identity fields: {', '.join(lane_check.get('fields') or [])}"
                    )

            if args.dry_run:
                create_result = {
                    "research_run_id": make_dry_run_research_run_id(case_ctx["case_key"], persona),
                    "case_id": case_ctx["case_id"],
                    "run_label": f"{persona}-{case_ctx['case_key']}",
                    "agent_label": persona,
                    "runtime": DEFAULT_RUNTIME_LABEL,
                    "status": "queued",
                    "started_at": None,
                    "workspace_note_path": workspace_note_path,
                    "notes": {"difficulty_profile": difficulty_profile},
                    "created_at": created_at,
                    "dry_run": True,
                }
            else:
                create_result = python_json(
                    create_run_script,
                    [
                        "--case-id", case_ctx["case_id"],
                        "--agent-label", persona,
                        "--run-label", f"{persona}-{case_ctx['case_key']}",
                        "--workspace-note-path", workspace_note_path,
                        "--runtime", DEFAULT_RUNTIME_LABEL,
                        "--notes-json", json.dumps({"difficulty_profile": difficulty_profile}),
                    ],
                )

            prompt_payload = {
                **case_ctx,
                "agent_label": persona,
                "workspace_note_path": workspace_note_path,
                "reasoning_sidecar_path": reasoning_sidecar_path,
                "source_note_dir": source_note_dir,
                "source_note_prefix": source_note_prefix_value,
                "assumption_note_path": assumption_note_path_value,
                "evidence_map_path": evidence_map_path_value,
                "analysis_summary_path": summary_path(case_ctx["case_key"], created_at, dispatch_id),
                "case_file_path": case_file_path(case_ctx["case_key"]),
                "current_file_path": current_file_path(case_ctx["case_key"]),
                "timeline_file_path": timeline_file_path(case_ctx["case_key"]),
                "difficulty_profile": difficulty_profile,
                "qmd_bundle": qmd_bundle,
                "qmd_bundle_path": qmd_bundle_path,
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
                reasoning_sidecar_path=reasoning_sidecar_path,
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
                "reuse_existing_topic_id": lane_seed.get("delivery_target_topic_id"),
                "reuse_existing_controller_topic_id": lane_seed.get("controller_topic_id"),
            }

            handoff_payload = {
                "chatId": research_group["chat_id"],
                "topicTitle": persona_topic_title,
                "message": handoff_message,
            }

            base_notes = {
                "delivery_target_chat_id": lane_seed.get("delivery_target_chat_id") or research_group["chat_id"],
                "delivery_target_topic_title": persona_topic_title,
                "controller_chat_id": lane_seed.get("controller_chat_id") or research_group["chat_id"],
                "controller_topic_title": controller_topic_title,
                "dispatch_id": dispatch_id,
                "dispatch_stage": "awaiting_topic_reuse_or_creation",
                "refresh_mode": refresh_mode,
                "refresh_reasons": refresh_reasons,
                "refresh_detected_marker": refresh_detected_marker,
                "runtime_surface": DEFAULT_RUNTIME_SURFACE,
                "expected_start_marker": start_marker,
                "expected_finish_marker": finish_marker,
                "model": args.model,
                "thinking": args.thinking,
                "difficulty_profile": difficulty_profile,
                "lane_policy": "persistent_case_topics",
                "lane_reused": bool(lane_seed),
                "lane_source_research_run_id": lane_seed.get("source_research_run_id"),
                "lane_source_dispatch_id": lane_seed.get("source_dispatch_id"),
                "lane_fingerprint": lane_fingerprint,
                "run_kind": rerun_context["run_kind"],
                "rerun_scope": rerun_context["rerun_scope"],
                "prior_dispatch_count": rerun_context["prior_dispatch_count"],
                "prior_case_count": rerun_context["prior_case_count"],
                "qmd_used": qmd_bundle.get("qmd_used", False),
                "qmd_tier": qmd_bundle.get("qmd_tier"),
                "qmd_bundle_path": qmd_bundle_path,
                "qmd_result_paths": qmd_bundle.get("result_paths") or [],
                "qmd_query_profile": qmd_bundle.get("query_profile") or {},
                "reasoning_sidecar_path": reasoning_sidecar_path,
            }
            if lane_seed.get("delivery_target_topic_id"):
                base_notes["delivery_target_topic_id"] = lane_seed["delivery_target_topic_id"]
            if lane_seed.get("delivery_target_session_key"):
                base_notes["delivery_target_session_key"] = lane_seed["delivery_target_session_key"]
            if lane_seed.get("controller_topic_id"):
                base_notes["controller_topic_id"] = lane_seed["controller_topic_id"]

            post_handoff_update_template = {
                "research_run_id": create_result["research_run_id"],
                "status": "running",
                "mark_started": True,
                "workspace_note_path": workspace_note_path,
                "notes": {
                    **base_notes,
                    "dispatch_stage": "persona_topic_running",
                },
            }

            notes = dict(base_notes)

            if args.dry_run:
                update_result = {
                    **create_result,
                    "status": "queued",
                    "workspace_note_path": workspace_note_path,
                    "notes": notes,
                    "dry_run": True,
                }
            else:
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
                    "reasoning_sidecar_path": reasoning_sidecar_path,
                    "expected_auxiliary_paths": {
                        "source_note_directory": source_note_dir,
                        "source_note_prefix": source_note_prefix_value,
                        "reasoning_sidecar_path": reasoning_sidecar_path,
                        "assumption_note_path": assumption_note_path_value,
                        "evidence_map_path": evidence_map_path_value,
                    },
                    "research_run": update_result,
                    "lane_reused": bool(lane_seed),
                    "lane_fingerprint_check": lane_check,
                    "handoff": {
                        "status": "awaiting_topic_reuse_or_creation",
                        "target": logical_target,
                        "handoff_payload": handoff_payload,
                        "post_handoff_update_template": post_handoff_update_template,
                    },
                }
            )

        result = {
            "dispatch_id": dispatch_id,
            "created_at": created_at,
            "dry_run": args.dry_run,
            "mode": "dry_run" if args.dry_run else "apply",
            "difficulty_profile": difficulty_profile,
            "difficulty_persistence": case_notes_result,
            "scaffolds": scaffold_result,
            "qmd": {"bundle_path": qmd_bundle_path, "bundle_write": qmd_bundle_write, "bundle": qmd_bundle},
            "superseded_stale_runs": superseded_runs,
            "planner": {
                "script": "roles/orchestrator/researchers-swarm-subagents/planner/scripts/dispatch_case_research.py",
                "version": None,
            },
            "case": {
                "case_id": case_ctx["case_id"],
                "case_key": case_ctx["case_key"],
                "status": case_ctx["case_status"],
                "previous_active_dispatch_id": case_run_state.get("active_dispatch_id"),
                "lane_policy": "persistent_case_topics",
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
                "refresh_mode": refresh_mode,
                "refresh_reasons": refresh_reasons,
                "refresh_detected_marker": refresh_detected_marker,
                "refresh_start_marker": refresh_controller_start_marker,
                "refresh_finish_marker": refresh_controller_finish_marker,
                "model": args.model,
                "thinking": args.thinking,
            },
            "pipeline_status": market_state["pipeline_status"],
            "dispatch_stage": "dry_run_preview" if args.dry_run else "awaiting_topic_reuse_or_creation",
            "agent_runtime_dispatch_required": not args.dry_run,
            "preflight": {
                "running_conflict_count": len(running_conflicts),
                "stale_queued_count": len(stale_queued),
                "would_set_active_dispatch_id": dispatch_id,
                "would_reuse_lane_count": sum(1 for run in runs if run.get("lane_reused")),
                "would_create_attempt_count": len(runs),
            },
            "agent_runtime_steps": [
                "validate manifest before launch",
                "for each run, check idempotency against current research_runs status and prior telegram topic metadata",
                "if the case already has active running attempts, block the rerun until the active swarm is reconciled",
                "if the case has stale queued attempts, supersede them before creating new attempt rows",
                "before reusing a prior lane, require an exact lane fingerprint match on case_id, market_id, platform, external_market_id, and outcome_type",
                "legacy lanes without a stored fingerprint must not be reused; create fresh topics for those personas instead",
                "reuse the existing controller/persona Telegram topics when prior lane metadata exists and the fingerprint matches; otherwise create the missing topics",
                "resolve each created or reused topic to a telegram topic session key",
                "after topic bootstrap, materialize each topic session if needed and fan out the eligible persona sessions.send handoffs in parallel where possible",
                "after each successful handoff, build a filled DB patch from runs[i].handoff.post_handoff_update_template",
                "patch the corresponding research_runs row using update_research_run.py so status becomes running only after topic reuse/creation and persona-topic handoff succeed",
                "scope later reconciliation/finalization to the case's active_dispatch_id so historical attempts do not block closure",
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
