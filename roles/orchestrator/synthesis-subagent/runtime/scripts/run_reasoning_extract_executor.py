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
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import WORKSPACE_ROOT, load_json, relative_to_workspace, sha256_text, write_json  # noqa: E402
from status import append_stage_event, locked_status, set_overall_status, update_request, write_status_file  # noqa: E402
from validation import validate_reasoning_extract_artifact, validate_reasoning_extract_payload  # noqa: E402

PLANNER_DIR = SUBAGENT_DIR / "planner" / "scripts"
RUNTIME_DIR = SUBAGENT_DIR / "runtime" / "scripts"
BUILD_BUNDLE = PLANNER_DIR / "build_synthesis_bundle.py"
BUILD_JOBS = PLANNER_DIR / "build_reasoning_extract_jobs.py"
BUILD_PROMPT = PLANNER_DIR / "build_reasoning_extract_prompt.py"
VALIDATE_EXTRACT = RUNTIME_DIR / "validate_reasoning_extract.py"
LAUNCH_SYNTHESIS_IF_READY = RUNTIME_DIR / "launch_synthesis_if_ready.py"
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
    parser = argparse.ArgumentParser(description="Run the persona reasoning-extract executor")
    parser.add_argument("--persona", required=True, help="Persona key to extract")
    parser.add_argument("--dispatch-id", help="Dispatch id to build from if jobs/bundle are not supplied")
    parser.add_argument("--case-key", help="Optional case key to disambiguate dispatch lookup")
    parser.add_argument("--bundle-json", help="Use an existing synthesis bundle JSON")
    parser.add_argument("--jobs-json", help="Use an existing reasoning-extract-jobs JSON")
    parser.add_argument("--prompt-path", help="Optional explicit prompt output path")
    parser.add_argument("--result-json", help="Use an existing reasoning extract JSON instead of invoking a session")
    parser.add_argument("--session-key", help="Target session key for live extraction execution (prefer a dedicated extraction subagent session)")
    parser.add_argument("--agent-id", help="Optional agent id to pass to sessions.send")
    parser.add_argument("--timeout-seconds", type=float, default=180.0)
    parser.add_argument("--announce-thread-markers", action="store_true", help="Legacy fallback: ask the session itself to mention start/end markers in-thread")
    parser.add_argument("--visible-chat-id", help="Telegram chat id for runtime-owned visible thread markers")
    parser.add_argument("--visible-topic-id", help="Telegram topic/thread id for runtime-owned visible thread markers")
    parser.add_argument("--visible-start-marker", help="Visible start marker text to post before extraction begins")
    parser.add_argument("--visible-finish-marker", help="Visible finish marker text to post after extraction succeeds")
    parser.add_argument("--artifact-path", help="Optional explicit output path for the validated extract artifact")
    parser.add_argument("--raw-response-path", help="Optional explicit path for the raw Gateway/session response")
    parser.add_argument("--status-file", help="Optional synthesis-stage-status.json path for explicit stage logging")
    parser.add_argument("--include-support-bodies", action="store_true", help="Build jobs with inline support-note bodies")
    parser.add_argument("--prepare-only", action="store_true", help="Only build bundle/jobs/prompt; do not execute or write the extract artifact")
    parser.add_argument("--pretty", action="store_true")
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


def build_jobs(bundle_path: Path, args: argparse.Namespace) -> Path:
    if args.jobs_json:
        path = Path(args.jobs_json)
        return path if path.is_absolute() else WORKSPACE_ROOT / path
    cmd = [sys.executable, str(BUILD_JOBS), "--bundle-json", str(bundle_path)]
    if args.include_support_bodies:
        cmd.append("--include-support-bodies")
    if args.pretty:
        cmd.append("--pretty")
    proc = run_command(cmd)
    data = parse_json_stdout(proc)
    return WORKSPACE_ROOT / data["jobs_path"]


def default_prompt_path(jobs_path: Path, persona: str) -> Path:
    return jobs_path.with_name(f"reasoning-extract-{persona}-prompt.md")


def default_result_path(jobs_path: Path, persona: str) -> Path:
    return jobs_path.with_name(f"reasoning-extract-{persona}-result.json")


def default_raw_response_path(artifact_path: Path) -> Path:
    return artifact_path.with_name(f"{artifact_path.stem}.response.json")


def load_persona_job(jobs_path: Path, persona: str) -> tuple[dict[str, Any], dict[str, Any]]:
    jobs_payload = load_json(jobs_path)
    matches = [job for job in jobs_payload.get("jobs", []) if job.get("persona") == persona]
    if not matches:
        raise ExecutorError(f"persona not found in jobs file: {persona}")
    if len(matches) > 1:
        raise ExecutorError(f"multiple jobs found for persona: {persona}")
    return jobs_payload, matches[0]


def build_prompt(jobs_path: Path, persona: str, args: argparse.Namespace) -> Path:
    prompt_path = Path(args.prompt_path) if args.prompt_path else default_prompt_path(jobs_path, persona)
    if not prompt_path.is_absolute():
        prompt_path = WORKSPACE_ROOT / prompt_path
    cmd = [
        sys.executable,
        str(BUILD_PROMPT),
        "--jobs-json",
        str(jobs_path),
        "--persona",
        persona,
        "--out",
        str(prompt_path),
    ]
    if args.pretty:
        cmd.append("--pretty")
    run_command(cmd)
    return prompt_path


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


def extract_json_payload(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if not stripped:
        raise ExecutorError("empty reasoning extract response text")
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
            obj, _end = decoder.raw_decode(stripped[index:])
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError:
            continue
    raise ExecutorError("could not parse JSON object from reasoning extract response text")


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


def build_live_execution_message(prompt_text: str, args: argparse.Namespace) -> str:
    if not args.announce_thread_markers:
        return prompt_text
    prefix = (
        "Before doing the extraction, post a short visible status message in this Telegram topic that says 'STARTING EXTRACTION'. "
        "After completing the extraction, post another short visible status message that says 'FINISHED EXTRACTION'. "
        "Your final substantive reply in this thread must still contain the JSON object for the reasoning extract so the runtime can parse it.\n\n"
    )
    return prefix + prompt_text


def obtain_result_json(prompt_path: Path, jobs_path: Path, artifact_path: Path, args: argparse.Namespace) -> Path:
    if args.result_json:
        result_path = Path(args.result_json)
        return result_path if result_path.is_absolute() else WORKSPACE_ROOT / result_path
    if not args.session_key:
        raise ExecutorError("either --result-json or --session-key is required unless --prepare-only is set")

    maybe_send_visible_marker(args.visible_chat_id, args.visible_topic_id, args.visible_start_marker)

    payload = {
        "sessionKey": args.session_key,
        "message": build_live_execution_message(prompt_path.read_text(), args),
        "timeoutSeconds": args.timeout_seconds,
    }
    if args.agent_id:
        payload["agentId"] = args.agent_id

    proc = run_command(["node", str(OPENCLAW_SESSIONS_SEND), "--payload-json", json.dumps(payload)])
    gateway_response = json.loads(proc.stdout)
    raw_response_path = Path(args.raw_response_path) if args.raw_response_path else default_raw_response_path(artifact_path)
    if not raw_response_path.is_absolute():
        raw_response_path = WORKSPACE_ROOT / raw_response_path
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
    result_path = default_result_path(jobs_path, args.persona)
    write_json(result_path, result, pretty=True)
    return result_path


def validate_result(result_path: Path, args: argparse.Namespace) -> dict[str, Any]:
    proc = run_command(
        [
            sys.executable,
            str(VALIDATE_EXTRACT),
            "--result-json",
            str(result_path),
            *( ["--pretty"] if args.pretty else [] ),
        ]
    )
    return parse_json_stdout(proc)


def build_artifact_payload(result_path: Path, job: dict[str, Any], prompt_path: Path, args: argparse.Namespace) -> dict[str, Any]:
    payload = load_json(result_path)
    if not isinstance(payload, dict):
        raise ExecutorError("reasoning extract result must be a JSON object")
    artifact_payload = dict(payload)
    artifact_payload["runtime_metadata"] = {
        "extraction_mode": "manual_result" if args.result_json else "live_session",
        "extracted_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "source_persona_finding_path": job.get("persona_finding_path") or "",
        "source_persona_sha256": job.get("persona_source_sha256") or "",
        "job_input_sha256": job.get("job_input_sha256") or "",
        "prompt_sha256": sha256_text(prompt_path.read_text()),
        "source_explicit_probability": job.get("persona_explicit_probability"),
    }
    return artifact_payload


def write_artifact(artifact_payload: dict[str, Any], artifact_path: Path) -> None:
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(artifact_path, artifact_payload, pretty=True)


def status_path_for(args: argparse.Namespace, artifact_path: Path) -> Path:
    if args.status_file:
        path = Path(args.status_file)
        return path if path.is_absolute() else WORKSPACE_ROOT / path
    return artifact_path.parent.parent / "synthesis-stage-status.json"


def main() -> None:
    args = parse_args()
    bundle_path = build_bundle(args)
    jobs_path = build_jobs(bundle_path, args)
    jobs_payload, job = load_persona_job(jobs_path, args.persona)
    prompt_path = build_prompt(jobs_path, args.persona, args)

    artifact_path = Path(args.artifact_path) if args.artifact_path else Path(job["reasoning_extract_path"])
    if not artifact_path.is_absolute():
        artifact_path = WORKSPACE_ROOT / artifact_path
    status_path = status_path_for(args, artifact_path)
    status_exists = status_path.exists()
    if status_exists:
        with locked_status(status_path) as status_payload:
            update_request(status_payload, args.persona, {"status": "running"})
            append_stage_event(
                status_payload,
                stage="reasoning_extract_execution",
                state="running",
                message="Reasoning extract executor started",
                extra={"persona": args.persona},
            )

    if args.prepare_only:
        summary = {
            "ok": True,
            "prepare_only": True,
            "bundle_json": relative_to_workspace(bundle_path),
            "jobs_json": relative_to_workspace(jobs_path),
            "persona": args.persona,
            "prompt_path": relative_to_workspace(prompt_path),
            "artifact_path": relative_to_workspace(artifact_path),
            "support_mode": jobs_payload.get("support_mode"),
        }
        print(json.dumps(summary, indent=2 if args.pretty else None))
        return

    try:
        result_path = obtain_result_json(prompt_path, jobs_path, artifact_path, args)
        validation = validate_reasoning_extract_payload(load_json(result_path))
        if not validation["ok"]:
            if status_exists:
                with locked_status(status_path) as status_payload:
                    update_request(status_payload, args.persona, {"status": "failed", "failure_errors": validation["errors"], "failure_warnings": validation["warnings"]})
                    set_overall_status(status_payload, "reasoning_extracts_failed", stage="reasoning_extract_execution", message="Reasoning extract executor failed structural validation", extra={"persona": args.persona, "errors": validation["errors"]})
            summary = {
                "ok": False,
                "bundle_json": relative_to_workspace(bundle_path),
                "jobs_json": relative_to_workspace(jobs_path),
                "persona": args.persona,
                "prompt_path": relative_to_workspace(prompt_path),
                "result_json": relative_to_workspace(result_path),
                "errors": validation["errors"],
                "warnings": validation["warnings"],
            }
            print(json.dumps(summary, indent=2 if args.pretty else None))
            raise SystemExit(1)

        artifact_payload = build_artifact_payload(result_path, job, prompt_path, args)
        artifact_validation = validate_reasoning_extract_artifact(artifact_payload, job=job, prompt_text=prompt_path.read_text())
        if not artifact_validation["ok"]:
            if status_exists:
                with locked_status(status_path) as status_payload:
                    update_request(status_payload, args.persona, {"status": "failed", "failure_errors": artifact_validation["errors"], "failure_warnings": artifact_validation["warnings"], "artifact_state": "stale"})
                    set_overall_status(status_payload, "reasoning_extracts_failed", stage="reasoning_extract_execution", message="Reasoning extract executor failed freshness/provenance validation", extra={"persona": args.persona, "errors": artifact_validation["errors"]})
            summary = {
                "ok": False,
                "bundle_json": relative_to_workspace(bundle_path),
                "jobs_json": relative_to_workspace(jobs_path),
                "persona": args.persona,
                "prompt_path": relative_to_workspace(prompt_path),
                "result_json": relative_to_workspace(result_path),
                "errors": artifact_validation["errors"],
                "warnings": artifact_validation["warnings"],
            }
            print(json.dumps(summary, indent=2 if args.pretty else None))
            raise SystemExit(1)

        write_artifact(artifact_payload, artifact_path)
        visible_finish = maybe_send_visible_marker(args.visible_chat_id, args.visible_topic_id, args.visible_finish_marker)

        if status_exists:
            with locked_status(status_path) as status_payload:
                update_request(status_payload, args.persona, {
                    "status": "completed",
                    "artifact_state": "current",
                    "artifact_validation_errors": [],
                    "artifact_validation_warnings": artifact_validation["warnings"],
                    "completed_artifact_path": relative_to_workspace(artifact_path),
                })
                append_stage_event(status_payload, stage="reasoning_extract_execution", state="completed", message="Reasoning extract executor completed", extra={"persona": args.persona, "artifact_path": relative_to_workspace(artifact_path)})

        synthesis_launch = None
        if status_exists and LAUNCH_SYNTHESIS_IF_READY.exists():
            proc = subprocess.run(
                [
                    sys.executable,
                    str(LAUNCH_SYNTHESIS_IF_READY),
                    "--status-file",
                    str(status_path),
                    *( ["--pretty"] if args.pretty else [] ),
                ],
                cwd=str(WORKSPACE_ROOT),
                capture_output=True,
                text=True,
            )
            if proc.returncode == 0 and proc.stdout.strip():
                synthesis_launch = json.loads(proc.stdout)
            else:
                if status_exists:
                    with locked_status(status_path) as status_payload:
                        set_overall_status(status_payload, "ready_for_reasoning_extracts", stage="reasoning_extract_execution", message="Automatic synthesis promotion check returned nonzero", extra={"persona": args.persona, "returncode": proc.returncode})
                synthesis_launch = {
                    "ok": False,
                    "returncode": proc.returncode,
                    "stdout": proc.stdout,
                    "stderr": proc.stderr,
                }

        summary = {
            "ok": True,
            "bundle_json": relative_to_workspace(bundle_path),
            "jobs_json": relative_to_workspace(jobs_path),
            "persona": args.persona,
            "prompt_path": relative_to_workspace(prompt_path),
            "result_json": relative_to_workspace(result_path),
            "artifact_path": relative_to_workspace(artifact_path),
            "visible_finish": visible_finish,
            "synthesis_launch": synthesis_launch,
            "warnings": validation["warnings"] + artifact_validation["warnings"],
            "support_mode": jobs_payload.get("support_mode"),
        }
        print(json.dumps(summary, indent=2 if args.pretty else None))
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001
        if status_exists:
            with locked_status(status_path) as status_payload:
                update_request(status_payload, args.persona, {"status": "failed", "failure_errors": [str(exc)]})
                set_overall_status(status_payload, "reasoning_extracts_failed", stage="reasoning_extract_execution", message="Reasoning extract executor crashed", extra={"persona": args.persona, "error": str(exc)})
        raise


if __name__ == "__main__":
    main()
