#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
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

from run_evaluator_review import (  # noqa: E402
    DEFAULT_EVALUATOR_AGENT_SESSION_KEY,
    OPENCLAW_SESSIONS_SEND,
    extract_text_from_gateway_response,
    run_command,
    strip_reply_tag,
    wait_for_assistant_text,
)
from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url  # noqa: E402
from lib.io import read_json, write_json  # noqa: E402
from lib.paths import case_review_dir, case_review_markdown_path, learning_packet_path, signal_packet_path, to_repo_relative  # noqa: E402
from upsert_learning_case_review_index import build_index_record  # noqa: E402

PROMPT_CONTRACT_PATH = ROLE_ROOT / 'prompts' / 'memory_upgrade_from_review_contract.md'
EVALUATOR_WORKSPACE = Path.home() / '.openclaw' / 'evaluator'
EVALUATOR_MEMORY_PATH = EVALUATOR_WORKSPACE / 'MEMORY.md'
EVALUATOR_DAILY_MEMORY_DIR = EVALUATOR_WORKSPACE / 'memory'
TIMEZONE = ZoneInfo('America/New_York')
DAILY_IMPORTANCE_THRESHOLD = 0.70
DURABLE_IMPORTANCE_THRESHOLD = 0.88
DURABLE_MIN_CASE_COUNT = 2
HYBRID_IMPORTANCE_VERSION = 'v2'
BASE_IMPORTANCE = 0.08
REVIEW_STATUS_WEIGHTS = {
    'reviewed': 0.18,
    'active': 0.22,
}
SIGNAL_KIND_WEIGHTS = {
    'workflow_performance': 0.24,
    'driver_pattern': 0.18,
    'missed_signal': 0.16,
    'false_signal': 0.14,
    'source_performance': 0.10,
}

RECURRENCE_SQL = r'''
WITH current_signals AS (
  SELECT DISTINCT signal_kind, signal_key
  FROM public.learning_signal_occurrences
  WHERE case_key = :'case_key'
)
SELECT json_build_object(
  'rows', COALESCE(
    (
      SELECT json_agg(row_to_json(x) ORDER BY x.case_count DESC, x.occurrence_count DESC, x.signal_kind, x.signal_key)
      FROM (
        SELECT
          cs.signal_kind,
          cs.signal_key,
          COUNT(*) AS occurrence_count,
          COUNT(DISTINCT lso.case_key) AS case_count
        FROM current_signals cs
        JOIN public.learning_signal_occurrences lso
          ON lso.signal_kind = cs.signal_kind
         AND lso.signal_key = cs.signal_key
        GROUP BY cs.signal_kind, cs.signal_key
      ) x
    ),
    '[]'::json
  )
)::text;
'''

STRICT_JSON_REPAIR_FOOTER = (
    "\n\nIMPORTANT RETRY INSTRUCTION:\n"
    "Your previous response was not valid JSON for the required memory-upgrade schema. "
    "Return exactly one valid JSON object and nothing else. "
    "Do not include commentary, markdown fences, or apologies."
)


@dataclass
class GateDecision:
    accepted: bool
    destination: str
    reason: str
    candidate: dict[str, Any] | None
    target_path: str | None = None
    recurrence_case_count: int | None = None
    importance: float | None = None
    importance_breakdown: dict[str, Any] | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run importance-gated evaluator memory upgrades from a reviewed case review')
    parser.add_argument('--case-key')
    parser.add_argument('--review-path')
    parser.add_argument('--signal-path')
    parser.add_argument('--packet-path')
    parser.add_argument('--session-key', default=DEFAULT_EVALUATOR_AGENT_SESSION_KEY)
    parser.add_argument('--agent-id')
    parser.add_argument('--timeout-seconds', type=float, default=240.0)
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--ignore-duplicates', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def today_local_date() -> str:
    return datetime.now(TIMEZONE).date().isoformat()


def daily_memory_path() -> Path:
    return EVALUATOR_DAILY_MEMORY_DIR / f'{today_local_date()}.md'


def extract_json_payload(text: str) -> dict[str, Any]:
    stripped = strip_reply_tag(text).strip()
    if not stripped:
        raise RuntimeError('empty evaluator memory-upgrade response')
    if stripped.startswith('```') and stripped.endswith('```'):
        stripped = stripped.strip('`').strip()
    if stripped.startswith('json\n'):
        stripped = stripped[5:]
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        start = stripped.find('{')
        end = stripped.rfind('}')
        if start != -1 and end != -1 and end > start:
            return json.loads(stripped[start:end + 1])
        raise


def recurrence_rows(case_key: str, *, db_url: str = '', psql_bin: str = DEFAULT_PSQL) -> list[dict[str, Any]]:
    payload = exec_sql(psql_bin, resolve_db_url(db_url), RECURRENCE_SQL, {'case_key': case_key})
    return payload.get('rows') or []


def recurrence_lookup(rows: list[dict[str, Any]]) -> dict[tuple[str, str], dict[str, Any]]:
    lookup: dict[tuple[str, str], dict[str, Any]] = {}
    for row in rows:
        kind = str(row.get('signal_kind') or '')
        key = str(row.get('signal_key') or '')
        if kind and key:
            lookup[(kind, key)] = row
    return lookup


def memory_text(path: Path) -> str:
    if not path.exists():
        return ''
    return path.read_text(encoding='utf-8')


def build_prompt(*, case_key: str, review_path: Path, signal_path: Path, packet_path: Path, recurrence: list[dict[str, Any]]) -> str:
    contract = PROMPT_CONTRACT_PATH.read_text(encoding='utf-8')
    index_record = build_index_record(review_path, packet_path)
    current_daily_path = daily_memory_path()
    return f"""You are proposing importance-gated memory upgrades for Evaluator.

{contract}

## Files to read before answering

- Review note: `{review_path}`
- Signal packet: `{signal_path}`
- Learning packet: `{packet_path}`
- Evaluator durable memory: `{EVALUATOR_MEMORY_PATH}`
- Evaluator daily memory for today (may not exist yet): `{current_daily_path}`

## Current review/index status

```json
{json.dumps(index_record, indent=2)}
```

## Recurrence statistics for this case's signal keys

```json
{json.dumps(recurrence, indent=2)}
```

## Task

Propose at most one daily candidate and at most one durable candidate.
Use the exact `signal_kind` and `signal_key` values from the recurrence statistics when anchoring a candidate.
The system will compute the actual importance score deterministically; focus on whether a candidate should exist at all and how it should be described.
If no candidate clearly clears the bar, return `null` for that slot.
Return only the final JSON object.
"""


def validate_candidate(candidate: Any, *, slot: str) -> list[str]:
    errors: list[str] = []
    if candidate is None:
        return errors
    if not isinstance(candidate, dict):
        return [f'{slot}:not_object']
    for key in ['summary', 'duplicate_guard', 'tags', 'why', 'anchor_signal_kind', 'anchor_signal_key']:
        if key not in candidate:
            errors.append(f'{slot}:missing_{key}')
    if 'importance' in candidate:
        errors.append(f'{slot}:importance_field_not_allowed')
    if 'tags' in candidate and not isinstance(candidate.get('tags'), list):
        errors.append(f'{slot}:tags_not_list')
    return errors


def validate_payload(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ['payload_not_object']
    if 'daily_candidate' not in payload:
        errors.append('missing_daily_candidate')
    if 'durable_candidate' not in payload:
        errors.append('missing_durable_candidate')
    errors.extend(validate_candidate(payload.get('daily_candidate'), slot='daily_candidate'))
    errors.extend(validate_candidate(payload.get('durable_candidate'), slot='durable_candidate'))
    return errors


def append_daily_entry(path: Path, candidate: dict[str, Any], *, case_key: str, recurrence_case_count: int | None, importance: float) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = memory_text(path)
    heading = f'## {today_local_date()} evaluator memory upgrades'
    lines: list[str] = []
    if not existing.strip():
        lines.append(heading)
        lines.append('')
    elif heading not in existing:
        lines.append('')
        lines.append(heading)
        lines.append('')
    else:
        lines.append('')
    tags = ', '.join(candidate.get('tags') or [])
    anchor = f"{candidate.get('anchor_signal_kind')}:{candidate.get('anchor_signal_key')}"
    lines.append(f"- guard: `{candidate.get('duplicate_guard')}` | importance: {importance:.2f} | source_case: `{case_key}` | anchor: `{anchor}`")
    lines.append(f"  - summary: {candidate.get('summary')}")
    lines.append(f"  - rationale: {candidate.get('why')}")
    if tags:
        lines.append(f"  - tags: {tags}")
    if recurrence_case_count is not None:
        lines.append(f"  - recurrence_case_count: {recurrence_case_count}")
    path.write_text(existing + '\n'.join(lines).rstrip() + '\n', encoding='utf-8')


def append_durable_entry(path: Path, candidate: dict[str, Any], *, case_key: str, recurrence_case_count: int | None, importance: float) -> None:
    existing = memory_text(path)
    heading = '## Importance-gated learned rules'
    lines: list[str] = []
    if not existing.strip():
        lines.append('# MEMORY.md')
        lines.append('')
        lines.append(heading)
        lines.append('')
    elif heading not in existing:
        lines.append('')
        lines.append(heading)
        lines.append('')
    else:
        lines.append('')
    tags = ', '.join(candidate.get('tags') or [])
    anchor = f"{candidate.get('anchor_signal_kind')}:{candidate.get('anchor_signal_key')}"
    lines.append(f"- guard: `{candidate.get('duplicate_guard')}` | importance: {importance:.2f} | source_case: `{case_key}` | anchor: `{anchor}`")
    lines.append(f"  - summary: {candidate.get('summary')}")
    lines.append(f"  - rationale: {candidate.get('why')}")
    if tags:
        lines.append(f"  - tags: {tags}")
    if recurrence_case_count is not None:
        lines.append(f"  - recurrence_case_count: {recurrence_case_count}")
    path.write_text(existing + '\n'.join(lines).rstrip() + '\n', encoding='utf-8')


def duplicate_exists(target_path: Path, duplicate_guard: str) -> bool:
    if not target_path.exists() or not duplicate_guard.strip():
        return False
    return duplicate_guard in target_path.read_text(encoding='utf-8')


def review_is_agent_authored(case_key: str) -> bool:
    return (case_review_dir(case_key) / 'review-agent-metadata.json').exists()


def recurrence_case_score(case_count: int) -> float:
    if case_count >= 4:
        return 0.30
    if case_count == 3:
        return 0.24
    if case_count == 2:
        return 0.18
    if case_count == 1:
        return 0.08
    return 0.0


def recurrence_occurrence_score(occurrence_count: int) -> float:
    if occurrence_count >= 5:
        return 0.08
    if occurrence_count >= 3:
        return 0.05
    if occurrence_count >= 2:
        return 0.03
    return 0.0


def signal_richness_score(signal_count: int) -> float:
    if signal_count >= 30:
        return 0.08
    if signal_count >= 15:
        return 0.05
    if signal_count >= 8:
        return 0.03
    return 0.0


def similar_rule_penalty(candidate: dict[str, Any]) -> float:
    anchor_key = str(candidate.get('anchor_signal_key') or '').strip()
    anchor_kind = str(candidate.get('anchor_signal_kind') or '').strip()
    combined = (memory_text(EVALUATOR_MEMORY_PATH) + '\n' + memory_text(daily_memory_path())).lower()
    if not combined:
        return 0.0
    if anchor_key and anchor_key.lower() in combined:
        return -0.08
    if anchor_kind and anchor_kind.lower() in combined:
        return -0.05
    return 0.0


def compute_importance(candidate: dict[str, Any], *, case_key: str, review_status: str, recurrence: dict[tuple[str, str], dict[str, Any]], signal_packet: dict[str, Any]) -> tuple[float, dict[str, Any], int]:
    anchor = recurrence.get((str(candidate.get('anchor_signal_kind') or ''), str(candidate.get('anchor_signal_key') or '')))
    case_count = int(anchor.get('case_count') or 0) if anchor else 0
    occurrence_count = int(anchor.get('occurrence_count') or 0) if anchor else 0
    signal_kind = str(candidate.get('anchor_signal_kind') or '')
    signal_count = int(signal_packet.get('signal_count') or 0)
    breakdown = {
        'version': HYBRID_IMPORTANCE_VERSION,
        'base': BASE_IMPORTANCE,
        'review_status': REVIEW_STATUS_WEIGHTS.get(review_status, 0.0),
        'signal_kind': SIGNAL_KIND_WEIGHTS.get(signal_kind, 0.08),
        'recurrence_case_count': recurrence_case_score(case_count),
        'recurrence_occurrence_count': recurrence_occurrence_score(occurrence_count),
        'agent_review_authored': 0.10 if review_is_agent_authored(case_key) else 0.0,
        'signal_packet_richness': signal_richness_score(signal_count),
        'similar_rule_penalty': similar_rule_penalty(candidate),
    }
    importance = max(0.0, min(1.0, round(sum(float(v) for v in breakdown.values() if isinstance(v, (int, float))), 4)))
    breakdown['computed_importance'] = importance
    breakdown['recurrence_case_count_raw'] = case_count
    breakdown['recurrence_occurrence_count_raw'] = occurrence_count
    breakdown['signal_packet_count_raw'] = signal_count
    return importance, breakdown, case_count


def gate_candidate(candidate: dict[str, Any] | None, *, slot: str, case_key: str, review_status: str, recurrence: dict[tuple[str, str], dict[str, Any]], signal_packet: dict[str, Any], dry_run: bool = False, ignore_duplicates: bool = False) -> GateDecision:
    if candidate is None:
        return GateDecision(False, slot, 'no_candidate', None, importance=0.0, importance_breakdown={'version': HYBRID_IMPORTANCE_VERSION})
    duplicate_guard = str(candidate.get('duplicate_guard') or '').strip()
    importance, breakdown, recurrence_case_count = compute_importance(candidate, case_key=case_key, review_status=review_status, recurrence=recurrence, signal_packet=signal_packet)
    if review_status not in {'reviewed', 'active'}:
        return GateDecision(False, slot, f'review_status_not_promotable:{review_status}', candidate, recurrence_case_count=recurrence_case_count, importance=importance, importance_breakdown=breakdown)
    if not duplicate_guard:
        return GateDecision(False, slot, 'missing_duplicate_guard', candidate, recurrence_case_count=recurrence_case_count, importance=importance, importance_breakdown=breakdown)

    if slot == 'daily':
        target = daily_memory_path()
        if importance < DAILY_IMPORTANCE_THRESHOLD:
            return GateDecision(False, slot, f'importance_below_daily_threshold:{importance:.2f}', candidate, target_path=str(target), recurrence_case_count=recurrence_case_count, importance=importance, importance_breakdown=breakdown)
        if not ignore_duplicates and (duplicate_exists(target, duplicate_guard) or duplicate_exists(EVALUATOR_MEMORY_PATH, duplicate_guard)):
            return GateDecision(False, slot, 'duplicate_guard_exists', candidate, target_path=str(target), recurrence_case_count=recurrence_case_count, importance=importance, importance_breakdown=breakdown)
        return GateDecision(True, slot, 'accepted_dry_run' if dry_run else 'accepted', candidate, target_path=str(target), recurrence_case_count=recurrence_case_count, importance=importance, importance_breakdown=breakdown)

    target = str(EVALUATOR_MEMORY_PATH)
    if importance < DURABLE_IMPORTANCE_THRESHOLD:
        return GateDecision(False, slot, f'importance_below_durable_threshold:{importance:.2f}', candidate, target_path=target, recurrence_case_count=recurrence_case_count, importance=importance, importance_breakdown=breakdown)
    if recurrence_case_count < DURABLE_MIN_CASE_COUNT:
        return GateDecision(False, slot, f'recurrence_case_count_below_threshold:{recurrence_case_count}', candidate, target_path=target, recurrence_case_count=recurrence_case_count, importance=importance, importance_breakdown=breakdown)
    if not ignore_duplicates and duplicate_exists(EVALUATOR_MEMORY_PATH, duplicate_guard):
        return GateDecision(False, slot, 'duplicate_guard_exists', candidate, target_path=target, recurrence_case_count=recurrence_case_count, importance=importance, importance_breakdown=breakdown)
    return GateDecision(True, slot, 'accepted_dry_run' if dry_run else 'accepted', candidate, target_path=target, recurrence_case_count=recurrence_case_count, importance=importance, importance_breakdown=breakdown)


def invoke_memory_upgrade_agent(*, case_key: str, review_path: Path, signal_path: Path, packet_path: Path, session_key: str, agent_id: str | None, timeout_seconds: float, recurrence: list[dict[str, Any]]) -> dict[str, Any]:
    prompt = build_prompt(case_key=case_key, review_path=review_path, signal_path=signal_path, packet_path=packet_path, recurrence=recurrence)
    prompt_path = case_review_dir(case_key) / 'memory-upgrade-prompt.md'
    gateway_response_path = case_review_dir(case_key) / 'memory-upgrade-gateway-response.json'
    raw_response_path = case_review_dir(case_key) / 'memory-upgrade-agent-response.raw.json'
    prompt_path.write_text(prompt, encoding='utf-8')

    last_errors: list[str] = []
    attempts: list[dict[str, Any]] = []
    original_prompt = prompt
    final_payload: dict[str, Any] | None = None

    for attempt in range(1, 3):
        send_payload = {
            'sessionKey': session_key,
            'message': original_prompt if attempt == 1 else (original_prompt.rstrip() + STRICT_JSON_REPAIR_FOOTER + '\n' + '\n'.join(f'- {err}' for err in last_errors) + '\n'),
            'timeoutSeconds': timeout_seconds,
        }
        if agent_id:
            send_payload['agentId'] = agent_id
        proc = run_command(['node', str(OPENCLAW_SESSIONS_SEND), '--payload-json', json.dumps(send_payload)], cwd=REPO_ROOT)
        gateway_response = json.loads(proc.stdout)
        write_json(gateway_response_path, gateway_response, pretty=True)
        try:
            text = extract_text_from_gateway_response(gateway_response)
        except RuntimeError:
            message_seq = gateway_response.get('messageSeq') if isinstance(gateway_response, dict) else None
            text = wait_for_assistant_text(session_key, min_seq=message_seq if isinstance(message_seq, int) else None, timeout_seconds=timeout_seconds)
        raw_response_path.write_text(strip_reply_tag(text).strip() + '\n', encoding='utf-8')
        try:
            payload = extract_json_payload(text)
            errors = validate_payload(payload)
        except Exception as exc:
            payload = None
            errors = [f'json_parse_failed:{exc}']
        attempts.append({'attempt': attempt, 'errors': errors, 'gateway_status': gateway_response.get('status') if isinstance(gateway_response, dict) else ''})
        if not errors and isinstance(payload, dict):
            final_payload = payload
            break
        last_errors = errors
        if attempt == 2:
            raise RuntimeError('invalid evaluator memory-upgrade response: ' + ', '.join(errors))

    metadata = {
        'artifact_type': 'evaluator_memory_upgrade_agent_metadata',
        'schema_version': 'v1',
        'case_key': case_key,
        'session_key': session_key,
        'agent_id': agent_id or '',
        'prompt_path': to_repo_relative(prompt_path),
        'gateway_response_path': to_repo_relative(gateway_response_path),
        'raw_response_path': to_repo_relative(raw_response_path),
        'attempts': attempts,
    }
    return {'proposal': final_payload or {}, 'metadata': metadata, 'prompt_path': prompt_path, 'gateway_response_path': gateway_response_path, 'raw_response_path': raw_response_path}


def run_memory_upgrade_flow(case_key: str, *, review_path: Path | None = None, signal_path: Path | None = None, packet_path: Path | None = None, session_key: str = DEFAULT_EVALUATOR_AGENT_SESSION_KEY, agent_id: str | None = None, timeout_seconds: float = 240.0, db_url: str = '', psql_bin: str = DEFAULT_PSQL, dry_run: bool = False, ignore_duplicates: bool = False) -> dict[str, Any]:
    review_path = review_path or case_review_markdown_path(case_key)
    signal_path = signal_path or signal_packet_path(case_key)
    packet_path = packet_path or learning_packet_path(case_key)
    index_record = build_index_record(review_path, packet_path)
    signal_packet = read_json(signal_path, default={}) or {}
    recurrence = recurrence_rows(case_key, db_url=db_url, psql_bin=psql_bin)
    recurrence_map = recurrence_lookup(recurrence)
    proposal_result = invoke_memory_upgrade_agent(
        case_key=case_key,
        review_path=review_path,
        signal_path=signal_path,
        packet_path=packet_path,
        session_key=session_key,
        agent_id=agent_id,
        timeout_seconds=timeout_seconds,
        recurrence=recurrence,
    )
    proposal = proposal_result['proposal']
    daily_decision = gate_candidate(
        proposal.get('daily_candidate'),
        slot='daily',
        case_key=case_key,
        review_status=index_record.get('status') or '',
        recurrence=recurrence_map,
        signal_packet=signal_packet,
        dry_run=dry_run,
        ignore_duplicates=ignore_duplicates,
    )
    durable_decision = gate_candidate(
        proposal.get('durable_candidate'),
        slot='durable',
        case_key=case_key,
        review_status=index_record.get('status') or '',
        recurrence=recurrence_map,
        signal_packet=signal_packet,
        dry_run=dry_run,
        ignore_duplicates=ignore_duplicates,
    )

    if daily_decision.accepted and daily_decision.candidate and not dry_run:
        append_daily_entry(Path(daily_decision.target_path), daily_decision.candidate, case_key=case_key, recurrence_case_count=daily_decision.recurrence_case_count, importance=float(daily_decision.importance or 0.0))
    if durable_decision.accepted and durable_decision.candidate and not dry_run:
        append_durable_entry(Path(durable_decision.target_path), durable_decision.candidate, case_key=case_key, recurrence_case_count=durable_decision.recurrence_case_count, importance=float(durable_decision.importance or 0.0))

    output = {
        'ok': True,
        'case_key': case_key,
        'review_status': index_record.get('status'),
        'hybrid_importance_version': HYBRID_IMPORTANCE_VERSION,
        'proposal': proposal,
        'decisions': {
            'daily': {
                'accepted': daily_decision.accepted,
                'reason': daily_decision.reason,
                'target_path': daily_decision.target_path,
                'recurrence_case_count': daily_decision.recurrence_case_count,
                'importance': daily_decision.importance,
                'importance_breakdown': daily_decision.importance_breakdown,
            },
            'durable': {
                'accepted': durable_decision.accepted,
                'reason': durable_decision.reason,
                'target_path': durable_decision.target_path,
                'recurrence_case_count': durable_decision.recurrence_case_count,
                'importance': durable_decision.importance,
                'importance_breakdown': durable_decision.importance_breakdown,
            },
        },
        'metadata': proposal_result['metadata'],
        'paths': {
            'durable_memory_path': str(EVALUATOR_MEMORY_PATH),
            'daily_memory_path': str(daily_memory_path()),
        },
        'dry_run': dry_run,
        'ignore_duplicates': ignore_duplicates,
    }
    result_path = case_review_dir(case_key) / 'memory-upgrade.json'
    write_json(result_path, output, pretty=True)
    return output


def main() -> int:
    args = parse_args()
    case_key = args.case_key
    if not case_key and args.review_path:
        review_text = Path(args.review_path).read_text(encoding='utf-8')
        match = re.search(r'^case_key:\s*(.+)$', review_text, flags=re.MULTILINE)
        case_key = match.group(1).strip() if match else None
    if not case_key:
        raise SystemExit('Provide --case-key or --review-path with frontmatter case_key')
    result = run_memory_upgrade_flow(
        case_key,
        review_path=Path(args.review_path) if args.review_path else None,
        signal_path=Path(args.signal_path) if args.signal_path else None,
        packet_path=Path(args.packet_path) if args.packet_path else None,
        session_key=args.session_key,
        agent_id=args.agent_id,
        timeout_seconds=args.timeout_seconds,
        db_url=args.db_url,
        psql_bin=args.psql,
        dry_run=args.dry_run,
        ignore_duplicates=args.ignore_duplicates,
    )
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
