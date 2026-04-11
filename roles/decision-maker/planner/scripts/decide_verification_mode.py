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

from common import WORKSPACE_ROOT, coerce_string, load_json, normalize_probability, relative_to_workspace, write_json  # noqa: E402


EDGE_ESCALATE_PP = 5.0
EDGE_REOPEN_PP = 12.0
HIGH_CONFIDENCE_MAX_EDGE_PP = 3.0
HIGH_CONFIDENCE_MAX_PROBABILITY_SPAN = 0.08
DIVERGENCE_ESCALATE = 0.12
CONTRACT_KEYWORDS = (
    "contract",
    "rule",
    "reply",
    "main-feed",
    "deleted",
    "tracker",
    "fallback",
    "resolution",
    "classification",
)
EXPLICIT_CONTRACT_AMBIGUITY_TRIGGER_LEVELS = {"moderate", "major"}
MAX_TARGETED_FETCHES = 4
MAX_TARGETED_SEARCH_QUERIES = 5


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Decide Decision-Maker verification mode deterministically")
    parser.add_argument("--decision-context-json", required=True)
    parser.add_argument("--out")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def default_output_path(context_path: Path, dispatch_id: str) -> Path:
    return context_path.with_name(f"verification-mode-{dispatch_id or context_path.stem}.json")


def load_optional_json(path_str: str) -> dict[str, Any]:
    if not path_str:
        return {}
    path = Path(path_str)
    if not path.is_absolute():
        path = WORKSPACE_ROOT / path
    if not path.exists():
        return {}
    payload = load_json(path)
    return payload if isinstance(payload, dict) else {}


def contains_contract_ambiguity(sidecars: list[dict[str, Any]]) -> bool:
    for sidecar in sidecars:
        payload = (sidecar or {}).get("payload") or {}
        texts = []
        texts.extend(payload.get("unresolved_ambiguities") or [])
        texts.extend(payload.get("strongest_disconfirmers") or [])
        for item in texts:
            lowered = str(item).lower()
            if any(keyword in lowered for keyword in CONTRACT_KEYWORDS):
                return True
    return False


def structured_handoff_complete(upstream: dict[str, Any]) -> tuple[bool, list[str]]:
    missing: list[str] = []
    required_string_fields = [
        "verification_gap_summary",
        "best_countercase_summary",
        "main_reason_for_disagreement",
        "resolution_mechanics_summary",
        "disagreement_type",
    ]
    for field in required_string_fields:
        if not coerce_string(upstream.get(field)):
            missing.append(field)
    points = upstream.get("independently_verified_points")
    if not isinstance(points, list) or not points:
        missing.append("independently_verified_points")
    contract_level = coerce_string(upstream.get("contract_ambiguity_level"))
    if contract_level not in {"none", "minor", "moderate", "major"}:
        missing.append("contract_ambiguity_level")
    if contract_level in {"minor", "moderate", "major"} and not coerce_string(upstream.get("contract_ambiguity_reason")):
        missing.append("contract_ambiguity_reason")
    freshness = coerce_string(upstream.get("freshness_sensitive"))
    if freshness not in {"yes", "no"}:
        missing.append("freshness_sensitive")
    if freshness == "yes" and not coerce_string(upstream.get("freshness_driver")):
        missing.append("freshness_driver")
    blockers_flag = coerce_string(upstream.get("blockers_require_new_research"))
    blockers = upstream.get("decision_blockers")
    if blockers_flag not in {"yes", "no"}:
        missing.append("blockers_require_new_research")
    if not isinstance(blockers, list):
        missing.append("decision_blockers")
    return (not missing, missing)


def high_confidence_no_extra_verification_gate(*, upstream: dict[str, Any], verification_quality: str, contract_ambiguity_level: str, freshness_sensitive: bool, decision_blockers: list[Any], blockers_require_new_research: bool, disagreement_intensity: str, probability_span: float, edge_pp_abs: float) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    structured_complete, missing = structured_handoff_complete(upstream)
    if not structured_complete:
        reasons.append(f"structured handoff incomplete: {', '.join(missing)}")
    if verification_quality != "high":
        reasons.append("edge_independent_verification_quality is not high")
    if contract_ambiguity_level not in {"none", "minor"}:
        reasons.append("contract ambiguity is above minor")
    if freshness_sensitive:
        reasons.append("freshness-sensitive case requires extra verification")
    if blockers_require_new_research:
        reasons.append("synthesis marked blockers requiring new research")
    if decision_blockers:
        reasons.append("decision blockers are present")
    if disagreement_intensity != "low":
        reasons.append("disagreement intensity is not low")
    if probability_span >= HIGH_CONFIDENCE_MAX_PROBABILITY_SPAN:
        reasons.append("persona probability span is above the high-confidence threshold")
    if edge_pp_abs > HIGH_CONFIDENCE_MAX_EDGE_PP:
        reasons.append("edge magnitude is above the high-confidence no-extra-verification threshold")
    return (not reasons, reasons)


def compute_targeted_search_budget(*, verification_quality: str, contract_ambiguity: bool, contract_ambiguity_level: str, freshness_sensitive: bool, decision_blockers: list[Any], disagreement_intensity: str, probability_span: float, edge_pp_abs: float, internal_inconsistency: bool) -> tuple[dict[str, int], int, list[str]]:
    score = 0
    reasons: list[str] = []

    if freshness_sensitive:
        score += 2
        reasons.append("freshness-sensitive case")
    if contract_ambiguity:
        weight = 2 if contract_ambiguity_level in {"moderate", "major"} else 1
        score += weight
        reasons.append(f"contract ambiguity ({contract_ambiguity_level or 'detected'})")
    if decision_blockers:
        score += 1
        reasons.append("decision blockers present")
    if internal_inconsistency:
        score += 1
        reasons.append("internal inconsistency / wide persona spread")
    if disagreement_intensity == "high":
        score += 1
        reasons.append("high disagreement intensity")
    if verification_quality == "low":
        score += 2
        reasons.append("low independent verification quality")
    elif verification_quality == "medium":
        score += 1
        reasons.append("medium independent verification quality")
    if edge_pp_abs >= EDGE_REOPEN_PP:
        score += 2
        reasons.append("very large apparent edge vs market")
    elif edge_pp_abs >= EDGE_ESCALATE_PP:
        score += 1
        reasons.append("meaningful apparent edge vs market")
    if probability_span >= 0.20:
        score += 1
        reasons.append("very wide persona probability span")

    fetches = 1
    if score >= 2:
        fetches += 1
    if score >= 4:
        fetches += 1
    if score >= 6:
        fetches += 1
    fetches = max(1, min(fetches, MAX_TARGETED_FETCHES))

    searches = min(MAX_TARGETED_SEARCH_QUERIES, fetches + 1 + (1 if score >= 5 else 0))
    minimum_distinct_source_families = 1 if fetches <= 1 else 2 if fetches <= 3 else 3
    preferred_distinct_source_families = min(fetches, minimum_distinct_source_families + (1 if score >= 6 else 0))

    return {
        "search_queries_allowed": searches,
        "source_fetches_allowed": fetches,
        "minimum_distinct_source_families": minimum_distinct_source_families,
        "preferred_distinct_source_families": preferred_distinct_source_families,
    }, score, reasons


def main() -> None:
    args = parse_args()
    context_path = Path(args.decision_context_json)
    if not context_path.is_absolute():
        context_path = WORKSPACE_ROOT / context_path
    context = load_json(context_path)
    upstream = context.get("upstream") or {}
    dispatch_id = coerce_string(context.get("dispatch_id"))
    case_key = coerce_string(context.get("case_key"))

    bundle = load_optional_json(coerce_string(upstream.get("sidecar_synthesis_bundle_path")))
    sidecars = bundle.get("sidecars") if isinstance(bundle.get("sidecars"), list) else []
    probs = [float(item.get("own_probability")) for item in (s.get("payload") or {} for s in sidecars) if isinstance(item.get("own_probability"), (int, float))]
    probability_span = round((max(probs) - min(probs)), 4) if probs else 0.0

    edge_pp = upstream.get("edge_mid_vs_market_pct_points")
    edge_pp = float(edge_pp) if isinstance(edge_pp, (int, float)) else 0.0
    verification_quality = coerce_string(upstream.get("edge_independent_verification_quality")) or "medium"
    follow_up_needed = coerce_string(upstream.get("follow_up_needed")) == "yes"
    freshness_sensitive_field = coerce_string(upstream.get("freshness_sensitive"))
    freshness_driver = coerce_string(upstream.get("freshness_driver"))
    decision_blockers = upstream.get("decision_blockers") if isinstance(upstream.get("decision_blockers"), list) else []
    blockers_require_new_research = coerce_string(upstream.get("blockers_require_new_research")) == "yes"
    disagreement_type = coerce_string(upstream.get("disagreement_type"))
    disagreement_intensity = coerce_string(upstream.get("disagreement_intensity")) or "medium"
    contract_ambiguity_level = coerce_string(upstream.get("contract_ambiguity_level"))
    contract_ambiguity_reason = coerce_string(upstream.get("contract_ambiguity_reason"))
    explicit_contract_ambiguity_present = contract_ambiguity_level in {"none", "minor", "moderate", "major"}
    inferred_contract_ambiguity = contains_contract_ambiguity(sidecars)
    contract_ambiguity = (
        contract_ambiguity_level in EXPLICIT_CONTRACT_AMBIGUITY_TRIGGER_LEVELS
        if explicit_contract_ambiguity_present
        else inferred_contract_ambiguity
    )
    explicit_freshness_present = freshness_sensitive_field in {"yes", "no"}
    inferred_freshness_sensitive = any(
        any(token in str((s.get("payload") or {}).get("timing_relevance", "")).lower() for token in ("high", "immediate", "intraday"))
        for s in sidecars
    ) or follow_up_needed
    freshness_sensitive = (freshness_sensitive_field == "yes") if explicit_freshness_present else inferred_freshness_sensitive
    internal_inconsistency = probability_span >= DIVERGENCE_ESCALATE

    high_confidence_passed, high_confidence_reasons = high_confidence_no_extra_verification_gate(
        upstream=upstream,
        verification_quality=verification_quality,
        contract_ambiguity_level=contract_ambiguity_level,
        freshness_sensitive=freshness_sensitive,
        decision_blockers=decision_blockers,
        blockers_require_new_research=blockers_require_new_research,
        disagreement_intensity=disagreement_intensity,
        probability_span=probability_span,
        edge_pp_abs=abs(edge_pp),
    )

    triggers: list[str] = []
    if abs(edge_pp) >= EDGE_ESCALATE_PP:
        triggers.append("large_apparent_edge_vs_market")
    if contract_ambiguity:
        triggers.append("source_of_truth_or_contract_ambiguity")
    if freshness_sensitive:
        triggers.append("freshness_sensitive_catalyst")
    if decision_blockers:
        triggers.append("decision_blockers_present")
    if internal_inconsistency:
        triggers.append("internal_inconsistency_in_package")

    targeted_search_budget = {
        "search_queries_allowed": 0,
        "source_fetches_allowed": 0,
        "minimum_distinct_source_families": 0,
        "preferred_distinct_source_families": 0,
    }
    targeted_search_uncertainty_score = 0
    targeted_search_budget_reasons: list[str] = []

    mode = "targeted_escalation"
    reasons: list[str] = []
    if blockers_require_new_research:
        mode = "not_ready_reopen_recommended"
        reasons.append("Synthesis marked blockers that require new research, so Decision-Maker should not pretend bounded verification is enough.")
    elif abs(edge_pp) >= EDGE_REOPEN_PP and verification_quality == "low":
        mode = "not_ready_reopen_recommended"
        reasons.append("Large apparent edge with low verification quality exceeds bounded-verification comfort.")
    elif contract_ambiguity and internal_inconsistency and verification_quality != "high":
        mode = "not_ready_reopen_recommended"
        reasons.append("Package shows both contract ambiguity and internal inconsistency without high verification quality.")
    elif high_confidence_passed:
        mode = "bounded_internal_audit"
        reasons.append("High-confidence sufficiency gate passed, so a no-extra-verification decision turn is allowed.")
    else:
        mode = "targeted_escalation"
        reasons.append("High-confidence sufficiency gate did not pass, so extra bounded context is required before final judgment.")
        reasons.extend(high_confidence_reasons)
        targeted_search_budget, targeted_search_uncertainty_score, targeted_search_budget_reasons = compute_targeted_search_budget(
            verification_quality=verification_quality,
            contract_ambiguity=contract_ambiguity,
            contract_ambiguity_level=contract_ambiguity_level,
            freshness_sensitive=freshness_sensitive,
            decision_blockers=decision_blockers,
            disagreement_intensity=disagreement_intensity,
            probability_span=probability_span,
            edge_pp_abs=abs(edge_pp),
            internal_inconsistency=internal_inconsistency,
        )
        reasons.append(
            "Deterministic search/fetch budget set to "
            f"queries={targeted_search_budget['search_queries_allowed']}, fetches={targeted_search_budget['source_fetches_allowed']}, "
            f"min_families={targeted_search_budget['minimum_distinct_source_families']} based on uncertainty score {targeted_search_uncertainty_score}."
        )

    budgets = {
        "bounded_internal_audit": {
            "persona_sidecars_max": 2,
            "assumption_snippets_max": 0,
            "evidence_snippets_max": 0,
            "supporting_note_snippets_max": 0,
            "search_queries_allowed": 0,
            "source_fetches_allowed": 0,
            "minimum_distinct_source_families": 0,
            "preferred_distinct_source_families": 0,
            "max_selected_bundle_chars": 12000,
        },
        "targeted_escalation": {
            "persona_sidecars_max": 3,
            "assumption_snippets_max": 1,
            "evidence_snippets_max": 1,
            "supporting_note_snippets_max": 1,
            "search_queries_allowed": targeted_search_budget["search_queries_allowed"],
            "source_fetches_allowed": targeted_search_budget["source_fetches_allowed"],
            "minimum_distinct_source_families": targeted_search_budget["minimum_distinct_source_families"],
            "preferred_distinct_source_families": targeted_search_budget["preferred_distinct_source_families"],
            "max_selected_bundle_chars": 18000,
        },
        "not_ready_reopen_recommended": {
            "persona_sidecars_max": 2,
            "assumption_snippets_max": 1,
            "evidence_snippets_max": 0,
            "supporting_note_snippets_max": 0,
            "search_queries_allowed": 0,
            "source_fetches_allowed": 0,
            "minimum_distinct_source_families": 0,
            "preferred_distinct_source_families": 0,
            "max_selected_bundle_chars": 10000,
        },
    }[mode]

    payload = {
        "artifact_type": "decision_verification_mode",
        "schema_version": "decision-verification-mode/v1",
        "case_key": case_key,
        "dispatch_id": dispatch_id,
        "mode": mode,
        "triggers": triggers,
        "reasons": reasons,
        "signals": {
            "edge_mid_vs_market_pct_points_abs": round(abs(edge_pp), 1),
            "verification_quality": verification_quality,
            "probability_span": probability_span,
            "contract_ambiguity_detected": contract_ambiguity,
            "contract_ambiguity_level": contract_ambiguity_level,
            "contract_ambiguity_reason": contract_ambiguity_reason,
            "contract_ambiguity_source": "synthesis_frontmatter" if explicit_contract_ambiguity_present else "researcher_sidecar_keyword_fallback",
            "freshness_sensitive": freshness_sensitive,
            "freshness_driver": freshness_driver,
            "freshness_source": "synthesis_frontmatter" if explicit_freshness_present else "sidecar_timing_fallback",
            "decision_blocker_count": len(decision_blockers),
            "blockers_require_new_research": blockers_require_new_research,
            "disagreement_type": disagreement_type,
            "disagreement_intensity": disagreement_intensity,
            "internal_inconsistency": internal_inconsistency,
            "sidecar_count": len(sidecars),
            "high_confidence_no_extra_verification_passed": high_confidence_passed,
            "high_confidence_gate_reasons": high_confidence_reasons,
            "targeted_search_uncertainty_score": targeted_search_uncertainty_score,
            "targeted_search_budget_reasons": targeted_search_budget_reasons,
        },
        "budgets": budgets,
    }

    out_path = Path(args.out) if args.out else default_output_path(context_path, dispatch_id)
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    write_json(out_path, payload, pretty=True)
    print(json.dumps({
        "ok": True,
        "mode": mode,
        "verification_mode_path": relative_to_workspace(out_path),
        "triggers": triggers,
    }, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
