#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.io import extract_bullets, parse_frontmatter, read_json, read_text, split_markdown_sections, write_json  # noqa: E402
from lib.paths import case_review_markdown_path, ensure_parent, learning_packet_path, signal_packet_path, to_repo_relative  # noqa: E402

UPSERT_SQL = r'''
INSERT INTO public.learning_signal_occurrences (
  review_path,
  packet_path,
  case_key,
  signal_kind,
  signal_key,
  signal_label,
  direction,
  confidence,
  evidence_excerpt,
  supporting_paths,
  metadata,
  updated_at
)
VALUES (
  :'review_path',
  NULLIF(:'packet_path', ''),
  :'case_key',
  :'signal_kind',
  :'signal_key',
  NULLIF(:'signal_label', ''),
  NULLIF(:'direction', ''),
  NULLIF(:'confidence', '')::numeric,
  NULLIF(:'evidence_excerpt', ''),
  COALESCE(NULLIF(:'supporting_paths_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'metadata_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (review_path, signal_kind, signal_key, evidence_excerpt) DO UPDATE SET
  packet_path = EXCLUDED.packet_path,
  case_key = EXCLUDED.case_key,
  signal_label = EXCLUDED.signal_label,
  direction = EXCLUDED.direction,
  confidence = EXCLUDED.confidence,
  supporting_paths = EXCLUDED.supporting_paths,
  metadata = EXCLUDED.metadata,
  updated_at = NOW()
RETURNING json_build_object('signal_kind', signal_kind, 'signal_key', signal_key)::text;
'''


def slugify(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', (value or '').strip().lower()).strip('-')


def _signal(kind: str, label: str, *, direction: str, evidence: str, review_path: str, packet_path: str, case_key: str, supporting_paths: list[str], confidence: float | None = None, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        'review_path': review_path,
        'packet_path': packet_path,
        'case_key': case_key,
        'signal_kind': kind,
        'signal_key': slugify(label) or slugify(evidence) or kind,
        'signal_label': label,
        'direction': direction,
        'confidence': confidence,
        'evidence_excerpt': evidence,
        'supporting_paths': supporting_paths,
        'metadata': metadata or {},
    }


def build_signal_packet(review_path: Path, packet_path: Path) -> dict[str, Any]:
    review_text = read_text(review_path)
    review_frontmatter = parse_frontmatter(review_text)
    sections = split_markdown_sections(review_text)
    packet = read_json(packet_path, default={}) or {}
    provenance_paths = [path for path in (packet.get('provenance_paths') or {}).values() if isinstance(path, str) and path]
    case_key = packet.get('case_key') or review_frontmatter.get('case_key') or ''

    signals: list[dict[str, Any]] = []

    for bullet in extract_bullets(sections.get('Which inputs were high signal', '')):
        label = bullet.split(':', 1)[0].strip() if ':' in bullet else 'high-signal-input'
        signals.append(_signal('source_performance', label, direction='positive', evidence=bullet, review_path=to_repo_relative(review_path), packet_path=to_repo_relative(packet_path), case_key=case_key, supporting_paths=provenance_paths, confidence=0.7, metadata={'section': 'Which inputs were high signal'}))

    for bullet in extract_bullets(sections.get('Which inputs were misleading', '')):
        label = bullet.split(':', 1)[0].strip() if ':' in bullet else 'misleading-input'
        signals.append(_signal('false_signal', label, direction='negative', evidence=bullet, review_path=to_repo_relative(review_path), packet_path=to_repo_relative(packet_path), case_key=case_key, supporting_paths=provenance_paths, confidence=0.7, metadata={'section': 'Which inputs were misleading'}))

    for bullet in extract_bullets(sections.get('What was missing', '')):
        label = 'missing-input-or-check'
        signals.append(_signal('missed_signal', label, direction='negative', evidence=bullet, review_path=to_repo_relative(review_path), packet_path=to_repo_relative(packet_path), case_key=case_key, supporting_paths=provenance_paths, confidence=0.6, metadata={'section': 'What was missing'}))

    error_pattern = review_frontmatter.get('error_pattern')
    if isinstance(error_pattern, str) and error_pattern.strip():
        signals.append(_signal('workflow_performance', error_pattern, direction='neutral', evidence=f"error_pattern={error_pattern}", review_path=to_repo_relative(review_path), packet_path=to_repo_relative(packet_path), case_key=case_key, supporting_paths=provenance_paths, confidence=0.8, metadata={'section': 'frontmatter'}))

    for driver in review_frontmatter.get('related_drivers') or []:
        if isinstance(driver, str) and driver.strip():
            signals.append(_signal('driver_pattern', driver, direction='neutral', evidence=f"related_driver={driver}", review_path=to_repo_relative(review_path), packet_path=to_repo_relative(packet_path), case_key=case_key, supporting_paths=provenance_paths, confidence=0.6, metadata={'section': 'frontmatter'}))

    return {
        'artifact_type': 'learning_signal_packet',
        'schema_version': 'v1-draft',
        'case_key': case_key,
        'review_path': to_repo_relative(review_path),
        'packet_path': to_repo_relative(packet_path),
        'signal_count': len(signals),
        'signals': signals,
    }


def persist_signal_packet(packet: dict[str, Any], *, db_url: str = '', psql_bin: str = DEFAULT_PSQL) -> dict[str, Any]:
    resolved_db_url = resolve_db_url(db_url)
    table_present = table_exists('learning_signal_occurrences', db_url=resolved_db_url, psql_bin=psql_bin) if resolved_db_url else False
    result: dict[str, Any] = {
        'persisted_count': 0,
        'table_present': table_present,
    }
    if resolved_db_url and table_present:
        for signal in packet['signals']:
            exec_sql(
                psql_bin,
                resolved_db_url,
                UPSERT_SQL,
                {
                    'review_path': signal['review_path'],
                    'packet_path': signal['packet_path'],
                    'case_key': signal['case_key'],
                    'signal_kind': signal['signal_kind'],
                    'signal_key': signal['signal_key'],
                    'signal_label': signal['signal_label'] or '',
                    'direction': signal['direction'] or '',
                    'confidence': '' if signal['confidence'] is None else str(signal['confidence']),
                    'evidence_excerpt': signal['evidence_excerpt'] or '',
                    'supporting_paths_json': json.dumps(signal['supporting_paths']),
                    'metadata_json': json.dumps(signal['metadata']),
                },
            )
            result['persisted_count'] += 1
    elif resolved_db_url and not table_present:
        result['warning'] = 'learning_signal_occurrences table not present; apply roles/evaluator/sql/011_learning_signal_occurrences.sql to enable persistence'
    else:
        result['warning'] = 'db url unavailable; emitted signal packet only'
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Extract deterministic learning signals from one evaluator case review')
    parser.add_argument('--case-key')
    parser.add_argument('--review-path')
    parser.add_argument('--packet-path')
    parser.add_argument('--out')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.case_key and not args.review_path:
        raise SystemExit('Provide --case-key or --review-path')
    review_path = Path(args.review_path) if args.review_path else case_review_markdown_path(args.case_key)
    packet_path = Path(args.packet_path) if args.packet_path else learning_packet_path(args.case_key)
    output_path = Path(args.out) if args.out else signal_packet_path(args.case_key or parse_frontmatter(read_text(review_path)).get('case_key') or 'unknown-case')

    packet = build_signal_packet(review_path, packet_path)
    ensure_parent(output_path)
    write_json(output_path, packet, pretty=True)

    result: dict[str, Any] = {
        'ok': True,
        'signal_packet_path': to_repo_relative(output_path) if output_path.is_absolute() else str(output_path),
        'signal_count': packet['signal_count'],
        **persist_signal_packet(packet, db_url=args.db_url, psql_bin=args.psql),
    }

    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
