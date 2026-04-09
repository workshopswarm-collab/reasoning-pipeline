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
        else:
            normalized.append(hint)
    return list(dict.fromkeys(normalized))


def normalize_rationale(value) -> list[str]:
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return []
    cleaned = []
    for item in value:
        if isinstance(item, str) and item.strip():
            cleaned.append(item.strip())
    return list(dict.fromkeys(cleaned))


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
        rationale.append("market-implied probability is extreme")

    if has_any(DATE_PATTERNS, text):
        difficulty_score += 1
        risk_score += 1
        focus_hints.append("date_timing_check")
        rationale.append("date-specific or deadline-sensitive market")

    has_exclusions = has_any(EXCLUSION_PATTERNS, text)
    if has_exclusions:
        difficulty_score += 1
        risk_score += 2
        focus_hints.append("resolution_audit")
        rationale.append("resolution wording contains explicit exclusions or narrow qualifying criteria")

    has_attribution = has_any(ATTRIBUTION_PATTERNS, text)
    if has_attribution:
        difficulty_score += 1
        risk_score += 1
        focus_hints.append("attribution_check")
        rationale.append("contract includes attribution or identity requirements")

    has_consensus_reporting = has_any(CONSENSUS_PATTERNS, text)
    has_authoritative_fallback = has_any(AUTHORITATIVE_FALLBACK_PATTERNS, text)
    has_settlement_mechanics = has_any(SETTLEMENT_MECHANICS_PATTERNS, text)
    if has_consensus_reporting:
        difficulty_score += 1
        risk_score += 2
        focus_hints.append("source_of_truth_check")
        rationale.append("resolution depends on official statements or consensus reporting")

    if has_any(MULTI_CONDITION_PATTERNS, text):
        difficulty_score += 1
        risk_score += 1
        focus_hints.append("multi_condition_check")
        rationale.append("contract appears to require multiple conditions to resolve yes")

    geo_strong_matches = count_matches(GEO_STRONG_PATTERNS, text)
    geo_weak_matches = count_matches(GEO_WEAK_PATTERNS, text)
    geo_category = category in {"geopolitics", "politics", "world", "news"}
    geoish = geo_category or geo_strong_matches >= 1 or (geo_strong_matches >= 1 and geo_weak_matches >= 1) or geo_weak_matches >= 2
    if geoish:
        difficulty_score += 1
        risk_score += 1
        focus_hints.append("independent_confirmation")
        rationale.append("domain appears geopolitics / conflict / public-reporting sensitive")

    official_source_like = has_any(OFFICIAL_SOURCE_PATTERNS, text) or any(
        token in title for token in ["netflix", "youtube", "settle at", "top 10", "box office", "box score", "subscribers"]
    )
    if official_source_like:
        focus_hints.append("authoritative_source_first")
        rationale.append("market may be resolvable from an authoritative source-of-truth surface")
        difficulty_score -= 1
        risk_score -= 1
        if has_authoritative_fallback:
            difficulty_score -= 1
            risk_score -= 1
            rationale.append("authoritative source appears primary and consensus reporting looks like fallback language")

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
        rationale.append("resolution depends on structured settlement mechanics rather than a simple point-in-time reading")
        if difficulty_class == "low":
            difficulty_class = "medium"
        if resolution_risk == "low":
            resolution_risk = "medium"
        if evidence_floor == "1_authoritative":
            evidence_floor = "2_meaningful"
        extra_verification_required = True
        ambiguity_reasons.append("structured settlement mechanics warrant conservative classification")

    if difficulty_class == "high":
        focus_hints.extend(["disconfirming_source_required", "independent_confirmation"])

    extra_verification_required = bool(
        (isinstance(current_price, (int, float)) and (current_price >= 0.85 or current_price <= 0.15))
        or difficulty_class == "high"
        or resolution_risk == "high"
    )

    if difficulty_class == "medium":
        ambiguity_reasons.append("heuristic classification landed in medium band")
    if source_of_truth_class == "authoritative_with_fallback":
        ambiguity_reasons.append("authoritative source with fallback reporting may be over- or under-classified")
    if source_of_truth_class == "multi_source_ambiguous":
        ambiguity_reasons.append("source of truth classification is ambiguous")
    if official_source_like and has_consensus_reporting and difficulty_class != "low":
        ambiguity_reasons.append("official-source cues and consensus-reporting cues both present")

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
        "classifier_version": "v2-hybrid-ready",
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


def merge_profiles(heuristic_profile: dict, model_profile: dict) -> dict:
    merged = dict(heuristic_profile)

    # Safe refinement: preserve conservative heuristic defaults on edge cases.
    for key in ["source_of_truth_class", "focus_hints", "difficulty_rationale"]:
        if key in model_profile:
            merged[key] = model_profile[key]

    heuristic_hard = heuristic_profile["difficulty_class"] == "high" or heuristic_profile["resolution_risk"] == "high"
    heuristic_mediumish = heuristic_profile["difficulty_class"] == "medium" or heuristic_profile["resolution_risk"] == "medium"
    model_difficulty = model_profile.get("difficulty_class")
    model_risk = model_profile.get("resolution_risk")
    settlement_guard = "settlement_mechanics_check" in (heuristic_profile.get("focus_hints") or [])

    if heuristic_hard:
        # For obvious hard cases, allow stricter but not looser adjustments.
        if model_profile.get("evidence_floor") == "direct_settlement_required":
            merged["evidence_floor"] = "direct_settlement_required"
        merged["extra_verification_required"] = True
    elif settlement_guard and heuristic_mediumish:
        # Settlement-mechanics markets should not be casually downgraded to low.
        if model_profile.get("evidence_floor") in VALID_EVIDENCE:
            merged["evidence_floor"] = model_profile["evidence_floor"]
        merged["difficulty_class"] = heuristic_profile["difficulty_class"]
        merged["resolution_risk"] = heuristic_profile["resolution_risk"]
        merged["extra_verification_required"] = heuristic_profile["extra_verification_required"]
    else:
        # Conservative merge: prefer medium/high over low on edge cases.
        if model_difficulty in VALID_DIFFICULTY:
            if heuristic_mediumish and model_difficulty == "low":
                merged["difficulty_class"] = heuristic_profile["difficulty_class"]
            else:
                merged["difficulty_class"] = model_difficulty
        if model_risk in VALID_RISK:
            if heuristic_mediumish and model_risk == "low":
                merged["resolution_risk"] = heuristic_profile["resolution_risk"]
            else:
                merged["resolution_risk"] = model_risk
        if model_profile.get("evidence_floor") in VALID_EVIDENCE:
            merged["evidence_floor"] = model_profile["evidence_floor"]
        if isinstance(model_profile.get("extra_verification_required"), bool):
            if heuristic_mediumish and model_profile.get("extra_verification_required") is False:
                merged["extra_verification_required"] = heuristic_profile["extra_verification_required"]
            else:
                merged["extra_verification_required"] = model_profile["extra_verification_required"]

    merged["classifier_source"] = "hybrid"
    merged["classifier_model"] = model_profile.get("classifier_model")
    merged["classifier_version"] = "v2-hybrid"
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
        "classifier_version": "v2-hybrid",
    }
    try:
        validate_profile(model_profile)
        merged_profile = merge_profiles(heuristic_profile, model_profile)
    except Exception as exc:  # noqa: BLE001
        result["model_summary"] = {
            "used": False,
            "mode": mode,
            "fallback_reason": f"invalid model output: {exc}",
            "model_confidence": model_result.get("model_confidence") if model_result.get("model_confidence") in VALID_MODEL_CONFIDENCE else None,
            "raw_model_result": model_result,
        }
        return result

    result["difficulty_profile"] = merged_profile
    result["model_summary"] = {
        "used": True,
        "mode": mode,
        "fallback_reason": None,
        "model_confidence": model_result.get("model_confidence") if model_result.get("model_confidence") in VALID_MODEL_CONFIDENCE else None,
        "raw_model_result": model_result,
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
