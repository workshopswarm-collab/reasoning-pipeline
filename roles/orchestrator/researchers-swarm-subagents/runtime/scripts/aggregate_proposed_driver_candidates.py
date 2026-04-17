#!/usr/bin/env python3
from __future__ import annotations

"""Aggregate proposed driver labels into generated review-queue candidate notes.

E2 behavior:
- read proposed-driver occurrences from Postgres when available
- supplement with markdown-derived occurrences that are not yet present in the DB
- write generated top-level index into:

  qualitative-db/40-research/review-queue/drivers-candidates/generated-index.md

- write generated raw candidate notes into:

  qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/

- reserve:

  qualitative-db/40-research/review-queue/drivers-candidates/surfaced-family-review/

  for LLM-assisted family review outputs

This preserves historical visibility before backfill while moving the system toward
Postgres as the durable source of truth.
"""

import argparse
import json
import os
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from validate_research_artifact_linkages import (  # type: ignore
    DRIVER_ROOT,
    WORKSPACE_ROOT,
    listify,
    load_catalog,
    parse_frontmatter,
    resolve_value,
    slugify,
)

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
QUEUE_DIR = WORKSPACE_ROOT / "qualitative-db" / "40-research" / "review-queue" / "drivers-candidates"
CANDIDATE_NOTES_DIR = QUEUE_DIR / "candidate-notes"
FAMILY_REVIEW_DIR = QUEUE_DIR / "surfaced-family-review"
INDEX_PATH = QUEUE_DIR / "generated-index.md"
INDEX_JSON_PATH = QUEUE_DIR / "generated-index.json"
GENERATED_PREFIX = "generated-driver-candidate-"
NOW_UTC = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
MAX_EXAMPLES = 12
GENERIC_CANONICAL_DRIVERS = {
    'performance',
    'sentiment',
    'operational-risk',
    'reliability',
    'momentum',
    'volatility',
}
MIN_SURFACED_FAMILY_RAW_CANDIDATES = 2
MIN_SURFACED_FAMILY_DISTINCT_CASES = 2

DB_OCCURRENCES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(x) ORDER BY x.occurred_at DESC NULLS LAST, x.artifact_path), '[]'::json)::text
FROM (
  SELECT
    artifact_path,
    proposed_driver_label,
    proposed_driver_slug,
    case_key,
    dispatch_id,
    persona,
    artifact_kind,
    occurred_at,
    related_entities,
    related_canonical_drivers,
    canonical_driver_suggestions,
    status
  FROM public.proposed_driver_occurrences
  WHERE status = 'active'
) x;
'''


@dataclass
class Occurrence:
    label: str
    label_slug: str
    rel_path: str
    case_key: str | None
    dispatch_id: str | None
    persona: str | None
    artifact_kind: str
    occurred_at: str | None
    related_entities: list[str]
    related_drivers: list[str]
    suggestions: list[str]
    source: str


@dataclass(frozen=True)
class OccurrenceKey:
    artifact_path: str
    proposed_driver_slug: str


@dataclass(frozen=True)
class FamilyInfo:
    slug: str
    label: str


@dataclass(frozen=True)
class CanonCoverage:
    status: str
    canonical_slug: str | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Aggregate proposed driver labels into generated review-queue notes")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def exec_sql(psql_bin: str, db_url: str, sql: str) -> Any:
    if not db_url:
        return []
    proc = subprocess.run([psql_bin, db_url, '-X', '-qAt', '-v', 'ON_ERROR_STOP=1', '-f', '-'], input=sql, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'psql failed')
    stdout = proc.stdout.strip()
    return json.loads(stdout.splitlines()[-1]) if stdout else []


def iter_case_artifacts() -> list[Path]:
    base = WORKSPACE_ROOT / "qualitative-db" / "40-research" / "cases"
    out: list[Path] = []
    for path in sorted(base.rglob("*.md")):
        rel = path.relative_to(WORKSPACE_ROOT)
        parts = rel.parts
        if "researcher-analyses" not in parts:
            continue
        if not any(part in {"personas", "assumptions", "evidence"} for part in parts):
            continue
        out.append(path)
    return out


def classify_artifact(path: Path) -> tuple[str, str | None, str | None, str | None]:
    rel = path.relative_to(WORKSPACE_ROOT)
    parts = rel.parts
    artifact_kind = "unknown"
    case_key = None
    dispatch_id = None
    persona = None
    if "cases" in parts:
        idx = parts.index("cases")
        if idx + 1 < len(parts):
            case_key = parts[idx + 1]
    if "researcher-analyses" in parts:
        idx = parts.index("researcher-analyses")
        if idx + 2 < len(parts):
            dispatch_id = parts[idx + 2]
    for kind in ["personas", "assumptions", "evidence"]:
        if kind in parts:
            artifact_kind = kind[:-1] if kind.endswith("s") else kind
            persona = path.stem
            break
    return artifact_kind, case_key, dispatch_id, persona


def load_db_occurrences(psql_bin: str, db_url: str) -> tuple[list[Occurrence], set[OccurrenceKey]]:
    rows = exec_sql(psql_bin, db_url, DB_OCCURRENCES_SQL) if db_url else []
    occurrences: list[Occurrence] = []
    keys: set[OccurrenceKey] = set()
    for row in rows or []:
        artifact_path = row.get("artifact_path") or ""
        slug = row.get("proposed_driver_slug") or ""
        if not artifact_path or not slug:
            continue
        key = OccurrenceKey(artifact_path=artifact_path, proposed_driver_slug=slug)
        keys.add(key)
        occurrences.append(
            Occurrence(
                label=row.get("proposed_driver_label") or slug,
                label_slug=slug,
                rel_path=artifact_path,
                case_key=row.get("case_key"),
                dispatch_id=row.get("dispatch_id"),
                persona=row.get("persona"),
                artifact_kind=row.get("artifact_kind") or "unknown",
                occurred_at=row.get("occurred_at"),
                related_entities=listify(row.get("related_entities")),
                related_drivers=listify(row.get("related_canonical_drivers")),
                suggestions=listify(row.get("canonical_driver_suggestions")),
                source="db",
            )
        )
    return occurrences, keys


def load_markdown_only_occurrences(existing_keys: set[OccurrenceKey]) -> list[Occurrence]:
    driver_aliases, driver_slugs = load_catalog(DRIVER_ROOT, kind="driver")
    occurrences: list[Occurrence] = []
    for path in iter_case_artifacts():
        text = path.read_text()
        frontmatter, _ = parse_frontmatter(text)
        if frontmatter is None:
            continue
        proposed_drivers = listify(frontmatter.get("proposed_drivers"))
        if not proposed_drivers:
            continue
        artifact_kind, case_key, dispatch_id, persona = classify_artifact(path)
        related_entities = listify(frontmatter.get("related_entities"))
        related_drivers = listify(frontmatter.get("related_drivers"))
        date_created = frontmatter.get("date_created") if isinstance(frontmatter.get("date_created"), str) else None
        rel_path = str(path.relative_to(WORKSPACE_ROOT))
        for label in proposed_drivers:
            slug = slugify(label)
            if not slug:
                continue
            key = OccurrenceKey(artifact_path=rel_path, proposed_driver_slug=slug)
            if key in existing_keys:
                continue
            _, suggestions = resolve_value(label, driver_aliases, driver_slugs)
            occurrences.append(
                Occurrence(
                    label=label,
                    label_slug=slug,
                    rel_path=rel_path,
                    case_key=case_key,
                    dispatch_id=dispatch_id,
                    persona=persona,
                    artifact_kind=artifact_kind,
                    occurred_at=date_created,
                    related_entities=related_entities,
                    related_drivers=related_drivers,
                    suggestions=suggestions,
                    source="markdown_fallback",
                )
            )
    return occurrences


def collect_occurrences(psql_bin: str, db_url: str) -> tuple[dict[str, list[Occurrence]], dict[str, int]]:
    db_occurrences, db_keys = load_db_occurrences(psql_bin, db_url)
    markdown_occurrences = load_markdown_only_occurrences(db_keys)
    grouped: dict[str, list[Occurrence]] = defaultdict(list)
    for occ in db_occurrences + markdown_occurrences:
        grouped[occ.label_slug].append(occ)
    source_counts = {
        "db_occurrence_count": len(db_occurrences),
        "markdown_fallback_occurrence_count": len(markdown_occurrences),
    }
    return grouped, source_counts


def choose_family(label: str, suggestions: list[str], related_drivers: list[str]) -> FamilyInfo:
    slug = slugify(label)
    text = slug.replace('-', ' ')
    tokens = set(filter(None, re.split(r'[^a-z0-9]+', text)))
    suggestion_set = {slugify(s) for s in suggestions if s}
    related_set = {slugify(s) for s in related_drivers if s}

    def has(*words: str) -> bool:
        return any(word in tokens for word in words)

    if has('expiry') and has('timing'):
        return FamilyInfo(slug='expiry-timing', label='expiry timing')
    if has('release', 'window', 'week', 'viewership', 'demand', 'concentration'):
        return FamilyInfo(slug='release-window-demand', label='release-window demand')
    if has('chart', 'publication', 'refresh', 'timing') and (has('publication', 'refresh', 'timing') or 'publication-timing-risk' in suggestion_set):
        return FamilyInfo(slug='publication-timing', label='publication timing')
    if has('title', 'label', 'mapping') or {'title', 'mapping'} <= tokens or {'label', 'mapping'} <= tokens:
        return FamilyInfo(slug='resolution-mapping', label='resolution mapping')
    if has('resolution', 'settlement', 'mechanics', 'threshold') or related_set.intersection({'operational-risk', 'reliability'}):
        return FamilyInfo(slug='resolution-mechanics', label='resolution mechanics')
    return FamilyInfo(slug=slug, label=label)


def assess_canon_coverage(family: FamilyInfo, occurrences: list[Occurrence], driver_slugs: list[str]) -> CanonCoverage:
    canonical_slug_set = set(driver_slugs)
    if family.slug in canonical_slug_set:
        return CanonCoverage(status='covered', canonical_slug=family.slug)

    family_tokens = set(filter(None, family.slug.split('-')))
    distinct_cases = len({o.case_key for o in occurrences if o.case_key})
    distinct_personas = len({o.persona for o in occurrences if o.persona})

    suggestion_counts = Counter(slugify(s) for o in occurrences for s in o.suggestions if s)
    if suggestion_counts:
        top_slug, top_count = suggestion_counts.most_common(1)[0]
        top_tokens = set(filter(None, top_slug.split('-')))
        token_overlap = len(family_tokens & top_tokens)
        if (
            top_slug not in GENERIC_CANONICAL_DRIVERS
            and top_slug in canonical_slug_set
            and top_count >= 2
            and (distinct_cases >= 2 or distinct_personas >= 2)
            and token_overlap >= 1
        ):
            return CanonCoverage(status='maybe_covered', canonical_slug=top_slug)

    related_driver_counts = Counter(slugify(d) for o in occurrences for d in o.related_drivers if d)
    if related_driver_counts:
        top_related, top_count = related_driver_counts.most_common(1)[0]
        top_tokens = set(filter(None, top_related.split('-')))
        token_overlap = len(family_tokens & top_tokens)
        if (
            top_related not in GENERIC_CANONICAL_DRIVERS
            and top_related in canonical_slug_set
            and top_count >= 3
            and distinct_cases >= 2
            and token_overlap >= 1
        ):
            return CanonCoverage(status='maybe_covered', canonical_slug=top_related)

    return CanonCoverage(status='novel', canonical_slug=None)


def build_family_groups(grouped: dict[str, list[Occurrence]], driver_slugs: list[str]) -> dict[str, dict[str, Any]]:
    families: dict[str, dict[str, Any]] = {}
    for slug, occurrences in grouped.items():
        primary_label = Counter(o.label for o in occurrences).most_common(1)[0][0]
        related_drivers = [driver for o in occurrences for driver in o.related_drivers]
        suggestions = [s for o in occurrences for s in o.suggestions]
        family = choose_family(primary_label, suggestions, related_drivers)
        bucket = families.setdefault(
            family.slug,
            {
                'family': family,
                'candidate_slugs': [],
                'candidate_labels': [],
                'occurrences': [],
            },
        )
        bucket['candidate_slugs'].append(slug)
        bucket['candidate_labels'].append(primary_label)
        bucket['occurrences'].extend(occurrences)
    for info in families.values():
        info['canon_coverage'] = assess_canon_coverage(info['family'], info['occurrences'], driver_slugs)
    return families


def render_candidate_note(slug: str, occurrences: list[Occurrence], driver_slugs: list[str]) -> str:
    primary_label = Counter(o.label for o in occurrences).most_common(1)[0][0]
    label_variants = [label for label, _ in Counter(o.label for o in occurrences).most_common()]
    case_keys = sorted({o.case_key for o in occurrences if o.case_key})
    personas = sorted({o.persona for o in occurrences if o.persona})
    artifact_kinds = Counter(o.artifact_kind for o in occurrences if o.artifact_kind)
    related_entities = Counter(entity for o in occurrences for entity in o.related_entities)
    related_drivers = Counter(driver for o in occurrences for driver in o.related_drivers)
    suggestions = Counter(s for o in occurrences for s in o.suggestions)
    source_mix = Counter(o.source for o in occurrences)
    timestamps = [o.occurred_at for o in occurrences if o.occurred_at]
    first_seen = min(timestamps) if timestamps else NOW_UTC
    last_seen = max(timestamps) if timestamps else NOW_UTC
    family = choose_family(primary_label, list(suggestions.elements()), list(related_drivers.elements()))
    coverage = assess_canon_coverage(family, occurrences, driver_slugs)

    lines = [
        "---",
        "type: proposed_driver_candidate",
        f"candidate_slug: {slug}",
        f"candidate_label: {json.dumps(primary_label, ensure_ascii=False)}",
        f"label_variants: {json.dumps(label_variants, ensure_ascii=False)}",
        f"normalized_driver_family: {family.slug}",
        f"normalized_driver_family_label: {json.dumps(family.label, ensure_ascii=False)}",
        f"canonical_coverage_status: {coverage.status}",
        f"canonical_coverage_driver: {coverage.canonical_slug or ''}",
        f"generated_by: proposed_driver_candidate_aggregator",
        f"generated_at: {NOW_UTC}",
        "status: active",
        f"total_occurrences: {len(occurrences)}",
        f"distinct_cases: {len(case_keys)}",
        f"distinct_personas: {len(personas)}",
        f"artifact_kinds: {json.dumps(dict(artifact_kinds), ensure_ascii=False, sort_keys=True)}",
        f"source_mix: {json.dumps(dict(source_mix), ensure_ascii=False, sort_keys=True)}",
        f"first_seen: {first_seen}",
        f"last_seen: {last_seen}",
        "---",
        "",
        f"# Proposed driver candidate: {primary_label}",
        "",
        "## Why this candidate exists",
        f"This generated note tracks repeated use of the unresolved proposed driver label `{primary_label}` across case research artifacts.",
        "",
        "## Frequency snapshot",
        f"- total occurrences: **{len(occurrences)}**",
        f"- distinct cases: **{len(case_keys)}**",
        f"- distinct personas: **{len(personas)}**",
        f"- artifact kinds: `{dict(artifact_kinds)}`",
        f"- source mix: `{dict(source_mix)}`",
        "",
        "## Normalized driver family",
        f"- family: `{family.label}` (`{family.slug}`)",
        "",
        "## Label variants observed",
    ]
    for label in label_variants:
        lines.append(f"- `{label}`")
    lines.extend([
        "",
        "## Cases observed",
    ])
    for case_key in case_keys:
        lines.append(f"- `{case_key}`")
    lines.extend([
        "",
        "## Personas observed",
    ])
    for persona in personas:
        lines.append(f"- `{persona}`")
    if related_entities:
        lines.extend([
            "",
            "## Common co-mentioned entities",
        ])
        for entity, count in related_entities.most_common(8):
            lines.append(f"- `{entity}` ({count})")
    if related_drivers:
        lines.extend([
            "",
            "## Common co-mentioned canonical drivers",
        ])
        for driver, count in related_drivers.most_common(8):
            lines.append(f"- `{driver}` ({count})")
    if suggestions:
        lines.extend([
            "",
            "## Nearest existing canonical driver suggestions",
        ])
        for suggestion, count in suggestions.most_common(8):
            lines.append(f"- `{suggestion}` ({count})")
    lines.extend([
        "",
        "## Example occurrences",
    ])
    for occ in sorted(occurrences, key=lambda o: (o.case_key or "", o.dispatch_id or "", o.persona or "", o.rel_path))[:MAX_EXAMPLES]:
        lines.append(
            f"- `{occ.label}` -> `{occ.rel_path}`"
            f" (case `{occ.case_key or 'unknown'}`, persona `{occ.persona or 'unknown'}`, kind `{occ.artifact_kind}`, source `{occ.source}`)"
        )
    lines.extend([
        "",
        "## Promotion review guidance",
        "Consider promotion when this candidate recurs across multiple cases/personas and represents a durable causal mechanism rather than a case-local phrasing artifact.",
        "",
    ])
    return "\n".join(lines)


def render_index(grouped: dict[str, list[Occurrence]], source_counts: dict[str, int], driver_slugs: list[str]) -> str:
    ranked = sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0]))
    family_groups = build_family_groups(grouped, driver_slugs)
    surfaced_families: list[tuple[str, dict[str, Any]]] = []
    provisional_families: list[tuple[str, dict[str, Any]]] = []
    for family_slug, info in family_groups.items():
        occurrences = info['occurrences']
        coverage = info['canon_coverage']
        raw_candidate_count = len(set(info['candidate_slugs']))
        distinct_cases = len({o.case_key for o in occurrences if o.case_key})
        if (
            raw_candidate_count >= MIN_SURFACED_FAMILY_RAW_CANDIDATES
            or distinct_cases >= MIN_SURFACED_FAMILY_DISTINCT_CASES
            or coverage.status == 'maybe_covered'
        ):
            surfaced_families.append((family_slug, info))
        else:
            provisional_families.append((family_slug, info))
    ranked_families = sorted(surfaced_families, key=lambda item: (-len(item[1]['occurrences']), item[0]))
    ranked_provisional = sorted(provisional_families, key=lambda item: (-len(item[1]['occurrences']), item[0]))
    lines = [
        "---",
        "type: proposed_driver_candidate_index",
        f"generated_by: proposed_driver_candidate_aggregator",
        f"generated_at: {NOW_UTC}",
        f"candidate_count: {len(ranked)}",
        f"normalized_family_count: {len(ranked_families)}",
        f"provisional_family_count: {len(ranked_provisional)}",
        f"db_occurrence_count: {source_counts.get('db_occurrence_count', 0)}",
        f"markdown_fallback_occurrence_count: {source_counts.get('markdown_fallback_occurrence_count', 0)}",
        "status: active",
        "---",
        "",
        "# Generated proposed-driver candidate index",
        "",
        "This index is generated primarily from `public.proposed_driver_occurrences` and supplemented by markdown-only fallback occurrences that have not yet been backfilled into the structured store.",
        "",
        "## Ranked normalized mechanism families",
    ]
    if not ranked_families:
        lines.append("- none")
    else:
        for family_slug, info in ranked_families:
            family = info['family']
            occurrences = info['occurrences']
            coverage = info['canon_coverage']
            candidate_labels = [label for label, _ in Counter(info['candidate_labels']).most_common()]
            case_count = len({o.case_key for o in occurrences if o.case_key})
            persona_count = len({o.persona for o in occurrences if o.persona})
            coverage_suffix = f", canon: {coverage.status}"
            if coverage.canonical_slug:
                coverage_suffix += f" -> {coverage.canonical_slug}"
            lines.append(
                f"- `{family.label}` (`{family_slug}`) "
                f"(occurrences: {len(occurrences)}, cases: {case_count}, personas: {persona_count}, raw_candidates: {len(set(info['candidate_slugs']))}{coverage_suffix})"
            )
            for label in candidate_labels[:8]:
                note_name = f"candidate-notes/{GENERATED_PREFIX}{slugify(label)}.md"
                lines.append(f"  - `{label}` -> `{note_name}`")
    lines.extend([
        "",
        "## Provisional unresolved family buckets",
    ])
    if not ranked_provisional:
        lines.append("- none")
    else:
        for family_slug, info in ranked_provisional:
            family = info['family']
            occurrences = info['occurrences']
            coverage = info['canon_coverage']
            candidate_labels = [label for label, _ in Counter(info['candidate_labels']).most_common()]
            case_count = len({o.case_key for o in occurrences if o.case_key})
            persona_count = len({o.persona for o in occurrences if o.persona})
            coverage_suffix = f", canon: {coverage.status}"
            if coverage.canonical_slug:
                coverage_suffix += f" -> {coverage.canonical_slug}"
            lines.append(
                f"- `{family.label}` (`{family_slug}`) "
                f"(occurrences: {len(occurrences)}, cases: {case_count}, personas: {persona_count}, raw_candidates: {len(set(info['candidate_slugs']))}{coverage_suffix})"
            )
            for label in candidate_labels[:5]:
                note_name = f"candidate-notes/{GENERATED_PREFIX}{slugify(label)}.md"
                lines.append(f"  - `{label}` -> `{note_name}`")
    lines.extend([
        "",
        "## Ranked raw candidates",
    ])
    if not ranked:
        lines.append("- none")
    else:
        for slug, occurrences in ranked:
            primary_label = Counter(o.label for o in occurrences).most_common(1)[0][0]
            note_name = f"candidate-notes/{GENERATED_PREFIX}{slug}.md"
            case_count = len({o.case_key for o in occurrences if o.case_key})
            persona_count = len({o.persona for o in occurrences if o.persona})
            family = choose_family(primary_label, [s for o in occurrences for s in o.suggestions], [d for o in occurrences for d in o.related_drivers])
            coverage = assess_canon_coverage(family, occurrences, driver_slugs)
            coverage_suffix = f", canon: {coverage.status}"
            if coverage.canonical_slug:
                coverage_suffix += f" -> {coverage.canonical_slug}"
            lines.append(
                f"- `{primary_label}` -> `{note_name}` "
                f"(family: `{family.slug}`, occurrences: {len(occurrences)}, cases: {case_count}, personas: {persona_count}{coverage_suffix})"
            )
    lines.append("")
    return "\n".join(lines)


def build_family_summary_rows(family_groups: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for family_slug, info in sorted(family_groups.items(), key=lambda item: (-len(item[1]['occurrences']), item[0])):
        occurrences = info['occurrences']
        rows.append(
            {
                'family_slug': family_slug,
                'family_label': info['family'].label,
                'canon_coverage_status': info['canon_coverage'].status,
                'canon_coverage_driver': info['canon_coverage'].canonical_slug,
                'occurrences': len(occurrences),
                'distinct_cases': len({o.case_key for o in occurrences if o.case_key}),
                'distinct_personas': len({o.persona for o in occurrences if o.persona}),
                'raw_candidate_count': len(set(info['candidate_slugs'])),
                'raw_candidate_labels': [label for label, _ in Counter(info['candidate_labels']).most_common()],
                'candidate_slugs': sorted(set(info['candidate_slugs'])),
            }
        )
    return rows



def build_candidate_summary_rows(grouped: dict[str, list[Occurrence]], driver_slugs: list[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for slug, occurrences in sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0])):
        primary_label = Counter(o.label for o in occurrences).most_common(1)[0][0]
        family = choose_family(primary_label, [s for o in occurrences for s in o.suggestions], [d for o in occurrences for d in o.related_drivers])
        coverage = assess_canon_coverage(family, occurrences, driver_slugs)
        rows.append(
            {
                'candidate_slug': slug,
                'candidate_label': primary_label,
                'candidate_note_path': f"candidate-notes/{GENERATED_PREFIX}{slug}.md",
                'normalized_family': family.slug,
                'canon_coverage_status': coverage.status,
                'canon_coverage_driver': coverage.canonical_slug,
                'occurrences': len(occurrences),
                'distinct_cases': len({o.case_key for o in occurrences if o.case_key}),
                'distinct_personas': len({o.persona for o in occurrences if o.persona}),
                'source_mix': dict(Counter(o.source for o in occurrences)),
                'case_keys': sorted({o.case_key for o in occurrences if o.case_key}),
                'personas': sorted({o.persona for o in occurrences if o.persona}),
                'related_drivers': sorted({driver for o in occurrences for driver in o.related_drivers}),
                'canonical_driver_suggestions': sorted({suggestion for o in occurrences for suggestion in o.suggestions}),
            }
        )
    return rows



def build_generated_index_payload(
    grouped: dict[str, list[Occurrence]],
    source_counts: dict[str, int],
    driver_slugs: list[str],
    family_groups: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    family_rows = build_family_summary_rows(family_groups)
    candidate_rows = build_candidate_summary_rows(grouped, driver_slugs)
    return {
        'type': 'proposed_driver_generated_index',
        'generated_at': NOW_UTC,
        'queue_root': str(QUEUE_DIR.relative_to(WORKSPACE_ROOT)),
        'source_counts': dict(source_counts),
        'summary': {
            'generated_candidate_count': len(grouped),
            'normalized_family_count': len(family_groups),
            'total_proposed_driver_occurrences': sum(len(v) for v in grouped.values()),
        },
        'families': family_rows,
        'candidates': candidate_rows,
    }



def sync_generated_files(grouped: dict[str, list[Occurrence]], source_counts: dict[str, int], driver_slugs: list[str], family_groups: dict[str, dict[str, Any]]) -> tuple[dict[str, int], dict[str, Any]]:
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    CANDIDATE_NOTES_DIR.mkdir(parents=True, exist_ok=True)
    FAMILY_REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    outcomes = Counter()
    expected_files = {INDEX_PATH.name, INDEX_JSON_PATH.name}
    expected_candidate_files: set[str] = set()

    index_content = render_index(grouped, source_counts, driver_slugs)
    if INDEX_PATH.exists() and INDEX_PATH.read_text() == index_content:
        outcomes["index_unchanged"] += 1
    else:
        INDEX_PATH.write_text(index_content)
        outcomes["index_written"] += 1

    index_payload = build_generated_index_payload(grouped, source_counts, driver_slugs, family_groups)
    index_json_content = json.dumps(index_payload, indent=2, sort_keys=False)
    if INDEX_JSON_PATH.exists() and INDEX_JSON_PATH.read_text() == index_json_content + "\n":
        outcomes["index_json_unchanged"] += 1
    else:
        INDEX_JSON_PATH.write_text(index_json_content + "\n")
        outcomes["index_json_written"] += 1

    for slug, occurrences in grouped.items():
        name = f"{GENERATED_PREFIX}{slug}.md"
        expected_candidate_files.add(name)
        path = CANDIDATE_NOTES_DIR / name
        content = render_candidate_note(slug, occurrences, driver_slugs)
        if path.exists() and path.read_text() == content:
            outcomes["candidate_unchanged"] += 1
        else:
            path.write_text(content)
            outcomes["candidate_written"] += 1

    for path in CANDIDATE_NOTES_DIR.glob(f"{GENERATED_PREFIX}*.md"):
        if path.name not in expected_candidate_files:
            path.unlink()
            outcomes["candidate_removed"] += 1

    # Clean up legacy top-level candidate files after moving to candidate-notes/.
    for path in QUEUE_DIR.glob(f"{GENERATED_PREFIX}*.md"):
        path.unlink()
        outcomes["legacy_candidate_removed"] += 1

    return dict(outcomes), index_payload


def main() -> int:
    args = parse_args()
    grouped, source_counts = collect_occurrences(args.psql, args.db_url)
    _, driver_slugs = load_catalog(DRIVER_ROOT, kind='driver')
    family_groups = build_family_groups(grouped, driver_slugs)
    outcomes, index_payload = sync_generated_files(grouped, source_counts, driver_slugs, family_groups)
    summary = {
        "status": "ok",
        "generated_candidate_count": len(grouped),
        "normalized_family_count": len(family_groups),
        "total_proposed_driver_occurrences": sum(len(v) for v in grouped.values()),
        "db_occurrence_count": source_counts.get("db_occurrence_count", 0),
        "markdown_fallback_occurrence_count": source_counts.get("markdown_fallback_occurrence_count", 0),
        "top_families": index_payload.get("families", [])[:10],
        "top_candidates": index_payload.get("candidates", [])[:10],
        "write_outcomes": outcomes,
    }
    if args.pretty:
        print(json.dumps(summary, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(summary, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
