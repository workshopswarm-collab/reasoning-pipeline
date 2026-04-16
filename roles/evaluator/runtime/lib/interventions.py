from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .io import parse_frontmatter, read_json, read_text, split_markdown_sections
from .paths import INTERVENTIONS_ROOT, intervention_sidecar_path, to_repo_relative

ALLOWED_STATUSES = {"draft", "active", "paused", "retired", "rejected"}
ALLOWED_SURFACES = {"planner", "researcher_prompt", "synthesis", "decision", "refresh"}
ALLOWED_CHANGE_KINDS = {
    "prompt_guardrail",
    "verification_rule",
    "retrieval_rule",
    "routing_rule",
    "threshold_change",
    "weighting_rule",
}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (value or "").strip().lower()).strip("-")


def listify(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return []
        if stripped.startswith("[") and stripped.endswith("]"):
            inner = stripped[1:-1].strip()
            if not inner:
                return []
            return [item.strip().strip('"').strip("'") for item in inner.split(",") if item.strip()]
        return [stripped]
    return [str(value).strip()]


def first_heading(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return ""


def infer_status(note_path: Path, frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    explicit = str(sidecar.get("status") or frontmatter.get("intervention_status") or "").strip().lower()
    if explicit in ALLOWED_STATUSES:
        return explicit
    parts = note_path.parts
    for part in reversed(parts):
        lowered = part.strip().lower()
        if lowered in ALLOWED_STATUSES:
            return lowered
    return "draft"


def infer_intervention_key(note_path: Path, frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    raw = (
        sidecar.get("intervention_key")
        or frontmatter.get("intervention_key")
        or frontmatter.get("topic")
        or note_path.stem
    )
    key = slugify(str(raw))
    if key.startswith("intervention-"):
        key = key[len("intervention-") :]
    return key


def infer_label(note_text: str, frontmatter: dict[str, Any], sidecar: dict[str, Any], note_path: Path) -> str:
    label = (
        sidecar.get("intervention_label")
        or frontmatter.get("intervention_label")
        or frontmatter.get("topic")
        or first_heading(note_text)
        or note_path.stem.replace("-", " ").replace("intervention ", "").strip().title()
    )
    return str(label).strip()


def infer_application_surface(frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    surface = str(sidecar.get("application_surface") or frontmatter.get("application_surface") or "").strip()
    return surface if surface in ALLOWED_SURFACES else "researcher_prompt"


def infer_change_kind(frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    change_kind = str(sidecar.get("change_kind") or frontmatter.get("change_kind") or "").strip()
    return change_kind if change_kind in ALLOWED_CHANGE_KINDS else "verification_rule"


def infer_hypothesis(frontmatter: dict[str, Any], sidecar: dict[str, Any], sections: dict[str, str]) -> str:
    hypothesis = str(sidecar.get("hypothesis") or frontmatter.get("hypothesis") or "").strip()
    if hypothesis:
        return hypothesis
    section_text = sections.get("Proposed intervention or hold decision", "")
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            return stripped[2:].strip()
    return ""


def build_retrieval_tags(frontmatter: dict[str, Any], *, status: str, surface: str, change_kind: str) -> list[str]:
    tags = [slugify(tag) for tag in listify(frontmatter.get("tags"))]
    tags.extend(
        [
            slugify(f"status {status}"),
            slugify(f"surface {surface}"),
            slugify(f"change kind {change_kind}"),
            *(slugify(driver) for driver in listify(frontmatter.get("related_drivers"))),
            *(slugify(entity) for entity in listify(frontmatter.get("related_entities"))),
        ]
    )
    return sorted({tag for tag in tags if tag})


def intervention_note_paths(root: Path = INTERVENTIONS_ROOT) -> list[Path]:
    if not root.exists():
        return []
    out: list[Path] = []
    for status in sorted(ALLOWED_STATUSES):
        status_dir = root / status
        if not status_dir.exists():
            continue
        out.extend(sorted(path for path in status_dir.rglob("*.md") if path.is_file()))
    return out


def build_intervention_record(note_path: Path) -> dict[str, Any]:
    note_text = read_text(note_path)
    frontmatter = parse_frontmatter(note_text)
    sidecar_path = intervention_sidecar_path(note_path)
    sidecar = read_json(sidecar_path, default={}) or {}
    sections = split_markdown_sections(note_text)

    status = infer_status(note_path, frontmatter, sidecar)
    surface = infer_application_surface(frontmatter, sidecar)
    change_kind = infer_change_kind(frontmatter, sidecar)
    evidence_paths = sidecar.get("evidence_paths")
    if not isinstance(evidence_paths, list) or not evidence_paths:
        evidence_paths = listify(frontmatter.get("upstream_inputs"))

    activated_at = sidecar.get("activated_at") or frontmatter.get("activated_at") or ""
    ended_at = sidecar.get("ended_at") or frontmatter.get("ended_at") or ""

    record = {
        "intervention_key": infer_intervention_key(note_path, frontmatter, sidecar),
        "path": to_repo_relative(note_path),
        "intervention_label": infer_label(note_text, frontmatter, sidecar, note_path),
        "status": status,
        "application_surface": surface,
        "change_kind": change_kind,
        "target_selector": sidecar.get("target_selector") if isinstance(sidecar.get("target_selector"), dict) else {},
        "change_payload": sidecar.get("change_payload") if isinstance(sidecar.get("change_payload"), dict) else {},
        "hypothesis": infer_hypothesis(frontmatter, sidecar, sections),
        "evidence_paths": [str(path) for path in evidence_paths if str(path).strip()],
        "metric_definition": sidecar.get("metric_definition") if isinstance(sidecar.get("metric_definition"), dict) else {},
        "retrieval_tags": build_retrieval_tags(frontmatter, status=status, surface=surface, change_kind=change_kind),
        "note_frontmatter": frontmatter,
        "activated_at": str(activated_at or ""),
        "ended_at": str(ended_at or ""),
        "sidecar_path": to_repo_relative(sidecar_path) if sidecar_path.exists() else "",
    }
    return record
