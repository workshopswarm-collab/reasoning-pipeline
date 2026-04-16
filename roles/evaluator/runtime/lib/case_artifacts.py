from __future__ import annotations

from pathlib import Path
from typing import Any

from .io import extract_bullet_kv, parse_frontmatter, read_json, read_text, strip_frontmatter
from .paths import ORCHESTRATOR_ROOT, case_dir, to_repo_relative


def _resolve_repo_path(raw: str | None) -> Path | None:
    if not raw:
        return None
    p = Path(raw)
    if p.is_absolute():
        return p
    return (ORCHESTRATOR_ROOT / raw).resolve()


def load_case_markdown(case_key: str) -> dict[str, Any]:
    path = case_dir(case_key) / "case.md"
    text = read_text(path)
    body = strip_frontmatter(text)
    return {
        "path": path,
        "frontmatter": parse_frontmatter(text),
        "body": body,
        "bullet_map": extract_bullet_kv(body),
        "text": text,
    }


def load_swarm_current(case_key: str) -> dict[str, Any] | None:
    path = case_dir(case_key) / "researcher-swarm-current.md"
    if not path.exists():
        return None
    text = read_text(path)
    return {
        "path": path,
        "frontmatter": parse_frontmatter(text),
        "body": strip_frontmatter(text),
        "bullet_map": extract_bullet_kv(strip_frontmatter(text)),
        "text": text,
    }


def discover_dispatch_dir(case_key: str) -> Path | None:
    current = load_swarm_current(case_key)
    if current:
        raw = current["bullet_map"].get("dispatch_dir")
        resolved = _resolve_repo_path(raw)
        if resolved and resolved.exists():
            return resolved
    analyses_root = case_dir(case_key) / "researcher-analyses"
    if not analyses_root.exists():
        return None
    candidates = [p for p in analyses_root.glob("*/*") if p.is_dir()]
    if not candidates:
        return None
    return sorted(candidates)[-1]


def collect_persona_sidecars(dispatch_dir: Path | None) -> list[dict[str, Any]]:
    if dispatch_dir is None:
        return []
    personas_dir = dispatch_dir / "personas"
    if not personas_dir.exists():
        return []
    items: list[dict[str, Any]] = []
    for sidecar_path in sorted(personas_dir.glob("*.sidecar.json")):
        data = read_json(sidecar_path, default={}) or {}
        persona = data.get("persona") or sidecar_path.stem.replace(".sidecar", "")
        runtime = data.get("runtime_metadata") or {}
        items.append({
            "persona": persona,
            "research_run_id": runtime.get("research_run_id"),
            "finding_path": runtime.get("source_persona_finding_path") or to_repo_relative(sidecar_path.with_suffix("").with_suffix(".md")),
            "sidecar_path": to_repo_relative(sidecar_path),
            "own_probability": data.get("own_probability"),
            "recommended_weight": data.get("recommended_weight"),
            "key_assumptions": data.get("key_assumptions") or [],
            "strongest_supports": data.get("strongest_supports") or [],
            "strongest_disconfirmers": data.get("strongest_disconfirmers") or [],
            "timing_relevance": data.get("timing_relevance"),
            "source_quality_view": data.get("source_quality_view"),
        })
    return items


def collect_paths(base: Path) -> list[str]:
    if not base.exists():
        return []
    return [to_repo_relative(path) for path in sorted(base.glob("*.md")) if path.is_file()]


def discover_case_artifacts(case_key: str) -> dict[str, Any]:
    case_markdown = load_case_markdown(case_key)
    current = load_swarm_current(case_key)
    case_root = case_dir(case_key)
    dispatch_dir = discover_dispatch_dir(case_key)
    dispatch_rel = to_repo_relative(dispatch_dir) if dispatch_dir else None

    decision_json_path = case_root / "decision-maker" / "artifacts" / "decision-maker-packet.json"
    synthesis_runtime_path = case_root / "synthesizer-agent" / "syndicated-finding.runtime.json"
    timeline_path = case_root / "timeline.md"

    assumption_paths = collect_paths(dispatch_dir / "assumptions") if dispatch_dir else []
    evidence_paths = collect_paths(dispatch_dir / "evidence") if dispatch_dir else []
    summary_path = dispatch_dir / "summary.md" if dispatch_dir else None

    refresh_jsons = sorted(case_root.glob("decision-maker/refreshes/*/outputs/artifacts/decision-maker-packet.json"))

    return {
        "case_root": case_root,
        "case_markdown": case_markdown,
        "swarm_current": current,
        "dispatch_dir": dispatch_dir,
        "dispatch_dir_rel": dispatch_rel,
        "dispatch_id": dispatch_dir.name if dispatch_dir else None,
        "persona_runs": collect_persona_sidecars(dispatch_dir),
        "source_note_paths": collect_paths(case_root / "researcher-source-notes"),
        "assumption_paths": assumption_paths,
        "evidence_paths": evidence_paths,
        "summary_path": to_repo_relative(summary_path) if summary_path and summary_path.exists() else None,
        "decision_packet_json_path": decision_json_path,
        "decision_packet_json": read_json(decision_json_path, default={}) or {},
        "synthesis_runtime_path": synthesis_runtime_path,
        "synthesis_runtime": read_json(synthesis_runtime_path, default={}) or {},
        "timeline_path": timeline_path,
        "timeline_text": read_text(timeline_path) if timeline_path.exists() else "",
        "refresh_packet_paths": [to_repo_relative(p) for p in refresh_jsons],
    }
