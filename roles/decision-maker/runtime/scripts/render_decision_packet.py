#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import (  # noqa: E402
    CASE_DECISION_PACKET_JSON_RELATIVE,
    DECISION_PACKET_FRONTMATTER_ORDER,
    WORKSPACE_ROOT,
    case_decision_packet_json_path,
    case_decision_packet_markdown_path,
    coerce_string,
    dump_frontmatter,
    load_json,
    relative_to_workspace,
)
from validation import validate_decision_packet_payload  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render the canonical markdown decision packet from JSON payload")
    parser.add_argument("--packet-json", required=True)
    parser.add_argument("--out")
    parser.add_argument("--write-current", action="store_true")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def ordered_frontmatter(packet: dict[str, Any]) -> OrderedDict[str, Any]:
    context = packet.get("context") or {}
    decision = packet.get("decision") or {}
    valuation = packet.get("valuation") or {}
    execution = packet.get("execution_semantics") or {}
    risk = packet.get("risk_controls") or {}
    epistemic = packet.get("epistemic_status") or {}
    values = {
        "type": "decision_packet",
        "case_key": context.get("case_key", ""),
        "dispatch_id": context.get("dispatch_id", ""),
        "question": context.get("question", ""),
        "market_id": context.get("market_id", ""),
        "market_title": context.get("market_title", ""),
        "source_decision_handoff_path": context.get("source_decision_handoff_path", ""),
        "source_syndicated_finding_path": context.get("source_syndicated_finding_path", ""),
        "recommended_side": (decision.get("side") or "").upper(),
        "trade_authorization": decision.get("trade_authorization", ""),
        "position_policy": decision.get("position_policy", ""),
        "decision_readiness": decision.get("decision_readiness", ""),
        "fair_value_low": valuation.get("fair_value_low", ""),
        "fair_value_high": valuation.get("fair_value_high", ""),
        "fair_value_mid": valuation.get("fair_value_mid", ""),
        "market_reference_price": valuation.get("market_reference_price", ""),
        "edge_mid_vs_market_pct_points": valuation.get("edge_mid_vs_market_pct_points", ""),
        "independent_verification_quality": valuation.get("independent_verification_quality", ""),
        "compressed_toward_market_applied": valuation.get("compressed_toward_market_applied", ""),
        "decision_confidence": risk.get("confidence_level", ""),
        "valid_until": execution.get("valid_until", ""),
        "tags": [],
    }
    ordered = OrderedDict()
    for key in DECISION_PACKET_FRONTMATTER_ORDER:
        ordered[key] = values.get(key, "")
    return ordered


def section_list(items: list[str]) -> list[str]:
    if not items:
        return ["- "]
    return [f"- {item}" for item in items]


def build_body(packet: dict[str, Any]) -> str:
    context = packet.get("context") or {}
    decision = packet.get("decision") or {}
    valuation = packet.get("valuation") or {}
    execution = packet.get("execution_semantics") or {}
    risk = packet.get("risk_controls") or {}
    invalidation = packet.get("invalidation") or {}
    epistemic = packet.get("epistemic_status") or {}
    audit = packet.get("audit") or {}
    bands = packet.get("bands") or []

    lines: list[str] = []
    lines.extend([
        "# Decision packet",
        "",
        "Use this template for the Decision-Maker's final executable recommendation after reviewing synthesis.",
        "",
        "Pipeline position:",
        "- upstream = researcher swarm -> synthesis -> `decision-handoff.md`",
        "- this artifact = Decision-Maker's final commitment object",
        "- downstream = isolated execution, accounting, evaluator, retrospective review",
        "",
        "Canonical machine-readable contract:",
        f"- `{CASE_DECISION_PACKET_JSON_RELATIVE}`",
        "",
        "## Decision summary",
        "",
        f"- Side: `{(decision.get('side') or '').upper()}`",
        f"- Trade authorization: `{decision.get('trade_authorization', '')}`",
        f"- Position policy: `{decision.get('position_policy', '')}`",
        f"- Decision readiness: `{decision.get('decision_readiness', '')}`",
        f"- Primary crux: {decision.get('primary_crux', '')}",
        f"- One-sentence rationale: {audit.get('one_sentence_rationale', '')}",
        "",
        "## Why this is the right action / no-action call",
        "",
        audit.get("notes", "") or "No additional notes provided.",
        "",
        "## Valuation",
        "",
        f"- Fair value low: {valuation.get('fair_value_low', '')}",
        f"- Fair value high: {valuation.get('fair_value_high', '')}",
        f"- Fair value midpoint: {valuation.get('fair_value_mid', '')}",
        f"- Market reference price: {valuation.get('market_reference_price', '')}",
        f"- Edge vs market (percentage points): {valuation.get('edge_mid_vs_market_pct_points', '')}",
        f"- Independent verification quality: `{valuation.get('independent_verification_quality', '')}`",
        f"- Compressed toward market applied: `{str(valuation.get('compressed_toward_market_applied', '')).lower()}`",
        f"- Compression reason: {valuation.get('compression_reason', '')}",
        "",
        "## Action bands",
        "",
        "Define deterministic bands on the market-implied true-probability axis.",
        "",
    ])
    for band in bands:
        lines.extend([
            f"- `{band.get('name', '')}`",
            f"  - `min_p:` {band.get('min_p', '')}",
            f"  - `max_p:` {band.get('max_p', '')}",
            f"  - `target_exposure_fraction:` {band.get('target_exposure_fraction', '')}",
            f"  - `notes:` {band.get('notes', '')}",
        ])
    lines.extend([
        "",
        "## Execution semantics",
        "",
        f"- Price axis: `{execution.get('price_axis', '')}`",
        f"- Price source: `{execution.get('price_source', '')}`",
        f"- Rebalance threshold fraction: {execution.get('rebalance_threshold_fraction', '')}",
        f"- Allow auto reversal: `{str(execution.get('allow_auto_reversal', '')).lower()}`",
        f"- Quote staleness seconds: {execution.get('quote_staleness_seconds', '')}",
        f"- Valid until: {execution.get('valid_until', '')}",
        f"- Time horizon: {execution.get('time_horizon', '')}",
        "",
        "## Risk controls",
        "",
        f"- Max position size (% bankroll): {risk.get('max_position_size_pct_bankroll', '')}",
        f"- Max additional exposure (% bankroll): {risk.get('max_additional_exposure_pct_bankroll', '')}",
        f"- Max single order (% bankroll): {risk.get('max_single_order_pct_bankroll', '')}",
        f"- Slippage tolerance (bps): {risk.get('slippage_tolerance_bps', '')}",
        f"- Liquidity minimum depth: {risk.get('liquidity_min_depth', '')}",
        f"- Correlation bucket limit (% bankroll): {risk.get('correlation_bucket_limit_pct_bankroll', '')}",
        f"- Confidence level: `{risk.get('confidence_level', '')}`",
        f"- Portfolio constraints: {', '.join(risk.get('portfolio_constraints', [])) if risk.get('portfolio_constraints') else ''}",
        "",
        "## Invalidation",
        "",
        "### Thesis breakers",
        *section_list(invalidation.get("thesis_breakers", [])),
        "",
        "### Market structure breakers",
        *section_list(invalidation.get("market_structure_breakers", [])),
        "",
        "### Time breakers",
        *section_list(invalidation.get("time_breakers", [])),
        "",
        "### Reversal conditions",
        *section_list(invalidation.get("reversal_conditions", [])),
        "",
        "## Epistemic status",
        "",
        "### Key uncertainties",
        *section_list(epistemic.get("key_uncertainties", [])),
        "",
        "### Reasons to pass / stay small",
        *section_list(epistemic.get("reasons_to_pass", [])),
        "",
        "### What would change my mind",
        *section_list(epistemic.get("what_would_change_my_mind", [])),
        "",
        "### Decision quality",
        f"- `{epistemic.get('decision_quality', '')}`",
        "",
        "## Audit checks",
        "",
        f"- Market baseline respected: `{str(audit.get('market_baseline_respected', '')).lower()}`",
        f"- Action bias check passed: `{str(audit.get('action_bias_check_passed', '')).lower()}`",
        f"- Self-preservation bias check passed: `{str(audit.get('self_preservation_bias_check_passed', '')).lower()}`",
        f"- Additional notes: {audit.get('notes', '')}",
        "",
        "## Notes for downstream evaluator",
        "",
        coerce_string(decision.get("primary_crux")) or "No evaluator note provided.",
        "",
    ])
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    packet_path = Path(args.packet_json)
    if not packet_path.is_absolute():
        packet_path = WORKSPACE_ROOT / packet_path
    packet = load_json(packet_path)
    validation = validate_decision_packet_payload(packet)
    if not validation["ok"]:
        print(json.dumps({
            "ok": False,
            "packet_json": relative_to_workspace(packet_path),
            "errors": validation["errors"],
            "warnings": validation["warnings"],
        }, indent=2 if args.pretty else None))
        raise SystemExit(1)

    case_key = coerce_string((packet.get("context") or {}).get("case_key"))
    out_path = Path(args.out) if args.out else case_decision_packet_markdown_path(case_key)
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(dump_frontmatter(ordered_frontmatter(packet), build_body(packet)))

    current_json_path = None
    if args.write_current:
        current_json_path = case_decision_packet_json_path(case_key)

    print(json.dumps({
        "ok": True,
        "packet_json": relative_to_workspace(packet_path),
        "decision_packet_path": relative_to_workspace(out_path),
        "current_decision_packet_json_path": relative_to_workspace(current_json_path) if current_json_path else "",
        "warnings": validation["warnings"],
    }, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
