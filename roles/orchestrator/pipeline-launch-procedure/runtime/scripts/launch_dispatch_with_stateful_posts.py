#!/usr/bin/env python3
from __future__ import annotations

"""Execute a Telegram fresh-topic dispatch end-to-end with immediate state patching.

Canonical runtime behavior:
1. bootstrap/reuse controller + persona topics
2. materialize each persona topic session and deliver the assignment via `sessions.send`
3. immediately patch each successful handoff to `running` via `update_research_run.py`
4. let `update_research_run.py` auto-post visible STARTING markers from stored metadata
5. ensure the Telegram swarm runtime loop is running once research begins
6. return a delivery summary with per-run patch outcomes

This removes normal-path dependence on a later/manual replay step. Replay/finalize
helpers remain available as repair/backstop tools.

Important runtime note:
- internal handoff execution is performed through the bundled Node helper
  `openclaw_sessions_send.mjs`, which calls the confirmed Gateway RPC
  method `sessions.send`
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = BASE_DIR.parent
PIPELINE_DIR = RUNTIME_DIR.parent
WORKSPACE_ROOT = PIPELINE_DIR.parents[2]
BOOTSTRAP_TOPICS = BASE_DIR / "internal" / "bootstrap_telegram_topics.py"
RUNTIME_HELPER = BASE_DIR / "internal" / "runtime_execute_dispatch.py"
UPDATE_RUN = BASE_DIR / "update_research_run.py"
SESSIONS_SEND_HELPER = BASE_DIR / "internal" / "openclaw_sessions_send.mjs"
RUNTIME_LOOP = BASE_DIR / "run_telegram_swarm_runtime_loop.py"
STATE_DIR = BASE_DIR / ".runtime-state"
RUNTIME_LOOP_PID = STATE_DIR / "telegram_swarm_runtime_loop.pid"
RUNTIME_LOOP_ERROR = STATE_DIR / "telegram_swarm_runtime_loop.error.json"
DEFAULT_ENV_PATH = WORKSPACE_ROOT / ".env"


def maybe_load_workspace_env() -> None:
    if os.getenv("PREDQUANT_ORCHESTRATOR_URL"):
        return
    if not DEFAULT_ENV_PATH.exists():
        return
    for raw_line in DEFAULT_ENV_PATH.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch a dispatch with immediate running-state patching")
    parser.add_argument("--manifest-path", required=True, help="Dispatch manifest JSON path")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def parse_json_lines(raw: str) -> dict[str, Any]:
    stdout = (raw or "").strip()
    if not stdout:
        return {}
    try:
        parsed = json.loads(stdout)
        if isinstance(parsed, dict):
            return parsed
        raise RuntimeError(f"expected top-level JSON object, got {type(parsed).__name__}")
    except json.JSONDecodeError:
        pass
    for line in reversed([line for line in stdout.splitlines() if line.strip()]):
        try:
            parsed = json.loads(line)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            continue
    raise RuntimeError("unable to parse JSON object from command output")


def python_json(script: Path, args: list[str]) -> dict[str, Any]:
    proc = subprocess.run([sys.executable, str(script), *args], text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"{script.name} failed")
    return parse_json_lines(proc.stdout)


def load_manifest(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def manifest_run_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    runs = manifest.get("runs") or manifest.get("persona_runs") or []
    return {
        run["research_run_id"]: run
        for run in runs
        if isinstance(run, dict) and isinstance(run.get("research_run_id"), str)
    }


def sessions_send(payload: dict[str, Any]) -> dict[str, Any]:
    payload_json = json.dumps(payload, separators=(",", ":"))
    proc = subprocess.run(
        ["node", str(SESSIONS_SEND_HELPER), "--payload-json", payload_json],
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "sessions.send helper failed")
    return parse_json_lines(proc.stdout)


def apply_patch(patch_payload: dict[str, Any], db_url: str) -> dict[str, Any]:
    cmd = [
        sys.executable,
        str(UPDATE_RUN),
        "--research-run-id", patch_payload["research_run_id"],
        "--status", patch_payload["status"],
        "--workspace-note-path", patch_payload["workspace_note_path"],
        "--notes-json", json.dumps(patch_payload.get("notes", {}), separators=(",", ":")),
    ]
    if patch_payload.get("mark_started"):
        cmd.append("--mark-started")
    if db_url:
        cmd.extend(["--db-url", db_url])
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "update_research_run.py failed")
    return parse_json_lines(proc.stdout)


def runtime_loop_status() -> dict[str, Any]:
    pid_file = RUNTIME_LOOP_PID
    if not pid_file.exists():
        return {"active": False}
    try:
        pid = int(pid_file.read_text().strip())
    except Exception:
        return {"active": False, "stale_pid_file": True}
    try:
        os.kill(pid, 0)
    except OSError:
        return {"active": False, "pid": pid, "stale_pid_file": True}
    return {"active": True, "pid": pid, "pid_file": str(pid_file)}


def ensure_runtime_loop(db_url: str) -> dict[str, Any]:
    status = runtime_loop_status()
    if status.get("active"):
        return {"status": "already_running", **status, "error_file": str(RUNTIME_LOOP_ERROR)}
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    if db_url:
        env.setdefault("PREDQUANT_ORCHESTRATOR_URL", db_url)
    cmd = [
        sys.executable,
        str(RUNTIME_LOOP),
        "--db-url", db_url,
        "--pid-file", str(RUNTIME_LOOP_PID),
        "--error-file", str(RUNTIME_LOOP_ERROR),
    ]
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        start_new_session=True,
        env=env,
    )
    return {
        "status": "started",
        "pid": proc.pid,
        "pid_file": str(RUNTIME_LOOP_PID),
        "error_file": str(RUNTIME_LOOP_ERROR),
    }


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    try:
        manifest_path = Path(args.manifest_path).expanduser().resolve()
        manifest = load_manifest(manifest_path)
        run_map = manifest_run_map(manifest)

        bootstrap = python_json(BOOTSTRAP_TOPICS, ["--manifest-path", str(manifest_path), "--apply"])
        steps = ((bootstrap.get("parallel_handoff_group") or {}).get("steps") or [])

        delivered_results: list[dict[str, Any]] = []
        failures: list[dict[str, Any]] = []

        for step in steps:
            research_run_id = step["research_run_id"]
            persona = step["persona"]
            internal = step.get("internal_handoff_step") or {}
            payload = internal.get("payload")
            delivered_template = dict(step.get("delivered_result_template") or {})
            run_info = run_map.get(research_run_id) or {}

            if not payload:
                failures.append({
                    "research_run_id": research_run_id,
                    "persona": persona,
                    "status": "failed",
                    "error": "missing_sessions_send_payload",
                })
                continue

            try:
                send_result = sessions_send(payload)
                run_status = send_result.get("status")
                if run_status not in {"ok", "done", "success", "timeout", "started"}:
                    raise RuntimeError(f"unexpected sessions_send status: {run_status}")

                target_session_key = payload.get("sessionKey")
                if not target_session_key:
                    raise RuntimeError("sessions_send payload missing sessionKey")

                patch_payload = python_json(
                    RUNTIME_HELPER,
                    [
                        "--file", str(manifest_path),
                        "--action", "build-patch",
                        "--research-run-id", research_run_id,
                        "--target-session-key", target_session_key,
                        "--delivery-chat-id", delivered_template.get("delivery_chat_id") or "",
                        "--delivery-topic-id", delivered_template.get("delivery_topic_id") or "",
                        "--delivery-topic-title", delivered_template.get("delivery_topic_title") or "",
                        "--controller-topic-id", delivered_template.get("controller_topic_id") or "",
                        "--controller-topic-title", delivered_template.get("controller_topic_title") or "",
                    ],
                )
                patch_result = apply_patch(patch_payload, args.db_url)

                delivered = dict(delivered_template)
                delivered.update(
                    {
                        "status": "delivered",
                        "target_session_key": target_session_key,
                        "workspace_note_path": run_info.get("workspace_note_path"),
                        "sessions_send_result": send_result,
                        "patch_result": patch_result,
                    }
                )
                delivered_results.append(delivered)
            except Exception as exc:  # noqa: BLE001
                failures.append(
                    {
                        "research_run_id": research_run_id,
                        "persona": persona,
                        "status": "failed",
                        "workspace_note_path": run_info.get("workspace_note_path"),
                        "error": str(exc),
                    }
                )

        summary = python_json(
            RUNTIME_HELPER,
            [
                "--file", str(manifest_path),
                "--action", "finalize-summary",
                "--run-results-json", json.dumps(delivered_results + failures, separators=(",", ":")),
            ],
        )

        runtime_loop = None
        if delivered_results:
            runtime_loop = ensure_runtime_loop(args.db_url)

        result = {
            "status": "ok",
            "manifest_path": str(manifest_path),
            "bootstrap": bootstrap,
            "delivered_results": delivered_results,
            "failures": failures,
            "summary": summary,
            "runtime_loop": runtime_loop,
        }
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(result, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
