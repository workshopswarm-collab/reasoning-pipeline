#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

MAX_PROSE_FALLBACK_CHARS = 700
MAX_SNIPPET_CHARS = 500
MAX_PERSONA_THESIS_CHARS = 220
MAX_PERSONA_REASON_CHARS = 140
MAX_EXPANDED_PERSONA_THESIS_CHARS = 320
MAX_EXPANDED_CHAIN_ITEM_CHARS = 180
MAX_EXPANDED_SNIPPET_CHARS = 900

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import WORKSPACE_ROOT, coerce_string, load_json, relative_to_workspace  # noqa: E402

CONTRACT_PATH = DECISION_MAKER_DIR / "planner" / "prompts" / "decision-maker-contract.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the prompt for the Decision-Maker agent")
    parser.add_argument("--decision-context-json", required=True)
    parser.add_argument("--selected-input-bundle-json", required=True)
    parser.add_argument("--targeted-verification-pack-json")
    parser.add_argument("--out")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def default_prompt_path(context_path: Path, case_key: str, dispatch_id: str) -> Path:
    stem = dispatch_id or case_key or context_path.stem
    return context_path.with_name(f"decision-prompt-{stem}.md")


def trim_text(value: str, max_chars: int) -> str:
    text = coerce_string(value).strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + " …"


def compact_string_list(values: list[object], *, max_items: int = 1, max_chars: int = MAX_PERSONA_REASON_CHARS) -> list[str]:
    out: list[str] = []
    for item in values[:max_items]:
        text = trim_text(coerce_string(item), max_chars)
        if text:
            out.append(text)
    return out


def short_source_label(path_str: str) -> str:
    text = coerce_string(path_str)
    if not text:
        return ""
    try:
        p = Path(text)
        if p.name:
            parent = p.parent.name
            return f"{parent}/{p.name}" if parent else p.name
    except Exception:
        pass
    return text


def compact_persona(item: dict[str, object]) -> dict[str, object]:
    payload = {
        "persona": coerce_string(item.get("persona")),
        "p": item.get("own_probability"),
        "w": coerce_string(item.get("recommended_weight")),
        "thesis": trim_text(coerce_string(item.get("main_thesis")), MAX_PERSONA_THESIS_CHARS),
        "support": compact_string_list(list(item.get("strongest_supports") or []), max_items=1),
        "disconfirm": compact_string_list(list(item.get("strongest_disconfirmers") or []), max_items=1),
        "ambiguity": compact_string_list(list(item.get("unresolved_ambiguities") or []), max_items=1),
        "change": trim_text(coerce_string(item.get("what_would_change_view")), MAX_PERSONA_REASON_CHARS),
    }
    return {k: v for k, v in payload.items() if v not in ("", None, [])}


def compact_snippet(item: dict[str, object]) -> dict[str, str]:
    payload = {
        "src": short_source_label(coerce_string(item.get("path"))),
        "text": trim_text(coerce_string(item.get("snippet")), MAX_SNIPPET_CHARS),
    }
    return {k: v for k, v in payload.items() if v not in ("", None)}


def compact_structured_handoff(structured: dict[str, object]) -> dict[str, object]:
    fields = [
        "edge_quality",
        "edge_independent_verification_quality",
        "compressed_toward_market_due_to_verification",
        "contract_ambiguity_level",
        "contract_ambiguity_reason",
        "verification_gap_summary",
        "best_countercase_summary",
        "main_reason_for_disagreement",
        "resolution_mechanics_summary",
        "disagreement_intensity",
        "freshness_sensitive",
        "freshness_driver",
        "blockers_require_new_research",
        "disagreement_type",
    ]
    payload: dict[str, object] = {}
    for field in fields:
        value = structured.get(field)
        text = coerce_string(value)
        if text:
            payload[field] = trim_text(text, 220)
    verified_points = compact_string_list(list(structured.get("independently_verified_points") or []), max_items=3, max_chars=140)
    blockers = compact_string_list(list(structured.get("decision_blockers") or []), max_items=2, max_chars=140)
    if verified_points:
        payload["independently_verified_points"] = verified_points
    if blockers:
        payload["decision_blockers"] = blockers
    return payload


def persona_rank(item: dict[str, object]) -> tuple[int, float, int]:
    weight_rank = {"high": 0, "medium": 1, "low": 2}.get(coerce_string(item.get("recommended_weight")), 3)
    probability = item.get("own_probability")
    try:
        prob_score = -abs(float(probability) - 0.5)
    except Exception:
        prob_score = 0.0
    ambiguity_score = len(list(item.get("unresolved_ambiguities") or [])) + len(list(item.get("strongest_disconfirmers") or []))
    return (weight_rank, prob_score, -ambiguity_score)


def build_expanded_persona_fallback(item: dict[str, object]) -> dict[str, object]:
    payload = {
        "persona": coerce_string(item.get("persona")),
        "p": item.get("own_probability"),
        "w": coerce_string(item.get("recommended_weight")),
        "thesis": trim_text(coerce_string(item.get("main_thesis")), MAX_EXPANDED_PERSONA_THESIS_CHARS),
        "logical_chain": compact_string_list(list(item.get("main_logical_chain") or []), max_items=3, max_chars=MAX_EXPANDED_CHAIN_ITEM_CHARS),
        "supports": compact_string_list(list(item.get("strongest_supports") or []), max_items=2, max_chars=MAX_EXPANDED_CHAIN_ITEM_CHARS),
        "disconfirmers": compact_string_list(list(item.get("strongest_disconfirmers") or []), max_items=2, max_chars=MAX_EXPANDED_CHAIN_ITEM_CHARS),
        "ambiguities": compact_string_list(list(item.get("unresolved_ambiguities") or []), max_items=2, max_chars=MAX_EXPANDED_CHAIN_ITEM_CHARS),
        "change": trim_text(coerce_string(item.get("what_would_change_view")), MAX_EXPANDED_CHAIN_ITEM_CHARS),
    }
    return {k: v for k, v in payload.items() if v not in ("", None, [])}


def build_expanded_snippet_fallback(item: dict[str, object]) -> dict[str, str]:
    payload = {
        "src": short_source_label(coerce_string(item.get("path"))),
        "text": trim_text(coerce_string(item.get("snippet")), MAX_EXPANDED_SNIPPET_CHARS),
    }
    return {k: v for k, v in payload.items() if v not in ("", None)}


def should_include_expanded_fallback(selected_bundle: dict[str, object]) -> bool:
    if coerce_string(selected_bundle.get("verification_mode")) == "targeted_escalation":
        return True
    structured = selected_bundle.get("structured_handoff_primary") if isinstance(selected_bundle.get("structured_handoff_primary"), dict) else {}
    ambiguity = coerce_string(structured.get("contract_ambiguity_level"))
    blockers = list(structured.get("decision_blockers") or [])
    if ambiguity in {"moderate", "major"}:
        return True
    if blockers:
        return True
    return False


def main() -> None:
    args = parse_args()
    context_path = Path(args.decision_context_json)
    if not context_path.is_absolute():
        context_path = WORKSPACE_ROOT / context_path
    context = load_json(context_path)
    bundle_path = Path(args.selected_input_bundle_json)
    if not bundle_path.is_absolute():
        bundle_path = WORKSPACE_ROOT / bundle_path
    selected_bundle = load_json(bundle_path)
    targeted_pack = {}
    targeted_pack_path = None
    if args.targeted_verification_pack_json:
        targeted_pack_path = Path(args.targeted_verification_pack_json)
        if not targeted_pack_path.is_absolute():
            targeted_pack_path = WORKSPACE_ROOT / targeted_pack_path
        targeted_pack = load_json(targeted_pack_path)
    verification_enforcement = selected_bundle.get("verification_enforcement") or {}
    verification_budget = selected_bundle.get("verification_budget") or {}
    verification_mode = coerce_string(selected_bundle.get("verification_mode"))
    case_key = coerce_string(context.get("case_key"))
    dispatch_id = coerce_string(context.get("dispatch_id"))
    question = coerce_string(context.get("question"))
    market = context.get("market") or {}
    contract = CONTRACT_PATH.read_text()

    out_path = Path(args.out) if args.out else default_prompt_path(context_path, case_key, dispatch_id)
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    core_case = dict(selected_bundle.get("core_case") or {})
    for key in ["question", "market_title", "relation_to_market", "follow_up_needed"]:
        if not coerce_string(core_case.get(key)):
            core_case.pop(key, None)
    core_case.pop("market_quote_timestamp", None)

    prose_fallback = selected_bundle.get("prose_fallback") or {}
    compact_prose_fallback = {}
    if bool(prose_fallback.get("included", False)):
        compact_prose_fallback = {
            "included": True,
            "text": trim_text(coerce_string(prose_fallback.get("decision_handoff_excerpt")), MAX_PROSE_FALLBACK_CHARS),
        }

    prompt_selected_bundle = {
        "verification_mode": verification_mode,
        "verification_triggers": list(selected_bundle.get("verification_triggers") or []),
        "core_case": core_case,
        "structured_handoff_primary": compact_structured_handoff(selected_bundle.get("structured_handoff_primary") or {}),
        "structured_handoff_policy": {
            "structured_handoff_is_primary_starting_point": True,
            "prose_is_fallback_only": True,
        },
        "prose_fallback": compact_prose_fallback,
        "selected_persona_sidecars": [
            compact_persona(item)
            for item in (selected_bundle.get("selected_persona_sidecars") or []) if isinstance(item, dict)
        ],
        "selected_assumption_snippets": [
            compact_snippet(item)
            for item in (selected_bundle.get("selected_assumption_snippets") or []) if isinstance(item, dict)
        ],
        "selected_evidence_snippets": [
            compact_snippet(item)
            for item in (selected_bundle.get("selected_evidence_snippets") or []) if isinstance(item, dict)
        ],
        "selected_supporting_note_snippets": [
            compact_snippet(item)
            for item in (selected_bundle.get("selected_supporting_note_snippets") or []) if isinstance(item, dict)
        ],
    }
    compact_selected_bundle = json.dumps(prompt_selected_bundle, ensure_ascii=False, separators=(",", ":"))

    expanded_reasoning_fallback = {}
    if should_include_expanded_fallback(selected_bundle):
        personas = [item for item in (selected_bundle.get("selected_persona_sidecars") or []) if isinstance(item, dict)]
        if personas:
            best_persona = sorted(personas, key=persona_rank)[0]
            expanded_reasoning_fallback["persona_deep_dive"] = build_expanded_persona_fallback(best_persona)
        snippet_candidates = []
        for key in ["selected_evidence_snippets", "selected_assumption_snippets", "selected_supporting_note_snippets"]:
            for item in (selected_bundle.get(key) or []):
                if isinstance(item, dict):
                    snippet_candidates.append(item)
        if snippet_candidates:
            expanded_reasoning_fallback["note_deep_dive"] = build_expanded_snippet_fallback(snippet_candidates[0])
    compact_targeted_pack = {}
    if targeted_pack:
        focus = targeted_pack.get("structured_handoff_focus") or {}
        compact_targeted_pack = {
            "verification_questions": list(targeted_pack.get("verification_questions") or [])[:4],
            "focus": {
                "contract_ambiguity_level": coerce_string(focus.get("contract_ambiguity_level")),
                "verification_gap_summary": trim_text(coerce_string(focus.get("verification_gap_summary")), 180),
                "best_countercase_summary": trim_text(coerce_string(focus.get("best_countercase_summary")), 180),
                "freshness_sensitive": coerce_string(focus.get("freshness_sensitive")),
                "freshness_driver": trim_text(coerce_string(focus.get("freshness_driver")), 180),
                "decision_blockers": compact_string_list(list(focus.get("decision_blockers") or []), max_items=2, max_chars=140),
            },
        }

    tool_policy_lines = [
        "Do not use tools for additional research, browsing, or file reads during this decision turn. The runtime inspects the session and will fail the run if tool use occurs.",
    ]
    verification_policy_lines = [
        "- The planner/runtime already selected your verification mode and compact evidence bundle programmatically.",
        "- Treat `structured_handoff_primary` as the main synthesis handoff interface.",
        "- Use `prose_fallback` only for additional context on those compact structured fields, not as the default starting point.",
        "- Treat synthesis and researcher material as advisory evidence to evaluate critically, not as a conclusion you are expected to ratify.",
        "- You may materially disagree with upstream synthesis when evidence quality, ambiguity, freshness, or actionability justify that disagreement.",
        "- Do not assume access to the whole case tree is required for a good decision.",
        "- If the compact bundle is insufficient for a responsible decision, express that with `needs_more_research`, `needs_market_update`, `watch_only`, or `forbidden` as appropriate.",
        "- Do not turn this stage into an unbounded second synthesis pass.",
    ]
    if verification_mode == "targeted_escalation" and verification_enforcement.get("agent_tool_use_allowed"):
        tool_policy_lines = [
            f"You may use only {', '.join(verification_enforcement.get('allowed_agent_tools') or []) or 'no tools'} in this turn.",
            f"Stay within: searches<={int(verification_budget.get('search_queries_allowed', 0) or 0)}, fetches<={int(verification_budget.get('source_fetches_allowed', 0) or 0)}, min_distinct_source_families={int(verification_budget.get('minimum_distinct_source_families', 0) or 0)} when feasible.",
            "Choose sources independently and prefer primary, official, and resolution-relevant sources.",
            "Do not count multiple pages from the same source family as real diversity.",
        ]
        verification_policy_lines.insert(6, "- In `targeted_escalation`, independent tool-enabled verification is allowed, but source choice remains your responsibility and budgets remain runtime-enforced.")
    else:
        verification_policy_lines.insert(6, "- Do not use tools for additional research or file inspection during this turn; the runtime will treat tool use as a policy violation.")
    if expanded_reasoning_fallback:
        verification_policy_lines.insert(7, "- If the compact bundle feels too compressed, use the bounded expanded fallback below before assuming broader case access is needed.")

    prompt = "\n".join([
        f"# Decision-Maker task | case `{case_key}`",
        "",
        "You are the separate `decision-maker` agent. Return the final decision packet JSON only.",
        "Do not wrap the JSON in markdown fences. Do not prepend explanation.",
        "The runtime will persist artifacts and post visible Telegram markers; you should focus on judgment quality and packet correctness.",
        "The runtime has already deterministically bounded your verification context. Use the compact selected bundle below rather than trying to reconstruct the whole case tree.",
        "Treat `structured_handoff_primary` as the main starting point for synthesis->decision transfer. Treat `prose_fallback` only as fallback context on those compact fields.",
        "Synthesis, researcher findings, sidecars, and handoff prose are advisory inputs only. They are not determinative of the final decision.",
        "Your job is to critically evaluate those upstream materials, decide how much weight they deserve, and form your own final judgment.",
        *tool_policy_lines,
        "",
        "## Case",
        f"- case_key: `{case_key}`",
        f"- dispatch_id: `{dispatch_id}`",
        f"- question: {question}",
        f"- market_title: {market.get('market_title', '')}",
        f"- market_reference_price: {market.get('market_reference_price', '')}",
        "",
        "## Contract",
        "",
        contract.rstrip(),
        "",
        "## Deterministic verification mode and bounded-input policy",
        "",
        *verification_policy_lines,
        "",
        "## Structured selected-input bundle for this run",
        "```json",
        compact_selected_bundle,
        "```",
        "",
        *([
            "## Targeted verification scaffold for this run",
            "```json",
            json.dumps(compact_targeted_pack, ensure_ascii=False, separators=(',', ':')),
            "```",
            "",
        ] if compact_targeted_pack else []),
        *([
            "## Bounded expanded reasoning fallback (use only if needed)",
            "```json",
            json.dumps(expanded_reasoning_fallback, ensure_ascii=False, separators=(',', ':')),
            "```",
            "",
        ] if expanded_reasoning_fallback else []),
        "## Final reminder",
        "Return one JSON object only. No markdown fences. No commentary before or after the JSON.",
        "",
    ]) + "\n"

    out_path.write_text(prompt)
    print(json.dumps({
        "ok": True,
        "decision_context_json": relative_to_workspace(context_path),
        "selected_input_bundle_json": relative_to_workspace(bundle_path),
        "targeted_verification_pack_json": relative_to_workspace(targeted_pack_path) if targeted_pack_path else "",
        "prompt_path": relative_to_workspace(out_path),
    }, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
