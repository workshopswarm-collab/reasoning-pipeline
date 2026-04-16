#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
ORCH_ROOT = SCRIPT_PATH.parents[4]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.causal_projection import assign_projection_significance, significance_profile  # noqa: E402
from lib.db import DEFAULT_PSQL  # noqa: E402
from lib.io import write_json  # noqa: E402
from lib.paths import CASE_REVIEWS_ROOT, case_causal_projection_path, case_review_markdown_path, learning_packet_path, signal_packet_path, to_repo_relative  # noqa: E402
from project_case_to_causal_map import build_projection, persist_projection  # noqa: E402

SUMMARY_PATH = ORCH_ROOT / 'qualitative-db' / '60-causal-map' / 'generated' / 'significant-projection-backfill-summary.json'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Backfill only significant case causal projections from existing reviewed case bundles')
    parser.add_argument('--case-key', action='append', help='Optional one or more case keys to evaluate')
    parser.add_argument('--include-existing', action='store_true', help='Recompute cases that already have causal-projection.json')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--min-active-nodes', type=int, default=4)
    parser.add_argument('--min-candidate-edges', type=int, default=2)
    parser.add_argument('--min-contested-edges', type=int, default=1)
    parser.add_argument('--min-non-intervention-active-nodes', type=int, default=2)
    parser.add_argument('--min-non-intervention-candidate-edges', type=int, default=1)
    parser.add_argument('--min-non-intervention-required-checks', type=int, default=2)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def iter_case_keys(selected: list[str] | None = None, *, include_existing: bool = False) -> list[str]:
    selected_set = {str(item).strip() for item in (selected or []) if str(item).strip()}
    out: list[str] = []
    for case_dir in sorted(CASE_REVIEWS_ROOT.glob('case-*')):
        if not case_dir.is_dir():
            continue
        case_key = case_dir.name
        if selected_set and case_key not in selected_set:
            continue
        if not case_review_markdown_path(case_key).exists():
            continue
        if not learning_packet_path(case_key).exists():
            continue
        if not signal_packet_path(case_key).exists():
            continue
        if not include_existing and case_causal_projection_path(case_key).exists():
            continue
        out.append(case_key)
    return out


def main() -> int:
    args = parse_args()
    profile = significance_profile(
        {
            'min_active_nodes': args.min_active_nodes,
            'min_candidate_edges': args.min_candidate_edges,
            'min_contested_edges': args.min_contested_edges,
            'min_non_intervention_active_nodes': args.min_non_intervention_active_nodes,
            'min_non_intervention_candidate_edges': args.min_non_intervention_candidate_edges,
            'min_non_intervention_required_checks': args.min_non_intervention_required_checks,
        }
    )
    case_keys = iter_case_keys(args.case_key or [], include_existing=args.include_existing)

    selected: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    persisted_count = 0
    written_count = 0
    refreshed_existing_count = 0

    for case_key in case_keys:
        out_path = case_causal_projection_path(case_key)
        projection_preexisted = out_path.exists()
        projection = build_projection(
            case_key=case_key,
            review_path=case_review_markdown_path(case_key),
            signal_path=signal_packet_path(case_key),
            packet_path=learning_packet_path(case_key),
        )
        significance = assign_projection_significance(projection, profile=profile)
        row = {
            'case_key': case_key,
            'projection_path': to_repo_relative(out_path),
            'projection_preexisted': projection_preexisted,
            **significance,
        }

        refresh_existing = projection_preexisted
        should_write_projection = bool(significance['significant'] or refresh_existing)
        persist_result: dict[str, Any] = {'persisted': False, 'table_present': False, 'warning': 'dry_run'}
        if not args.dry_run and should_write_projection:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            write_json(out_path, projection, pretty=True)
            written_count += 1
            if refresh_existing:
                refreshed_existing_count += 1
        if significance['significant'] and not args.dry_run:
            learning_packet = json.loads(learning_packet_path(case_key).read_text(encoding='utf-8'))
            persist_result = persist_projection(projection, learning_packet=learning_packet, db_url=args.db_url, psql_bin=args.psql)
            if persist_result.get('persisted'):
                persisted_count += 1
        elif not significance['significant']:
            persist_result = {
                'persisted': False,
                'table_present': False,
                'warning': 'not_significant_under_current_profile',
            }
        row['persistence'] = persist_result
        if significance['significant']:
            selected.append(row)
        else:
            skipped.append(row)

    summary = {
        'ok': True,
        'profile': profile,
        'case_count_evaluated': len(case_keys),
        'selected_count': len(selected),
        'skipped_count': len(skipped),
        'written_count': written_count,
        'refreshed_existing_count': refreshed_existing_count,
        'persisted_count': persisted_count,
        'selected_cases': selected,
        'skipped_cases': skipped,
    }
    if not args.dry_run:
        SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
        write_json(SUMMARY_PATH, summary, pretty=True)
        summary['summary_path'] = str(SUMMARY_PATH.relative_to(ORCH_ROOT))
    print(json.dumps(summary, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
