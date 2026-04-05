#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
BASE_DIR = Path(__file__).resolve().parent
SELECT_NEXT = BASE_DIR.parents[1] / "planner" / "scripts" / "select_next_market.py"
PREPARE_AND_LAUNCH = BASE_DIR / "prepare_and_launch_headless_telegram_dispatch.py"
ANOMALY_REPORT = BASE_DIR / "pipeline_anomaly_report.py"
SWEEP_ORPHANS = BASE_DIR / "sweep_orphaned_research_runs.py"

STATUS_SQL = r'''
WITH case_rollup AS (
  SELECT
    c.id AS case_id,
    c.case_key,
    c.status AS case_status,
    c.opened_at,
    COALESCE(c.orchestration_notes->>'active_dispatch_id', '') AS active_dispatch_id,
    m.id AS market_id,
    m.title,
    m.pipeline_status,
    COUNT(*) FILTER (WHERE rr.status = 'queued') AS queued_runs,
    COUNT(*) FILTER (WHERE rr.status = 'running') AS running_runs,
    COUNT(*) FILTER (WHERE rr.status = 'completed') AS completed_runs,
    COUNT(*) FILTER (WHERE rr.status = 'failed') AS failed_runs,
    COUNT(*) FILTER (WHERE rr.status = 'superseded') AS superseded_runs
  FROM cases c
  JOIN markets m ON m.id = c.market_id
  LEFT JOIN research_runs rr ON rr.case_id = c.id
  GROUP BY c.id, c.case_key, c.status, c.opened_at, COALESCE(c.orchestration_notes->>'active_dispatch_id', ''), m.id, m.title, m.pipeline_status
)
SELECT json_build_object(
  'status_summary', json_build_object(
    'actively_running_case_count', (
      SELECT COUNT(*) FROM case_rollup cr
      WHERE cr.case_status='open' AND cr.pipeline_status='researching' AND cr.running_runs > 0
    ),
    'prepared_waiting_launch_count', (
      SELECT COUNT(*) FROM case_rollup cr
      WHERE cr.case_status='open' AND cr.pipeline_status='researching' AND cr.running_runs = 0 AND cr.queued_runs > 0 AND cr.active_dispatch_id <> ''
    ),
    'stale_researching_case_count', (
      SELECT COUNT(*) FROM case_rollup cr
      WHERE cr.case_status='open' AND cr.pipeline_status='researching' AND cr.running_runs = 0 AND cr.queued_runs > 0 AND cr.active_dispatch_id = ''
    ),
    'terminal_researching_case_count', (
      SELECT COUNT(*) FROM case_rollup cr
      WHERE cr.case_status='open' AND cr.pipeline_status='researching' AND cr.running_runs = 0 AND cr.queued_runs = 0 AND (cr.completed_runs > 0 OR cr.failed_runs > 0)
    )
  ),
  'actively_running_cases', COALESCE((
    SELECT json_agg(row_to_json(x) ORDER BY x.opened_at DESC)
    FROM (
      SELECT *
      FROM case_rollup cr
      WHERE cr.case_status='open' AND cr.pipeline_status='researching' AND cr.running_runs > 0
      ORDER BY cr.opened_at DESC
      LIMIT 20
    ) x
  ), '[]'::json),
  'prepared_dispatches_waiting_launch', COALESCE((
    SELECT json_agg(row_to_json(x) ORDER BY x.opened_at DESC)
    FROM (
      SELECT *
      FROM case_rollup cr
      WHERE cr.case_status='open' AND cr.pipeline_status='researching' AND cr.running_runs = 0 AND cr.queued_runs > 0 AND cr.active_dispatch_id <> ''
      ORDER BY cr.opened_at DESC
      LIMIT 20
    ) x
  ), '[]'::json),
  'stale_researching_cases', COALESCE((
    SELECT json_agg(row_to_json(x) ORDER BY x.opened_at DESC)
    FROM (
      SELECT *
      FROM case_rollup cr
      WHERE cr.case_status='open' AND cr.pipeline_status='researching' AND cr.running_runs = 0 AND cr.queued_runs > 0 AND cr.active_dispatch_id = ''
      ORDER BY cr.opened_at DESC
      LIMIT 20
    ) x
  ), '[]'::json),
  'terminal_researching_cases', COALESCE((
    SELECT json_agg(row_to_json(x) ORDER BY x.opened_at DESC)
    FROM (
      SELECT *
      FROM case_rollup cr
      WHERE cr.case_status='open' AND cr.pipeline_status='researching' AND cr.running_runs = 0 AND cr.queued_runs = 0 AND (cr.completed_runs > 0 OR cr.failed_runs > 0)
      ORDER BY cr.opened_at DESC
      LIMIT 20
    ) x
  ), '[]'::json),
  'active_researching_cases', COALESCE((
    SELECT json_agg(row_to_json(x) ORDER BY x.opened_at DESC)
    FROM (
      SELECT *
      FROM case_rollup cr
      WHERE cr.case_status='open' AND cr.pipeline_status='researching'
      ORDER BY cr.opened_at DESC
      LIMIT 20
    ) x
  ), '[]'::json),
  'queued_open_cases', COALESCE((
    SELECT json_agg(row_to_json(x) ORDER BY x.opened_at DESC)
    FROM (
      SELECT *
      FROM case_rollup cr
      WHERE cr.case_status='open' AND cr.pipeline_status <> 'researching'
      ORDER BY cr.opened_at DESC
      LIMIT 20
    ) x
  ), '[]'::json)
)::text;
'''

INSPECT_CASE_SQL = r'''
WITH target AS (
  SELECT c.id, c.case_key, c.status AS case_status, c.opened_at, c.closed_at,
         c.orchestration_notes,
         m.id AS market_id, m.title, m.platform, m.pipeline_status, m.status AS market_status,
         m.current_price, m.closes_at, m.resolves_at
  FROM cases c
  JOIN markets m ON m.id = c.market_id
  WHERE c.id::text = NULLIF(:'case_ref', '') OR c.case_key = NULLIF(:'case_ref', '')
  LIMIT 1
)
SELECT json_build_object(
  'case', (SELECT row_to_json(t) FROM target t),
  'runs', COALESCE((
    SELECT json_agg(row_to_json(x) ORDER BY x.created_at DESC, x.agent_label)
    FROM (
      SELECT rr.id AS research_run_id, rr.agent_label, rr.status, rr.created_at, rr.started_at, rr.completed_at,
             rr.workspace_note_path,
             rr.notes->>'dispatch_id' AS dispatch_id,
             rr.notes->>'dispatch_stage' AS dispatch_stage,
             rr.notes->>'delivery_target_topic_id' AS delivery_target_topic_id,
             rr.notes->>'delivery_target_session_key' AS delivery_target_session_key
      FROM research_runs rr
      JOIN target t ON t.id = rr.case_id
    ) x
  ), '[]'::json)
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manual control-plane harness for sequential batch execution")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    sub = parser.add_subparsers(dest="command", required=True)

    status = sub.add_parser("status", help="Show active cases, queued cases, and anomaly summary")
    status.add_argument("--pretty", action="store_true", help=argparse.SUPPRESS)

    select_next = sub.add_parser("select-next", help="Show the next eligible market/case candidate under the current gate")
    select_next.add_argument("--pretty", action="store_true", help=argparse.SUPPRESS)

    launch_next = sub.add_parser("launch-next", help="Prepare and launch the next eligible market")
    launch_next.add_argument("--pretty", action="store_true", help=argparse.SUPPRESS)
    launch_next.add_argument("--allow-when-busy", action="store_true")
    launch_next.add_argument("--model", default="openai-codex/gpt-5.4")
    launch_next.add_argument("--thinking", default="medium")

    launch_case = sub.add_parser("launch-case", help="Prepare and launch a specific existing case")
    launch_case.add_argument("--pretty", action="store_true", help=argparse.SUPPRESS)
    launch_case.add_argument("--case-id", required=True)
    launch_case.add_argument("--model", default="openai-codex/gpt-5.4")
    launch_case.add_argument("--thinking", default="medium")

    inspect_case = sub.add_parser("inspect-case", help="Inspect one case and its runs")
    inspect_case.add_argument("--pretty", action="store_true", help=argparse.SUPPRESS)
    inspect_case.add_argument("--case-ref", required=True, help="Case UUID or case_key")

    repair_preview = sub.add_parser("repair-preview", help="Preview stale/orphan repair actions")
    repair_preview.add_argument("--pretty", action="store_true", help=argparse.SUPPRESS)
    repair_preview.add_argument("--queued-stale-minutes", type=int, default=90)

    repair_apply = sub.add_parser("repair-apply", help="Apply safe stale/orphan repair actions")
    repair_apply.add_argument("--pretty", action="store_true", help=argparse.SUPPRESS)
    repair_apply.add_argument("--queued-stale-minutes", type=int, default=90)
    repair_apply.add_argument("--supersede-stale-queued", action="store_true")
    repair_apply.add_argument("--finalize-stranded-cases", action="store_true")
    repair_apply.add_argument("--mark-stranded-needs-intervention", action="store_true")

    return parser.parse_args()


def parse_json_output(stdout: str) -> dict[str, Any]:
    text = stdout.strip()
    if not text:
        return {}
    lines = [line for line in text.splitlines() if line.strip()]
    for idx in range(len(lines)):
        chunk = "\n".join(lines[idx:])
        try:
            parsed = json.loads(chunk)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return parsed
    try:
        parsed = json.loads(text)
        return parsed if isinstance(parsed, dict) else {}
    except json.JSONDecodeError:
        return {}


def run_script(args: list[str], cwd: Path) -> dict[str, Any]:
    proc = subprocess.run([sys.executable, *args], cwd=cwd, text=True, capture_output=True)
    payload = parse_json_output(proc.stdout)
    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "payload": payload,
    }


def run_sql(psql_bin: str, db_url: str, sql_text: str, variables: dict[str, str] | None = None) -> dict[str, Any]:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")
    cmd = [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1"]
    for k, v in (variables or {}).items():
        cmd.extend(["-v", f"{k}={v}"])
    cmd.extend(["-f", "-"])
    proc = subprocess.run(cmd, input=sql_text, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    if not stdout:
        return {}
    return json.loads(stdout.splitlines()[-1])


def render(result: dict[str, Any], pretty: bool) -> None:
    print(json.dumps(result, indent=2 if pretty else None, sort_keys=pretty, default=str))


def main() -> int:
    args = parse_args()
    root = BASE_DIR.parents[4]
    try:
        if args.command == "status":
            db_state = run_sql(args.psql, args.db_url, STATUS_SQL)
            anomaly = run_script([str(ANOMALY_REPORT), "--db-url", args.db_url, "--psql", args.psql, "--pretty"], root)
            next_sel = run_script([str(SELECT_NEXT), "--db-url", args.db_url, "--psql", args.psql, "--pretty"], root)
            result = {
                "status": "ok",
                "db_state": db_state,
                "anomaly_report": anomaly["payload"],
                "next_candidate": next_sel["payload"],
                "next_candidate_error": None if next_sel["returncode"] == 0 else (next_sel["stderr"].strip() or next_sel["stdout"].strip()),
            }
        elif args.command == "select-next":
            selection = run_script([str(SELECT_NEXT), "--db-url", args.db_url, "--psql", args.psql, "--pretty"], root)
            if selection["returncode"] != 0:
                raise ValueError(selection["stderr"].strip() or selection["stdout"].strip() or "select-next failed")
            result = {"status": "ok", "selection": selection["payload"]}
        elif args.command == "launch-next":
            cmd = [str(PREPARE_AND_LAUNCH), "--model", args.model, "--thinking", args.thinking, "--db-url", args.db_url, "--psql", args.psql, "--pretty"]
            if args.allow_when_busy:
                cmd.append("--allow-when-busy")
            launched = run_script(cmd, root)
            result = {"status": "ok" if launched["returncode"] == 0 else "launch_failed", "launch": launched["payload"], "stderr": launched["stderr"]}
        elif args.command == "launch-case":
            cmd = [str(PREPARE_AND_LAUNCH), "--case-id", args.case_id, "--model", args.model, "--thinking", args.thinking, "--db-url", args.db_url, "--psql", args.psql, "--pretty"]
            launched = run_script(cmd, root)
            result = {"status": "ok" if launched["returncode"] == 0 else "launch_failed", "launch": launched["payload"], "stderr": launched["stderr"]}
        elif args.command == "inspect-case":
            inspection = run_sql(args.psql, args.db_url, INSPECT_CASE_SQL, {"case_ref": args.case_ref})
            if not inspection:
                raise ValueError("case not found")
            result = {"status": "ok", "inspection": inspection}
        elif args.command == "repair-preview":
            preview = run_script([
                str(SWEEP_ORPHANS),
                "--queued-stale-minutes", str(args.queued_stale_minutes),
                "--db-url", args.db_url,
                "--psql", args.psql,
                "--pretty",
            ], root)
            result = {"status": "ok" if preview["returncode"] == 0 else "repair_preview_failed", "preview": preview["payload"], "stderr": preview["stderr"]}
        elif args.command == "repair-apply":
            cmd = [
                str(SWEEP_ORPHANS),
                "--queued-stale-minutes", str(args.queued_stale_minutes),
                "--db-url", args.db_url,
                "--psql", args.psql,
                "--pretty",
            ]
            if args.supersede_stale_queued:
                cmd.append("--apply-supersede-stale-queued")
            if args.finalize_stranded_cases:
                cmd.append("--apply-finalize-stranded-cases")
            if args.mark_stranded_needs_intervention:
                cmd.append("--apply-mark-stranded-needs-intervention")
            applied = run_script(cmd, root)
            result = {"status": "ok" if applied["returncode"] == 0 else "repair_apply_failed", "apply": applied["payload"], "stderr": applied["stderr"]}
        else:
            raise ValueError(f"unknown command: {args.command}")
    except Exception as exc:  # noqa: BLE001
        render({"status": "error", "error": str(exc)}, args.pretty)
        return 1

    render(result, args.pretty)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
