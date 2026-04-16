from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .io import parse_frontmatter, read_json, read_text, strip_frontmatter
from .paths import (
    CAUSAL_EDGES_ROOT,
    CAUSAL_NODES_ROOT,
    causal_edge_sidecar_path,
    causal_node_sidecar_path,
    to_repo_relative,
)

ALLOWED_STATUSES = {"draft", "active", "paused", "hold", "retired", "archived"}
ALLOWED_NODE_TYPES = {
    "market_state",
    "external_event",
    "resolution_condition",
    "workflow_condition",
    "source_condition",
    "intervention_condition",
    "risk_state",
}
ALLOWED_EFFECT_SIGNS = {"increases", "decreases", "conditions"}
ALLOWED_CONFIDENCE_MODES = {"reviewed", "hypothesis", "empirical"}
ALLOWED_SOURCE_KINDS = {"seed", "manual", "proposal_auto", "merged", "unknown"}
ALLOWED_LIFECYCLE_STAGES = {"draft", "trial", "active", "hold", "retired", "archived"}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (value or "").strip().lower()).strip("-")


def normalize_key(value: str) -> str:
    lowered = (value or "").strip().lower()
    lowered = re.sub(r"\s+", "-", lowered)
    lowered = re.sub(r"[^a-z0-9_\-]+", "-", lowered)
    lowered = re.sub(r"-{2,}", "-", lowered)
    return lowered.strip("-")


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


def first_paragraph(text: str) -> str:
    lines: list[str] = []
    for raw in strip_frontmatter(text).splitlines():
        stripped = raw.strip()
        if not stripped:
            if lines:
                break
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("- "):
            if lines:
                break
            lines.append(stripped[2:].strip())
            continue
        lines.append(stripped)
    return " ".join(lines).strip()


def optional_text(*values: Any) -> str:
    for value in values:
        if value is None:
            continue
        text = str(value).strip()
        if text:
            return text
    return ""


def optional_float(*values: Any, default: float | None = None) -> float | None:
    for value in values:
        if value in (None, ""):
            continue
        try:
            return float(value)
        except Exception:
            continue
    return default


def infer_status(note_path: Path, frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    explicit = str(sidecar.get("status") or frontmatter.get("status") or "").strip().lower()
    if explicit in ALLOWED_STATUSES:
        return explicit
    parts = note_path.parts
    for part in reversed(parts):
        lowered = part.strip().lower()
        if lowered in ALLOWED_STATUSES:
            return lowered
    return "active"


def infer_node_key(note_path: Path, frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    raw = sidecar.get("node_key") or frontmatter.get("node_key") or note_path.stem
    return normalize_key(str(raw))


def infer_edge_key(note_path: Path, frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    raw = sidecar.get("edge_key") or frontmatter.get("edge_key") or note_path.stem
    return normalize_key(str(raw))


def infer_label(note_text: str, frontmatter: dict[str, Any], sidecar: dict[str, Any], note_path: Path, *, key_name: str) -> str:
    label = (
        sidecar.get("label")
        or sidecar.get(f"{key_name}_label")
        or frontmatter.get("label")
        or frontmatter.get(f"{key_name}_label")
        or first_heading(note_text)
        or note_path.stem.replace("-", " ").strip().title()
    )
    return str(label).strip()


def infer_description(note_text: str, frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    desc = str(sidecar.get("description") or frontmatter.get("description") or "").strip()
    if desc:
        return desc
    return first_paragraph(note_text)


def infer_node_type(frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    node_type = str(sidecar.get("node_type") or frontmatter.get("node_type") or "").strip()
    return node_type if node_type in ALLOWED_NODE_TYPES else "market_state"


def infer_effect_sign(frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    effect_sign = str(sidecar.get("effect_sign") or frontmatter.get("effect_sign") or "").strip()
    return effect_sign if effect_sign in ALLOWED_EFFECT_SIGNS else "increases"


def infer_confidence_mode(frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    mode = str(sidecar.get("confidence_mode") or frontmatter.get("confidence_mode") or "").strip()
    return mode if mode in ALLOWED_CONFIDENCE_MODES else "reviewed"


def infer_source_kind(note_text: str, frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    explicit = str(sidecar.get("source_kind") or frontmatter.get("source_kind") or "").strip().lower()
    if explicit in ALLOWED_SOURCE_KINDS:
        return explicit
    tags = {slugify(tag) for tag in listify(frontmatter.get("tags"))}
    if "seed" in tags or "seeded" in tags:
        return "seed"
    if "seeded as part of the initial reviewed v1 causal-map ontology" in note_text.lower():
        return "seed"
    return "manual"


def infer_lifecycle_stage(note_path: Path, frontmatter: dict[str, Any], sidecar: dict[str, Any]) -> str:
    explicit = str(sidecar.get("lifecycle_stage") or frontmatter.get("lifecycle_stage") or "").strip().lower()
    if explicit in ALLOWED_LIFECYCLE_STAGES:
        return explicit
    status = infer_status(note_path, frontmatter, sidecar)
    return {
        "draft": "draft",
        "active": "active",
        "paused": "hold",
        "hold": "hold",
        "retired": "retired",
        "archived": "archived",
    }.get(status, "draft")


def infer_mechanism_family(note_text: str, frontmatter: dict[str, Any], sidecar: dict[str, Any], key_hint: str) -> str:
    explicit = str(sidecar.get("mechanism_family") or frontmatter.get("mechanism_family") or "").strip()
    if explicit:
        return normalize_key(explicit)

    combined = " ".join(
        part for part in [
            key_hint,
            str(sidecar.get("label") or ""),
            str(frontmatter.get("label") or ""),
            str(sidecar.get("description") or ""),
            str(frontmatter.get("description") or ""),
            note_text,
            " ".join(listify(frontmatter.get("tags"))),
        ] if part
    ).lower()

    publication_tokens = {"publication", "reporting", "publication-window", "scheduled-publication", "report", "release"}
    workflow_pricing_tokens = {"fair-value", "discount", "pricing", "underconfidence", "resistance", "verification-caution"}
    source_resolution_tokens = {"settlement", "resolution", "source", "governing", "verification-state"}
    threshold_tokens = {"threshold", "touch", "intraperiod", "time-remaining", "path-volatility"}

    if any(token in combined for token in publication_tokens):
        return "publication_timing"
    if any(token in combined for token in workflow_pricing_tokens):
        return "workflow_pricing"
    if any(token in combined for token in source_resolution_tokens):
        return "source_resolution"
    if any(token in combined for token in threshold_tokens):
        return "threshold_touch"
    return "unassigned"


def infer_superseded_by_key(frontmatter: dict[str, Any], sidecar: dict[str, Any], *, key_name: str) -> str:
    raw = sidecar.get("superseded_by_key") or frontmatter.get("superseded_by_key") or ""
    text = str(raw).strip()
    return normalize_key(text) if text else ""


def normalize_evidence_rows(edge_record: dict[str, Any], sidecar: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    raw_rows = sidecar.get("evidence_rows")
    if isinstance(raw_rows, list):
        for item in raw_rows:
            if not isinstance(item, dict):
                continue
            support_direction = str(item.get("support_direction") or "supports").strip().lower()
            if support_direction not in {"supports", "weakens", "contests"}:
                support_direction = "supports"
            confidence_raw = item.get("confidence")
            confidence: float | None = None
            if confidence_raw not in (None, ""):
                try:
                    confidence = float(confidence_raw)
                except Exception:
                    confidence = None
            review_path = str(item.get("review_path") or "").strip()
            evidence_path = str(item.get("evidence_path") or review_path or "").strip()
            rows.append({
                "edge_key": edge_record["edge_key"],
                "case_key": str(item.get("case_key") or "").strip(),
                "review_path": review_path,
                "signal_kind": str(item.get("signal_kind") or "").strip(),
                "signal_key": str(item.get("signal_key") or "").strip(),
                "evidence_path": evidence_path,
                "support_direction": support_direction,
                "confidence": confidence,
                "notes": item.get("notes") if isinstance(item.get("notes"), dict) else {},
            })
    if rows:
        return rows
    for evidence_path in edge_record.get("evidence_paths") or []:
        rows.append({
            "edge_key": edge_record["edge_key"],
            "case_key": "",
            "review_path": evidence_path if evidence_path.endswith("review.md") else "",
            "signal_kind": "",
            "signal_key": "",
            "evidence_path": evidence_path,
            "support_direction": "supports",
            "confidence": None,
            "notes": {},
        })
    return rows


def node_note_paths(root: Path = CAUSAL_NODES_ROOT) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("*.md") if path.is_file() and path.name != "README.md")


def edge_note_paths(root: Path = CAUSAL_EDGES_ROOT) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("*.md") if path.is_file() and path.name != "README.md")


def build_node_record(note_path: Path) -> dict[str, Any]:
    note_text = read_text(note_path)
    frontmatter = parse_frontmatter(note_text)
    sidecar_path = causal_node_sidecar_path(note_path)
    sidecar = read_json(sidecar_path, default={}) or {}

    contexts = sidecar.get("contexts") if isinstance(sidecar.get("contexts"), dict) else {}
    linked_paths = sidecar.get("linked_paths") if isinstance(sidecar.get("linked_paths"), dict) else {}
    tags = sidecar.get("tags") if isinstance(sidecar.get("tags"), list) else None
    if tags is None:
        tags = listify(frontmatter.get("tags"))

    record = {
        "node_key": infer_node_key(note_path, frontmatter, sidecar),
        "path": to_repo_relative(note_path),
        "node_label": infer_label(note_text, frontmatter, sidecar, note_path, key_name="node"),
        "node_type": infer_node_type(frontmatter, sidecar),
        "status": infer_status(note_path, frontmatter, sidecar),
        "mechanism_family": infer_mechanism_family(note_text, frontmatter, sidecar, note_path.stem),
        "source_kind": infer_source_kind(note_text, frontmatter, sidecar),
        "lifecycle_stage": infer_lifecycle_stage(note_path, frontmatter, sidecar),
        "promotion_score": optional_float(sidecar.get("promotion_score"), frontmatter.get("promotion_score"), default=0.0),
        "description": infer_description(note_text, frontmatter, sidecar),
        "contexts": contexts,
        "tags": [str(tag).strip() for tag in tags if str(tag).strip()],
        "linked_paths": linked_paths,
        "note_frontmatter": frontmatter,
        "sidecar_path": to_repo_relative(sidecar_path) if sidecar_path.exists() else "",
        "last_seen_at": optional_text(sidecar.get("last_seen_at"), frontmatter.get("last_seen_at")),
        "last_matched_at": optional_text(sidecar.get("last_matched_at"), frontmatter.get("last_matched_at")),
        "last_injected_at": optional_text(sidecar.get("last_injected_at"), frontmatter.get("last_injected_at")),
        "last_helpful_at": optional_text(sidecar.get("last_helpful_at"), frontmatter.get("last_helpful_at")),
        "decay_score": optional_float(sidecar.get("decay_score"), frontmatter.get("decay_score"), default=0.0),
        "demotion_reason": optional_text(sidecar.get("demotion_reason"), frontmatter.get("demotion_reason")),
        "superseded_by_key": infer_superseded_by_key(frontmatter, sidecar, key_name="node"),
    }
    return record


def build_edge_record(note_path: Path) -> dict[str, Any]:
    note_text = read_text(note_path)
    frontmatter = parse_frontmatter(note_text)
    sidecar_path = causal_edge_sidecar_path(note_path)
    sidecar = read_json(sidecar_path, default={}) or {}

    contexts = sidecar.get("contexts") if isinstance(sidecar.get("contexts"), dict) else {}
    evidence_paths = sidecar.get("evidence_paths")
    if not isinstance(evidence_paths, list):
        evidence_paths = listify(frontmatter.get("evidence_paths"))

    linked_intervention_keys = sidecar.get("linked_intervention_keys")
    if not isinstance(linked_intervention_keys, list):
        linked_intervention_keys = listify(frontmatter.get("linked_intervention_keys"))

    record = {
        "edge_key": infer_edge_key(note_path, frontmatter, sidecar),
        "path": to_repo_relative(note_path),
        "edge_label": infer_label(note_text, frontmatter, sidecar, note_path, key_name="edge"),
        "source_node_key": normalize_key(str(sidecar.get("source_node_key") or frontmatter.get("source_node_key") or "")),
        "target_node_key": normalize_key(str(sidecar.get("target_node_key") or frontmatter.get("target_node_key") or "")),
        "effect_sign": infer_effect_sign(frontmatter, sidecar),
        "status": infer_status(note_path, frontmatter, sidecar),
        "mechanism_family": infer_mechanism_family(note_text, frontmatter, sidecar, note_path.stem),
        "source_kind": infer_source_kind(note_text, frontmatter, sidecar),
        "lifecycle_stage": infer_lifecycle_stage(note_path, frontmatter, sidecar),
        "confidence_mode": infer_confidence_mode(frontmatter, sidecar),
        "confidence_prior": sidecar.get("confidence_prior") if sidecar.get("confidence_prior") not in (None, "") else frontmatter.get("confidence_prior"),
        "promotion_score": optional_float(sidecar.get("promotion_score"), frontmatter.get("promotion_score"), default=0.0),
        "description": infer_description(note_text, frontmatter, sidecar),
        "contexts": contexts,
        "linked_intervention_keys": [slugify(str(key)) for key in linked_intervention_keys if str(key).strip()],
        "evidence_paths": [str(path).strip() for path in evidence_paths if str(path).strip()],
        "note_frontmatter": frontmatter,
        "sidecar_path": to_repo_relative(sidecar_path) if sidecar_path.exists() else "",
        "last_seen_at": optional_text(sidecar.get("last_seen_at"), frontmatter.get("last_seen_at")),
        "last_matched_at": optional_text(sidecar.get("last_matched_at"), frontmatter.get("last_matched_at")),
        "last_injected_at": optional_text(sidecar.get("last_injected_at"), frontmatter.get("last_injected_at")),
        "last_helpful_at": optional_text(sidecar.get("last_helpful_at"), frontmatter.get("last_helpful_at")),
        "decay_score": optional_float(sidecar.get("decay_score"), frontmatter.get("decay_score"), default=0.0),
        "demotion_reason": optional_text(sidecar.get("demotion_reason"), frontmatter.get("demotion_reason")),
        "superseded_by_key": infer_superseded_by_key(frontmatter, sidecar, key_name="edge"),
    }
    record["evidence_rows"] = normalize_evidence_rows(record, sidecar)
    return record
