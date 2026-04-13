#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
REPO_ROOT = SCRIPT_DIR.parents[3]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))
if str(REPO_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "scripts"))

from case_pipeline_status import update_case_pipeline_status_with_followups as update_case_pipeline_status  # noqa: E402
from common import (  # noqa: E402
    CASE_DECISION_PACKET_JSON_RELATIVE,
    WORKSPACE_ROOT,
    append_case_timeline_entry,
    case_decision_packet_json_path,
    case_decision_packet_markdown_path,
    case_decision_stage_status_path,
    coerce_string,
    load_json,
    normalize_probability,
    percent_points_from_prob_delta,
    relative_to_workspace,
    round_probability,
    utc_now_iso,
    write_json,
)
from status import append_stage_event, locked_status, set_overall_status  # noqa: E402
from validation import validate_decision_packet_payload  # noqa: E402

BUILD_CONTEXT = SCRIPT_DIR / "build_decision_context.py"
BUILD_VERIFICATION_MODE = DECISION_MAKER_DIR / "planner" / "scripts" / "decide_verification_mode.py"
SELECT_DECISION_INPUTS = DECISION_MAKER_DIR / "planner" / "scripts" / "select_decision_inputs.py"
BUILD_TARGETED_VERIFICATION_PACK = DECISION_MAKER_DIR / "planner" / "scripts" / "build_targeted_verification_pack.py"
BUILD_PROMPT = DECISION_MAKER_DIR / "planner" / "scripts" / "build_decision_prompt.py"
VALIDATE_PACKET = SCRIPT_DIR / "validate_decision_packet.py"
PERSIST_FORECAST_DECISION = SCRIPT_DIR / "persist_forecast_decision.py"
RENDER_PACKET = SCRIPT_DIR / "render_decision_packet.py"
BOOTSTRAP_DECISION_LANE = SCRIPT_DIR / "bootstrap_decision_telegram_lane.py"
OPENCLAW_SESSIONS_SEND = (
    WORKSPACE_ROOT
    / "roles"
    / "orchestrator"
    / "researchers-swarm-subagents"
    / "runtime"
    / "scripts"
    / "internal"
    / "openclaw_sessions_send.mjs"
)
DEFAULT_DECISION_AGENT_SESSION_KEY = "agent:decision-maker:main"


class DecisionMakerError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the real Decision-Maker flow using the separate decision-maker agent")
    parser.add_argument("--case-key")
    parser.add_argument("--dispatch-id")
    parser.add_argument("--decision-context-json")
    parser.add_argument("--prompt-path")
    parser.add_argument("--session-key", default=DEFAULT_DECISION_AGENT_SESSION_KEY)
    parser.add_argument("--agent-id")
    parser.add_argument("--market-price", type=float)
    parser.add_argument("--market-id")
    parser.add_argument("--market-title")
    parser.add_argument("--quote-timestamp")
    parser.add_argument("--valid-hours", type=int, default=24)
    parser.add_argument("--timeout-seconds", type=float, default=600.0)
    parser.add_argument("--result-json", help="Use an existing Decision-Maker JSON response instead of invoking the agent")
    parser.add_argument("--status-file")
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def run_command(cmd: list[str], *, cwd: Path = WORKSPACE_ROOT) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    if proc.returncode != 0:
        raise DecisionMakerError(f"command failed ({proc.returncode}): {' '.join(cmd)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")
    return proc


def parse_json_stdout(proc: subprocess.CompletedProcess[str]) -> dict[str, Any]:
    stdout = proc.stdout.strip()
    if not stdout:
        return {}
    return json.loads(stdout)


def build_context(args: argparse.Namespace) -> Path:
    if args.decision_context_json:
        path = Path(args.decision_context_json)
        return path if path.is_absolute() else WORKSPACE_ROOT / path
    cmd = [sys.executable, str(BUILD_CONTEXT)]
    if args.case_key:
        cmd.extend(["--case-key", args.case_key])
    if args.dispatch_id:
        cmd.extend(["--dispatch-id", args.dispatch_id])
    if args.market_price is not None:
        cmd.extend(["--market-price", str(args.market_price)])
    if args.market_id:
        cmd.extend(["--market-id", args.market_id])
    if args.market_title:
        cmd.extend(["--market-title", args.market_title])
    if args.quote_timestamp:
        cmd.extend(["--quote-timestamp", args.quote_timestamp])
    if args.pretty:
        cmd.append("--pretty")
    proc = run_command(cmd)
    payload = parse_json_stdout(proc)
    return WORKSPACE_ROOT / payload["decision_context_path"]


def build_selected_bundle(context_path: Path, args: argparse.Namespace) -> tuple[Path, Path]:
    mode_proc = run_command([
        sys.executable,
        str(BUILD_VERIFICATION_MODE),
        "--decision-context-json",
        str(context_path),
        *( ["--pretty"] if args.pretty else [] ),
    ])
    mode_payload = parse_json_stdout(mode_proc)
    mode_path = WORKSPACE_ROOT / mode_payload["verification_mode_path"]

    selected_proc = run_command([
        sys.executable,
        str(SELECT_DECISION_INPUTS),
        "--decision-context-json",
        str(context_path),
        "--verification-mode-json",
        str(mode_path),
        *( ["--pretty"] if args.pretty else [] ),
    ])
    selected_payload = parse_json_stdout(selected_proc)
    selected_path = WORKSPACE_ROOT / selected_payload["selected_input_bundle_path"]
    return mode_path, selected_path


def enforce_sidecar_selection_guardrail(context: dict[str, Any], selected_bundle: dict[str, Any]) -> None:
    guardrail = selected_bundle.get("sidecar_selection_guardrail") if isinstance(selected_bundle.get("sidecar_selection_guardrail"), dict) else {}
    if not bool(guardrail.get("violation")):
        return
    upstream = context.get("upstream") if isinstance(context.get("upstream"), dict) else {}
    raise DecisionMakerError(
        "Decision-Maker sidecar selection guardrail triggered: synthesis reported ready structured sidecars but the selected bundle resolved zero persona sidecars. "
        f"resolved_sidecar_bundle_path={coerce_string(guardrail.get('resolved_sidecar_bundle_path')) or coerce_string(upstream.get('sidecar_synthesis_bundle_path'))}; "
        f"ready_sidecar_count={upstream.get('ready_sidecar_count', 0)}; "
        f"sidecar_bundle_sidecar_count={upstream.get('sidecar_bundle_sidecar_count', 0)}"
    )


def build_targeted_verification_pack(context_path: Path, selected_input_bundle_path: Path, args: argparse.Namespace) -> Path | None:
    selected_bundle = load_json(selected_input_bundle_path)
    if coerce_string(selected_bundle.get("verification_mode")) != "targeted_escalation":
        return None
    proc = run_command([
        sys.executable,
        str(BUILD_TARGETED_VERIFICATION_PACK),
        "--decision-context-json",
        str(context_path),
        "--selected-input-bundle-json",
        str(selected_input_bundle_path),
        *( ["--pretty"] if args.pretty else [] ),
    ])
    payload = parse_json_stdout(proc)
    return WORKSPACE_ROOT / payload["targeted_verification_pack_path"]


def build_prompt(context_path: Path, selected_input_bundle_path: Path, targeted_verification_pack_path: Path | None, args: argparse.Namespace) -> Path:
    prompt_path = Path(args.prompt_path) if args.prompt_path else None
    cmd = [
        sys.executable,
        str(BUILD_PROMPT),
        "--decision-context-json",
        str(context_path),
        "--selected-input-bundle-json",
        str(selected_input_bundle_path),
    ]
    if targeted_verification_pack_path is not None:
        cmd.extend(["--targeted-verification-pack-json", str(targeted_verification_pack_path)])
    if prompt_path is not None:
        if not prompt_path.is_absolute():
            prompt_path = WORKSPACE_ROOT / prompt_path
        cmd.extend(["--out", str(prompt_path)])
    if args.pretty:
        cmd.append("--pretty")
    proc = run_command(cmd)
    payload = parse_json_stdout(proc)
    return WORKSPACE_ROOT / payload["prompt_path"]


def send_visible_telegram_message(*, chat_id: str, topic_id: str, message: str) -> dict[str, Any]:
    proc = subprocess.run(
        [
            "openclaw",
            "message",
            "send",
            "--channel",
            "telegram",
            "--target",
            str(chat_id),
            "--thread-id",
            str(topic_id),
            "--message",
            message,
            "--json",
        ],
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise DecisionMakerError(proc.stderr.strip() or proc.stdout.strip() or "telegram visible send failed")
    return parse_json_stdout(proc)


def maybe_send_visible_marker(status_path: Path, *, marker_key: str, stage: str, message: str) -> dict[str, Any] | None:
    with locked_status(status_path) as status:
        if status.get(marker_key):
            return None
        chat_id = coerce_string(status.get("decision_target_chat_id"))
        topic_id = coerce_string(status.get("decision_target_topic_id"))
        if not chat_id or not topic_id or not message:
            return None
    result = send_visible_telegram_message(chat_id=chat_id, topic_id=topic_id, message=message)
    with locked_status(status_path) as status:
        status[marker_key] = utc_now_iso()
        append_stage_event(status, stage=stage, state="visible_marker_sent", message=message)
    return result


def gateway_sessions_get(session_key: str, *, limit: int = 12) -> dict[str, Any]:
    proc = run_command([
        "openclaw",
        "gateway",
        "call",
        "sessions.get",
        "--params",
        json.dumps({"key": session_key, "limit": limit}),
        "--json",
    ])
    return json.loads(proc.stdout)


def latest_session_seq(session_key: str) -> int:
    payload = gateway_sessions_get(session_key, limit=1)
    messages = payload.get("messages") or []
    if not isinstance(messages, list) or not messages:
        return -1
    latest = messages[-1]
    seq = ((latest.get("__openclaw") or {}).get("seq")) if isinstance(latest, dict) else None
    return seq if isinstance(seq, int) else -1


def extract_text_from_message_content(content: list[Any]) -> str:
    parts: list[str] = []
    for part in content:
        if isinstance(part, str):
            parts.append(part)
        elif isinstance(part, dict):
            text = part.get("text") or part.get("content")
            if isinstance(text, str):
                parts.append(text)
    return "\n".join(part for part in parts if part.strip()).strip()


def extract_assistant_text_from_messages(messages: list[Any], *, min_seq: int | None = None) -> str | None:
    ordered = sorted(
        [msg for msg in messages if isinstance(msg, dict)],
        key=lambda msg: ((msg.get("__openclaw") or {}).get("seq") or -1),
    )
    for item in reversed(ordered):
        seq = ((item.get("__openclaw") or {}).get("seq"))
        if min_seq is not None and isinstance(seq, int) and seq <= min_seq:
            continue
        if item.get("role") != "assistant":
            continue
        text = extract_text_from_message_content(item.get("content") or [])
        if text:
            return text
        for key in ["text", "message", "responseText", "content"]:
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                return value
    return None


def parse_tool_call_args(part: dict[str, Any]) -> dict[str, Any]:
    for key in ["args", "arguments", "input", "params", "parameters", "json"]:
        value = part.get(key)
        if isinstance(value, dict):
            return value
        if isinstance(value, str) and value.strip():
            try:
                parsed = json.loads(value)
            except json.JSONDecodeError:
                continue
            if isinstance(parsed, dict):
                return parsed
    return {}


def infer_source_family(url: str) -> str:
    lowered = coerce_string(url).lower()
    if not lowered:
        return ""
    if "xtracker.polymarket.com" in lowered:
        return "xtracker"
    if "polymarket.com" in lowered:
        return "polymarket"
    if "truthsocial.com" in lowered or "trumpstruth.org" in lowered:
        return "truth_social"
    if lowered.startswith("http://") or lowered.startswith("https://"):
        host = lowered.split("//", 1)[-1].split("/", 1)[0]
        return host
    return ""


def collect_tool_usage(messages: list[Any], *, min_seq: int | None = None) -> dict[str, Any]:
    tool_names: list[str] = []
    search_queries: list[str] = []
    fetched_urls: list[str] = []
    ordered = sorted(
        [msg for msg in messages if isinstance(msg, dict)],
        key=lambda msg: ((msg.get("__openclaw") or {}).get("seq") or -1),
    )
    for item in ordered:
        seq = ((item.get("__openclaw") or {}).get("seq"))
        if min_seq is not None and isinstance(seq, int) and seq <= min_seq:
            continue
        role = item.get("role")
        if role == "toolResult":
            name = coerce_string(item.get("toolName")) or coerce_string(item.get("name"))
            if name:
                tool_names.append(name)
        if role != "assistant":
            continue
        named_tool_call_found = False
        for part in item.get("content") or []:
            if not isinstance(part, dict) or part.get("type") != "toolCall":
                continue
            name = coerce_string(part.get("toolName")) or coerce_string(part.get("name"))
            if name:
                named_tool_call_found = True
                tool_names.append(name)
            args = parse_tool_call_args(part)
            if name == "web_search":
                query = coerce_string(args.get("query"))
                if query:
                    search_queries.append(query)
            elif name == "web_fetch":
                url = coerce_string(args.get("url"))
                if url:
                    fetched_urls.append(url)
        if coerce_string(item.get("stopReason")) == "toolUse" and not named_tool_call_found:
            tool_names.append("<unknown_tool>")

    deduped_names: list[str] = []
    seen_names = set()
    for name in tool_names:
        if name in seen_names:
            continue
        seen_names.add(name)
        deduped_names.append(name)

    source_families: list[str] = []
    seen_families = set()
    for url in fetched_urls:
        family = infer_source_family(url)
        if not family or family in seen_families:
            continue
        seen_families.add(family)
        source_families.append(family)

    return {
        "tool_activity_detected": bool(deduped_names),
        "tool_names": deduped_names,
        "tool_names_sequence": tool_names,
        "search_queries": search_queries,
        "fetched_urls": fetched_urls,
        "search_query_count": len(search_queries),
        "source_fetch_count": len(fetched_urls),
        "source_families": source_families,
        "distinct_source_family_count": len(source_families),
    }


def detect_tool_activity(messages: list[Any], *, min_seq: int | None = None) -> dict[str, Any]:
    return collect_tool_usage(messages, min_seq=min_seq)


def wait_for_assistant_result(session_key: str, *, min_seq: int | None, timeout_seconds: float) -> dict[str, Any]:
    deadline = time.time() + max(timeout_seconds, 1.0)
    last_messages: list[Any] = []
    while time.time() < deadline:
        payload = gateway_sessions_get(session_key, limit=30)
        messages = payload.get("messages") or []
        last_messages = messages if isinstance(messages, list) else []
        text = extract_assistant_text_from_messages(last_messages, min_seq=min_seq)
        if text:
            tool_info = detect_tool_activity(last_messages, min_seq=min_seq)
            return {"text": text, **tool_info}
        time.sleep(2.0)
    raise DecisionMakerError(
        f"timed out waiting for assistant response via sessions.get for session {session_key}; last message count={len(last_messages)}"
    )


def extract_text_from_gateway_response(payload: Any) -> str:
    candidates: list[Any] = []
    if isinstance(payload, dict):
        for key in ["text", "message", "responseText", "content"]:
            if key in payload:
                candidates.append(payload[key])
        for key in ["assistantMessage", "response", "result", "data"]:
            if key in payload:
                candidates.append(payload[key])
        if isinstance(payload.get("messages"), list):
            candidates.extend(reversed(payload["messages"]))
    elif isinstance(payload, list):
        candidates.extend(reversed(payload))
    else:
        candidates.append(payload)

    while candidates:
        item = candidates.pop(0)
        if isinstance(item, str) and item.strip():
            return item
        if isinstance(item, dict):
            for key in ["text", "message", "responseText", "content"]:
                value = item.get(key)
                if isinstance(value, str) and value.strip():
                    return value
                if isinstance(value, list):
                    text = extract_text_from_message_content(value)
                    if text:
                        return text
            if isinstance(item.get("messages"), list):
                candidates.extend(reversed(item["messages"]))
        if isinstance(item, list):
            text = extract_text_from_message_content(item)
            if text:
                return text
    raise DecisionMakerError("could not extract assistant text from sessions.send response")


def extract_json_payload(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if not stripped:
        raise DecisionMakerError("empty decision-maker response text")
    try:
        obj = json.loads(stripped)
        if isinstance(obj, dict):
            return obj
    except json.JSONDecodeError:
        pass

    if "```json" in stripped:
        start = stripped.find("```json") + len("```json")
        end = stripped.find("```", start)
        if end != -1:
            candidate = stripped[start:end].strip()
            try:
                obj = json.loads(candidate)
                if isinstance(obj, dict):
                    return obj
            except json.JSONDecodeError:
                pass
    if "```" in stripped:
        start = stripped.find("```") + len("```")
        end = stripped.find("```", start)
        if end != -1:
            candidate = stripped[start:end].strip()
            try:
                obj = json.loads(candidate)
                if isinstance(obj, dict):
                    return obj
            except json.JSONDecodeError:
                pass

    decoder = json.JSONDecoder()
    for index, ch in enumerate(stripped):
        if ch != "{":
            continue
        try:
            obj, _ = decoder.raw_decode(stripped[index:])
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError:
            continue
    raise DecisionMakerError("could not parse JSON object from decision-maker response text")


def start_decision_maker_turn(prompt_path: Path, args: argparse.Namespace) -> dict[str, Any]:
    baseline_seq = latest_session_seq(args.session_key)
    prompt = prompt_path.read_text()
    payload = {
        "sessionKey": args.session_key,
        "message": prompt,
        "timeoutSeconds": args.timeout_seconds,
    }
    if args.agent_id:
        payload["agentId"] = args.agent_id
    proc = run_command([
        "node",
        str(OPENCLAW_SESSIONS_SEND),
        "--payload-json",
        json.dumps(payload),
    ])
    gateway_response = json.loads(proc.stdout)
    status = coerce_string(gateway_response.get("status")) if isinstance(gateway_response, dict) else ""
    accepted = bool(gateway_response) and status not in {"", "error", "failed"}
    return {
        "baseline_seq": baseline_seq,
        "gateway_response": gateway_response,
        "accepted": accepted,
        "status": status,
    }


def finish_decision_maker_turn(*, session_key: str, baseline_seq: int, timeout_seconds: float) -> dict[str, Any]:
    result = wait_for_assistant_result(session_key, min_seq=baseline_seq, timeout_seconds=timeout_seconds)
    text = result["text"]
    return {
        "packet": extract_json_payload(text),
        "tool_activity_detected": bool(result.get("tool_activity_detected")),
        "tool_names": list(result.get("tool_names") or []),
        "tool_names_sequence": list(result.get("tool_names_sequence") or []),
        "search_queries": list(result.get("search_queries") or []),
        "fetched_urls": list(result.get("fetched_urls") or []),
        "search_query_count": int(result.get("search_query_count") or 0),
        "source_fetch_count": int(result.get("source_fetch_count") or 0),
        "source_families": list(result.get("source_families") or []),
        "distinct_source_family_count": int(result.get("distinct_source_family_count") or 0),
    }


def invoke_decision_maker(prompt_path: Path, args: argparse.Namespace) -> dict[str, Any]:
    if args.result_json:
        path = Path(args.result_json)
        if not path.is_absolute():
            path = WORKSPACE_ROOT / path
        return {"packet": load_json(path), "tool_activity_detected": False, "tool_names": [], "accepted": True, "status": "offline_result_json"}

    started = start_decision_maker_turn(prompt_path, args)
    if not started.get("accepted"):
        raise DecisionMakerError(f"decision-maker handoff was not accepted: {started.get('gateway_response')}")
    finished = finish_decision_maker_turn(session_key=args.session_key, baseline_seq=int(started.get("baseline_seq", -1)), timeout_seconds=args.timeout_seconds)
    return {
        **finished,
        "accepted": True,
        "status": started.get("status", "accepted"),
        "baseline_seq": started.get("baseline_seq", -1),
        "gateway_response": started.get("gateway_response", {}),
    }


def default_band_shape(side: str) -> list[dict[str, Any]]:
    if side == "yes":
        targets = [1.0, 0.65, 0.35, 0.15, 0.0]
    elif side == "no":
        targets = [0.0, 0.15, 0.35, 0.65, 1.0]
    else:
        targets = [0.0, 0.0, 0.0, 0.0, 0.0]
    ranges = [
        ("max_enter", 0.0, 0.2),
        ("scaled_enter", 0.2, 0.4),
        ("hold", 0.4, 0.6),
        ("trim", 0.6, 0.8),
        ("exit", 0.8, 1.0),
    ]
    return [
        {
            "name": name,
            "min_p": min_p,
            "max_p": max_p,
            "target_exposure_fraction": target,
            "notes": "default fallback band",
        }
        for (name, min_p, max_p), target in zip(ranges, targets, strict=False)
    ]


def enforce_verification_tool_policy(selected_bundle: dict[str, Any], tool_usage: dict[str, Any], raw_packet: dict[str, Any] | None = None) -> None:
    enforcement = selected_bundle.get("verification_enforcement") if isinstance(selected_bundle.get("verification_enforcement"), dict) else {}
    budget = selected_bundle.get("verification_budget") if isinstance(selected_bundle.get("verification_budget"), dict) else {}
    tool_names = list(tool_usage.get("tool_names") or [])
    search_query_count = int(tool_usage.get("search_query_count") or 0)
    source_fetch_count = int(tool_usage.get("source_fetch_count") or 0)
    distinct_source_family_count = int(tool_usage.get("distinct_source_family_count") or 0)

    if tool_usage.get("tool_activity_detected") and not enforcement.get("agent_tool_use_allowed", False):
        raise DecisionMakerError("Decision-Maker used tools during a no-tools verification mode")

    allowed_tools = set(enforcement.get("allowed_agent_tools") or [])
    disallowed = [name for name in tool_names if name not in allowed_tools and name != "<unknown_tool>"]
    if disallowed:
        raise DecisionMakerError(f"Decision-Maker used disallowed tools: {', '.join(disallowed)}")
    if "<unknown_tool>" in tool_names:
        raise DecisionMakerError("Decision-Maker emitted tool activity that runtime could not classify safely")

    max_search_queries = int(budget.get("search_queries_allowed") or 0)
    max_fetches = int(budget.get("source_fetches_allowed") or 0)
    if search_query_count > max_search_queries:
        raise DecisionMakerError(f"Decision-Maker exceeded search-query budget ({search_query_count} > {max_search_queries})")
    if source_fetch_count > max_fetches:
        raise DecisionMakerError(f"Decision-Maker exceeded source-fetch budget ({source_fetch_count} > {max_fetches})")

    packet = raw_packet if isinstance(raw_packet, dict) else {}
    decision = packet.get("decision") if isinstance(packet.get("decision"), dict) else {}
    decision_readiness = coerce_string(decision.get("decision_readiness"))
    trade_authorization = coerce_string(decision.get("trade_authorization"))
    minimum_distinct_source_families = int(budget.get("minimum_distinct_source_families") or 0)
    if (
        enforcement.get("agent_tool_use_allowed", False)
        and decision_readiness == "ready"
        and trade_authorization == "authorized"
        and source_fetch_count > 0
        and distinct_source_family_count < minimum_distinct_source_families
    ):
        raise DecisionMakerError(
            f"Decision-Maker authorized action without meeting source-family diversity floor ({distinct_source_family_count} < {minimum_distinct_source_families})"
        )


def hydrate_packet_from_context(packet: dict[str, Any], context: dict[str, Any], selected_bundle: dict[str, Any], targeted_verification_pack: dict[str, Any] | None = None, *, valid_hours: int, tool_usage: dict[str, Any] | None = None) -> dict[str, Any]:
    now = datetime.now(timezone.utc)
    market = context.get("market") or {}
    upstream = context.get("upstream") or {}
    portfolio = context.get("portfolio_context") or {}
    defaults = context.get("recommended_runtime_defaults") or {}
    bundle_policy = selected_bundle.get("structured_handoff_policy") or {}
    bundle_enforcement = selected_bundle.get("verification_enforcement") or {}
    bundle_budget = selected_bundle.get("verification_budget") or {}
    targeted_pack = targeted_verification_pack or {}
    targeted_pack_required = bool(targeted_pack.get("required"))
    usage = tool_usage or {}
    tool_activity_detected = bool(usage.get("tool_activity_detected"))
    tool_names = list(usage.get("tool_names") or [])
    search_queries = list(usage.get("search_queries") or [])
    fetched_urls = list(usage.get("fetched_urls") or [])
    source_families = list(usage.get("source_families") or [])

    packet.setdefault("schema_version", "decision-packet/v1")
    packet.setdefault("generated_at", utc_now_iso())

    ctx = packet.setdefault("context", {})
    ctx["case_key"] = coerce_string(context.get("case_key"))
    ctx["dispatch_id"] = coerce_string(context.get("dispatch_id"))
    ctx["question"] = coerce_string(context.get("question"))
    ctx["market_id"] = coerce_string(ctx.get("market_id")) or coerce_string(market.get("market_id"))
    ctx["external_market_id"] = coerce_string(ctx.get("external_market_id")) or coerce_string(market.get("external_market_id"))
    ctx["market_slug"] = coerce_string(ctx.get("market_slug")) or coerce_string(market.get("market_slug"))
    ctx["platform"] = coerce_string(ctx.get("platform")) or coerce_string(market.get("platform")) or "polymarket"
    ctx["primary_market_url"] = coerce_string(ctx.get("primary_market_url")) or coerce_string(market.get("primary_market_url"))
    ctx["market_title"] = coerce_string(ctx.get("market_title")) or coerce_string(market.get("market_title"))
    ctx["source_decision_handoff_path"] = coerce_string(upstream.get("decision_handoff_path"))
    ctx["source_syndicated_finding_path"] = coerce_string(upstream.get("syndicated_finding_path"))
    ctx["source_light_refresh_brief_path"] = coerce_string(upstream.get("light_refresh_brief_path"))
    ctx["refresh_mode"] = coerce_string(upstream.get("light_refresh_mode"))
    ctx["decision_maker_agent"] = "decision-maker"
    ctx["canonical_markdown_path"] = "decision-maker-packet.md"
    ctx["canonical_json_path"] = CASE_DECISION_PACKET_JSON_RELATIVE

    decision = packet.setdefault("decision", {})
    valuation = packet.setdefault("valuation", {})
    execution = packet.setdefault("execution_semantics", {})
    risk = packet.setdefault("risk_controls", {})
    invalidation = packet.setdefault("invalidation", {})
    epistemic = packet.setdefault("epistemic_status", {})
    audit = packet.setdefault("audit", {})

    market_reference_price = normalize_probability(valuation.get("market_reference_price"))
    if market_reference_price is None:
        market_reference_price = normalize_probability(market.get("market_reference_price"))
    valuation["market_reference_price"] = round_probability(market_reference_price)

    fair_low = normalize_probability(valuation.get("fair_value_low"))
    fair_high = normalize_probability(valuation.get("fair_value_high"))
    fair_mid = normalize_probability(valuation.get("fair_value_mid"))
    if fair_mid is None and fair_low is not None and fair_high is not None:
        fair_mid = round_probability((fair_low + fair_high) / 2.0)
        valuation["fair_value_mid"] = fair_mid
    if fair_low is not None:
        valuation["fair_value_low"] = round_probability(fair_low)
    if fair_high is not None:
        valuation["fair_value_high"] = round_probability(fair_high)
    if fair_mid is not None:
        valuation["fair_value_mid"] = round_probability(fair_mid)
    if fair_mid is not None and market_reference_price is not None:
        valuation["edge_mid_vs_market_pct_points"] = percent_points_from_prob_delta(fair_mid - market_reference_price)

    valuation.setdefault("independent_verification_quality", coerce_string(upstream.get("edge_independent_verification_quality")) or "medium")
    compressed_default = coerce_string(upstream.get("compressed_toward_market_due_to_verification")) == "yes"
    valuation.setdefault("compressed_toward_market_applied", compressed_default)
    valuation.setdefault("compression_reason", "")

    execution["price_axis"] = "market_implied_true_prob"
    execution.setdefault("price_source", coerce_string(defaults.get("price_source")) or "market_snapshot_quote")
    execution.setdefault("rebalance_threshold_fraction", defaults.get("rebalance_threshold_fraction", 0.1))
    execution.setdefault("allow_auto_reversal", bool(defaults.get("allow_auto_reversal", False)))
    execution.setdefault("quote_staleness_seconds", int(defaults.get("quote_staleness_seconds", 300)))
    execution.setdefault("valid_until", (now + timedelta(hours=max(valid_hours, 1))).isoformat())

    risk.setdefault("max_position_size_pct_bankroll", 0.02)
    risk.setdefault("max_additional_exposure_pct_bankroll", 0.01)
    risk.setdefault("max_single_order_pct_bankroll", 0.005)
    risk.setdefault("slippage_tolerance_bps", 100)
    risk.setdefault("liquidity_min_depth", 0)
    risk.setdefault("correlation_bucket_limit_pct_bankroll", 0.05)
    risk.setdefault("confidence_level", valuation.get("independent_verification_quality", "medium"))
    risk.setdefault("portfolio_constraints", [])
    risk.setdefault("liquidity_caution", "medium")

    if not isinstance(packet.get("bands"), list) or not packet.get("bands"):
        packet["bands"] = default_band_shape(coerce_string(decision.get("side")))

    invalidation.setdefault("thesis_breakers", [])
    invalidation.setdefault("market_structure_breakers", [])
    invalidation.setdefault("time_breakers", [])
    invalidation.setdefault("reversal_conditions", [])

    epistemic.setdefault("key_uncertainties", [])
    epistemic.setdefault("reasons_to_pass", [])
    epistemic.setdefault("what_would_change_my_mind", [])

    audit.pop("portfolio_context_checked", None)
    audit.setdefault("market_baseline_respected", True)
    audit.setdefault("action_bias_check_passed", True)
    audit.setdefault("self_preservation_bias_check_passed", True)
    audit["structured_handoff_primary_used"] = bool(bundle_policy.get("structured_handoff_is_primary_starting_point", True))
    audit["prose_fallback_used"] = bool((selected_bundle.get("prose_fallback") or {}).get("included", False))
    audit["verification_mode_used"] = coerce_string(selected_bundle.get("verification_mode")) or "bounded_internal_audit"
    audit["additional_verification_performed"] = bool(targeted_pack_required or tool_activity_detected)
    notes_bits = []
    if targeted_pack_required:
        notes_bits.append("targeted_pack")
    if tool_activity_detected:
        notes_bits.append(
            f"tools:q={int(usage.get('search_query_count', 0) or 0)},f={int(usage.get('source_fetch_count', 0) or 0)},fam={int(usage.get('distinct_source_family_count', 0) or 0)}"
        )
    if tool_names:
        notes_bits.append(", ".join(tool_names))
    audit["additional_verification_notes"] = "; ".join(notes_bits)
    audit.setdefault("one_sentence_rationale", coerce_string(decision.get("primary_crux")) or "Decision rationale missing.")
    note_prefix = ""
    if not bundle_enforcement.get("agent_tool_use_allowed", False):
        note_prefix = "runtime_budget:no_tools"
    else:
        note_prefix = (
            f"runtime_budget:q<={int(bundle_budget.get('search_queries_allowed', 0) or 0)},"
            f"f<={int(bundle_budget.get('source_fetches_allowed', 0) or 0)},"
            f"fam>={int(bundle_budget.get('minimum_distinct_source_families', 0) or 0)}"
        )
    audit.setdefault("notes", note_prefix)

    return packet


def status_path_for(args: argparse.Namespace, case_key: str) -> Path:
    if args.status_file:
        path = Path(args.status_file)
        return path if path.is_absolute() else WORKSPACE_ROOT / path
    return case_decision_stage_status_path(case_key)


def bootstrap_lane_if_possible(status_path: Path) -> dict[str, Any] | None:
    with locked_status(status_path) as status:
        if status.get("decision_lane_session_key"):
            return {
                "session_key": status.get("decision_lane_session_key"),
                "topic_id": status.get("decision_lane_topic_id"),
            }
        if not status.get("decision_target_chat_id"):
            return None
    proc = run_command([sys.executable, str(BOOTSTRAP_DECISION_LANE), "--status-file", str(status_path)])
    return parse_json_stdout(proc)


def append_decision_timeline_entry(case_key: str, dispatch_id: str, packet_path: str) -> dict[str, Any]:
    timestamp = datetime.now(timezone.utc).isoformat()
    entry = f"- {timestamp} — completed decision-making `{dispatch_id}` with packet `{packet_path}`."
    unique_token = f"completed decision-making `{dispatch_id}` with packet `{packet_path}`."
    appended = append_case_timeline_entry(case_key, entry, unique_token=unique_token)
    return {
        "appended": appended,
        "case_key": case_key,
        "dispatch_id": dispatch_id,
        "packet_path": packet_path,
        "entry": entry,
    }


def main() -> None:
    args = parse_args()
    context_path = build_context(args)
    context = load_json(context_path)
    case_key = coerce_string(context.get("case_key"))
    dispatch_id = coerce_string(context.get("dispatch_id"))
    question = coerce_string(context.get("question"))
    market = context.get("market") or {}
    outputs = context.get("canonical_outputs") or {}
    upstream = context.get("upstream") or {}
    telegram = context.get("telegram") or {}
    status_path = status_path_for(args, case_key)

    with locked_status(status_path) as status:
        status.setdefault("artifact_type", "decision_stage_status")
        status.setdefault("schema_version", "decision-stage-status/v1")
        prior_status = coerce_string(status.get("status"))
        if prior_status:
            status["previous_status"] = prior_status
        status["case_key"] = case_key
        status["dispatch_id"] = dispatch_id
        status["question"] = question
        status["decision_context_path"] = relative_to_workspace(context_path)
        status["actor"] = "orchestrator"
        status["decision_target_chat_id"] = coerce_string(telegram.get("controller_chat_id"))
        status["decision_target_session_key"] = coerce_string(status.get("decision_target_session_key")) or coerce_string(status.get("decision_lane_session_key"))
        status["trade_authorization"] = ""
        status["position_policy"] = ""
        status["decision_readiness"] = ""
        status["recommended_side"] = ""
        status["warnings"] = []
        status.setdefault("packet_json_path", outputs.get("decision_packet_json", relative_to_workspace(case_decision_packet_json_path(case_key))))
        status.setdefault("packet_markdown_path", outputs.get("decision_packet_markdown", relative_to_workspace(case_decision_packet_markdown_path(case_key))))
        status["decision_visible_receipt_marker"] = f"SYNTHESIS RECEIVED | market={question} | dispatch_id={dispatch_id} | decision_context_path={relative_to_workspace(context_path)}"
        status["decision_visible_start_marker"] = f"DECISION-MAKING ANALYSIS UNDERWAY | market={question} | dispatch_id={dispatch_id} | decision_context_path={relative_to_workspace(context_path)}"
        status["decision_visible_finish_marker"] = f"DECISION-MAKING COMPLETED, DECISION PACKAGE CREATED | market={question} | dispatch_id={dispatch_id} | packet_path={outputs.get('decision_packet_markdown', relative_to_workspace(case_decision_packet_markdown_path(case_key)))}"
        set_overall_status(status, "decision_ready_for_receipt", stage="kickoff", message="Decision-Maker stage initialized from synthesis handoff", extra={"source_decision_handoff_path": upstream.get("decision_handoff_path", "")})

    verification_mode_path, selected_input_bundle_path = build_selected_bundle(context_path, args)
    selected_bundle = load_json(selected_input_bundle_path)
    try:
        enforce_sidecar_selection_guardrail(context, selected_bundle)
    except DecisionMakerError as exc:
        with locked_status(status_path) as status:
            status["verification_mode_path"] = relative_to_workspace(verification_mode_path)
            status["selected_input_bundle_path"] = relative_to_workspace(selected_input_bundle_path)
            status["selected_input_bundle_mode"] = coerce_string(selected_bundle.get("verification_mode"))
            status["selected_input_bundle_estimated_tokens"] = ((selected_bundle.get("bundle_budget") or {}).get("approx_tokens_after_trim", 0))
            append_stage_event(
                status,
                stage="decision_input_selection",
                state="guardrail_failed",
                message=str(exc),
                extra={
                    "selected_persona_count": len(selected_bundle.get("selected_persona_sidecars") or []),
                    "resolved_sidecar_bundle_path": coerce_string((selected_bundle.get("sidecar_selection_guardrail") or {}).get("resolved_sidecar_bundle_path")),
                },
            )
            set_overall_status(status, "decision_failed", stage="decision_input_selection", message="Decision-Maker sidecar selection guardrail failed", extra={"error": str(exc)})
        update_case_pipeline_status(
            case_key=case_key,
            dispatch_id=dispatch_id,
            market_id=coerce_string(market.get("market_id")),
            market_title=coerce_string(market.get("market_title")),
            status="pipeline_failed",
            current_stage="decision",
            stage_status_patch={"decision": "failed"},
            runner_id="run_decision_maker",
            message="Decision-Maker sidecar selection guardrail failed",
            terminal_summary_patch={"failure_reason": str(exc), "failed_stage": "decision"},
        )
        raise
    targeted_verification_pack_path = build_targeted_verification_pack(context_path, selected_input_bundle_path, args)
    targeted_verification_pack = load_json(targeted_verification_pack_path) if targeted_verification_pack_path else {}
    prompt_path = build_prompt(context_path, selected_input_bundle_path, targeted_verification_pack_path, args)
    with locked_status(status_path) as status:
        status["verification_mode_path"] = relative_to_workspace(verification_mode_path)
        status["selected_input_bundle_path"] = relative_to_workspace(selected_input_bundle_path)
        status["selected_input_bundle_mode"] = coerce_string(selected_bundle.get("verification_mode"))
        status["selected_input_bundle_estimated_tokens"] = ((selected_bundle.get("bundle_budget") or {}).get("approx_tokens_after_trim", 0))
        status["targeted_verification_pack_path"] = relative_to_workspace(targeted_verification_pack_path) if targeted_verification_pack_path else ""
        status["targeted_verification_pack_required"] = bool((targeted_verification_pack or {}).get("required", False))
        status.pop("targeted_external_checks_path", None)
        status.pop("targeted_external_checks_executed", None)
        status.pop("targeted_external_checks_successful", None)
        status["decision_prompt_path"] = relative_to_workspace(prompt_path)
        status["agent_tool_use_allowed"] = bool((selected_bundle.get("verification_enforcement") or {}).get("agent_tool_use_allowed", False))
        append_stage_event(status, stage="decision_input_selection", state="built", message="Built deterministic Decision-Maker selected-input bundle", extra={"verification_mode_path": relative_to_workspace(verification_mode_path), "selected_input_bundle_path": relative_to_workspace(selected_input_bundle_path), "verification_mode": coerce_string(selected_bundle.get("verification_mode")), "approx_tokens_after_trim": ((selected_bundle.get("bundle_budget") or {}).get("approx_tokens_after_trim", 0)), "agent_tool_use_allowed": bool((selected_bundle.get("verification_enforcement") or {}).get("agent_tool_use_allowed", False))})
        if targeted_verification_pack_path:
            append_stage_event(status, stage="decision_targeted_verification", state="built", message="Built deterministic targeted verification pack", extra={"targeted_verification_pack_path": relative_to_workspace(targeted_verification_pack_path), "approx_tokens_after_trim": ((targeted_verification_pack.get("pack_budget") or {}).get("approx_tokens_after_trim", 0))})
        append_stage_event(status, stage="decision_prompt", state="built", message="Built Decision-Maker prompt from compact selected-input bundle", extra={"prompt_path": relative_to_workspace(prompt_path)})

    if args.prepare_only:
        print(json.dumps({
            "ok": True,
            "prepare_only": True,
            "decision_context_path": relative_to_workspace(context_path),
            "verification_mode_path": relative_to_workspace(verification_mode_path),
            "selected_input_bundle_path": relative_to_workspace(selected_input_bundle_path),
            "targeted_verification_pack_path": relative_to_workspace(targeted_verification_pack_path) if targeted_verification_pack_path else "",
            "prompt_path": relative_to_workspace(prompt_path),
            "decision_stage_status_path": relative_to_workspace(status_path),
        }, indent=2 if args.pretty else None))
        return

    bootstrap_lane_if_possible(status_path)

    update_case_pipeline_status(
        case_key=case_key,
        dispatch_id=dispatch_id,
        market_id=coerce_string(market.get("market_id")),
        market_title=coerce_string(market.get("market_title")),
        status="pipeline_in_progress",
        current_stage="decision",
        stage_status_patch={"decision": "running"},
        runner_id="run_decision_maker",
        message="Decision-Maker stage started",
    )

    try:
        if args.result_json:
            with locked_status(status_path) as status:
                append_stage_event(status, stage="decision_receipt", state="offline_result_loaded", message="Loaded Decision-Maker result from provided JSON instead of live handoff")
                set_overall_status(status, "decision_analysis_running", stage="decision_execution", message="Decision-Maker packet loading started from provided JSON", extra={"prompt_path": relative_to_workspace(prompt_path)})
        else:
            started = start_decision_maker_turn(prompt_path, args)
            if not started.get("accepted"):
                with locked_status(status_path) as status:
                    set_overall_status(status, "decision_failed", stage="decision_receipt", message="Decision-Maker handoff was not accepted", extra={"gateway_response": started.get("gateway_response", {})})
                raise DecisionMakerError(f"decision-maker handoff was not accepted: {started.get('gateway_response')}")
            maybe_send_visible_marker(status_path, marker_key="decision_receipt_marker_sent_at", stage="decision_receipt", message=coerce_string(load_json(status_path).get("decision_visible_receipt_marker")))
            with locked_status(status_path) as status:
                append_stage_event(status, stage="decision_receipt", state="accepted", message="Decision-Maker handoff accepted", extra={"session_key": args.session_key, "handoff_status": started.get("status", "accepted")})
                set_overall_status(status, "decision_analysis_running", stage="decision_execution", message="Decision-Maker agent invocation accepted and analysis started", extra={"session_key": args.session_key, "prompt_path": relative_to_workspace(prompt_path), "handoff_status": started.get("status", "accepted")})
            maybe_send_visible_marker(status_path, marker_key="decision_analysis_marker_sent_at", stage="decision_execution", message=coerce_string(load_json(status_path).get("decision_visible_start_marker")))

        if args.result_json:
            invocation = {"packet": load_json(Path(args.result_json) if Path(args.result_json).is_absolute() else WORKSPACE_ROOT / args.result_json), "tool_activity_detected": False, "tool_names": [], "accepted": True, "status": "offline_result_json"}
        else:
            invocation = finish_decision_maker_turn(session_key=args.session_key, baseline_seq=int(started.get("baseline_seq", -1)), timeout_seconds=args.timeout_seconds)
            invocation.update({"accepted": True, "status": started.get("status", "accepted"), "baseline_seq": started.get("baseline_seq", -1), "gateway_response": started.get("gateway_response", {})})
        raw_packet = invocation["packet"]
        tool_usage = {
            "tool_activity_detected": bool(invocation.get("tool_activity_detected")),
            "tool_names": list(invocation.get("tool_names") or []),
            "tool_names_sequence": list(invocation.get("tool_names_sequence") or []),
            "search_queries": list(invocation.get("search_queries") or []),
            "fetched_urls": list(invocation.get("fetched_urls") or []),
            "search_query_count": int(invocation.get("search_query_count") or 0),
            "source_fetch_count": int(invocation.get("source_fetch_count") or 0),
            "source_families": list(invocation.get("source_families") or []),
            "distinct_source_family_count": int(invocation.get("distinct_source_family_count") or 0),
        }
        try:
            enforce_verification_tool_policy(selected_bundle, tool_usage, raw_packet)
        except DecisionMakerError as exc:
            with locked_status(status_path) as status:
                set_overall_status(status, "decision_failed", stage="decision_execution", message="Decision-Maker violated verification tool policy", extra={"error": str(exc), "tool_usage": tool_usage, "verification_mode": selected_bundle.get("verification_mode")})
            update_case_pipeline_status(
                case_key=case_key,
                dispatch_id=dispatch_id,
                market_id=coerce_string(market.get("market_id")),
                market_title=coerce_string(market.get("market_title")),
                status="pipeline_failed",
                current_stage="decision",
                stage_status_patch={"decision": "failed"},
                runner_id="run_decision_maker",
                message="Decision-Maker violated verification tool policy",
                terminal_summary_patch={"failure_reason": str(exc), "failed_stage": "decision"},
            )
            print(json.dumps({
                "ok": False,
                "decision_context_path": relative_to_workspace(context_path),
                "verification_mode_path": relative_to_workspace(verification_mode_path),
                "selected_input_bundle_path": relative_to_workspace(selected_input_bundle_path),
                "targeted_verification_pack_path": relative_to_workspace(targeted_verification_pack_path) if targeted_verification_pack_path else "",
                "prompt_path": relative_to_workspace(prompt_path),
                "error": str(exc),
                "tool_usage": tool_usage,
            }, indent=2 if args.pretty else None))
            raise SystemExit(1)

        packet = hydrate_packet_from_context(raw_packet, context, selected_bundle, targeted_verification_pack, valid_hours=args.valid_hours, tool_usage=tool_usage)
        validation = validate_decision_packet_payload(packet)
        if not validation["ok"]:
            with locked_status(status_path) as status:
                set_overall_status(status, "decision_failed", stage="decision_validation", message="Decision packet failed validation", extra={"errors": validation["errors"], "warnings": validation["warnings"]})
            update_case_pipeline_status(
                case_key=case_key,
                dispatch_id=dispatch_id,
                market_id=coerce_string(market.get("market_id")),
                market_title=coerce_string(market.get("market_title")),
                status="pipeline_failed",
                current_stage="decision",
                stage_status_patch={"decision": "failed"},
                runner_id="run_decision_maker",
                message="Decision packet failed validation",
                terminal_summary_patch={"failure_reason": "; ".join(validation["errors"]), "failed_stage": "decision"},
            )
            print(json.dumps({
                "ok": False,
                "decision_context_path": relative_to_workspace(context_path),
                "verification_mode_path": relative_to_workspace(verification_mode_path),
                "selected_input_bundle_path": relative_to_workspace(selected_input_bundle_path),
                "targeted_verification_pack_path": relative_to_workspace(targeted_verification_pack_path) if targeted_verification_pack_path else "",
                "prompt_path": relative_to_workspace(prompt_path),
                "errors": validation["errors"],
                "warnings": validation["warnings"],
            }, indent=2 if args.pretty else None))
            raise SystemExit(1)

        packet_json_path = case_decision_packet_json_path(case_key)
        packet_json_path.parent.mkdir(parents=True, exist_ok=True)
        write_json(packet_json_path, packet, pretty=True)

        run_command([sys.executable, str(VALIDATE_PACKET), "--packet-json", str(packet_json_path), *( ["--pretty"] if args.pretty else [] )])

        forecast_persist_summary: dict[str, Any] | None = None
        forecast_persist_error = ""
        try:
            persist_proc = run_command([sys.executable, str(PERSIST_FORECAST_DECISION), "--packet-json", str(packet_json_path), *( ["--pretty"] if args.pretty else [] )])
            forecast_persist_summary = parse_json_stdout(persist_proc)
        except Exception as exc:  # noqa: BLE001
            forecast_persist_error = str(exc)

        render_proc = run_command([sys.executable, str(RENDER_PACKET), "--packet-json", str(packet_json_path), *( ["--pretty"] if args.pretty else [] )])
        render_summary = parse_json_stdout(render_proc)
        packet_markdown_path = render_summary.get("decision_packet_path", relative_to_workspace(case_decision_packet_markdown_path(case_key)))
        timeline_update = append_decision_timeline_entry(case_key, dispatch_id, packet_markdown_path)

        with locked_status(status_path) as status:
            status["actor"] = "decision-maker"
            status["packet_json_path"] = relative_to_workspace(packet_json_path)
            status["packet_markdown_path"] = packet_markdown_path
            status["trade_authorization"] = (packet.get("decision") or {}).get("trade_authorization", "")
            status["position_policy"] = (packet.get("decision") or {}).get("position_policy", "")
            status["decision_readiness"] = (packet.get("decision") or {}).get("decision_readiness", "")
            status["recommended_side"] = (packet.get("decision") or {}).get("side", "")
            status["timeline_update"] = timeline_update
            if forecast_persist_summary is not None:
                status["forecast_decision_persist"] = forecast_persist_summary
            if forecast_persist_error:
                status["forecast_decision_persist_error"] = forecast_persist_error
            set_overall_status(status, "decision_completed", stage="decision_execution", message="Decision-Maker completed and packet rendered", extra={"warnings": validation["warnings"], "forecast_decision_persist_error": forecast_persist_error})

        maybe_send_visible_marker(status_path, marker_key="decision_completion_marker_sent_at", stage="decision_execution", message=coerce_string(load_json(status_path).get("decision_visible_finish_marker")))

        update_case_pipeline_status(
            case_key=case_key,
            dispatch_id=dispatch_id,
            market_id=coerce_string(market.get("market_id")),
            market_title=coerce_string(market.get("market_title")),
            status="pipeline_completed",
            current_stage="decision",
            stage_status_patch={"decision": "completed"},
            runner_id="run_decision_maker",
            message="Decision-Maker completed and packet rendered",
            terminal_summary_patch={
                "decision_packet_json": relative_to_workspace(packet_json_path),
                "decision_packet_markdown": packet_markdown_path,
                "trade_authorization": (packet.get("decision") or {}).get("trade_authorization", ""),
                "position_policy": (packet.get("decision") or {}).get("position_policy", ""),
                "decision_readiness": (packet.get("decision") or {}).get("decision_readiness", ""),
                "recommended_side": (packet.get("decision") or {}).get("side", ""),
                "forecast_decision_persisted": bool(forecast_persist_summary and forecast_persist_summary.get("ok")),
                "forecast_decision_persist_error": forecast_persist_error,
            },
        )

        print(json.dumps({
            "ok": True,
            "decision_context_path": relative_to_workspace(context_path),
            "verification_mode_path": relative_to_workspace(verification_mode_path),
            "selected_input_bundle_path": relative_to_workspace(selected_input_bundle_path),
            "targeted_verification_pack_path": relative_to_workspace(targeted_verification_pack_path) if targeted_verification_pack_path else "",
            "prompt_path": relative_to_workspace(prompt_path),
            "packet_json": relative_to_workspace(packet_json_path),
            "decision_packet_path": packet_markdown_path,
            "decision_stage_status_path": relative_to_workspace(status_path),
            "timeline_update": timeline_update,
            "forecast_decision_persist": forecast_persist_summary or {},
            "forecast_decision_persist_error": forecast_persist_error,
            "warnings": validation["warnings"],
        }, indent=2 if args.pretty else None))
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001
        with locked_status(status_path) as status:
            set_overall_status(status, "decision_failed", stage="decision_execution", message="Decision-Maker executor crashed", extra={"error": str(exc)})
        update_case_pipeline_status(
            case_key=case_key,
            dispatch_id=dispatch_id,
            market_id=coerce_string(market.get("market_id")),
            market_title=coerce_string(market.get("market_title")),
            status="pipeline_failed",
            current_stage="decision",
            stage_status_patch={"decision": "failed"},
            runner_id="run_decision_maker",
            message="Decision-Maker executor crashed",
            terminal_summary_patch={"failure_reason": str(exc), "failed_stage": "decision"},
        )
        raise


if __name__ == "__main__":
    main()
