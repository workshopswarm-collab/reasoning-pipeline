#!/usr/bin/env python3
from __future__ import annotations

"""Plan or apply Telegram forum-topic bootstrap for a dispatch manifest.

This helper bridges the remaining runtime seam between a planner-emitted logical
Telegram-target manifest and the actual fresh-topic execution model.

Default mode is non-destructive planning:
- load current run state from Postgres
- prepare launchable runs with runtime_execute_dispatch.py
- determine whether controller/persona topics can be reused
- emit topic-create commands plus exact topic-session handoff payloads when topic ids are known

With --apply it will create missing Telegram topics via the installed
Telegram forum-topic provider API, then emit resolved session keys and handoff payloads.

It does not call `sessions.send` itself.
Visible kickoff commands are emitted for compatibility/debugging, but the canonical lifecycle is that visible start messages are posted automatically when the runtime applies the `queued -> running` DB patch through `update_research_run.py`.
"""

import argparse
import json
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR.parent
RUNTIME_DIR = SCRIPTS_DIR.parent
LOAD_EXISTING = BASE_DIR / "load_dispatch_existing_state.py"
RUNTIME_EXECUTE = BASE_DIR / "runtime_execute_dispatch.py"
TELEGRAM_TOPIC_CREATE = BASE_DIR / "telegram_topic_create.py"
DEFAULT_CHAT_ID = "-1003846500961"
SESSION_KEY_TEMPLATE = "agent:main:telegram:group:{chat_id}:topic:{topic_id}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Plan or apply Telegram topic bootstrap for a dispatch manifest")
    parser.add_argument("--manifest-path", required=True, help="Path to dispatch manifest JSON")
    parser.add_argument("--apply", action="store_true", help="Create missing Telegram topics")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def python_json(script: Path, args: list[str], stdin_json: dict | None = None) -> dict:
    proc = subprocess.run(
        [sys.executable, str(script), *args],
        input=(json.dumps(stdin_json) if stdin_json is not None else None),
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"{script.name} failed")
    out = proc.stdout.strip()
    if not out:
        return {}
    return json.loads(out.splitlines()[-1])


def create_forum_topic(chat_id: str, title: str) -> dict:
    return python_json(TELEGRAM_TOPIC_CREATE, ["--chat-id", chat_id, "--title", title])


def load_manifest(path: str) -> dict:
    return json.loads(Path(path).read_text())


def write_manifest(path: str, manifest: dict) -> None:
    target = Path(path)
    target.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def research_run_ids(manifest: dict) -> list[str]:
    return [run["research_run_id"] for run in manifest.get("runs", [])]


def load_existing_map(ids: list[str]) -> dict:
    if not ids:
        return {}
    return python_json(LOAD_EXISTING, [], {"research_run_ids": ids})


def prepare_launchable(manifest: dict, existing_map: dict) -> dict:
    return python_json(
        RUNTIME_EXECUTE,
        ["--action", "prepare", "--existing-map-json", json.dumps(existing_map)],
        manifest,
    )


def manifest_bootstrap_state(manifest: dict) -> dict:
    raw = manifest.get("bootstrap_state")
    return raw if isinstance(raw, dict) else {}


def existing_controller_info(existing_map: dict, manifest: dict) -> tuple[str | None, str | None]:
    for entry in existing_map.values():
        notes = entry.get("notes") or {}
        topic_id = entry.get("controller_topic_id") or notes.get("controller_topic_id")
        topic_title = entry.get("controller_topic_title") or notes.get("controller_topic_title")
        if topic_id:
            return str(topic_id), (str(topic_title) if topic_title else None)
    bootstrap = manifest_bootstrap_state(manifest)
    controller = bootstrap.get("controller_topic") if isinstance(bootstrap.get("controller_topic"), dict) else {}
    topic_id = controller.get("topic_id")
    topic_title = controller.get("topic_title")
    if topic_id:
        return str(topic_id), (str(topic_title) if topic_title else None)
    return None, None


def existing_persona_topic_info(existing: dict, manifest: dict, research_run_id: str, target: dict) -> tuple[str | None, str | None]:
    notes = existing.get("notes") or {}
    topic_id = existing.get("delivery_target_topic_id") or notes.get("delivery_target_topic_id")
    topic_title = existing.get("delivery_target_topic_title") or notes.get("delivery_target_topic_title") or target.get("topic_title")
    if topic_id:
        return (str(topic_id) if topic_id else None), (str(topic_title) if topic_title else None)
    bootstrap = manifest_bootstrap_state(manifest)
    runs = bootstrap.get("runs") if isinstance(bootstrap.get("runs"), dict) else {}
    run_state = runs.get(research_run_id) if isinstance(runs.get(research_run_id), dict) else {}
    topic_id = run_state.get("topic_id")
    topic_title = run_state.get("topic_title") or target.get("topic_title")
    return (str(topic_id) if topic_id else None), (str(topic_title) if topic_title else None)


def build_thread_create_cmd(*, chat_id: str, title: str) -> list[str]:
    return [
        sys.executable,
        str(TELEGRAM_TOPIC_CREATE),
        "--chat-id",
        str(chat_id),
        "--title",
        title,
    ]


def parse_created_topic(result: dict) -> tuple[str, str]:
    payload = result.get("payload") or result
    # support both direct and nested shapes
    topic_id = (
        payload.get("topicId")
        or payload.get("threadId")
        or payload.get("messageThreadId")
        or (payload.get("thread") or {}).get("id")
        or (payload.get("thread") or {}).get("threadId")
    )
    title = payload.get("name") or payload.get("threadName") or payload.get("title")
    if topic_id is None:
        raise ValueError(f"could not determine created topic id from result: {result}")
    return str(topic_id), (str(title) if title else "")


def build_session_key(chat_id: str, topic_id: str) -> str:
    return SESSION_KEY_TEMPLATE.format(chat_id=chat_id, topic_id=topic_id)


def materialize_sessions_send_payload(payload_template: dict, session_key: str) -> dict:
    payload = dict(payload_template)
    payload["sessionKey"] = session_key
    payload.pop("chatId", None)
    payload.pop("topicTitle", None)
    return payload


def build_visible_send_command(*, chat_id: str, topic_id: str, message: str) -> str:
    return " ".join(
        [
            "openclaw", "message", "send",
            "--channel", "telegram",
            "--target", shlex.quote(str(chat_id)),
            "--thread-id", shlex.quote(str(topic_id)),
            "--message", shlex.quote(message),
            "--json",
        ]
    )


def main() -> int:
    args = parse_args()
    try:
        manifest = load_manifest(args.manifest_path)
        ids = research_run_ids(manifest)
        existing_map = load_existing_map(ids)
        prepare = prepare_launchable(manifest, existing_map)
        launchable = prepare.get("launchable_runs") or []

        runtime_defaults = manifest.get("runtime_defaults") or {}
        chat_id = str(runtime_defaults.get("chat_id") or DEFAULT_CHAT_ID)
        controller_title = str(runtime_defaults.get("controller_topic_title") or f"{manifest.get('case', {}).get('case_key', 'case')} | controller")

        controller_topic_id, controller_topic_title = existing_controller_info(existing_map, manifest)
        controller_action = "reuse" if controller_topic_id else "create"
        controller_command = None
        if controller_action == "create":
            controller_command = build_thread_create_cmd(chat_id=chat_id, title=controller_title)
            if args.apply:
                created = create_forum_topic(chat_id, controller_title)
                controller_topic_id, created_title = parse_created_topic(created)
                controller_topic_title = created_title or controller_title
        else:
            controller_topic_title = controller_topic_title or controller_title

        controller_visible_message = (
            f"SWARM LAUNCH | case_key={(manifest.get('case') or {}).get('case_key')} "
            f"| market={(manifest.get('market') or {}).get('title')} "
            f"| dispatch_id={manifest.get('dispatch_id')}"
        )
        controller_visible_send_command = (
            build_visible_send_command(chat_id=chat_id, topic_id=controller_topic_id, message=controller_visible_message)
            if controller_topic_id else None
        )

        run_plans: list[dict[str, Any]] = []
        for run in launchable:
            research_run_id = run["research_run_id"]
            target = run["target"]
            payload_template = run["handoff_payload"]
            existing = existing_map.get(research_run_id) or {}
            topic_id, topic_title = existing_persona_topic_info(existing, manifest, research_run_id, target)
            action = "reuse" if topic_id else "create"
            create_command = None
            if action == "create":
                create_command = build_thread_create_cmd(chat_id=str(target["chat_id"]), title=str(target["topic_title"]))
                if args.apply:
                    created = create_forum_topic(str(target["chat_id"]), str(target["topic_title"]))
                    topic_id, created_title = parse_created_topic(created)
                    topic_title = created_title or str(target["topic_title"])
            else:
                topic_title = topic_title or str(target["topic_title"])

            session_key = build_session_key(str(target["chat_id"]), topic_id) if topic_id else None
            visible_kickoff_message = (
                ((run.get("post_handoff_update_template") or {}).get("notes") or {}).get("expected_start_marker")
                or ((run.get("post_handoff_update_template") or {}).get("notes") or {}).get("start_marker")
                or f"STARTING RESEARCH | persona={run['persona']} | research_run_id={research_run_id}"
            )
            visible_kickoff_command = (
                build_visible_send_command(chat_id=str(target["chat_id"]), topic_id=topic_id, message=visible_kickoff_message)
                if topic_id else None
            )
            run_plan = {
                "research_run_id": research_run_id,
                "persona": run["persona"],
                "chat_id": str(target["chat_id"]),
                "topic_title": topic_title,
                "controller_topic_title": controller_topic_title,
                "controller_topic_id": controller_topic_id,
                "topic_action": action,
                "create_topic_command": create_command,
                "topic_id": topic_id,
                "session_key": session_key,
                "visible_kickoff_message": visible_kickoff_message,
                "visible_kickoff_command": visible_kickoff_command,
                "visible_finish_message": ((run.get("post_handoff_update_template") or {}).get("notes") or {}).get("expected_finish_marker"),
                "sessions_send_payload": materialize_sessions_send_payload(payload_template, session_key) if session_key else None,
                "delivered_result_template": {
                    "research_run_id": research_run_id,
                    "persona": run["persona"],
                    "status": "delivered",
                    "target_session_key": session_key,
                    "delivery_chat_id": str(target["chat_id"]),
                    "delivery_topic_id": topic_id,
                    "delivery_topic_title": topic_title,
                    "controller_topic_id": controller_topic_id,
                    "controller_topic_title": controller_topic_title,
                    "error": None,
                } if session_key else None,
            }
            run_plans.append(run_plan)

        parallel_steps = []
        for run in run_plans:
            if run.get("sessions_send_payload"):
                parallel_steps.append(
                    {
                        "research_run_id": run["research_run_id"],
                        "persona": run["persona"],
                        "visible_kickoff_step": {
                            "tool": "exec",
                            "command": run.get("visible_kickoff_command"),
                            "description": "Visible Telegram kickoff post for the persona topic.",
                        } if run.get("visible_kickoff_command") else None,
                        "internal_handoff_step": {
                            "tool": "sessions_send",
                            "payload": run["sessions_send_payload"],
                        },
                        "delivered_result_template": run.get("delivered_result_template"),
                    }
                )

        if args.apply and controller_topic_id:
            manifest["bootstrap_state"] = {
                "chat_id": chat_id,
                "controller_topic": {
                    "topic_id": controller_topic_id,
                    "topic_title": controller_topic_title,
                },
                "runs": {
                    run["research_run_id"]: {
                        "persona": run["persona"],
                        "topic_id": run.get("topic_id"),
                        "topic_title": run.get("topic_title"),
                        "session_key": run.get("session_key"),
                    }
                    for run in run_plans
                    if run.get("topic_id")
                },
            }
            write_manifest(args.manifest_path, manifest)

        result = {
            "status": "topics_bootstrapped" if args.apply else "bootstrap_plan_ready",
            "dispatch_id": manifest.get("dispatch_id"),
            "case_key": (manifest.get("case") or {}).get("case_key"),
            "chat_id": chat_id,
            "controller_topic": {
                "action": controller_action,
                "topic_title": controller_topic_title,
                "topic_id": controller_topic_id,
                "create_command": controller_command,
                "visible_launch_message": controller_visible_message,
                "visible_launch_command": controller_visible_send_command,
            },
            "launchable_runs": run_plans,
            "parallel_handoff_group": {
                "parallel": True,
                "description": "After topic bootstrap, execute visible Telegram kickoff posts and internal persona handoffs in parallel where possible.",
                "steps": parallel_steps,
            },
            "replay_hint": {
                "script": str(RUNTIME_DIR / "scripts" / "internal" / "run_dispatch_runtime.py"),
                "mode": "replay-results",
                "note": "After executing `sessions.send` for each run, collect delivered_result_template objects with final status/error and feed them into internal/run_dispatch_runtime.py --mode replay-results --handoff-results-json <...>."
            },
        }
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(json.dumps(result, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
