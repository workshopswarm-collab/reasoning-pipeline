#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import WORKSPACE_ROOT, coerce_string, load_json, relative_to_workspace, write_json  # noqa: E402

MAX_PACK_CHARS = 6000
MAX_QUESTIONS = 4
MAX_PERSONAS = 2


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build deterministic targeted verification pack for Decision-Maker")
    parser.add_argument("--decision-context-json", required=True)
    parser.add_argument("--selected-input-bundle-json", required=True)
    parser.add_argument("--out")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def default_output_path(bundle_path: Path, dispatch_id: str) -> Path:
    return bundle_path.with_name(f"targeted-verification-pack-{dispatch_id or bundle_path.stem}.json")


def build_questions(structured: dict[str, Any]) -> list[str]:
    questions: list[str] = []
    if coerce_string(structured.get("freshness_sensitive")) == "yes":
        driver = coerce_string(structured.get("freshness_driver")) or "freshness-sensitive catalyst"
        questions.append(f"Does the latest available information materially change the decision, given: {driver}?")
    ambiguity = coerce_string(structured.get("contract_ambiguity_level"))
    if ambiguity in {"minor", "moderate", "major"}:
        reason = coerce_string(structured.get("contract_ambiguity_reason"))
        questions.append(f"How decision-relevant is the remaining contract/source-of-truth ambiguity: {reason}?")
    blockers = structured.get("decision_blockers") if isinstance(structured.get("decision_blockers"), list) else []
    if blockers:
        questions.append(f"Are the current blockers still material to final judgment: {blockers[0]}?")
    gap = coerce_string(structured.get("verification_gap_summary"))
    if gap:
        questions.append(f"Is the main verification gap still decision-material: {gap}?")
    countercase = coerce_string(structured.get("best_countercase_summary"))
    if countercase:
        questions.append(f"Does the strongest surviving countercase remain live enough to compress the edge further: {countercase}?")
    deduped: list[str] = []
    seen = set()
    for q in questions:
        if q in seen:
            continue
        seen.add(q)
        deduped.append(q)
    return deduped[:MAX_QUESTIONS]


def maybe_trim_pack(payload: dict[str, Any]) -> dict[str, Any]:
    text = json.dumps(payload, ensure_ascii=False)
    if len(text) <= MAX_PACK_CHARS:
        payload.setdefault("pack_budget", {})["actual_chars_after_trim"] = len(text)
        payload.setdefault("pack_budget", {})["approx_tokens_after_trim"] = int(len(text) / 4)
        payload.setdefault("pack_budget", {})["trim_applied"] = False
        return payload

    personas = payload.get("supporting_persona_summaries") or []
    if len(personas) > 1:
        payload["supporting_persona_summaries"] = personas[:1]
        text = json.dumps(payload, ensure_ascii=False)
    evidence = payload.get("selected_evidence_snippets") or []
    if len(text) > MAX_PACK_CHARS and evidence:
        payload["selected_evidence_snippets"] = evidence[:1]
        text = json.dumps(payload, ensure_ascii=False)
    support = payload.get("selected_supporting_note_snippets") or []
    if len(text) > MAX_PACK_CHARS and support:
        payload["selected_supporting_note_snippets"] = support[:1]
        text = json.dumps(payload, ensure_ascii=False)

    payload.setdefault("pack_budget", {})["actual_chars_after_trim"] = len(text)
    payload.setdefault("pack_budget", {})["approx_tokens_after_trim"] = int(len(text) / 4)
    payload.setdefault("pack_budget", {})["trim_applied"] = True
    return payload


def main() -> None:
    args = parse_args()
    context_path = Path(args.decision_context_json)
    if not context_path.is_absolute():
        context_path = WORKSPACE_ROOT / context_path
    bundle_path = Path(args.selected_input_bundle_json)
    if not bundle_path.is_absolute():
        bundle_path = WORKSPACE_ROOT / bundle_path

    context = load_json(context_path)
    bundle = load_json(bundle_path)
    dispatch_id = coerce_string(context.get("dispatch_id"))
    structured = bundle.get("structured_handoff_primary") if isinstance(bundle.get("structured_handoff_primary"), dict) else {}
    mode = coerce_string(bundle.get("verification_mode"))

    required = mode == "targeted_escalation"
    questions = build_questions(structured) if required else []

    payload = {
        "artifact_type": "targeted_verification_pack",
        "schema_version": "decision-targeted-verification-pack/v1",
        "case_key": coerce_string(context.get("case_key")),
        "dispatch_id": dispatch_id,
        "required": required,
        "verification_mode": mode,
        "pack_purpose": "Deterministic narrow follow-up pack for targeted escalation. It defines the crux questions and operational budgets, while source choice may remain model-driven within runtime-enforced tool guardrails.",
        "verification_questions": questions,
        "structured_handoff_focus": {
            "contract_ambiguity_level": coerce_string(structured.get("contract_ambiguity_level")),
            "contract_ambiguity_reason": coerce_string(structured.get("contract_ambiguity_reason")),
            "verification_gap_summary": coerce_string(structured.get("verification_gap_summary")),
            "best_countercase_summary": coerce_string(structured.get("best_countercase_summary")),
            "main_reason_for_disagreement": coerce_string(structured.get("main_reason_for_disagreement")),
            "resolution_mechanics_summary": coerce_string(structured.get("resolution_mechanics_summary")),
            "freshness_sensitive": coerce_string(structured.get("freshness_sensitive")),
            "freshness_driver": coerce_string(structured.get("freshness_driver")),
            "decision_blockers": list(structured.get("decision_blockers") or []),
            "disagreement_type": coerce_string(structured.get("disagreement_type")),
        },
        "supporting_persona_summaries": list((bundle.get("selected_persona_sidecars") or [])[:MAX_PERSONAS]),
        "selected_assumption_snippets": list(bundle.get("selected_assumption_snippets") or []),
        "selected_evidence_snippets": list(bundle.get("selected_evidence_snippets") or []),
        "selected_supporting_note_snippets": list(bundle.get("selected_supporting_note_snippets") or []),
        "pack_budget": {
            "max_chars": MAX_PACK_CHARS,
            "actual_chars_before_trim": 0,
            "actual_chars_after_trim": 0,
            "approx_tokens_before_trim": 0,
            "approx_tokens_after_trim": 0,
            "trim_applied": False,
        },
    }

    payload["pack_budget"]["actual_chars_before_trim"] = len(json.dumps(payload, ensure_ascii=False))
    payload["pack_budget"]["approx_tokens_before_trim"] = int(payload["pack_budget"]["actual_chars_before_trim"] / 4)
    payload = maybe_trim_pack(payload)

    out_path = Path(args.out) if args.out else default_output_path(bundle_path, dispatch_id)
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    write_json(out_path, payload, pretty=True)
    print(json.dumps({
        "ok": True,
        "targeted_verification_pack_path": relative_to_workspace(out_path),
        "required": required,
        "verification_mode": mode,
        "approx_tokens_after_trim": (payload.get("pack_budget") or {}).get("approx_tokens_after_trim", 0),
    }, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
