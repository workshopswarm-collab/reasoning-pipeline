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
    SECTION_ORDER,
    SYNDICATED_TEMPLATE_PATH,
    WORKSPACE_ROOT,
    load_json,
)

BASE_CONTRACT_PATH = SUBAGENT_DIR / "planner" / "prompts" / "synthesis_base_contract.md"
TRUTH_FINDING_POLICY_PATH = SUBAGENT_DIR / "planner" / "prompts" / "synthesis_gapfill_research_policy.md"

SYNTHESIZER_FRONTMATTER_FIELDS = [
    ("coverage_status", "complete | partial"),
    ("syndicated_probability_low", "decimal probability in [0,1]"),
    ("syndicated_probability_high", "decimal probability in [0,1]"),
    ("edge_independent_verification_quality", "low | medium | high"),
    ("compressed_toward_market_due_to_verification", "yes | no"),
    ("contract_ambiguity_level", "none | minor | moderate | major"),
    ("contract_ambiguity_reason", "short string; required when ambiguity level is not none"),
    ("independently_verified_points", "list of short strings"),
    ("verification_gap_summary", "short string"),
    ("best_countercase_summary", "short string"),
    ("main_reason_for_disagreement", "short string"),
    ("resolution_mechanics_summary", "short string"),
    ("freshness_sensitive", "yes | no"),
    ("freshness_driver", "short string"),
    ("decision_blockers", "list of short strings"),
    ("blockers_require_new_research", "yes | no"),
    ("disagreement_type", "facts | contract | timing | interpretation | market_pricing | mixed"),
    ("disagreement_intensity", "low | medium | high"),
    ("synthesis_confidence_quality", "low | medium | high"),
    ("staleness_risk", "low | medium | high"),
    ("next_checkpoint", "short string"),
    ("follow_up_needed", "yes | no"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a synthesis prompt from a sidecar-first or raw synthesis bundle")
    parser.add_argument("--bundle-json", required=True, help="Bundle JSON emitted by build_sidecar_synthesis_bundle.py or build_synthesis_bundle.py")
    parser.add_argument("--out", help="Optional output path for the prompt markdown")
    parser.add_argument("--allow-truth-finding-research", dest="allow_truth_finding_research", action="store_true", help="Permit synthesis-stage truth-finding internet research aimed at improving predictive accuracy")
    parser.add_argument("--no-truth-finding-research", dest="allow_truth_finding_research", action="store_false", help="Disable synthesis-stage truth-finding research guidance")
    parser.add_argument("--allow-gapfill-research", dest="allow_truth_finding_research", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--no-gapfill-research", dest="allow_truth_finding_research", action="store_false", help=argparse.SUPPRESS)
    parser.set_defaults(allow_truth_finding_research=True)
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def indent_block(text: str, prefix: str = "    ") -> str:
    return "\n".join(prefix + line for line in text.rstrip().splitlines())


def render_output_contract(lines: list[str]) -> None:
    lines.append("## Output contract")
    lines.append("")
    lines.append("Return JSON only. Do not wrap the JSON in markdown fences.")
    lines.append("")
    lines.append("Top-level schema:")
    lines.append("")
    lines.append("```json")
    lines.append("{")
    lines.append('  "claim": "...",')
    lines.append('  "frontmatter": {')
    for idx, (field, desc) in enumerate(SYNTHESIZER_FRONTMATTER_FIELDS):
        comma = "," if idx < len(SYNTHESIZER_FRONTMATTER_FIELDS) - 1 else ""
        lines.append(f'    "{field}": "{desc}"{comma}')
    lines.append("  },")
    lines.append('  "sections": {')
    for idx, section in enumerate(SECTION_ORDER):
        comma = "," if idx < len(SECTION_ORDER) - 1 else ""
        lines.append(f'    "{section}": "..."{comma}')
    lines.append("  }")
    lines.append("}")
    lines.append("```")
    lines.append("")
    lines.append("Rules:")
    lines.append("- Fill only the synthesizer-authored frontmatter fields above.")
    lines.append("- Do not invent runtime-populated fields such as case_key, dispatch_id, question, or market_implied_probability.")
    lines.append("- Do not hand-calculate midpoint, edge_vs_market_pct_points, relation_to_market, or edge_quality.")
    lines.append("- Use decimal probabilities in [0,1].")
    lines.append("- The syndicated probability range must be your own final post-synthesis judgment, not a mechanical summary of lane probabilities.")
    lines.append("- Use the swarm-implied probability center as a meaningful baseline input, but move away from it when critical review, verification, or truth-finding justifies doing so.")
    lines.append("- If your final probability differs materially from the swarm-implied center, explain why.")
    lines.append("- Preserve disagreement when the bundle does not justify flattening it.")
    lines.append("- Explicitly rate how well the final edge was independently verified.")
    lines.append("- Explicitly say whether the final synthesis compressed toward market because verification was insufficient.")
    lines.append("- Set contract_ambiguity_level to none | minor | moderate | major based on whether resolution mechanics, classification, source-of-truth rules, or operational implementation could materially change the final decision.")
    lines.append("- Use contract_ambiguity_reason to name the exact ambiguity concisely; leave it blank only when contract_ambiguity_level is none.")
    lines.append("- independently_verified_points should be a compact list of the specific points the synthesis regards as independently verified enough for downstream decision use.")
    lines.append("- verification_gap_summary should name the most important remaining verification gap in one short sentence.")
    lines.append("- best_countercase_summary should compress the strongest surviving countercase into one short sentence.")
    lines.append("- main_reason_for_disagreement should name the main driver of remaining persona disagreement in one short sentence.")
    lines.append("- resolution_mechanics_summary should compress the key resolution/source-of-truth mechanics into one short sentence for downstream decision use.")
    lines.append("- freshness_sensitive should be yes when timing freshness could materially change the downstream decision.")
    lines.append("- freshness_driver should name the exact catalyst, data source, or timing dependency causing freshness sensitivity.")
    lines.append("- decision_blockers should list the concrete blockers most likely to stop a downstream decision or force caution.")
    lines.append("- blockers_require_new_research should be yes only when at least one blocker really requires additional research rather than just operator caution.")
    lines.append("- disagreement_type should classify the main remaining disagreement as facts | contract | timing | interpretation | market_pricing | mixed.")
    lines.append("- These structured handoff fields are for the downstream Decision-Maker; make them compact, explicit, and directly reusable without rereading long prose.")
    lines.append("- If a section genuinely has nothing material to add, return an empty string rather than filler.")
    lines.append("")


def normalize_inline_text(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines()).strip()


def compact_body_excerpt(body: str, *, max_chars: int = 900) -> str:
    text = normalize_inline_text(body)
    if not text:
        return ""
    paragraphs = [part.strip() for part in text.split("\n\n") if part.strip()]
    excerpt_parts: list[str] = []
    total = 0
    for part in paragraphs:
        if total >= max_chars:
            break
        remaining = max_chars - total
        take = part[:remaining].rstrip()
        if not take:
            continue
        excerpt_parts.append(take)
        total += len(take)
    excerpt = "\n\n".join(excerpt_parts).strip()
    if len(text) > len(excerpt):
        excerpt = excerpt.rstrip() + "\n\n[truncated]"
    return excerpt


def meaningful_summary(persona: dict[str, Any]) -> str:
    summary = normalize_inline_text(persona.get("summary") or "")
    if summary and summary.lower() not in {"# claim", "claim"} and len(summary) > 20:
        return summary
    return compact_body_excerpt(persona.get("body") or "", max_chars=500)


def select_personas_for_extended_raw_body(bundle: dict[str, Any]) -> set[str]:
    selected: set[str] = set()
    median = bundle.get("provisional_swarm_probability_median")
    for extract in bundle.get("extracts", []):
        persona = str(extract.get("persona") or "").strip()
        payload = extract.get("payload") or {}
        if not persona:
            continue
        if str(payload.get("recommended_weight") or "").strip() == "high":
            selected.add(persona)
            continue
        own_prob = payload.get("own_probability")
        if isinstance(median, (int, float)) and isinstance(own_prob, (int, float)) and abs(float(own_prob) - float(median)) >= 0.02:
            selected.add(persona)
    return selected


def render_raw_persona_reference(lines: list[str], source_bundle: dict[str, Any], bundle: dict[str, Any]) -> None:
    lines.append("## Raw persona finding reference")
    lines.append("")
    lines.append("These raw persona findings remain the authoritative upstream artifacts. Use them to verify or challenge extracts that seem compressed, overstated, or incomplete.")
    lines.append("By default this section is selective rather than full-body: all personas get a compact claim/summary excerpt, and only a small subset get a larger raw-body excerpt.")
    lines.append("")
    extended_personas = select_personas_for_extended_raw_body(bundle)
    for persona in source_bundle.get("persona_findings", []):
        persona_name = persona['persona']
        lines.append(f"### Persona: {persona_name}")
        lines.append(f"Path: `{persona['path']}`")
        frontmatter = persona.get("frontmatter") or {}
        if frontmatter:
            lines.append(f"Frontmatter: {json.dumps(frontmatter, ensure_ascii=False)}")
        summary = meaningful_summary(persona)
        if summary:
            lines.append("")
            lines.append("Claim/summary excerpt:")
            lines.append(summary)
        if persona_name in extended_personas:
            body_excerpt = compact_body_excerpt(persona.get("body") or "", max_chars=1600)
            if body_excerpt:
                lines.append("")
                lines.append("Extended raw-body excerpt:")
                lines.append(body_excerpt)
        lines.append("")


def render_sidecar_bundle(lines: list[str], bundle: dict[str, Any], source_bundle: dict[str, Any] | None) -> None:
    lines.append("## Researcher-sidecar synthesis substrate")
    lines.append("")
    lines.append("This bundle is sidecar-first for navigation efficiency, but the sidecars are not canonical truth.")
    lines.append("Treat each persona reasoning sidecar as a compact, structured summary of the corresponding raw finding, not as an independent evidentiary source.")
    lines.append("The raw persona findings remain the authoritative upstream artifacts, and you should critically compare the sidecars against those raw findings before trusting them.")
    lines.append("")
    lines.append(f"- coverage_status: {bundle.get('coverage_status')}")
    lines.append(f"- available_personas: {', '.join(bundle.get('available_personas', [])) or '[none]'}")
    lines.append(f"- missing_personas: {', '.join(bundle.get('missing_personas', [])) or '[none]'}")
    if bundle.get("market_implied_probability") is not None:
        lines.append(f"- market_implied_probability: {bundle['market_implied_probability']}")
    if bundle.get("market_snapshot_time"):
        lines.append(f"- market_snapshot_time: {bundle['market_snapshot_time']}")
    if bundle.get("reasoning_mode_counts"):
        lines.append(f"- reasoning_mode_counts: {json.dumps(bundle['reasoning_mode_counts'], ensure_ascii=False)}")
    if bundle.get("recommended_weight_counts"):
        lines.append(f"- recommended_weight_counts: {json.dumps(bundle['recommended_weight_counts'], ensure_ascii=False)}")
    if bundle.get("persona_probability_estimates"):
        lines.append(f"- persona_probability_estimates: {json.dumps(bundle['persona_probability_estimates'], ensure_ascii=False)}")
    if bundle.get("provisional_swarm_probability_median") is not None:
        lines.append(f"- provisional_swarm_probability_range: {bundle.get('provisional_swarm_probability_low')} to {bundle.get('provisional_swarm_probability_high')}")
        lines.append(f"- provisional_swarm_probability_median: {bundle.get('provisional_swarm_probability_median')}")
        lines.append(f"- provisional_swarm_edge_vs_market_pct_points: {bundle.get('provisional_swarm_edge_vs_market_pct_points')}")
        lines.append(f"- provisional_edge_verification_bar: {bundle.get('provisional_edge_verification_bar')}")
        lines.append("- instruction: treat the provisional swarm probability center as a real baseline prior from the swarm's probability outputs, but not as a final answer.")
        lines.append("- instruction: treat this provisional swarm-vs-market gap as a skepticism aid, not as a conclusion. The larger the provisional edge, the stronger the independent verification bar before trusting it.")
        lines.append("- instruction: if your final range differs materially from the provisional swarm center, explain why in 'Difference from swarm-implied center'.")
    lines.append("")
    lines.append("## Persona reasoning sidecars")
    lines.append("")
    for sidecar in bundle.get("sidecars", []):
        payload = sidecar.get("payload") or {}
        lines.append(f"### Persona: {sidecar.get('persona')}")
        lines.append(f"Sidecar path: `{sidecar.get('path')}`")
        if sidecar.get("persona_finding_path"):
            lines.append(f"Raw finding path: `{sidecar['persona_finding_path']}`")
        lines.append("Critical reading task: decide whether this sidecar appears faithful, incomplete, distorted, or overconfident relative to the raw finding.")
        assumption_paths = sidecar.get("assumption_artifact_paths") or []
        evidence_paths = sidecar.get("evidence_artifact_paths") or []
        if assumption_paths:
            lines.append(f"Assumption paths: {json.dumps(assumption_paths, ensure_ascii=False)}")
        if evidence_paths:
            lines.append(f"Evidence paths: {json.dumps(evidence_paths, ensure_ascii=False)}")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(payload, indent=2, ensure_ascii=False))
        lines.append("```")
        lines.append("")
    if source_bundle:
        render_raw_persona_reference(lines, source_bundle, bundle)

def render_raw_bundle(lines: list[str], bundle: dict[str, Any]) -> None:
    lines.append("## Raw persona findings")
    lines.append("")
    lines.append("This prompt is using the older raw synthesis bundle format. Raw persona findings are therefore the primary synthesis substrate.")
    lines.append("")
    for persona in bundle.get("persona_findings", []):
        lines.append(f"### Persona: {persona['persona']}")
        lines.append(f"Path: `{persona['path']}`")
        lines.append("")
        lines.append(persona["body"].rstrip())
        lines.append("")
    if bundle.get("supporting_artifacts"):
        lines.append("## Supporting artifacts")
        lines.append("")
        for artifact in bundle["supporting_artifacts"]:
            lines.append(f"### {artifact['kind'].title()}: {artifact['persona']}")
            lines.append(f"Path: `{artifact['path']}`")
            lines.append("")
            lines.append(artifact["body"].rstrip())
            lines.append("")


def build_prompt(bundle: dict, *, allow_truth_finding_research: bool) -> str:
    artifact_type = bundle.get("artifact_type") or ""
    contract = BASE_CONTRACT_PATH.read_text().strip()
    truth_finding_policy = TRUTH_FINDING_POLICY_PATH.read_text().strip() if allow_truth_finding_research and TRUTH_FINDING_POLICY_PATH.exists() else ""
    template = SYNDICATED_TEMPLATE_PATH.read_text().strip()
    source_bundle = None
    if artifact_type == "sidecar_synthesis_bundle" and bundle.get("source_bundle_path"):
        source_bundle_path = Path(str(bundle["source_bundle_path"]))
        if not source_bundle_path.is_absolute():
            source_bundle_path = WORKSPACE_ROOT / source_bundle_path
        if source_bundle_path.exists():
            source_bundle = load_json(source_bundle_path)
    lines: list[str] = []
    lines.append("# Synthesis Task")
    lines.append("")
    lines.append(f"- case_key: `{bundle['case_key']}`")
    lines.append(f"- dispatch_id: `{bundle['dispatch_id']}`")
    lines.append(f"- analysis_date: `{bundle['analysis_date']}`")
    lines.append(f"- question: {bundle.get('question') or '[missing question]'}")
    if bundle.get("market_implied_probability") is not None:
        lines.append(f"- market_implied_probability: {bundle['market_implied_probability']}")
    available_personas = bundle.get("available_personas") or bundle.get("source_personas") or []
    missing_personas = bundle.get("missing_personas") or []
    lines.append(f"- available_personas: {', '.join(available_personas) or '[none]'}")
    lines.append(f"- missing_personas: {', '.join(missing_personas) or '[none]'}")
    lines.append(f"- bundle_artifact_type: {artifact_type or '[unknown]'}")
    lines.append("")
    lines.append("## Base contract")
    lines.append("")
    lines.append(contract)
    lines.append("")
    if truth_finding_policy:
        lines.append("## Synthesis-stage truth-finding research policy")
        lines.append("")
        lines.append(truth_finding_policy)
        lines.append("")
    render_output_contract(lines)
    lines.append("## Artifact template reference")
    lines.append("")
    lines.append(indent_block(template))
    lines.append("")

    if artifact_type == "sidecar_synthesis_bundle":
        render_sidecar_bundle(lines, bundle, source_bundle)
    else:
        render_raw_bundle(lines, bundle)

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    bundle_path = Path(args.bundle_json)
    if not bundle_path.is_absolute():
        bundle_path = WORKSPACE_ROOT / bundle_path
    bundle = load_json(bundle_path)
    prompt = build_prompt(bundle, allow_truth_finding_research=args.allow_truth_finding_research)
    out_path = Path(args.out) if args.out else bundle_path.with_name("synthesis-prompt.md")
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(prompt)
    summary = {
        "ok": True,
        "bundle_json": str(bundle_path.resolve().relative_to(WORKSPACE_ROOT)),
        "prompt_path": str(out_path.resolve().relative_to(WORKSPACE_ROOT)),
        "bundle_artifact_type": bundle.get("artifact_type") or "",
        "allow_truth_finding_research": args.allow_truth_finding_research,
        "sidecar_count": len(bundle.get("sidecars", [])) if bundle.get("artifact_type") == "sidecar_synthesis_bundle" else 0,
        "source_persona_count": len(bundle.get("persona_findings", [])) if bundle.get("artifact_type") != "sidecar_synthesis_bundle" else 0,
    }
    print(json.dumps(summary, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
