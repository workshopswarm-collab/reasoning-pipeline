#!/usr/bin/env python3
from __future__ import annotations

"""Review provisional driver buckets for possible family synthesis with local Ollama.

Lane B: selective, best-effort, post-aggregation.
- Reads the generated driver index and candidate notes
- Focuses only on provisional unresolved family buckets
- Uses deterministic trigger rules to identify synthesis-worthy buckets
- Optionally calls local Ollama for structured advisory review
- Writes JSON + markdown outputs plus a top-level synthesis index

This lane is intentionally non-blocking and should be invoked best-effort.
"""

import argparse
import hashlib
import json
import re
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from validate_research_artifact_linkages import (  # type: ignore
    WORKSPACE_ROOT,
    listify,
    parse_frontmatter,
)

QUEUE_DIR = WORKSPACE_ROOT / "qualitative-db" / "40-research" / "review-queue" / "drivers-candidates"
INDEX_PATH = QUEUE_DIR / "generated-index.md"
CANDIDATE_NOTES_DIR = QUEUE_DIR / "candidate-notes"
DRIVER_ROOT = WORKSPACE_ROOT / "qualitative-db" / "30-drivers"
SYNTHESIS_DIR = QUEUE_DIR / "provisional-family-synthesis"
ARCHIVE_DIR = SYNTHESIS_DIR / "archive"
INPUTS_DIR = SYNTHESIS_DIR / "inputs"
REVIEW_NOTES_DIR = SYNTHESIS_DIR / "review-notes"
SYNTHESIS_INDEX_PATH = SYNTHESIS_DIR / "LLM-proposed-provisional-synthesis-index.md"
NOW_UTC = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
DEFAULT_OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
DEFAULT_OLLAMA_MODEL = "qwen3.5:9b"
PROMPT_VERSION = "v1"
STRONG_NEIGHBOR_SCORE = 1.5
MODERATE_NEIGHBOR_SCORE = 1.0
GENERIC_TOKENS = {
    "risk", "timing", "market", "driver", "official", "specific", "company", "surface",
    "demand", "release", "publication", "resolution", "mechanics", "mapping", "cadence",
}
ALLOWED_ACTIONS = {
    "keep_provisional",
    "merge_provisional_buckets",
    "fold_into_existing_family",
    "mark_as_canon_adjacent",
    "insufficient_evidence",
}
ALLOWED_CONFIDENCE = {"low", "medium", "high"}

FAMILY_LINE_RE = re.compile(
    r"^- `(?P<label>.+?)` \(`(?P<slug>.+?)`\) "
    r"\(occurrences: (?P<occurrences>\d+), cases: (?P<cases>\d+), personas: (?P<personas>\d+), raw_candidates: (?P<raw>\d+), canon: (?P<canon_status>[a-z_]+)(?: -> (?P<canon_driver>[a-z0-9\-]+))?\)$"
)


@dataclass
class CandidateNote:
    rel_path: str
    candidate_slug: str
    candidate_label: str
    normalized_family: str
    normalized_family_label: str
    canonical_coverage_status: str
    canonical_coverage_driver: str | None
    total_occurrences: int
    distinct_cases: int
    distinct_personas: int
    personas: list[str]
    case_keys: list[str]
    label_variants: list[str]
    related_entities: list[str]
    related_canonical_drivers: list[str]
    canonical_driver_suggestions: list[str]


@dataclass
class FamilyIndexEntry:
    family_slug: str
    family_label: str
    total_occurrences: int
    distinct_cases: int
    distinct_personas: int
    raw_candidate_count: int
    canon_coverage_status: str
    canon_coverage_driver: str | None
    section: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Review provisional driver synthesis opportunities with local Ollama")
    parser.add_argument("--family-slug", action="append", help="Limit synthesis review to one or more provisional family slugs")
    parser.add_argument("--all-families", action="store_true", help="Allow all provisional families to be considered")
    parser.add_argument("--run-ollama", action="store_true", help="Also call local Ollama and write review outputs")
    parser.add_argument("--auto", action="store_true", help="Only review provisional packets whose input changed since the last synthesis review")
    parser.add_argument("--model", default=DEFAULT_OLLAMA_MODEL, help="Ollama model to use when --run-ollama is set")
    parser.add_argument("--ollama-url", default=DEFAULT_OLLAMA_URL, help="Ollama generate API URL")
    parser.add_argument("--timeout-seconds", type=int, default=180, help="HTTP timeout for each Ollama review call")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def parse_index() -> dict[str, FamilyIndexEntry]:
    text = INDEX_PATH.read_text()
    current_section = ""
    entries: dict[str, FamilyIndexEntry] = {}
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line == "## Ranked normalized mechanism families":
            current_section = "surfaced"
            continue
        if line == "## Provisional unresolved family buckets":
            current_section = "provisional"
            continue
        if line.startswith("## "):
            current_section = ""
            continue
        if not current_section or not line.startswith("- "):
            continue
        m = FAMILY_LINE_RE.match(line)
        if not m:
            continue
        entry = FamilyIndexEntry(
            family_slug=m.group("slug"),
            family_label=m.group("label"),
            total_occurrences=int(m.group("occurrences")),
            distinct_cases=int(m.group("cases")),
            distinct_personas=int(m.group("personas")),
            raw_candidate_count=int(m.group("raw")),
            canon_coverage_status=m.group("canon_status"),
            canon_coverage_driver=m.group("canon_driver") or None,
            section=current_section,
        )
        entries[entry.family_slug] = entry
    return entries


def parse_simple_bullets(body: str, section_heading: str) -> list[str]:
    out: list[str] = []
    in_section = False
    for raw_line in body.splitlines():
        line = raw_line.rstrip()
        if line == section_heading:
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if not in_section or not line.startswith("- `"):
            continue
        m = re.match(r"^- `(.+?)`$", line)
        if m:
            out.append(m.group(1))
    return out


def parse_counted_bullets(body: str, section_heading: str) -> list[str]:
    out: list[str] = []
    in_section = False
    for raw_line in body.splitlines():
        line = raw_line.rstrip()
        if line == section_heading:
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if not in_section or not line.startswith("- `"):
            continue
        m = re.match(r"^- `(.+?)` \((\d+)\)$", line)
        if m:
            out.append(m.group(1))
            continue
        m = re.match(r"^- `(.+?)`$", line)
        if m:
            out.append(m.group(1))
    return out


def load_candidate_notes() -> list[CandidateNote]:
    notes: list[CandidateNote] = []
    for path in sorted(CANDIDATE_NOTES_DIR.glob("generated-driver-candidate-*.md")):
        text = path.read_text()
        frontmatter, body_start = parse_frontmatter(text)
        if frontmatter is None or body_start is None:
            continue
        body = text[body_start:]
        rel_path = str(path.relative_to(WORKSPACE_ROOT)) if path.is_relative_to(WORKSPACE_ROOT) else str(path)
        notes.append(
            CandidateNote(
                rel_path=rel_path,
                candidate_slug=str(frontmatter.get("candidate_slug") or path.stem.replace("generated-driver-candidate-", "")),
                candidate_label=str(frontmatter.get("candidate_label") or "").strip().strip('"'),
                normalized_family=str(frontmatter.get("normalized_driver_family") or "").strip(),
                normalized_family_label=str(frontmatter.get("normalized_driver_family_label") or "").strip().strip('"'),
                canonical_coverage_status=str(frontmatter.get("canonical_coverage_status") or "novel").strip() or "novel",
                canonical_coverage_driver=(str(frontmatter.get("canonical_coverage_driver") or "").strip() or None),
                total_occurrences=int(frontmatter.get("total_occurrences") or 0),
                distinct_cases=int(frontmatter.get("distinct_cases") or 0),
                distinct_personas=int(frontmatter.get("distinct_personas") or 0),
                personas=parse_simple_bullets(body, "## Personas observed"),
                case_keys=parse_simple_bullets(body, "## Cases observed"),
                label_variants=listify(frontmatter.get("label_variants")),
                related_entities=parse_counted_bullets(body, "## Common co-mentioned entities"),
                related_canonical_drivers=parse_counted_bullets(body, "## Common co-mentioned canonical drivers"),
                canonical_driver_suggestions=parse_counted_bullets(body, "## Nearest existing canonical driver suggestions"),
            )
        )
    return notes


def load_driver_catalog() -> dict[str, dict[str, Any]]:
    catalog: dict[str, dict[str, Any]] = {}
    for path in sorted(DRIVER_ROOT.rglob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text()
        fm, body_start = parse_frontmatter(text)
        fm = fm or {}
        slug = str(fm.get("driver") or path.stem).strip()
        aliases = [str(a).strip() for a in listify(fm.get("aliases")) if str(a).strip()]
        body = text[body_start:] if fm is not None and body_start is not None else text
        summary = ""
        lines = body.splitlines()
        in_summary = False
        buff: list[str] = []
        for line in lines:
            stripped = line.strip()
            if stripped == "# Overview summary":
                in_summary = True
                continue
            if in_summary and stripped.startswith("## "):
                break
            if in_summary and stripped:
                buff.append(stripped)
        if buff:
            summary = " ".join(buff)
        catalog[slug] = {"aliases": aliases, "summary": summary}
    return catalog


def build_family_groups(index_entries: dict[str, FamilyIndexEntry], notes: list[CandidateNote]) -> dict[str, dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for note in notes:
        fam = note.normalized_family
        if not fam:
            continue
        entry = grouped.setdefault(
            fam,
            {
                "index_entry": index_entries.get(fam),
                "candidates": [],
            },
        )
        entry["candidates"].append(note)
    return grouped


def family_tokens(slug: str, labels: list[str]) -> set[str]:
    toks = set(filter(None, slug.split("-")))
    for label in labels:
        toks.update(filter(None, re.split(r"[^a-z0-9]+", label.lower())))
    return toks


def compute_neighbors(family_slug: str, groups: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    focal = groups[family_slug]
    focal_labels = [c.candidate_label for c in focal["candidates"]]
    focal_tokens = family_tokens(family_slug, focal_labels)
    focal_related = {d for c in focal["candidates"] for d in c.related_canonical_drivers}
    out: list[dict[str, Any]] = []
    for other_slug, other in groups.items():
        if other_slug == family_slug:
            continue
        other_labels = [c.candidate_label for c in other["candidates"]]
        other_tokens = family_tokens(other_slug, other_labels)
        other_related = {d for c in other["candidates"] for d in c.related_canonical_drivers}
        family_overlap = len((focal_tokens - GENERIC_TOKENS) & (other_tokens - GENERIC_TOKENS))
        related_overlap = len(focal_related & other_related)
        score = family_overlap * 1.0 + related_overlap * 0.75
        if score <= 0:
            continue
        reason_parts = []
        if family_overlap:
            reason_parts.append("mechanism-token")
        if related_overlap:
            reason_parts.append("co-mentioned-driver")
        out.append(
            {
                "family_slug": other_slug,
                "family_label": (other.get("index_entry").family_label if other.get("index_entry") else other_slug.replace("-", " ")),
                "section": (other.get("index_entry").section if other.get("index_entry") else "unknown"),
                "reason": "+".join(reason_parts),
                "overlap_score": round(score, 2),
            }
        )
    return sorted(out, key=lambda item: (-item["overlap_score"], item["family_slug"]))


def synthesis_trigger_reasons(family_slug: str, groups: dict[str, dict[str, Any]]) -> list[str]:
    entry = groups[family_slug].get("index_entry")
    if not entry or entry.section != "provisional":
        return []
    neighbors = compute_neighbors(family_slug, groups)
    strong = [n for n in neighbors if n["overlap_score"] >= STRONG_NEIGHBOR_SCORE]
    moderate = [n for n in neighbors if n["overlap_score"] >= MODERATE_NEIGHBOR_SCORE]
    reasons: list[str] = []
    if strong:
        reasons.append("strong_neighbor_overlap")
    elif len(moderate) >= 2:
        reasons.append("multiple_moderate_neighbors")
    if any("co-mentioned-driver" in n["reason"] for n in neighbors[:3]):
        reasons.append("shared_canonical_driver_signal")
    combined_occurrences = entry.total_occurrences + sum(groups[n["family_slug"]]["index_entry"].total_occurrences for n in strong[:2] if groups[n["family_slug"]].get("index_entry"))
    if combined_occurrences >= 3:
        reasons.append("combined_evidence_threshold")
    if entry.canon_coverage_status == "covered":
        return []
    if not reasons:
        return []
    if "strong_neighbor_overlap" in reasons or ("multiple_moderate_neighbors" in reasons and len(reasons) >= 2):
        return reasons
    return []


def build_canonical_driver_context(family_slug: str, groups: dict[str, dict[str, Any]], driver_catalog: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    focal = groups[family_slug]
    seen: dict[str, set[str]] = defaultdict(set)
    for c in focal["candidates"]:
        for slug in c.canonical_driver_suggestions:
            if slug in driver_catalog:
                seen[slug].add("suggestion")
        for slug in c.related_canonical_drivers:
            if slug in driver_catalog:
                seen[slug].add("related_driver")
        if c.canonical_coverage_driver and c.canonical_coverage_driver in driver_catalog:
            seen[c.canonical_coverage_driver].add("candidate_coverage")
    out = []
    for slug, why in sorted(seen.items(), key=lambda item: (-len(item[1]), item[0]))[:6]:
        out.append({
            "driver_slug": slug,
            "why_included": "+".join(sorted(why)),
            "summary": driver_catalog[slug]["summary"],
            "aliases": driver_catalog[slug]["aliases"],
        })
    return out


def build_packet(family_slug: str, groups: dict[str, dict[str, Any]], driver_catalog: dict[str, dict[str, Any]]) -> dict[str, Any]:
    entry = groups[family_slug]["index_entry"]
    candidates = groups[family_slug]["candidates"]
    neighbors = compute_neighbors(family_slug, groups)[:5]
    trigger_reasons = synthesis_trigger_reasons(family_slug, groups)
    return {
        "family_slug": family_slug,
        "family_label": entry.family_label,
        "generated_at": NOW_UTC,
        "heuristic_summary": {
            "section": entry.section,
            "canon_coverage_status": entry.canon_coverage_status,
            "canon_coverage_driver": entry.canon_coverage_driver,
            "total_occurrences": entry.total_occurrences,
            "distinct_cases": entry.distinct_cases,
            "distinct_personas": entry.distinct_personas,
            "raw_candidate_count": entry.raw_candidate_count,
        },
        "trigger_reasons": trigger_reasons,
        "focal_bucket": {
            "family_slug": family_slug,
            "family_label": entry.family_label,
            "raw_candidates": [
                {
                    "candidate_slug": c.candidate_slug,
                    "candidate_label": c.candidate_label,
                    "occurrences": c.total_occurrences,
                    "distinct_cases": c.distinct_cases,
                    "distinct_personas": c.distinct_personas,
                    "personas": c.personas,
                    "case_keys": c.case_keys,
                    "related_entities": c.related_entities,
                    "related_canonical_drivers": c.related_canonical_drivers,
                    "canonical_driver_suggestions": c.canonical_driver_suggestions,
                    "source_candidate_note": c.rel_path,
                }
                for c in candidates
            ],
        },
        "neighbor_buckets": [
            {
                **neighbor,
                "raw_candidates": [
                    {
                        "candidate_slug": c.candidate_slug,
                        "candidate_label": c.candidate_label,
                        "occurrences": c.total_occurrences,
                        "related_canonical_drivers": c.related_canonical_drivers,
                        "canonical_driver_suggestions": c.canonical_driver_suggestions,
                        "source_candidate_note": c.rel_path,
                    }
                    for c in groups[neighbor["family_slug"]]["candidates"]
                ],
            }
            for neighbor in neighbors[:3]
        ],
        "canonical_driver_context": build_canonical_driver_context(family_slug, groups, driver_catalog),
        "review_task": {
            "allowed_actions": [
                "keep_provisional",
                "merge_provisional_buckets",
                "fold_into_existing_family",
                "mark_as_canon_adjacent",
                "insufficient_evidence",
            ],
            "instruction": "Review whether this provisional bucket should remain provisional, merge with another bucket, fold into an existing surfaced family, or stay unresolved due to insufficient evidence.",
        },
    }


def is_synthesis_worthy(family_slug: str, groups: dict[str, dict[str, Any]], args: argparse.Namespace) -> bool:
    requested = set(args.family_slug or [])
    if requested:
        return family_slug in requested
    if args.all_families:
        return True
    return bool(synthesis_trigger_reasons(family_slug, groups))


def packet_hash(payload: dict[str, Any]) -> str:
    stable = json.loads(json.dumps(payload))
    stable.pop("generated_at", None)
    canonical = json.dumps(stable, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def previous_hash(family_slug: str) -> str | None:
    path = SYNTHESIS_DIR / f"generated-provisional-synthesis-{family_slug}.json"
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return None
    return str(payload.get("source_input_hash") or "").strip() or None


def sync_input_packets(packets: dict[str, dict[str, Any]]) -> dict[str, int]:
    SYNTHESIS_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    INPUTS_DIR.mkdir(parents=True, exist_ok=True)
    outcomes: dict[str, int] = defaultdict(int)
    expected: set[str] = set()
    for slug, payload in packets.items():
        name = f"generated-provisional-synthesis-input-{slug}.json"
        expected.add(name)
        path = INPUTS_DIR / name
        content = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        if path.exists() and path.read_text() == content:
            outcomes["input_unchanged"] += 1
        else:
            path.write_text(content)
            outcomes["input_written"] += 1
    for path in INPUTS_DIR.glob("generated-provisional-synthesis-input-*.json"):
        if path.name not in expected:
            path.unlink()
            outcomes["input_removed"] += 1
    return dict(outcomes)


def build_system_prompt() -> str:
    return (
        "You are reviewing provisional proposed-driver buckets for possible family synthesis in a quantitative research memory system.\n\n"
        "Your job is to decide whether a provisional bucket should remain provisional, merge with another provisional bucket, fold into an existing surfaced family, or stay unresolved due to insufficient evidence.\n\n"
        "Important rules:\n"
        "1. Do not invent facts, families, cases, or canonical drivers not present in the input.\n"
        "2. Prefer conservative judgments. Sparse evidence should usually produce insufficient_evidence or keep_provisional, not aggressive merging.\n"
        "3. Only recommend merge_provisional_buckets when the focal bucket and named provisional neighbor clearly appear to represent the same broader mechanism.\n"
        "4. Only recommend fold_into_existing_family when a surfaced neighboring family already appears to capture the mechanism.\n"
        "5. Output valid JSON only.\n"
        "Return exactly these fields: family_slug, recommended_action, target_family_slug, target_family_label, target_canonical_driver, confidence, rationale, suggested_follow_up."
    )


def build_user_prompt(payload: dict[str, Any]) -> str:
    return "Review this provisional synthesis packet. Return JSON only.\n\nInput:\n" + json.dumps(payload, ensure_ascii=False, indent=2)


def call_ollama(model: str, url: str, payload: dict[str, Any], timeout_seconds: int) -> tuple[str, dict[str, Any], dict[str, Any]]:
    req_payload = {
        "model": model,
        "system": build_system_prompt(),
        "prompt": build_user_prompt(payload),
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.2},
    }
    req = urllib.request.Request(url, data=json.dumps(req_payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout_seconds) as response:  # noqa: S310
        raw = response.read().decode("utf-8")
    decoded = json.loads(raw)
    text = str(decoded.get("response") or "").strip() or str(decoded.get("thinking") or "").strip()
    if not text:
        raise ValueError(f"Ollama returned no JSON text: {raw[:500]}")
    return text, json.loads(text), decoded


def normalize_action(value: Any) -> str:
    text = str(value or "").strip().lower().replace("-", "_").replace(" ", "_")
    aliases = {
        "hold": "keep_provisional",
        "keep": "keep_provisional",
        "merge": "merge_provisional_buckets",
        "fold": "fold_into_existing_family",
        "canon_adjacent": "mark_as_canon_adjacent",
        "insufficient": "insufficient_evidence",
    }
    text = aliases.get(text, text)
    return text if text in ALLOWED_ACTIONS else "insufficient_evidence"


def normalize_review(parsed: dict[str, Any], payload: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    notes: list[str] = []
    action = normalize_action(parsed.get("recommended_action"))
    if action != str(parsed.get("recommended_action") or ""):
        notes.append("recommended_action_normalized")
    confidence = str(parsed.get("confidence") or "").strip().lower()
    if confidence not in ALLOWED_CONFIDENCE:
        confidence = "low"
        notes.append("confidence_defaulted")
    normalized = {
        "family_slug": str(payload.get("family_slug") or ""),
        "recommended_action": action,
        "target_family_slug": str(parsed.get("target_family_slug") or "").strip() or None,
        "target_family_label": str(parsed.get("target_family_label") or "").strip() or None,
        "target_canonical_driver": str(parsed.get("target_canonical_driver") or "").strip() or None,
        "confidence": confidence,
        "rationale": str(parsed.get("rationale") or "").strip(),
        "suggested_follow_up": str(parsed.get("suggested_follow_up") or "").strip(),
    }
    return normalized, notes


def render_markdown(payload: dict[str, Any]) -> str:
    norm = payload.get("normalized_review") or {}
    notes = payload.get("normalization_notes") or []
    src = str(payload.get("source_input_path") or "")
    lines = [
        "---",
        "type: proposed_driver_provisional_synthesis_review",
        f"family_slug: {payload.get('family_slug')}",
        f"review_model: {payload.get('review_model')}",
        f"generated_at: {payload.get('generated_at')}",
        f"prompt_version: {payload.get('prompt_version')}",
        f"recommended_action: {norm.get('recommended_action') or ''}",
        f"target_family_slug: {norm.get('target_family_slug') or ''}",
        f"target_family_label: {json.dumps(norm.get('target_family_label') or '', ensure_ascii=False)}",
        f"target_canonical_driver: {norm.get('target_canonical_driver') or ''}",
        f"review_confidence: {norm.get('confidence') or ''}",
        "status: active",
        "---",
        "",
        f"# Provisional synthesis review: {payload.get('family_slug')}",
        "",
        "## Recommendation",
        f"- action: `{norm.get('recommended_action') or ''}`",
        f"- target family slug: `{norm.get('target_family_slug') or ''}`",
        f"- target family label: `{norm.get('target_family_label') or ''}`",
        f"- target canonical driver: `{norm.get('target_canonical_driver') or ''}`",
        f"- confidence: `{norm.get('confidence') or ''}`",
        "",
        "## Rationale",
        norm.get('rationale') or '',
        "",
        "## Suggested follow-up",
        norm.get('suggested_follow_up') or '',
        "",
        "## Normalization notes",
    ]
    lines.extend([f"- `{n}`" for n in notes] or ["- none"])
    lines.extend([
        "",
        "## Source input",
        f"- `{src}`",
        "",
    ])
    return "\n".join(lines)


def render_index(outputs: dict[str, dict[str, Any]], review_model: str) -> str:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for payload in outputs.values():
        grouped[(payload.get("normalized_review") or {}).get("recommended_action") or "insufficient_evidence"].append(payload)
    order = ["merge_provisional_buckets", "fold_into_existing_family", "mark_as_canon_adjacent", "keep_provisional", "insufficient_evidence"]
    lines = [
        "---",
        "type: proposed_driver_provisional_synthesis_index",
        "generated_by: ollama_provisional_synthesis_pass",
        f"generated_at: {NOW_UTC}",
        f"review_model: {review_model}",
        f"family_review_count: {len(outputs)}",
        "status: active",
        "---",
        "",
        "# LLM proposed provisional synthesis index",
        "",
    ]
    for action in order:
        lines.append(f"## {action}")
        items = sorted(grouped.get(action, []), key=lambda p: p.get("family_slug") or "")
        if not items:
            lines.append("- none")
            lines.append("")
            continue
        for payload in items:
            norm = payload.get("normalized_review") or {}
            note_name = f"review-notes/generated-provisional-synthesis-{payload.get('family_slug')}.md"
            lines.append(f"- `{payload.get('family_slug')}` -> `{note_name}` (confidence: `{norm.get('confidence') or ''}`)")
        lines.append("")
    return "\n".join(lines)


def load_existing_outputs() -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    if not SYNTHESIS_DIR.exists():
        return out
    for path in SYNTHESIS_DIR.glob("generated-provisional-synthesis-*.json"):
        try:
            payload = json.loads(path.read_text())
        except Exception:
            continue
        slug = str(payload.get("family_slug") or "").strip()
        if slug:
            out[slug] = payload
    return out


def sync_review_outputs(outputs: dict[str, dict[str, Any]], review_model: str, active_family_slugs: set[str] | None = None) -> dict[str, int]:
    SYNTHESIS_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    REVIEW_NOTES_DIR.mkdir(parents=True, exist_ok=True)
    outcomes: dict[str, int] = defaultdict(int)
    for slug, payload in outputs.items():
        json_path = SYNTHESIS_DIR / f"generated-provisional-synthesis-{slug}.json"
        md_path = REVIEW_NOTES_DIR / f"generated-provisional-synthesis-{slug}.md"
        json_content = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        if json_path.exists() and json_path.read_text() == json_content:
            outcomes["review_json_unchanged"] += 1
        else:
            json_path.write_text(json_content)
            outcomes["review_json_written"] += 1
        md_content = render_markdown(payload)
        if md_path.exists() and md_path.read_text() == md_content:
            outcomes["review_md_unchanged"] += 1
        else:
            md_path.write_text(md_content)
            outcomes["review_md_written"] += 1
    existing = load_existing_outputs()
    if active_family_slugs is not None:
        existing = {slug: payload for slug, payload in existing.items() if slug in active_family_slugs}
    index_content = render_index(existing, review_model)
    if SYNTHESIS_INDEX_PATH.exists() and SYNTHESIS_INDEX_PATH.read_text() == index_content:
        outcomes["review_index_unchanged"] += 1
    else:
        SYNTHESIS_INDEX_PATH.write_text(index_content)
        outcomes["review_index_written"] += 1
    return dict(outcomes)


def main() -> int:
    args = parse_args()
    index_entries = parse_index()
    notes = load_candidate_notes()
    driver_catalog = load_driver_catalog()
    groups = build_family_groups(index_entries, notes)
    packets = {slug: build_packet(slug, groups, driver_catalog) for slug in sorted(groups) if is_synthesis_worthy(slug, groups, args)}
    input_outcomes = sync_input_packets(packets)

    review_outputs: dict[str, dict[str, Any]] = {}
    review_errors: dict[str, str] = {}
    skipped_review_families: list[str] = []
    review_outcomes: dict[str, int] = {}
    if args.run_ollama:
        for slug, packet in packets.items():
            current_hash = packet_hash(packet)
            previous = previous_hash(slug)
            if args.auto and previous and previous == current_hash:
                skipped_review_families.append(slug)
                continue
            try:
                raw_text, parsed, raw_api = call_ollama(args.model, args.ollama_url, packet, args.timeout_seconds)
                normalized, norm_notes = normalize_review(parsed, packet)
                review_outputs[slug] = {
                    "type": "proposed_driver_provisional_synthesis_review",
                    "family_slug": slug,
                    "review_model": args.model,
                    "generated_at": NOW_UTC,
                    "prompt_version": PROMPT_VERSION,
                    "source_input_path": str((INPUTS_DIR / f"generated-provisional-synthesis-input-{slug}.json").relative_to(WORKSPACE_ROOT)),
                    "source_input_hash": current_hash,
                    "raw_model_output": raw_text,
                    "raw_api_response": raw_api,
                    "parsed_review": parsed,
                    "normalized_review": normalized,
                    "normalization_notes": norm_notes,
                }
            except Exception as exc:  # noqa: BLE001
                review_errors[slug] = str(exc)
        review_outcomes = sync_review_outputs(review_outputs, args.model, set(packets.keys()))

    result = {
        "status": "ok",
        "family_count": len(groups),
        "selected_family_count": len(packets),
        "selected_families": sorted(packets.keys()),
        "write_outcomes": input_outcomes,
        "inputs_dir": str(INPUTS_DIR.relative_to(WORKSPACE_ROOT)),
        "run_ollama": bool(args.run_ollama),
        "auto_mode": bool(args.auto),
        "review_model": args.model if args.run_ollama else None,
        "review_write_outcomes": review_outcomes,
        "review_output_count": len(review_outputs),
        "skipped_review_families": skipped_review_families,
        "review_errors": review_errors,
    }
    print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
