#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
ORCH_ROOT = SCRIPT_PATH.parents[4]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.causal_map import build_edge_record, build_node_record, edge_note_paths, node_note_paths  # noqa: E402
from lib.causal_suggestions import canonicalize_suggestion, proposal_catalog  # noqa: E402
from lib.io import read_json, write_json  # noqa: E402
from lib.paths import (  # noqa: E402
    CASE_REVIEWS_ROOT,
    CAUSAL_MAP_ROOT,
    case_canonical_causal_suggestions_path,
    case_causal_suggestions_path,
    ensure_parent,
    to_repo_relative,
)

GENERATED_ROOT = CAUSAL_MAP_ROOT / 'generated'
SUMMARY_PATH = GENERATED_ROOT / 'canonical-causal-suggestions-summary.json'
INDEX_PATH = GENERATED_ROOT / 'canonical-causal-suggestions-index.md'


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Canonicalize extracted causal suggestions against live graph + existing proposals')
    parser.add_argument('--case-key', action='append')
    parser.add_argument('--pretty', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    return parser.parse_args()



def case_keys_from_args(selected: list[str] | None) -> list[str]:
    wanted = {str(item).strip() for item in (selected or []) if str(item).strip()}
    keys: list[str] = []
    for path in sorted(CASE_REVIEWS_ROOT.glob('case-*')):
        if not path.is_dir():
            continue
        if wanted and path.name not in wanted:
            continue
        if case_causal_suggestions_path(path.name).exists():
            keys.append(path.name)
    return keys



def load_generated_proposals() -> dict[str, dict[str, Any]]:
    payload = read_json(GENERATED_ROOT / 'proposed-causal-candidates-summary.json', default={}) or {}
    out: dict[str, dict[str, Any]] = {}
    for row in payload.get('proposals') or []:
        if not isinstance(row, dict):
            continue
        key = str(row.get('proposal_key') or '').strip()
        if key:
            out[key] = row
    return out



def build_markdown(summary: dict[str, Any]) -> str:
    lines = [
        '# Canonical causal suggestions',
        '',
        f"- case_count: {summary['case_count']}",
        f"- suggestion_count: {summary['suggestion_count']}",
        '',
    ]
    for case in summary['cases']:
        lines.append(f"## `{case['case_key']}`")
        lines.append('')
        lines.append(f"- projection_significant: `{case['projection_significant']}`")
        lines.append(f"- suggestion_count: `{case['suggestion_count']}`")
        for row in case['suggestions']:
            lines.append(f"### `{row['proposal_key']}`")
            lines.append(f"- status: `{row['canonical_status']}` | family: `{row['mechanism_family']}` | type: `{row['candidate_type']}`")
            if row.get('matched_key'):
                lines.append(f"- matched_key: `{row['matched_key']}`")
            lines.append(f"- reason: {row['canonical_reason']}")
            lines.append(f"- excerpt: {row['evidence_excerpt']}")
            lines.append('')
    return '\n'.join(lines) + '\n'



def canonicalize_case_suggestions(
    case_keys: list[str],
    *,
    write_output: bool = True,
) -> dict[str, Any]:
    live_nodes = {record['node_key']: record for record in (build_node_record(path) for path in node_note_paths())}
    live_edges = {record['edge_key']: record for record in (build_edge_record(path) for path in edge_note_paths())}
    existing_rules = proposal_catalog()
    generated_proposals = load_generated_proposals()

    cases: list[dict[str, Any]] = []
    all_suggestions: list[dict[str, Any]] = []
    for case_key in case_keys:
        raw_path = case_causal_suggestions_path(case_key)
        raw_payload = read_json(raw_path, default={}) or {}
        canonical_rows: list[dict[str, Any]] = []
        for suggestion in raw_payload.get('suggestions') or []:
            if not isinstance(suggestion, dict):
                continue
            canonical_rows.append(
                canonicalize_suggestion(
                    suggestion,
                    live_nodes=live_nodes,
                    live_edges=live_edges,
                    proposal_rules=existing_rules,
                    generated_proposals=generated_proposals,
                )
            )
        canonical_rows.sort(key=lambda row: (row.get('canonical_status') or '', row.get('mechanism_family') or '', row.get('proposal_key') or ''))
        out_payload = {
            'artifact_type': 'case_canonical_causal_suggestions',
            'schema_version': 'v1',
            'generated_at': utc_now_iso(),
            'generated_by': str(SCRIPT_PATH.relative_to(ORCH_ROOT)),
            'case_key': case_key,
            'source_path': to_repo_relative(raw_path),
            'projection_significance': raw_payload.get('projection_significance') or {},
            'context_snapshot': raw_payload.get('context_snapshot') or {},
            'suggestions': canonical_rows,
            'counts': {
                'suggestion_count': len(canonical_rows),
                'status_counts': {
                    status: sum(1 for row in canonical_rows if row.get('canonical_status') == status)
                    for status in sorted({str(row.get('canonical_status') or '') for row in canonical_rows})
                },
            },
        }
        if write_output:
            write_json(ensure_parent(case_canonical_causal_suggestions_path(case_key)), out_payload, pretty=True)
        cases.append(
            {
                'case_key': case_key,
                'projection_significant': bool((raw_payload.get('projection_significance') or {}).get('significant')),
                'suggestion_count': len(canonical_rows),
                'suggestions': canonical_rows,
            }
        )
        all_suggestions.extend([{**row, 'case_key': case_key} for row in canonical_rows])

    summary = {
        'artifact_type': 'canonical_causal_suggestions_summary',
        'schema_version': 'v1',
        'generated_at': utc_now_iso(),
        'generated_by': str(SCRIPT_PATH.relative_to(ORCH_ROOT)),
        'case_count': len(cases),
        'suggestion_count': len(all_suggestions),
        'status_counts': {
            status: sum(1 for row in all_suggestions if row.get('canonical_status') == status)
            for status in sorted({str(row.get('canonical_status') or '') for row in all_suggestions})
        },
        'family_counts': {
            family: sum(1 for row in all_suggestions if row.get('mechanism_family') == family)
            for family in sorted({str(row.get('mechanism_family') or '') for row in all_suggestions})
        },
        'cases': cases,
    }
    if write_output:
        GENERATED_ROOT.mkdir(parents=True, exist_ok=True)
        write_json(SUMMARY_PATH, summary, pretty=True)
        INDEX_PATH.write_text(build_markdown(summary), encoding='utf-8')

    return {
        'ok': True,
        'case_count': len(cases),
        'suggestion_count': len(all_suggestions),
        'summary_path': to_repo_relative(SUMMARY_PATH),
        'index_path': to_repo_relative(INDEX_PATH),
        'summary': summary,
    }



def main() -> int:
    args = parse_args()
    result = canonicalize_case_suggestions(case_keys_from_args(args.case_key), write_output=not args.dry_run)
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
