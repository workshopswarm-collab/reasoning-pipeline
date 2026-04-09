#!/usr/bin/env python3
from __future__ import annotations

"""Summarize pipeline health/anomalies for operator use.

This is a read-only report intended to make high-volume automation safer by
surfacing the classes of drift that should block or repair sequential batch
processing.
"""

import argparse
import json
import os
import subprocess
import sys

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

SQL = r'''
WITH case_rollup AS (
  SELECT
    c.id AS case_id,
    c.case_key,
    c.status AS case_status,
    m.id AS market_id,
    m.title,
    m.pipeline_status,
    COALESCE(c.orchestration_notes->>'active_dispatch_id', '') AS active_dispatch_id,
    COUNT(*) FILTER (WHERE rr.status = 'queued') AS queued_count,
    COUNT(*) FILTER (WHERE rr.status = 'running') AS running_count,
    COUNT(*) FILTER (WHERE rr.status = 'completed') AS completed_count,
    COUNT(*) FILTER (WHERE rr.status = 'failed') AS failed_count,
    COUNT(*) FILTER (WHERE rr.status = 'superseded') AS superseded_count
  FROM cases c
  JOIN markets m ON m.id = c.market_id
  LEFT JOIN research_runs rr ON rr.case_id = c.id
  GROUP BY c.id, c.case_key, c.status, m.id, m.title, m.pipeline_status, COALESCE(c.orchestration_notes->>'active_dispatch_id', '')
),
summary AS (
  SELECT json_build_object(
    'markets_by_pipeline_status', (
      SELECT COALESCE(json_object_agg(pipeline_status, count_rows), '{}'::json)
      FROM (
        SELECT pipeline_status::text, COUNT(*) AS count_rows
        FROM markets
        GROUP BY pipeline_status
      ) x
    ),
    'expired_open_new_markets', (
      SELECT COUNT(*)
      FROM markets m
      WHERE m.status = 'open'
        AND m.pipeline_status = 'new'
        AND (
          (m.closes_at IS NOT NULL AND m.closes_at <= NOW())
          OR (m.resolves_at IS NOT NULL AND m.resolves_at <= NOW())
        )
    ),
    'cases_by_status', (
      SELECT COALESCE(json_object_agg(status, count_rows), '{}'::json)
      FROM (
        SELECT status, COUNT(*) AS count_rows
        FROM cases
        GROUP BY status
      ) x
    ),
    'research_runs_by_status', (
      SELECT COALESCE(json_object_agg(status, count_rows), '{}'::json)
      FROM (
        SELECT status, COUNT(*) AS count_rows
        FROM research_runs
        GROUP BY status
      ) x
    )
  ) AS body
),
state_buckets AS (
  SELECT json_build_object(
    'actively_running_cases', (
      SELECT COUNT(*)
      FROM case_rollup cr
      WHERE cr.case_status = 'open'
        AND cr.pipeline_status = 'researching'
        AND cr.running_count > 0
    ),
    'researching_markets_without_open_case', (
      SELECT COUNT(*)
      FROM markets m
      WHERE m.pipeline_status = 'researching'
        AND NOT EXISTS (
          SELECT 1
          FROM cases c
          WHERE c.market_id = m.id
            AND c.status = 'open'
        )
    ),
    'expired_open_new_markets', (
      SELECT COUNT(*)
      FROM markets m
      WHERE m.status = 'open'
        AND m.pipeline_status = 'new'
        AND (
          (m.closes_at IS NOT NULL AND m.closes_at <= NOW())
          OR (m.resolves_at IS NOT NULL AND m.resolves_at <= NOW())
        )
    ),
    'prepared_dispatches_waiting_launch', (
      SELECT COUNT(*)
      FROM case_rollup cr
      WHERE cr.case_status = 'open'
        AND cr.pipeline_status = 'researching'
        AND cr.running_count = 0
        AND cr.queued_count > 0
        AND cr.active_dispatch_id <> ''
    ),
    'stale_researching_cases_missing_active_dispatch', (
      SELECT COUNT(*)
      FROM case_rollup cr
      WHERE cr.case_status = 'open'
        AND cr.pipeline_status = 'researching'
        AND cr.running_count = 0
        AND cr.queued_count > 0
        AND cr.active_dispatch_id = ''
    ),
    'terminal_researching_cases', (
      SELECT COUNT(*)
      FROM case_rollup cr
      WHERE cr.case_status = 'open'
        AND cr.pipeline_status = 'researching'
        AND cr.running_count = 0
        AND cr.queued_count = 0
        AND (cr.completed_count > 0 OR cr.failed_count > 0)
    )
  ) AS body
),
anomalies AS (
  SELECT json_build_object(
    'researching_cases_with_no_active_attempts', (
      SELECT COUNT(*)
      FROM case_rollup cr
      WHERE cr.case_status = 'open'
        AND cr.pipeline_status = 'researching'
        AND cr.queued_count = 0
        AND cr.running_count = 0
    ),
    'duplicate_active_case_persona_attempts', (
      SELECT COUNT(*)
      FROM (
        SELECT case_id, agent_label
        FROM research_runs
        WHERE status IN ('queued', 'running')
        GROUP BY case_id, agent_label
        HAVING COUNT(*) > 1
      ) x
    ),
    'closed_cases_with_active_attempts', (
      SELECT COUNT(*)
      FROM cases c
      WHERE c.status = 'closed'
        AND EXISTS (
          SELECT 1 FROM research_runs rr
          WHERE rr.case_id = c.id AND rr.status IN ('queued', 'running')
        )
    ),
    'queued_without_delivery_metadata', (
      SELECT COUNT(*)
      FROM research_runs rr
      WHERE rr.status = 'queued'
        AND rr.started_at IS NULL
        AND COALESCE(rr.notes->>'delivery_target_topic_id', '') = ''
        AND COALESCE(rr.notes->>'delivery_target_session_key', '') = ''
    ),
    'queued_started_without_running', (
      SELECT COUNT(*)
      FROM research_runs rr
      WHERE rr.status = 'queued'
        AND rr.started_at IS NOT NULL
    ),
    'open_researching_cases_missing_active_dispatch', (
      SELECT COUNT(*)
      FROM case_rollup cr
      WHERE cr.case_status = 'open'
        AND cr.pipeline_status = 'researching'
        AND cr.active_dispatch_id = ''
    ),
    'researching_markets_without_open_case', (
      SELECT COUNT(*)
      FROM markets m
      WHERE m.pipeline_status = 'researching'
        AND NOT EXISTS (
          SELECT 1
          FROM cases c
          WHERE c.market_id = m.id
            AND c.status = 'open'
        )
    ),
    'open_new_markets_past_close_or_resolve', (
      SELECT COUNT(*)
      FROM markets m
      WHERE m.status = 'open'
        AND m.pipeline_status = 'new'
        AND (
          (m.closes_at IS NOT NULL AND m.closes_at <= NOW())
          OR (m.resolves_at IS NOT NULL AND m.resolves_at <= NOW())
        )
    )
  ) AS body
),
anomaly_samples AS (
  SELECT json_build_object(
    'researching_markets_without_open_case', (
      SELECT COALESCE(json_agg(row_to_json(x) ORDER BY x.updated_at DESC NULLS LAST), '[]'::json)
      FROM (
        SELECT m.id AS market_id, m.title, m.status, m.pipeline_status, m.closes_at, m.resolves_at, m.updated_at
        FROM markets m
        WHERE m.pipeline_status = 'researching'
          AND NOT EXISTS (
            SELECT 1
            FROM cases c
            WHERE c.market_id = m.id
              AND c.status = 'open'
          )
        ORDER BY m.updated_at DESC NULLS LAST, m.id ASC
        LIMIT 10
      ) x
    ),
    'open_new_markets_past_close_or_resolve', (
      SELECT COALESCE(json_agg(row_to_json(x) ORDER BY x.closes_at DESC NULLS LAST, x.updated_at DESC NULLS LAST), '[]'::json)
      FROM (
        SELECT m.id AS market_id, m.title, m.status, m.pipeline_status, m.closes_at, m.resolves_at, m.updated_at
        FROM markets m
        WHERE m.status = 'open'
          AND m.pipeline_status = 'new'
          AND (
            (m.closes_at IS NOT NULL AND m.closes_at <= NOW())
            OR (m.resolves_at IS NOT NULL AND m.resolves_at <= NOW())
          )
        ORDER BY m.closes_at DESC NULLS LAST, m.updated_at DESC NULLS LAST, m.id ASC
        LIMIT 10
      ) x
    )
  ) AS body
)
SELECT json_build_object(
  'summary', (SELECT body FROM summary),
  'state_buckets', (SELECT body FROM state_buckets),
  'anomalies', (SELECT body FROM anomalies),
  'anomaly_samples', (SELECT body FROM anomaly_samples)
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Report pipeline health/anomalies")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.db_url:
        print("ERROR: --db-url or PREDQUANT_ORCHESTRATOR_URL is required", file=sys.stderr)
        return 1
    proc = subprocess.run([args.psql, args.db_url, '-X', '-qAt', '-v', 'ON_ERROR_STOP=1', '-f', '-'], input=SQL, text=True, capture_output=True)
    if proc.returncode != 0:
        print(f"ERROR: {proc.stderr.strip() or 'psql failed'}", file=sys.stderr)
        return 1
    stdout = proc.stdout.strip()
    payload = json.loads(stdout.splitlines()[-1]) if stdout else {}
    if args.pretty:
        print(json.dumps(payload, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(payload, separators=(',', ':'), default=str))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
