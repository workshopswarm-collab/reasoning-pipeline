#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import relative_to_workspace, telegram_topic_session_key  # noqa: E402
from light_refresh_status import append_stage_event, locked_status, set_overall_status  # noqa: E402

TELEGRAM_TOPIC_CREATE = (
    Path('/Users/agent2/.openclaw/orchestrator')
    / 'roles'
    / 'orchestrator'
    / 'researchers-swarm-subagents'
    / 'runtime'
    / 'scripts'
    / 'internal'
    / 'telegram_topic_create.py'
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Create or reuse a dedicated Telegram light-refresh lane')
    parser.add_argument('--status-file', required=True)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def parse_created_topic(result: dict[str, Any]) -> tuple[str, str]:
    payload = result.get('payload') or result
    topic_id = (
        payload.get('topicId')
        or payload.get('threadId')
        or payload.get('messageThreadId')
        or (payload.get('thread') or {}).get('id')
        or (payload.get('thread') or {}).get('threadId')
    )
    title = payload.get('name') or payload.get('threadName') or payload.get('title') or ''
    if topic_id is None:
        raise ValueError(f'could not determine created topic id from result: {result}')
    return str(topic_id), str(title)


def run_json(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"command failed: {' '.join(cmd)}")
    out = proc.stdout.strip()
    return json.loads(out.splitlines()[-1]) if out else {}


def discover_existing_case_refresh_lane(status_path: Path, *, case_key: str, chat_id: str) -> dict[str, str]:
    refresh_root = status_path.parent.parent
    if not refresh_root.exists():
        return {}
    candidates = []
    for candidate in sorted(refresh_root.glob('*/light-refresh-status.json'), key=lambda p: p.stat().st_mtime, reverse=True):
        if candidate.resolve() == status_path.resolve():
            continue
        try:
            payload = json.loads(candidate.read_text())
        except Exception:
            continue
        if str(payload.get('case_key') or '').strip() != case_key:
            continue
        if str(payload.get('refresh_target_chat_id') or '').strip() != chat_id:
            continue
        topic_id = str(payload.get('refresh_lane_topic_id') or '').strip()
        session_key = str(payload.get('refresh_lane_session_key') or '').strip()
        if topic_id and session_key:
            candidates.append({
                'topic_id': topic_id,
                'session_key': session_key,
                'topic_title': str(payload.get('refresh_lane_topic_title') or '').strip(),
                'status_path': relative_to_workspace(candidate),
            })
    return candidates[0] if candidates else {}


def main() -> None:
    args = parse_args()
    status_path = Path(args.status_file).expanduser().resolve()

    with locked_status(status_path) as status:
        existing_topic_id = status.get('refresh_lane_topic_id') or ''
        existing_session_key = status.get('refresh_lane_session_key') or ''
        if existing_topic_id and existing_session_key:
            append_stage_event(
                status,
                stage='refresh_lane_bootstrap',
                state='reused',
                message='Reused existing light-refresh Telegram lane',
                extra={'topic_id': existing_topic_id, 'session_key': existing_session_key},
            )
            print(json.dumps({
                'ok': True,
                'action': 'reused',
                'status_file': relative_to_workspace(status_path),
                'topic_id': existing_topic_id,
                'session_key': existing_session_key,
                'topic_title': status.get('refresh_lane_topic_title', ''),
            }, indent=2 if args.pretty else None))
            return

        chat_id = str(status.get('refresh_target_chat_id') or status.get('decision_target_chat_id') or '').strip()
        if not chat_id:
            set_overall_status(status, status.get('status', 'refresh_pending'), stage='refresh_lane_bootstrap', message='Missing refresh_target_chat_id; cannot create dedicated light-refresh lane')
            raise SystemExit('missing refresh_target_chat_id')

        case_key = str(status.get('case_key') or 'case').strip()
        existing_case_lane = discover_existing_case_refresh_lane(status_path, case_key=case_key, chat_id=chat_id)
        if existing_case_lane:
            status.update({
                'refresh_lane_topic_id': existing_case_lane['topic_id'],
                'refresh_lane_topic_title': existing_case_lane.get('topic_title', ''),
                'refresh_lane_session_key': existing_case_lane['session_key'],
                'refresh_target_topic_id': existing_case_lane['topic_id'],
                'refresh_target_topic_title': existing_case_lane.get('topic_title', ''),
                'refresh_target_session_key': existing_case_lane['session_key'],
            })
            append_stage_event(
                status,
                stage='refresh_lane_bootstrap',
                state='reused',
                message='Reused existing case-level light-refresh Telegram lane',
                extra={
                    'topic_id': existing_case_lane['topic_id'],
                    'session_key': existing_case_lane['session_key'],
                    'source_status_path': existing_case_lane.get('status_path', ''),
                },
            )
            print(json.dumps({
                'ok': True,
                'action': 'reused-case-lane',
                'status_file': relative_to_workspace(status_path),
                'topic_id': existing_case_lane['topic_id'],
                'session_key': existing_case_lane['session_key'],
                'topic_title': existing_case_lane.get('topic_title', ''),
            }, indent=2 if args.pretty else None))
            return

        title = f"{case_key} | refresh"

    created = run_json([sys.executable, str(TELEGRAM_TOPIC_CREATE), '--chat-id', chat_id, '--title', title])
    topic_id, created_title = parse_created_topic(created)
    topic_title = created_title or title
    session_key = telegram_topic_session_key(chat_id, topic_id)

    with locked_status(status_path) as status:
        if status.get('refresh_lane_topic_id') and status.get('refresh_lane_session_key'):
            append_stage_event(
                status,
                stage='refresh_lane_bootstrap',
                state='reused',
                message='Another process already created the light-refresh Telegram lane',
                extra={
                    'topic_id': status.get('refresh_lane_topic_id'),
                    'session_key': status.get('refresh_lane_session_key'),
                },
            )
            print(json.dumps({
                'ok': True,
                'action': 'reused-after-race',
                'status_file': relative_to_workspace(status_path),
                'topic_id': status.get('refresh_lane_topic_id'),
                'session_key': status.get('refresh_lane_session_key'),
                'topic_title': status.get('refresh_lane_topic_title', ''),
            }, indent=2 if args.pretty else None))
            return

        status.update({
            'refresh_lane_topic_id': topic_id,
            'refresh_lane_topic_title': topic_title,
            'refresh_lane_session_key': session_key,
            'refresh_target_topic_id': topic_id,
            'refresh_target_topic_title': topic_title,
            'refresh_target_session_key': session_key,
        })
        append_stage_event(
            status,
            stage='refresh_lane_bootstrap',
            state='created',
            message='Created dedicated Telegram light-refresh lane',
            extra={'topic_id': topic_id, 'topic_title': topic_title, 'session_key': session_key},
        )

    print(json.dumps({
        'ok': True,
        'action': 'created',
        'status_file': relative_to_workspace(status_path),
        'chat_id': chat_id,
        'topic_id': topic_id,
        'topic_title': topic_title,
        'session_key': session_key,
    }, indent=2 if args.pretty else None))


if __name__ == '__main__':
    main()
