#!/usr/bin/env python3
"""Build a compact persona-specific researcher prompt for one case.

The runtime prompt is intentionally concise to reduce drift and startup overhead.
It encodes the live operating brief directly and points to longer repo docs only
when the researcher truly needs extra formatting or governance detail.
"""

import argparse
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = BASE_DIR.parents[4]
PROMPTS_DIR = BASE_DIR.parent / "prompts"
BASE_CONTRACT_PATH = PROMPTS_DIR / "researcher_base_contract.md"
PERSONA_FILES = {
    "base-rate": PROMPTS_DIR / "researcher_base-rate.md",
    "market-implied": PROMPTS_DIR / "researcher_market-implied.md",
    "variant-view": PROMPTS_DIR / "researcher_variant-view.md",
    "risk-manager": PROMPTS_DIR / "researcher_risk-manager.md",
    "catalyst-hunter": PROMPTS_DIR / "researcher_catalyst-hunter.md",
}
PERSONA_BRIEFS = {
    "base-rate": [
        "Start from historical frequency, structural constraints, and outside-view priors.",
        "Be skeptical of vivid narratives unless they clearly overwhelm the prior.",
        "Ask what usually happens in analogous setups before focusing on why this case may differ.",
    ],
    "market-implied": [
        "Infer what the current price seems to be assuming and whether public evidence supports that assumption.",
        "Identify what the market may already know versus what seems under- or over-weighted.",
        "Explain whether the price looks efficient, early, stale, or overextended.",
    ],
    "variant-view": [
        "Look for the strongest credible alternative to the obvious consensus narrative.",
        "Surface neglected mechanisms, hidden conditionals, or asymmetric outcomes.",
        "Do not force contrarianism; only develop a variant view if it is genuinely supported.",
    ],
    "risk-manager": [
        "Focus on failure modes, disconfirming evidence, and what could break the current thesis.",
        "Highlight fragility, missing assumptions, and scenario tails that matter for resolution.",
        "State what evidence would most quickly invalidate the current working view.",
    ],
    "catalyst-hunter": [
        "Focus on upcoming catalysts, timelines, and concrete events that could move the market or resolution path.",
        "Distinguish soft narrative catalysts from events that genuinely change probabilities.",
        "Emphasize timing, sequencing, and what should be watched next.",
    ],
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

    # Ensure referenced docs exist even though the live prompt is now compact.
    if not BASE_CONTRACT_PATH.exists():
        raise FileNotFoundError(f"missing base contract: {BASE_CONTRACT_PATH}")
    if not PERSONA_FILES[agent_label].exists():
        raise FileNotFoundError(f"missing persona prompt: {PERSONA_FILES[agent_label]}")

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
    base_contract_rel = BASE_CONTRACT_PATH.relative_to(WORKSPACE_ROOT)
    persona_prompt_rel = PERSONA_FILES[agent_label].relative_to(WORKSPACE_ROOT)
    persona_brief = "\n".join(f"- {line}" for line in PERSONA_BRIEFS[agent_label])

    prompt = f"""You are the `{agent_label}` researcher for one active market case.

## Before serious work
Read only what you need, not the whole repo:
- shared contract: `{base_contract_rel}`
- persona brief: `{persona_prompt_rel}`
- vault protocol: `qualitative-db/00-system/roles-protocols/researcher-operating-protocol.md`
- read templates only if you need to create or substantially rewrite a supporting artifact

## Persona focus
{persona_brief}

## Case context
- case_id: {case_id}
- case_key: {case_key}
- market_id: {market_id}
- external_market_id: {external_market_id}
- slug: {slug}
- title: {title}
- current_price: {current_price}
- closes_at: {closes_at}
- resolves_at: {resolves_at}
- primary_market_url: {url}

## Required output
- write the main agent finding exactly to: `{workspace_note_path}`
- if you create source notes, keep them only under: `{source_note_dir}` with filenames starting: `{source_note_prefix}-`
- if you create an assumption note, use exactly: `{assumption_note_path}`
- if you create an evidence map, use exactly: `{evidence_map_path}`
- do not invent alternate folders for this case

## Operating rules
- treat this run as self-contained except for the current assignment, the vault, and the database
- do not read unrelated old case artifacts unless they are directly relevant stable context
- use internet research independently, prioritizing recent and credible sources
- preserve enough provenance in `qualitative-db/40-research/` to make the finding auditable
- compare explicitly against the market-implied probability from `current_price`
- state whether you agree, roughly agree, or disagree with the market and why
- preserve uncertainty rather than continuing to search indefinitely
- do not rewrite canon during routine case work

## Materiality stop rule
Stop gathering new evidence and start writing as soon as both conditions are true:
1. you can state a directional probability view with main reasons and caveats
2. the next likely source is unlikely to move your estimate by roughly 5 percentage points or change the main mechanism materially

If uncertainty remains after that threshold, record it in the finding instead of continuing to explore.

## Supporting artifacts
Supporting artifacts are optional. Create them only if they materially improve traceability or clarify a key assumption/disagreement. The main finding is mandatory.

## Market description
{description}
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
