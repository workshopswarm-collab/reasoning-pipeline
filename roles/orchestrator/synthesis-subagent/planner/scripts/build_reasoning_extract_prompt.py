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

from common import WORKSPACE_ROOT, load_json, sha256_text  # noqa: E402

CONTRACT_PATH = SUBAGENT_DIR / "planner" / "prompts" / "persona_reasoning_extract_contract.md"

EXTRACT_SCHEMA = {
    "persona": "string",
    "main_thesis": "string",
    "own_probability": "decimal probability in [0,1] or blank",
    "reasoning_mode": [
        "base_rate",
        "market_anchor",
        "scenario_analysis",
        "catalyst_analysis",
        "risk_management",
        "contract_interpretation",
        "variant_hypothesis",
        "technical_reference",
        "other",
    ],
    "key_assumptions": ["short strings"],
    "strongest_supports": ["short strings"],
    "strongest_disconfirmers": ["short strings"],
    "main_logical_chain": ["short strings"],
    "fragility_points": ["short strings"],
    "unresolved_ambiguities": ["short strings"],
    "timing_relevance": "string",
    "source_quality_view": "string",
    "what_would_change_view": "string",
    "recommended_weight": "low | medium | high",
    "confidence_in_extract": "low | medium | high",
    "quote_anchors": ["optional short supporting quotes or anchored snippets"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a compact persona reasoning-extraction prompt")
    parser.add_argument("--jobs-json", required=True)
    parser.add_argument("--persona", required=True)
    parser.add_argument("--out", help="Optional output path for the prompt markdown")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def find_job(jobs_payload: dict, persona: str) -> dict:
    matches = [job for job in jobs_payload.get("jobs", []) if job.get("persona") == persona]
    if not matches:
        raise SystemExit(f"persona not found in jobs file: {persona}")
    if len(matches) > 1:
        raise SystemExit(f"multiple jobs found for persona: {persona}")
    return matches[0]


def format_support_block(items: list[dict], label: str) -> list[str]:
    lines: list[str] = []
    if not items:
        lines.append(f"## {label}")
        lines.append("")
        lines.append("[none]")
        lines.append("")
        return lines
    lines.append(f"## {label}")
    lines.append("")
    for item in items:
        lines.append(f"- Path: `{item['path']}`")
        if item.get("summary"):
            lines.append(f"  - Summary: {item['summary']}")
        if item.get("body"):
            lines.append("  - Body:")
            for body_line in str(item["body"]).rstrip().splitlines():
                lines.append(f"      {body_line}")
        lines.append("")
    return lines


def build_prompt(job: dict) -> str:
    contract = CONTRACT_PATH.read_text().strip()
    lines: list[str] = []
    lines.append("# Persona Reasoning Extraction Task")
    lines.append("")
    lines.append(f"- case_key: `{job['case_key']}`")
    lines.append(f"- dispatch_id: `{job['dispatch_id']}`")
    lines.append(f"- analysis_date: `{job['analysis_date']}`")
    lines.append(f"- persona: `{job['persona']}`")
    lines.append(f"- question: {job.get('question') or '[missing question]'}")
    if job.get("market_implied_probability") is not None:
        lines.append(f"- market_implied_probability: {job['market_implied_probability']}")
    lines.append(f"- support_mode: {job.get('support_mode')}")
    lines.append("")
    lines.append("## Contract")
    lines.append("")
    lines.append(contract)
    lines.append("")
    lines.append("## Output schema")
    lines.append("")
    lines.append("Return JSON only. Do not wrap the JSON in markdown fences.")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(EXTRACT_SCHEMA, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Persona finding")
    lines.append("")
    lines.append(f"Path: `{job['persona_finding_path']}`")
    lines.append("")
    if job.get("persona_summary"):
        lines.append(f"Summary: {job['persona_summary']}")
        lines.append("")
    lines.append(job.get("persona_body", "").rstrip())
    lines.append("")
    lines.extend(format_support_block(job.get("assumption_artifacts", []), "Assumption artifacts"))
    lines.extend(format_support_block(job.get("evidence_artifacts", []), "Evidence artifacts"))
    lines.append("## Extraction reminders")
    lines.append("")
    lines.append("- Preserve the persona's actual reasoning rather than rewriting it into generic synthesis language.")
    lines.append("- If the note implies a heuristic but does not state it explicitly, keep the label conservative.")
    lines.append("- Keep list items short and evidence-bearing.")
    lines.append("- Leave `own_probability` blank if the persona did not clearly commit to one.")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    jobs_path = Path(args.jobs_json)
    if not jobs_path.is_absolute():
        jobs_path = WORKSPACE_ROOT / jobs_path
    jobs_payload = load_json(jobs_path)
    job = find_job(jobs_payload, args.persona)
    prompt = build_prompt(job)
    out_path = Path(args.out) if args.out else jobs_path.with_name(f"reasoning-extract-{args.persona}-prompt.md")
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(prompt)
    summary = {
        "ok": True,
        "jobs_json": str(jobs_path.resolve().relative_to(WORKSPACE_ROOT)),
        "persona": args.persona,
        "prompt_path": str(out_path.resolve().relative_to(WORKSPACE_ROOT)),
        "prompt_sha256": sha256_text(prompt),
        "support_mode": job.get("support_mode"),
        "assumption_artifact_count": len(job.get("assumption_artifacts", [])),
        "evidence_artifact_count": len(job.get("evidence_artifacts", [])),
    }
    print(json.dumps(summary, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
