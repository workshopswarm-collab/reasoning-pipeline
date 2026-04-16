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
from lib.io import parse_frontmatter, read_json, read_text, split_markdown_sections  # noqa: E402
from lib.paths import case_review_markdown_path, learning_packet_path, to_repo_relative  # noqa: E402

UPSERT_SQL = r'''
INSERT INTO public.learning_case_reviews (
  review_path,
  packet_path,
  case_key,
  case_db_id,
  market_id,
  contract_id,
  status,
  category,
  platform,
  resolution_status,
  resolved_value,
  resolved_at,
  error_pattern,
  latest_forecast_prob,
  latest_brier_component,
  retrieval_tags,
  source_paths,
  review_frontmatter,
  updated_at
)
VALUES (
  :'review_path',
  :'packet_path',
  :'case_key',
  NULLIF(:'case_db_id', ''),
  NULLIF(:'market_id', ''),
  NULLIF(:'contract_id', ''),
  :'status',
  NULLIF(:'category', ''),
  NULLIF(:'platform', ''),
  NULLIF(:'resolution_status', ''),
  NULLIF(:'resolved_value', '')::numeric,
  NULLIF(:'resolved_at', '')::timestamptz,
  NULLIF(:'error_pattern', ''),
  NULLIF(:'latest_forecast_prob', '')::numeric,
  NULLIF(:'latest_brier_component', '')::numeric,
  COALESCE(NULLIF(:'retrieval_tags_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'source_paths_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'review_frontmatter_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (review_path) DO UPDATE SET
  packet_path = EXCLUDED.packet_path,
  case_key = EXCLUDED.case_key,
  case_db_id = EXCLUDED.case_db_id,
  market_id = EXCLUDED.market_id,
  contract_id = EXCLUDED.contract_id,
  status = EXCLUDED.status,
  category = EXCLUDED.category,
  platform = EXCLUDED.platform,
  resolution_status = EXCLUDED.resolution_status,
  resolved_value = EXCLUDED.resolved_value,
  resolved_at = EXCLUDED.resolved_at,
  error_pattern = EXCLUDED.error_pattern,
  latest_forecast_prob = EXCLUDED.latest_forecast_prob,
  latest_brier_component = EXCLUDED.latest_brier_component,
  retrieval_tags = EXCLUDED.retrieval_tags,
  source_paths = EXCLUDED.source_paths,
  review_frontmatter = EXCLUDED.review_frontmatter,
  updated_at = NOW()
RETURNING json_build_object(
  'review_path', review_path,
  'case_key', case_key,
  'status', status,
  'resolution_status', resolution_status
)::text;
'''


def slugify(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', (value or '').strip().lower()).strip('-')


def infer_status(frontmatter: dict[str, Any], packet: dict[str, Any]) -> str:
    tags = set(frontmatter.get('tags') or [])
    if 'evaluator/draft' in tags:
        return 'draft'
    if (packet.get('market_truth') or {}).get('resolution_status') == 'resolved':
        return 'reviewed'
    return 'draft'


def build_index_record(review_path: Path, packet_path: Path) -> dict[str, Any]:
    review_text = read_text(review_path)
    review_frontmatter = parse_frontmatter(review_text)
    sections = split_markdown_sections(review_text)
    packet = read_json(packet_path, default={}) or {}
    market_truth = packet.get('market_truth') or {}
    forecast_summary = packet.get('forecast_summary') or {}
    provenance_paths = packet.get('provenance_paths') or {}

    retrieval_tags = []
    for item in [
        packet.get('platform'),
        packet.get('category'),
        market_truth.get('resolution_status'),
        review_frontmatter.get('error_pattern'),
        *(review_frontmatter.get('tags') or []),
    ]:
        if isinstance(item, str) and item.strip():
            retrieval_tags.append(slugify(item))

    record = {
        'review_path': to_repo_relative(review_path),
        'packet_path': to_repo_relative(packet_path),
        'case_key': packet.get('case_key') or review_frontmatter.get('case_key') or '',
        'case_db_id': packet.get('case_id') or '',
        'market_id': packet.get('market_id') or '',
        'contract_id': packet.get('contract_id') or '',
        'status': infer_status(review_frontmatter, packet),
        'category': packet.get('category') or review_frontmatter.get('market_category') or '',
        'platform': packet.get('platform') or '',
        'resolution_status': market_truth.get('resolution_status') or '',
        'resolved_value': market_truth.get('resolved_value'),
        'resolved_at': packet.get('resolved_at') or '',
        'error_pattern': review_frontmatter.get('error_pattern') or '',
        'latest_forecast_prob': forecast_summary.get('latest_forecast_prob'),
        'latest_brier_component': forecast_summary.get('latest_brier_component'),
        'retrieval_tags': sorted(set(tag for tag in retrieval_tags if tag)),
        'source_paths': sorted(set(path for path in provenance_paths.values() if isinstance(path, str) and path)),
        'review_frontmatter': review_frontmatter,
        'sections_present': sorted(sections.keys()),
    }
    return record


def persist_index_record(record: dict[str, Any], *, db_url: str = '', psql_bin: str = DEFAULT_PSQL) -> dict[str, Any]:
    resolved_db_url = resolve_db_url(db_url)
    table_present = table_exists('learning_case_reviews', db_url=resolved_db_url, psql_bin=psql_bin) if resolved_db_url else False
    result: dict[str, Any] = {
        'persisted': False,
        'table_present': table_present,
    }
    if resolved_db_url and table_present:
        payload = exec_sql(
            psql_bin,
            resolved_db_url,
            UPSERT_SQL,
            {
                'review_path': record['review_path'],
                'packet_path': record['packet_path'],
                'case_key': record['case_key'],
                'case_db_id': str(record['case_db_id'] or ''),
                'market_id': str(record['market_id'] or ''),
                'contract_id': str(record['contract_id'] or ''),
                'status': record['status'],
                'category': record['category'],
                'platform': record['platform'],
                'resolution_status': record['resolution_status'],
                'resolved_value': '' if record['resolved_value'] is None else str(record['resolved_value']),
                'resolved_at': record['resolved_at'],
                'error_pattern': record['error_pattern'],
                'latest_forecast_prob': '' if record['latest_forecast_prob'] is None else str(record['latest_forecast_prob']),
                'latest_brier_component': '' if record['latest_brier_component'] is None else str(record['latest_brier_component']),
                'retrieval_tags_json': json.dumps(record['retrieval_tags']),
                'source_paths_json': json.dumps(record['source_paths']),
                'review_frontmatter_json': json.dumps(record['review_frontmatter']),
            },
        )
        result['persisted'] = True
        result['db_result'] = payload
    elif resolved_db_url and not table_present:
        result['warning'] = 'learning_case_reviews table not present; apply roles/evaluator/sql/010_learning_case_reviews.sql to enable persistence'
    else:
        result['warning'] = 'db url unavailable; emitting record only'
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Index one evaluator case review')
    parser.add_argument('--case-key')
    parser.add_argument('--review-path')
    parser.add_argument('--packet-path')
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
    record = build_index_record(review_path, packet_path)
    result: dict[str, Any] = {
        'ok': True,
        'record': record,
        **persist_index_record(record, db_url=args.db_url, psql_bin=args.psql),
    }

    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
