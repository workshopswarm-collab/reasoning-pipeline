#!/usr/bin/env python3
from __future__ import annotations

"""Normalize research-artifact entity/driver linkage metadata.

Increment A/B behavior:
- canonical fields remain `entity`, `driver`, `related_entities`, `related_drivers`
- unresolved labels are moved into `proposed_entities` / `proposed_drivers`
- canonically resolvable proposal labels are promoted back into canonical related-linkage fields
- canonical values are normalized against the existing `20-entities/` and `30-drivers/` vocabularies
- the script rewrites artifact frontmatter in place and returns a compact JSON summary
- when asked, it also validates sibling assumption/evidence artifacts for the same persona

This intentionally does not create or mutate canonical entity/driver notes.
"""

import argparse
import difflib
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = BASE_DIR.parent
PIPELINE_DIR = RUNTIME_DIR.parent
WORKSPACE_ROOT = PIPELINE_DIR.parents[2]
ENTITY_ROOT = WORKSPACE_ROOT / "qualitative-db" / "20-entities"
DRIVER_ROOT = WORKSPACE_ROOT / "qualitative-db" / "30-drivers"

CANONICAL_ENTITY_LIST_FIELDS = ["related_entities"]
CANONICAL_DRIVER_LIST_FIELDS = ["related_drivers"]
PROPOSED_ENTITY_FIELD = "proposed_entities"
PROPOSED_DRIVER_FIELD = "proposed_drivers"
INSERT_AFTER_FIELD = "related_drivers"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize entity/driver linkage frontmatter in research artifacts")
    parser.add_argument("--artifact-path", action="append", required=True, help="Artifact path relative to workspace or absolute; may be repeated")
    parser.add_argument("--include-linked-artifacts", action="store_true", help="Also validate sibling assumption/evidence artifacts for the same persona when the path is a main finding")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def slugify(value: str) -> str:
    text = (value or "").strip().lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[\s_/]+", "-", text)
    text = re.sub(r"[^a-z0-9.-]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-.")
    return text


def parse_flow_list(text: str) -> list[str] | None:
    stripped = text.strip()
    if not (stripped.startswith("[") and stripped.endswith("]")):
        return None
    inner = stripped[1:-1].strip()
    if not inner:
        return []
    try:
        parsed = json.loads(stripped)
        if isinstance(parsed, list):
            return [str(item).strip() for item in parsed if str(item).strip()]
    except json.JSONDecodeError:
        pass
    parts = [part.strip().strip('"').strip("'") for part in inner.split(",")]
    return [part for part in parts if part]


def load_jsonish_scalar(value: str) -> Any:
    text = value.strip()
    if text == "":
        return ""
    flow_list = parse_flow_list(text)
    if flow_list is not None:
        return flow_list
    if text in {"{}"}:
        return json.loads(text)
    if text.startswith("{"):
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return text.strip().strip('"').strip("'")
    if text.lower() == "true":
        return True
    if text.lower() == "false":
        return False
    if re.fullmatch(r"-?\d+", text):
        return int(text)
    if re.fullmatch(r"-?\d+\.\d+", text):
        return float(text)
    return text.strip().strip('"').strip("'")


def parse_frontmatter(text: str) -> tuple[OrderedDict[str, Any], int] | tuple[None, None]:
    if not text.startswith("---\n"):
        return None, None
    lines = text.splitlines(keepends=True)
    if not lines or lines[0] != "---\n":
        return None, None
    data: OrderedDict[str, Any] = OrderedDict()
    i = 1
    while i < len(lines):
        raw = lines[i]
        stripped = raw.rstrip("\n")
        if stripped == "---":
            return data, sum(len(line) for line in lines[: i + 1])
        if not stripped.strip():
            i += 1
            continue
        match = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", stripped)
        if not match:
            i += 1
            continue
        key, remainder = match.group(1), match.group(2)
        if remainder == "":
            block_items: list[str] = []
            j = i + 1
            while j < len(lines):
                next_stripped = lines[j].rstrip("\n")
                if next_stripped == "---":
                    break
                if re.match(r"^\s{2,}-\s+", next_stripped):
                    block_items.append(re.sub(r"^\s{2,}-\s+", "", next_stripped))
                    j += 1
                    continue
                if next_stripped.strip() == "":
                    j += 1
                    continue
                if re.match(r"^[A-Za-z0-9_]+:\s*.*$", next_stripped):
                    break
                j += 1
            if block_items:
                data[key] = [load_jsonish_scalar(item) for item in block_items]
                i = j
                continue
            data[key] = ""
            i += 1
            continue
        data[key] = load_jsonish_scalar(remainder)
        i += 1
    return None, None


def dump_scalar(value: Any) -> str:
    if value is None or value == "":
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    text = str(value)
    if re.fullmatch(r"[A-Za-z0-9_./:-]+", text):
        return text
    return json.dumps(text, ensure_ascii=False)


def dump_frontmatter(data: OrderedDict[str, Any], body: str) -> str:
    lines = ["---\n"]
    for key, value in data.items():
        rendered = dump_scalar(value)
        if rendered == "":
            lines.append(f"{key}:\n")
        else:
            lines.append(f"{key}: {rendered}\n")
    lines.append("---\n")
    if body and not body.startswith("\n"):
        lines.append("\n")
    lines.append(body)
    return "".join(lines)


def listify(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        out: list[str] = []
        for item in value:
            out.extend(listify(item))
        return out
    if isinstance(value, str):
        parsed = parse_flow_list(value)
        if parsed is not None:
            return parsed
    return [str(value).strip()] if str(value).strip() else []


def dedupe_preserve(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        key = item.strip()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(key)
    return out


def ensure_field_order(data: OrderedDict[str, Any], new_key: str, after_key: str) -> OrderedDict[str, Any]:
    if new_key in data:
        return data
    out: OrderedDict[str, Any] = OrderedDict()
    inserted = False
    for key, value in data.items():
        out[key] = value
        if key == after_key:
            out[new_key] = []
            inserted = True
    if not inserted:
        out[new_key] = []
    return out


def load_catalog(root: Path, *, kind: str) -> tuple[dict[str, str], list[str]]:
    alias_to_slug: dict[str, str] = {}
    canonical_slugs: list[str] = []
    if not root.exists():
        return alias_to_slug, canonical_slugs
    for path in sorted(root.rglob("*.md")):
        if path.name == "README.md":
            continue
        slug = slugify(path.stem)
        if not slug:
            continue
        canonical_slugs.append(slug)
        aliases = {slug}
        text = path.read_text()
        frontmatter, _ = parse_frontmatter(text)
        if frontmatter:
            if kind == "entity":
                raw = frontmatter.get("entity")
                if isinstance(raw, str) and raw.strip():
                    aliases.add(slugify(raw))
            if kind == "driver":
                raw = frontmatter.get("driver")
                if isinstance(raw, str) and raw.strip():
                    aliases.add(slugify(raw))
            for alias in listify(frontmatter.get("aliases")):
                aliases.add(slugify(alias))
        for alias in aliases:
            alias_to_slug.setdefault(alias, slug)
    return alias_to_slug, canonical_slugs


def resolve_value(label: str, alias_map: dict[str, str], canonical_slugs: list[str]) -> tuple[str | None, list[str]]:
    cleaned = (label or "").strip()
    if not cleaned:
        return None, []
    normalized = slugify(cleaned)
    resolved = alias_map.get(normalized)
    if resolved:
        return resolved, []
    suggestions = difflib.get_close_matches(normalized, canonical_slugs, n=3, cutoff=0.72)
    return None, suggestions


def sibling_artifact_paths(path: Path) -> list[Path]:
    try:
        rel = path.relative_to(WORKSPACE_ROOT)
    except ValueError:
        return []
    parts = rel.parts
    if 'researcher-analyses' not in parts or 'personas' not in parts:
        return []
    if len(parts) < 2 or path.suffix != '.md':
        return []
    persona = path.stem
    analysis_dir = path.parent.parent
    candidates = [
        analysis_dir / 'assumptions' / f'{persona}.md',
        analysis_dir / 'evidence' / f'{persona}.md',
    ]
    return [candidate for candidate in candidates if candidate.exists()]


def infer_artifact_context(path: Path) -> dict[str, str]:
    try:
        rel = path.relative_to(WORKSPACE_ROOT)
    except ValueError:
        return {}
    parts = rel.parts
    context: dict[str, str] = {}
    if len(parts) >= 7 and parts[0] == 'qualitative-db' and parts[1] == '40-research' and parts[2] == 'cases':
        context['case_key'] = parts[3]
    if 'researcher-analyses' in parts:
        idx = parts.index('researcher-analyses')
        if len(parts) > idx + 2:
            context['analysis_date'] = parts[idx + 1]
            context['dispatch_id'] = parts[idx + 2]
        if len(parts) > idx + 4:
            context['artifact_group'] = parts[idx + 3]
            context['persona'] = Path(parts[idx + 4]).stem
    return context


def sanitize_metadata_field(value: Any) -> str:
    text = str(value or '').strip()
    if not text:
        return ''
    if text.startswith('question:'):
        text = text.split(':', 1)[1].strip()
    if text.startswith('topic:'):
        text = text.split(':', 1)[1].strip()
    return text.strip().strip('"').strip("'")


def reconcile_proposed_values(
    items: list[str],
    alias_map: dict[str, str],
    canonical_slugs: list[str],
    *,
    prefix: str,
    suggestions: dict[str, list[str]],
) -> tuple[list[str], list[str]]:
    promoted: list[str] = []
    unresolved: list[str] = []
    for item in items:
        resolved, hinted = resolve_value(item, alias_map, canonical_slugs)
        if resolved:
            promoted.append(resolved)
        else:
            unresolved.append(item)
            if hinted:
                suggestions[f"{prefix}:{item}"] = hinted
    return promoted, unresolved


def normalize_artifact(path: Path, entity_aliases: dict[str, str], entity_slugs: list[str], driver_aliases: dict[str, str], driver_slugs: list[str]) -> dict[str, Any]:
    original = path.read_text()
    frontmatter, body_start = parse_frontmatter(original)
    rel_path = str(path.relative_to(WORKSPACE_ROOT) if path.is_relative_to(WORKSPACE_ROOT) else path)
    if frontmatter is None or body_start is None:
        return {
            "path": rel_path,
            "status": "skipped_no_frontmatter",
            "changed": False,
            "missing_frontmatter": True,
            "had_frontmatter_repairs": False,
            "frontmatter_repair_count": 0,
        }

    data = OrderedDict(frontmatter)
    data = ensure_field_order(data, PROPOSED_ENTITY_FIELD, INSERT_AFTER_FIELD)
    data = ensure_field_order(data, PROPOSED_DRIVER_FIELD, PROPOSED_ENTITY_FIELD)

    existing_proposed_entities = listify(data.get(PROPOSED_ENTITY_FIELD))
    existing_proposed_drivers = listify(data.get(PROPOSED_DRIVER_FIELD))

    unresolved_entities: list[str] = []
    unresolved_drivers: list[str] = []
    suggestions: dict[str, list[str]] = {}
    repairs_applied: list[str] = []
    inferred = infer_artifact_context(path)

    promoted_proposed_entities, remaining_proposed_entities = reconcile_proposed_values(
        existing_proposed_entities,
        entity_aliases,
        entity_slugs,
        prefix="entity",
        suggestions=suggestions,
    )
    promoted_proposed_drivers, remaining_proposed_drivers = reconcile_proposed_values(
        existing_proposed_drivers,
        driver_aliases,
        driver_slugs,
        prefix="driver",
        suggestions=suggestions,
    )
    if promoted_proposed_entities:
        repairs_applied.append("proposed_entities_promoted_to_related_entities")
    if promoted_proposed_drivers:
        repairs_applied.append("proposed_drivers_promoted_to_related_drivers")

    # Light metadata sanity for fields we can infer safely from the artifact path.
    inferred_type_map = {
        'personas': 'agent_finding',
        'assumptions': 'assumption_note',
        'evidence': 'evidence_map',
    }
    expected_type = inferred_type_map.get(inferred.get('artifact_group', ''))
    for key in ['case_key', 'dispatch_id', 'analysis_date', 'persona']:
        expected = inferred.get(key, '')
        current = sanitize_metadata_field(data.get(key))
        if expected and current != expected:
            data[key] = expected
            repairs_applied.append(f'{key}_normalized_from_path')
    if expected_type:
        current_type = sanitize_metadata_field(data.get('type'))
        if current_type != expected_type:
            data['type'] = expected_type
            repairs_applied.append('type_normalized_from_path')

    raw_question = sanitize_metadata_field(data.get("question"))
    if raw_question != str(data.get("question") or "").strip():
        data["question"] = raw_question
        repairs_applied.append("question_sanitized")
    topic_value = sanitize_metadata_field(data.get("topic"))
    if topic_value:
        cleaned_topic = topic_value
        if cleaned_topic.startswith("topic:"):
            cleaned_topic = cleaned_topic.split(":", 1)[1].strip()
            repairs_applied.append("topic_prefix_removed")
        if cleaned_topic.startswith("case-") and "|" in cleaned_topic and raw_question:
            cleaned_topic = slugify(raw_question)
            repairs_applied.append("topic_runtime_title_replaced")
        elif '|' in cleaned_topic and raw_question:
            cleaned_topic = slugify(raw_question)
            repairs_applied.append("topic_pipe_title_replaced")
        elif cleaned_topic and cleaned_topic.startswith('will-'):
            cleaned_topic = slugify(cleaned_topic)
        elif cleaned_topic != topic_value and cleaned_topic:
            cleaned_topic = slugify(cleaned_topic)
        if cleaned_topic != topic_value:
            data["topic"] = cleaned_topic
            topic_value = cleaned_topic

    scalar_entity = sanitize_metadata_field(data.get("entity"))
    if scalar_entity.startswith("topic:") or (scalar_entity.startswith("case-") and '|' in scalar_entity) or scalar_entity == topic_value:
        data["entity"] = ""
        repairs_applied.append("entity_cleared_topic_like_value")
        scalar_entity = ""
    if scalar_entity:
        resolved, hinted = resolve_value(scalar_entity, entity_aliases, entity_slugs)
        if resolved:
            data["entity"] = resolved
        else:
            data["entity"] = ""
            unresolved_entities.append(scalar_entity)
            if hinted:
                suggestions[f"entity:{scalar_entity}"] = hinted
    else:
        data["entity"] = ""

    scalar_driver = sanitize_metadata_field(data.get("driver"))
    if (
        scalar_driver.startswith("date_created:")
        or scalar_driver.startswith("analysis_date:")
        or scalar_driver.startswith("topic:")
        or scalar_driver.startswith("case-")
        or scalar_driver == topic_value
        or scalar_driver == raw_question
        or '|' in scalar_driver
    ):
        data["driver"] = ""
        repairs_applied.append("driver_cleared_metadata_like_value")
        scalar_driver = ""
    if scalar_driver:
        resolved, hinted = resolve_value(scalar_driver, driver_aliases, driver_slugs)
        if resolved:
            data["driver"] = resolved
        else:
            data["driver"] = ""
            unresolved_drivers.append(scalar_driver)
            if hinted:
                suggestions[f"driver:{scalar_driver}"] = hinted
    else:
        data["driver"] = ""

    normalized_entities: list[str] = []
    for key in CANONICAL_ENTITY_LIST_FIELDS:
        bucket: list[str] = list(promoted_proposed_entities)
        for item in listify(data.get(key)):
            resolved, hinted = resolve_value(item, entity_aliases, entity_slugs)
            if resolved:
                bucket.append(resolved)
            else:
                unresolved_entities.append(item)
                if hinted:
                    suggestions[f"entity:{item}"] = hinted
        data[key] = dedupe_preserve(bucket)
        normalized_entities.extend(data[key])

    normalized_drivers: list[str] = []
    for key in CANONICAL_DRIVER_LIST_FIELDS:
        bucket: list[str] = list(promoted_proposed_drivers)
        for item in listify(data.get(key)):
            resolved, hinted = resolve_value(item, driver_aliases, driver_slugs)
            if resolved:
                bucket.append(resolved)
            else:
                unresolved_drivers.append(item)
                if hinted:
                    suggestions[f"driver:{item}"] = hinted
        data[key] = dedupe_preserve(bucket)
        normalized_drivers.extend(data[key])

    data[PROPOSED_ENTITY_FIELD] = dedupe_preserve(remaining_proposed_entities + unresolved_entities)
    data[PROPOSED_DRIVER_FIELD] = dedupe_preserve(remaining_proposed_drivers + unresolved_drivers)

    rewritten = dump_frontmatter(data, original[body_start:])
    changed = rewritten != original
    if changed:
        path.write_text(rewritten)

    return {
        "path": rel_path,
        "status": "ok",
        "changed": changed,
        "missing_frontmatter": False,
        "had_frontmatter_repairs": bool(repairs_applied),
        "frontmatter_repair_count": len(repairs_applied),
        "resolved_entity": data.get("entity") or None,
        "resolved_driver": data.get("driver") or None,
        "resolved_related_entities": data.get("related_entities") or [],
        "resolved_related_drivers": data.get("related_drivers") or [],
        "proposed_entities": data.get(PROPOSED_ENTITY_FIELD) or [],
        "proposed_drivers": data.get(PROPOSED_DRIVER_FIELD) or [],
        "suggestions": suggestions,
    }


def main() -> int:
    args = parse_args()
    entity_aliases, entity_slugs = load_catalog(ENTITY_ROOT, kind="entity")
    driver_aliases, driver_slugs = load_catalog(DRIVER_ROOT, kind="driver")

    artifacts: list[dict[str, Any]] = []
    had_unresolved = False
    artifacts_changed = 0

    try:
        expanded_paths: list[Path] = []
        seen: set[Path] = set()
        for raw_path in args.artifact_path:
            path = Path(raw_path)
            if not path.is_absolute():
                path = (WORKSPACE_ROOT / raw_path).resolve()
            candidates = [path]
            if args.include_linked_artifacts:
                candidates.extend(sibling_artifact_paths(path))
            for candidate in candidates:
                resolved = candidate.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                expanded_paths.append(resolved)

        for path in expanded_paths:
            if not path.exists():
                artifacts.append({"path": str(path), "status": "missing", "changed": False})
                continue
            result = normalize_artifact(path, entity_aliases, entity_slugs, driver_aliases, driver_slugs)
            artifacts.append(result)
            if result.get("changed"):
                artifacts_changed += 1
            if result.get("proposed_entities") or result.get("proposed_drivers"):
                had_unresolved = True
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    artifacts_with_frontmatter_repairs = sum(1 for artifact in artifacts if artifact.get("had_frontmatter_repairs"))
    frontmatter_repair_count = sum(int(artifact.get("frontmatter_repair_count") or 0) for artifact in artifacts)
    missing_frontmatter_count = sum(1 for artifact in artifacts if artifact.get("missing_frontmatter"))
    summary = {
        "status": "ok",
        "artifacts_checked": len(artifacts),
        "artifacts_changed": artifacts_changed,
        "had_unresolved": had_unresolved,
        "artifacts_with_frontmatter_repairs": artifacts_with_frontmatter_repairs,
        "frontmatter_repair_count": frontmatter_repair_count,
        "missing_frontmatter_count": missing_frontmatter_count,
        "unresolved_entities": sorted({item for artifact in artifacts for item in artifact.get("proposed_entities") or []}),
        "unresolved_drivers": sorted({item for artifact in artifacts for item in artifact.get("proposed_drivers") or []}),
        "artifacts": artifacts,
    }
    if args.pretty:
        print(json.dumps(summary, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(summary, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
