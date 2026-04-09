#!/usr/bin/env python3
from __future__ import annotations

"""Prepare and optionally review normalized proposed-driver families with local Ollama.

V1 behavior:
- read the generated proposed-driver family index
- read generated raw candidate notes from candidate-notes/
- select review-worthy families using simple deterministic thresholds
- write per-family JSON input packets into surfaced-family-review/inputs/
- optionally call local Ollama for structured family review
- write raw JSON review outputs into surfaced-family-review/
"""

import argparse
import hashlib
import json
import re
import urllib.error
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
FAMILY_REVIEW_DIR = QUEUE_DIR / "surfaced-family-review"
INPUTS_DIR = FAMILY_REVIEW_DIR / "inputs"
REVIEW_NOTES_DIR = FAMILY_REVIEW_DIR / "review-notes"
FAMILY_REVIEW_INDEX_PATH = FAMILY_REVIEW_DIR / "LLM-proposed-family-index.md"
NOW_UTC = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
DEFAULT_OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
DEFAULT_OLLAMA_MODEL = "qwen3.5:9b"
PROMPT_VERSION = "v1"
ALLOWED_ACTIONS = {
    "hold",
    "rename_family",
    "split_family",
    "merge_with_other_family",
    "merge_into_canon",
    "promote_new_family",
}
ALLOWED_CANON_OVERLAP = {"none", "partial", "strong"}
ALLOWED_CONFIDENCE = {"low", "medium", "high"}

FAMILY_LINE_RE = re.compile(
    r"^- `(?P<label>.+?)` \(`(?P<slug>.+?)`\) "
    r"\(occurrences: (?P<occurrences>\d+), cases: (?P<cases>\d+), personas: (?P<personas>\d+), raw_candidates: (?P<raw>\d+), canon: (?P<canon_status>[a-z_]+)(?: -> (?P<canon_driver>[a-z0-9\-]+))?\)$"
)


@dataclass
class CandidateNote:
    path: Path
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
    example_occurrences: list[dict[str, str]]


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


@dataclass
class FamilyPacket:
    family_slug: str
    family_label: str
    index_entry: FamilyIndexEntry | None
    candidates: list[CandidateNote]


@dataclass
class CanonicalDriverContext:
    driver_slug: str
    why_included: str
    summary: str
    aliases: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare Ollama review packets for proposed-driver families")
    parser.add_argument("--family-slug", action="append", help="Limit packet generation to one or more specific family slugs")
    parser.add_argument("--all-families", action="store_true", help="Generate packets for all discovered families")
    parser.add_argument("--min-raw-candidates", type=int, default=2, help="Minimum raw candidate count to mark a family review-worthy")
    parser.add_argument("--min-occurrences", type=int, default=3, help="Minimum occurrence count to mark a family review-worthy")
    parser.add_argument("--run-ollama", action="store_true", help="Also call local Ollama and write review outputs")
    parser.add_argument("--auto", action="store_true", help="When combined with --run-ollama, only review families whose input packet changed since the last review")
    parser.add_argument("--model", default=DEFAULT_OLLAMA_MODEL, help="Ollama model to use when --run-ollama is set")
    parser.add_argument("--ollama-url", default=DEFAULT_OLLAMA_URL, help="Ollama generate API URL")
    parser.add_argument("--timeout-seconds", type=int, default=120, help="HTTP timeout for each Ollama review call")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def parse_index() -> tuple[dict[str, FamilyIndexEntry], dict[str, Any]]:
    if not INDEX_PATH.exists():
        raise FileNotFoundError(f"Missing generated index: {INDEX_PATH}")
    text = INDEX_PATH.read_text()
    frontmatter, _ = parse_frontmatter(text)
    meta = dict(frontmatter or {})
    entries: dict[str, FamilyIndexEntry] = {}
    in_family_section = False
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line == "## Ranked normalized mechanism families":
            in_family_section = True
            continue
        if in_family_section and line.startswith("## "):
            break
        if not in_family_section or not line.startswith("- "):
            continue
        match = FAMILY_LINE_RE.match(line)
        if not match:
            continue
        entry = FamilyIndexEntry(
            family_slug=match.group("slug"),
            family_label=match.group("label"),
            total_occurrences=int(match.group("occurrences")),
            distinct_cases=int(match.group("cases")),
            distinct_personas=int(match.group("personas")),
            raw_candidate_count=int(match.group("raw")),
            canon_coverage_status=match.group("canon_status"),
            canon_coverage_driver=match.group("canon_driver") or None,
        )
        entries[entry.family_slug] = entry
    return entries, meta


def parse_example_occurrences(body: str) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    in_examples = False
    for raw_line in body.splitlines():
        line = raw_line.rstrip()
        if line == "## Example occurrences":
            in_examples = True
            continue
        if in_examples and line.startswith("## "):
            break
        if not in_examples or not line.startswith("- "):
            continue
        match = re.match(
            r"^- `(?P<label>.+?)` -> `(?P<artifact_path>.+?)` \(case `(?P<case_key>.+?)`, persona `(?P<persona>.+?)`, kind `(?P<artifact_kind>.+?)`, source `(?P<source>.+?)`\)$",
            line,
        )
        if not match:
            continue
        out.append(match.groupdict())
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
        match = re.match(r"^- `(.+?)` \((\d+)\)$", line)
        if match:
            out.append(match.group(1))
            continue
        match = re.match(r"^- `(.+?)`$", line)
        if match:
            out.append(match.group(1))
    return out


def extract_driver_summary(path: Path) -> str:
    text = path.read_text()
    lines = text.splitlines()
    in_summary = False
    collected: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped == "# Overview summary":
            in_summary = True
            continue
        if in_summary and stripped.startswith("## "):
            break
        if in_summary and stripped:
            collected.append(stripped)
    if collected:
        return " ".join(collected)
    frontmatter, body_start = parse_frontmatter(text)
    body = text[body_start:] if frontmatter is not None and body_start is not None else text
    for raw_line in body.splitlines():
        stripped = raw_line.strip()
        if stripped and not stripped.startswith('#'):
            return stripped
    return ""


def load_driver_catalog() -> dict[str, CanonicalDriverContext]:
    catalog: dict[str, CanonicalDriverContext] = {}
    if not DRIVER_ROOT.exists():
        return catalog
    for path in sorted(DRIVER_ROOT.rglob('*.md')):
        if path.name == 'README.md':
            continue
        text = path.read_text()
        frontmatter, _ = parse_frontmatter(text)
        frontmatter = frontmatter or {}
        slug = str(frontmatter.get('driver') or path.stem).strip()
        aliases = [str(a).strip() for a in listify(frontmatter.get('aliases')) if str(a).strip()]
        catalog[slug] = CanonicalDriverContext(
            driver_slug=slug,
            why_included='',
            summary=extract_driver_summary(path),
            aliases=aliases,
        )
    return catalog


def load_candidate_notes() -> list[CandidateNote]:
    notes: list[CandidateNote] = []
    if not CANDIDATE_NOTES_DIR.exists():
        return notes
    for path in sorted(CANDIDATE_NOTES_DIR.glob("generated-driver-candidate-*.md")):
        text = path.read_text()
        frontmatter, body_start = parse_frontmatter(text)
        if frontmatter is None or body_start is None:
            continue
        body = text[body_start:]
        rel_path = str(path.relative_to(WORKSPACE_ROOT)) if path.is_relative_to(WORKSPACE_ROOT) else str(path)
        notes.append(
            CandidateNote(
                path=path,
                rel_path=rel_path,
                candidate_slug=str(frontmatter.get("candidate_slug") or path.stem.replace("generated-driver-candidate-", "")),
                candidate_label=str(frontmatter.get("candidate_label") or "").strip().strip('"'),
                normalized_family=str(frontmatter.get("normalized_driver_family") or "").strip(),
                normalized_family_label=str(frontmatter.get("normalized_driver_family_label") or "").strip().strip('"'),
                canonical_coverage_status=str(frontmatter.get("canonical_coverage_status") or "").strip() or "novel",
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
                example_occurrences=parse_example_occurrences(body),
            )
        )
    return notes


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
        match = re.match(r"^- `(.+?)`$", line)
        if match:
            out.append(match.group(1))
    return out


def build_family_packets(index_entries: dict[str, FamilyIndexEntry], candidate_notes: list[CandidateNote]) -> dict[str, FamilyPacket]:
    grouped: dict[str, list[CandidateNote]] = defaultdict(list)
    for note in candidate_notes:
        if note.normalized_family:
            grouped[note.normalized_family].append(note)
    packets: dict[str, FamilyPacket] = {}
    for family_slug, candidates in grouped.items():
        entry = index_entries.get(family_slug)
        family_label = entry.family_label if entry else (candidates[0].normalized_family_label if candidates else family_slug.replace('-', ' '))
        packets[family_slug] = FamilyPacket(
            family_slug=family_slug,
            family_label=family_label,
            index_entry=entry,
            candidates=sorted(candidates, key=lambda c: (-c.total_occurrences, c.candidate_slug)),
        )
    return packets


def is_review_worthy(packet: FamilyPacket, args: argparse.Namespace) -> bool:
    requested = set(args.family_slug or [])
    if requested:
        return packet.family_slug in requested
    if args.all_families:
        return True
    entry = packet.index_entry
    if entry is None:
        return False
    return (
        entry.raw_candidate_count >= args.min_raw_candidates
        or entry.distinct_cases >= 2
        or entry.canon_coverage_status == "maybe_covered"
    )


def build_family_neighbors(packet: FamilyPacket, family_packets: dict[str, FamilyPacket]) -> list[dict[str, Any]]:
    neighbors: list[dict[str, Any]] = []
    own_tokens = set(packet.family_slug.split('-'))
    own_candidate_tokens = set()
    own_related_drivers = {d for c in packet.candidates for d in c.related_canonical_drivers}
    for c in packet.candidates:
        own_candidate_tokens.update(c.candidate_slug.split('-'))
        own_candidate_tokens.update(c.candidate_label.replace('-', ' ').split())
    for other_slug, other in family_packets.items():
        if other_slug == packet.family_slug:
            continue
        other_tokens = set(other.family_slug.split('-'))
        other_candidate_tokens = set()
        other_related_drivers = {d for c in other.candidates for d in c.related_canonical_drivers}
        for c in other.candidates:
            other_candidate_tokens.update(c.candidate_slug.split('-'))
            other_candidate_tokens.update(c.candidate_label.replace('-', ' ').split())
        family_overlap = len(own_tokens & other_tokens)
        candidate_overlap = len(own_candidate_tokens & other_candidate_tokens)
        related_overlap = len(own_related_drivers & other_related_drivers)
        overlap_score = family_overlap * 1.0 + candidate_overlap * 0.25 + related_overlap * 0.75
        if overlap_score <= 0:
            continue
        reason_parts = []
        if family_overlap:
            reason_parts.append('lexical')
        if candidate_overlap:
            reason_parts.append('candidate-token')
        if related_overlap:
            reason_parts.append('co-mentioned-driver')
        neighbors.append(
            {
                'family_slug': other.family_slug,
                'family_label': other.family_label,
                'reason': '+'.join(reason_parts),
                'overlap_score': round(overlap_score, 2),
            }
        )
    return sorted(neighbors, key=lambda item: (-item['overlap_score'], item['family_slug']))[:5]


def build_canonical_driver_context(packet: FamilyPacket, driver_catalog: dict[str, CanonicalDriverContext], heuristic_driver: str | None) -> list[dict[str, Any]]:
    scored: dict[str, dict[str, Any]] = {}

    def add(slug: str, why: str) -> None:
        slug = str(slug or '').strip()
        if not slug or slug not in driver_catalog:
            return
        entry = scored.setdefault(slug, {'driver_slug': slug, 'why': set()})
        entry['why'].add(why)

    if heuristic_driver:
        add(heuristic_driver, 'heuristic_overlap')
    for candidate in packet.candidates:
        for slug in candidate.canonical_driver_suggestions:
            add(slug, 'suggestion')
        for slug in candidate.related_canonical_drivers:
            add(slug, 'related_driver')
        if candidate.canonical_coverage_driver:
            add(candidate.canonical_coverage_driver, 'candidate_coverage')

    if not scored:
        family_tokens = set(packet.family_slug.split('-'))
        candidate_tokens = set()
        for candidate in packet.candidates:
            candidate_tokens.update(candidate.candidate_slug.split('-'))
            candidate_tokens.update(str(candidate.candidate_label).replace('-', ' ').lower().split())
        base_tokens = family_tokens | candidate_tokens
        lexical_scores: list[tuple[float, str]] = []
        for slug, canon in driver_catalog.items():
            canon_tokens = set(slug.split('-'))
            for alias in canon.aliases:
                canon_tokens.update(alias.replace('-', ' ').lower().split())
            overlap = len(base_tokens & canon_tokens)
            if overlap <= 0:
                continue
            score = overlap / max(1, len(canon_tokens))
            lexical_scores.append((score, slug))
        for _, slug in sorted(lexical_scores, reverse=True)[:3]:
            add(slug, 'lexical_nearby_driver')

    out: list[dict[str, Any]] = []
    for slug, meta in sorted(scored.items(), key=lambda item: (len(item[1]['why']), item[0]), reverse=True):
        canon = driver_catalog[slug]
        out.append(
            {
                'driver_slug': slug,
                'why_included': '+'.join(sorted(meta['why'])),
                'summary': canon.summary,
                'aliases': canon.aliases,
            }
        )
    return out[:6]


def packet_to_jsonable(
    packet: FamilyPacket,
    index_meta: dict[str, Any],
    family_packets: dict[str, FamilyPacket],
    driver_catalog: dict[str, CanonicalDriverContext],
) -> dict[str, Any]:
    entry = packet.index_entry
    heuristic_driver = entry.canon_coverage_driver if entry else None
    heuristic_summary = {
        "canon_coverage_status": entry.canon_coverage_status if entry else "novel",
        "canon_coverage_driver": heuristic_driver,
        "total_occurrences": entry.total_occurrences if entry else sum(c.total_occurrences for c in packet.candidates),
        "distinct_cases": entry.distinct_cases if entry else len({case for c in packet.candidates for case in c.case_keys}),
        "distinct_personas": entry.distinct_personas if entry else len({persona for c in packet.candidates for persona in c.personas}),
        "raw_candidate_count": entry.raw_candidate_count if entry else len(packet.candidates),
    }
    raw_candidates = []
    for candidate in packet.candidates:
        raw_candidates.append(
            {
                "candidate_slug": candidate.candidate_slug,
                "candidate_label": candidate.candidate_label,
                "occurrences": candidate.total_occurrences,
                "distinct_cases": candidate.distinct_cases,
                "distinct_personas": candidate.distinct_personas,
                "personas": candidate.personas,
                "case_keys": candidate.case_keys,
                "canonical_driver_suggestions": candidate.canonical_driver_suggestions,
                "related_canonical_drivers": candidate.related_canonical_drivers,
                "related_entities": candidate.related_entities,
                "label_variants": candidate.label_variants,
                "sample_occurrences": candidate.example_occurrences,
                "source_candidate_note": candidate.rel_path,
            }
        )
    return {
        "family_slug": packet.family_slug,
        "family_label": packet.family_label,
        "generated_at": NOW_UTC,
        "source_index_generated_at": index_meta.get("generated_at"),
        "heuristic_summary": heuristic_summary,
        "raw_candidates": raw_candidates,
        "family_neighbors": build_family_neighbors(packet, family_packets),
        "canonical_driver_context": build_canonical_driver_context(packet, driver_catalog, heuristic_driver),
        "review_task": {
            "allowed_actions": [
                "hold",
                "rename_family",
                "split_family",
                "merge_with_other_family",
                "merge_into_canon",
                "promote_new_family",
            ],
            "instruction": "Review whether this family grouping is coherent, whether it is already covered by canon, and what action is most appropriate.",
        },
    }


def packet_hash(payload: dict[str, Any]) -> str:
    stable_payload = json.loads(json.dumps(payload))
    stable_payload.pop("generated_at", None)
    stable_payload.pop("source_index_generated_at", None)
    canonical = json.dumps(stable_payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def sync_input_packets(selected: dict[str, dict[str, Any]]) -> dict[str, int]:
    FAMILY_REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    INPUTS_DIR.mkdir(parents=True, exist_ok=True)
    outcomes: dict[str, int] = defaultdict(int)
    expected: set[str] = set()
    for family_slug, payload in selected.items():
        name = f"generated-family-review-input-{family_slug}.json"
        expected.add(name)
        path = INPUTS_DIR / name
        content = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        if path.exists() and path.read_text() == content:
            outcomes["input_unchanged"] += 1
        else:
            path.write_text(content)
            outcomes["input_written"] += 1
    for path in INPUTS_DIR.glob("generated-family-review-input-*.json"):
        if path.name not in expected:
            path.unlink()
            outcomes["input_removed"] += 1
    return dict(outcomes)


def previously_reviewed_hash(family_slug: str) -> str | None:
    path = FAMILY_REVIEW_DIR / f"generated-family-review-{family_slug}.json"
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return None
    return str(payload.get("source_input_hash") or "").strip() or None


def build_system_prompt() -> str:
    return (
        "You are reviewing proposed causal-driver families for ontology normalization in a quantitative research memory system.\n\n"
        "Your job is to evaluate a single heuristic family cluster of proposed drivers and recommend a conservative next action.\n\n"
        "Important rules:\n"
        "1. Do not invent facts, cases, candidate labels, canonical drivers, or evidence not present in the input.\n"
        "2. Prefer conservative judgments. If evidence is sparse but the family still appears plausibly coherent, choose hold rather than split, merge, or promote.\n"
        "3. Only recommend split_family when the raw candidates appear to represent materially different mechanisms, not merely different personas, different wording, or sparse evidence.\n"
        "4. Only recommend merge_into_canon when the proposed family is substantially covered by an existing canonical driver in substance, not just vaguely adjacent.\n"
        "5. Only recommend promote_new_family when the family appears reusable, distinct, coherent, and not already covered by existing canon.\n"
        "6. Recommend merge_with_other_family only if the current family clearly belongs with a named neighboring family provided in the input.\n"
        "7. Keep reasoning short, concrete, and tied to the input.\n"
        "8. Output valid JSON only. No markdown. No extra commentary.\n\n"
        "Decision rubric:\n"
        "- hold: use when the family may be coherent but evidence is sparse, the grouping is not yet clear enough for promotion, or there is not enough basis for a confident split/merge.\n"
        "- split_family: use only when the raw candidates clearly point to two or more materially different mechanisms.\n"
        "- rename_family: use when the grouping seems coherent but the family name is poor or misleading.\n"
        "- merge_with_other_family: use when this family is better treated as part of a named neighboring family in the input.\n"
        "- merge_into_canon: use when an existing canonical driver already substantially covers the family.\n"
        "- promote_new_family: use when the family is coherent, reusable, and novel enough to deserve durable canon consideration.\n\n"
        "Consistency requirements:\n"
        "- If recommended_action is hold, then family_quality should usually say coherent_cluster=true and needs_split=false unless you explicitly explain why the cluster is borderline.\n"
        "- If recommended_action is split_family, then family_quality should say coherent_cluster=false and needs_split=true.\n"
        "- Do not recommend split_family solely because the evidence is sparse. Sparse evidence alone points to hold, not split.\n\n"
        "Return an object with exactly these fields: family_slug, recommended_action, recommended_family_slug, recommended_family_label, merge_target_family_slug, merge_target_canonical_driver, canon_overlap, family_quality, raw_candidate_assignments, rationale, suggested_follow_up.\n"
        "canon_overlap must be an object with fields status, canonical_driver_slug, reason.\n"
        "family_quality must be an object with fields coherent_cluster, needs_split, confidence.\n"
        "raw_candidate_assignments must be a list of objects with fields candidate_slug, candidate_label, recommended_family_slug, notes."
    )


def build_user_prompt(payload: dict[str, Any]) -> str:
    return (
        "Review this proposed-driver family cluster.\n\n"
        "Assess:\n"
        "- whether the current family is coherent\n"
        "- whether it overlaps strongly with existing canon\n"
        "- whether it should be held, renamed, split, merged, or promoted\n\n"
        "Return JSON only.\n\n"
        "Input:\n"
        f"{json.dumps(payload, ensure_ascii=False, indent=2)}"
    )


def normalize_action(value: Any) -> str:
    text = str(value or "").strip().lower().replace("-", "_").replace(" ", "_")
    if text in ALLOWED_ACTIONS:
        return text
    aliases = {
        "keep": "hold",
        "keep_as_is": "hold",
        "no_action": "hold",
        "rename": "rename_family",
        "split": "split_family",
        "merge": "merge_with_other_family",
        "merge_family": "merge_with_other_family",
        "merge_to_canon": "merge_into_canon",
        "promote": "promote_new_family",
        "promote_family": "promote_new_family",
    }
    return aliases.get(text, "hold")


def normalize_overlap(value: Any, fallback_driver: str | None) -> tuple[dict[str, Any], list[str]]:
    notes: list[str] = []
    if isinstance(value, dict):
        status = str(value.get("status") or "").strip().lower()
        canonical_driver_slug = str(value.get("canonical_driver_slug") or fallback_driver or "").strip() or None
        reason = str(value.get("reason") or "").strip()
    else:
        status = str(value or "").strip().lower()
        canonical_driver_slug = fallback_driver
        reason = ""
        if status:
            notes.append("canon_overlap_coerced_from_scalar")
    if status not in ALLOWED_CANON_OVERLAP:
        if canonical_driver_slug:
            status = "partial"
            notes.append("canon_overlap_status_defaulted_to_partial")
        else:
            status = "none"
            notes.append("canon_overlap_status_defaulted_to_none")
    return {
        "status": status,
        "canonical_driver_slug": canonical_driver_slug,
        "reason": reason,
    }, notes


def normalize_family_quality(value: Any, action: str) -> tuple[dict[str, Any], list[str]]:
    notes: list[str] = []
    if isinstance(value, dict):
        confidence = str(value.get("confidence") or "").strip().lower()
        coherent_cluster = bool(value.get("coherent_cluster")) if "coherent_cluster" in value else action != "split_family"
        needs_split = bool(value.get("needs_split")) if "needs_split" in value else action == "split_family"
    else:
        confidence = str(value or "").strip().lower()
        coherent_cluster = action != "split_family"
        needs_split = action == "split_family"
        if confidence:
            notes.append("family_quality_coerced_from_scalar")
    if confidence not in ALLOWED_CONFIDENCE:
        confidence = "low"
        notes.append("family_quality_confidence_defaulted")
    return {
        "coherent_cluster": coherent_cluster,
        "needs_split": needs_split,
        "confidence": confidence,
    }, notes


def normalize_candidate_assignments(value: Any, payload: dict[str, Any], family_slug: str) -> tuple[list[dict[str, Any]], list[str]]:
    notes: list[str] = []
    by_slug = {item.get("candidate_slug"): item for item in payload.get("raw_candidates") or []}
    normalized: list[dict[str, Any]] = []
    seen: set[str] = set()
    if isinstance(value, list):
        for item in value:
            if not isinstance(item, dict):
                continue
            candidate_slug = str(item.get("candidate_slug") or "").strip()
            if not candidate_slug or candidate_slug not in by_slug:
                continue
            src = by_slug[candidate_slug]
            normalized.append(
                {
                    "candidate_slug": candidate_slug,
                    "candidate_label": str(item.get("candidate_label") or src.get("candidate_label") or "").strip(),
                    "recommended_family_slug": str(item.get("recommended_family_slug") or family_slug).strip() or family_slug,
                    "notes": str(item.get("notes") or item.get("rationale") or item.get("action") or "").strip(),
                }
            )
            seen.add(candidate_slug)
    for candidate_slug, src in by_slug.items():
        if candidate_slug in seen:
            continue
        normalized.append(
            {
                "candidate_slug": candidate_slug,
                "candidate_label": str(src.get("candidate_label") or "").strip(),
                "recommended_family_slug": family_slug,
                "notes": "",
            }
        )
        notes.append(f"candidate_assignment_defaulted:{candidate_slug}")
    return normalized, notes


def normalize_review_output(parsed_review: dict[str, Any], payload: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    notes: list[str] = []
    family_slug = str(parsed_review.get("family_slug") or payload.get("family_slug") or "").strip()
    if family_slug != str(payload.get("family_slug") or ""):
        notes.append("family_slug_normalized_from_input")
        family_slug = str(payload.get("family_slug") or family_slug)

    action = normalize_action(parsed_review.get("recommended_action"))
    if action != str(parsed_review.get("recommended_action") or ""):
        notes.append("recommended_action_normalized")

    canon_overlap, overlap_notes = normalize_overlap(
        parsed_review.get("canon_overlap"),
        str(parsed_review.get("merge_target_canonical_driver") or "").strip() or None,
    )
    notes.extend(overlap_notes)

    family_quality, quality_notes = normalize_family_quality(parsed_review.get("family_quality"), action)
    notes.extend(quality_notes)

    assignments, assignment_notes = normalize_candidate_assignments(
        parsed_review.get("raw_candidate_assignments"), payload, family_slug
    )
    notes.extend(assignment_notes)

    normalized = {
        "family_slug": family_slug,
        "recommended_action": action,
        "recommended_family_slug": str(parsed_review.get("recommended_family_slug") or "").strip() or None,
        "recommended_family_label": str(parsed_review.get("recommended_family_label") or "").strip() or None,
        "merge_target_family_slug": str(parsed_review.get("merge_target_family_slug") or "").strip() or None,
        "merge_target_canonical_driver": str(parsed_review.get("merge_target_canonical_driver") or canon_overlap.get("canonical_driver_slug") or "").strip() or None,
        "canon_overlap": canon_overlap,
        "family_quality": family_quality,
        "raw_candidate_assignments": assignments,
        "rationale": str(parsed_review.get("rationale") or "").strip(),
        "suggested_follow_up": str(parsed_review.get("suggested_follow_up") or "").strip(),
    }

    if not normalized["recommended_family_slug"] and action in {"rename_family", "promote_new_family"}:
        normalized["recommended_family_slug"] = family_slug
        notes.append("recommended_family_slug_defaulted")
    if not normalized["recommended_family_label"] and action in {"rename_family", "promote_new_family"}:
        normalized["recommended_family_label"] = str(payload.get("family_label") or "").strip() or None
        notes.append("recommended_family_label_defaulted")
    if action == "merge_into_canon" and not normalized["merge_target_canonical_driver"]:
        normalized["merge_target_canonical_driver"] = canon_overlap.get("canonical_driver_slug")
        notes.append("merge_target_canonical_driver_defaulted_from_overlap")

    return normalized, notes


def call_ollama(model: str, ollama_url: str, payload: dict[str, Any], timeout_seconds: int) -> tuple[str, dict[str, Any], dict[str, Any]]:
    request_payload = {
        "model": model,
        "system": build_system_prompt(),
        "prompt": build_user_prompt(payload),
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.2,
        },
    }
    data = json.dumps(request_payload).encode("utf-8")
    request = urllib.request.Request(
        ollama_url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout_seconds) as response:  # noqa: S310
        raw = response.read().decode("utf-8")
    decoded = json.loads(raw)
    model_text = str(decoded.get("response") or "").strip()
    if not model_text:
        model_text = str(decoded.get("thinking") or "").strip()
    if not model_text:
        raise ValueError(f"Ollama returned no JSON text: {raw[:500]}")
    parsed = json.loads(model_text)
    return model_text, parsed, decoded


def render_review_markdown(payload: dict[str, Any]) -> str:
    normalized = payload.get("normalized_review") or {}
    overlap = normalized.get("canon_overlap") or {}
    quality = normalized.get("family_quality") or {}
    assignments = normalized.get("raw_candidate_assignments") or []
    notes = payload.get("normalization_notes") or []
    source_input_rel = str(payload.get("source_input_path") or "").strip()
    source_candidates: list[dict[str, str]] = []
    if source_input_rel:
        input_path = WORKSPACE_ROOT / source_input_rel
        if input_path.exists():
            try:
                input_payload = json.loads(input_path.read_text())
                for item in input_payload.get("raw_candidates") or []:
                    source_candidates.append(
                        {
                            "candidate_label": str(item.get("candidate_label") or item.get("candidate_slug") or "").strip(),
                            "candidate_slug": str(item.get("candidate_slug") or "").strip(),
                            "source_candidate_note": str(item.get("source_candidate_note") or "").strip(),
                        }
                    )
            except Exception:
                source_candidates = []
    lines = [
        "---",
        "type: proposed_driver_family_review",
        f"family_slug: {payload.get('family_slug')}",
        f"review_model: {payload.get('review_model')}",
        f"generated_at: {payload.get('generated_at')}",
        f"prompt_version: {payload.get('prompt_version')}",
        f"recommended_action: {normalized.get('recommended_action') or ''}",
        f"recommended_family_slug: {normalized.get('recommended_family_slug') or ''}",
        f"recommended_family_label: {json.dumps(normalized.get('recommended_family_label') or '', ensure_ascii=False)}",
        f"merge_target_family_slug: {normalized.get('merge_target_family_slug') or ''}",
        f"merge_target_canonical_driver: {normalized.get('merge_target_canonical_driver') or ''}",
        f"canon_overlap_status: {overlap.get('status') or ''}",
        f"canon_overlap_driver: {overlap.get('canonical_driver_slug') or ''}",
        f"review_confidence: {quality.get('confidence') or ''}",
        "status: active",
        "---",
        "",
        f"# Family review: {payload.get('family_slug')}",
        "",
        "## Recommendation",
        f"- action: `{normalized.get('recommended_action') or ''}`",
        f"- recommended family slug: `{normalized.get('recommended_family_slug') or ''}`",
        f"- recommended family label: `{normalized.get('recommended_family_label') or ''}`",
        f"- merge target family: `{normalized.get('merge_target_family_slug') or ''}`",
        f"- merge target canonical driver: `{normalized.get('merge_target_canonical_driver') or ''}`",
        "",
        "## Canon overlap",
        f"- status: `{overlap.get('status') or ''}`",
        f"- canonical driver: `{overlap.get('canonical_driver_slug') or ''}`",
        f"- reason: {overlap.get('reason') or ''}",
        "",
        "## Family quality",
        f"- coherent cluster: `{quality.get('coherent_cluster')}`",
        f"- needs split: `{quality.get('needs_split')}`",
        f"- confidence: `{quality.get('confidence') or ''}`",
        "",
        "## Rationale",
        normalized.get('rationale') or '',
        "",
        "## Raw candidate assignments",
    ]
    if assignments:
        for item in assignments:
            lines.append(
                f"- `{item.get('candidate_label') or item.get('candidate_slug')}` -> family `{item.get('recommended_family_slug') or ''}`"
                f" | notes: {item.get('notes') or ''}"
            )
    else:
        lines.append("- none")
    lines.extend([
        "",
        "## Suggested follow-up",
        normalized.get('suggested_follow_up') or '',
        "",
        "## Normalization notes",
    ])
    if notes:
        lines.extend(f"- `{note}`" for note in notes)
    else:
        lines.append("- none")
    lines.extend([
        "",
        "## Source candidate notes",
    ])
    if source_candidates:
        for item in source_candidates:
            lines.append(
                f"- `{item.get('candidate_label') or item.get('candidate_slug')}` -> `{item.get('source_candidate_note') or ''}`"
            )
    else:
        lines.append("- none")
    lines.extend([
        "",
        "## Source input",
        f"- `{payload.get('source_input_path') or ''}`",
        "",
    ])
    return "\n".join(lines)


def render_review_index(outputs: dict[str, dict[str, Any]], review_model: str) -> str:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for payload in outputs.values():
        action = ((payload.get('normalized_review') or {}).get('recommended_action') or 'hold')
        grouped[action].append(payload)
    action_order = [
        'promote_new_family',
        'merge_into_canon',
        'rename_family',
        'split_family',
        'merge_with_other_family',
        'hold',
    ]
    lines = [
        '---',
        'type: proposed_driver_family_review_index',
        'generated_by: ollama_family_review_pass',
        f'generated_at: {NOW_UTC}',
        f'review_model: {review_model}',
        f'family_review_count: {len(outputs)}',
        'status: active',
        '---',
        '',
        '# Generated family review suggestions',
        '',
    ]
    for action in action_order:
        lines.append(f'## {action}')
        items = sorted(grouped.get(action, []), key=lambda p: p.get('family_slug') or '')
        if not items:
            lines.append('- none')
            lines.append('')
            continue
        for payload in items:
            normalized = payload.get('normalized_review') or {}
            overlap = normalized.get('canon_overlap') or {}
            name = f"review-notes/generated-family-review-{payload.get('family_slug')}.md"
            lines.append(
                f"- `{payload.get('family_slug')}` -> `{name}` "
                f"(confidence: `{(normalized.get('family_quality') or {}).get('confidence') or ''}`, canon_overlap: `{overlap.get('status') or ''}`)"
            )
        lines.append('')
    return '\n'.join(lines)


def load_existing_review_outputs() -> dict[str, dict[str, Any]]:
    outputs: dict[str, dict[str, Any]] = {}
    if not FAMILY_REVIEW_DIR.exists():
        return outputs
    for path in FAMILY_REVIEW_DIR.glob("generated-family-review-*.json"):
        try:
            payload = json.loads(path.read_text())
        except Exception:
            continue
        family_slug = str(payload.get("family_slug") or "").strip()
        if family_slug:
            outputs[family_slug] = payload
    return outputs


def sync_review_outputs(outputs: dict[str, dict[str, Any]], review_model: str, active_family_slugs: set[str] | None = None) -> dict[str, int]:
    FAMILY_REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    REVIEW_NOTES_DIR.mkdir(parents=True, exist_ok=True)
    outcomes: dict[str, int] = defaultdict(int)
    written_md: set[str] = set()
    for family_slug, payload in outputs.items():
        json_name = f"generated-family-review-{family_slug}.json"
        md_name = f"generated-family-review-{family_slug}.md"

        json_path = FAMILY_REVIEW_DIR / json_name
        json_content = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        if json_path.exists() and json_path.read_text() == json_content:
            outcomes["review_json_unchanged"] += 1
        else:
            json_path.write_text(json_content)
            outcomes["review_json_written"] += 1

        md_path = REVIEW_NOTES_DIR / md_name
        md_content = render_review_markdown(payload)
        written_md.add(md_name)
        if md_path.exists() and md_path.read_text() == md_content:
            outcomes["review_md_unchanged"] += 1
        else:
            md_path.write_text(md_content)
            outcomes["review_md_written"] += 1

    all_outputs = load_existing_review_outputs()
    if active_family_slugs is not None:
        all_outputs = {slug: payload for slug, payload in all_outputs.items() if slug in active_family_slugs}
    index_content = render_review_index(all_outputs, review_model)
    if FAMILY_REVIEW_INDEX_PATH.exists() and FAMILY_REVIEW_INDEX_PATH.read_text() == index_content:
        outcomes["review_index_unchanged"] += 1
    else:
        FAMILY_REVIEW_INDEX_PATH.write_text(index_content)
        outcomes["review_index_written"] += 1

    for path in FAMILY_REVIEW_DIR.glob("generated-family-review-*.md"):
        path.unlink()
        outcomes["legacy_review_md_removed"] += 1
    return dict(outcomes)


def main() -> int:
    args = parse_args()
    index_entries, index_meta = parse_index()
    candidate_notes = load_candidate_notes()
    driver_catalog = load_driver_catalog()
    family_packets = build_family_packets(index_entries, candidate_notes)
    selected_packets = {
        slug: packet_to_jsonable(packet, index_meta, family_packets, driver_catalog)
        for slug, packet in sorted(family_packets.items())
        if is_review_worthy(packet, args)
    }
    input_outcomes = sync_input_packets(selected_packets)

    review_outputs: dict[str, dict[str, Any]] = {}
    review_errors: dict[str, str] = {}
    review_outcomes: dict[str, int] = {}
    skipped_review_families: list[str] = []
    if args.run_ollama:
        for family_slug, packet in selected_packets.items():
            current_hash = packet_hash(packet)
            previous_hash = previously_reviewed_hash(family_slug)
            if args.auto and previous_hash and previous_hash == current_hash:
                skipped_review_families.append(family_slug)
                continue
            try:
                raw_model_output, parsed_review, raw_api_response = call_ollama(args.model, args.ollama_url, packet, args.timeout_seconds)
                normalized_review, normalization_notes = normalize_review_output(parsed_review, packet)
                review_outputs[family_slug] = {
                    "type": "proposed_driver_family_review_suggestion",
                    "family_slug": family_slug,
                    "review_model": args.model,
                    "generated_at": NOW_UTC,
                    "prompt_version": PROMPT_VERSION,
                    "source_input_path": str((INPUTS_DIR / f"generated-family-review-input-{family_slug}.json").relative_to(WORKSPACE_ROOT)),
                    "source_input_hash": current_hash,
                    "raw_model_output": raw_model_output,
                    "raw_api_response": raw_api_response,
                    "parsed_review": parsed_review,
                    "normalized_review": normalized_review,
                    "normalization_notes": normalization_notes,
                }
            except Exception as exc:  # noqa: BLE001
                review_errors[family_slug] = str(exc)
        review_outcomes = sync_review_outputs(review_outputs, args.model, set(selected_packets.keys()))

    result = {
        "status": "ok",
        "index_path": str(INDEX_PATH.relative_to(WORKSPACE_ROOT)),
        "candidate_note_count": len(candidate_notes),
        "family_count": len(family_packets),
        "selected_family_count": len(selected_packets),
        "selected_families": sorted(selected_packets.keys()),
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
    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
    else:
        print(json.dumps(result, separators=(",", ":"), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
