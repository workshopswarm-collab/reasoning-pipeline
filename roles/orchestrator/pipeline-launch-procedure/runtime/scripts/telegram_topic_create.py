#!/usr/bin/env python3
from __future__ import annotations

"""Create a Telegram forum topic via the installed OpenClaw Telegram provider.

This script is the canonical local wrapper for Telegram topic creation used by
runtime/bootstrap helpers. It isolates the provider-specific Node call behind a
small stable interface.
"""

import argparse
import json
import subprocess
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a Telegram forum topic")
    parser.add_argument("--chat-id", required=True, help="Telegram supergroup chat id")
    parser.add_argument("--title", required=True, help="Topic title")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script = f"""
import {{ createForumTopicTelegram }} from '/opt/homebrew/lib/node_modules/openclaw/dist/plugin-sdk/telegram.js';
const result = await createForumTopicTelegram({json.dumps(args.chat_id)}, {json.dumps(args.title)});
console.log(JSON.stringify(result));
"""
    proc = subprocess.run([
        "node",
        "--input-type=module",
        "--eval",
        script,
    ], text=True, capture_output=True)
    if proc.returncode != 0:
        print(proc.stderr.strip() or proc.stdout.strip() or "createForumTopicTelegram failed", file=sys.stderr)
        return 1
    out = proc.stdout.strip()
    if not out:
        print("{}")
        return 0
    data = json.loads(out.splitlines()[-1])
    if args.pretty:
        print(json.dumps(data, indent=2, sort_keys=True))
    else:
        print(json.dumps(data, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
