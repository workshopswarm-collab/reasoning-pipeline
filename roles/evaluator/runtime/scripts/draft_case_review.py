#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.io import read_json  # noqa: E402
from lib.paths import case_review_markdown_path, ensure_parent, learning_packet_path  # noqa: E402


def _yaml_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return str(value)


def _yaml_list(items: list[str]) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(items) + "]"


def build_review_markdown(packet: dict[str, Any]) -> str:
    case_key = packet.get("case_key") or ""
    market_truth = packet.get("market_truth") or {}
    decision_summary = packet.get("decision_summary") or {}
    belief = packet.get("belief_evolution") or {}
    research = packet.get("research_summary") or {}
    forecast_summary = packet.get("forecast_summary") or {}
    warnings = packet.get("warnings") or []
    event_timeline = ((packet.get("event_timeline") or {}).get("events") or [])[:7]
    high_signal = []
    misleading = []
    missing = []

    for persona in research.get("persona_runs") or []:
        supports = persona.get("strongest_supports") or []
        disconfirmers = persona.get("strongest_disconfirmers") or []
        if supports:
            high_signal.append(f"{persona.get('persona')}: {supports[0]}")
        if disconfirmers:
            misleading.append(f"{persona.get('persona')}: {disconfirmers[0]}")

    if warnings:
        missing.append("Packet warnings indicate the evaluator bridge is still incomplete: " + ", ".join(warnings))
    if market_truth.get("resolution_status") != "resolved":
        missing.append("Case is not yet fully resolved in the quant truth layer, so this review remains a draft rather than a final resolved-case judgment.")
    if market_truth.get("resolved_value") is None:
        missing.append("Structured resolution outcome and score are not yet fully populated into the learning packet.")
    if forecast_summary.get("latest_brier_component") is None:
        missing.append("Per-case scoring is still sparse or unavailable; evaluator follow-up should confirm the final score path.")

    tags = [
        "learning/case_review",
        "evaluator/draft",
        f"platform/{packet.get('platform') or 'unknown'}",
    ]

    header = f"""---
type: learning_note
learning_type: case_review
learning_scope: resolved_case
case_key: {case_key}
market_category: {_yaml_value(packet.get('category'))}
domain: 
subdomain: 
entity: 
topic: 
question: { _yaml_value(packet.get('title')) }
date_created: 
resolution_date: {_yaml_value(packet.get('resolved_at'))}
evaluation_scope: resolved_case
evaluation_target: pipeline_case
outcome_observed: {_yaml_value(market_truth.get('resolved_value'))}
decision_taken: {_yaml_value(decision_summary.get('trade_authorization') or decision_summary.get('side'))}
error_pattern: {'resolved_case_review_pending' if market_truth.get('resolution_status') == 'resolved' else 'settlement_or_path_review_pending'}
intervention_status: candidate
related_entities: []
related_drivers: []
upstream_inputs: {_yaml_list([repr(path) for path in [packet.get('provenance_paths', {}).get('case_markdown'), packet.get('provenance_paths', {}).get('decision_packet_json'), packet.get('provenance_paths', {}).get('synthesis_runtime_json')] if path])}
downstream_uses: []
promotion_candidates: []
tags: {_yaml_list([repr(tag) for tag in tags])}
---
"""

    def render_bullets(items: list[str], fallback: str) -> str:
        if not items:
            return f"- {fallback}"
        return "\n".join(f"- {item}" for item in items)

    timeline_excerpt = render_bullets([
        f"{item.get('ts') or 'unknown-time'} — {item.get('summary')}" for item in event_timeline
    ], "No structured timeline events captured yet.")

    body = f"""
# Learning Note

## What was being evaluated

- Case: `{case_key}`
- Question: {packet.get('title') or 'Unknown question'}
- Platform: {packet.get('platform') or 'unknown'}
- Current case status: {packet.get('case_status') or 'unknown'}
- Resolution status: {market_truth.get('resolution_status') or 'unknown'}

## What the pipeline believed or did

- Decision side: {decision_summary.get('side') or 'unknown'}
- Trade authorization: {decision_summary.get('trade_authorization') or 'unknown'}
- Position policy: {decision_summary.get('position_policy') or 'unknown'}
- Decision fair value mid: {belief.get('decision_fair_value_mid')}
- Market reference price at decision: {belief.get('market_reference_price')}
- Primary crux: {decision_summary.get('primary_crux') or 'No primary crux captured.'}

## What happened in reality

- Resolution status in packet: {market_truth.get('resolution_status') or 'unknown'}
- Resolved outcome: {market_truth.get('resolved_outcome')}
- Resolved value: {market_truth.get('resolved_value')}
- Resolved at: {packet.get('resolved_at')}
- This draft is based on the evaluator bridge packet combining qualitative provenance and quant truth.

## Outcome and scoring evidence

- Persona probability range: {belief.get('persona_probability_min')} to {belief.get('persona_probability_max')}
- Initial forecast probability: {forecast_summary.get('initial_forecast_prob')}
- Latest forecast probability: {forecast_summary.get('latest_forecast_prob')}
- Initial Brier component: {forecast_summary.get('initial_brier_component')}
- Latest Brier component: {forecast_summary.get('latest_brier_component')}
- Decision fair value range: {belief.get('decision_fair_value_low')} to {belief.get('decision_fair_value_high')}
- Market reference price: {belief.get('market_reference_price')}
- Edge mid vs market pct points: {belief.get('edge_mid_vs_market_pct_points')}
- Timeline excerpt:
{timeline_excerpt}

## Which inputs were high signal

{render_bullets(high_signal, 'High-signal inputs still need evaluator review after resolution.')}

## Which inputs were misleading

{render_bullets(misleading, 'Misleading inputs cannot be classified confidently until resolution and scoring are populated.')}

## What was missing

{render_bullets(missing, 'No obvious missing inputs recorded yet.')}

## Error-pattern classification

- Initial draft classification: settlement_or_path_review_pending
- This should be updated after structured resolution outcome and score are available.

## Driver and mechanism takeaways

- Keep source-of-truth mechanics and path dependence separate from generic directional thesis quality.
- Use this note to evaluate whether threshold-touch / settlement-mechanics logic materially influenced the case.

## Source / input / workflow takeaways

- Persona sidecars appear available and usable for structured evaluator extraction.
- The learning packet bridge is now sufficient for a first-pass review, but still needs richer structured market-path and resolution ingestion.

## Proposed intervention or hold decision

- If quant truth is present, compare the initial/latest forecast path against the resolved value before deciding whether the miss was directional, calibration-related, timing-related, or execution-policy-related.
- Decide whether a verification-rule, retrieval-rule, or workflow guardrail intervention is warranted.

## Promotion candidates for stable layers

- None yet. Promotion should wait for reviewed resolved-case evidence.

## How this should be reused later

- Re-open this note after resolution and scoring data are populated.
- Use it as the evaluator-facing bridge between upstream provenance, decision behavior, and future intervention candidates.
""".strip() + "\n"

    return header + "\n" + body


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Draft a markdown evaluator case review from a learning packet")
    parser.add_argument("--case-key")
    parser.add_argument("--packet")
    parser.add_argument("--out")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.packet and not args.case_key:
        raise SystemExit("Provide --packet or --case-key")
    packet_path = Path(args.packet) if args.packet else learning_packet_path(args.case_key)
    packet = read_json(packet_path)
    if not isinstance(packet, dict):
        raise SystemExit(f"Could not load learning packet: {packet_path}")
    case_key = packet.get("case_key") or args.case_key
    out_path = Path(args.out) if args.out else case_review_markdown_path(case_key)
    ensure_parent(out_path)
    out_path.write_text(build_review_markdown(packet), encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
