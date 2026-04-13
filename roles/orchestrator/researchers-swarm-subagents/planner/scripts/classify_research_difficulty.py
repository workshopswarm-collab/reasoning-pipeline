#!/usr/bin/env python3
"""Classify case-level research difficulty for one market.

Hybrid planner-stage utility:
- deterministic heuristics always run first
- optional local-model refinement runs only for gray-area cases
- heuristic output remains the safe fallback if the local model is unavailable
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

from local_model_client import ollama_generate, ollama_tags


VALID_DIFFICULTY = {"low", "medium", "high"}
VALID_RISK = {"low", "medium", "high"}
VALID_EVIDENCE = {
    "1_authoritative",
    "2_meaningful",
    "3_meaningful",
    "direct_settlement_required",
}
VALID_SOURCE_OF_TRUTH = {
    "authoritative_direct",
    "authoritative_with_fallback",
    "consensus_reporting_primary",
    "multi_source_ambiguous",
}
VALID_MODEL_CONFIDENCE = {"low", "medium", "high"}

FOCUS_HINT_NORMALIZATION = {
    "verify_active_month_contract": ["settlement_mechanics_check"],
    "confirm_cme_settlement_publication": ["official_source_verification", "source_of_truth_check"],
    "check_settlement_time_window": ["date_timing_check", "settlement_mechanics_check"],
    "validate_price_calculation_method": ["settlement_mechanics_check"],
    "confirm_official_ranking_update": ["official_source_verification", "date_timing_check"],
    "confirm_metric_threshold_method": ["source_of_truth_check"],
    "verify_utc_conversion": ["date_timing_check", "settlement_mechanics_check"],
    "check_binance_candle_close": ["official_source_verification", "settlement_mechanics_check"],
    "exclude_other_exchanges": ["source_of_truth_check"],
    "verify_on_chain_price_history": ["official_source_verification"],
    "check_exchange_rules": ["settlement_mechanics_check"],
    "verify_exact_btc/usdt_pair": ["source_of_truth_check"],
    "check_et_1200_utc_alignment": ["date_timing_check"],
    "confirm_close_price_logic": ["settlement_mechanics_check"],
    "authoritative_direct": ["authoritative_source_first", "official_source_verification"],
}

CANONICAL_FOCUS_HINTS = {
    "extra_verification",
    "date_timing_check",
    "resolution_audit",
    "attribution_check",
    "source_of_truth_check",
    "multi_condition_check",
    "independent_confirmation",
    "disconfirming_source_required",
    "authoritative_source_first",
    "official_source_verification",
    "settlement_mechanics_check",
}

FOCUS_HINT_PRIORITY = {
    "official_source_verification": 10,
    "authoritative_source_first": 20,
    "source_of_truth_check": 30,
    "settlement_mechanics_check": 40,
    "date_timing_check": 50,
    "resolution_audit": 60,
    "multi_condition_check": 70,
    "attribution_check": 80,
    "independent_confirmation": 90,
    "disconfirming_source_required": 100,
    "extra_verification": 110,
}

CANONICAL_RATIONALES = {
    "extreme_market_probability",
    "date_sensitive_resolution",
    "explicit_exclusion_rules",
    "attribution_requirement",
    "consensus_reporting_dependency",
    "multi_condition_contract",
    "geopolitics_reporting_sensitivity",
    "authoritative_source_available",
    "authoritative_source_with_fallback",
    "settlement_mechanics_complexity",
    "structured_settlement_guard",
    "ambiguous_source_of_truth",
    "heuristic_medium_band",
    "official_and_consensus_cues",
}

RATIONALE_PRIORITY = {
    "authoritative_source_available": 10,
    "authoritative_source_with_fallback": 20,
    "settlement_mechanics_complexity": 30,
    "date_sensitive_resolution": 40,
    "explicit_exclusion_rules": 50,
    "attribution_requirement": 60,
    "consensus_reporting_dependency": 70,
    "multi_condition_contract": 80,
    "geopolitics_reporting_sensitivity": 90,
    "extreme_market_probability": 100,
    "ambiguous_source_of_truth": 110,
    "official_and_consensus_cues": 120,
    "structured_settlement_guard": 130,
    "heuristic_medium_band": 140,
}

SOURCE_OF_TRUTH_ORDER = {
    "authoritative_direct": 0,
    "authoritative_with_fallback": 1,
    "consensus_reporting_primary": 2,
    "multi_source_ambiguous": 3,
}

DIFFICULTY_ORDER = {"low": 0, "medium": 1, "high": 2}
EVIDENCE_ORDER = {
    "1_authoritative": 0,
    "2_meaningful": 1,
    "3_meaningful": 2,
    "direct_settlement_required": 3,
}

DATE_PATTERNS = [
    r"\bon\s+(january|february|march|april|may|june|july|august|september|october|november|december)\b",
    r"\bby\s+(january|february|march|april|may|june|july|august|september|october|november|december)\b",
    r"\bthis\s+week\b",
    r"\btoday\b",
    r"\btomorrow\b",
    r"\bdeadline\b",
    r"\bend of the third calendar date\b",
]

OFFICIAL_SOURCE_PATTERNS = [
    r"official .* chart",
    r"official .* leaderboard",
    r"official .* top 10",
    r"official .* box score",
    r"official .* stats?",
    r"cme .* settlement",
    r"settle at",
    r"official government data",
    r"netflix",
    r"tudum",
    r"youtube channel",
]

SETTLEMENT_MECHANICS_PATTERNS = [
    r"active month",
    r"final trading day",
    r"settlement price",
    r"intraday trades.*do not count",
    r"first published",
    r"later corrections",
    r"range bracket",
    r"market-holiday schedule",
]

EXCLUSION_PATTERNS = [
    r"will not count",
    r"does not count",
    r"do not count",
    r"only .* will count",
    r"must impact",
    r"must be confirmed",
    r"proxy forces .* will not count",
    r"intercepted .* will not count",
]

ATTRIBUTION_PATTERNS = [
    r"confirmed to have originated",
    r"explicitly claimed",
    r"attribution",
    r"authorized representatives",
]

CONSENSUS_PATTERNS = [
    r"consensus of credible reporting",
    r"major international media",
    r"national broadcasters",
    r"official government/military statements",
    r"primary resolution source",
]

AUTHORITATIVE_FALLBACK_PATTERNS = [
    r"primary resolution source .* or a consensus of credible reporting",
    r"will be .* or a consensus of credible reporting",
    r"resolution source .* or a consensus of credible reporting",
]

GEO_STRONG_PATTERNS = [
    r"military action",
    r"iran",
    r"israel",
    r"ceasefire",
    r"proxy forces",
    r"missile",
    r"drone",
    r"official government/military statements",
    r"multilateral bodies",
]

GEO_WEAK_PATTERNS = [
    r"\bstrike\b",
    r"\bwar\b",
    r"\bconflict\b",
    r"diplomatic meeting",
    r"troops?",
    r"shelling",
]

MULTI_CONDITION_PATTERNS = [
    r"if .* and .*",
    r"only .* if .*",
    r"must .* and .*",
    r"regardless of whether",
]

SCRIPT_DIR = Path(__file__).resolve().parent
CLASSIFIER_PROMPT_PATH = SCRIPT_DIR.parent / "prompts" / "research_difficulty_classifier.md"
DEFAULT_OLLAMA_ENDPOINT = os.getenv("RESEARCH_DIFFICULTY_LOCAL_ENDPOINT", "http://127.0.0.1:11434")
DEFAULT_OLLAMA_MODEL = os.getenv("RESEARCH_DIFFICULTY_LOCAL_MODEL", "qwen3.5:9b")
DEFAULT_MODE = os.getenv("RESEARCH_DIFFICULTY_CLASSIFIER_MODE", "heuristic")
DEFAULT_TIMEOUT_SECONDS = float(os.getenv("RESEARCH_DIFFICULTY_TIMEOUT_SECONDS", "55"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Classify research difficulty for one case/market payload")
    parser.add_argument("--file", default="-", help="Path to input JSON file, or - for stdin")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    parser.add_argument("--mode", choices=["heuristic", "hybrid"], default=DEFAULT_MODE)
    parser.add_argument("--ollama-endpoint", default=DEFAULT_OLLAMA_ENDPOINT)
    parser.add_argument("--ollama-model", default=DEFAULT_OLLAMA_MODEL)
    parser.add_argument("--timeout-seconds", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    return parser.parse_args()


def load_json(path_str: str):
    if path_str == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path_str).read_text()
    if not raw.strip():
        raise ValueError("input JSON is empty")
    return json.loads(raw)


def text_blob(payload: dict) -> str:
    fields = [
        payload.get("title") or "",
        payload.get("description") or "",
        payload.get("category") or "",
        payload.get("platform") or "",
        payload.get("outcome_type") or "",
    ]
    metadata = payload.get("metadata") or {}
    if isinstance(metadata, dict):
        for key in ("question", "rules", "resolution", "url"):
            value = metadata.get(key)
            if isinstance(value, str):
                fields.append(value)
    return "\n".join(fields).lower()


def has_any(patterns: list[str], text: str) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE | re.DOTALL) for pattern in patterns)


def count_matches(patterns: list[str], text: str) -> int:
    return sum(1 for pattern in patterns if re.search(pattern, text, re.IGNORECASE | re.DOTALL))


def _priority_sort(values: list[str], priority_map: dict[str, int]) -> list[str]:
    return sorted(dict.fromkeys(values), key=lambda item: (priority_map.get(item, 9999), item))


def normalize_focus_hints(focus_hints: list[str]) -> list[str]:
    normalized: list[str] = []
    for raw_hint in focus_hints or []:
        if not isinstance(raw_hint, str):
            continue
        hint = raw_hint.strip().lower().replace("-", "_").replace(" ", "_")
        if not hint:
            continue
        mapped = FOCUS_HINT_NORMALIZATION.get(hint)
        if mapped:
            normalized.extend(mapped)
        elif hint in CANONICAL_FOCUS_HINTS:
            normalized.append(hint)
    return _priority_sort(normalized, FOCUS_HINT_PRIORITY)


def _normalize_rationale_item(item: str) -> str | None:
    text = item.strip().lower().replace('-', '_').replace(' ', '_')
    if not text:
        return None
    if text in CANONICAL_RATIONALES:
        return text

    pattern_map = [
        (r"extreme.*probability|market_implied_probability_is_extreme", "extreme_market_probability"),
        (r"date.*deadline|date_specific|deadline_sensitive", "date_sensitive_resolution"),
        (r"explicit_exclusions|narrow_qualifying_criteria|exclusion", "explicit_exclusion_rules"),
        (r"attribution|identity_requirement", "attribution_requirement"),
        (r"consensus_reporting|official_statements", "consensus_reporting_dependency"),
        (r"multiple_conditions|multi_condition", "multi_condition_contract"),
        (r"geopolitics|conflict|public_reporting_sensitive", "geopolitics_reporting_sensitivity"),
        (r"authoritative_source_available|authoritative_source_appears_primary|authoritative_source", "authoritative_source_available"),
        (r"fallback_reporting|authoritative_with_fallback", "authoritative_source_with_fallback"),
        (r"settlement_mechanics|structured_settlement", "settlement_mechanics_complexity"),
        (r"medium_band", "heuristic_medium_band"),
        (r"ambiguous.*source_of_truth|source_of_truth.*ambiguous", "ambiguous_source_of_truth"),
        (r"official.*consensus|consensus.*official", "official_and_consensus_cues"),
        (r"structured_settlement_mechanics_warrant_conservative_classification|settlement_guard", "structured_settlement_guard"),
    ]
    for pattern, canonical in pattern_map:
        if re.search(pattern, text):
            return canonical
    return None


def normalize_rationale(value) -> list[str]:
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return []
    cleaned: list[str] = []
    for item in value:
        if not isinstance(item, str):
            continue
        canonical = _normalize_rationale_item(item)
        if canonical:
            cleaned.append(canonical)
    return _priority_sort(cleaned, RATIONALE_PRIORITY)


def heuristic_classify(payload: dict) -> dict:
    text = text_blob(payload)
    title = (payload.get("title") or "").lower()
    category = (payload.get("category") or "").lower()
    current_price = payload.get("current_price")

    difficulty_score = 0
    risk_score = 0
    focus_hints: list[str] = []
    rationale: list[str] = []
    ambiguity_reasons: list[str] = []

    if isinstance(current_price, (int, float)) and (current_price >= 0.85 or current_price <= 0.15):
        difficulty_score += 1
        risk_score += 1
        focus_hints.append("extra_verification")
        rationale.append("extreme_market_probability")

    if has_any(DATE_PATTERNS, text):
        difficulty_score += 1
        risk_score += 1
        focus_hints.append("date_timing_check")
        rationale.append("date_sensitive_resolution")

    has_exclusions = has_any(EXCLUSION_PATTERNS, text)
    if has_exclusions:
        difficulty_score += 1
        risk_score += 2
        focus_hints.append("resolution_audit")
        rationale.append("explicit_exclusion_rules")

    has_attribution = has_any(ATTRIBUTION_PATTERNS, text)
    if has_attribution:
        difficulty_score += 1
        risk_score += 1
        focus_hints.append("attribution_check")
        rationale.append("attribution_requirement")

    has_consensus_reporting = has_any(CONSENSUS_PATTERNS, text)
    has_authoritative_fallback = has_any(AUTHORITATIVE_FALLBACK_PATTERNS, text)
    has_settlement_mechanics = has_any(SETTLEMENT_MECHANICS_PATTERNS, text)
    if has_consensus_reporting:
        difficulty_score += 1
        risk_score += 2
        focus_hints.append("source_of_truth_check")
        rationale.append("consensus_reporting_dependency")

    if has_any(MULTI_CONDITION_PATTERNS, text):
        difficulty_score += 1
        risk_score += 1
        focus_hints.append("multi_condition_check")
        rationale.append("multi_condition_contract")

    geo_strong_matches = count_matches(GEO_STRONG_PATTERNS, text)
    geo_weak_matches = count_matches(GEO_WEAK_PATTERNS, text)
    geo_category = category in {"geopolitics", "politics", "world", "news"}
    geoish = geo_category or geo_strong_matches >= 1 or (geo_strong_matches >= 1 and geo_weak_matches >= 1) or geo_weak_matches >= 2
    if geoish:
        difficulty_score += 1
        risk_score += 1
        focus_hints.append("independent_confirmation")
        rationale.append("geopolitics_reporting_sensitivity")

    official_source_like = has_any(OFFICIAL_SOURCE_PATTERNS, text) or any(
        token in title for token in ["netflix", "youtube", "settle at", "top 10", "box office", "box score", "subscribers"]
    )
    if official_source_like:
        focus_hints.append("authoritative_source_first")
        rationale.append("authoritative_source_available")
        difficulty_score -= 1
        risk_score -= 1
        if has_authoritative_fallback:
            difficulty_score -= 1
            risk_score -= 1
            rationale.append("authoritative_source_with_fallback")

    difficulty_score = max(difficulty_score, 0)
    risk_score = max(risk_score, 0)

    if difficulty_score >= 4 or risk_score >= 4:
        difficulty_class = "high"
    elif difficulty_score >= 2 or risk_score >= 2:
        difficulty_class = "medium"
    else:
        difficulty_class = "low"

    if risk_score >= 4:
        resolution_risk = "high"
    elif risk_score >= 2:
        resolution_risk = "medium"
    else:
        resolution_risk = "low"

    if official_source_like and has_authoritative_fallback:
        source_of_truth_class = "authoritative_with_fallback"
    elif official_source_like:
        source_of_truth_class = "authoritative_direct"
    elif has_consensus_reporting:
        source_of_truth_class = "consensus_reporting_primary"
    else:
        source_of_truth_class = "multi_source_ambiguous"

    if difficulty_class == "low" and official_source_like and resolution_risk == "low":
        evidence_floor = "1_authoritative"
    elif difficulty_class == "high":
        evidence_floor = "3_meaningful"
    else:
        evidence_floor = "2_meaningful"

    if official_source_like and re.search(r"settle at|official .* chart|official .* top 10|box score|youtube channel", text, re.IGNORECASE):
        focus_hints.append("official_source_verification")

    if has_settlement_mechanics:
        focus_hints.append("settlement_mechanics_check")
        rationale.append("settlement_mechanics_complexity")
        if difficulty_class == "low":
            difficulty_class = "medium"
        if resolution_risk == "low":
            resolution_risk = "medium"
        if evidence_floor == "1_authoritative":
            evidence_floor = "2_meaningful"
        extra_verification_required = True
        ambiguity_reasons.append("structured_settlement_guard")

    if difficulty_class == "high":
        focus_hints.extend(["disconfirming_source_required", "independent_confirmation"])

    extra_verification_required = bool(
        (isinstance(current_price, (int, float)) and (current_price >= 0.85 or current_price <= 0.15))
        or difficulty_class == "high"
        or resolution_risk == "high"
    )

    if difficulty_class == "medium":
        ambiguity_reasons.append("heuristic_medium_band")
    if source_of_truth_class == "authoritative_with_fallback":
        ambiguity_reasons.append("authoritative_source_with_fallback")
    if source_of_truth_class == "multi_source_ambiguous":
        ambiguity_reasons.append("ambiguous_source_of_truth")
    if official_source_like and has_consensus_reporting and difficulty_class != "low":
        ambiguity_reasons.append("official_and_consensus_cues")

    heuristic_confidence = "high"
    if ambiguity_reasons:
        heuristic_confidence = "medium"
    if len(ambiguity_reasons) >= 2:
        heuristic_confidence = "low"

    needs_model_review = bool(ambiguity_reasons)

    focus_hints = normalize_focus_hints(focus_hints)
    rationale = normalize_rationale(rationale)[:6]
    ambiguity_reasons = list(dict.fromkeys(ambiguity_reasons))[:4]

    profile = {
        "difficulty_class": difficulty_class,
        "resolution_risk": resolution_risk,
        "evidence_floor": evidence_floor,
        "extra_verification_required": extra_verification_required,
        "focus_hints": focus_hints,
        "difficulty_rationale": rationale,
        "source_of_truth_class": source_of_truth_class,
        "classifier_source": "heuristic",
        "classifier_model": None,
        "classifier_version": "v3-hybrid-ready",
    }
    validate_profile(profile)
    return {
        "difficulty_profile": profile,
        "heuristic_summary": {
            "needs_model_review": needs_model_review,
            "heuristic_confidence": heuristic_confidence,
            "ambiguity_reasons": ambiguity_reasons,
            "difficulty_score": difficulty_score,
            "risk_score": risk_score,
        },
    }


def build_model_prompt(payload: dict, heuristic_result: dict) -> str:
    instruction = CLASSIFIER_PROMPT_PATH.read_text().strip()
    compact_payload = {
        "title": payload.get("title"),
        "description": payload.get("description"),
        "category": payload.get("category"),
        "platform": payload.get("platform"),
        "current_price": payload.get("current_price"),
        "closes_at": payload.get("closes_at"),
        "resolves_at": payload.get("resolves_at"),
        "slug": payload.get("slug"),
    }
    return (
        instruction
        + "\n\n## Market payload\n"
        + json.dumps(compact_payload, indent=2)
        + "\n\n## Heuristic summary\n"
        + json.dumps(heuristic_result, indent=2)
    )


def validate_profile(profile: dict) -> None:
    if profile.get("difficulty_class") not in VALID_DIFFICULTY:
        raise ValueError("invalid difficulty_class")
    if profile.get("resolution_risk") not in VALID_RISK:
        raise ValueError("invalid resolution_risk")
    if profile.get("evidence_floor") not in VALID_EVIDENCE:
        raise ValueError("invalid evidence_floor")
    if not isinstance(profile.get("extra_verification_required"), bool):
        raise ValueError("extra_verification_required must be boolean")
    if not isinstance(profile.get("focus_hints"), list):
        raise ValueError("focus_hints must be a list")
    if not isinstance(profile.get("difficulty_rationale"), list):
        raise ValueError("difficulty_rationale must be a list")
    source_of_truth_class = profile.get("source_of_truth_class")
    if source_of_truth_class is not None and source_of_truth_class not in VALID_SOURCE_OF_TRUTH:
        raise ValueError("invalid source_of_truth_class")


def model_available(endpoint: str, model: str, timeout_seconds: float) -> tuple[bool, str | None]:
    try:
        tags = ollama_tags(endpoint=endpoint, timeout_seconds=min(timeout_seconds, 3.0))
    except Exception as exc:  # noqa: BLE001
        return False, f"ollama unavailable: {exc}"
    models = tags.get("models") or []
    model_names = {item.get("name") for item in models if isinstance(item, dict)}
    if model not in model_names:
        return False, f"ollama model not installed: {model}"
    return True, None


def _more_conservative_value(heuristic_value: str, model_value: str, order: dict[str, int]) -> str:
    if heuristic_value not in order:
        return model_value
    if model_value not in order:
        return heuristic_value
    return model_value if order[model_value] > order[heuristic_value] else heuristic_value


def merge_focus_hints(heuristic_hints: list[str], model_hints: list[str], *, heuristic_confidence: str, model_confidence: str | None) -> list[str]:
    base = normalize_focus_hints(heuristic_hints or [])
    if model_confidence not in {"medium", "high"}:
        return base[:5]
    extra = normalize_focus_hints(model_hints or [])
    if heuristic_confidence == "high":
        return base[:5]
    merged = _priority_sort(base + extra, FOCUS_HINT_PRIORITY)
    return merged[:5]


def merge_rationale(heuristic_rationale: list[str], model_rationale: list[str], *, heuristic_confidence: str, model_confidence: str | None) -> list[str]:
    base = normalize_rationale(heuristic_rationale or [])
    if model_confidence not in {"medium", "high"}:
        return base[:4]
    extra = normalize_rationale(model_rationale or [])
    if heuristic_confidence == "high":
        return base[:4]
    merged = _priority_sort(base + extra, RATIONALE_PRIORITY)
    return merged[:4]


def merge_source_of_truth_class(heuristic_source: str | None, model_source: str | None, *, heuristic_confidence: str, model_confidence: str | None) -> str | None:
    if heuristic_source not in VALID_SOURCE_OF_TRUTH:
        return model_source if model_source in VALID_SOURCE_OF_TRUTH else heuristic_source
    if model_source not in VALID_SOURCE_OF_TRUTH:
        return heuristic_source
    if heuristic_confidence == "high":
        return heuristic_source
    if heuristic_source == model_source:
        return heuristic_source
    if heuristic_source == "multi_source_ambiguous" and heuristic_confidence == "low" and model_confidence == "high":
        return model_source
    if model_confidence == "high" and SOURCE_OF_TRUTH_ORDER[model_source] > SOURCE_OF_TRUTH_ORDER[heuristic_source]:
        return model_source
    return heuristic_source


def merge_profiles(heuristic_profile: dict, model_profile: dict, *, heuristic_confidence: str, model_confidence: str | None) -> dict:
    merged = dict(heuristic_profile)
    heuristic_hard = heuristic_profile["difficulty_class"] == "high" or heuristic_profile["resolution_risk"] == "high"
    heuristic_mediumish = heuristic_profile["difficulty_class"] == "medium" or heuristic_profile["resolution_risk"] == "medium"
    settlement_guard = "settlement_mechanics_check" in (heuristic_profile.get("focus_hints") or [])
    model_confident = model_confidence in {"medium", "high"}
    detail_lock = heuristic_hard or (settlement_guard and heuristic_mediumish)
    detail_confidence = "high" if detail_lock else heuristic_confidence

    merged["source_of_truth_class"] = merge_source_of_truth_class(
        heuristic_profile.get("source_of_truth_class"),
        model_profile.get("source_of_truth_class"),
        heuristic_confidence=detail_confidence,
        model_confidence=model_confidence,
    )
    merged["focus_hints"] = merge_focus_hints(
        heuristic_profile.get("focus_hints") or [],
        model_profile.get("focus_hints") or [],
        heuristic_confidence=detail_confidence,
        model_confidence=model_confidence,
    )
    merged["difficulty_rationale"] = merge_rationale(
        heuristic_profile.get("difficulty_rationale") or [],
        model_profile.get("difficulty_rationale") or [],
        heuristic_confidence=detail_confidence,
        model_confidence=model_confidence,
    )

    if heuristic_confidence == "high":
        if model_confident:
            if model_profile.get("difficulty_class") in VALID_DIFFICULTY:
                merged["difficulty_class"] = _more_conservative_value(heuristic_profile["difficulty_class"], model_profile["difficulty_class"], DIFFICULTY_ORDER)
            if model_profile.get("resolution_risk") in VALID_RISK:
                merged["resolution_risk"] = _more_conservative_value(heuristic_profile["resolution_risk"], model_profile["resolution_risk"], DIFFICULTY_ORDER)
            if model_profile.get("evidence_floor") in VALID_EVIDENCE:
                merged["evidence_floor"] = _more_conservative_value(heuristic_profile["evidence_floor"], model_profile["evidence_floor"], EVIDENCE_ORDER)
            merged["extra_verification_required"] = bool(heuristic_profile["extra_verification_required"] or model_profile.get("extra_verification_required"))
    elif heuristic_hard:
        if model_profile.get("evidence_floor") == "direct_settlement_required":
            merged["evidence_floor"] = "direct_settlement_required"
        merged["extra_verification_required"] = True
    elif settlement_guard and heuristic_mediumish:
        if model_profile.get("evidence_floor") in VALID_EVIDENCE and model_confident:
            merged["evidence_floor"] = _more_conservative_value(heuristic_profile["evidence_floor"], model_profile["evidence_floor"], EVIDENCE_ORDER)
        merged["difficulty_class"] = heuristic_profile["difficulty_class"]
        merged["resolution_risk"] = heuristic_profile["resolution_risk"]
        merged["extra_verification_required"] = heuristic_profile["extra_verification_required"]
    else:
        if model_confident:
            model_difficulty = model_profile.get("difficulty_class")
            model_risk = model_profile.get("resolution_risk")
            if model_difficulty in VALID_DIFFICULTY:
                if heuristic_mediumish and model_difficulty == "low":
                    merged["difficulty_class"] = heuristic_profile["difficulty_class"]
                elif heuristic_confidence == "low" and model_confidence == "high":
                    merged["difficulty_class"] = model_difficulty
                else:
                    merged["difficulty_class"] = _more_conservative_value(heuristic_profile["difficulty_class"], model_difficulty, DIFFICULTY_ORDER)
            if model_risk in VALID_RISK:
                if heuristic_mediumish and model_risk == "low":
                    merged["resolution_risk"] = heuristic_profile["resolution_risk"]
                elif heuristic_confidence == "low" and model_confidence == "high":
                    merged["resolution_risk"] = model_risk
                else:
                    merged["resolution_risk"] = _more_conservative_value(heuristic_profile["resolution_risk"], model_risk, DIFFICULTY_ORDER)
            if model_profile.get("evidence_floor") in VALID_EVIDENCE:
                if heuristic_confidence == "low" and model_confidence == "high":
                    merged["evidence_floor"] = model_profile["evidence_floor"]
                else:
                    merged["evidence_floor"] = _more_conservative_value(heuristic_profile["evidence_floor"], model_profile["evidence_floor"], EVIDENCE_ORDER)
            if isinstance(model_profile.get("extra_verification_required"), bool):
                if heuristic_confidence == "low" and model_confidence == "high":
                    merged["extra_verification_required"] = model_profile["extra_verification_required"]
                else:
                    merged["extra_verification_required"] = bool(heuristic_profile["extra_verification_required"] or model_profile["extra_verification_required"])

    merged["classifier_source"] = "hybrid"
    merged["classifier_model"] = model_profile.get("classifier_model")
    merged["classifier_version"] = "v3-hybrid"
    validate_profile(merged)
    return merged


def classify(payload: dict, *, mode: str, endpoint: str, model: str, timeout_seconds: float) -> dict:
    heuristic_result = heuristic_classify(payload)
    heuristic_profile = heuristic_result["difficulty_profile"]
    heuristic_summary = heuristic_result["heuristic_summary"]

    result = {
        "difficulty_profile": heuristic_profile,
        "heuristic_profile": dict(heuristic_profile),
        "heuristic_summary": heuristic_summary,
        "model_summary": {
            "used": False,
            "mode": mode,
            "fallback_reason": None,
            "model_confidence": None,
            "merge_policy": "confidence_gated_conservative_v3",
        },
    }

    if mode != "hybrid" or not heuristic_summary.get("needs_model_review"):
        return result

    available, reason = model_available(endpoint, model, timeout_seconds)
    if not available:
        result["model_summary"]["fallback_reason"] = reason
        return result

    prompt = build_model_prompt(payload, heuristic_result)
    try:
        model_result = ollama_generate(endpoint=endpoint, model=model, prompt=prompt, timeout_seconds=timeout_seconds)
    except Exception as exc:  # noqa: BLE001
        result["model_summary"]["fallback_reason"] = str(exc)
        return result

    model_profile = {
        "difficulty_class": model_result.get("difficulty_class"),
        "resolution_risk": model_result.get("resolution_risk"),
        "evidence_floor": model_result.get("evidence_floor"),
        "extra_verification_required": model_result.get("extra_verification_required"),
        "focus_hints": normalize_focus_hints(model_result.get("focus_hints") or []),
        "difficulty_rationale": normalize_rationale(model_result.get("difficulty_rationale") or []),
        "source_of_truth_class": model_result.get("source_of_truth_class"),
        "classifier_source": "hybrid",
        "classifier_model": model,
        "classifier_version": "v3-hybrid",
    }
    try:
        validate_profile(model_profile)
        model_confidence = model_result.get("model_confidence") if model_result.get("model_confidence") in VALID_MODEL_CONFIDENCE else None
        merged_profile = merge_profiles(
            heuristic_profile,
            model_profile,
            heuristic_confidence=heuristic_summary.get("heuristic_confidence") or "low",
            model_confidence=model_confidence,
        )
    except Exception as exc:  # noqa: BLE001
        result["model_summary"] = {
            "used": False,
            "mode": mode,
            "fallback_reason": f"invalid model output: {exc}",
            "model_confidence": model_result.get("model_confidence") if model_result.get("model_confidence") in VALID_MODEL_CONFIDENCE else None,
            "raw_model_result": model_result,
            "merge_policy": "confidence_gated_conservative_v3",
        }
        return result

    result["difficulty_profile"] = merged_profile
    result["model_summary"] = {
        "used": True,
        "mode": mode,
        "fallback_reason": None,
        "model_confidence": model_confidence,
        "raw_model_result": model_result,
        "merge_policy": "confidence_gated_conservative_v3",
    }
    return result


def main() -> int:
    args = parse_args()
    try:
        payload = load_json(args.file)
        if not isinstance(payload, dict):
            raise ValueError("input JSON must be an object")
        result = classify(
            payload,
            mode=args.mode,
            endpoint=args.ollama_endpoint,
            model=args.ollama_model,
            timeout_seconds=args.timeout_seconds,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(json.dumps(result, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
