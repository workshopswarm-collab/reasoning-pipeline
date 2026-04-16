#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url  # noqa: E402
from lib.paths import LEARNINGS_ROOT, case_review_dir, to_repo_relative  # noqa: E402

SQL = r'''
SELECT json_build_object(
  'signals', COALESCE(
    (
      SELECT json_agg(row_to_json(x) ORDER BY x.case_key, x.signal_kind, x.signal_key)
      FROM (
        SELECT review_path, packet_path, case_key, signal_kind, signal_key, signal_label, direction, confidence, evidence_excerpt, supporting_paths, metadata
        FROM public.learning_signal_occurrences
      ) x
    ),
    '[]'::json
  ),
  'reviews', COALESCE(
    (
      SELECT json_agg(row_to_json(y) ORDER BY y.case_key)
      FROM (
        SELECT case_key, review_path, status, resolution_status, latest_forecast_prob, latest_brier_component, retrieval_tags
        FROM public.learning_case_reviews
      ) y
    ),
    '[]'::json
  )
)::text;
'''

AGG_DIRS = {
    'false_signal': LEARNINGS_ROOT / 'error-patterns' / 'false-signals',
    'missed_signal': LEARNINGS_ROOT / 'error-patterns' / 'missed-signals',
    'source_performance': LEARNINGS_ROOT / 'source-performance',
    'workflow_performance': LEARNINGS_ROOT / 'workflow-performance',
    'driver_pattern': LEARNINGS_ROOT / 'driver-learning',
}

TITLES = {
    'false_signal': 'False signal patterns',
    'missed_signal': 'Missed signal patterns',
    'source_performance': 'Source performance patterns',
    'workflow_performance': 'Workflow performance patterns',
    'driver_pattern': 'Driver learning patterns',
}


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_text(path: Path, text: str) -> None:
    ensure_dir(path.parent)
    path.write_text(text, encoding='utf-8')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Aggregate evaluator learning signals into generated pattern indexes')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def build_markdown(kind: str, rows: list[dict[str, Any]], review_meta: dict[str, dict[str, Any]]) -> str:
    title = TITLES[kind]
    counts = Counter(row.get('signal_key') or 'unknown' for row in rows)
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row.get('signal_key') or 'unknown'].append(row)

    lines = [f'# {title}', '', f'- generated_from_cases: {len({row.get("case_key") for row in rows if row.get("case_key")})}', f'- generated_from_signals: {len(rows)}', '']
    lines.append('## Top recurring patterns')
    lines.append('')
    for key, count in counts.most_common(20):
        sample = grouped[key][0]
        label = sample.get('signal_label') or key
        lines.append(f'- `{key}` — {label} ({count} occurrences)')
    lines.append('')
    lines.append('## Occurrence details')
    lines.append('')
    for key, _count in counts.most_common(20):
        sample = grouped[key][0]
        label = sample.get('signal_label') or key
        lines.append(f'### {label} (`{key}`)')
        lines.append('')
        for row in grouped[key][:10]:
            case_key = row.get('case_key') or 'unknown-case'
            review_path = row.get('review_path') or ''
            meta = review_meta.get(case_key) or {}
            lines.append(f'- case: `{case_key}` | review: `{review_path}` | status: `{meta.get("status") or ""}` | resolution: `{meta.get("resolution_status") or ""}`')
            if row.get('evidence_excerpt'):
                lines.append(f'  - evidence: {row.get("evidence_excerpt")}')
        lines.append('')
    return '\n'.join(lines).rstrip() + '\n'


def main() -> int:
    args = parse_args()
    db_url = resolve_db_url(args.db_url)
    payload = exec_sql(args.psql, db_url, SQL, {})
    signals = payload.get('signals') or []
    reviews = payload.get('reviews') or []
    review_meta = {row.get('case_key'): row for row in reviews if row.get('case_key')}

    written: list[str] = []
    counts_by_kind: dict[str, int] = {}
    for kind, out_dir in AGG_DIRS.items():
        rows = [row for row in signals if row.get('signal_kind') == kind]
        counts_by_kind[kind] = len(rows)
        md = build_markdown(kind, rows, review_meta)
        out_path = ensure_dir(out_dir) / 'generated-index.md'
        write_text(out_path, md)
        summary_json = {
            'artifact_type': 'learning_pattern_aggregate',
            'schema_version': 'v1',
            'signal_kind': kind,
            'signal_count': len(rows),
            'distinct_case_count': len({row.get('case_key') for row in rows if row.get('case_key')}),
            'distinct_pattern_count': len({row.get('signal_key') for row in rows if row.get('signal_key')}),
        }
        write_text(out_dir / 'generated-summary.json', json.dumps(summary_json, indent=2) + '\n')
        written.append(to_repo_relative(out_path))
        written.append(to_repo_relative(out_dir / 'generated-summary.json'))

    output = {
        'ok': True,
        'counts_by_kind': counts_by_kind,
        'written': written,
    }
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
