from __future__ import annotations

from typing import Any

from common import normalize_probability

SIDE_ENUM = {"yes", "no", "none"}
TRADE_AUTHORIZATION_ENUM = {"authorized", "watch_only", "risk_reduce_only", "forbidden"}
POSITION_POLICY_ENUM = {"enter_or_add", "hold_only", "reduce_only", "exit_only", "flat"}
DECISION_READINESS_ENUM = {"ready", "needs_more_research", "needs_market_update"}
QUALITY_ENUM = {"low", "medium", "high"}
DECISION_QUALITY_ENUM = {"clean", "good_not_clean", "fragile", "not_ready"}
PRICE_SOURCE_ENUM = {"effective_executable_quote", "market_snapshot_quote"}
THESIS_CLASS_ENUM = {"edge_present", "edge_too_small", "price_not_good_enough", "not_decision_ready", "risk_constraint_binding"}
BAND_NAME_ENUM = {"max_enter", "scaled_enter", "hold", "trim", "exit"}
CANONICAL_BAND_ORDER = ["max_enter", "scaled_enter", "hold", "trim", "exit"]


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _validate_probability_field(errors: list[str], payload: dict[str, Any], field: str) -> float | None:
    value = normalize_probability(payload.get(field))
    if value is None:
        errors.append(f"missing or invalid probability field: {field}")
    return value


def validate_decision_packet_payload(payload: Any) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(payload, dict):
        return {"ok": False, "errors": ["top-level payload must be a JSON object"], "warnings": []}

    for key in [
        "schema_version",
        "generated_at",
        "context",
        "decision",
        "valuation",
        "execution_semantics",
        "risk_controls",
        "bands",
        "invalidation",
        "epistemic_status",
        "audit",
    ]:
        if key not in payload:
            errors.append(f"missing top-level key: {key}")

    if payload.get("schema_version") != "decision-packet/v1":
        errors.append("schema_version must equal decision-packet/v1")

    context = payload.get("context") if isinstance(payload.get("context"), dict) else {}
    decision = payload.get("decision") if isinstance(payload.get("decision"), dict) else {}
    valuation = payload.get("valuation") if isinstance(payload.get("valuation"), dict) else {}
    execution = payload.get("execution_semantics") if isinstance(payload.get("execution_semantics"), dict) else {}
    risk = payload.get("risk_controls") if isinstance(payload.get("risk_controls"), dict) else {}
    invalidation = payload.get("invalidation") if isinstance(payload.get("invalidation"), dict) else {}
    epistemic = payload.get("epistemic_status") if isinstance(payload.get("epistemic_status"), dict) else {}
    audit = payload.get("audit") if isinstance(payload.get("audit"), dict) else {}
    bands = payload.get("bands") if isinstance(payload.get("bands"), list) else []

    for field in ["case_key", "dispatch_id", "question"]:
        value = context.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"missing or invalid context field: {field}")

    if context.get("canonical_markdown_path") not in {None, "decision-maker-packet.md"}:
        errors.append("context.canonical_markdown_path must be decision-maker-packet.md when supplied")
    if context.get("canonical_json_path") not in {None, "artifacts/decision-maker-packet.json"}:
        errors.append("context.canonical_json_path must be artifacts/decision-maker-packet.json when supplied")

    side = decision.get("side")
    if side not in SIDE_ENUM:
        errors.append("decision.side must be one of yes|no|none")
    trade_authorization = decision.get("trade_authorization")
    if trade_authorization not in TRADE_AUTHORIZATION_ENUM:
        errors.append("decision.trade_authorization has invalid enum")
    position_policy = decision.get("position_policy")
    if position_policy not in POSITION_POLICY_ENUM:
        errors.append("decision.position_policy has invalid enum")
    readiness = decision.get("decision_readiness")
    if readiness not in DECISION_READINESS_ENUM:
        errors.append("decision.decision_readiness has invalid enum")
    thesis_class = decision.get("thesis_class")
    if thesis_class not in (None, "") and thesis_class not in THESIS_CLASS_ENUM:
        errors.append("decision.thesis_class has invalid enum")
    primary_crux = decision.get("primary_crux")
    if not isinstance(primary_crux, str) or not primary_crux.strip():
        errors.append("decision.primary_crux must be a non-empty string")

    low = _validate_probability_field(errors, valuation, "fair_value_low")
    high = _validate_probability_field(errors, valuation, "fair_value_high")
    mid = _validate_probability_field(errors, valuation, "fair_value_mid")
    market = _validate_probability_field(errors, valuation, "market_reference_price")
    if low is not None and high is not None and low > high:
        errors.append("valuation.fair_value_low cannot exceed valuation.fair_value_high")
    if low is not None and high is not None and mid is not None and not (low <= mid <= high):
        errors.append("valuation.fair_value_mid must fall within fair_value_low..fair_value_high")
    if valuation.get("independent_verification_quality") not in QUALITY_ENUM:
        errors.append("valuation.independent_verification_quality has invalid enum")
    compressed = valuation.get("compressed_toward_market_applied")
    if not isinstance(compressed, bool):
        errors.append("valuation.compressed_toward_market_applied must be boolean")
    edge_value = valuation.get("edge_mid_vs_market_pct_points")
    if not _is_number(edge_value):
        errors.append("valuation.edge_mid_vs_market_pct_points must be numeric")
    elif mid is not None and market is not None:
        expected_edge = round((mid - market) * 100.0, 1)
        if round(float(edge_value), 1) != expected_edge:
            errors.append(
                f"valuation.edge_mid_vs_market_pct_points inconsistent with fair_value_mid and market_reference_price (expected {expected_edge})"
            )

    if execution.get("price_axis") != "market_implied_true_prob":
        errors.append("execution_semantics.price_axis must equal market_implied_true_prob")
    if execution.get("price_source") not in PRICE_SOURCE_ENUM:
        errors.append("execution_semantics.price_source has invalid enum")
    rebalance = execution.get("rebalance_threshold_fraction")
    if not _is_number(rebalance) or not (0 <= float(rebalance) <= 1):
        errors.append("execution_semantics.rebalance_threshold_fraction must be in [0,1]")
    if not isinstance(execution.get("allow_auto_reversal"), bool):
        errors.append("execution_semantics.allow_auto_reversal must be boolean")
    quote_staleness = execution.get("quote_staleness_seconds")
    if not isinstance(quote_staleness, int) or quote_staleness < 1:
        errors.append("execution_semantics.quote_staleness_seconds must be an integer >= 1")
    valid_until = execution.get("valid_until")
    if not isinstance(valid_until, str) or not valid_until.strip():
        errors.append("execution_semantics.valid_until must be a non-empty ISO datetime string")

    for field in [
        "max_position_size_pct_bankroll",
        "max_additional_exposure_pct_bankroll",
        "max_single_order_pct_bankroll",
    ]:
        value = risk.get(field)
        if not _is_number(value) or not (0 <= float(value) <= 1):
            errors.append(f"risk_controls.{field} must be in [0,1]")
    slippage = risk.get("slippage_tolerance_bps")
    if not isinstance(slippage, int) or slippage < 0:
        errors.append("risk_controls.slippage_tolerance_bps must be a non-negative integer")
    if risk.get("confidence_level") not in QUALITY_ENUM:
        errors.append("risk_controls.confidence_level has invalid enum")

    if side == "none" and position_policy != "flat":
        errors.append("decision.position_policy must be flat when decision.side is none")
    if trade_authorization == "forbidden" and position_policy != "flat":
        errors.append("decision.position_policy must be flat when trade_authorization is forbidden")
    if trade_authorization == "risk_reduce_only" and position_policy not in {"reduce_only", "exit_only"}:
        errors.append("decision.position_policy must be reduce_only or exit_only when trade_authorization is risk_reduce_only")
    if trade_authorization == "watch_only" and position_policy not in {"hold_only", "reduce_only", "exit_only", "flat"}:
        errors.append("decision.position_policy invalid for watch_only")

    if not bands:
        errors.append("bands must contain at least one band")
    else:
        seen_names: list[str] = []
        prior_max: float | None = None
        band_ranges: list[tuple[str, float, float, float]] = []
        for index, band in enumerate(bands):
            if not isinstance(band, dict):
                errors.append(f"band at index {index} must be an object")
                continue
            name = band.get("name")
            if name not in BAND_NAME_ENUM:
                errors.append(f"band at index {index} has invalid name")
                continue
            seen_names.append(str(name))
            min_p = normalize_probability(band.get("min_p"))
            max_p = normalize_probability(band.get("max_p"))
            target = band.get("target_exposure_fraction")
            if min_p is None or max_p is None:
                errors.append(f"band {name} has invalid min_p/max_p")
                continue
            if min_p > max_p:
                errors.append(f"band {name} has min_p greater than max_p")
            if not _is_number(target) or not (0 <= float(target) <= 1):
                errors.append(f"band {name} has invalid target_exposure_fraction")
                continue
            band_ranges.append((str(name), min_p, max_p, float(target)))
            if prior_max is not None and round(min_p, 6) != round(prior_max, 6):
                errors.append(f"band {name} does not begin where the prior band ended")
            prior_max = max_p
        if set(seen_names) != set(CANONICAL_BAND_ORDER):
            warnings.append("bands do not include the full canonical five-band set")
        if band_ranges:
            first = band_ranges[0]
            last = band_ranges[-1]
            if round(first[1], 6) != 0.0:
                errors.append("first band must start at 0")
            if round(last[2], 6) != 1.0:
                errors.append("last band must end at 1")
            exposure_sequence = [target for _, _, _, target in band_ranges]
            if side == "yes":
                if any(exposure_sequence[i] < exposure_sequence[i + 1] for i in range(len(exposure_sequence) - 1)):
                    errors.append("for side=yes, target_exposure_fraction must be non-increasing as price rises")
            elif side == "no":
                if any(exposure_sequence[i] > exposure_sequence[i + 1] for i in range(len(exposure_sequence) - 1)):
                    errors.append("for side=no, target_exposure_fraction must be non-decreasing as price rises")

    for field in ["thesis_breakers", "time_breakers"]:
        value = invalidation.get(field)
        if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
            errors.append(f"invalidation.{field} must be a list of strings")

    for field in ["key_uncertainties", "what_would_change_my_mind"]:
        value = epistemic.get(field)
        if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
            errors.append(f"epistemic_status.{field} must be a list of strings")
    decision_quality = epistemic.get("decision_quality")
    if decision_quality not in (None, "") and decision_quality not in DECISION_QUALITY_ENUM:
        errors.append("epistemic_status.decision_quality has invalid enum")

    for field in [
        "market_baseline_respected",
        "action_bias_check_passed",
        "self_preservation_bias_check_passed",
        "structured_handoff_primary_used",
        "prose_fallback_used",
        "additional_verification_performed",
    ]:
        if not isinstance(audit.get(field), bool):
            errors.append(f"audit.{field} must be boolean")
    rationale = audit.get("one_sentence_rationale")
    if not isinstance(rationale, str) or not rationale.strip():
        errors.append("audit.one_sentence_rationale must be a non-empty string")
    verification_mode_used = audit.get("verification_mode_used")
    if verification_mode_used not in {"bounded_internal_audit", "targeted_escalation", "not_ready_reopen_recommended"}:
        errors.append("audit.verification_mode_used has invalid enum")
    additional_notes = audit.get("additional_verification_notes")
    if not isinstance(additional_notes, str):
        errors.append("audit.additional_verification_notes must be a string")

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "canonical_band_order": list(CANONICAL_BAND_ORDER),
    }
