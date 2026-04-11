#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    case_decision_handoff_path_for,
    coerce_string,
    derive_syndicated_fields,
    dump_frontmatter,
    load_json,
    relative_to_workspace,
)
from validation import validate_synthesis_result_payload  # noqa: E402

FRONTMATTER_ORDER = [
    "type",
    "case_key",
    "dispatch_id",
    "question",
    "source_syndicated_finding_path",
    "market_implied_probability",
    "syndicated_probability_low",
    "syndicated_probability_high",
    "syndicated_probability_midpoint",
    "relation_to_market",
    "edge_quality",
    "edge_independent_verification_quality",
    "compressed_toward_market_due_to_verification",
    "contract_ambiguity_level",
    "contract_ambiguity_reason",
    "independently_verified_points",
    "verification_gap_summary",
    "best_countercase_summary",
    "main_reason_for_disagreement",
    "resolution_mechanics_summary",
    "freshness_sensitive",
    "freshness_driver",
    "decision_blockers",
    "blockers_require_new_research",
    "disagreement_type",
    "follow_up_needed",
]

BODY_SECTION_MAP = [
    ("Decision summary", None),
    ("Why this may matter now", "Alpha summary"),
    ("Shift versus swarm baseline", "Difference from swarm-implied center"),
    ("Edge verification status", "Independent verification of edge"),
    ("Compression toward market", "Compression toward market due to verification"),
    ("Timing and catalyst posture", "Timing and catalyst posture"),
    ("Key blockers", "Decision blockers"),
    ("Best countercase", "Best countercase"),
    ("What would change the view", "What would falsify this interpretation / change the view"),
    ("Recommended next action", "Recommended follow-up"),
    ("Verification impact", "Verification impact"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a decision-maker handoff markdown artifact from synthesis output")
    parser.add_argument("--bundle-json", required=True)
    parser.add_argument("--result-json", required=True)
    parser.add_argument("--syndicated-artifact-path", required=True)
    parser.add_argument("--out", help="Optional explicit output markdown path")
    parser.add_argument("--write-current", action="store_true", help="Also write the canonical case-level handoff under cases/<case-key>/synthesizer-agent/")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def default_output_path(bundle: dict) -> Path:
    return (
        WORKSPACE_ROOT
        / "qualitative-db"
        / "40-research"
        / "cases"
        / bundle["case_key"]
        / "researcher-analyses"
        / bundle["analysis_date"]
        / bundle["dispatch_id"]
        / "decision-handoff.md"
    )


def build_frontmatter(bundle: dict, result: dict, syndicated_artifact_path: Path) -> OrderedDict[str, object]:
    authored_frontmatter = result.get("frontmatter") or {}
    derived = derive_syndicated_fields(
        market_implied_probability=bundle.get("market_implied_probability"),
        low=authored_frontmatter.get("syndicated_probability_low"),
        high=authored_frontmatter.get("syndicated_probability_high"),
    )
    values = {
        "type": "synthesis_decision_handoff",
        "case_key": bundle.get("case_key", ""),
        "dispatch_id": bundle.get("dispatch_id", ""),
        "question": bundle.get("question", ""),
        "source_syndicated_finding_path": relative_to_workspace(syndicated_artifact_path),
        "market_implied_probability": derived.get("market_implied_probability"),
        "syndicated_probability_low": derived.get("syndicated_probability_low"),
        "syndicated_probability_high": derived.get("syndicated_probability_high"),
        "syndicated_probability_midpoint": derived.get("syndicated_probability_midpoint"),
        "relation_to_market": derived.get("relation_to_market"),
        "edge_quality": derived.get("edge_quality"),
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
        "follow_up_needed": coerce_string(authored_frontmatter.get("follow_up_needed")),
    }
    ordered = OrderedDict()
    for key in FRONTMATTER_ORDER:
        ordered[key] = values.get(key, "")
    return ordered


def build_body(result: dict) -> str:
    sections = result.get("sections") or {}
    claim = coerce_string(result.get("claim")) or "No synthesized claim provided."
    lines: list[str] = []
    for output_heading, source_heading in BODY_SECTION_MAP:
        lines.append(f"# {output_heading}" if not lines else f"## {output_heading}")
        lines.append("")
        if source_heading is None:
            lines.append(claim.strip())
        else:
            content = coerce_string(sections.get(source_heading))
            lines.append(content.strip() if content.strip() else "No additional content provided.")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_markdown(path: Path, frontmatter: OrderedDict[str, object], body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_frontmatter(frontmatter, body))


def main() -> None:
    args = parse_args()
    bundle_path = Path(args.bundle_json)
    result_path = Path(args.result_json)
    syndicated_artifact_path = Path(args.syndicated_artifact_path)
    if not bundle_path.is_absolute():
        bundle_path = WORKSPACE_ROOT / bundle_path
    if not result_path.is_absolute():
        result_path = WORKSPACE_ROOT / result_path
    if not syndicated_artifact_path.is_absolute():
        syndicated_artifact_path = WORKSPACE_ROOT / syndicated_artifact_path

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

    frontmatter = build_frontmatter(bundle, result, syndicated_artifact_path)
    body = build_body(result)

    out_path = Path(args.out) if args.out else default_output_path(bundle)
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    write_markdown(out_path, frontmatter, body)

    current_path = None
    if args.write_current:
        current_path = case_decision_handoff_path_for(bundle["case_key"])
        write_markdown(current_path, frontmatter, body)

    print(json.dumps({
        "ok": True,
        "bundle_json": relative_to_workspace(bundle_path),
        "result_json": relative_to_workspace(result_path),
        "syndicated_artifact_path": relative_to_workspace(syndicated_artifact_path),
        "decision_handoff_path": relative_to_workspace(out_path),
        "current_decision_handoff_path": relative_to_workspace(current_path) if current_path else "",
        "warnings": validation["warnings"],
    }, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
