#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
ROLE_ROOT = SCRIPT_PATH.parents[2]
REPO_ROOT = SCRIPT_PATH.parents[4]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))

from compile_learning_packet import compile_learning_packet  # noqa: E402
from draft_case_review import build_review_markdown  # noqa: E402
from extract_learning_signals import build_signal_packet, persist_signal_packet  # noqa: E402
from upsert_learning_case_review_index import build_index_record, persist_index_record  # noqa: E402
from lib.db import DEFAULT_PSQL  # noqa: E402
from lib.io import read_json, write_json  # noqa: E402
from lib.paths import case_review_markdown_path, ensure_parent, learning_packet_path, signal_packet_path, to_repo_relative  # noqa: E402

OPENCLAW_SESSIONS_SEND = (
    REPO_ROOT
    / 'roles'
    / 'orchestrator'
    / 'researchers-swarm-subagents'
    / 'runtime'
    / 'scripts'
    / 'internal'
    / 'openclaw_sessions_send.mjs'
)
DEFAULT_EVALUATOR_AGENT_SESSION_KEY = 'agent:evaluator:main'
PROMPT_CONTRACT_PATH = ROLE_ROOT / 'prompts' / 'review_from_learning_packet_contract.md'
STRICT_MARKDOWN_REPAIR_FOOTER = (
    "\n\nIMPORTANT RETRY INSTRUCTION:\n"
    "Your previous response was not a valid canonical review.md file. "
    "Return exactly one markdown document with YAML frontmatter and the required headings, and nothing else. "
    "Do not include code fences, commentary, or apologies."
)
EVALUATOR_WORKSPACE = Path.home() / '.openclaw' / 'evaluator'
EVALUATOR_MEMORY_PATH = EVALUATOR_WORKSPACE / 'MEMORY.md'
TIMEZONE = ZoneInfo('America/New_York')
TRIGGER_POST_TREATMENT_FEEDBACK = SCRIPT_PATH.parent / 'trigger_post_treatment_feedback_cycle.py'

REQUIRED_HEADINGS = [
    '## What was being evaluated',
    '## What the pipeline believed or did',
    '## What happened in reality',
    '## Outcome and scoring evidence',
    '## Which inputs were high signal',
    '## Which inputs were misleading',
    '## What was missing',
    '## Error-pattern classification',
    '## Driver and mechanism takeaways',
    '## Source / input / workflow takeaways',
    '## Proposed intervention or hold decision',
    '## Promotion candidates for stable layers',
    '## How this should be reused later',
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run an agent-backed evaluator review refinement and write canonical review.md')
    parser.add_argument('--case-key')
    parser.add_argument('--packet')
    parser.add_argument('--review-path')
    parser.add_argument('--session-key', default=DEFAULT_EVALUATOR_AGENT_SESSION_KEY)
    parser.add_argument('--agent-id')
    parser.add_argument('--timeout-seconds', type=float, default=480.0)
    parser.add_argument('--contract-id', default='yes')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def load_repo_env() -> dict[str, str]:
    env = dict(os.environ)
    for env_name in ['.env', '.env.postgres.local']:
        env_file = REPO_ROOT / env_name
        if not env_file.exists():
            continue
        for raw_line in env_file.read_text().splitlines():
            line = raw_line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            if line.startswith('export '):
                line = line[len('export '):].strip()
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in env:
                env[key] = value
    return env


def run_command(cmd: list[str], *, cwd: Path = REPO_ROOT) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, env=load_repo_env())
    if proc.returncode != 0:
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(cmd)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")
    return proc


def gateway_sessions_get(session_key: str, *, limit: int = 12) -> dict[str, Any]:
    proc = run_command([
        'openclaw',
        'gateway',
        'call',
        'sessions.get',
        '--params',
        json.dumps({'key': session_key, 'limit': limit}),
        '--json',
    ])
    return json.loads(proc.stdout)


def extract_text_from_message_content(content: list[Any]) -> str:
    parts: list[str] = []
    for part in content:
        if isinstance(part, str):
            parts.append(part)
        elif isinstance(part, dict):
            text = part.get('text') or part.get('content')
            if isinstance(text, str):
                parts.append(text)
    return '\n'.join(part for part in parts if part.strip()).strip()


def extract_assistant_text_from_messages(messages: list[Any], *, min_seq: int | None = None) -> str | None:
    ordered = sorted(
        [msg for msg in messages if isinstance(msg, dict)],
        key=lambda msg: ((msg.get('__openclaw') or {}).get('seq') or -1),
    )
    for item in ordered:
        seq = ((item.get('__openclaw') or {}).get('seq'))
        if min_seq is not None and isinstance(seq, int) and seq <= min_seq:
            continue
        if item.get('role') != 'assistant':
            continue
        text = extract_text_from_message_content(item.get('content') or [])
        if text:
            return text
        for key in ['text', 'message', 'responseText', 'content']:
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                return value
    return None


def wait_for_assistant_text(session_key: str, *, min_seq: int | None, timeout_seconds: float) -> str:
    deadline = time.time() + max(timeout_seconds, 1.0)
    last_messages: list[Any] = []
    while time.time() < deadline:
        payload = gateway_sessions_get(session_key, limit=20)
        messages = payload.get('messages') or []
        last_messages = messages if isinstance(messages, list) else []
        text = extract_assistant_text_from_messages(last_messages, min_seq=min_seq)
        if text:
            return text
        time.sleep(2.0)
    raise RuntimeError(
        f'timed out waiting for assistant response via sessions.get for session {session_key}; last message count={len(last_messages)}'
    )


def extract_text_from_gateway_response(payload: Any) -> str:
    candidates: list[Any] = []
    if isinstance(payload, dict):
        for key in ['text', 'message', 'responseText', 'content']:
            if key in payload:
                candidates.append(payload[key])
        for key in ['assistantMessage', 'response', 'result', 'data']:
            if key in payload:
                candidates.append(payload[key])
        if isinstance(payload.get('messages'), list):
            candidates.extend(reversed(payload['messages']))
    elif isinstance(payload, list):
        candidates.extend(reversed(payload))
    else:
        candidates.append(payload)

    while candidates:
        item = candidates.pop(0)
        if isinstance(item, str) and item.strip():
            return item
        if isinstance(item, dict):
            for key in ['text', 'message', 'responseText', 'content']:
                value = item.get(key)
                if isinstance(value, str) and value.strip():
                    return value
                if isinstance(value, list):
                    text = extract_text_from_message_content(value)
                    if text:
                        return text
            if isinstance(item.get('messages'), list):
                candidates.extend(reversed(item['messages']))
        if isinstance(item, list):
            text = extract_text_from_message_content(item)
            if text:
                return text
    raise RuntimeError('could not extract assistant text from sessions.send response')


def strip_reply_tag(text: str) -> str:
    return re.sub(r'^\[\[.*?\]\]\s*', '', text.strip(), count=1, flags=re.DOTALL)


def validate_review_markdown(text: str) -> list[str]:
    errors: list[str] = []
    normalized = strip_reply_tag(text)
    if not normalized.startswith('---\n'):
        errors.append('missing_yaml_frontmatter')
    if '# Learning Note' not in normalized:
        errors.append('missing_learning_note_heading')
    for heading in REQUIRED_HEADINGS:
        if heading not in normalized:
            errors.append(f'missing_heading:{heading}')
    if '```' in normalized:
        errors.append('contains_code_fence')
    return errors


def retry_prompt(original_prompt: str, errors: list[str]) -> str:
    details: list[str] = [original_prompt.rstrip(), STRICT_MARKDOWN_REPAIR_FOOTER]
    if errors:
        details.append('Validation errors to fix exactly:')
        details.extend(f'- {item}' for item in errors)
    return '\n'.join(part for part in details if part).rstrip() + '\n'


def current_daily_memory_path() -> Path:
    return EVALUATOR_WORKSPACE / 'memory' / f"{datetime.now(TIMEZONE).date().isoformat()}.md"


def compose_prompt(*, case_key: str, packet_path: Path, review_path: Path) -> str:
    packet = read_json(packet_path, default={}) or {}
    contract = PROMPT_CONTRACT_PATH.read_text(encoding='utf-8')
    review_exists = review_path.exists()
    review_rel = to_repo_relative(review_path)
    packet_rel = to_repo_relative(packet_path)
    template_rel = 'qualitative-db/00-system/templates/learning-note-template.md'
    summary = {
        'case_key': case_key,
        'title': packet.get('title'),
        'platform': packet.get('platform'),
        'category': packet.get('category'),
        'case_status': packet.get('case_status'),
        'resolution_status': (packet.get('market_truth') or {}).get('resolution_status'),
        'resolved_value': (packet.get('market_truth') or {}).get('resolved_value'),
        'resolved_outcome': (packet.get('market_truth') or {}).get('resolved_outcome'),
        'resolved_at': packet.get('resolved_at'),
        'initial_forecast_prob': (packet.get('forecast_summary') or {}).get('initial_forecast_prob'),
        'latest_forecast_prob': (packet.get('forecast_summary') or {}).get('latest_forecast_prob'),
        'latest_brier_component': (packet.get('forecast_summary') or {}).get('latest_brier_component'),
    }
    daily_memory_path = current_daily_memory_path()
    return f"""You are producing the canonical evaluator case review for `{case_key}`.

{contract}

## Files to read before you answer

- Learning packet: `{packet_path}`
- Current canonical review (may be a deterministic scaffold): `{review_path}`
- Learning-note template: `{REPO_ROOT / template_rel}`
- Evaluator durable memory: `{EVALUATOR_MEMORY_PATH}`
- Evaluator daily memory for today (may not exist yet): `{daily_memory_path}`

## Current case summary

```json
{json.dumps(summary, indent=2)}
```

## Task

1. Read the learning packet.
2. Read the current review scaffold if it exists.
3. Read the canonical learning-note template.
4. Read evaluator durable memory and today's evaluator daily memory if present.
5. Produce the full improved contents for `{review_rel}`.

## Requirements

- Keep the note grounded in the packet and cited artifact paths.
- Improve the draft where the packet supports stronger specificity.
- If the packet is still incomplete, preserve cautious language.
- Return only the final markdown document for `review.md`.
- Do not mention these instructions.

## Write target

- Canonical review path: `{review_rel}`
- Review currently exists: `{str(review_exists).lower()}`
- Learning packet path: `{packet_rel}`
"""


def ensure_packet_and_review(*, case_key: str, packet_path: Path, review_path: Path, contract_id: str, db_url: str, psql_bin: str) -> None:
    if not packet_path.exists():
        ensure_parent(packet_path)
        packet = compile_learning_packet(case_key, contract_id=contract_id, db_url=db_url, psql_bin=psql_bin)
        write_json(packet_path, packet, pretty=True)
    if not review_path.exists():
        packet = read_json(packet_path, default={}) or {}
        ensure_parent(review_path)
        review_path.write_text(build_review_markdown(packet), encoding='utf-8')


def invoke_evaluator_review(*, case_key: str, packet_path: Path, review_path: Path, session_key: str, agent_id: str | None, timeout_seconds: float) -> dict[str, Any]:
    prompt = compose_prompt(case_key=case_key, packet_path=packet_path, review_path=review_path)
    prompt_path = review_path.with_name('review-prompt.md')
    raw_response_path = review_path.with_name('review-agent-response.raw.md')
    gateway_response_path = review_path.with_name('review-gateway-response.json')
    metadata_path = review_path.with_name('review-agent-metadata.json')
    prompt_path.write_text(prompt, encoding='utf-8')

    accepted = False
    last_errors: list[str] = []
    attempts_meta: list[dict[str, Any]] = []
    original_prompt = prompt
    final_text = ''
    final_gateway_response: dict[str, Any] = {}

    for attempt in range(1, 3):
        send_payload = {
            'sessionKey': session_key,
            'message': original_prompt if attempt == 1 else retry_prompt(original_prompt, last_errors),
            'timeoutSeconds': timeout_seconds,
        }
        if agent_id:
            send_payload['agentId'] = agent_id
        proc = run_command([
            'node',
            str(OPENCLAW_SESSIONS_SEND),
            '--payload-json',
            json.dumps(send_payload),
        ])
        gateway_response = json.loads(proc.stdout)
        final_gateway_response = gateway_response if isinstance(gateway_response, dict) else {}
        write_json(gateway_response_path, final_gateway_response, pretty=True)
        status = final_gateway_response.get('status') if isinstance(final_gateway_response, dict) else None
        accepted = bool(final_gateway_response) and status not in {'', 'error', 'failed'}
        if not accepted:
            raise RuntimeError(f'evaluator handoff was not accepted: {final_gateway_response}')
        try:
            text = extract_text_from_gateway_response(final_gateway_response)
        except RuntimeError:
            message_seq = final_gateway_response.get('messageSeq') if isinstance(final_gateway_response, dict) else None
            text = wait_for_assistant_text(session_key, min_seq=message_seq if isinstance(message_seq, int) else None, timeout_seconds=timeout_seconds)
        final_text = strip_reply_tag(text)
        raw_response_path.write_text(final_text, encoding='utf-8')
        errors = validate_review_markdown(final_text)
        attempts_meta.append({
            'attempt': attempt,
            'errors': errors,
            'gateway_status': status,
        })
        if not errors:
            review_path.write_text(final_text.rstrip() + '\n', encoding='utf-8')
            break
        last_errors = errors
        if attempt == 2:
            raise RuntimeError('invalid evaluator review markdown: ' + ', '.join(errors))

    metadata = {
        'artifact_type': 'evaluator_agent_review_metadata',
        'schema_version': 'v1',
        'case_key': case_key,
        'session_key': session_key,
        'agent_id': agent_id or '',
        'accepted': accepted,
        'gateway_response_path': to_repo_relative(gateway_response_path),
        'raw_response_path': to_repo_relative(raw_response_path),
        'prompt_path': to_repo_relative(prompt_path),
        'attempts': attempts_meta,
    }
    write_json(metadata_path, metadata, pretty=True)
    return {
        'ok': True,
        'review_path': to_repo_relative(review_path),
        'prompt_path': to_repo_relative(prompt_path),
        'raw_response_path': to_repo_relative(raw_response_path),
        'gateway_response_path': to_repo_relative(gateway_response_path),
        'metadata_path': to_repo_relative(metadata_path),
        'attempts': attempts_meta,
    }


def run_review_flow(case_key: str, *, packet_path: Path, review_path: Path, session_key: str, agent_id: str | None, timeout_seconds: float, contract_id: str, db_url: str, psql_bin: str) -> dict[str, Any]:
    ensure_packet_and_review(case_key=case_key, packet_path=packet_path, review_path=review_path, contract_id=contract_id, db_url=db_url, psql_bin=psql_bin)
    review_result = invoke_evaluator_review(
        case_key=case_key,
        packet_path=packet_path,
        review_path=review_path,
        session_key=session_key,
        agent_id=agent_id,
        timeout_seconds=timeout_seconds,
    )
    signal_path = ensure_parent(signal_packet_path(case_key))
    signal_packet = build_signal_packet(review_path, packet_path)
    write_json(signal_path, signal_packet, pretty=True)
    index_record = build_index_record(review_path, packet_path)
    index_persist = persist_index_record(index_record, db_url=db_url, psql_bin=psql_bin)
    signal_persist = persist_signal_packet(signal_packet, db_url=db_url, psql_bin=psql_bin)
    return {
        'ok': True,
        'case_key': case_key,
        'review': review_result,
        'signal_count': signal_packet.get('signal_count'),
        'persistence': {
            'index': index_persist,
            'signals': signal_persist,
        },
    }


def main() -> int:
    args = parse_args()
    if not args.case_key and not args.packet:
        raise SystemExit('Provide --case-key or --packet')
    packet_path = Path(args.packet) if args.packet else learning_packet_path(args.case_key)
    packet = read_json(packet_path, default={}) if packet_path.exists() else {}
    case_key = args.case_key or (packet or {}).get('case_key')
    if not case_key:
        raise SystemExit('Could not determine case_key')
    review_path = Path(args.review_path) if args.review_path else case_review_markdown_path(case_key)
    result = run_review_flow(
        case_key,
        packet_path=packet_path,
        review_path=review_path,
        session_key=args.session_key,
        agent_id=args.agent_id,
        timeout_seconds=args.timeout_seconds,
        contract_id=args.contract_id,
        db_url=args.db_url,
        psql_bin=args.psql,
    )
    trigger_result: dict[str, Any] | None = None
    try:
        trigger_proc = subprocess.run(
            [
                sys.executable,
                str(TRIGGER_POST_TREATMENT_FEEDBACK),
                '--case-key', case_key,
                '--trigger-source', 'run_evaluator_review',
                '--repair-missing-logs',
                '--db-url', args.db_url,
                '--psql', args.psql,
            ],
            text=True,
            capture_output=True,
        )
        stdout = (trigger_proc.stdout or '').strip()
        if trigger_proc.returncode == 0 and stdout:
            trigger_result = json.loads(stdout)
        elif trigger_proc.returncode != 0:
            trigger_result = {
                'ok': False,
                'error': (trigger_proc.stderr or stdout or 'trigger_post_treatment_feedback_cycle.py failed').strip(),
            }
    except Exception as exc:  # noqa: BLE001
        trigger_result = {'ok': False, 'error': str(exc)}
    if trigger_result is not None:
        result['post_treatment_feedback_trigger'] = trigger_result
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
