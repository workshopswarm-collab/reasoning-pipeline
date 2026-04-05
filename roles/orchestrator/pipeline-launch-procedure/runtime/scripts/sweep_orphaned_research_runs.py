#!/usr/bin/env python3
from __future__ import annotations

"""Detect and optionally repair orphaned/stale research-run state.

Goals:
- identify stale queued attempts that were never launched or got stuck before transitioning to `running`
- identify stranded researching cases with no active queued/running attempts
- optionally supersede stale queued attempts
- optionally attempt parent-case finalization from the newest terminal attempt
- optionally mark stranded researching parents as `needs_intervention`

This is intended as a deterministic control-plane repair helper for sequential
batch processing, not as a replacement for the main runtime loop.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
BASE_DIR = Path(__file__).resolve().parent
AUTO_FINALIZE = BASE_DIR / "internal" / "auto_finalize_case_after_terminal_run.py"

SQL = r'''
WITH case_rollup AS (
  SELECT
    c.id AS case_id,
    c.case_key,
    c.status AS case_status,
    m.id AS market_id,
    m.title AS market_title,
    m.pipeline_status,
    COALESCE(c.orchestration_notes->>'active_dispatch_id', '') AS active_dispatch_id,
    COUNT(*) FILTER (WHERE rr.status = 'queued') AS queued_count,
    COUNT(*) FILTER (WHERE rr.status = 'running') AS running_count,
    COUNT(*) FILTER (WHERE rr.status = 'completed') AS completed_count,
    COUNT(*) FILTER (WHERE rr.status = 'failed') AS failed_count,
    COUNT(*) FILTER (WHERE rr.status = 'superseded') AS superseded_count,
    MAX(rr.created_at) AS latest_run_created_at
  FROM cases c
  JOIN markets m ON m.id = c.market_id
  LEFT JOIN research_runs rr ON rr.case_id = c.id
  GROUP BY c.id, c.case_key, c.status, m.id, m.title, m.pipeline_status, COALESCE(c.orchestration_notes->>'active_dispatch_id', '')
),
queued AS (
  SELECT json_agg(json_build_object(
    'research_run_id', rr.id,
    'case_id', rr.case_id,
    'case_key', cr.case_key,
    'active_dispatch_id', cr.active_dispatch_id,
    'agent_label', rr.agent_label,
    'status', rr.status,
    'created_at', rr.created_at,
    'started_at', rr.started_at,
    'queued_started_without_running', (rr.started_at IS NOT NULL),
    'workspace_note_path', rr.workspace_note_path,
    'dispatch_id', rr.notes->>'dispatch_id',
    'has_delivery_metadata', (
      COALESCE(rr.notes->>'delivery_target_topic_id', '') <> ''
      OR COALESCE(rr.notes->>'delivery_target_session_key', '') <> ''
    ),
    'legacy_case_shell_eligible', (
      (
        COALESCE(rr.notes->>'delivery_target_topic_id', '') <> ''
        OR COALESCE(rr.notes->>'delivery_target_session_key', '') <> ''
      )
      AND COALESCE(cr.active_dispatch_id, '') = ''
    ),
    'auto_supersede_eligible', (
      NOT (
        COALESCE(rr.notes->>'delivery_target_topic_id', '') <> ''
        OR COALESCE(rr.notes->>'delivery_target_session_key', '') <> ''
      )
      OR COALESCE(cr.active_dispatch_id, '') = ''
    ),
    'case_running_count', cr.running_count,
    'case_completed_count', cr.completed_count,
    'case_failed_count', cr.failed_count,
    'market_pipeline_status', cr.pipeline_status
  ) ORDER BY rr.created_at ASC) AS rows
  FROM research_runs rr
  JOIN case_rollup cr ON cr.case_id = rr.case_id
  WHERE rr.status = 'queued'
    AND rr.created_at < NOW() - (:'queued_stale_minutes'::int || ' minutes')::interval
),
stranded_cases AS (
  SELECT json_agg(json_build_object(
    'case_id', cr.case_id,
    'case_key', cr.case_key,
    'case_status', cr.case_status,
    'market_id', cr.market_id,
    'market_title', cr.market_title,
    'pipeline_status', cr.pipeline_status,
    'active_dispatch_id', cr.active_dispatch_id,
    'queued_count', cr.queued_count,
    'running_count', cr.running_count,
    'completed_count', cr.completed_count,
    'failed_count', cr.failed_count,
    'superseded_count', cr.superseded_count,
    'latest_terminal_run_id', latest_terminal.id
  ) ORDER BY cr.case_key ASC) AS rows
  FROM case_rollup cr
  LEFT JOIN LATERAL (
    SELECT rr.id
    FROM research_runs rr
    WHERE rr.case_id = cr.case_id
      AND rr.status IN ('completed', 'failed')
    ORDER BY rr.completed_at DESC NULLS LAST, rr.created_at DESC, rr.id DESC
    LIMIT 1
  ) latest_terminal ON TRUE
  WHERE cr.case_status = 'open'
    AND cr.pipeline_status = 'researching'
    AND cr.queued_count = 0
    AND cr.running_count = 0
)
SELECT json_build_object(
  'stale_queued_runs', COALESCE((SELECT rows FROM queued), '[]'::json),
  'stranded_researching_cases', COALESCE((SELECT rows FROM stranded_cases), '[]'::json)
)::text;
'''

SUPERSEDE_SQL = r'''
WITH updated AS (
  UPDATE research_runs rr
  SET
    status = 'superseded',
    notes = COALESCE(rr.notes, '{}'::jsonb) || jsonb_build_object(
      'dispatch_stage', 'swept_stale_queued',
      'swept_at', NOW(),
      'swept_reason', CASE
        WHEN COALESCE(:'sweep_reason', '') <> '' THEN :'sweep_reason'
        ELSE 'stale_queued_without_launch'
      END
    )
  WHERE rr.id = NULLIF(:'research_run_id', '')::uuid
  RETURNING rr.id, rr.case_id, rr.agent_label, rr.status
)
SELECT json_build_object(
  'updated', EXISTS(SELECT 1 FROM updated),
  'research_run_id', (SELECT id FROM updated LIMIT 1),
  'case_id', (SELECT case_id FROM updated LIMIT 1),
  'agent_label', (SELECT agent_label FROM updated LIMIT 1),
  'status', (SELECT status FROM updated LIMIT 1)
)::text;
'''

MARK_NEEDS_INTERVENTION_SQL = r'''
WITH target AS (
  SELECT
    c.id AS case_id,
    c.market_id,
    c.case_key,
    c.status AS case_status,
    m.pipeline_status,
    COALESCE(c.orchestration_notes->>'active_dispatch_id', '') AS active_dispatch_id,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'queued')
      FROM research_runs r
      WHERE r.case_id = c.id
    ) AS queued_count,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'running')
      FROM research_runs r
      WHERE r.case_id = c.id
    ) AS running_count,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'completed')
      FROM research_runs r
      WHERE r.case_id = c.id
    ) AS completed_count,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'failed')
      FROM research_runs r
      WHERE r.case_id = c.id
    ) AS failed_count,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'superseded')
      FROM research_runs r
      WHERE r.case_id = c.id
    ) AS superseded_count,
    (
      SELECT COUNT(*)
      FROM research_runs r
      WHERE r.case_id = c.id
    ) AS total_count
  FROM cases c
  JOIN markets m ON m.id = c.market_id
  WHERE c.id = NULLIF(:'case_id', '')::uuid
  LIMIT 1
),
case_updated AS (
  UPDATE cases c
  SET orchestration_notes = COALESCE(c.orchestration_notes, '{}'::jsonb) || jsonb_build_object(
      'active_dispatch_id', NULLIF((SELECT active_dispatch_id FROM target LIMIT 1), ''),
      'repair_marked_at', NOW(),
      'swarm_terminal', true,
      'swarm_outcome', 'needs_intervention',
      'repair_reason', CASE
        WHEN COALESCE(:'repair_reason', '') <> '' THEN :'repair_reason'
        ELSE 'stale_researching_without_active_dispatch'
      END,
      'run_counts', jsonb_build_object(
        'queued', (SELECT queued_count FROM target LIMIT 1),
        'running', (SELECT running_count FROM target LIMIT 1),
        'completed', (SELECT completed_count FROM target LIMIT 1),
        'failed', (SELECT failed_count FROM target LIMIT 1),
        'superseded', (SELECT superseded_count FROM target LIMIT 1),
        'total', (SELECT total_count FROM target LIMIT 1)
      )
    )
  FROM target t
  WHERE c.id = t.case_id
    AND t.queued_count = 0
    AND t.running_count = 0
  RETURNING c.id, c.status, c.orchestration_notes
),
market_updated AS (
  UPDATE markets m
  SET pipeline_status = 'needs_intervention'::processing_status
  FROM target t
  WHERE m.id = t.market_id
    AND t.queued_count = 0
    AND t.running_count = 0
  RETURNING m.id, m.pipeline_status
)
SELECT json_build_object(
  'case_updated', EXISTS(SELECT 1 FROM case_updated),
  'market_updated', EXISTS(SELECT 1 FROM market_updated),
  'case_id', (SELECT case_id FROM target LIMIT 1),
  'case_key', (SELECT case_key FROM target LIMIT 1),
  'pipeline_status', COALESCE((SELECT pipeline_status FROM market_updated LIMIT 1), (SELECT pipeline_status FROM target LIMIT 1)),
  'counts', json_build_object(
    'queued', (SELECT queued_count FROM target LIMIT 1),
    'running', (SELECT running_count FROM target LIMIT 1),
    'completed', (SELECT completed_count FROM target LIMIT 1),
    'failed', (SELECT failed_count FROM target LIMIT 1),
    'superseded', (SELECT superseded_count FROM target LIMIT 1),
    'total', (SELECT total_count FROM target LIMIT 1)
  )
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sweep orphaned/stale research-run state")
    parser.add_argument("--queued-stale-minutes", type=int, default=90, help="Consider queued rows stale after this many minutes")
    parser.add_argument("--apply-supersede-stale-queued", action="store_true", help="Mark stale queued rows superseded")
    parser.add_argument("--apply-finalize-stranded-cases", action="store_true", help="Attempt parent finalization for researching cases with no queued/running attempts")
    parser.add_argument("--apply-mark-stranded-needs-intervention", action="store_true", help="Mark stranded researching parents as needs_intervention when no terminal run exists")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def exec_sql(psql_bin: str, db_url: str, sql_text: str, variables: dict[str, str]) -> dict[str, Any]:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")
    cmd = [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1"]
    for key, value in variables.items():
        cmd.extend(["-v", f"{key}={value}"])
    cmd.extend(["-f", "-"])
    proc = subprocess.run(cmd, input=sql_text, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    return json.loads(stdout.splitlines()[-1]) if stdout else {}


def python_json(script: Path, args: list[str]) -> dict[str, Any]:
    proc = subprocess.run([sys.executable, str(script), *args], text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"{script.name} failed")
    stdout = proc.stdout.strip()
    if not stdout:
        return {}
    for line in reversed([line for line in stdout.splitlines() if line.strip()]):
        try:
            return json.loads(line)
        except json.JSONDecodeError:
            continue
    return json.loads(stdout)


def snapshot_state(args: argparse.Namespace) -> dict[str, Any]:
    return exec_sql(
        args.psql,
        args.db_url,
        SQL,
        {"queued_stale_minutes": str(args.queued_stale_minutes)},
    )


def main() -> int:
    args = parse_args()
    try:
        snapshot = snapshot_state(args)
        stale_queued = snapshot.get("stale_queued_runs") or []
        stranded_cases = snapshot.get("stranded_researching_cases") or []

        superseded = []
        if args.apply_supersede_stale_queued:
            for row in stale_queued:
                if not row.get("auto_supersede_eligible"):
                    continue
                sweep_reason = (
                    "stale_started_or_queued_legacy_or_missing_active_dispatch"
                    if row.get("legacy_case_shell_eligible")
                    else ("stale_started_queued_without_launch" if row.get("queued_started_without_running") else "stale_queued_without_launch")
                )
                superseded.append(
                    exec_sql(
                        args.psql,
                        args.db_url,
                        SUPERSEDE_SQL,
                        {
                            "research_run_id": row["research_run_id"],
                            "sweep_reason": sweep_reason,
                        },
                    )
                )
            snapshot = snapshot_state(args)
            stale_queued = snapshot.get("stale_queued_runs") or []
            stranded_cases = snapshot.get("stranded_researching_cases") or []

        finalized = []
        intervention_marked = []
        if args.apply_finalize_stranded_cases or args.apply_mark_stranded_needs_intervention:
            for case in stranded_cases:
                if args.apply_finalize_stranded_cases and case.get("latest_terminal_run_id"):
                    finalized.append(
                        python_json(
                            AUTO_FINALIZE,
                            [
                                "--research-run-id", case["latest_terminal_run_id"],
                                "--db-url", args.db_url,
                                "--psql", args.psql,
                                "--pretty",
                            ],
                        )
                    )
                elif args.apply_mark_stranded_needs_intervention:
                    intervention_marked.append(
                        exec_sql(
                            args.psql,
                            args.db_url,
                            MARK_NEEDS_INTERVENTION_SQL,
                            {
                                "case_id": case["case_id"],
                                "repair_reason": "stale_researching_without_active_dispatch",
                            },
                        )
                    )
            snapshot = snapshot_state(args)
            stale_queued = snapshot.get("stale_queued_runs") or []
            stranded_cases = snapshot.get("stranded_researching_cases") or []

        result = {
            "status": "ok",
            "queued_stale_minutes": args.queued_stale_minutes,
            "stale_queued_runs": stale_queued,
            "stranded_researching_cases": stranded_cases,
            "superseded_results": superseded,
            "finalized_results": finalized,
            "marked_needs_intervention_results": intervention_marked,
        }
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
