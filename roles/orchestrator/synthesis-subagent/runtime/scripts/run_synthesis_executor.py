#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
REPO_ROOT = SCRIPT_DIR.parents[4]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))
if str(REPO_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "scripts"))

from case_pipeline_status import update_case_pipeline_status  # noqa: E402
from common import (  # noqa: E402
    WORKSPACE_ROOT,
    append_case_timeline_entry,
    load_json,
    relative_to_workspace,
    runtime_json_path_for,
    write_json,
)
from status import append_stage_event, locked_status, set_overall_status, write_status_file  # noqa: E402
from validation import validate_synthesis_result_payload  # noqa: E402

PLANNER_DIR = SUBAGENT_DIR / "planner" / "scripts"
RUNTIME_DIR = SUBAGENT_DIR / "runtime" / "scripts"
BUILD_BUNDLE = PLANNER_DIR / "build_synthesis_bundle.py"
BUILD_PROMPT = PLANNER_DIR / "build_synthesis_prompt.py"
VALIDATE_RESULT = RUNTIME_DIR / "validate_synthesis_result.py"
RENDER_SCRIPT = RUNTIME_DIR / "render_syndicated_finding.py"
RENDER_DECISION_HANDOFF = RUNTIME_DIR / "render_decision_handoff.py"
WRITE_SIDECAR = RUNTIME_DIR / "write_syndicated_runtime_metadata.py"
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


class ExecutorError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the synthesis executor for one dispatch")
    parser.add_argument("--dispatch-id", help="Dispatch id to synthesize")
    parser.add_argument("--case-key", help="Optional case key to disambiguate dispatch lookup")
    parser.add_argument("--bundle-json", help="Use an existing synthesis bundle JSON instead of rebuilding it")
    parser.add_argument("--prompt-path", help="Optional explicit prompt output path")
    parser.add_argument("--allow-truth-finding-research", dest="allow_truth_finding_research", action="store_true", help="Permit synthesis-stage truth-finding internet research aimed at improving predictive accuracy")
    parser.add_argument("--no-truth-finding-research", dest="allow_truth_finding_research", action="store_false", help="Disable synthesis-stage truth-finding research guidance")
    parser.add_argument("--allow-gapfill-research", dest="allow_truth_finding_research", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--no-gapfill-research", dest="allow_truth_finding_research", action="store_false", help=argparse.SUPPRESS)
    parser.add_argument("--result-json", help="Use an existing synthesizer result JSON instead of invoking a session")
    parser.add_argument("--session-key", help="Target session key for live synthesis execution (prefer a dedicated synthesis subagent session)")
    parser.add_argument("--agent-id", help="Optional agent id to pass to sessions.send")
    parser.add_argument("--timeout-seconds", type=float, default=240.0)
    parser.add_argument("--visible-chat-id", help="Telegram chat id for runtime-owned visible thread markers")
    parser.add_argument("--visible-topic-id", help="Telegram topic/thread id for runtime-owned visible thread markers")
    parser.add_argument("--visible-start-marker", help="Visible start marker text to post before synthesis begins")
    parser.add_argument("--visible-finish-marker", help="Visible finish marker text to post after synthesis succeeds")
    parser.add_argument("--status-file", help="Optional synthesis-stage-status.json path for explicit stage logging")
    parser.add_argument("--artifact-path", help="Optional explicit syndicated-finding markdown output path")
    parser.add_argument("--decision-handoff-path", help="Optional explicit decision-handoff markdown output path")
    parser.add_argument("--sidecar-path", help="Optional explicit sidecar output path")
    parser.add_argument("--write-current", action="store_true", help="Also write the canonical case-level artifacts under cases/<case-key>/synthesizer-agent/")
    parser.add_argument("--generated-by", default="orchestrator")
    parser.add_argument("--synthesis-method", default="dispatch_bundle_v1")
    parser.add_argument("--synthesis-status", default="rendered")
    parser.add_argument("--prepare-only", action="store_true", help="Only build bundle + prompt; do not execute or render")
    parser.add_argument("--pretty", action="store_true")
    parser.set_defaults(allow_truth_finding_research=True)
    return parser.parse_args()


def run_command(cmd: list[str], *, cwd: Path = WORKSPACE_ROOT) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    if proc.returncode != 0:
        raise ExecutorError(
            f"command failed ({proc.returncode}): {' '.join(cmd)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
        )
    return proc


def parse_json_stdout(proc: subprocess.CompletedProcess[str]) -> dict[str, Any]:
    stdout = proc.stdout.strip()
    if not stdout:
        return {}
    return json.loads(stdout)


def default_result_path(bundle_path: Path) -> Path:
    return bundle_path.with_name("synthesis-result.json")


def default_raw_response_path(bundle_path: Path) -> Path:
    return bundle_path.with_name("synthesis-response.json")


def default_artifact_path(bundle_path: Path) -> Path:
    return bundle_path.with_name("syndicated-finding.md")


def default_prompt_path(bundle_path: Path) -> Path:
    return bundle_path.with_name("synthesis-prompt.md")


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


def extract_assistant_text_from_messages(messages: list[Any], *, min_seq: int | None = None) -> str | None:
    ordered = sorted(
        [msg for msg in messages if isinstance(msg, dict)],
        key=lambda msg: ((msg.get("__openclaw") or {}).get("seq") or -1),
    )
    for item in ordered:
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


def wait_for_assistant_text(session_key: str, *, min_seq: int | None, timeout_seconds: float) -> str:
    deadline = time.time() + max(timeout_seconds, 1.0)
    last_messages: list[Any] = []
    while time.time() < deadline:
        payload = gateway_sessions_get(session_key, limit=20)
        messages = payload.get("messages") or []
        last_messages = messages if isinstance(messages, list) else []
        text = extract_assistant_text_from_messages(last_messages, min_seq=min_seq)
        if text:
            return text
        time.sleep(2.0)
    raise ExecutorError(
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
    raise ExecutorError("could not extract assistant text from sessions.send response")


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


def extract_json_payload(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if not stripped:
        raise ExecutorError("empty synthesis response text")
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        pass

    if "```json" in stripped:
        start = stripped.find("```json") + len("```json")
        end = stripped.find("```", start)
        if end != -1:
            candidate = stripped[start:end].strip()
            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                pass
    if "```" in stripped:
        start = stripped.find("```") + len("```")
        end = stripped.find("```", start)
        if end != -1:
            candidate = stripped[start:end].strip()
            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                pass

    decoder = json.JSONDecoder()
    for index, ch in enumerate(stripped):
        if ch != "{":
            continue
        try:
            obj, end = decoder.raw_decode(stripped[index:])
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError:
            continue
    raise ExecutorError("could not parse JSON object from synthesis response text")


def build_bundle(args: argparse.Namespace) -> Path:
    if args.bundle_json:
        path = Path(args.bundle_json)
        return path if path.is_absolute() else WORKSPACE_ROOT / path
    if not args.dispatch_id:
        raise ExecutorError("either --bundle-json or --dispatch-id is required")
    cmd = [sys.executable, str(BUILD_BUNDLE), "--dispatch-id", args.dispatch_id]
    if args.case_key:
        cmd.extend(["--case-key", args.case_key])
    if args.pretty:
        cmd.append("--pretty")
    proc = run_command(cmd)
    data = parse_json_stdout(proc)
    return WORKSPACE_ROOT / data["bundle_path"]


def build_prompt(bundle_path: Path, args: argparse.Namespace) -> Path:
    prompt_path = Path(args.prompt_path) if args.prompt_path else default_prompt_path(bundle_path)
    if not prompt_path.is_absolute():
        prompt_path = WORKSPACE_ROOT / prompt_path
    cmd = [
        sys.executable,
        str(BUILD_PROMPT),
        "--bundle-json",
        str(bundle_path),
        "--out",
        str(prompt_path),
        *( ["--allow-truth-finding-research"] if args.allow_truth_finding_research else ["--no-truth-finding-research"] ),
    ]
    if args.pretty:
        cmd.append("--pretty")
    run_command(cmd)
    return prompt_path


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
        raise ExecutorError(proc.stderr.strip() or proc.stdout.strip() or "telegram visible send failed")
    return parse_json_stdout(proc)


def maybe_send_visible_marker(chat_id: str | None, topic_id: str | None, message: str | None) -> dict[str, Any] | None:
    if not chat_id or not topic_id or not message:
        return None
    return send_visible_telegram_message(chat_id=str(chat_id), topic_id=str(topic_id), message=str(message))


def invoke_synthesizer(prompt_path: Path, bundle_path: Path, args: argparse.Namespace) -> Path:
    if args.result_json:
        result_path = Path(args.result_json)
        return result_path if result_path.is_absolute() else WORKSPACE_ROOT / result_path
    if not args.session_key:
        raise ExecutorError("either --result-json or --session-key is required unless --prepare-only is set")

    maybe_send_visible_marker(args.visible_chat_id, args.visible_topic_id, args.visible_start_marker)

    prompt = prompt_path.read_text()
    payload = {
        "sessionKey": args.session_key,
        "message": prompt,
        "timeoutSeconds": args.timeout_seconds,
    }
    if args.agent_id:
        payload["agentId"] = args.agent_id
    proc = run_command(
        [
            "node",
            str(OPENCLAW_SESSIONS_SEND),
            "--payload-json",
            json.dumps(payload),
        ]
    )
    gateway_response = json.loads(proc.stdout)
    raw_response_path = default_raw_response_path(bundle_path)
    write_json(raw_response_path, gateway_response, pretty=True)
    try:
        text = extract_text_from_gateway_response(gateway_response)
    except ExecutorError:
        status = gateway_response.get("status") if isinstance(gateway_response, dict) else None
        message_seq = gateway_response.get("messageSeq") if isinstance(gateway_response, dict) else None
        if args.session_key and status in {"started", "accepted", "running"}:
            text = wait_for_assistant_text(args.session_key, min_seq=message_seq if isinstance(message_seq, int) else None, timeout_seconds=args.timeout_seconds)
        else:
            raise
    result = extract_json_payload(text)
    result_path = default_result_path(bundle_path)
    write_json(result_path, result, pretty=True)
    return result_path


def validate_result(result_path: Path, args: argparse.Namespace) -> dict[str, Any]:
    proc = run_command([sys.executable, str(VALIDATE_RESULT), "--result-json", str(result_path), *( ["--pretty"] if args.pretty else [] )])
    return parse_json_stdout(proc)


def render_and_write(bundle_path: Path, result_path: Path, args: argparse.Namespace) -> dict[str, Any]:
    artifact_path = Path(args.artifact_path) if args.artifact_path else default_artifact_path(bundle_path)
    if not artifact_path.is_absolute():
        artifact_path = WORKSPACE_ROOT / artifact_path
    render_cmd = [
        sys.executable,
        str(RENDER_SCRIPT),
        "--bundle-json",
        str(bundle_path),
        "--result-json",
        str(result_path),
        "--out",
        str(artifact_path),
    ]
    if args.write_current:
        render_cmd.append("--write-current")
    if args.pretty:
        render_cmd.append("--pretty")
    render_proc = run_command(render_cmd)
    render_summary = parse_json_stdout(render_proc)

    sidecar_path = Path(args.sidecar_path) if args.sidecar_path else runtime_json_path_for(artifact_path)
    if not sidecar_path.is_absolute():
        sidecar_path = WORKSPACE_ROOT / sidecar_path
    sidecar_cmd = [
        sys.executable,
        str(WRITE_SIDECAR),
        "--bundle-json",
        str(bundle_path),
        "--artifact-path",
        str(artifact_path),
        "--out",
        str(sidecar_path),
        "--generated-by",
        args.generated_by,
        "--synthesis-method",
        args.synthesis_method,
        "--synthesis-status",
        args.synthesis_status,
    ]
    if args.write_current:
        sidecar_cmd.append("--write-current")
    if args.pretty:
        sidecar_cmd.append("--pretty")
    sidecar_proc = run_command(sidecar_cmd)
    sidecar_summary = parse_json_stdout(sidecar_proc)

    decision_handoff_path = Path(args.decision_handoff_path) if args.decision_handoff_path else artifact_path.with_name("decision-handoff.md")
    if not decision_handoff_path.is_absolute():
        decision_handoff_path = WORKSPACE_ROOT / decision_handoff_path
    handoff_cmd = [
        sys.executable,
        str(RENDER_DECISION_HANDOFF),
        "--bundle-json",
        str(bundle_path),
        "--result-json",
        str(result_path),
        "--syndicated-artifact-path",
        str(artifact_path),
        "--out",
        str(decision_handoff_path),
    ]
    if args.write_current:
        handoff_cmd.append("--write-current")
    if args.pretty:
        handoff_cmd.append("--pretty")
    handoff_proc = run_command(handoff_cmd)
    handoff_summary = parse_json_stdout(handoff_proc)
    return {"render": render_summary, "sidecar": sidecar_summary, "decision_handoff": handoff_summary}


def status_path_for(args: argparse.Namespace, bundle_path: Path) -> Path:
    if args.status_file:
        path = Path(args.status_file)
        return path if path.is_absolute() else WORKSPACE_ROOT / path
    return bundle_path.with_name("synthesis-stage-status.json")


def extract_case_key_from_path(path: Path) -> str:
    for part in path.parts:
        if part.startswith("case-"):
            return part
    return ""


def extract_dispatch_id_from_path(path: Path) -> str:
    for part in path.parts:
        if part.startswith("dispatch-case-"):
            return part
    return ""


def append_synthesis_timeline_entry(bundle_path: Path, artifact_path: str) -> dict[str, Any]:
    bundle = load_json(bundle_path)
    case_key = bundle.get("case_key") or ""
    dispatch_id = bundle.get("dispatch_id") or ""
    if not case_key or not dispatch_id:
        raise ExecutorError("bundle is missing case_key or dispatch_id; cannot append synthesis timeline entry")
    timestamp = datetime.now(timezone.utc).isoformat()
    entry = f"- {timestamp} — completed synthesis `{dispatch_id}` with artifact `{artifact_path}`."
    unique_token = f"completed synthesis `{dispatch_id}` with artifact `{artifact_path}`."
    appended = append_case_timeline_entry(case_key, entry, unique_token=unique_token)
    return {
        "appended": appended,
        "case_key": case_key,
        "dispatch_id": dispatch_id,
        "artifact_path": artifact_path,
        "entry": entry,
    }


def main() -> None:
    args = parse_args()
    bundle_path = build_bundle(args)
    prompt_path = build_prompt(bundle_path, args)
    status_path = status_path_for(args, bundle_path)
    status_exists = status_path.exists()
    if status_exists:
        with locked_status(status_path) as status_payload:
            append_stage_event(status_payload, stage="final_synthesis_execution", state="running", message="Final synthesis executor started", extra={"prompt_path": relative_to_workspace(prompt_path)})

    if args.prepare_only:
        summary = {
            "ok": True,
            "prepare_only": True,
            "bundle_json": relative_to_workspace(bundle_path),
            "prompt_path": relative_to_workspace(prompt_path),
        }
        print(json.dumps(summary, indent=2 if args.pretty else None))
        return

    try:
        result_path = invoke_synthesizer(prompt_path, bundle_path, args)
        validation = validate_synthesis_result_payload(load_json(result_path))
        if not validation["ok"]:
            if status_exists:
                with locked_status(status_path) as status_payload:
                    set_overall_status(status_payload, "final_synthesis_failed", stage="final_synthesis_execution", message="Final synthesis result failed validation", extra={"errors": validation["errors"]})
            summary = {
                "ok": False,
                "bundle_json": relative_to_workspace(bundle_path),
                "prompt_path": relative_to_workspace(prompt_path),
                "result_json": relative_to_workspace(result_path),
                "errors": validation["errors"],
                "warnings": validation["warnings"],
            }
            print(json.dumps(summary, indent=2 if args.pretty else None))
            raise SystemExit(1)

        outputs = render_and_write(bundle_path, result_path, args)
        timeline_update = append_synthesis_timeline_entry(bundle_path, outputs["render"]["artifact_path"])
        visible_finish = maybe_send_visible_marker(args.visible_chat_id, args.visible_topic_id, args.visible_finish_marker)
        bundle_payload = load_json(bundle_path)
        bundle_artifact_type = str(bundle_payload.get("artifact_type") or "").strip() if isinstance(bundle_payload, dict) else ""
        resolved_structured_bundle_path = ""
        resolved_structured_bundle_artifact_type = ""
        if bundle_artifact_type == "sidecar_synthesis_bundle":
            resolved_structured_bundle_path = relative_to_workspace(bundle_path)
            resolved_structured_bundle_artifact_type = bundle_artifact_type
        else:
            sibling_sidecar_bundle = bundle_path.with_name("sidecar-synthesis-bundle.json")
            if sibling_sidecar_bundle.exists():
                sibling_payload = load_json(sibling_sidecar_bundle)
                sibling_type = str(sibling_payload.get("artifact_type") or "").strip() if isinstance(sibling_payload, dict) else ""
                if sibling_type == "sidecar_synthesis_bundle":
                    resolved_structured_bundle_path = relative_to_workspace(sibling_sidecar_bundle)
                    resolved_structured_bundle_artifact_type = sibling_type
        if status_exists:
            with locked_status(status_path) as status_payload:
                status_payload.update({
                    "synthesis_prompt_path": relative_to_workspace(prompt_path),
                    "result_json": relative_to_workspace(result_path),
                    "final_artifact_path": outputs["render"]["artifact_path"],
                    "final_sidecar_path": outputs["sidecar"]["sidecar_path"],
                    "final_decision_handoff_path": outputs["decision_handoff"]["decision_handoff_path"],
                    "timeline_update": timeline_update,
                })
                if resolved_structured_bundle_path:
                    status_payload.update({
                        "structured_bundle_path": resolved_structured_bundle_path,
                        "structured_bundle_artifact_type": resolved_structured_bundle_artifact_type,
                    })
                set_overall_status(status_payload, "synthesis_completed", stage="final_synthesis_execution", message="Final synthesis completed and artifacts rendered")
        case_key = extract_case_key_from_path(bundle_path)
        dispatch_id = extract_dispatch_id_from_path(bundle_path)
        if case_key:
            update_case_pipeline_status(
                case_key=case_key,
                dispatch_id=dispatch_id,
                status="pipeline_in_progress",
                current_stage="synthesis",
                stage_status_patch={
                    "swarm": "completed",
                    "synthesis": "completed",
                    "decision": "pending",
                },
                runner_id="run_synthesis_executor",
                message="Synthesis completed and decision handoff is ready",
                terminal_summary_patch={
                    "synthesis_artifact_path": outputs["render"]["artifact_path"],
                    "decision_handoff_path": outputs["decision_handoff"]["decision_handoff_path"],
                },
            )
        summary = {
            "ok": True,
            "bundle_json": relative_to_workspace(bundle_path),
            "prompt_path": relative_to_workspace(prompt_path),
            "result_json": relative_to_workspace(result_path),
            "warnings": validation["warnings"],
            "artifact_path": outputs["render"]["artifact_path"],
            "current_artifact_path": outputs["render"].get("current_artifact_path", ""),
            "decision_handoff_path": outputs["decision_handoff"]["decision_handoff_path"],
            "current_decision_handoff_path": outputs["decision_handoff"].get("current_decision_handoff_path", ""),
            "sidecar_path": outputs["sidecar"]["sidecar_path"],
            "current_sidecar_path": outputs["sidecar"].get("current_sidecar_path", ""),
            "timeline_update": timeline_update,
            "allow_truth_finding_research": args.allow_truth_finding_research,
            "visible_finish": visible_finish,
        }
        print(json.dumps(summary, indent=2 if args.pretty else None))
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001
        if status_exists:
            with locked_status(status_path) as status_payload:
                set_overall_status(status_payload, "final_synthesis_failed", stage="final_synthesis_execution", message="Final synthesis executor crashed", extra={"error": str(exc)})
        case_key = extract_case_key_from_path(bundle_path if 'bundle_path' in locals() else status_path)
        dispatch_id = extract_dispatch_id_from_path(bundle_path if 'bundle_path' in locals() else status_path)
        if case_key:
            update_case_pipeline_status(
                case_key=case_key,
                dispatch_id=dispatch_id,
                status="pipeline_failed",
                current_stage="synthesis",
                stage_status_patch={"synthesis": "failed"},
                runner_id="run_synthesis_executor",
                message="Synthesis failed",
                terminal_summary_patch={"failure_reason": str(exc), "failed_stage": "synthesis"},
            )
        raise


if __name__ == "__main__":
    main()
