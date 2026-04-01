#!/usr/bin/env python3
"""Automatically reconcile/finalize a dispatch once a run hits a terminal state.

Best-effort flow:
1. Load the run's case/market/dispatch context.
2. If a matching dispatch manifest can be found, run the standard manifest finalizer
   to repair artifact-vs-DB lag.
3. Reload sibling run counts for the case.
4. Close the parent case/market only when the full swarm has completed cleanly
   (all sibling runs are `completed`).

This is intentionally idempotent and safe to call after any terminal run update.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR.parent
RUNTIME_DIR = SCRIPTS_DIR.parent
DISPATCH_MANIFESTS_DIR = RUNTIME_DIR / "dispatch-manifests"
FINALIZE_DISPATCH = SCRIPTS_DIR / "runrepairs" / "finalize_dispatch_after_swarm.py"
PIPELINE_DIR = RUNTIME_DIR.parent
WORKSPACE_ROOT = PIPELINE_DIR.parents[2]
DEFAULT_ENV_PATH = WORKSPACE_ROOT / ".env"

SQL_CONTEXT = r'''
WITH target AS (
  SELECT
    rr.id,
    rr.case_id,
    rr.status,
    COALESCE(rr.notes->>'dispatch_id', '') AS dispatch_id,
    c.case_key,
    c.status AS case_status,
    c.market_id,
    m.status AS market_status,
    m.pipeline_status,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'queued')
      FROM research_runs r
      WHERE r.case_id = rr.case_id
    ) AS queued_count,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'running')
      FROM research_runs r
      WHERE r.case_id = rr.case_id
    ) AS running_count,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'completed')
      FROM research_runs r
      WHERE r.case_id = rr.case_id
    ) AS completed_count,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'failed')
      FROM research_runs r
      WHERE r.case_id = rr.case_id
    ) AS failed_count,
    (
      SELECT COUNT(*)
      FROM research_runs r
      WHERE r.case_id = rr.case_id
    ) AS total_count
  FROM research_runs rr
  JOIN cases c ON c.id = rr.case_id
  JOIN markets m ON m.id = c.market_id
  WHERE rr.id = NULLIF(:'research_run_id', '')::uuid
)
SELECT json_build_object(
  'research_run_id', id,
  'case_id', case_id,
  'status', status,
  'dispatch_id', NULLIF(dispatch_id, ''),
  'case_key', case_key,
  'case_status', case_status,
  'market_id', market_id,
  'market_status', market_status,
  'pipeline_status', pipeline_status,
  'counts', json_build_object(
    'queued', queued_count,
    'running', running_count,
    'completed', completed_count,
    'failed', failed_count,
    'total', total_count
  )
)::text
FROM target;
'''

SQL_CLOSE_PARENT = r'''
WITH target AS (
  SELECT
    rr.case_id,
    c.market_id,
    c.case_key,
    c.status AS case_status,
    m.pipeline_status,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'queued')
      FROM research_runs r
      WHERE r.case_id = rr.case_id
    ) AS queued_count,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'running')
      FROM research_runs r
      WHERE r.case_id = rr.case_id
    ) AS running_count,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'completed')
      FROM research_runs r
      WHERE r.case_id = rr.case_id
    ) AS completed_count,
    (
      SELECT COUNT(*) FILTER (WHERE r.status = 'failed')
      FROM research_runs r
      WHERE r.case_id = rr.case_id
    ) AS failed_count,
    (
      SELECT COUNT(*)
      FROM research_runs r
      WHERE r.case_id = rr.case_id
    ) AS total_count
  FROM research_runs rr
  JOIN cases c ON c.id = rr.case_id
  JOIN markets m ON m.id = c.market_id
  WHERE rr.id = NULLIF(:'research_run_id', '')::uuid
  LIMIT 1
),
case_completed AS (
  UPDATE cases c
  SET
    status = 'closed',
    closed_at = COALESCE(c.closed_at, NOW()),
    orchestration_notes = COALESCE(c.orchestration_notes, '{}'::jsonb) || jsonb_build_object(
      'auto_finalized_at', NOW(),
      'swarm_terminal', true,
      'swarm_outcome', 'completed',
      'run_counts', jsonb_build_object(
        'queued', t.queued_count,
        'running', t.running_count,
        'completed', t.completed_count,
        'failed', t.failed_count,
        'total', t.total_count
      )
    )
  FROM target t
  WHERE c.id = t.case_id
    AND t.queued_count = 0
    AND t.running_count = 0
    AND t.completed_count = t.total_count
  RETURNING c.id, c.status, c.closed_at, c.orchestration_notes
),
case_intervention AS (
  UPDATE cases c
  SET orchestration_notes = COALESCE(c.orchestration_notes, '{}'::jsonb) || jsonb_build_object(
      'auto_finalized_at', NOW(),
      'swarm_terminal', true,
      'swarm_outcome', 'needs_intervention',
      'run_counts', jsonb_build_object(
        'queued', t.queued_count,
        'running', t.running_count,
        'completed', t.completed_count,
        'failed', t.failed_count,
        'total', t.total_count
      )
    )
  FROM target t
  WHERE c.id = t.case_id
    AND t.queued_count = 0
    AND t.running_count = 0
    AND t.completed_count < t.total_count
  RETURNING c.id, c.status, c.closed_at, c.orchestration_notes
),
market_completed AS (
  UPDATE markets m
  SET pipeline_status = 'closed'::processing_status
  FROM target t
  WHERE m.id = t.market_id
    AND t.queued_count = 0
    AND t.running_count = 0
    AND t.completed_count = t.total_count
  RETURNING m.id, m.pipeline_status
),
market_intervention AS (
  UPDATE markets m
  SET pipeline_status = 'needs_intervention'::processing_status
  FROM target t
  WHERE m.id = t.market_id
    AND t.queued_count = 0
    AND t.running_count = 0
    AND t.completed_count < t.total_count
  RETURNING m.id, m.pipeline_status
)
SELECT json_build_object(
  'case_updated', EXISTS(SELECT 1 FROM case_completed) OR EXISTS(SELECT 1 FROM case_intervention),
  'market_updated', EXISTS(SELECT 1 FROM market_completed) OR EXISTS(SELECT 1 FROM market_intervention),
  'all_completed', COALESCE((SELECT completed_count = total_count FROM target LIMIT 1), false),
  'needs_intervention', COALESCE((SELECT completed_count < total_count AND queued_count = 0 AND running_count = 0 FROM target LIMIT 1), false),
  'case_status', COALESCE((SELECT status FROM case_completed LIMIT 1), (SELECT status FROM case_intervention LIMIT 1), (SELECT case_status FROM target LIMIT 1)),
  'pipeline_status', COALESCE((SELECT pipeline_status FROM market_completed LIMIT 1), (SELECT pipeline_status FROM market_intervention LIMIT 1), (SELECT pipeline_status FROM target LIMIT 1)),
  'counts', json_build_object(
    'queued', (SELECT queued_count FROM target LIMIT 1),
    'running', (SELECT running_count FROM target LIMIT 1),
    'completed', (SELECT completed_count FROM target LIMIT 1),
    'failed', (SELECT failed_count FROM target LIMIT 1),
    'total', (SELECT total_count FROM target LIMIT 1)
  )
)::text;
'''


def maybe_load_workspace_env() -> None:
    if os.getenv("PREDQUANT_ORCHESTRATOR_URL"):
        return
    if not DEFAULT_ENV_PATH.exists():
        return
    for raw_line in DEFAULT_ENV_PATH.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Auto-finalize a case after a terminal run update")
    parser.add_argument("--research-run-id", required=True, help="research_runs UUID")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def run_psql(psql_bin: str, db_url: str, sql: str, *, vars_map: dict[str, str]) -> dict:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")
    cmd = [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1"]
    for key, value in vars_map.items():
        cmd.extend(["-v", f"{key}={value}"])
    proc = subprocess.run(cmd + ["-f", "-"], input=sql, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    if not stdout:
        return {}
    return json.loads(stdout.splitlines()[-1])


def python_json(script: Path, args: list[str]) -> dict:
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


def find_manifest(dispatch_id: str | None) -> Path | None:
    if not dispatch_id:
        return None
    direct = DISPATCH_MANIFESTS_DIR / f"{dispatch_id}.json"
    if direct.exists():
        return direct
    matches = sorted(DISPATCH_MANIFESTS_DIR.glob(f"**/{dispatch_id}.json"))
    return matches[-1] if matches else None


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    try:
        context = run_psql(
            args.psql,
            args.db_url,
            SQL_CONTEXT,
            vars_map={"research_run_id": args.research_run_id},
        )
        if not context:
            raise ValueError("research run not found")

        manifest_path = find_manifest(context.get("dispatch_id"))
        finalize_result = None
        finalize_error = None
        if manifest_path is not None:
            os.environ["ORCHESTRATOR_SKIP_AUTO_FINALIZE"] = "1"
            try:
                finalize_result = python_json(
                    FINALIZE_DISPATCH,
                    ["--file", str(manifest_path), "--apply"],
                )
            except Exception as exc:  # noqa: BLE001
                finalize_error = str(exc)

        post_context = run_psql(
            args.psql,
            args.db_url,
            SQL_CONTEXT,
            vars_map={"research_run_id": args.research_run_id},
        )
        close_result = run_psql(
            args.psql,
            args.db_url,
            SQL_CLOSE_PARENT,
            vars_map={"research_run_id": args.research_run_id},
        )

        output = {
            "research_run_id": args.research_run_id,
            "dispatch_id": context.get("dispatch_id"),
            "manifest_path": str(manifest_path) if manifest_path else None,
            "manifest_finalizer": finalize_result,
            "manifest_finalizer_error": finalize_error,
            "post_reconcile_counts": (post_context or {}).get("counts") or {},
            "parent_finalize": close_result,
            "all_terminal": ((post_context or {}).get("counts") or {}).get("queued", 0) == 0
            and ((post_context or {}).get("counts") or {}).get("running", 0) == 0,
        }
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(output, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(output, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
