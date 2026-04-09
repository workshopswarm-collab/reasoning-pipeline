#!/usr/bin/env python3
"""Merge JSON into cases.orchestration_notes for one case.

Uses PREDQUANT_ORCHESTRATOR_URL by default.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

SQL = r'''
WITH input AS (
  SELECT (:'payload'::jsonb) AS j
),
updated AS (
  UPDATE cases c
  SET orchestration_notes = COALESCE(c.orchestration_notes, '{}'::jsonb) || COALESCE((SELECT j->'orchestration_notes' FROM input), '{}'::jsonb)
  FROM input i
  WHERE c.id = NULLIF(i.j->>'case_id', '')::uuid
  RETURNING c.id, c.case_key, c.status, c.orchestration_notes
)
SELECT json_build_object(
  'case_id', id,
  'case_key', case_key,
  'status', status,
  'orchestration_notes', orchestration_notes
)::text
FROM updated;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update one case orchestration_notes JSONB")
    parser.add_argument("--file", default="-", help="Path to input JSON file, or - for stdin")
    parser.add_argument("--case-id", help="cases UUID")
    parser.add_argument("--orchestration-notes-json", help="JSON object to merge into orchestration_notes")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON result")
    return parser.parse_args()


def load_json(path_str: str):
    if path_str == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path_str).read_text()
    if not raw.strip():
        return {}
    return json.loads(raw)


def build_payload(args: argparse.Namespace) -> dict:
    payload = load_json(args.file)
    if payload and not isinstance(payload, dict):
        raise ValueError("input JSON must be an object")

    payload = dict(payload or {})

    if args.case_id:
        payload["case_id"] = args.case_id
    if args.orchestration_notes_json:
        payload["orchestration_notes"] = json.loads(args.orchestration_notes_json)

    if not payload.get("case_id"):
        raise ValueError("case_id is required")
    if not isinstance(payload.get("orchestration_notes"), dict):
        raise ValueError("orchestration_notes must be a JSON object")

    return payload


def run_psql(psql_bin: str, db_url: str, payload: dict) -> dict:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")

    payload_json = json.dumps(payload, separators=(",", ":"))

    proc = subprocess.run(
        [
            psql_bin,
            db_url,
            "-X",
            "-qAt",
            "-v",
            "ON_ERROR_STOP=1",
            "-v",
            f"payload={payload_json}",
            "-f",
            "-",
        ],
        input=SQL,
        text=True,
        capture_output=True,
    )

    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")

    stdout = proc.stdout.strip()
    if not stdout:
        raise ValueError("case not found or not updated")

    return json.loads(stdout.splitlines()[-1])


def main() -> int:
    args = parse_args()
    try:
        payload = build_payload(args)
        result = run_psql(args.psql, args.db_url, payload)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(result, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
