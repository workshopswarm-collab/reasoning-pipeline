#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from classify_research_difficulty import classify  # noqa: E402

FIXTURES_DIR = SCRIPT_DIR.parent / 'tests' / 'fixtures'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Replay research-difficulty fixtures repeatedly and summarize output drift')
    parser.add_argument('--fixture', action='append', default=[], help='Fixture filename under planner/tests/fixtures (default: all *.json)')
    parser.add_argument('--iterations', type=int, default=3)
    parser.add_argument('--mode', choices=['heuristic', 'hybrid'], default='hybrid')
    parser.add_argument('--ollama-endpoint', default='http://127.0.0.1:11434')
    parser.add_argument('--ollama-model', default='qwen3.5:9b')
    parser.add_argument('--timeout-seconds', type=float, default=55.0)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def fixture_paths(names: list[str]) -> list[Path]:
    if names:
        return [FIXTURES_DIR / name for name in names]
    return sorted(FIXTURES_DIR.glob('*.json'))


def stable_signature(result: dict[str, Any]) -> dict[str, Any]:
    profile = result.get('difficulty_profile') or {}
    return {
        'difficulty_class': profile.get('difficulty_class'),
        'resolution_risk': profile.get('resolution_risk'),
        'evidence_floor': profile.get('evidence_floor'),
        'extra_verification_required': profile.get('extra_verification_required'),
        'focus_hints': profile.get('focus_hints'),
        'difficulty_rationale': profile.get('difficulty_rationale'),
        'source_of_truth_class': profile.get('source_of_truth_class'),
        'classifier_version': profile.get('classifier_version'),
    }


def main() -> int:
    args = parse_args()
    summaries: list[dict[str, Any]] = []
    for path in fixture_paths(args.fixture):
        payload = json.loads(path.read_text())
        runs: list[dict[str, Any]] = []
        for _ in range(args.iterations):
            result = classify(
                payload,
                mode=args.mode,
                endpoint=args.ollama_endpoint,
                model=args.ollama_model,
                timeout_seconds=args.timeout_seconds,
            )
            runs.append(stable_signature(result))
        unique = [json.dumps(item, sort_keys=True) for item in runs]
        summaries.append({
            'fixture': path.name,
            'iterations': args.iterations,
            'unique_signature_count': len(set(unique)),
            'stable': len(set(unique)) == 1,
            'runs': runs,
        })
    print(json.dumps({'fixtures': summaries}, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
