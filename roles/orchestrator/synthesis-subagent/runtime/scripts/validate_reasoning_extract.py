#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import WORKSPACE_ROOT, load_json, relative_to_workspace  # noqa: E402
from validation import validate_reasoning_extract_payload  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate one persona reasoning-extract JSON payload")
    parser.add_argument("--result-json", required=True)
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result_path = Path(args.result_json)
    if not result_path.is_absolute():
        result_path = WORKSPACE_ROOT / result_path
    payload = load_json(result_path)
    validation = validate_reasoning_extract_payload(payload)
    validation["result_json"] = relative_to_workspace(result_path)
    text = json.dumps(validation, indent=2 if args.pretty else None)
    print(text)
    if not validation["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
