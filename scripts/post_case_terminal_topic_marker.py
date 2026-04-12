#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any

from case_pipeline_status import (  # type: ignore
    REPO_ROOT,
    load_json_if_exists,
    locked_json_file,
    pipeline_status_path,
    utc_now_iso,
)

DISPATCH_MANIFESTS_DIR = REPO_ROOT / "roles" / "orchestrator" / "researchers-swarm-subagents" / "runtime" / "dispatch-manifests"
TERMINAL_STATUSES = {"pipeline_completed", "pipeline_failed", "pipeline_skipped"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Post a terminal marker into a case Telegram topic when the case is no longer active")
    parser.add_argument("--case-key", required=True)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def load_dispatch_manifest(dispatch_id: str) -> dict[str, Any]:
    if not dispatch_id:
        return {}
    path = DISPATCH_MANIFESTS_DIR / f"{dispatch_id}.json"
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def first_present(*values: Any) -> str:
    for value in values:
        text = str(value or '').strip()
        if text:
            return text
    return ''


SESSION_KEY_RE = re.compile(r"agent:main:telegram:group:(-?\d+):topic:(\d+)")


def fallback_topic_binding_from_case(case_key: str) -> tuple[str, str]:
    case_dir = REPO_ROOT / 'qualitative-db' / '40-research' / 'cases' / case_key
    if not case_dir.exists():
        return '', ''
    matches: list[tuple[str, str]] = []
    for path in case_dir.rglob('*'):
        if not path.is_file():
            continue
        try:
            text = path.read_text(errors='ignore')
        except Exception:
            continue
        for match in SESSION_KEY_RE.finditer(text):
            pair = (match.group(1), match.group(2))
            if pair not in matches:
                matches.append(pair)
    return matches[0] if matches else ('', '')


def resolve_topic_binding(manifest: dict[str, Any], case_key: str) -> tuple[str, str]:
    runtime_defaults = manifest.get("runtime_defaults") if isinstance(manifest.get("runtime_defaults"), dict) else {}
    bootstrap_state = manifest.get("bootstrap_state") if isinstance(manifest.get("bootstrap_state"), dict) else {}
    controller = bootstrap_state.get("controller") if isinstance(bootstrap_state.get("controller"), dict) else {}
    delivery = bootstrap_state.get("delivery") if isinstance(bootstrap_state.get("delivery"), dict) else {}
    chat_id = first_present(
        runtime_defaults.get("chat_id"),
        runtime_defaults.get("controller_chat_id"),
        bootstrap_state.get("chat_id"),
        controller.get("chat_id"),
        delivery.get("chat_id"),
    )
    topic_id = first_present(
        bootstrap_state.get("controller_topic_id"),
        controller.get("topic_id"),
        bootstrap_state.get("delivery_topic_id"),
        delivery.get("topic_id"),
    )
    if chat_id and topic_id:
        return chat_id, topic_id
    fallback_chat_id, fallback_topic_id = fallback_topic_binding_from_case(case_key)
    return first_present(chat_id, fallback_chat_id), first_present(topic_id, fallback_topic_id)


def build_message(payload: dict[str, Any]) -> str:
    terminal_summary = payload.get("terminal_summary") if isinstance(payload.get("terminal_summary"), dict) else {}
    status = str(payload.get("status") or "")
    stage = str(payload.get("current_stage") or "")
    reason = str(
        terminal_summary.get("failure_reason")
        or terminal_summary.get("decision_failure_reason")
        or terminal_summary.get("skip_reason")
        or ""
    ).strip()
    market_title = str(payload.get("market_title") or "").strip()
    pieces = [
        "CASE INACTIVE",
        f"case_key={payload.get('case_key', '')}",
        f"status={status}",
    ]
    if stage:
        pieces.append(f"stage={stage}")
    if market_title:
        pieces.append(f"market={market_title}")
    base = " | ".join(pieces)
    if reason:
        return f"{base}\n\nThis topic is no longer active for automation.\nReason: {reason}"
    return f"{base}\n\nThis topic is no longer active for automation."


def send_terminal_marker(*, chat_id: str, topic_id: str, message: str) -> dict[str, Any]:
    proc = subprocess.run(
        [
            "openclaw", "message", "send",
            "--channel", "telegram",
            "--target", str(chat_id),
            "--thread-id", str(topic_id),
            "--message", message,
            "--json",
        ],
        cwd=str(REPO_ROOT),
        text=True,
        capture_output=True,
    )
    stdout = (proc.stdout or "").strip()
    parsed: dict[str, Any] = {}
    if stdout:
        try:
            maybe = json.loads(stdout.splitlines()[-1])
            if isinstance(maybe, dict):
                parsed = maybe
        except Exception:
            parsed = {"raw_stdout": stdout[-1000:]}
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or stdout or "openclaw message send failed")
    return parsed


def main() -> int:
    args = parse_args()
    status_path = pipeline_status_path(args.case_key)
    payload = load_json_if_exists(status_path)
    if not payload:
        raise SystemExit(f"missing pipeline status for {args.case_key}")
    status = str(payload.get("status") or "")
    terminal_summary = payload.get("terminal_summary") if isinstance(payload.get("terminal_summary"), dict) else {}
    if status not in TERMINAL_STATUSES:
        print(json.dumps({"ok": True, "noop": True, "reason": f"status_not_terminal:{status}", "case_key": args.case_key}, indent=2 if args.pretty else None))
        return 0
    if terminal_summary.get("topic_terminal_marker_posted_at") and not args.force:
        print(json.dumps({"ok": True, "noop": True, "reason": "already_posted", "case_key": args.case_key}, indent=2 if args.pretty else None))
        return 0

    dispatch_id = str(payload.get("dispatch_id") or "")
    manifest = load_dispatch_manifest(dispatch_id)
    chat_id, topic_id = resolve_topic_binding(manifest, args.case_key)
    if not chat_id or not topic_id:
        print(json.dumps({
            "ok": True,
            "noop": True,
            "reason": "missing_topic_binding",
            "case_key": args.case_key,
            "dispatch_id": dispatch_id,
        }, indent=2 if args.pretty else None))
        return 0

    message = build_message(payload)
    send_result = send_terminal_marker(chat_id=chat_id, topic_id=topic_id, message=message)

    with locked_json_file(status_path) as current:
        term = current.setdefault("terminal_summary", {})
        term["topic_terminal_marker_posted_at"] = utc_now_iso()
        term["topic_terminal_marker_chat_id"] = chat_id
        term["topic_terminal_marker_topic_id"] = topic_id
        term["topic_terminal_marker_message"] = message
        term["topic_terminal_marker_dispatch_id"] = dispatch_id
        if send_result:
            term["topic_terminal_marker_result"] = send_result

    print(json.dumps({
        "ok": True,
        "case_key": args.case_key,
        "dispatch_id": dispatch_id,
        "chat_id": chat_id,
        "topic_id": topic_id,
        "message": message,
        "send_result": send_result,
    }, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
