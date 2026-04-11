#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    coerce_string,
    load_json,
    load_markdown_frontmatter,
    relative_to_workspace,
    write_json,
)

DEFAULT_SNIPPET_CHARS = 1600
SUPPORTING_NOTE_CHARS = 1000
PRIMARY_STRUCTURED_HANDOFF_FIELDS = [
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
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Select a compact deterministic Decision-Maker input bundle")
    parser.add_argument("--decision-context-json", required=True)
    parser.add_argument("--verification-mode-json", required=True)
    parser.add_argument("--out")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def default_output_path(context_path: Path, dispatch_id: str) -> Path:
    return context_path.with_name(f"selected-inputs-{dispatch_id or context_path.stem}.json")


def resolve_path(path_str: str) -> Path | None:
    if not path_str:
        return None
    path = Path(path_str)
    if not path.is_absolute():
        path = WORKSPACE_ROOT / path
    return path


def strip_frontmatter_and_compact(text: str) -> str:
    if text.startswith("---\n"):
        lines = text.splitlines(keepends=True)
        for i in range(1, len(lines)):
            if lines[i].rstrip("\n") == "---":
                text = "".join(lines[i + 1 :])
                break
    return "\n".join(line.rstrip() for line in text.strip().splitlines() if line.strip())


def read_snippet(path_str: str, *, max_chars: int) -> dict[str, Any] | None:
    path = resolve_path(path_str)
    if path is None or not path.exists():
        return None
    try:
        frontmatter, body = load_markdown_frontmatter(path)
        text = strip_frontmatter_and_compact(body)
    except Exception:
        text = strip_frontmatter_and_compact(path.read_text())
        frontmatter = {}
    snippet = text[:max_chars].strip()
    if len(text) > max_chars:
        snippet += " …"
    return {
        "path": relative_to_workspace(path),
        "frontmatter": dict(frontmatter) if isinstance(frontmatter, dict) else {},
        "snippet": snippet,
        "full_char_count": len(text),
        "snippet_char_count": len(snippet),
    }


def sidecar_score(item: dict[str, Any]) -> tuple[int, float, str]:
    payload = item.get("payload") or {}
    weight = 2 if coerce_string(payload.get("recommended_weight")) == "high" else 1
    prob = float(payload.get("own_probability")) if isinstance(payload.get("own_probability"), (int, float)) else 0.5
    persona = coerce_string(item.get("persona") or payload.get("persona"))
    persona_priority = 0
    if persona == "market-implied":
        persona_priority = 2
    elif persona == "risk-manager":
        persona_priority = 1
    return (weight + persona_priority, prob, persona)


def unique_persona_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for item in items:
        persona = coerce_string(item.get("persona") or (item.get("payload") or {}).get("persona"))
        if not persona or persona in seen:
            continue
        seen.add(persona)
        out.append(item)
    return out


def choose_sidecars(sidecars: list[dict[str, Any]], context: dict[str, Any], mode_payload: dict[str, Any]) -> list[dict[str, Any]]:
    if not sidecars:
        return []
    budget = ((mode_payload.get("budgets") or {}).get("persona_sidecars_max")) or 2
    relation = coerce_string(((context.get("upstream") or {}).get("relation_to_market")))

    sorted_by_prob = sorted(sidecars, key=lambda s: float(((s.get("payload") or {}).get("own_probability")) or 0.5))
    selected: list[dict[str, Any]] = []

    market_implied = next((s for s in sidecars if coerce_string(s.get("persona") or (s.get("payload") or {}).get("persona")) == "market-implied"), None)
    if market_implied is not None:
        selected.append(market_implied)

    if relation == "below_market":
        selected.append(sorted_by_prob[0])
        selected.append(sorted_by_prob[-1])
    elif relation == "above_market":
        selected.append(sorted_by_prob[-1])
        selected.append(sorted_by_prob[0])
    else:
        mid = (context.get("upstream") or {}).get("syndicated_probability_midpoint")
        if not isinstance(mid, (int, float)):
            mid = 0.5
        closest = min(sidecars, key=lambda s: abs(float(((s.get("payload") or {}).get("own_probability")) or 0.5) - float(mid)))
        farthest = max(sidecars, key=lambda s: abs(float(((s.get("payload") or {}).get("own_probability")) or 0.5) - float(mid)))
        selected.extend([closest, farthest])

    selected = unique_persona_items(selected)
    if len(selected) < budget:
        remaining = [s for s in sorted(sidecars, key=sidecar_score, reverse=True) if coerce_string(s.get("persona") or (s.get("payload") or {}).get("persona")) not in {coerce_string(x.get("persona") or (x.get("payload") or {}).get("persona")) for x in selected}]
        selected.extend(remaining[: max(0, budget - len(selected))])
    return selected[:budget]


def persona_summary(sidecar: dict[str, Any]) -> dict[str, Any]:
    payload = sidecar.get("payload") or {}
    return {
        "persona": coerce_string(sidecar.get("persona") or payload.get("persona")),
        "recommended_weight": coerce_string(payload.get("recommended_weight")),
        "own_probability": payload.get("own_probability"),
        "main_thesis": coerce_string(payload.get("main_thesis")),
        "main_logical_chain": list(payload.get("main_logical_chain") or [])[:4],
        "strongest_supports": list(payload.get("strongest_supports") or [])[:2],
        "strongest_disconfirmers": list(payload.get("strongest_disconfirmers") or [])[:2],
        "unresolved_ambiguities": list(payload.get("unresolved_ambiguities") or [])[:2],
        "what_would_change_view": coerce_string(payload.get("what_would_change_view")),
        "timing_relevance": coerce_string(payload.get("timing_relevance")),
        "source_quality_view": coerce_string(payload.get("source_quality_view")),
        "persona_finding_path": coerce_string(sidecar.get("persona_finding_path")),
        "assumption_artifact_paths": list(sidecar.get("assumption_artifact_paths") or []),
        "evidence_artifact_paths": list(sidecar.get("evidence_artifact_paths") or []),
    }


def choose_risk_focus_sidecar(selected: list[dict[str, Any]], context: dict[str, Any]) -> dict[str, Any] | None:
    if not selected:
        return None
    relation = coerce_string(((context.get("upstream") or {}).get("relation_to_market")))
    if relation == "below_market":
        return min(selected, key=lambda s: float(((s.get("payload") or {}).get("own_probability")) or 0.5))
    if relation == "above_market":
        return max(selected, key=lambda s: float(((s.get("payload") or {}).get("own_probability")) or 0.5))
    return max(selected, key=lambda s: len(((s.get("payload") or {}).get("strongest_disconfirmers")) or []))


def maybe_trim_bundle(payload: dict[str, Any], *, max_chars: int) -> dict[str, Any]:
    text = json.dumps(payload, ensure_ascii=False)
    if len(text) <= max_chars:
        payload.setdefault("bundle_budget", {})["actual_chars_after_trim"] = len(text)
        payload.setdefault("bundle_budget", {})["approx_tokens_after_trim"] = int(len(text) / 4)
        payload.setdefault("bundle_budget", {})["trim_applied"] = False
        return payload

    assumptions = payload.get("selected_assumption_snippets") or []
    evidence = payload.get("selected_evidence_snippets") or []
    support = payload.get("selected_supporting_note_snippets") or []

    if support:
        payload["selected_supporting_note_snippets"] = []
        text = json.dumps(payload, ensure_ascii=False)
    if len(text) > max_chars and evidence:
        payload["selected_evidence_snippets"] = []
        text = json.dumps(payload, ensure_ascii=False)
    if len(text) > max_chars and assumptions:
        payload["selected_assumption_snippets"] = []
        text = json.dumps(payload, ensure_ascii=False)
    if len(text) > max_chars:
        for summary in payload.get("selected_persona_sidecars", [])[1:]:
            summary["main_logical_chain"] = summary.get("main_logical_chain", [])[:2]
            summary["strongest_supports"] = summary.get("strongest_supports", [])[:1]
            summary["strongest_disconfirmers"] = summary.get("strongest_disconfirmers", [])[:1]
            summary["unresolved_ambiguities"] = summary.get("unresolved_ambiguities", [])[:1]
        text = json.dumps(payload, ensure_ascii=False)

    payload.setdefault("bundle_budget", {})["actual_chars_after_trim"] = len(text)
    payload.setdefault("bundle_budget", {})["approx_tokens_after_trim"] = int(len(text) / 4)
    payload.setdefault("bundle_budget", {})["trim_applied"] = True
    return payload


def has_meaningful_structured_handoff(upstream: dict[str, Any]) -> tuple[bool, list[str]]:
    missing: list[str] = []
    for field in PRIMARY_STRUCTURED_HANDOFF_FIELDS:
        value = upstream.get(field)
        if field == "independently_verified_points":
            if not isinstance(value, list) or not value:
                missing.append(field)
            continue
        if not coerce_string(value):
            missing.append(field)
    return (not missing, missing)


def valid_sidecar_bundle(path: Path | None) -> bool:
    if path is None or not path.exists():
        return False
    try:
        payload = load_json(path)
    except Exception:
        return False
    return (
        isinstance(payload, dict)
        and coerce_string(payload.get("artifact_type")) == "sidecar_synthesis_bundle"
        and isinstance(payload.get("sidecars"), list)
        and bool(payload.get("sidecars"))
    )


def resolve_sidecar_bundle_path(upstream: dict[str, Any]) -> Path | None:
    candidates: list[Path] = []
    explicit_path = resolve_path(coerce_string(upstream.get("sidecar_synthesis_bundle_path")))
    if explicit_path is not None:
        candidates.append(explicit_path)
        candidates.append(explicit_path.with_name("sidecar-synthesis-bundle.json"))
    synthesis_status_path = resolve_path(coerce_string(upstream.get("synthesis_stage_status_path")))
    if synthesis_status_path is not None:
        candidates.append(synthesis_status_path.with_name("sidecar-synthesis-bundle.json"))

    seen: set[str] = set()
    for candidate in candidates:
        key = str(candidate)
        if key in seen:
            continue
        seen.add(key)
        if valid_sidecar_bundle(candidate):
            return candidate
    return None


def main() -> None:
    args = parse_args()
    context_path = Path(args.decision_context_json)
    if not context_path.is_absolute():
        context_path = WORKSPACE_ROOT / context_path
    mode_path = Path(args.verification_mode_json)
    if not mode_path.is_absolute():
        mode_path = WORKSPACE_ROOT / mode_path

    context = load_json(context_path)
    mode_payload = load_json(mode_path)
    case_key = coerce_string(context.get("case_key"))
    dispatch_id = coerce_string(context.get("dispatch_id"))
    upstream = context.get("upstream") or {}
    market = context.get("market") or {}
    bundle_path = resolve_sidecar_bundle_path(upstream)
    sidecar_bundle = load_json(bundle_path) if bundle_path and bundle_path.exists() else {}
    sidecars = sidecar_bundle.get("sidecars") if isinstance(sidecar_bundle.get("sidecars"), list) else []

    selected_sidecars_raw = choose_sidecars(sidecars, context, mode_payload)
    selected_persona_sidecars = [persona_summary(item) for item in selected_sidecars_raw]
    risk_focus = choose_risk_focus_sidecar(selected_sidecars_raw, context)

    budgets = mode_payload.get("budgets") or {}
    selected_assumption_snippets: list[dict[str, Any]] = []
    selected_evidence_snippets: list[dict[str, Any]] = []
    selected_supporting_note_snippets: list[dict[str, Any]] = []

    if risk_focus is not None:
        for path_str in list(risk_focus.get("assumption_artifact_paths") or [])[: int(budgets.get("assumption_snippets_max", 0))]:
            snippet = read_snippet(path_str, max_chars=DEFAULT_SNIPPET_CHARS)
            if snippet:
                selected_assumption_snippets.append(snippet)
        for path_str in list(risk_focus.get("evidence_artifact_paths") or [])[: int(budgets.get("evidence_snippets_max", 0))]:
            snippet = read_snippet(path_str, max_chars=DEFAULT_SNIPPET_CHARS)
            if snippet:
                selected_evidence_snippets.append(snippet)

    structured_handoff_complete, missing_structured_fields = has_meaningful_structured_handoff(upstream)
    handoff_body = coerce_string((context.get("source_excerpt") or {}).get("decision_handoff_body"))
    include_prose_fallback = (not structured_handoff_complete) or coerce_string(mode_payload.get("mode")) == "targeted_escalation"
    if include_prose_fallback and int(budgets.get("supporting_note_snippets_max", 0)) > 0 and handoff_body:
        selected_supporting_note_snippets.append({
            "path": coerce_string(upstream.get("decision_handoff_path")),
            "label": "decision_handoff_body_excerpt",
            "snippet": handoff_body[:SUPPORTING_NOTE_CHARS].strip() + (" …" if len(handoff_body) > SUPPORTING_NOTE_CHARS else ""),
        })

    structured_handoff_primary = {
        "relation_to_market": coerce_string(upstream.get("relation_to_market")),
        "edge_quality": coerce_string(upstream.get("edge_quality")),
        "edge_independent_verification_quality": coerce_string(upstream.get("edge_independent_verification_quality")),
        "compressed_toward_market_due_to_verification": coerce_string(upstream.get("compressed_toward_market_due_to_verification")),
        "contract_ambiguity_level": coerce_string(upstream.get("contract_ambiguity_level")),
        "contract_ambiguity_reason": coerce_string(upstream.get("contract_ambiguity_reason")),
        "independently_verified_points": list(upstream.get("independently_verified_points") or []),
        "verification_gap_summary": coerce_string(upstream.get("verification_gap_summary")),
        "best_countercase_summary": coerce_string(upstream.get("best_countercase_summary")),
        "main_reason_for_disagreement": coerce_string(upstream.get("main_reason_for_disagreement")),
        "resolution_mechanics_summary": coerce_string(upstream.get("resolution_mechanics_summary")),
        "disagreement_intensity": coerce_string(upstream.get("disagreement_intensity")),
        "freshness_sensitive": coerce_string(upstream.get("freshness_sensitive")),
        "freshness_driver": coerce_string(upstream.get("freshness_driver")),
        "decision_blockers": list(upstream.get("decision_blockers") or []),
        "blockers_require_new_research": coerce_string(upstream.get("blockers_require_new_research")),
        "disagreement_type": coerce_string(upstream.get("disagreement_type")),
        "follow_up_needed": coerce_string(upstream.get("follow_up_needed")),
    }

    expected_nonzero_sidecars = bool(
        (int(upstream.get("ready_sidecar_count") or 0) > 0)
        or (int(upstream.get("sidecar_bundle_sidecar_count") or 0) > 0)
    )
    sidecar_guardrail_violation = expected_nonzero_sidecars and not selected_persona_sidecars

    mode = coerce_string(mode_payload.get("mode"))

    payload = {
        "artifact_type": "decision_selected_inputs",
        "schema_version": "decision-selected-inputs/v1",
        "case_key": case_key,
        "dispatch_id": dispatch_id,
        "verification_mode": mode_payload.get("mode"),
        "verification_triggers": mode_payload.get("triggers", []),
        "core_case": {
            "question": coerce_string(context.get("question")),
            "market_title": coerce_string(market.get("market_title")),
            "market_reference_price": market.get("market_reference_price"),
            "market_quote_timestamp": coerce_string(market.get("quote_timestamp")),
            "syndicated_probability_low": upstream.get("syndicated_probability_low"),
            "syndicated_probability_high": upstream.get("syndicated_probability_high"),
            "syndicated_probability_midpoint": upstream.get("syndicated_probability_midpoint"),
            "edge_mid_vs_market_pct_points": upstream.get("edge_mid_vs_market_pct_points"),
            "relation_to_market": coerce_string(upstream.get("relation_to_market")),
            "edge_independent_verification_quality": coerce_string(upstream.get("edge_independent_verification_quality")),
            "contract_ambiguity_level": coerce_string(upstream.get("contract_ambiguity_level")),
            "contract_ambiguity_reason": coerce_string(upstream.get("contract_ambiguity_reason")),
            "freshness_sensitive": coerce_string(upstream.get("freshness_sensitive")),
            "freshness_driver": coerce_string(upstream.get("freshness_driver")),
            "decision_blockers": list(upstream.get("decision_blockers") or []),
            "blockers_require_new_research": coerce_string(upstream.get("blockers_require_new_research")),
            "disagreement_type": coerce_string(upstream.get("disagreement_type")),
            "follow_up_needed": coerce_string(upstream.get("follow_up_needed")),
        },
        "required_upstream_inputs": {
            "decision_handoff_path": coerce_string(upstream.get("decision_handoff_path")),
            "syndicated_runtime_path": coerce_string(upstream.get("syndicated_runtime_path")),
            "syndicated_finding_path": coerce_string(upstream.get("syndicated_finding_path")),
            "sidecar_synthesis_bundle_path": relative_to_workspace(bundle_path) if bundle_path else "",
            "synthesis_sidecar_readiness": {
                "ready_sidecar_count": int(upstream.get("ready_sidecar_count") or 0),
                "pending_sidecar_count": int(upstream.get("pending_sidecar_count") or 0),
                "sidecar_bundle_sidecar_count": int(upstream.get("sidecar_bundle_sidecar_count") or 0),
                "sidecar_bundle_coverage_status": coerce_string(upstream.get("sidecar_bundle_coverage_status")),
            },
            "syndicated_runtime_summary": {
                "artifact_type": coerce_string(((context.get("source_excerpt") or {}).get("syndicated_runtime", {}) or {}).get("artifact_type")),
                "market_snapshot_time": coerce_string(((context.get("source_excerpt") or {}).get("syndicated_runtime", {}) or {}).get("market_snapshot_time")),
                "source_persona_count": ((context.get("source_excerpt") or {}).get("syndicated_runtime", {}) or {}).get("source_persona_count"),
                "supporting_artifact_count": ((context.get("source_excerpt") or {}).get("syndicated_runtime", {}) or {}).get("supporting_artifact_count"),
            },
        },
        "structured_handoff_primary": structured_handoff_primary,
        "structured_handoff_policy": {
            "structured_handoff_is_primary_starting_point": True,
            "prose_is_fallback_only": True,
            "structured_handoff_complete": structured_handoff_complete,
            "missing_structured_fields": missing_structured_fields,
        },
        "verification_enforcement": {
            "agent_tool_use_allowed": mode == "targeted_escalation",
            "allowed_agent_tools": ["web_search", "web_fetch"] if mode == "targeted_escalation" else [],
            "enforcement_method": "session_message_inspection",
            "violation_action": "fail_run",
            "rationale": (
                "Decision-Maker may perform bounded independent source discovery/search during targeted escalation, but only within runtime-enforced tool/query/fetch budgets."
                if mode == "targeted_escalation"
                else "Decision-Maker should use the deterministic selected-input bundle as its verification boundary; additional agent-side tool use is disallowed in this mode."
            ),
        },
        "verification_budget": {
            "search_queries_allowed": int((mode_payload.get("budgets") or {}).get("search_queries_allowed", 0)),
            "source_fetches_allowed": int((mode_payload.get("budgets") or {}).get("source_fetches_allowed", 0)),
            "minimum_distinct_source_families": int((mode_payload.get("budgets") or {}).get("minimum_distinct_source_families", 0)),
            "preferred_distinct_source_families": int((mode_payload.get("budgets") or {}).get("preferred_distinct_source_families", 0)),
        },
        "prose_fallback": {
            "included": include_prose_fallback,
            "reason": "missing_structured_handoff_fields" if not structured_handoff_complete else ("targeted_escalation_context" if include_prose_fallback else "not_included"),
            "decision_handoff_excerpt": (handoff_body[:1200].strip() + (" …" if len(handoff_body) > 1200 else "")) if include_prose_fallback and handoff_body else "",
        },
        "selected_persona_sidecars": selected_persona_sidecars,
        "selected_assumption_snippets": selected_assumption_snippets,
        "selected_evidence_snippets": selected_evidence_snippets,
        "selected_supporting_note_snippets": selected_supporting_note_snippets,
        "bundle_budget": {
            "max_chars": int(budgets.get("max_selected_bundle_chars", 12000)),
            "approx_tokens_before_trim": 0,
            "approx_tokens_after_trim": 0,
            "actual_chars_before_trim": 0,
            "actual_chars_after_trim": 0,
            "trim_applied": False,
        },
        "enforcement_summary": {
            "full_case_tree_excluded": True,
            "full_persona_markdown_excluded": True,
            "unbounded_research_excluded_from_default_bundle": True,
            "structured_handoff_primary_enforced": True,
            "prose_fallback_only": True,
            "agent_tool_use_allowed": mode == "targeted_escalation",
            "selected_persona_count": len(selected_persona_sidecars),
            "selected_assumption_count": len(selected_assumption_snippets),
            "selected_evidence_count": len(selected_evidence_snippets),
            "selected_supporting_note_count": len(selected_supporting_note_snippets),
        },
        "sidecar_selection_guardrail": {
            "expected_nonzero_sidecars": expected_nonzero_sidecars,
            "violation": sidecar_guardrail_violation,
            "message": "Synthesis indicated ready structured sidecars but Decision-Maker resolved zero selected persona sidecars." if sidecar_guardrail_violation else "",
            "resolved_sidecar_bundle_path": relative_to_workspace(bundle_path) if bundle_path else "",
            "resolved_sidecar_bundle_sidecar_count": len(sidecars),
            "selected_persona_count": len(selected_persona_sidecars),
        },
    }

    payload["bundle_budget"]["actual_chars_before_trim"] = len(json.dumps(payload, ensure_ascii=False))
    payload["bundle_budget"]["approx_tokens_before_trim"] = int(payload["bundle_budget"]["actual_chars_before_trim"] / 4)
    payload = maybe_trim_bundle(payload, max_chars=int(payload["bundle_budget"]["max_chars"]))
    payload["enforcement_summary"]["selected_persona_count"] = len(payload.get("selected_persona_sidecars", []))
    payload["enforcement_summary"]["selected_assumption_count"] = len(payload.get("selected_assumption_snippets", []))
    payload["enforcement_summary"]["selected_evidence_count"] = len(payload.get("selected_evidence_snippets", []))
    payload["enforcement_summary"]["selected_supporting_note_count"] = len(payload.get("selected_supporting_note_snippets", []))

    out_path = Path(args.out) if args.out else default_output_path(context_path, dispatch_id)
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    write_json(out_path, payload, pretty=True)
    print(json.dumps({
        "ok": True,
        "selected_input_bundle_path": relative_to_workspace(out_path),
        "verification_mode": payload.get("verification_mode"),
        "selected_persona_count": len(payload.get("selected_persona_sidecars", [])),
        "sidecar_guardrail_violation": ((payload.get("sidecar_selection_guardrail") or {}).get("violation", False)),
        "approx_tokens_after_trim": (payload.get("bundle_budget") or {}).get("approx_tokens_after_trim", 0),
        "trim_applied": (payload.get("bundle_budget") or {}).get("trim_applied", False),
    }, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
