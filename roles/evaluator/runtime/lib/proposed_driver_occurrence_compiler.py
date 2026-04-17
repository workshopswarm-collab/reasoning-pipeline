from __future__ import annotations

import hashlib
import json
import os
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .db import exec_sql, maybe_load_workspace_env
from .io import read_json, write_json
from .paths import CAUSAL_MAP_ROOT, ORCHESTRATOR_ROOT, ensure_parent, to_repo_relative

COMPILER_VERSION = '2026-04-16-occurrence-v1'
PROPOSAL_SOURCE = 'driver_occurrence_compiler'
GENERATED_DRIVER_NOTE_PREFIX = 'generated-driver-candidate-'

DRIVER_REVIEW_QUEUE_ROOT = ORCHESTRATOR_ROOT / 'qualitative-db' / '40-research' / 'review-queue' / 'drivers-candidates'
DRIVER_INDEX_JSON_PATH = DRIVER_REVIEW_QUEUE_ROOT / 'generated-index.json'
OCCURRENCE_COMPILER_ROOT = CAUSAL_MAP_ROOT / 'generated' / 'occurrence-compiler'
PACKETS_ROOT = OCCURRENCE_COMPILER_ROOT / 'packets'
STATUS_JSON_PATH = CAUSAL_MAP_ROOT / 'generated' / 'occurrence-compiler-status.json'
STATUS_MD_PATH = CAUSAL_MAP_ROOT / 'generated' / 'occurrence-compiler-status.md'

REQUIRED_OCCURRENCE_COLUMNS = [
    'artifact_path',
    'proposed_driver_label',
    'proposed_driver_slug',
    'case_key',
    'dispatch_id',
    'research_run_id',
    'persona',
    'artifact_kind',
    'related_entities',
    'related_canonical_drivers',
    'canonical_driver_suggestions',
    'difficulty_class',
    'source_of_truth_class',
    'status',
    'occurred_at',
]

ACTIVE_OCCURRENCES_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY t.proposed_driver_slug, t.artifact_path), '[]'::json)::text
FROM (
  SELECT
    artifact_path,
    proposed_driver_label,
    proposed_driver_slug,
    case_key,
    dispatch_id,
    research_run_id::text,
    persona,
    artifact_kind,
    related_entities,
    related_canonical_drivers,
    canonical_driver_suggestions,
    difficulty_class,
    source_of_truth_class,
    status,
    occurred_at
  FROM public.proposed_driver_occurrences
  WHERE status = 'active'
) t;
'''


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')



def resolve_occurrence_source_db_url(explicit: str | None = None) -> str:
    if explicit:
        return explicit
    maybe_load_workspace_env()
    return (
        os.getenv('PREDQUANT_ORCHESTRATOR_URL')
        or os.getenv('PREDQUANT_ADMIN_URL')
        or os.getenv('PREDQUANT_EVALUATOR_URL')
        or os.getenv('PREDQUANT_EVAL_URL')
        or ''
    )



def packet_json_path(candidate_slug: str) -> Path:
    return PACKETS_ROOT / f'{candidate_slug}.json'



def packet_markdown_path(candidate_slug: str) -> Path:
    return PACKETS_ROOT / f'{candidate_slug}.md'



def default_candidate_note_path(candidate_slug: str) -> str:
    return (
        'qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/'
        f'{GENERATED_DRIVER_NOTE_PREFIX}{candidate_slug}.md'
    )



def stable_hash(payload: Any) -> str:
    text = json.dumps(payload, sort_keys=True, separators=(',', ':'), ensure_ascii=False, default=str)
    return hashlib.sha256(text.encode('utf-8')).hexdigest()



def load_generated_index_payload() -> dict[str, Any]:
    payload = read_json(DRIVER_INDEX_JSON_PATH, default={}) or {}
    if not isinstance(payload, dict):
        return {}
    return payload



def build_candidate_hint_map(index_payload: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    rows = (index_payload or {}).get('candidates') or []
    hints: dict[str, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        candidate_slug = str(row.get('candidate_slug') or '').strip()
        if not candidate_slug:
            continue
        hints[candidate_slug] = row
    return hints



def load_active_occurrence_rows(psql_bin: str, db_url: str) -> list[dict[str, Any]]:
    rows = exec_sql(psql_bin, db_url, ACTIVE_OCCURRENCES_SQL, {})
    if isinstance(rows, list):
        return [row for row in rows if isinstance(row, dict)]
    return []



def group_occurrence_rows(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        candidate_slug = str(row.get('proposed_driver_slug') or '').strip()
        if not candidate_slug:
            continue
        grouped[candidate_slug].append(dict(row))
    return dict(grouped)



def normalize_occurrence_row(row: dict[str, Any]) -> dict[str, Any]:
    return {
        'artifact_path': str(row.get('artifact_path') or '').strip(),
        'proposed_driver_label': str(row.get('proposed_driver_label') or row.get('proposed_driver_slug') or '').strip(),
        'proposed_driver_slug': str(row.get('proposed_driver_slug') or '').strip(),
        'case_key': str(row.get('case_key') or '').strip(),
        'dispatch_id': str(row.get('dispatch_id') or '').strip(),
        'research_run_id': str(row.get('research_run_id') or '').strip(),
        'persona': str(row.get('persona') or '').strip(),
        'artifact_kind': str(row.get('artifact_kind') or 'unknown').strip() or 'unknown',
        'related_entities': sorted({str(value).strip() for value in (row.get('related_entities') or []) if str(value).strip()}),
        'related_canonical_drivers': sorted({str(value).strip() for value in (row.get('related_canonical_drivers') or []) if str(value).strip()}),
        'canonical_driver_suggestions': sorted({str(value).strip() for value in (row.get('canonical_driver_suggestions') or []) if str(value).strip()}),
        'difficulty_class': str(row.get('difficulty_class') or '').strip(),
        'source_of_truth_class': str(row.get('source_of_truth_class') or '').strip(),
        'occurred_at': str(row.get('occurred_at') or '').strip(),
        'status': str(row.get('status') or '').strip(),
    }



def top_counts(values: list[str], *, limit: int = 8) -> list[dict[str, Any]]:
    return [
        {'value': value, 'count': count}
        for value, count in Counter([item for item in values if item]).most_common(limit)
    ]



def compile_candidate_packet(candidate_slug: str, rows: list[dict[str, Any]], candidate_hint: dict[str, Any] | None = None) -> dict[str, Any]:
    normalized_rows = [normalize_occurrence_row(row) for row in rows]
    normalized_rows = sorted(normalized_rows, key=lambda row: (row['artifact_path'], row['occurred_at'], row['proposed_driver_label']))
    primary_label = Counter(row['proposed_driver_label'] for row in normalized_rows if row['proposed_driver_label']).most_common(1)
    candidate_label = primary_label[0][0] if primary_label else candidate_slug
    hint = dict(candidate_hint or {})
    normalized_family = str(hint.get('normalized_family') or '').strip() or candidate_slug or 'unassigned'
    family_assignment_source = 'generated_index' if str(hint.get('normalized_family') or '').strip() else 'slug_fallback'
    candidate_note_path = str(hint.get('candidate_note_path') or '').strip() or default_candidate_note_path(candidate_slug)
    case_keys = sorted({row['case_key'] for row in normalized_rows if row['case_key']})
    personas = sorted({row['persona'] for row in normalized_rows if row['persona']})
    dispatch_ids = sorted({row['dispatch_id'] for row in normalized_rows if row['dispatch_id']})
    difficulty_classes = sorted({row['difficulty_class'] for row in normalized_rows if row['difficulty_class']})
    source_of_truth_classes = sorted({row['source_of_truth_class'] for row in normalized_rows if row['source_of_truth_class']})
    artifact_kind_counts = Counter(row['artifact_kind'] for row in normalized_rows if row['artifact_kind'])
    related_entities = sorted({value for row in normalized_rows for value in row['related_entities']})
    related_canonical_drivers = sorted({value for row in normalized_rows for value in row['related_canonical_drivers']})
    canonical_driver_suggestions = sorted({value for row in normalized_rows for value in row['canonical_driver_suggestions']})
    occurrence_paths = [row['artifact_path'] for row in normalized_rows if row['artifact_path']]
    occurred_values = [row['occurred_at'] for row in normalized_rows if row['occurred_at']]

    packet: dict[str, Any] = {
        'packet_type': 'occurrence_backed_mechanism_packet',
        'compiler_version': COMPILER_VERSION,
        'proposal_source': PROPOSAL_SOURCE,
        'packet_key': f'occurrence-packet:{candidate_slug}',
        'proposal_key': f'driver-mechanism:{candidate_slug}',
        'candidate_type': 'packet',
        'candidate_slug': candidate_slug,
        'candidate_label': candidate_label,
        'normalized_family': normalized_family,
        'family_assignment_source': family_assignment_source,
        'candidate_note_path': candidate_note_path,
        'source_lane': 'public.proposed_driver_occurrences',
        'routing': {
            'mode': 'packet_only',
            'shadow_eligible': False,
            'trial_eligible': False,
            'promotion_eligible': False,
            'next_step': 'materialize_provisional_families',
        },
        'source_summary': {
            'source_occurrence_count': len(normalized_rows),
            'distinct_case_count': len(case_keys),
            'distinct_persona_count': len(personas),
            'distinct_dispatch_count': len(dispatch_ids),
            'source_mix': {'db': len(normalized_rows)},
            'artifact_kind_counts': dict(sorted(artifact_kind_counts.items())),
            'difficulty_classes': difficulty_classes,
            'source_of_truth_classes': source_of_truth_classes,
            'first_observed_at': min(occurred_values) if occurred_values else '',
            'last_observed_at': max(occurred_values) if occurred_values else '',
        },
        'support': {
            'case_keys': case_keys,
            'personas': personas,
            'dispatch_ids': dispatch_ids,
            'related_entities': related_entities,
            'related_canonical_drivers': related_canonical_drivers,
            'canonical_driver_suggestions': canonical_driver_suggestions,
            'top_related_entities': top_counts(related_entities, limit=6),
            'top_related_canonical_drivers': top_counts(related_canonical_drivers, limit=6),
            'top_canonical_driver_suggestions': top_counts(canonical_driver_suggestions, limit=6),
        },
        'seed_hints': {
            'node_seed': {
                'candidate_key': candidate_slug,
                'candidate_label': candidate_label,
                'mechanism_family': normalized_family,
                'status': 'shadow_only_provisional_seed',
            },
            'edge_seeds': [],
        },
        'compiler_metadata': {
            'generated_index_present': bool(candidate_hint),
            'hint_source_path': to_repo_relative(DRIVER_INDEX_JSON_PATH),
            'hint_canon_coverage_status': str(hint.get('canon_coverage_status') or '').strip(),
            'hint_canon_coverage_driver': str(hint.get('canon_coverage_driver') or '').strip(),
            'hint_occurrence_count': int(hint.get('occurrences') or 0),
            'hint_distinct_case_count': int(hint.get('distinct_cases') or 0),
            'hint_distinct_persona_count': int(hint.get('distinct_personas') or 0),
            'occurrence_paths': occurrence_paths,
        },
        'source_occurrences': normalized_rows,
    }
    packet_hash = stable_hash({k: v for k, v in packet.items() if k != 'packet_hash'})
    packet['packet_hash'] = packet_hash
    return packet



def compile_occurrence_packets(rows: list[dict[str, Any]], index_payload: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    candidate_hints = build_candidate_hint_map(index_payload)
    packets: list[dict[str, Any]] = []
    for candidate_slug, candidate_rows in sorted(group_occurrence_rows(rows).items(), key=lambda item: (-len(item[1]), item[0])):
        packets.append(compile_candidate_packet(candidate_slug, candidate_rows, candidate_hints.get(candidate_slug)))
    return packets



def render_packet_markdown(packet: dict[str, Any]) -> str:
    source_summary = packet.get('source_summary') or {}
    support = packet.get('support') or {}
    compiler_metadata = packet.get('compiler_metadata') or {}
    lines = [
        '---',
        'type: occurrence_backed_mechanism_packet',
        f"packet_key: {packet.get('packet_key')}",
        f"proposal_key: {packet.get('proposal_key')}",
        f"candidate_slug: {packet.get('candidate_slug')}",
        f"normalized_family: {packet.get('normalized_family')}",
        f"proposal_source: {packet.get('proposal_source')}",
        f"compiler_version: {packet.get('compiler_version')}",
        '---',
        '',
        f"# {packet.get('candidate_label')}",
        '',
        '## Summary',
        f"- family: `{packet.get('normalized_family')}`",
        f"- family_assignment_source: `{packet.get('family_assignment_source')}`",
        f"- candidate_note_path: `{packet.get('candidate_note_path')}`",
        f"- source_occurrence_count: `{source_summary.get('source_occurrence_count')}`",
        f"- distinct_case_count: `{source_summary.get('distinct_case_count')}`",
        f"- distinct_persona_count: `{source_summary.get('distinct_persona_count')}`",
        f"- first_observed_at: `{source_summary.get('first_observed_at') or ''}`",
        f"- last_observed_at: `{source_summary.get('last_observed_at') or ''}`",
        f"- packet_hash: `{packet.get('packet_hash')}`",
        '',
        '## Routing',
        f"- next_step: `{((packet.get('routing') or {}).get('next_step') or '')}`",
        f"- shadow_eligible: `{((packet.get('routing') or {}).get('shadow_eligible'))}`",
        f"- trial_eligible: `{((packet.get('routing') or {}).get('trial_eligible'))}`",
        '',
        '## Support',
        f"- case_keys: {', '.join(support.get('case_keys') or []) or '[]'}",
        f"- personas: {', '.join(support.get('personas') or []) or '[]'}",
        f"- related_entities: {', '.join(support.get('related_entities') or []) or '[]'}",
        f"- related_canonical_drivers: {', '.join(support.get('related_canonical_drivers') or []) or '[]'}",
        f"- canonical_driver_suggestions: {', '.join(support.get('canonical_driver_suggestions') or []) or '[]'}",
        '',
        '## Compiler metadata',
        f"- generated_index_present: `{compiler_metadata.get('generated_index_present')}`",
        f"- hint_canon_coverage_status: `{compiler_metadata.get('hint_canon_coverage_status') or ''}`",
        f"- hint_canon_coverage_driver: `{compiler_metadata.get('hint_canon_coverage_driver') or ''}`",
        '',
        '## Source occurrence paths',
    ]
    occurrence_paths = compiler_metadata.get('occurrence_paths') or []
    if not occurrence_paths:
        lines.append('- none')
    else:
        for path in occurrence_paths:
            lines.append(f'- `{path}`')
    lines.append('')
    return '\n'.join(lines)



def write_packet_artifacts(packets: list[dict[str, Any]], *, clean: bool = True) -> dict[str, int]:
    PACKETS_ROOT.mkdir(parents=True, exist_ok=True)
    outcomes = Counter()
    expected_files: set[str] = set()
    for packet in packets:
        candidate_slug = str(packet.get('candidate_slug') or '').strip()
        if not candidate_slug:
            continue
        json_path = packet_json_path(candidate_slug)
        md_path = packet_markdown_path(candidate_slug)
        expected_files.add(json_path.name)
        expected_files.add(md_path.name)
        previous_packet = read_json(json_path, default=None)
        if previous_packet == packet:
            outcomes['packet_json_unchanged'] += 1
        else:
            write_json(json_path, packet)
            outcomes['packet_json_written'] += 1
        markdown = render_packet_markdown(packet)
        if md_path.exists() and md_path.read_text(encoding='utf-8') == markdown:
            outcomes['packet_md_unchanged'] += 1
        else:
            md_path.write_text(markdown, encoding='utf-8')
            outcomes['packet_md_written'] += 1
    if clean:
        for path in PACKETS_ROOT.glob('*'):
            if path.name not in expected_files:
                path.unlink()
                outcomes['stale_removed'] += 1
    return dict(outcomes)



def build_family_summaries(packets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for packet in packets:
        family = str(packet.get('normalized_family') or 'unassigned').strip() or 'unassigned'
        bucket = grouped.setdefault(
            family,
            {
                'family_key': family,
                'candidate_count': 0,
                'source_occurrence_count': 0,
                'distinct_case_keys': set(),
                'distinct_personas': set(),
                'assignment_sources': Counter(),
            },
        )
        bucket['candidate_count'] += 1
        source_summary = packet.get('source_summary') or {}
        bucket['source_occurrence_count'] += int(source_summary.get('source_occurrence_count') or 0)
        support = packet.get('support') or {}
        bucket['distinct_case_keys'].update(support.get('case_keys') or [])
        bucket['distinct_personas'].update(support.get('personas') or [])
        bucket['assignment_sources'][str(packet.get('family_assignment_source') or 'unknown')] += 1
    rows: list[dict[str, Any]] = []
    for family, bucket in grouped.items():
        rows.append(
            {
                'family_key': family,
                'candidate_count': bucket['candidate_count'],
                'source_occurrence_count': bucket['source_occurrence_count'],
                'distinct_case_count': len(bucket['distinct_case_keys']),
                'distinct_persona_count': len(bucket['distinct_personas']),
                'assignment_source_mix': dict(bucket['assignment_sources']),
            }
        )
    return sorted(rows, key=lambda row: (-row['source_occurrence_count'], row['family_key']))



def build_status_payload(
    *,
    rows: list[dict[str, Any]],
    packets: list[dict[str, Any]],
    write_outcomes: dict[str, int],
    index_payload: dict[str, Any] | None,
    warnings: list[str] | None = None,
    run_id: str | None = None,
) -> dict[str, Any]:
    index_payload = index_payload or {}
    source_counts = index_payload.get('source_counts') or {}
    generated_summary = index_payload.get('summary') or {}
    packet_root_rel = to_repo_relative(PACKETS_ROOT)
    status = {
        'type': 'occurrence_compiler_status',
        'ok': True,
        'run_id': run_id or f'occurrence-compiler-{now_utc_iso()}',
        'generated_at': now_utc_iso(),
        'compiler_version': COMPILER_VERSION,
        'proposal_source': PROPOSAL_SOURCE,
        'source_lane': 'public.proposed_driver_occurrences',
        'driver_index_path': to_repo_relative(DRIVER_INDEX_JSON_PATH),
        'packet_root': packet_root_rel,
        'source_occurrence_count': len(rows),
        'candidate_count': len(packets),
        'family_count': len({str(packet.get('normalized_family') or 'unassigned') for packet in packets}),
        'db_occurrence_count': int(source_counts.get('db_occurrence_count') or len(rows)),
        'markdown_fallback_occurrence_count': int(source_counts.get('markdown_fallback_occurrence_count') or 0),
        'generated_index_present': bool(index_payload),
        'generated_index_candidate_count': int(generated_summary.get('generated_candidate_count') or 0),
        'generated_index_family_count': int(generated_summary.get('normalized_family_count') or 0),
        'fallback_family_assignment_count': sum(1 for packet in packets if packet.get('family_assignment_source') != 'generated_index'),
        'top_families': build_family_summaries(packets)[:12],
        'top_packets': [
            {
                'packet_key': packet.get('packet_key'),
                'proposal_key': packet.get('proposal_key'),
                'candidate_slug': packet.get('candidate_slug'),
                'candidate_label': packet.get('candidate_label'),
                'normalized_family': packet.get('normalized_family'),
                'packet_path': to_repo_relative(packet_json_path(str(packet.get('candidate_slug') or ''))),
                'packet_hash': packet.get('packet_hash'),
                'source_occurrence_count': ((packet.get('source_summary') or {}).get('source_occurrence_count') or 0),
                'distinct_case_count': ((packet.get('source_summary') or {}).get('distinct_case_count') or 0),
                'distinct_persona_count': ((packet.get('source_summary') or {}).get('distinct_persona_count') or 0),
            }
            for packet in packets[:20]
        ],
        'write_outcomes': write_outcomes,
        'warnings': list(warnings or []),
    }
    return status



def render_status_markdown(status: dict[str, Any]) -> str:
    lines = [
        '---',
        'type: occurrence_compiler_status',
        f"generated_at: {status.get('generated_at')}",
        f"run_id: {status.get('run_id')}",
        f"compiler_version: {status.get('compiler_version')}",
        '---',
        '',
        '# Occurrence-backed compiler status',
        '',
        '## Summary',
        f"- ok: `{status.get('ok')}`",
        f"- source_lane: `{status.get('source_lane')}`",
        f"- source_occurrence_count: `{status.get('source_occurrence_count')}`",
        f"- candidate_count: `{status.get('candidate_count')}`",
        f"- family_count: `{status.get('family_count')}`",
        f"- generated_index_present: `{status.get('generated_index_present')}`",
        f"- markdown_fallback_occurrence_count: `{status.get('markdown_fallback_occurrence_count')}`",
        f"- fallback_family_assignment_count: `{status.get('fallback_family_assignment_count')}`",
        f"- packet_root: `{status.get('packet_root')}`",
        '',
        '## Top families',
    ]
    top_families = status.get('top_families') or []
    if not top_families:
        lines.append('- none')
    else:
        for row in top_families:
            lines.append(
                f"- `{row.get('family_key')}` "
                f"(candidates: `{row.get('candidate_count')}`, occurrences: `{row.get('source_occurrence_count')}`, "
                f"cases: `{row.get('distinct_case_count')}`, personas: `{row.get('distinct_persona_count')}`)"
            )
    lines.extend(['', '## Top packets'])
    top_packets = status.get('top_packets') or []
    if not top_packets:
        lines.append('- none')
    else:
        for row in top_packets:
            lines.append(
                f"- `{row.get('candidate_label')}` -> `{row.get('normalized_family')}` "
                f"(occurrences: `{row.get('source_occurrence_count')}`, cases: `{row.get('distinct_case_count')}`, personas: `{row.get('distinct_persona_count')}`)"
            )
            lines.append(f"  - packet: `{row.get('packet_path')}`")
    lines.extend(['', '## Warnings'])
    warnings = status.get('warnings') or []
    if not warnings:
        lines.append('- none')
    else:
        for warning in warnings:
            lines.append(f'- `{warning}`')
    lines.append('')
    return '\n'.join(lines)



def write_status_artifacts(status: dict[str, Any]) -> None:
    write_json(ensure_parent(STATUS_JSON_PATH), status)
    ensure_parent(STATUS_MD_PATH).write_text(render_status_markdown(status), encoding='utf-8')



def load_packet_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not PACKETS_ROOT.exists():
        return rows
    for path in sorted(PACKETS_ROOT.glob('*.json')):
        payload = read_json(path, default=None)
        if isinstance(payload, dict):
            rows.append(payload)
    return rows
