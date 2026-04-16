from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .io import read_json

DEFAULT_LMD_EXPERIMENT_ID = "researcher-lmd-v1"
DEFAULT_LMD_GENERATOR_VERSION = "lmd-generator-v0"
DEFAULT_LMD_POLICY_VERSION = "lmd-policy-v0"
DEFAULT_TREATMENT_RATIO = 0.15


def assignment_digest(*, experiment_id: str, case_key: str) -> str:
    seed = f"{experiment_id}|{case_key}".encode("utf-8")
    return hashlib.sha256(seed).hexdigest()


def assignment_fraction(digest: str) -> float:
    value = int(digest[:16], 16)
    return value / float(0xFFFFFFFFFFFFFFFF)


def choose_arm(*, experiment_id: str, case_key: str, treatment_ratio: float = DEFAULT_TREATMENT_RATIO) -> dict[str, Any]:
    ratio = max(0.0, min(1.0, float(treatment_ratio)))
    digest = assignment_digest(experiment_id=experiment_id, case_key=case_key)
    fraction = assignment_fraction(digest)
    arm = "treatment" if fraction < ratio else "control"
    return {
        "experiment_id": experiment_id,
        "assignment_hash": digest,
        "assignment_fraction": round(fraction, 8),
        "treatment_ratio": ratio,
        "arm": arm,
        "assignment_unit": "case_key",
    }


def candidate_id(candidate_type: str, item: dict[str, Any]) -> str:
    if candidate_type == "case_review":
        return f"case_review:{item.get('case_key') or item.get('review_path') or item.get('path') or 'unknown'}"
    if candidate_type == "intervention":
        return f"intervention:{item.get('intervention_key') or item.get('path') or 'unknown'}"
    if candidate_type == "aggregate_note":
        return f"aggregate_note:{item.get('path') or 'unknown'}"
    if candidate_type == "node":
        return f"node:{item.get('node_key') or item.get('candidate_id') or 'unknown'}"
    if candidate_type == "edge":
        return f"edge:{item.get('edge_key') or item.get('candidate_id') or 'unknown'}"
    return f"{candidate_type}:{item.get('path') or item.get('candidate_id') or 'unknown'}"


def extract_required_check_keys(bundle: dict[str, Any]) -> list[str]:
    out: list[str] = []
    for item in ((bundle.get("results") or {}).get("required_checks") or []):
        if isinstance(item, dict):
            key = str(item.get("check_key") or "").strip()
            if key:
                out.append(key)
        elif isinstance(item, str) and item.strip():
            out.append(item.strip())
    return list(dict.fromkeys(out))


def bundle_candidates(bundle: dict[str, Any]) -> list[dict[str, Any]]:
    results = bundle.get("results") or {}
    required_check_keys = extract_required_check_keys(bundle)
    out: list[dict[str, Any]] = []

    for idx, item in enumerate(results.get("case_reviews") or [], start=1):
        if not isinstance(item, dict):
            continue
        out.append({
            "candidate_id": candidate_id("case_review", item),
            "candidate_type": "case_review",
            "candidate_path": item.get("review_path") or item.get("path") or "",
            "rank_position": idx,
            "retrieval_score": item.get("retrieval_score"),
            "required_check_keys": required_check_keys,
            "notes": {
                "why_retrieved": item.get("why_retrieved"),
                "case_key": item.get("case_key"),
                "packet_path": item.get("packet_path"),
                "error_pattern": item.get("error_pattern"),
                "reusable_checks": item.get("reusable_checks") or [],
            },
        })

    for idx, item in enumerate(results.get("active_interventions") or [], start=1):
        if not isinstance(item, dict):
            continue
        item_required_checks = [str(x).strip() for x in (item.get("required_checks") or []) if str(x).strip()]
        out.append({
            "candidate_id": candidate_id("intervention", item),
            "candidate_type": "intervention",
            "candidate_path": item.get("path") or "",
            "rank_position": idx,
            "retrieval_score": item.get("retrieval_score"),
            "required_check_keys": list(dict.fromkeys(required_check_keys + item_required_checks)),
            "notes": {
                "why_retrieved": item.get("why_retrieved"),
                "intervention_key": item.get("intervention_key"),
                "application_surface": item.get("application_surface"),
                "change_kind": item.get("change_kind"),
            },
        })

    for idx, item in enumerate(results.get("aggregate_notes") or [], start=1):
        if not isinstance(item, dict):
            continue
        out.append({
            "candidate_id": candidate_id("aggregate_note", item),
            "candidate_type": "aggregate_note",
            "candidate_path": item.get("path") or "",
            "rank_position": idx,
            "retrieval_score": item.get("retrieval_score"),
            "required_check_keys": required_check_keys,
            "notes": {
                "why_retrieved": item.get("why_retrieved"),
            },
        })

    causal_context = bundle.get("causal_context") or {}
    matched_edges = [str(edge_key or "").strip() for edge_key in (causal_context.get("matched_edges") or []) if str(edge_key or "").strip()]
    covered_node_keys: set[str] = set()
    for edge_key in matched_edges:
        parts = edge_key.split("__")
        if len(parts) >= 3:
            covered_node_keys.update([parts[0], parts[2]])

    node_metadata_by_key: dict[str, dict[str, Any]] = {}
    for row in (causal_context.get("active_node_metadata") or []):
        if not isinstance(row, dict):
            continue
        node_key = str(row.get("node_key") or "").strip()
        if node_key:
            node_metadata_by_key[node_key] = row
    for idx, node_key in enumerate(causal_context.get("active_nodes") or [], start=1):
        key = str(node_key or "").strip()
        if not key or key in covered_node_keys:
            continue
        metadata = node_metadata_by_key.get(key) or {}
        lifecycle_stage = str(metadata.get("lifecycle_stage") or "").strip().lower()
        if lifecycle_stage != "trial":
            continue
        out.append({
            "candidate_id": f"node:{key}",
            "candidate_type": "node",
            "candidate_path": metadata.get("path") or "",
            "rank_position": idx,
            "retrieval_score": None,
            "required_check_keys": required_check_keys,
            "notes": {
                "node_key": key,
                "node_label": metadata.get("node_label"),
                "lifecycle_stage": metadata.get("lifecycle_stage"),
                "source_kind": metadata.get("source_kind"),
                "mechanism_family": metadata.get("mechanism_family"),
                "node_only_trial_disclosure": True,
            },
        })

    edge_metadata_by_key: dict[str, dict[str, Any]] = {}
    for row in (causal_context.get("matched_edge_metadata") or []):
        if not isinstance(row, dict):
            continue
        edge_key = str(row.get("edge_key") or "").strip()
        if edge_key:
            edge_metadata_by_key[edge_key] = row
    for idx, edge_key in enumerate(matched_edges, start=1):
        metadata = edge_metadata_by_key.get(edge_key) or {}
        out.append({
            "candidate_id": f"edge:{edge_key}",
            "candidate_type": "edge",
            "candidate_path": metadata.get("path") or "",
            "rank_position": idx,
            "retrieval_score": None,
            "required_check_keys": required_check_keys,
            "notes": {
                "edge_key": edge_key,
                "contested": edge_key in set(causal_context.get("contested_edges") or []),
                "lifecycle_stage": metadata.get("lifecycle_stage"),
                "source_kind": metadata.get("source_kind"),
                "mechanism_family": metadata.get("mechanism_family"),
            },
        })

    return out


def load_bundle(*, bundle_path: str = "", bundle_json: str = "") -> tuple[dict[str, Any], str, str]:
    raw_text = ""
    if bundle_json.strip():
        raw_text = bundle_json.strip()
        parsed = json.loads(raw_text)
        return parsed if isinstance(parsed, dict) else {}, "", raw_text
    if not bundle_path:
        return {}, "", raw_text
    path = Path(bundle_path)
    raw_text = path.read_text(encoding="utf-8")
    parsed = read_json(path, default={}) or {}
    return parsed if isinstance(parsed, dict) else {}, str(path), raw_text


def bundle_sha256(raw_text: str) -> str:
    if not raw_text:
        return ""
    return hashlib.sha256(raw_text.encode("utf-8")).hexdigest()
