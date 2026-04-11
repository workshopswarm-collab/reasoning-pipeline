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
    case_decision_handoff_path,
    case_syndicated_finding_path,
    case_syndicated_runtime_path,
    coerce_string,
    find_case_dir_for_dispatch,
    find_synthesis_stage_status_path,
    load_json,
    load_markdown_frontmatter,
    normalize_probability,
    percent_points_from_prob_delta,
    relative_to_workspace,
    round_probability,
    telegram_topic_session_key,
    utc_now_iso,
    write_json,
)


class ContextError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the deterministic decision context bundle for Decision-Maker")
    parser.add_argument("--case-key")
    parser.add_argument("--dispatch-id")
    parser.add_argument("--decision-handoff-path")
    parser.add_argument("--syndicated-runtime-path")
    parser.add_argument("--synthesis-stage-status-path")
    parser.add_argument("--market-price", type=float, help="Optional override for current actionable market reference price in [0,1]")
    parser.add_argument("--market-id")
    parser.add_argument("--market-title")
    parser.add_argument("--quote-timestamp")
    parser.add_argument("--out")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def resolve_case_key(args: argparse.Namespace) -> str:
    if args.case_key:
        return args.case_key
    if args.dispatch_id:
        case_dir = find_case_dir_for_dispatch(args.dispatch_id)
        if case_dir is not None:
            return case_dir.name
    raise ContextError("must supply --case-key or a --dispatch-id resolvable from existing decision-handoff artifacts")


def default_output_path(case_key: str, dispatch_id: str | None) -> Path:
    filename = "decision-context.json" if not dispatch_id else f"decision-context-{dispatch_id}.json"
    return WORKSPACE_ROOT / "roles" / "decision-maker" / "runtime" / "artifacts" / case_key / filename


def load_handoff(path: Path) -> tuple[dict[str, Any], str]:
    if not path.exists():
        raise ContextError(f"decision handoff not found: {path}")
    frontmatter, body = load_markdown_frontmatter(path)
    return dict(frontmatter), body


def load_runtime(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    payload = load_json(path)
    return payload if isinstance(payload, dict) else {}


def resolve_workspace_path(path_str: str) -> Path | None:
    if not path_str:
        return None
    path = Path(path_str)
    if not path.is_absolute():
        path = WORKSPACE_ROOT / path
    return path


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


def resolve_sidecar_synthesis_bundle_path(synthesis_status_path: Path | None, synthesis_status: dict[str, Any]) -> str:
    candidates: list[Path] = []
    structured_value = coerce_string(synthesis_status.get("structured_bundle_path"))
    if structured_value:
        structured_path = resolve_workspace_path(structured_value)
        if structured_path is not None:
            candidates.append(structured_path)
            candidates.append(structured_path.with_name("sidecar-synthesis-bundle.json"))
    raw_bundle_value = coerce_string(synthesis_status.get("bundle_path"))
    if raw_bundle_value:
        raw_bundle_path = resolve_workspace_path(raw_bundle_value)
        if raw_bundle_path is not None:
            candidates.append(raw_bundle_path.with_name("sidecar-synthesis-bundle.json"))
    if synthesis_status_path is not None:
        candidates.append(synthesis_status_path.with_name("sidecar-synthesis-bundle.json"))

    seen: set[str] = set()
    for candidate in candidates:
        resolved = str(candidate.resolve()) if candidate.exists() else str(candidate)
        if resolved in seen:
            continue
        seen.add(resolved)
        if valid_sidecar_bundle(candidate):
            return relative_to_workspace(candidate)
    return ""


def main() -> None:
    args = parse_args()
    case_key = resolve_case_key(args)

    handoff_path = Path(args.decision_handoff_path) if args.decision_handoff_path else case_decision_handoff_path(case_key)
    if not handoff_path.is_absolute():
        handoff_path = WORKSPACE_ROOT / handoff_path
    runtime_path = Path(args.syndicated_runtime_path) if args.syndicated_runtime_path else case_syndicated_runtime_path(case_key)
    if not runtime_path.is_absolute():
        runtime_path = WORKSPACE_ROOT / runtime_path
    syndicated_finding_path = case_syndicated_finding_path(case_key)

    handoff_frontmatter, handoff_body = load_handoff(handoff_path)
    runtime_payload = load_runtime(runtime_path)

    dispatch_id = coerce_string(args.dispatch_id) or coerce_string(handoff_frontmatter.get("dispatch_id"))
    question = coerce_string(handoff_frontmatter.get("question")) or coerce_string(runtime_payload.get("question"))
    market_title = coerce_string(args.market_title) or coerce_string(handoff_frontmatter.get("market_title")) or question
    market_id = coerce_string(args.market_id) or coerce_string(handoff_frontmatter.get("market_id"))

    market_price = args.market_price
    if market_price is None:
        market_price = normalize_probability(handoff_frontmatter.get("market_implied_probability"))
    else:
        market_price = normalize_probability(market_price)
    if market_price is None:
        raise ContextError("could not determine market reference price; pass --market-price if handoff frontmatter lacks market_implied_probability")

    syndicated_low = normalize_probability(handoff_frontmatter.get("syndicated_probability_low"))
    syndicated_high = normalize_probability(handoff_frontmatter.get("syndicated_probability_high"))
    syndicated_mid = normalize_probability(handoff_frontmatter.get("syndicated_probability_midpoint"))
    if syndicated_mid is None and syndicated_low is not None and syndicated_high is not None:
        syndicated_mid = round_probability((syndicated_low + syndicated_high) / 2.0)

    synthesis_status_path = Path(args.synthesis_stage_status_path) if args.synthesis_stage_status_path else find_synthesis_stage_status_path(case_key, dispatch_id)
    if synthesis_status_path and not synthesis_status_path.is_absolute():
        synthesis_status_path = WORKSPACE_ROOT / synthesis_status_path
    synthesis_status = load_runtime(synthesis_status_path) if synthesis_status_path and synthesis_status_path.exists() else {}
    sidecar_synthesis_bundle_path = resolve_sidecar_synthesis_bundle_path(synthesis_status_path, synthesis_status)
    ready_sidecar_personas = list(synthesis_status.get("ready_sidecar_personas") or []) if isinstance(synthesis_status.get("ready_sidecar_personas"), list) else []
    pending_sidecar_personas = list(synthesis_status.get("pending_sidecar_personas") or []) if isinstance(synthesis_status.get("pending_sidecar_personas"), list) else []
    sidecar_bundle_payload = load_runtime(resolve_workspace_path(sidecar_synthesis_bundle_path)) if sidecar_synthesis_bundle_path else {}
    sidecar_bundle_sidecar_count = (sidecar_bundle_payload.get("sidecar_count") if isinstance(sidecar_bundle_payload.get("sidecar_count"), int) else (len(sidecar_bundle_payload.get("sidecars") or []) if isinstance(sidecar_bundle_payload.get("sidecars"), list) else 0))
    synthesis_target_chat_id = coerce_string(synthesis_status.get("synthesis_target_chat_id"))
    synthesis_target_topic_id = coerce_string(synthesis_status.get("synthesis_target_topic_id"))
    synthesis_target_topic_title = coerce_string(synthesis_status.get("synthesis_target_topic_title"))
    synthesis_target_session_key = coerce_string(synthesis_status.get("synthesis_target_session_key")) or telegram_topic_session_key(synthesis_target_chat_id, synthesis_target_topic_id)

    bundle = {
        "artifact_type": "decision_context_bundle",
        "schema_version": "decision-context/v1",
        "built_at": utc_now_iso(),
        "builder": "roles/decision-maker/runtime/scripts/build_decision_context.py",
        "case_key": case_key,
        "dispatch_id": dispatch_id,
        "question": question,
        "market": {
            "market_id": market_id,
            "market_title": market_title,
            "market_reference_price": round_probability(market_price),
            "quote_timestamp": coerce_string(args.quote_timestamp) or coerce_string(runtime_payload.get("market_snapshot_time")),
            "price_source": "market_snapshot_quote",
        },
        "upstream": {
            "decision_handoff_path": relative_to_workspace(handoff_path),
            "syndicated_runtime_path": relative_to_workspace(runtime_path) if runtime_path.exists() else "",
            "syndicated_finding_path": relative_to_workspace(syndicated_finding_path) if syndicated_finding_path.exists() else "",
            "synthesis_stage_status_path": relative_to_workspace(synthesis_status_path) if synthesis_status_path and synthesis_status_path.exists() else "",
            "sidecar_synthesis_bundle_path": sidecar_synthesis_bundle_path,
            "sidecar_synthesis_bundle_artifact_type": "sidecar_synthesis_bundle" if sidecar_synthesis_bundle_path else "",
            "sidecar_bundle_coverage_status": coerce_string(sidecar_bundle_payload.get("coverage_status")),
            "sidecar_bundle_sidecar_count": sidecar_bundle_sidecar_count,
            "ready_sidecar_personas": ready_sidecar_personas,
            "ready_sidecar_count": len(ready_sidecar_personas),
            "pending_sidecar_personas": pending_sidecar_personas,
            "pending_sidecar_count": len(pending_sidecar_personas),
            "syndicated_probability_low": round_probability(syndicated_low),
            "syndicated_probability_high": round_probability(syndicated_high),
            "syndicated_probability_midpoint": round_probability(syndicated_mid),
            "relation_to_market": coerce_string(handoff_frontmatter.get("relation_to_market")),
            "edge_quality": coerce_string(handoff_frontmatter.get("edge_quality")),
            "edge_independent_verification_quality": coerce_string(handoff_frontmatter.get("edge_independent_verification_quality")),
            "compressed_toward_market_due_to_verification": coerce_string(handoff_frontmatter.get("compressed_toward_market_due_to_verification")),
            "contract_ambiguity_level": coerce_string(handoff_frontmatter.get("contract_ambiguity_level")),
            "contract_ambiguity_reason": coerce_string(handoff_frontmatter.get("contract_ambiguity_reason")),
            "independently_verified_points": handoff_frontmatter.get("independently_verified_points") or [],
            "verification_gap_summary": coerce_string(handoff_frontmatter.get("verification_gap_summary")),
            "best_countercase_summary": coerce_string(handoff_frontmatter.get("best_countercase_summary")),
            "main_reason_for_disagreement": coerce_string(handoff_frontmatter.get("main_reason_for_disagreement")),
            "resolution_mechanics_summary": coerce_string(handoff_frontmatter.get("resolution_mechanics_summary")),
            "disagreement_intensity": coerce_string(handoff_frontmatter.get("disagreement_intensity")),
            "freshness_sensitive": coerce_string(handoff_frontmatter.get("freshness_sensitive")),
            "freshness_driver": coerce_string(handoff_frontmatter.get("freshness_driver")),
            "decision_blockers": handoff_frontmatter.get("decision_blockers") or [],
            "blockers_require_new_research": coerce_string(handoff_frontmatter.get("blockers_require_new_research")),
            "disagreement_type": coerce_string(handoff_frontmatter.get("disagreement_type")),
            "follow_up_needed": coerce_string(handoff_frontmatter.get("follow_up_needed")),
            "edge_mid_vs_market_pct_points": percent_points_from_prob_delta((syndicated_mid - market_price) if syndicated_mid is not None else None),
        },
        "telegram": {
            "controller_chat_id": synthesis_target_chat_id,
            "synthesis_topic_id": synthesis_target_topic_id,
            "synthesis_topic_title": synthesis_target_topic_title,
            "synthesis_session_key": synthesis_target_session_key,
        },
        "portfolio_context": {
            "status": "disabled",
            "notes": ["Portfolio-aware gating and execution context are currently out of scope for Decision-Maker."],
        },
        "verification_policy": {
            "policy_version": "decision-verification/v1",
            "default_mode": "bounded_internal_audit",
            "mode_descriptions": {
                "bounded_internal_audit": "Use synthesis as the starting compression, reread only the most decisive upstream artifacts, and avoid broad re-research by default.",
                "targeted_escalation": "Use a bounded internal audit plus a small number of targeted checks when a narrow ambiguity or meaningful edge justifies it.",
                "not_ready_reopen_recommended": "If responsible verification would require a much broader reread or new research pass, prefer a not-ready/non-action packet over pretending bounded verification was enough."
            },
            "default_artifact_budget": {
                "persona_findings_max": 2,
                "assumption_artifacts_max": 1,
                "evidence_artifacts_max": 1,
                "countercase_or_supporting_note_bundles_max": 1
            },
            "default_external_budget": {
                "external_source_surfaces_max": 2,
                "live_market_or_tracker_checks_max": 1
            },
            "escalation_triggers": [
                "large_apparent_edge_vs_market",
                "source_of_truth_or_contract_ambiguity",
                "freshness_sensitive_catalyst",
                "internal_inconsistency_in_package"
            ],
            "priority_order": [
                "verify_exact_crux",
                "verify_freshness_or_source_of_truth_mechanics",
                "verify_strongest_countercase",
                "only_then_expand_broader_reread"
            ],
            "hard_rule": "Decision-Maker is allowed to do targeted additional verification, but should not become a routine second synthesis pass. If adequate verification would require broader reread or new research, prefer a not-ready or non-action packet."
        },
        "canonical_runtime": {
            "build_decision_prompt_script": "roles/decision-maker/planner/scripts/build_decision_prompt.py",
            "run_decision_maker_script": "roles/decision-maker/runtime/scripts/run_decision_maker.py",
            "validate_decision_packet_script": "roles/decision-maker/runtime/scripts/validate_decision_packet.py",
            "render_decision_packet_script": "roles/decision-maker/runtime/scripts/render_decision_packet.py",
            "bootstrap_decision_telegram_lane_script": "roles/decision-maker/runtime/scripts/bootstrap_decision_telegram_lane.py",
            "show_decision_stage_status_script": "roles/decision-maker/runtime/scripts/show_decision_stage_status.py",
        },
        "canonical_outputs": {
            "decision_packet_markdown": f"qualitative-db/40-research/cases/{case_key}/decision-maker/decision-maker-packet.md",
            "decision_packet_json": f"qualitative-db/40-research/cases/{case_key}/decision-maker/artifacts/decision-maker-packet.json",
            "decision_stage_status_json": f"qualitative-db/40-research/cases/{case_key}/decision-maker/artifacts/decision-stage-status.json",
        },
        "recommended_runtime_defaults": {
            "valid_for_hours": 24,
            "quote_staleness_seconds": 300,
            "allow_auto_reversal": False,
            "rebalance_threshold_fraction": 0.1,
            "price_source": "market_snapshot_quote",
            "decision_agent_session_key": "agent:decision-maker:main",
        },
        "source_excerpt": {
            "decision_handoff_frontmatter": handoff_frontmatter,
            "decision_handoff_body": handoff_body,
            "syndicated_runtime": runtime_payload,
            "synthesis_stage_status": synthesis_status,
        },
    }

    out_path = Path(args.out) if args.out else default_output_path(case_key, dispatch_id or None)
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    write_json(out_path, bundle, pretty=True)

    print(json.dumps({
        "ok": True,
        "case_key": case_key,
        "dispatch_id": dispatch_id,
        "decision_context_path": relative_to_workspace(out_path),
        "decision_handoff_path": relative_to_workspace(handoff_path),
        "syndicated_runtime_path": relative_to_workspace(runtime_path) if runtime_path.exists() else "",
        "synthesis_stage_status_path": relative_to_workspace(synthesis_status_path) if synthesis_status_path and synthesis_status_path.exists() else "",
        "market_reference_price": round_probability(market_price),
        "syndicated_probability_midpoint": round_probability(syndicated_mid),
        "controller_chat_id": synthesis_target_chat_id,
    }, indent=2 if args.pretty else None))


if __name__ == "__main__":
    try:
        main()
    except ContextError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        raise SystemExit(1)
