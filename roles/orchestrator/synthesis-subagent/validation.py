from __future__ import annotations

from typing import Any

from common import (
    SECTION_ORDER,
    SYNTHESIZER_ENUMS,
    coerce_string,
    normalize_probability,
    reasoning_extract_job_input_fingerprint,
    sha256_text,
)

TOP_LEVEL_KEYS = {"claim", "frontmatter", "sections"}
ALLOWED_SYNTHESIZER_FRONTMATTER_FIELDS = {
    "coverage_status",
    "syndicated_probability_low",
    "syndicated_probability_high",
    "edge_independent_verification_quality",
    "compressed_toward_market_due_to_verification",
    "disagreement_intensity",
    "synthesis_confidence_quality",
    "staleness_risk",
    "next_checkpoint",
    "follow_up_needed",
}
RUNTIME_MANAGED_FIELDS = {
    "type",
    "case_key",
    "dispatch_id",
    "question",
    "market_implied_probability",
    "syndicated_probability_midpoint",
    "edge_vs_market_pct_points",
    "relation_to_market",
    "edge_quality",
}
REASONING_EXTRACT_REASONING_MODE_ENUM = {
    "base_rate",
    "market_anchor",
    "scenario_analysis",
    "catalyst_analysis",
    "risk_management",
    "contract_interpretation",
    "variant_hypothesis",
    "technical_reference",
    "other",
}
REASONING_EXTRACT_CONFIDENCE_ENUM = {"low", "medium", "high"}
REASONING_EXTRACT_REQUIRED_FIELDS = [
    "persona",
    "main_thesis",
    "own_probability",
    "reasoning_mode",
    "key_assumptions",
    "strongest_supports",
    "strongest_disconfirmers",
    "main_logical_chain",
    "fragility_points",
    "unresolved_ambiguities",
    "timing_relevance",
    "source_quality_view",
    "what_would_change_view",
    "recommended_weight",
    "confidence_in_extract",
]
REASONING_EXTRACT_OPTIONAL_FIELDS = {
    "quote_anchors",
    "runtime_metadata",
}
RECOMMENDED_NONEMPTY_SECTIONS = {
    "Alpha summary",
    "Input coverage",
    "Syndicated probability estimate",
    "Difference from swarm-implied center",
    "Independent verification of edge",
    "Compression toward market due to verification",
    "Consensus across personas",
    "Key disagreements across personas",
    "Best countercase",
    "Recommended follow-up",
}

RUNTIME_METADATA_REQUIRED_FIELDS = {
    "extraction_mode",
    "extracted_at",
    "source_persona_finding_path",
    "source_persona_sha256",
    "job_input_sha256",
    "prompt_sha256",
}


def validate_synthesis_result_payload(payload: Any) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(payload, dict):
        return {"ok": False, "errors": ["top-level payload must be a JSON object"], "warnings": []}

    unknown_top_level = sorted(set(payload.keys()) - TOP_LEVEL_KEYS)
    if unknown_top_level:
        warnings.append(f"unknown top-level keys: {', '.join(unknown_top_level)}")

    missing_top_level = [key for key in ["claim", "frontmatter", "sections"] if key not in payload]
    if missing_top_level:
        errors.extend(f"missing top-level key: {key}" for key in missing_top_level)

    claim = payload.get("claim")
    if claim is not None and not isinstance(claim, str):
        errors.append("claim must be a string")

    frontmatter = payload.get("frontmatter")
    if frontmatter is None:
        frontmatter = {}
    if not isinstance(frontmatter, dict):
        errors.append("frontmatter must be an object")
        frontmatter = {}

    sections = payload.get("sections")
    if sections is None:
        sections = {}
    if not isinstance(sections, dict):
        errors.append("sections must be an object")
        sections = {}

    supplied_fields = set(frontmatter.keys())
    runtime_managed_supplied = sorted(supplied_fields & RUNTIME_MANAGED_FIELDS)
    if runtime_managed_supplied:
        errors.extend(f"runtime-managed field supplied by synthesizer: {field}" for field in runtime_managed_supplied)

    unknown_frontmatter = sorted(supplied_fields - ALLOWED_SYNTHESIZER_FRONTMATTER_FIELDS - RUNTIME_MANAGED_FIELDS)
    if unknown_frontmatter:
        warnings.extend(f"unknown frontmatter field supplied by synthesizer: {field}" for field in unknown_frontmatter)

    for field in [
        "coverage_status",
        "syndicated_probability_low",
        "syndicated_probability_high",
        "edge_independent_verification_quality",
        "compressed_toward_market_due_to_verification",
        "disagreement_intensity",
        "synthesis_confidence_quality",
        "staleness_risk",
        "next_checkpoint",
        "follow_up_needed",
    ]:
        if field not in frontmatter:
            errors.append(f"missing synthesizer frontmatter field: {field}")

    for field, allowed in SYNTHESIZER_ENUMS.items():
        if field in frontmatter:
            value = coerce_string(frontmatter.get(field))
            if value not in allowed:
                errors.append(f"invalid enum for {field}: {value or '[blank]'}")

    low = normalize_probability(frontmatter.get("syndicated_probability_low"))
    high = normalize_probability(frontmatter.get("syndicated_probability_high"))
    if low is None:
        errors.append("missing or invalid syndicated_probability_low")
    if high is None:
        errors.append("missing or invalid syndicated_probability_high")
    if low is not None and high is not None and low > high:
        errors.append("syndicated_probability_low is greater than syndicated_probability_high")

    unknown_sections = sorted(set(sections.keys()) - set(SECTION_ORDER))
    if unknown_sections:
        warnings.extend(f"unknown section key: {section}" for section in unknown_sections)

    for section in SECTION_ORDER:
        if section not in sections:
            errors.append(f"missing section key: {section}")
            continue
        if not isinstance(sections.get(section), str):
            errors.append(f"section must be a string: {section}")
            continue
        if section in RECOMMENDED_NONEMPTY_SECTIONS and not sections[section].strip():
            warnings.append(f"recommended section is empty: {section}")

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "allowed_frontmatter_fields": sorted(ALLOWED_SYNTHESIZER_FRONTMATTER_FIELDS),
        "runtime_managed_fields": sorted(RUNTIME_MANAGED_FIELDS),
        "section_order": list(SECTION_ORDER),
    }


def reasoning_extract_core_payload(payload: Any) -> Any:
    if isinstance(payload, dict) and isinstance(payload.get("runtime_metadata"), dict):
        stripped = dict(payload)
        stripped.pop("runtime_metadata", None)
        return stripped
    return payload


def validate_reasoning_extract_payload(payload: Any) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    payload = reasoning_extract_core_payload(payload)
    if not isinstance(payload, dict):
        return {"ok": False, "errors": ["top-level payload must be a JSON object"], "warnings": []}

    unknown_fields = sorted(set(payload.keys()) - set(REASONING_EXTRACT_REQUIRED_FIELDS) - REASONING_EXTRACT_OPTIONAL_FIELDS)
    if unknown_fields:
        warnings.extend(f"unknown reasoning-extract field: {field}" for field in unknown_fields)

    for field in REASONING_EXTRACT_REQUIRED_FIELDS:
        if field not in payload:
            errors.append(f"missing reasoning-extract field: {field}")

    for field in [
        "persona",
        "main_thesis",
        "timing_relevance",
        "source_quality_view",
        "what_would_change_view",
    ]:
        if field in payload and not isinstance(payload.get(field), str):
            errors.append(f"field must be a string: {field}")

    own_probability = payload.get("own_probability")
    if own_probability not in (None, "") and normalize_probability(own_probability) is None:
        errors.append("own_probability must be blank or a decimal probability in [0,1]")

    reasoning_mode = payload.get("reasoning_mode")
    if "reasoning_mode" in payload:
        if not isinstance(reasoning_mode, list):
            errors.append("reasoning_mode must be a list")
        else:
            for item in reasoning_mode:
                if not isinstance(item, str):
                    errors.append("reasoning_mode entries must be strings")
                    continue
                if item not in REASONING_EXTRACT_REASONING_MODE_ENUM:
                    errors.append(f"invalid reasoning_mode entry: {item}")

    for field in [
        "key_assumptions",
        "strongest_supports",
        "strongest_disconfirmers",
        "main_logical_chain",
        "fragility_points",
        "unresolved_ambiguities",
    ]:
        value = payload.get(field)
        if field in payload:
            if not isinstance(value, list):
                errors.append(f"field must be a list: {field}")
            elif any(not isinstance(item, str) for item in value):
                errors.append(f"all entries must be strings: {field}")
            elif not value:
                warnings.append(f"reasoning-extract list is empty: {field}")

    quote_anchors = payload.get("quote_anchors")
    if quote_anchors is not None:
        if not isinstance(quote_anchors, list):
            errors.append("quote_anchors must be a list when present")
        elif any(not isinstance(item, str) for item in quote_anchors):
            errors.append("all quote_anchors entries must be strings")

    for field in ["recommended_weight", "confidence_in_extract"]:
        value = coerce_string(payload.get(field))
        if field in payload and value not in REASONING_EXTRACT_CONFIDENCE_ENUM:
            errors.append(f"invalid enum for {field}: {value or '[blank]'}")

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "required_fields": list(REASONING_EXTRACT_REQUIRED_FIELDS),
        "optional_fields": sorted(REASONING_EXTRACT_OPTIONAL_FIELDS),
    }


def validate_reasoning_extract_artifact(payload: Any, *, job: dict[str, Any], prompt_text: str | None = None) -> dict[str, Any]:
    structural = validate_reasoning_extract_payload(payload)
    errors = list(structural["errors"])
    warnings = list(structural["warnings"])

    if not isinstance(payload, dict):
        return {"ok": False, "errors": errors, "warnings": warnings}

    runtime_metadata = payload.get("runtime_metadata")
    if not isinstance(runtime_metadata, dict):
        errors.append("missing runtime_metadata on reasoning extract artifact")
        return {"ok": False, "errors": errors, "warnings": warnings}

    missing_runtime_fields = sorted(field for field in RUNTIME_METADATA_REQUIRED_FIELDS if field not in runtime_metadata)
    if missing_runtime_fields:
        errors.extend(f"missing runtime_metadata field: {field}" for field in missing_runtime_fields)

    expected_source_sha = job.get("persona_source_sha256") or ""
    if expected_source_sha and runtime_metadata.get("source_persona_sha256") != expected_source_sha:
        errors.append("reasoning extract artifact is stale: source_persona_sha256 does not match current persona input")

    expected_job_sha = reasoning_extract_job_input_fingerprint(job)
    if runtime_metadata.get("job_input_sha256") != expected_job_sha:
        errors.append("reasoning extract artifact is stale: job_input_sha256 does not match current extraction job input")

    if prompt_text is not None:
        expected_prompt_sha = sha256_text(prompt_text)
        if runtime_metadata.get("prompt_sha256") != expected_prompt_sha:
            errors.append("reasoning extract artifact is stale: prompt_sha256 does not match current extraction prompt")

    expected_source_path = job.get("persona_finding_path") or ""
    if expected_source_path and runtime_metadata.get("source_persona_finding_path") != expected_source_path:
        warnings.append("runtime_metadata source_persona_finding_path differs from current job path")

    explicit_prob = normalize_probability(job.get("persona_explicit_probability"))
    extract_prob = normalize_probability(reasoning_extract_core_payload(payload).get("own_probability") if isinstance(reasoning_extract_core_payload(payload), dict) else None)
    if explicit_prob is not None and extract_prob is not None:
        diff = abs(explicit_prob - extract_prob)
        if diff >= 0.12:
            errors.append(
                f"reasoning extract own_probability materially disagrees with explicit raw persona probability ({extract_prob:.4f} vs {explicit_prob:.4f})"
            )
        elif diff >= 0.05:
            warnings.append(
                f"reasoning extract own_probability differs noticeably from explicit raw persona probability ({extract_prob:.4f} vs {explicit_prob:.4f})"
            )

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "runtime_metadata": runtime_metadata,
    }
