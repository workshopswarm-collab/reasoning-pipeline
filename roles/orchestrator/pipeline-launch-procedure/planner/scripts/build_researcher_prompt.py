#!/usr/bin/env python3
"""Build a persona-specific researcher spawn prompt for one case.

Reads:
- researcher_base_contract.md
- one persona prompt file

Combines them with case/market context into a single task string suitable for fixed-channel Discord handoff.
"""

import argparse
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR.parent / "prompts"
BASE_CONTRACT_PATH = PROMPTS_DIR / "researcher_base_contract.md"
PERSONA_FILES = {
    "base-rate": PROMPTS_DIR / "researcher_base-rate.md",
    "market-implied": PROMPTS_DIR / "researcher_market-implied.md",
    "variant-view": PROMPTS_DIR / "researcher_variant-view.md",
    "risk-manager": PROMPTS_DIR / "researcher_risk-manager.md",
    "catalyst-hunter": PROMPTS_DIR / "researcher_catalyst-hunter.md",
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


def build_prompt(payload: dict) -> str:
    agent_label = require(payload, "agent_label")
    if agent_label not in PERSONA_FILES:
        raise ValueError(f"unsupported agent_label: {agent_label}")

    case_id = require(payload, "case_id")
    case_key = require(payload, "case_key")
    market_id = require(payload, "market_id")
    title = require(payload, "title")

    base_contract = BASE_CONTRACT_PATH.read_text()
    persona_text = PERSONA_FILES[agent_label].read_text()

    description = payload.get("description", "")
    current_price = payload.get("current_price")
    closes_at = payload.get("closes_at")
    resolves_at = payload.get("resolves_at")
    external_market_id = payload.get("external_market_id")
    slug = payload.get("slug")
    metadata = payload.get("metadata") or {}
    url = metadata.get("url")
    workspace_note_path = payload.get("workspace_note_path")
    source_note_dir = payload.get("source_note_dir") or "qualitative-db/40-research/source-notes/by-market"
    source_note_prefix = payload.get("source_note_prefix") or f"{case_key}-{agent_label}"
    assumption_note_path = payload.get("assumption_note_path") or f"qualitative-db/40-research/assumption-notes/{case_key}-{agent_label}-assumptions.md"
    evidence_map_path = payload.get("evidence_map_path") or f"qualitative-db/40-research/evidence-maps/{case_key}-{agent_label}-evidence-map.md"

    prompt = f"""You are being dispatched as the `{agent_label}` researcher for one active market case in the prediction-market research pipeline.

Read and follow the two instruction documents below.

===== BEGIN BASE CONTRACT =====
{base_contract}
===== END BASE CONTRACT =====

===== BEGIN PERSONA PROMPT =====
{persona_text}
===== END PERSONA PROMPT =====

Now work on the following case.

## Case context
- case_id: {case_id}
- case_key: {case_key}
- market_id: {market_id}
- agent_label: {agent_label}
- external_market_id: {external_market_id}
- slug: {slug}
- title: {title}
- current_price: {current_price}
- closes_at: {closes_at}
- resolves_at: {resolves_at}
- primary_market_url: {url}
- primary_workspace_note_path: {workspace_note_path}
- source_note_directory: {source_note_dir}
- source_note_filename_prefix: {source_note_prefix}
- assumption_note_path: {assumption_note_path}
- evidence_map_path: {evidence_map_path}

## Market description
{description}

## Exact artifact path conventions
1. Your primary agent-finding must be written exactly to:
   - {workspace_note_path}
2. If you create source notes for this run, they must go only in:
   - {source_note_dir}
   and filenames must start with:
   - {source_note_prefix}
3. If you create an assumption note, write it exactly to:
   - {assumption_note_path}
4. If you create an evidence map, write it exactly to:
   - {evidence_map_path}
5. Do not create alternate folders for this case unless explicitly instructed.

## Required operating instructions
1. Read relevant background context from the vault before making a strong judgment.
2. Use internet access and available tools to research independently.
3. Preserve provenance generously in `qualitative-db/40-research/`.
4. Usually create multiple qualitative artifacts where warranted, not just one compressed memo.
5. Ensure there is one main agent-finding artifact for this run.
6. Explicitly compare your view to the current market-implied probability from `current_price`.
7. State whether you agree, roughly agree, or disagree with the market and why.
8. Do not rewrite canon during ordinary case work.
9. Preserve uncertainty and unresolved disagreement explicitly.

## Main deliverables
- provenance-rich qualitative artifacts in `qualitative-db/40-research/` using the exact artifact path rules above
- one main agent-finding for this run exactly at: {workspace_note_path}
- a clear probability view that can later be logged structurally against this case/run/market

## Important reminder
The market price is not just context; it is part of the object of analysis. You must explicitly reason about whether the market-implied probability is right, wrong, or incomplete.
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
