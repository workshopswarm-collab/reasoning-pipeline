#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import (  # noqa: E402
    DECISION_HEADER_ORDER,
    RESEARCH_CASES_ROOT,
    SECTION_ORDER,
    WORKSPACE_ROOT,
    case_synthesis_markdown_path_for,
    coerce_string,
    derive_syndicated_fields,
    dump_frontmatter,
    load_json,
    relative_to_workspace,
)
from validation import validate_synthesis_result_payload  # noqa: E402


DEFAULT_CLAIM = "No synthesized claim provided."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render syndicated-finding markdown from bundle + synthesizer JSON")
    parser.add_argument("--bundle-json", required=True)
    parser.add_argument("--result-json", required=True, help="Synthesizer JSON result")
    parser.add_argument("--out", help="Optional explicit output markdown path")
    parser.add_argument("--write-current", action="store_true", help="Also write the canonical case-level artifact under cases/<case-key>/synthesizer-agent/")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def build_frontmatter(bundle: dict[str, Any], authored_frontmatter: dict[str, Any]) -> OrderedDict[str, Any]:
    derived = derive_syndicated_fields(
        market_implied_probability=bundle.get("market_implied_probability"),
        low=authored_frontmatter.get("syndicated_probability_low"),
        high=authored_frontmatter.get("syndicated_probability_high"),
    )
    merged: dict[str, Any] = {
        "type": "syndicated_finding",
        "case_key": bundle.get("case_key", ""),
        "dispatch_id": bundle.get("dispatch_id", ""),
        "question": bundle.get("question", ""),
        "coverage_status": coerce_string(authored_frontmatter.get("coverage_status")),
        "market_implied_probability": derived["market_implied_probability"],
        "syndicated_probability_low": derived["syndicated_probability_low"],
        "syndicated_probability_high": derived["syndicated_probability_high"],
        "syndicated_probability_midpoint": derived["syndicated_probability_midpoint"],
        "edge_vs_market_pct_points": derived["edge_vs_market_pct_points"],
        "relation_to_market": derived["relation_to_market"],
        "edge_quality": derived["edge_quality"],
        "edge_independent_verification_quality": coerce_string(authored_frontmatter.get("edge_independent_verification_quality")),
        "compressed_toward_market_due_to_verification": coerce_string(authored_frontmatter.get("compressed_toward_market_due_to_verification")),
        "contract_ambiguity_level": coerce_string(authored_frontmatter.get("contract_ambiguity_level")),
        "contract_ambiguity_reason": coerce_string(authored_frontmatter.get("contract_ambiguity_reason")),
        "independently_verified_points": authored_frontmatter.get("independently_verified_points") or [],
        "verification_gap_summary": coerce_string(authored_frontmatter.get("verification_gap_summary")),
        "best_countercase_summary": coerce_string(authored_frontmatter.get("best_countercase_summary")),
        "main_reason_for_disagreement": coerce_string(authored_frontmatter.get("main_reason_for_disagreement")),
        "resolution_mechanics_summary": coerce_string(authored_frontmatter.get("resolution_mechanics_summary")),
        "freshness_sensitive": coerce_string(authored_frontmatter.get("freshness_sensitive")),
        "freshness_driver": coerce_string(authored_frontmatter.get("freshness_driver")),
        "decision_blockers": authored_frontmatter.get("decision_blockers") or [],
        "blockers_require_new_research": coerce_string(authored_frontmatter.get("blockers_require_new_research")),
        "disagreement_type": coerce_string(authored_frontmatter.get("disagreement_type")),
        "disagreement_intensity": coerce_string(authored_frontmatter.get("disagreement_intensity")),
        "synthesis_confidence_quality": coerce_string(authored_frontmatter.get("synthesis_confidence_quality")),
        "staleness_risk": coerce_string(authored_frontmatter.get("staleness_risk")),
        "next_checkpoint": coerce_string(authored_frontmatter.get("next_checkpoint")),
        "follow_up_needed": coerce_string(authored_frontmatter.get("follow_up_needed")),
    }
    ordered = OrderedDict()
    for key in DECISION_HEADER_ORDER:
        ordered[key] = merged.get(key, "")
    return ordered


def build_body(claim: str, sections: dict[str, Any]) -> str:
    lines = ["# Claim", "", (claim or DEFAULT_CLAIM).strip(), ""]
    for section in SECTION_ORDER:
        content = coerce_string(sections.get(section))
        if not content:
            continue
        lines.extend([f"## {section}", "", content.strip(), ""])
    return "\n".join(lines).rstrip() + "\n"


def default_output_path(bundle: dict[str, Any]) -> Path:
    return RESEARCH_CASES_ROOT / bundle["case_key"] / "researcher-analyses" / bundle["analysis_date"] / bundle["dispatch_id"] / "syndicated-finding.md"


def current_output_path(bundle: dict[str, Any]) -> Path:
    return case_synthesis_markdown_path_for(bundle["case_key"])


def write_markdown(path: Path, frontmatter: OrderedDict[str, Any], body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_frontmatter(frontmatter, body))


def main() -> None:
    args = parse_args()
    bundle_path = Path(args.bundle_json)
    result_path = Path(args.result_json)
    if not bundle_path.is_absolute():
        bundle_path = WORKSPACE_ROOT / bundle_path
    if not result_path.is_absolute():
        result_path = WORKSPACE_ROOT / result_path

    bundle = load_json(bundle_path)
    result = load_json(result_path)
    validation = validate_synthesis_result_payload(result)
    if not validation["ok"]:
        print(json.dumps({
            "ok": False,
            "bundle_json": relative_to_workspace(bundle_path),
            "result_json": relative_to_workspace(result_path),
            "errors": validation["errors"],
            "warnings": validation["warnings"],
        }, indent=2 if args.pretty else None))
        raise SystemExit(1)

    authored_frontmatter = result.get("frontmatter") or {}
    sections = result.get("sections") or {}
    claim = coerce_string(result.get("claim"))

    warnings = list(validation["warnings"])
    frontmatter = build_frontmatter(bundle, authored_frontmatter)
    body = build_body(claim, sections)

    out_path = Path(args.out) if args.out else default_output_path(bundle)
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    write_markdown(out_path, frontmatter, body)

    current_path = None
    if args.write_current:
        current_path = current_output_path(bundle)
        write_markdown(current_path, frontmatter, body)

    summary = {
        "ok": True,
        "bundle_json": relative_to_workspace(bundle_path),
        "result_json": relative_to_workspace(result_path),
        "artifact_path": relative_to_workspace(out_path),
        "current_artifact_path": relative_to_workspace(current_path) if current_path else "",
        "warnings": warnings,
    }
    print(json.dumps(summary, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
