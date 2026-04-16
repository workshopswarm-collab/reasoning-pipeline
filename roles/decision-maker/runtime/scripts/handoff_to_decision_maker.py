#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    case_decision_packet_json_path,
    case_decision_packet_markdown_path,
    case_decision_stage_status_path,
    coerce_string,
    default_decision_agent_session_key,
    load_json,
    read_json_if_exists,
    relative_to_workspace,
    utc_now_iso,
    write_json,
)

BUILD_CONTEXT = SCRIPT_DIR / "build_decision_context.py"
DEFAULT_TARGET_SESSION = ""


class HandoffError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build and optionally send an Orchestrator -> Decision-Maker handoff")
    parser.add_argument("--case-key")
    parser.add_argument("--dispatch-id")
    parser.add_argument("--decision-context-json")
    parser.add_argument("--market-price", type=float)
    parser.add_argument("--market-id")
    parser.add_argument("--market-title")
    parser.add_argument("--quote-timestamp")
    parser.add_argument("--target-session", default=DEFAULT_TARGET_SESSION)
    parser.add_argument("--prompt-out")
    parser.add_argument("--send", action="store_true", help="Actually send the handoff via sessions.send")
    parser.add_argument("--timeout-seconds", type=float, default=0.0, help="0 = fire-and-forget")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def run_command(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, cwd=str(WORKSPACE_ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        raise HandoffError(f"command failed ({proc.returncode}): {' '.join(cmd)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")
    return proc


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
    payload = json.loads(proc.stdout)
    return WORKSPACE_ROOT / payload["decision_context_path"]


def default_prompt_path(case_key: str, dispatch_id: str) -> Path:
    filename = f"decision-maker-handoff-{dispatch_id or case_key}.md"
    return WORKSPACE_ROOT / "roles" / "decision-maker" / "runtime" / "artifacts" / case_key / filename


def build_handoff_message(context: dict[str, Any], *, context_path: Path) -> str:
    case_key = coerce_string(context.get("case_key"))
    dispatch_id = coerce_string(context.get("dispatch_id"))
    question = coerce_string(context.get("question"))
    market = context.get("market") or {}
    upstream = context.get("upstream") or {}

    decision_handoff_path = WORKSPACE_ROOT / coerce_string(upstream.get("decision_handoff_path"))
    syndicated_runtime_path = WORKSPACE_ROOT / coerce_string(upstream.get("syndicated_runtime_path")) if coerce_string(upstream.get("syndicated_runtime_path")) else None
    syndicated_finding_path = WORKSPACE_ROOT / coerce_string(upstream.get("syndicated_finding_path")) if coerce_string(upstream.get("syndicated_finding_path")) else None
    runtime_entry = WORKSPACE_ROOT / "roles" / "decision-maker" / "runtime" / "scripts" / "run_decision_maker.py"
    canonical_markdown = case_decision_packet_markdown_path(case_key)
    canonical_json = case_decision_packet_json_path(case_key)

    lines = [
        f"Decision-Maker handoff for case `{case_key}`.",
        "",
        "You are the separate `decision-maker` agent. Use your own workspace persona and continuity, but use the Orchestrator repo as the canonical implementation and artifact surface.",
        "",
        "Canonical implementation surface:",
        f"- {WORKSPACE_ROOT / 'roles' / 'decision-maker'}",
        "",
        "Canonical case artifacts:",
        f"- decision handoff: {decision_handoff_path}",
        f"- syndicated runtime: {syndicated_runtime_path if syndicated_runtime_path else '(not available)'}",
        f"- syndicated finding: {syndicated_finding_path if syndicated_finding_path else '(not available)'}",
        f"- decision context: {context_path}",
        "",
        "Canonical runtime entry point:",
        f"- {runtime_entry}",
        "",
        "Canonical outputs to write/update:",
        f"- markdown packet: {canonical_markdown}",
        f"- json packet: {canonical_json}",
        "",
        "Task:",
        "1. Review the upstream synthesis artifacts and decision context.",
        "2. Use the canonical implementation under the Orchestrator repo rather than creating parallel implementation files in your own workspace.",
        "3. Produce or update the final decision packet in the canonical Orchestrator case folder.",
        "4. Fail closed rather than manufacture action.",
        "5. Reply with a concise completion summary that includes the case key and any blockers.",
        "",
        "Key case details:",
        f"- case_key: {case_key}",
        f"- dispatch_id: {dispatch_id}",
        f"- question: {question}",
        f"- market_reference_price: {market.get('market_reference_price')}",
        f"- market_title: {market.get('market_title')}",
        "",
        "Structured context bundle:",
        "```json",
        json.dumps(context, indent=2, ensure_ascii=False),
        "```",
        "",
        "If you use the provided runtime entry point, prefer an equivalent of:",
        f"python3 {runtime_entry} --case-key {case_key}",
    ]
    if dispatch_id:
        lines[-1] += f" --dispatch-id {dispatch_id}"
    return "\n".join(lines).rstrip() + "\n"


def send_handoff(session_key: str, message: str, timeout_seconds: float) -> dict[str, Any]:
    proc = run_command([
        "openclaw",
        "gateway",
        "call",
        "sessions.send",
        "--params",
        json.dumps({
            "sessionKey": session_key,
            "message": message,
            "timeoutSeconds": timeout_seconds,
        }),
        "--json",
    ])
    stdout = proc.stdout.strip()
    return json.loads(stdout) if stdout else {"ok": True}


def main() -> None:
    args = parse_args()
    context_path = build_context(args)
    context = load_json(context_path)
    case_key = coerce_string(context.get("case_key"))
    dispatch_id = coerce_string(context.get("dispatch_id"))
    recommended_defaults = context.get("recommended_runtime_defaults") or {}
    target_session = coerce_string(args.target_session) or coerce_string(recommended_defaults.get("decision_agent_session_key")) or default_decision_agent_session_key(case_key)
    prompt_path = Path(args.prompt_out) if args.prompt_out else default_prompt_path(case_key, dispatch_id or case_key)
    if not prompt_path.is_absolute():
        prompt_path = WORKSPACE_ROOT / prompt_path
    prompt_path.parent.mkdir(parents=True, exist_ok=True)

    message = build_handoff_message(context, context_path=context_path)
    prompt_path.write_text(message)
    message_sha256 = hashlib.sha256(message.encode("utf-8")).hexdigest()

    send_result: dict[str, Any] | None = None
    status_value = "handoff_prepared"
    if args.send:
        send_result = send_handoff(target_session, message, args.timeout_seconds)
        status_value = "handoff_sent"

    status_path = case_decision_stage_status_path(case_key)
    prior_status = read_json_if_exists(status_path)
    status_payload = {
        "artifact_type": "decision_stage_status",
        "schema_version": "decision-stage-status/v1",
        "updated_at": utc_now_iso(),
        "case_key": case_key,
        "dispatch_id": dispatch_id,
        "status": status_value,
        "actor": "orchestrator",
        "target_session": target_session,
        "decision_context_path": relative_to_workspace(context_path),
        "handoff_prompt_path": relative_to_workspace(prompt_path),
        "message_sha256": message_sha256,
        "send_requested": bool(args.send),
        "send_timeout_seconds": args.timeout_seconds,
        "send_result": send_result or {},
        "packet_json_path": relative_to_workspace(case_decision_packet_json_path(case_key)),
        "packet_markdown_path": relative_to_workspace(case_decision_packet_markdown_path(case_key)),
        "previous_status": prior_status.get("status") if isinstance(prior_status, dict) else "",
    }
    write_json(status_path, status_payload, pretty=True)

    summary = {
        "ok": True,
        "decision_context_path": relative_to_workspace(context_path),
        "handoff_prompt_path": relative_to_workspace(prompt_path),
        "decision_stage_status_path": relative_to_workspace(status_path),
        "target_session": target_session,
        "sent": bool(args.send),
        "send_result": send_result or {},
    }
    print(json.dumps(summary, indent=2 if args.pretty else None))


if __name__ == "__main__":
    try:
        main()
    except HandoffError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        raise SystemExit(1)
