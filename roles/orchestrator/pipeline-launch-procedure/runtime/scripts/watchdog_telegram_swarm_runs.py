#!/usr/bin/env python3
from __future__ import annotations

"""Identify stalled Telegram swarm runs and emit intervention actions.

This helper does not call OpenClaw session tools directly. Instead it produces:
- stale-run diagnostics
- suggested `sessions_send` nudges
- optional failure patch payloads for runs that have exceeded a harder timeout

Use it from the runtime/agent layer when you want a lightweight watchdog pass.
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
BASE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = BASE_DIR.parent
PIPELINE_DIR = RUNTIME_DIR.parent
WORKSPACE_ROOT = PIPELINE_DIR.parents[2]
DEFAULT_ENV_PATH = WORKSPACE_ROOT / ".env"

SQL = r'''
SELECT COALESCE(json_agg(json_build_object(
  'research_run_id', rr.id::text,
  'run_label', rr.run_label,
  'agent_label', rr.agent_label,
  'status', rr.status,
  'started_at', rr.started_at,
  'workspace_note_path', rr.workspace_note_path,
  'case_key', c.case_key,
  'notes', rr.notes
) ORDER BY rr.started_at), '[]'::json)::text
FROM research_runs rr
JOIN cases c ON c.id = rr.case_id
WHERE rr.status = 'running'
  AND COALESCE(rr.notes->>'runtime_surface', '') = 'telegram-forum-topic';
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
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect stalled Telegram swarm runs and emit intervention actions")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--nudge-after-minutes", type=float, default=8.0)
    parser.add_argument("--fail-after-minutes", type=float, default=18.0)
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def run_psql(psql_bin: str, db_url: str) -> list[dict]:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")
    proc = subprocess.run([psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1", "-f", "-"], input=SQL, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    out = proc.stdout.strip()
    if not out:
        return []
    return json.loads(out.splitlines()[-1])


def parse_dt(value: str | None):
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def latest_artifact_activity(case_key: str, agent_label: str) -> datetime | None:
    base = WORKSPACE_ROOT / "qualitative-db" / "40-research"
    token = f"{case_key}-{agent_label}"
    latest = None
    for match in base.glob(f"**/*{token}*"):
        if not match.is_file():
            continue
        dt = datetime.fromtimestamp(match.stat().st_mtime, tz=timezone.utc)
        if latest is None or dt > latest:
            latest = dt
    return latest


def iso(dt: datetime | None) -> str | None:
    return dt.isoformat() if dt else None


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    try:
        runs = run_psql(args.psql, args.db_url)
        now = datetime.now(timezone.utc)
        findings = []
        for run in runs:
            notes = run.get("notes") or {}
            started_at = parse_dt(run.get("started_at"))
            artifact_at = latest_artifact_activity(run.get("case_key"), run.get("agent_label"))
            last_activity = artifact_at or started_at or now
            idle_minutes = max(0.0, (now - last_activity).total_seconds() / 60.0)
            state = "healthy"
            if idle_minutes >= args.fail_after_minutes:
                state = "fail_candidate"
            elif idle_minutes >= args.nudge_after_minutes:
                state = "nudge_candidate"

            nudge_payload = None
            if state == "nudge_candidate" and notes.get("delivery_target_session_key"):
                nudge_payload = {
                    "sessionKey": notes.get("delivery_target_session_key"),
                    "message": (
                        "You appear stalled. Either finish now using the evidence already gathered or post a concise blocker/progress update immediately. "
                        "Do not continue broadening research unless the next source is likely to change the estimate materially."
                    ),
                    "timeoutSeconds": 20,
                }

            fail_patch = None
            if state == "fail_candidate":
                fail_patch = {
                    "research_run_id": run.get("research_run_id"),
                    "status": "failed",
                    "mark_completed": True,
                    "workspace_note_path": run.get("workspace_note_path"),
                    "notes": {
                        "watchdog_failed_at": now.isoformat(),
                        "watchdog_reason": "stalled_without_progress",
                    },
                }

            findings.append(
                {
                    "research_run_id": run.get("research_run_id"),
                    "persona": run.get("agent_label"),
                    "case_key": run.get("case_key"),
                    "status": run.get("status"),
                    "state": state,
                    "started_at": iso(started_at),
                    "last_artifact_activity_at": iso(artifact_at),
                    "last_activity_at": iso(last_activity),
                    "idle_minutes": round(idle_minutes, 2),
                    "nudge_payload": nudge_payload,
                    "fail_patch": fail_patch,
                }
            )

        result = {
            "status": "ok",
            "nudge_after_minutes": args.nudge_after_minutes,
            "fail_after_minutes": args.fail_after_minutes,
            "running_count": len(findings),
            "findings": findings,
        }
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(json.dumps(result, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
