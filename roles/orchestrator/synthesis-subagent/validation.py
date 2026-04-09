from __future__ import annotations

from typing import Any

from common import (
    SECTION_ORDER,
    SYNTHESIZER_ENUMS,
    coerce_string,
    normalize_probability,
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
REASONING_SIDECAR_REASONING_MODE_ENUM = {
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
REASONING_SIDECAR_CONFIDENCE_ENUM = {"low", "medium", "high"}
REASONING_SIDECAR_REQUIRED_FIELDS = [
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
REASONING_SIDECAR_OPTIONAL_FIELDS = {
    "quote_anchors",
    "runtime_metadata",
    "artifact_type",
    "schema_version",
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
REASONING_SIDECAR_RUNTIME_METADATA_REQUIRED_FIELDS = {
    "generation_mode",
    "case_key",
    "dispatch_id",
    "research_run_id",
    "source_persona_finding_path",
    "source_persona_sha256",
    "prompt_contract_version",
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


def reasoning_sidecar_core_payload(payload: Any) -> Any:
    if not isinstance(payload, dict):
        return payload
    stripped = dict(payload)
    stripped.pop("runtime_metadata", None)
    stripped.pop("artifact_type", None)
    stripped.pop("schema_version", None)
    return stripped


def validate_reasoning_sidecar_payload(payload: Any) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(payload, dict):
        return {"ok": False, "errors": ["top-level payload must be a JSON object"], "warnings": []}

    artifact_type = coerce_string(payload.get("artifact_type"))
    if artifact_type and artifact_type != "persona_reasoning_sidecar":
        errors.append(f"invalid artifact_type for reasoning sidecar: {artifact_type}")

    schema_version = coerce_string(payload.get("schema_version"))
    if schema_version and schema_version != "v1":
        warnings.append(f"unexpected reasoning sidecar schema_version: {schema_version}")

    core = reasoning_sidecar_core_payload(payload)
    if not isinstance(core, dict):
        return {"ok": False, "errors": ["reasoning sidecar core payload must be a JSON object"], "warnings": warnings}

    unknown_fields = sorted(set(core.keys()) - set(REASONING_SIDECAR_REQUIRED_FIELDS) - (REASONING_SIDECAR_OPTIONAL_FIELDS - {"artifact_type", "schema_version", "runtime_metadata"}))
    if unknown_fields:
        warnings.extend(f"unknown reasoning-sidecar field: {field}" for field in unknown_fields)

    for field in REASONING_SIDECAR_REQUIRED_FIELDS:
        if field not in core:
            errors.append(f"missing reasoning-sidecar field: {field}")

    for field in [
        "persona",
        "main_thesis",
        "timing_relevance",
        "source_quality_view",
        "what_would_change_view",
    ]:
        if field in core and not isinstance(core.get(field), str):
            errors.append(f"field must be a string: {field}")

    own_probability = core.get("own_probability")
    if own_probability not in (None, "") and normalize_probability(own_probability) is None:
        errors.append("own_probability must be blank or a decimal probability in [0,1]")

    reasoning_mode = core.get("reasoning_mode")
    if "reasoning_mode" in core:
        if not isinstance(reasoning_mode, list):
            errors.append("reasoning_mode must be a list")
        else:
            for item in reasoning_mode:
                if not isinstance(item, str):
                    errors.append("reasoning_mode entries must be strings")
                    continue
                if item not in REASONING_SIDECAR_REASONING_MODE_ENUM:
                    errors.append(f"invalid reasoning_mode entry: {item}")

    for field in [
        "key_assumptions",
        "strongest_supports",
        "strongest_disconfirmers",
        "main_logical_chain",
        "fragility_points",
        "unresolved_ambiguities",
    ]:
        value = core.get(field)
        if field in core:
            if not isinstance(value, list):
                errors.append(f"field must be a list: {field}")
            elif any(not isinstance(item, str) for item in value):
                errors.append(f"all entries must be strings: {field}")
            elif not value:
                warnings.append(f"reasoning-sidecar list is empty: {field}")

    quote_anchors = core.get("quote_anchors")
    if quote_anchors is not None:
        if not isinstance(quote_anchors, list):
            errors.append("quote_anchors must be a list when present")
        elif any(not isinstance(item, str) for item in quote_anchors):
            errors.append("all quote_anchors entries must be strings")

    for field in ["recommended_weight", "confidence_in_extract"]:
        value = coerce_string(core.get(field))
        if field in core and value not in REASONING_SIDECAR_CONFIDENCE_ENUM:
            errors.append(f"invalid enum for {field}: {value or '[blank]'}")

    runtime_metadata = payload.get("runtime_metadata")
    if not isinstance(runtime_metadata, dict):
        errors.append("missing runtime_metadata on reasoning sidecar artifact")
    else:
        missing_runtime_fields = sorted(field for field in REASONING_SIDECAR_RUNTIME_METADATA_REQUIRED_FIELDS if field not in runtime_metadata)
        if missing_runtime_fields:
            errors.extend(f"missing runtime_metadata field: {field}" for field in missing_runtime_fields)

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "runtime_metadata": runtime_metadata if isinstance(runtime_metadata, dict) else {},
        "required_fields": list(REASONING_SIDECAR_REQUIRED_FIELDS),
        "optional_fields": sorted(REASONING_SIDECAR_OPTIONAL_FIELDS),
    }


def validate_reasoning_sidecar_artifact(payload: Any, *, persona_finding_path: str, source_persona_sha256: str, persona: str | None = None) -> dict[str, Any]:
    structural = validate_reasoning_sidecar_payload(payload)
    errors = list(structural["errors"])
    warnings = list(structural["warnings"])

    if not isinstance(payload, dict):
        return {"ok": False, "errors": errors, "warnings": warnings}

    runtime_metadata = payload.get("runtime_metadata") or {}
    if runtime_metadata.get("source_persona_sha256") != source_persona_sha256:
        errors.append("reasoning sidecar artifact is stale: source_persona_sha256 does not match current persona input")
    if runtime_metadata.get("source_persona_finding_path") != persona_finding_path:
        warnings.append("runtime_metadata source_persona_finding_path differs from current persona finding path")
    if persona is not None and coerce_string(payload.get("persona")) != coerce_string(persona):
        errors.append("reasoning sidecar persona does not match expected persona")

    own_probability = None
    if isinstance(payload, dict):
        core_payload = reasoning_sidecar_core_payload(payload)
        if isinstance(core_payload, dict):
            own_probability = normalize_probability(core_payload.get("own_probability"))
    if own_probability is None:
        warnings.append("reasoning sidecar own_probability is blank or invalid")

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "runtime_metadata": runtime_metadata,
    }
