#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

SQL = r'''
WITH market_input AS (
  SELECT (:'payload'::jsonb) AS j
),
snapshot_input AS (
  SELECT (:'snapshot'::jsonb) AS s
),
upserted_market AS (
  INSERT INTO markets (
    platform,
    external_market_id,
    slug,
    title,
    description,
    category,
    status,
    outcome_type,
    closes_at,
    resolves_at,
    metadata,
    current_price,
    updated_at
  )
  SELECT
    j->>'platform',
    j->>'external_market_id',
    NULLIF(j->>'slug', ''),
    j->>'title',
    NULLIF(j->>'description', ''),
    NULLIF(j->>'category', ''),
    COALESCE(NULLIF(j->>'status', ''), 'open'),
    NULLIF(j->>'outcome_type', ''),
    NULLIF(j->>'closes_at', '')::timestamptz,
    NULLIF(j->>'resolves_at', '')::timestamptz,
    COALESCE(j->'metadata', '{}'::jsonb),
    (s->>'yes_price')::numeric,
    NOW()
  FROM market_input
  CROSS JOIN snapshot_input s
  ON CONFLICT (platform, external_market_id)
  DO UPDATE SET
    slug = EXCLUDED.slug,
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    category = EXCLUDED.category,
    status = EXCLUDED.status,
    outcome_type = EXCLUDED.outcome_type,
    closes_at = EXCLUDED.closes_at,
    resolves_at = EXCLUDED.resolves_at,
    metadata = EXCLUDED.metadata,
    updated_at = NOW(),
    
    -- Use EXCLUDED to reference the new price we tried to insert
    current_price = EXCLUDED.current_price,
    
    pipeline_status = CASE 
        WHEN (
            (EXCLUDED.closes_at IS NOT NULL AND EXCLUDED.closes_at <= NOW())
            OR (EXCLUDED.resolves_at IS NOT NULL AND EXCLUDED.resolves_at <= NOW())
        )
        AND markets.pipeline_status IN ('new', 'pending_research')
        THEN 'closed'::processing_status
        WHEN (
            (EXCLUDED.closes_at IS NOT NULL AND EXCLUDED.closes_at <= NOW())
            OR (EXCLUDED.resolves_at IS NOT NULL AND EXCLUDED.resolves_at <= NOW())
        )
        AND markets.pipeline_status = 'researching'
        AND NOT EXISTS (
            SELECT 1
            FROM cases c
            WHERE c.market_id = markets.id
              AND c.status = 'open'
        )
        THEN 'closed'::processing_status
        WHEN markets.pipeline_status IN ('ignored', 'executed') 
             AND ABS(COALESCE(markets.last_reasoned_price, 0) - EXCLUDED.current_price) >= 0.05 
        THEN 'pending_research'::processing_status
        ELSE markets.pipeline_status
    END
  RETURNING id
),
inserted_snapshot AS (
  INSERT INTO market_snapshots (
    market_id,
    observed_at,
    last_price,
    best_bid,
    best_ask,
    yes_price,
    no_price,
    volume,
    open_interest,
    raw_payload
  )
  SELECT
    um.id,
    COALESCE(NULLIF(s->>'observed_at', '')::timestamptz, NOW()),
    NULLIF(s->>'last_price', '')::numeric,
    NULLIF(s->>'best_bid', '')::numeric,
    NULLIF(s->>'best_ask', '')::numeric,
    NULLIF(s->>'yes_price', '')::numeric,
    NULLIF(s->>'no_price', '')::numeric,
    NULLIF(s->>'volume', '')::numeric,
    NULLIF(s->>'open_interest', '')::numeric,
    COALESCE(s->'raw_payload', '{}'::jsonb)
  FROM upserted_market um
  CROSS JOIN snapshot_input s
  RETURNING id, market_id, observed_at
)
SELECT json_build_object(
  'market_id', market_id,
  'snapshot_id', id,
  'observed_at', observed_at
)::text
FROM inserted_snapshot;
'''

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Upsert one market and insert one market snapshot")
    parser.add_argument("--file", default="-", help="Path to input JSON file, or - for stdin")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_INGEST_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON result")
    return parser.parse_args()

def load_json(path_str: str):
    if path_str == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path_str).read_text()
    if not raw.strip():
        raise ValueError("input JSON is empty")
    return json.loads(raw)

def normalize_payload(payload: dict) -> tuple[dict, dict]:
    required = ["platform", "external_market_id", "title"]
    missing = [key for key in required if not payload.get(key)]
    if missing:
        raise ValueError(f"missing required fields: {', '.join(missing)}")
    payload.setdefault("metadata", {})
    snapshot = payload.get("snapshot") or {}
    if not snapshot.get("observed_at"):
        snapshot["observed_at"] = datetime.now(timezone.utc).isoformat()
    return payload, snapshot

def run_psql(psql_bin: str, db_url: str, payload: dict, snapshot: dict) -> dict:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_INGEST_URL is required")
    payload_json = json.dumps(payload, separators=(",", ":"))
    snapshot_json = json.dumps(snapshot, separators=(",", ":"))
    proc = subprocess.run(
        [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1",
         "-v", f"payload={payload_json}", "-v", f"snapshot={snapshot_json}", "-f", "-"],
        input=SQL, text=True, capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    line = proc.stdout.strip().splitlines()[-1]
    return json.loads(line)

def main() -> int:
    args = parse_args()
    try:
        payload = load_json(args.file)
        payload, snapshot = normalize_payload(payload)
        result = run_psql(args.psql, args.db_url, payload, snapshot)
        if args.pretty:
            print(json.dumps(result, indent=2, sort_keys=True))
        else:
            print(json.dumps(result, separators=(",", ":")))
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())