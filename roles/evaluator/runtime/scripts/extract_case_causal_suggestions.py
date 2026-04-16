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
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.causal_suggestions import extract_case_suggestions  # noqa: E402
from lib.io import read_json, read_text, write_json  # noqa: E402
from lib.paths import (  # noqa: E402
    case_canonical_causal_suggestions_path,
    case_causal_projection_path,
    case_causal_suggestions_path,
    case_review_markdown_path,
    ensure_parent,
    learning_packet_path,
    signal_packet_path,
    to_repo_relative,
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Extract raw causal suggestions from a reviewed case bundle')
    parser.add_argument('--case-key', required=True)
    parser.add_argument('--review-path')
    parser.add_argument('--signal-path')
    parser.add_argument('--packet-path')
    parser.add_argument('--projection-path')
    parser.add_argument('--pretty', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    return parser.parse_args()



def extract_case_suggestions_flow(
    case_key: str,
    *,
    review_path: Path | None = None,
    signal_path: Path | None = None,
    packet_path: Path | None = None,
    projection_path: Path | None = None,
    write_output: bool = True,
) -> dict[str, Any]:
    review_path = review_path or case_review_markdown_path(case_key)
    signal_path = signal_path or signal_packet_path(case_key)
    packet_path = packet_path or learning_packet_path(case_key)
    projection_path = projection_path or case_causal_projection_path(case_key)
    out_path = case_causal_suggestions_path(case_key)

    review_text = read_text(review_path)
    signal_packet = read_json(signal_path, default={}) or {}
    learning_packet = read_json(packet_path, default={}) or {}
    projection = read_json(projection_path, default={}) or {}

    payload = extract_case_suggestions(
        case_key=case_key,
        review_text=review_text,
        signal_packet=signal_packet,
        learning_packet=learning_packet,
        projection=projection,
    )
    payload['generated_at'] = utc_now_iso()
    payload['generated_by'] = str(SCRIPT_PATH.relative_to(SCRIPT_PATH.parents[4]))
    payload['source_paths'] = {
        'review_path': to_repo_relative(review_path),
        'signal_packet_path': to_repo_relative(signal_path),
        'learning_packet_path': to_repo_relative(packet_path),
        'causal_projection_path': to_repo_relative(projection_path),
        'canonical_output_path': to_repo_relative(case_canonical_causal_suggestions_path(case_key)),
    }
    payload['counts'] = {
        'suggestion_count': len(payload.get('suggestions') or []),
        'suggestion_count_by_type': {
            candidate_type: sum(1 for row in (payload.get('suggestions') or []) if row.get('candidate_type') == candidate_type)
            for candidate_type in sorted({str(row.get('candidate_type') or '') for row in (payload.get('suggestions') or [])})
        },
    }

    if write_output:
        write_json(ensure_parent(out_path), payload, pretty=True)

    return {
        'ok': True,
        'case_key': case_key,
        'out_path': to_repo_relative(out_path),
        'suggestion_count': payload['counts']['suggestion_count'],
        'suggestion_count_by_type': payload['counts']['suggestion_count_by_type'],
        'payload': payload,
    }



def main() -> int:
    args = parse_args()
    result = extract_case_suggestions_flow(
        args.case_key,
        review_path=Path(args.review_path) if args.review_path else None,
        signal_path=Path(args.signal_path) if args.signal_path else None,
        packet_path=Path(args.packet_path) if args.packet_path else None,
        projection_path=Path(args.projection_path) if args.projection_path else None,
        write_output=not args.dry_run,
    )
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
