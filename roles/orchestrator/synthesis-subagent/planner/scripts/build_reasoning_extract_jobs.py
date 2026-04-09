#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    extract_explicit_probability_from_persona,
    load_json,
    reasoning_extract_job_input_fingerprint,
    relative_to_workspace,
    sha256_text,
    synthesis_reasoning_extract_dir_for,
    synthesis_reasoning_extract_path_for,
    write_json,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build per-persona reasoning-extraction jobs from a synthesis bundle")
    parser.add_argument("--bundle-json", required=True)
    parser.add_argument("--out", help="Optional output path for reasoning-extract-jobs.json")
    parser.add_argument("--include-support-bodies", action="store_true", help="Inline support-note bodies in each job (off by default for token efficiency)")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def group_supporting_artifacts(bundle: dict[str, Any]) -> dict[str, dict[str, list[dict[str, Any]]]]:
    grouped: dict[str, dict[str, list[dict[str, Any]]]] = {}
    for artifact in bundle.get("supporting_artifacts", []):
        persona = str(artifact.get("persona") or "").strip()
        kind = str(artifact.get("kind") or "other").strip()
        grouped.setdefault(persona, {}).setdefault(kind, []).append(artifact)
    return grouped


def manifest_run_map(bundle: dict[str, Any]) -> dict[str, dict[str, Any]]:
    runs = (bundle.get("manifest") or {}).get("runs") or []
    out: dict[str, dict[str, Any]] = {}
    for run in runs:
        persona = str(run.get("persona") or "").strip()
        if persona:
            out[persona] = run
    return out


def manifest_bootstrap_state(bundle: dict[str, Any]) -> dict[str, Any]:
    manifest = bundle.get("manifest") or {}
    bootstrap = manifest.get("bootstrap_state")
    return bootstrap if isinstance(bootstrap, dict) else {}


def bootstrap_run_state(bootstrap: dict[str, Any], research_run_id: str) -> dict[str, Any]:
    runs = bootstrap.get("runs")
    if not isinstance(runs, dict):
        return {}
    run_state = runs.get(research_run_id)
    return run_state if isinstance(run_state, dict) else {}


def main() -> None:
    args = parse_args()
    bundle_path = Path(args.bundle_json)
    if not bundle_path.is_absolute():
        bundle_path = WORKSPACE_ROOT / bundle_path
    bundle = load_json(bundle_path)

    grouped_support = group_supporting_artifacts(bundle)
    run_map = manifest_run_map(bundle)
    bootstrap = manifest_bootstrap_state(bundle)
    controller_bootstrap = bootstrap.get("controller_topic") if isinstance(bootstrap.get("controller_topic"), dict) else {}
    dispatch_dir = (WORKSPACE_ROOT / bundle["dispatch_dir"]).resolve()
    reasoning_extract_dir = synthesis_reasoning_extract_dir_for(dispatch_dir)
    jobs = []
    for persona_entry in bundle.get("persona_findings", []):
        persona = persona_entry["persona"]
        persona_support = grouped_support.get(persona, {})
        assumptions = persona_support.get("assumption", [])
        evidence = persona_support.get("evidence", [])
        run_info = run_map.get(persona, {})
        research_run_id = run_info.get("research_run_id") or ""
        run_notes = (run_info.get("research_run") or {}).get("notes") or {}
        handoff_target = (run_info.get("handoff") or {}).get("target") or {}
        bootstrap_run = bootstrap_run_state(bootstrap, research_run_id)
        bootstrap_topic_id = bootstrap_run.get("topic_id") or ""
        bootstrap_topic_title = bootstrap_run.get("topic_title") or ""
        bootstrap_session_key = bootstrap_run.get("session_key") or ""
        controller_bootstrap_topic_id = controller_bootstrap.get("topic_id") or ""
        controller_bootstrap_topic_title = controller_bootstrap.get("topic_title") or ""
        persona_frontmatter = persona_entry.get("frontmatter") or {}
        persona_summary = persona_entry.get("summary") or ""
        persona_body = persona_entry.get("body") or ""
        job = {
            "artifact_type": "persona_reasoning_extract_job",
            "case_key": bundle.get("case_key", ""),
            "dispatch_id": bundle.get("dispatch_id", ""),
            "analysis_date": bundle.get("analysis_date", ""),
            "question": bundle.get("question", ""),
            "market_implied_probability": bundle.get("market_implied_probability"),
            "persona": persona,
            "persona_finding_path": persona_entry["path"],
            "persona_frontmatter": persona_frontmatter,
            "persona_summary": persona_summary,
            "persona_body": persona_body,
            "target_session_key": run_notes.get("delivery_target_session_key") or run_info.get("target_session_key") or bootstrap_session_key or "",
            "delivery_target_chat_id": run_notes.get("delivery_target_chat_id") or handoff_target.get("chat_id") or bootstrap.get("chat_id") or "",
            "delivery_target_topic_id": run_notes.get("delivery_target_topic_id") or run_info.get("telegram_topic_id") or handoff_target.get("reuse_existing_topic_id") or bootstrap_topic_id,
            "delivery_target_topic_title": run_notes.get("delivery_target_topic_title") or handoff_target.get("topic_title") or bootstrap_topic_title or "",
            "controller_chat_id": run_notes.get("controller_chat_id") or handoff_target.get("chat_id") or bootstrap.get("chat_id") or "",
            "controller_topic_id": run_notes.get("controller_topic_id") or handoff_target.get("reuse_existing_controller_topic_id") or controller_bootstrap_topic_id,
            "controller_topic_title": run_notes.get("controller_topic_title") or handoff_target.get("controller_topic_title") or controller_bootstrap_topic_title or "",
            "research_run_id": research_run_id,
            "support_mode": "with_bodies" if args.include_support_bodies else "metadata_and_summaries_only",
            "persona_source_sha256": sha256_text(persona_summary + "\n\n" + persona_body),
            "persona_explicit_probability": extract_explicit_probability_from_persona(persona_frontmatter, persona_body),
            "reasoning_extract_path": relative_to_workspace(synthesis_reasoning_extract_path_for(dispatch_dir, persona)),
            "assumption_artifacts": [
                {
                    "path": artifact["path"],
                    "summary": artifact.get("summary") or "",
                    **({"body": artifact.get("body") or ""} if args.include_support_bodies else {}),
                }
                for artifact in assumptions
            ],
            "evidence_artifacts": [
                {
                    "path": artifact["path"],
                    "summary": artifact.get("summary") or "",
                    **({"body": artifact.get("body") or ""} if args.include_support_bodies else {}),
                }
                for artifact in evidence
            ],
        }
        job["job_input_sha256"] = reasoning_extract_job_input_fingerprint(job)
        jobs.append(job)

    jobs_payload = {
        "artifact_type": "persona_reasoning_extract_jobs",
        "case_key": bundle.get("case_key", ""),
        "dispatch_id": bundle.get("dispatch_id", ""),
        "analysis_date": bundle.get("analysis_date", ""),
        "question": bundle.get("question", ""),
        "market_implied_probability": bundle.get("market_implied_probability"),
        "support_mode": "with_bodies" if args.include_support_bodies else "metadata_and_summaries_only",
        "source_bundle_path": relative_to_workspace(bundle_path),
        "reasoning_extract_dir": relative_to_workspace(reasoning_extract_dir),
        "jobs": jobs,
    }

    out_path = Path(args.out) if args.out else bundle_path.with_name("reasoning-extract-jobs.json")
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    write_json(out_path, jobs_payload, pretty=args.pretty)

    output = {
        "ok": True,
        "jobs_path": relative_to_workspace(out_path),
        "case_key": bundle.get("case_key", ""),
        "dispatch_id": bundle.get("dispatch_id", ""),
        "job_count": len(jobs),
        "support_mode": jobs_payload["support_mode"],
    }
    print(json.dumps(output, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
