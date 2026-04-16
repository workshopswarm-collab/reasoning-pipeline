#!/usr/bin/env python3
from __future__ import annotations

"""Build a compact persona-specific researcher prompt for one case.

The runtime prompt is intentionally concise to reduce drift and startup overhead.
It encodes the live operating brief directly and points to longer repo docs only
when the researcher truly needs extra formatting or governance detail.
"""

import argparse
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = BASE_DIR.parents[4]
PROMPTS_DIR = BASE_DIR.parent / "prompts"
BASE_CONTRACT_PATH = PROMPTS_DIR / "researcher_base_contract.md"
AGENT_FINDING_TEMPLATE_PATH = WORKSPACE_ROOT / "qualitative-db/00-system/templates/agent-finding-template.md"
SOURCE_NOTE_TEMPLATE_PATH = WORKSPACE_ROOT / "qualitative-db/00-system/templates/source-note-template.md"
ASSUMPTION_NOTE_TEMPLATE_PATH = WORKSPACE_ROOT / "qualitative-db/00-system/templates/assumption-note-template.md"
EVIDENCE_MAP_TEMPLATE_PATH = WORKSPACE_ROOT / "qualitative-db/00-system/templates/evidence-map-template.md"
PERSONA_FILES = {
    "base-rate": PROMPTS_DIR / "researcher_base-rate.md",
    "market-implied": PROMPTS_DIR / "researcher_market-implied.md",
    "variant-view": PROMPTS_DIR / "researcher_variant-view.md",
    "risk-manager": PROMPTS_DIR / "researcher_risk-manager.md",
    "catalyst-hunter": PROMPTS_DIR / "researcher_catalyst-hunter.md",
}
PERSONA_BRIEFS = {
    "base-rate": [
        "Start from historical frequency, structural constraints, and outside-view priors.",
        "Be skeptical of vivid narratives unless they clearly overwhelm the prior.",
        "Ask what usually happens in analogous setups before focusing on why this case may differ.",
    ],
    "market-implied": [
        "Infer what the current price seems to be assuming and whether public evidence supports that assumption.",
        "Identify what the market may already know versus what seems under- or over-weighted.",
        "Explain whether the price looks efficient, early, stale, or overextended.",
    ],
    "variant-view": [
        "Look for the strongest credible alternative to the obvious consensus narrative.",
        "Surface neglected mechanisms, hidden conditionals, or asymmetric outcomes.",
        "Do not force contrarianism; only develop a variant view if it is genuinely supported.",
    ],
    "risk-manager": [
        "Focus on failure modes, disconfirming evidence, and what could break the current thesis.",
        "Highlight fragility, missing assumptions, and scenario tails that matter for resolution.",
        "State what evidence would most quickly invalidate the current working view.",
    ],
    "catalyst-hunter": [
        "Focus on upcoming catalysts, timelines, and concrete events that could move the market or resolution path.",
        "Distinguish soft narrative catalysts from events that genuinely change probabilities.",
        "Emphasize timing, sequencing, and what should be watched next.",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a researcher spawn prompt")
    parser.add_argument("--file", default="-", help="Path to input JSON file, or - for stdin")
    parser.add_argument("--agent-label", help="Research persona label")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output instead of plain prompt text")
    return parser.parse_args()


def load_json(path_str: str):
    if path_str == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path_str).read_text()
    if not raw.strip():
        raise ValueError("input JSON is empty")
    return json.loads(raw)


def require(payload: dict, key: str):
    value = payload.get(key)
    if value is None or value == "":
        raise ValueError(f"missing required field: {key}")
    return value


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


def humanize_hint(hint: str) -> str:
    return hint.replace("_", " ").strip()


def normalize_focus_hints(focus_hints: list[str]) -> tuple[list[str], list[str]]:
    normalized: list[str] = []
    custom: list[str] = []
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
            custom.append(hint)
    normalized = list(dict.fromkeys(normalized))
    custom = list(dict.fromkeys(custom))
    return normalized, custom


def default_rationale_lines(difficulty_profile: dict, custom_hints: list[str] | None = None) -> list[str]:
    difficulty_class = difficulty_profile.get("difficulty_class") or "unknown"
    resolution_risk = difficulty_profile.get("resolution_risk") or "unknown"
    source_of_truth_class = difficulty_profile.get("source_of_truth_class") or "unknown"
    lines: list[str] = []

    if difficulty_class == "high":
        lines.append("case requires elevated rigor because contract semantics or evidence verification can materially change the answer")
    elif difficulty_class == "medium":
        lines.append("case is not trivially self-settling and needs more than a thin narrative memo")
    elif difficulty_class == "low":
        lines.append("case appears comparatively straightforward, but still requires explicit market comparison and auditable provenance")

    if resolution_risk == "high":
        lines.append("resolution wording or source-of-truth interpretation materially affects the answer")
    elif resolution_risk == "medium":
        lines.append("resolution or source-of-truth handling is structured enough to warrant explicit checking")

    if source_of_truth_class == "authoritative_direct":
        lines.append("a direct authoritative source seems available and should anchor the run")
    elif source_of_truth_class == "authoritative_with_fallback":
        lines.append("an authoritative source appears primary, but fallback reporting logic still matters")
    elif source_of_truth_class == "consensus_reporting_primary":
        lines.append("the case depends heavily on public-reporting verification rather than a single settlement surface")
    elif source_of_truth_class == "multi_source_ambiguous":
        lines.append("the governing source-of-truth is not fully explicit, so provenance should be especially legible")

    if custom_hints:
        lines.append("the classifier surfaced additional case-specific checks that should not be ignored")

    return list(dict.fromkeys(lines))[:4]


LMD_CHECK_INSTRUCTIONS = {
    "verify_primary_resolution_source": "verify the primary resolution / governing source directly before finalizing",
    "capture_governing_source_proof_when_event_near_complete": "capture explicit governing-source proof when the event appears near-complete",
    "separate_resolution_risk_from_path_probability": "separate resolution-risk uncertainty from path-probability uncertainty explicitly",
    "label_unverified_vs_not_occurred_distinctly": "distinguish 'not yet verified' from 'not yet occurred' explicitly",
    "confirm_any_qualifying_touch_resolves_yes": "confirm whether any qualifying touch resolves Yes before applying discretionary discounts",
    "evaluate_distance_to_threshold": "evaluate the remaining distance to the threshold explicitly",
    "evaluate_time_remaining_and_path_volatility": "evaluate remaining time and path volatility explicitly",
    "justify_any_resistance_discount_explicitly": "justify any resistance- or reversal-based discount explicitly rather than implying it",
    "label_event_state": "label the event-state explicitly",
    "label_verification_state": "label the verification-state explicitly",
}


def humanize_check_key(check_key: str) -> str:
    return LMD_CHECK_INSTRUCTIONS.get(check_key, check_key.replace('_', ' ').strip())


def build_completion_checklist(difficulty_profile: dict, *, lmd_required_checks: list[str] | None = None) -> str:
    if not difficulty_profile and not lmd_required_checks:
        return ""

    difficulty_class = difficulty_profile.get("difficulty_class") or "unknown"
    resolution_risk = difficulty_profile.get("resolution_risk") or "unknown"
    evidence_floor = difficulty_profile.get("evidence_floor") or "unknown"
    extra_verification_required = bool(difficulty_profile.get("extra_verification_required"))
    normalized_hints, custom_hints = normalize_focus_hints(difficulty_profile.get("focus_hints") or [])

    bullets = [
        "state both the market-implied probability and your own probability estimate",
        "name the strongest disconfirming evidence or consideration explicitly",
        "state what could still change your mind",
        "identify the governing source of truth explicitly, even if the case is otherwise simple",
        "perform an explicit canonical-mapping check for entities and drivers; if any causally or structurally important item lacks a clean canonical slug, record it in proposed_entities or proposed_drivers instead of forcing a weak fit",
        "include a source-quality assessment section covering the primary source, key secondary/contextual source, evidence independence, and source-of-truth ambiguity",
        "include a verification impact section stating whether extra verification was performed and whether it materially changed the view",
        "include a reusable lesson signals section even if the answer is 'none' or low-confidence",
        "include an Orchestrator review suggestions section even if the answer is 'no follow-up suggested'",
        "label your compliance clearly in the finding so later evaluation can tell how you met the evidence floor",
        "make your provenance legible enough that later evaluation can tell why this run should be trusted",
    ]

    if evidence_floor == "1_authoritative":
        bullets.append("verify at least one authoritative or direct source-of-truth surface, and say what it is")
        bullets.append("if the contract mechanics are nontrivial, add at least one contextual or verification source rather than relying on a bare single-source memo")
    elif evidence_floor == "2_meaningful":
        bullets.append("use at least two meaningful sources, ideally independent or one primary plus one strong contextual source")
    elif evidence_floor == "3_meaningful":
        bullets.append("use at least three meaningful sources unless one authoritative source directly settles the question")
        bullets.append("preserve visible provenance for those sources via source notes, an evidence map, or a clearly enumerated source list in the finding")
    elif evidence_floor == "direct_settlement_required":
        bullets.append("confirm the answer from the direct settlement / governing source before finalizing")

    if difficulty_class == "high":
        bullets.append("preserve enough artifact structure that a later reviewer can audit how you met the evidence floor")
    elif difficulty_class == "medium":
        bullets.append("do not default to a single-source memo unless the market is directly settled by an authoritative source")

    if resolution_risk == "high" or "resolution_audit" in normalized_hints:
        bullets.append("explicitly explain what counts, what does not count, and how the contract wording affects your view")
    if extra_verification_required or "extra_verification" in normalized_hints:
        bullets.append("perform and reflect an additional verification pass before finishing")
    if lmd_required_checks:
        for check_key in lmd_required_checks:
            if not isinstance(check_key, str) or not check_key.strip():
                continue
            bullets.append(f"reviewed mechanism-specific check: {humanize_check_key(check_key.strip())}")
    if "date_timing_check" in normalized_hints:
        bullets.append("verify the relevant date, deadline, timezone, or reporting window explicitly")
    if "attribution_check" in normalized_hints:
        bullets.append("verify attribution / origin requirements explicitly rather than assuming them")
    if "independent_confirmation" in normalized_hints:
        bullets.append("seek independent confirmation where the case depends on contested public reporting")
    if "source_of_truth_check" in normalized_hints:
        bullets.append("identify the primary resolution source and any fallback source-of-truth logic")
    if "multi_condition_check" in normalized_hints:
        bullets.append("spell out the material conditions that all must hold for the contract to resolve the way you claim")
    if "settlement_mechanics_check" in normalized_hints:
        bullets.append("verify the settlement mechanics rather than assuming a simple point-in-time read")
    if "official_source_verification" in normalized_hints:
        bullets.append("check the named official source directly before relying on secondary summaries")
    if "authoritative_source_first" in normalized_hints:
        bullets.append("treat the authoritative source as primary and use secondary reporting mainly for context or fallback")
    if "disconfirming_source_required" in normalized_hints:
        bullets.append("include a concrete disconfirming source or state plainly that none credible was found")
    for custom_hint in custom_hints:
        bullets.append(f"address this additional case-specific check explicitly: {humanize_hint(custom_hint)}")

    rendered = "\n".join(f"- {bullet}" for bullet in dict.fromkeys(bullets))
    return f"""
## Completion checklist for this case
Do not finish until you have done all of the following:
{rendered}
"""


def load_bundle(payload: dict, *, inline_key: str, path_key: str) -> dict | None:
    inline = payload.get(inline_key)
    if isinstance(inline, dict):
        return inline

    bundle_path = payload.get(path_key)
    if not bundle_path:
        return None
    path = Path(bundle_path)
    if not path.is_absolute():
        path = (WORKSPACE_ROOT / bundle_path).resolve()
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def load_qmd_bundle(payload: dict) -> dict | None:
    return load_bundle(payload, inline_key="qmd_bundle", path_key="qmd_bundle_path")


def load_lmd_bundle(payload: dict) -> dict | None:
    return load_bundle(payload, inline_key="lmd_bundle", path_key="lmd_bundle_path")


def render_path_block(label: str, paths: list[str]) -> list[str]:
    lines = [f"{label}:"]
    if paths:
        lines.extend(f"- {path}" for path in paths)
    else:
        lines.append("- []")
    return lines


def render_qmd_section(payload: dict) -> str:
    bundle = load_qmd_bundle(payload)
    if not bundle or not bundle.get("qmd_used"):
        return ""

    results = bundle.get("results") or {}
    entity_paths = [item.get("path") for item in (results.get("entity_notes") or []) if item.get("path")]
    driver_paths = [item.get("path") for item in (results.get("driver_notes") or []) if item.get("path")]
    case_paths = [item.get("path") for item in (results.get("similar_cases") or []) if item.get("path")]

    sections = ["## QMD"]
    sections.extend(render_path_block("entity_paths", entity_paths))
    sections.extend(render_path_block("driver_paths", driver_paths))
    sections.extend(render_path_block("case_paths", case_paths))
    sections.append("")
    return "\n".join(sections)


def edge_metadata_lookup(causal_context: dict) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for row in (causal_context.get("matched_edge_metadata") or []):
        if not isinstance(row, dict):
            continue
        edge_key = str(row.get("edge_key") or "").strip()
        if edge_key:
            out[edge_key] = row
    return out


def node_metadata_lookup(causal_context: dict) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for row in (causal_context.get("active_node_metadata") or []):
        if not isinstance(row, dict):
            continue
        node_key = str(row.get("node_key") or "").strip()
        if node_key:
            out[node_key] = row
    return out


def edge_endpoint_nodes(edge_key: str) -> set[str]:
    parts = str(edge_key or "").split("__")
    if len(parts) >= 3:
        return {parts[0], parts[2]}
    return set()


def render_causal_node_line(node_key: str, node_metadata: dict | None = None) -> str:
    if not isinstance(node_key, str) or not node_key.strip():
        return ""
    line = str((node_metadata or {}).get("node_label") or node_key).strip() or node_key
    suffixes: list[str] = []
    lifecycle_stage = str((node_metadata or {}).get("lifecycle_stage") or "").strip().lower()
    if lifecycle_stage and lifecycle_stage != "active":
        suffixes.append(lifecycle_stage)
    if suffixes:
        line += f" ({', '.join(suffixes)})"
    return line


def render_causal_focus_line(edge_key: str, contested_edges: set[str], edge_metadata: dict | None = None) -> str:
    if not isinstance(edge_key, str) or not edge_key.strip():
        return ""
    parts = edge_key.split("__")
    if len(parts) >= 3:
        source, effect, target = parts[0], parts[1], parts[2]
        effect_map = {
            "increases": "->",
            "decreases": "-x->",
            "conditions": "=>",
        }
        arrow = effect_map.get(effect, "->")
        line = f"{source} {arrow} {target}"
    else:
        line = edge_key
    suffixes: list[str] = []
    lifecycle_stage = str((edge_metadata or {}).get("lifecycle_stage") or "").strip().lower()
    if lifecycle_stage and lifecycle_stage != "active":
        suffixes.append(lifecycle_stage)
    if edge_key in contested_edges:
        suffixes.append("contested")
    if suffixes:
        line += f" ({', '.join(suffixes)})"
    return line


def render_lmd_section(payload: dict) -> tuple[str, list[str]]:
    bundle = load_lmd_bundle(payload)
    if not bundle or not bundle.get("lmd_used"):
        return "", []

    results = bundle.get("results") or {}
    case_paths = [item.get("review_path") for item in (results.get("case_reviews") or []) if item.get("review_path")]
    intervention_paths = [item.get("path") for item in (results.get("active_interventions") or []) if item.get("path")]
    required_check_rows = results.get("required_checks") or []
    required_check_keys = [row.get("check_key") for row in required_check_rows if isinstance(row, dict) and row.get("check_key")]
    negative_check_rows = [row for row in (results.get("negative_checks") or []) if isinstance(row, dict)]
    negative_check_text = [row.get("avoid") for row in negative_check_rows if row.get("avoid")]
    causal_context = bundle.get("causal_context") or {}
    contested_edges = set(causal_context.get("contested_edges") or [])
    edge_metadata = edge_metadata_lookup(causal_context)
    node_metadata = node_metadata_lookup(causal_context)
    matched_edges = [render_causal_focus_line(edge_key, contested_edges, edge_metadata.get(edge_key)) for edge_key in (causal_context.get("matched_edges") or [])]
    matched_edges = [line for line in matched_edges if line]
    covered_node_keys: set[str] = set()
    for edge_key in (causal_context.get("matched_edges") or []):
        covered_node_keys.update(edge_endpoint_nodes(str(edge_key or "")))
    disclosed_trial_nodes = [
        render_causal_node_line(node_key, node_metadata.get(node_key))
        for node_key in (causal_context.get("active_nodes") or [])
        if str((node_metadata.get(node_key) or {}).get("lifecycle_stage") or "").strip().lower() == "trial"
        and node_key not in covered_node_keys
    ]
    disclosed_trial_nodes = [line for line in disclosed_trial_nodes if line]
    has_trial_edges = any(str((row or {}).get("lifecycle_stage") or "").strip().lower() == "trial" for row in edge_metadata.values())
    has_trial_nodes = bool(disclosed_trial_nodes)

    sections = [
        "## LMD",
        "Use this as compact reviewed mechanism-specific guidance for this case. Treat it as case-relevant prior learning, not unconditional canon.",
    ]
    if has_trial_edges or has_trial_nodes:
        sections.append("Some causal_focus items below are live-graph trial mechanisms exposed only for this treatment/trial run. Treat them as bounded experimental structure, not settled canon.")
    sections.extend(render_path_block("case_review_paths", case_paths))
    sections.extend(render_path_block("active_intervention_paths", intervention_paths))
    sections.extend(render_path_block("causal_focus", matched_edges))
    if disclosed_trial_nodes:
        sections.extend(render_path_block("experimental_trial_nodes", disclosed_trial_nodes))
    sections.extend(render_path_block("required_checks", required_check_keys))
    sections.extend(render_path_block("negative_checks", negative_check_text))
    sections.append("")
    return "\n".join(sections), required_check_keys



def render_trial_overlay_section(payload: dict) -> str:
    bundle = load_lmd_bundle(payload)
    if not bundle:
        return ""
    overlay = bundle.get("trial_overlay") or {}
    if not isinstance(overlay, dict):
        return ""
    if not bool(overlay.get("used")):
        return ""

    selected = [row for row in (overlay.get("selected_candidates") or []) if isinstance(row, dict) and row.get("injected")]
    if not selected:
        return ""

    sections = [
        "## Trial mechanism checks (experimental)",
        "These items are proposal-layer trial overlays selected for this treatment run.",
        "Treat them as bounded experimental hypotheses, not canon. Use them only if the evidence supports them, and say so explicitly if they do not help.",
    ]
    for row in selected:
        proposal_key = str(row.get("proposal_key") or row.get("proposal_id") or "unknown").strip()
        candidate_type = str(row.get("candidate_type") or "unknown").strip()
        mechanism_family = str(row.get("mechanism_family") or "unassigned").strip()
        sections.append(
            f"- {proposal_key} [{candidate_type}; family={mechanism_family}; trial_score={row.get('shadow_trial_score')}; overlay_score={row.get('overlay_score')}]"
        )
        active_nodes = row.get("matched_active_nodes") or []
        candidate_edges = (row.get("matched_candidate_edges") or []) + (row.get("matched_contested_edges") or [])
        required_checks = row.get("matched_required_checks") or []
        if active_nodes:
            sections.append(f"  - matched_active_nodes: {', '.join(str(item) for item in active_nodes)}")
        if candidate_edges:
            sections.append(f"  - matched_edges: {', '.join(str(item) for item in candidate_edges)}")
        if required_checks:
            sections.append(f"  - suggested_checks: {', '.join(str(item) for item in required_checks)}")
    sections.append("")
    return "\n".join(sections)


def build_prompt(payload: dict) -> str:
    agent_label = require(payload, "agent_label")
    if agent_label not in PERSONA_FILES:
        raise ValueError(f"unsupported agent_label: {agent_label}")

    case_id = require(payload, "case_id")
    case_key = require(payload, "case_key")
    market_id = require(payload, "market_id")
    title = require(payload, "title")

    # Ensure referenced docs exist even though the live prompt is now compact.
    if not BASE_CONTRACT_PATH.exists():
        raise FileNotFoundError(f"missing base contract: {BASE_CONTRACT_PATH}")
    if not PERSONA_FILES[agent_label].exists():
        raise FileNotFoundError(f"missing persona prompt: {PERSONA_FILES[agent_label]}")

    description = payload.get("description", "")
    current_price = payload.get("current_price")
    closes_at = payload.get("closes_at")
    resolves_at = payload.get("resolves_at")
    external_market_id = payload.get("external_market_id")
    slug = payload.get("slug")
    metadata = payload.get("metadata") or {}
    url = metadata.get("url")
    workspace_note_path = payload.get("workspace_note_path")
    reasoning_sidecar_path = payload.get("reasoning_sidecar_path") or f"qualitative-db/40-research/cases/{case_key}/researcher-analyses/UNKNOWN-DATE/UNKNOWN-DISPATCH/personas/{agent_label}.sidecar.json"
    source_note_dir = payload.get("source_note_dir") or f"qualitative-db/40-research/cases/{case_key}/researcher-source-notes"
    source_note_prefix = payload.get("source_note_prefix") or f"{agent_label}"
    assumption_note_path = payload.get("assumption_note_path") or f"qualitative-db/40-research/cases/{case_key}/researcher-analyses/UNKNOWN-DATE/UNKNOWN-DISPATCH/assumptions/{agent_label}.md"
    evidence_map_path = payload.get("evidence_map_path") or f"qualitative-db/40-research/cases/{case_key}/researcher-analyses/UNKNOWN-DATE/UNKNOWN-DISPATCH/evidence/{agent_label}.md"
    analysis_summary_path = payload.get("analysis_summary_path") or f"qualitative-db/40-research/cases/{case_key}/researcher-analyses/UNKNOWN-DATE/UNKNOWN-DISPATCH/summary.md"
    case_file_path = payload.get("case_file_path") or f"qualitative-db/40-research/cases/{case_key}/case.md"
    current_file_path = payload.get("current_file_path") or f"qualitative-db/40-research/cases/{case_key}/researcher-swarm-current.md"
    timeline_file_path = payload.get("timeline_file_path") or f"qualitative-db/40-research/cases/{case_key}/timeline.md"
    difficulty_profile = payload.get("difficulty_profile") or {}
    qmd_section = render_qmd_section(payload)
    lmd_section, lmd_required_checks = render_lmd_section(payload)
    trial_overlay_section = render_trial_overlay_section(payload)
    base_contract_rel = BASE_CONTRACT_PATH.relative_to(WORKSPACE_ROOT)
    persona_prompt_rel = PERSONA_FILES[agent_label].relative_to(WORKSPACE_ROOT)
    agent_finding_template_rel = AGENT_FINDING_TEMPLATE_PATH.relative_to(WORKSPACE_ROOT)
    source_note_template_rel = SOURCE_NOTE_TEMPLATE_PATH.relative_to(WORKSPACE_ROOT)
    assumption_note_template_rel = ASSUMPTION_NOTE_TEMPLATE_PATH.relative_to(WORKSPACE_ROOT)
    evidence_map_template_rel = EVIDENCE_MAP_TEMPLATE_PATH.relative_to(WORKSPACE_ROOT)
    persona_brief = "\n".join(f"- {line}" for line in PERSONA_BRIEFS[agent_label])
    difficulty_lines = ""
    completion_checklist = ""
    if difficulty_profile:
        raw_hints = difficulty_profile.get("focus_hints") or []
        hints, custom_hints = normalize_focus_hints(raw_hints)
        rationale = difficulty_profile.get("difficulty_rationale") or []
        if isinstance(rationale, str):
            rationale = [rationale]
        rationale = [item for item in rationale if isinstance(item, str) and item.strip()]
        if not rationale:
            rationale = default_rationale_lines(difficulty_profile, custom_hints)
        evidence_floor_map = {
            "1_authoritative": "one authoritative source may be sufficient",
            "2_meaningful": "at least two meaningful sources",
            "3_meaningful": "at least three meaningful sources unless directly settled by an authoritative source",
            "direct_settlement_required": "direct settlement / authoritative source confirmation required",
        }
        rendered_hint_lines = [f"  - {hint}" for hint in hints]
        rendered_hint_lines.extend(f"  - {custom_hint} (case-specific)" for custom_hint in custom_hints)
        rendered_hints = "\n".join(rendered_hint_lines) if rendered_hint_lines else "  - none"
        rendered_rationale = "\n".join(f"- {item}" for item in rationale) if rationale else "- none provided"
        extra_verification = "yes" if difficulty_profile.get("extra_verification_required") else "no"
        difficulty_lines = f"""
## Difficulty guidance
- difficulty_class: {difficulty_profile.get('difficulty_class', 'unknown')}
- resolution_risk: {difficulty_profile.get('resolution_risk', 'unknown')}
- evidence_floor: {evidence_floor_map.get(difficulty_profile.get('evidence_floor'), difficulty_profile.get('evidence_floor', 'unknown'))}
- extra_verification_required: {extra_verification}
- focus_hints:
{rendered_hints}

Why this case is flagged:
{rendered_rationale}
"""
        completion_checklist = build_completion_checklist(difficulty_profile, lmd_required_checks=lmd_required_checks)
    elif lmd_required_checks:
        completion_checklist = build_completion_checklist({}, lmd_required_checks=lmd_required_checks)

    prompt = f"""You are the `{agent_label}` researcher for one active market case.

## Before serious work
Read only what you need, not the whole repo:
- shared contract: `{base_contract_rel}`
- persona brief: `{persona_prompt_rel}`
- vault protocol: `qualitative-db/00-system/roles-protocols/researcher-operating-protocol.md`
- before writing the main finding, read the finding template once: `{agent_finding_template_rel}`
- if you create source notes, read once: `{source_note_template_rel}`
- if you create an assumption note, read once: `{assumption_note_template_rel}`
- if you create an evidence map, read once: `{evidence_map_template_rel}`

## Persona focus
{persona_brief}

## Case context
- case_id: {case_id}
- case_key: {case_key}
- market_id: {market_id}
- external_market_id: {external_market_id}
- slug: {slug}
- title: {title}
- current_price: {current_price}
- closes_at: {closes_at}
- resolves_at: {resolves_at}
- primary_market_url: {url}
{difficulty_lines}
{completion_checklist}
{qmd_section}
{lmd_section}
{trial_overlay_section}
## Required output
- write the main agent finding exactly to: `{workspace_note_path}`
- also write a compact reasoning sidecar JSON exactly to: `{reasoning_sidecar_path}`
- structure the finding using the agent-finding template headings, including the source-quality assessment, verification impact, reusable lesson signals, and Orchestrator review suggestions sections
- keep the sidecar faithful to the finding; do not introduce claims in the sidecar that are not supported by the finding
- for frontmatter linkage fields (`entity`, `driver`, `related_entities`, `related_drivers`), use canonical slugs only when you know them from `qualitative-db/20-entities/` or `qualitative-db/30-drivers/`
- if you are unsure a linkage is canonical, keep it out of the canonical linkage fields and put it in `proposed_entities` or `proposed_drivers` instead
- do not invent new canonical entity or driver slugs in the artifact frontmatter
- add extra labeled sections when the checklist for this case requires them
- create at least one substantive source note when external sources materially inform the finding; keep source notes only under: `{source_note_dir}` with filenames starting: `{source_note_prefix}-`
- when the analysis relies on a nontrivial assumption or tradeoff, write an assumption note to exactly: `{assumption_note_path}`
- structure any assumption note using the assumption-note template headings from `{assumption_note_template_rel}`
- use the same canonical-vs-proposed linkage rule in assumption-note frontmatter when you fill entity/driver linkage fields there
- when evidence needs explicit netting, conflict framing, or auditability beyond the main note, write an evidence map to exactly: `{evidence_map_path}`
- use the same canonical-vs-proposed linkage rule in evidence-map frontmatter when you fill entity/driver linkage fields there
- treat these as system-managed case surfaces and do not write them yourself unless explicitly told: `{analysis_summary_path}`, `{case_file_path}`, `{current_file_path}`, `{timeline_file_path}`
- do not invent alternate folders for this case

## Required reasoning sidecar JSON
Write valid JSON only to `{reasoning_sidecar_path}` using this shape:
```json
{{
  "artifact_type": "persona_reasoning_sidecar",
  "schema_version": "v1",
  "persona": "{agent_label}",
  "main_thesis": "short string",
  "own_probability": 0.50,
  "reasoning_mode": ["other"],
  "key_assumptions": ["short bullet"],
  "strongest_supports": ["short bullet"],
  "strongest_disconfirmers": ["short bullet"],
  "main_logical_chain": ["step 1", "step 2"],
  "fragility_points": ["short bullet"],
  "unresolved_ambiguities": ["short bullet"],
  "timing_relevance": "short string",
  "source_quality_view": "short string",
  "what_would_change_view": "short string",
  "recommended_weight": "low|medium|high",
  "confidence_in_extract": "low|medium|high",
  "quote_anchors": ["optional short quote or anchor"],
  "runtime_metadata": {{
    "generation_mode": "researcher_sidecar_v1",
    "case_key": "{case_key}",
    "dispatch_id": "from your assignment context",
    "research_run_id": "from your assignment context",
    "source_persona_finding_path": "{workspace_note_path}",
    "source_persona_sha256": "sha256 hex of the exact final markdown finding you wrote",
    "prompt_contract_version": "researcher-sidecar-v1"
  }}
}}
```
Sidecar rules:
- keep it compact, structured, and faithful to the final finding
- `own_probability` should match your final stated probability estimate when one exists
- use only these reasoning_mode values: `base_rate`, `market_anchor`, `scenario_analysis`, `catalyst_analysis`, `risk_management`, `contract_interpretation`, `variant_hypothesis`, `technical_reference`, `other`
- after you finish writing the markdown finding, compute the sha256 of that exact markdown file and place it into `runtime_metadata.source_persona_sha256`
- do not leave placeholder strings like "from your assignment context" in the final sidecar

## Operating rules
- treat this run as self-contained except for the current assignment, the vault, and the database
- do not read unrelated old case artifacts unless they are directly relevant stable context
- use internet research independently, prioritizing recent, credible, and meaningfully independent sources
- preserve enough provenance in `qualitative-db/40-research/` to make the finding auditable
- compare explicitly against the market-implied probability from `current_price`
- state whether you agree, roughly agree, or disagree with the market and why
- identify the strongest disconfirming fact or source unless none exists; if none exists, say so explicitly
- distinguish direct evidence from indirect/contextual evidence when that difference matters
- preserve uncertainty rather than continuing to search indefinitely
- do not rewrite canon during routine case work

## Evidence sufficiency before stopping
- simple scoreboard / official-stat / official-chart markets: one authoritative source may be sufficient
- ordinary interpretive markets: aim for at least two meaningful sources, ideally independent or one primary plus one strong contextual source
- high-complexity, geopolitics, or rule-sensitive markets: aim for at least three meaningful sources unless one authoritative source directly settles the question
- narrow-resolution, date-specific, or exclusion-heavy markets: explicitly verify what counts and what does not count before finalizing
- if market-implied probability is >85% or <15%, perform at least one additional verification pass unless an authoritative source already directly settles the answer
- if your estimate differs from market by more than 10 percentage points, perform at least one additional verification pass before stopping

## Adaptive stop rule
Do not stop merely because you can write a coherent memo. Stop gathering new evidence and start writing only when both conditions are true:
1. you can state a directional probability view with main reasons, caveats, and strongest disconfirming consideration
2. the case has met an evidence threshold appropriate to its difficulty, and the next likely source is unlikely to move your estimate by roughly 5 percentage points or change the main mechanism materially

If uncertainty remains after that threshold, record it in the finding instead of continuing to explore.

## Supporting artifacts
The main finding is mandatory. Beyond that, prefer preserving provenance-rich supporting artifacts rather than too few when they materially improve traceability, clarify a key assumption, preserve an important disagreement, or make the evidence floor legible to later reviewers.

## Market description
{description}
"""
    return prompt


def main() -> int:
    args = parse_args()
    try:
        payload = load_json(args.file)
        if args.agent_label:
            payload["agent_label"] = args.agent_label
        prompt = build_prompt(payload)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps({"prompt": prompt}, indent=2))
    else:
        print(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
