#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import (  # noqa: E402
    DISPATCH_MANIFEST_ROOT,
    RESEARCH_CASES_ROOT,
    WORKSPACE_ROOT,
    extract_first_nonempty_paragraph,
    load_json,
    normalize_probability,
    parse_frontmatter,
    relative_to_workspace,
    write_json,
)


EXPECTED_SUPPORTING_DIRS = ["assumptions", "evidence"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a dispatch-scoped synthesis bundle from researcher artifacts")
    parser.add_argument("--dispatch-id", required=True, help="Dispatch id such as dispatch-case-...")
    parser.add_argument("--case-key", help="Optional case key to narrow bundle lookup")
    parser.add_argument("--out", help="Optional output path for the bundle JSON")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def locate_dispatch_dir(dispatch_id: str, case_key: str | None) -> Path:
    if case_key:
        matches = sorted((RESEARCH_CASES_ROOT / case_key / "researcher-analyses").glob(f"*/{dispatch_id}"))
    else:
        matches = sorted(RESEARCH_CASES_ROOT.glob(f"*/researcher-analyses/*/{dispatch_id}"))
    if not matches:
        raise SystemExit(f"dispatch analysis directory not found for {dispatch_id}")
    if len(matches) > 1:
        raise SystemExit(f"multiple dispatch analysis directories found for {dispatch_id}; pass --case-key")
    return matches[0]


def load_markdown_artifact(path: Path) -> dict[str, Any]:
    text = path.read_text()
    frontmatter, body_start = parse_frontmatter(text)
    body = text[body_start:] if body_start else text
    return {
        "path": relative_to_workspace(path),
        "frontmatter": dict(frontmatter or {}),
        "body": body,
        "summary": extract_first_nonempty_paragraph(body),
    }


def expected_personas_from_manifest(manifest: dict[str, Any]) -> list[str]:
    personas: list[str] = []
    for run in manifest.get("runs", []):
        persona = str(run.get("persona") or "").strip()
        if persona and persona not in personas:
            personas.append(persona)
    return personas


def main() -> None:
    args = parse_args()
    dispatch_dir = locate_dispatch_dir(args.dispatch_id, args.case_key)
    case_dir = dispatch_dir.parents[2]
    case_key = case_dir.name
    analysis_date = dispatch_dir.parent.name
    persona_dir = dispatch_dir / "personas"
    if not persona_dir.exists():
        raise SystemExit(f"persona directory missing: {persona_dir}")

    manifest_path = DISPATCH_MANIFEST_ROOT / f"{args.dispatch_id}.json"
    manifest = load_json(manifest_path) if manifest_path.exists() else {}
    expected_personas = expected_personas_from_manifest(manifest)

    persona_files = sorted(persona_dir.glob("*.md"))
    persona_entries = []
    for path in persona_files:
        entry = load_markdown_artifact(path)
        entry["persona"] = path.stem
        persona_entries.append(entry)

    source_personas = [entry["persona"] for entry in persona_entries]
    missing_personas = [persona for persona in expected_personas if persona not in source_personas]

    supporting_entries = []
    supporting_paths: list[str] = []
    for dirname in EXPECTED_SUPPORTING_DIRS:
        root = dispatch_dir / dirname
        if not root.exists():
            continue
        for path in sorted(root.glob("*.md")):
            entry = load_markdown_artifact(path)
            entry["kind"] = dirname[:-1] if dirname.endswith("s") else dirname
            entry["persona"] = path.stem
            supporting_entries.append(entry)
            supporting_paths.append(entry["path"])

    manifest_market = manifest.get("market") or {}
    question = str(manifest_market.get("title") or manifest.get("question") or "").strip()
    market_implied_probability = normalize_probability(
        manifest_market.get("current_price") or manifest.get("market_implied_probability")
    )
    market_snapshot_time = str(manifest.get("created_at") or manifest.get("market_snapshot_time") or "").strip()
    if persona_entries:
        first_frontmatter = persona_entries[0]["frontmatter"]
        if not question:
            question = str(first_frontmatter.get("question") or "").strip()
        if market_implied_probability is None:
            market_implied_probability = normalize_probability(first_frontmatter.get("market_implied_probability"))
        if not market_snapshot_time:
            market_snapshot_time = str(first_frontmatter.get("market_snapshot_time") or "").strip()

    bundle = {
        "artifact_type": "synthesis_bundle",
        "case_key": case_key,
        "dispatch_id": args.dispatch_id,
        "analysis_date": analysis_date,
        "question": question,
        "market_implied_probability": market_implied_probability,
        "market_snapshot_time": market_snapshot_time,
        "case_dir": relative_to_workspace(case_dir),
        "dispatch_dir": relative_to_workspace(dispatch_dir),
        "persona_dir": relative_to_workspace(persona_dir),
        "manifest_path": relative_to_workspace(manifest_path) if manifest_path.exists() else "",
        "source_personas": source_personas,
        "missing_personas": missing_personas,
        "source_persona_count": len(source_personas),
        "missing_persona_count": len(missing_personas),
        "source_finding_paths": [entry["path"] for entry in persona_entries],
        "source_supporting_artifacts": supporting_paths,
        "supporting_artifact_count": len(supporting_paths),
        "upstream_inputs": [path for path in [relative_to_workspace(manifest_path)] if manifest_path.exists()] + [entry["path"] for entry in persona_entries],
        "downstream_uses": [],
        "synthesis_method": "dispatch_bundle_v1",
        "synthesis_status": "bundle_built",
        "persona_findings": persona_entries,
        "supporting_artifacts": supporting_entries,
        "manifest": manifest,
    }

    out_path = Path(args.out) if args.out else dispatch_dir / "synthesis-bundle.json"
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    write_json(out_path, bundle, pretty=args.pretty)

    output = {
        "ok": True,
        "bundle_path": relative_to_workspace(out_path),
        "case_key": case_key,
        "dispatch_id": args.dispatch_id,
        "analysis_date": analysis_date,
        "source_persona_count": len(source_personas),
        "missing_persona_count": len(missing_personas),
        "supporting_artifact_count": len(supporting_paths),
        "source_personas": source_personas,
        "missing_personas": missing_personas,
    }
    print(json.dumps(output, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
