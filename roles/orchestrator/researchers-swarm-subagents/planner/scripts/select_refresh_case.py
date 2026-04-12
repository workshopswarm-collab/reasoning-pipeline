#!/usr/bin/env python3
"""Select the next tracked market that should be refreshed after a material market move.

Behavior:
- consider tracked markets back in `pipeline_status = pending_research`
- require an existing latest forecast row for the market/contract
- require a material absolute move versus `markets.last_reasoned_price`
- skip markets that already have queued/running research attempts on an open case
- by default, refuse selection while another case is actively researching
- if an open case exists, include it; otherwise return market identity so the caller can open a fresh case

Uses PREDQUANT_ORCHESTRATOR_URL by default.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

WORKSPACE_ROOT = Path(__file__).resolve().parents[5]
if str(WORKSPACE_ROOT / 'scripts') not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT / 'scripts'))

from case_pipeline_status import first_active_nonterminal_case, first_blocking_case_without_completed_decision_packet  # noqa: E402

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

BUSY_SQL = r'''
SELECT json_build_object(
  'pipeline_busy', EXISTS (
    SELECT 1
    FROM cases c
    JOIN markets m ON m.id = c.market_id
    WHERE c.status = 'open'
      AND m.pipeline_status = 'researching'
  )
)::text;
'''

SQL = r'''
WITH params AS (
  SELECT
    COALESCE(NULLIF(:'excluded_market_ids', ''), '[]')::jsonb AS excluded_market_ids,
    COALESCE(NULLIF(:'excluded_case_keys', ''), '[]')::jsonb AS excluded_case_keys
),
busy AS (
  SELECT EXISTS (
    SELECT 1
    FROM cases c
    JOIN markets m ON m.id = c.market_id
    WHERE c.status = 'open'
      AND m.pipeline_status = 'researching'
  ) AS pipeline_busy
),
latest_yes AS (
  SELECT *
  FROM public.latest_forecast_decisions
  WHERE contract_id = COALESCE(NULLIF(:'contract_id', ''), 'yes')
),
latest_open_case AS (
  SELECT DISTINCT ON (c.market_id)
    c.market_id,
    c.id AS case_id,
    c.case_key,
    c.priority,
    c.opened_at
  FROM cases c
  WHERE c.status = 'open'
  ORDER BY c.market_id, c.opened_at DESC, c.id DESC
),
eligible AS (
  SELECT
    loc.case_id,
    loc.case_key,
    loc.priority,
    m.id AS market_id,
    m.platform,
    m.external_market_id,
    m.slug,
    m.title,
    m.description,
    m.category,
    m.status AS market_status,
    m.outcome_type,
    m.closes_at,
    m.resolves_at,
    m.pipeline_status,
    m.current_price,
    m.last_reasoned_price,
    ABS(m.current_price - m.last_reasoned_price) AS price_delta,
    ly.forecast_id,
    ly.case_id AS latest_forecast_case_key,
    ly.decision_ts AS last_forecast_ts,
    ROUND(EXTRACT(EPOCH FROM (NOW() - ly.decision_ts)) / 3600.0, 2) AS hours_since_last_forecast,
    ROUND(EXTRACT(EPOCH FROM (m.closes_at - NOW())) / 3600.0, 2) AS hours_to_close,
    ly.forecast_prob,
    ly.decision_status AS last_forecast_status,
    ly.resolution_status
  FROM markets m
  JOIN latest_yes ly ON ly.market_id = m.id::text
  LEFT JOIN latest_open_case loc ON loc.market_id = m.id
  CROSS JOIN busy b
  CROSS JOIN params p
  WHERE (COALESCE(:'allow_when_busy', '') = 'true' OR b.pipeline_busy = false)
    AND NOT (p.excluded_market_ids ? (m.id::text))
    AND NOT (loc.case_key IS NOT NULL AND p.excluded_case_keys ? loc.case_key)
    AND NOT (ly.case_id IS NOT NULL AND p.excluded_case_keys ? ly.case_id)
    AND m.platform = COALESCE(NULLIF(:'platform', ''), 'polymarket')
    AND m.status = 'open'
    AND m.pipeline_status = 'pending_research'
    AND (m.closes_at IS NULL OR m.closes_at > NOW())
    AND (m.resolves_at IS NULL OR m.resolves_at > NOW())
    AND m.current_price IS NOT NULL
    AND m.last_reasoned_price IS NOT NULL
    AND ABS(m.current_price - m.last_reasoned_price) >= NULLIF(:'min_price_delta', '')::numeric
    AND COALESCE(ly.resolution_status, '') <> 'resolved'
    AND NOT EXISTS (
      SELECT 1
      FROM research_runs rr
      JOIN cases c2 ON c2.id = rr.case_id
      WHERE c2.market_id = m.id
        AND c2.status = 'open'
        AND rr.status IN ('queued', 'running')
    )
),
ranked AS (
  SELECT *
  FROM eligible
  ORDER BY
    price_delta DESC,
    closes_at ASC NULLS LAST,
    last_forecast_ts ASC,
    market_id ASC
  LIMIT 1
)
SELECT json_build_object(
  'case_id', case_id,
  'case_key', case_key,
  'priority', priority,
  'market_id', market_id,
  'platform', platform,
  'external_market_id', external_market_id,
  'slug', slug,
  'title', title,
  'description', description,
  'category', category,
  'market_status', market_status,
  'outcome_type', outcome_type,
  'closes_at', closes_at,
  'resolves_at', resolves_at,
  'pipeline_status', pipeline_status,
  'current_price', current_price,
  'last_reasoned_price', last_reasoned_price,
  'price_delta', price_delta,
  'forecast_id', forecast_id,
  'latest_forecast_case_key', latest_forecast_case_key,
  'last_forecast_ts', last_forecast_ts,
  'hours_since_last_forecast', hours_since_last_forecast,
  'hours_to_close', hours_to_close,
  'forecast_prob', forecast_prob,
  'last_forecast_status', last_forecast_status
)::text
FROM ranked;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Select the next tracked market to refresh after a material market move")
    parser.add_argument("--platform", default="polymarket")
    parser.add_argument("--contract-id", default="yes")
    parser.add_argument("--min-price-delta", default="0.05")
    parser.add_argument("--allow-when-busy", action="store_true")
    parser.add_argument("--exclude-market-id", action="append", default=[])
    parser.add_argument("--exclude-case-key", action="append", default=[])
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON result")
    return parser.parse_args()


def run_query(psql_bin: str, db_url: str, sql_text: str, *, allow_when_busy: bool, platform: str, contract_id: str, min_price_delta: str, excluded_market_ids: list[str], excluded_case_keys: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        [
            psql_bin,
            db_url,
            "-X",
            "-qAt",
            "-v",
            "ON_ERROR_STOP=1",
            "-v",
            f"allow_when_busy={'true' if allow_when_busy else 'false'}",
            "-v",
            f"platform={platform}",
            "-v",
            f"contract_id={contract_id}",
            "-v",
            f"min_price_delta={min_price_delta}",
            "-v",
            f"excluded_market_ids={json.dumps(sorted(set(excluded_market_ids)), separators=(',', ':'))}",
            "-v",
            f"excluded_case_keys={json.dumps(sorted(set(excluded_case_keys)), separators=(',', ':'))}",
            "-f",
            "-",
        ],
        input=sql_text,
        text=True,
        capture_output=True,
    )


def enforce_canonical_case_gate(*, allow_when_busy: bool) -> None:
    if allow_when_busy:
        return
    active_case = first_active_nonterminal_case()
    if active_case:
        raise ValueError(
            'pipeline already busy with a canonical non-terminal case '
            f"(case_key={active_case.get('case_key')}, status={active_case.get('status')}, current_stage={active_case.get('current_stage')})"
        )
    blocking_case = first_blocking_case_without_completed_decision_packet()
    if blocking_case:
        raise ValueError(
            'pipeline blocked by prior canonical case without clean decision-packet completion '
            f"(case_key={blocking_case.get('case_key')}, status={blocking_case.get('status')})"
        )



def run_psql(psql_bin: str, db_url: str, *, allow_when_busy: bool, platform: str, contract_id: str, min_price_delta: str, excluded_market_ids: list[str], excluded_case_keys: list[str]) -> dict:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")

    enforce_canonical_case_gate(allow_when_busy=allow_when_busy)

    proc = run_query(psql_bin, db_url, SQL, allow_when_busy=allow_when_busy, platform=platform, contract_id=contract_id, min_price_delta=min_price_delta, excluded_market_ids=excluded_market_ids, excluded_case_keys=excluded_case_keys)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")

    stdout = proc.stdout.strip()
    if not stdout:
        busy = run_query(psql_bin, db_url, BUSY_SQL, allow_when_busy=allow_when_busy, platform=platform, contract_id=contract_id, min_price_delta=min_price_delta, excluded_market_ids=excluded_market_ids, excluded_case_keys=excluded_case_keys)
        if busy.returncode == 0 and busy.stdout.strip():
            payload = json.loads(busy.stdout.splitlines()[-1])
            if payload.get("pipeline_busy") and not allow_when_busy:
                raise ValueError("pipeline already busy with an open researching case")
        raise ValueError("no eligible refresh market found")

    return json.loads(stdout.splitlines()[-1])


def main() -> int:
    args = parse_args()
    try:
        result = run_psql(
            args.psql,
            args.db_url,
            allow_when_busy=args.allow_when_busy,
            platform=args.platform,
            contract_id=args.contract_id,
            min_price_delta=args.min_price_delta,
            excluded_market_ids=args.exclude_market_id,
            excluded_case_keys=args.exclude_case_key,
        )
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
