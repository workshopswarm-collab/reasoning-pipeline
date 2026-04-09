#!/usr/bin/env python3
from __future__ import annotations

"""Runtime loop for active Telegram swarm runs.

Responsibilities:
- periodically run the Telegram watchdog
- auto-complete stale `running` rows when the primary artifact exists and has gone idle
- send internal nudges to stalled lanes through the Node `sessions.send` helper
- optionally mark hard-stalled lanes failed

This is intended to be the always-on runtime-side loop for active Telegram swarm
research, replacing manual babysitting with a small deterministic control loop.
"""

import argparse
import json
import os
import signal
import subprocess
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = BASE_DIR.parents[3]
DEFAULT_ENV_PATH = WORKSPACE_ROOT / ".env"
WATCHDOG = BASE_DIR / "internal" / "watchdog_telegram_swarm_runs.py"
SESSIONS_SEND_HELPER = BASE_DIR / "internal" / "openclaw_sessions_send.mjs"
UPDATE_RUN = BASE_DIR / "update_research_run.py"
STATE_DIR = BASE_DIR / ".runtime-state"
DEFAULT_PID_FILE = STATE_DIR / "telegram_swarm_runtime_loop.pid"
DEFAULT_ERROR_FILE = STATE_DIR / "telegram_swarm_runtime_loop.error.json"
DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"


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
    parser = argparse.ArgumentParser(description="Run the Telegram swarm runtime loop")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--interval-seconds", type=float, default=90.0, help="Sleep between watchdog passes")
    parser.add_argument("--complete-after-minutes", type=float, default=1.5)
    parser.add_argument("--nudge-after-minutes", type=float, default=8.0)
    parser.add_argument("--nudge-cooldown-minutes", type=float, default=10.0)
    parser.add_argument("--fail-after-minutes", type=float, default=18.0)
    parser.add_argument("--apply-failures", action="store_true", help="Actually mark fail candidates failed")
    parser.add_argument("--once", action="store_true", help="Run a single pass and exit")
    parser.add_argument("--stay-alive-when-idle", action="store_true", help="Keep polling even when there are no running swarm lanes")
    parser.add_argument("--pid-file", default=str(DEFAULT_PID_FILE), help="PID file path for singleton runtime-loop supervision")
    parser.add_argument("--error-file", default=str(DEFAULT_ERROR_FILE), help="Write runtime-loop errors here instead of emitting routine logs")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print final output")
    return parser.parse_args()


def parse_json(raw: str) -> dict[str, Any]:
    stdout = (raw or "").strip()
    if not stdout:
        return {}
    try:
        parsed = json.loads(stdout)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass
    for line in reversed([line for line in stdout.splitlines() if line.strip()]):
        try:
            parsed = json.loads(line)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            continue
    raise RuntimeError("unable to parse JSON object from command output")


def python_json(script: Path, args: list[str]) -> dict[str, Any]:
    proc = subprocess.run([sys.executable, str(script), *args], text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"{script.name} failed")
    return parse_json(proc.stdout)


def sessions_send(payload: dict[str, Any]) -> dict[str, Any]:
    proc = subprocess.run(
        ["node", str(SESSIONS_SEND_HELPER), "--payload-json", json.dumps(payload, separators=(",", ":"))],
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "sessions.send helper failed")
    return parse_json(proc.stdout)


def patch_notes(args: argparse.Namespace, research_run_id: str, notes: dict[str, Any]) -> dict[str, Any]:
    cmd = [
        sys.executable,
        str(UPDATE_RUN),
        "--research-run-id", research_run_id,
        "--notes-json", json.dumps(notes, separators=(",", ":")),
        "--db-url", args.db_url,
        "--psql", args.psql,
    ]
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "update_research_run.py failed")
    return parse_json(proc.stdout)


def apply_fail_patch(args: argparse.Namespace, fail_patch: dict[str, Any]) -> dict[str, Any]:
    cmd = [
        sys.executable,
        str(UPDATE_RUN),
        "--research-run-id", fail_patch["research_run_id"],
        "--status", fail_patch["status"],
        "--workspace-note-path", fail_patch.get("workspace_note_path") or "",
        "--notes-json", json.dumps(fail_patch.get("notes", {}), separators=(",", ":")),
        "--db-url", args.db_url,
        "--psql", args.psql,
    ]
    if fail_patch.get("mark_completed"):
        cmd.append("--mark-completed")
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "failed to apply fail patch")
    return parse_json(proc.stdout)


def write_pid_file(pid_file: Path) -> None:
    pid_file.parent.mkdir(parents=True, exist_ok=True)
    pid_file.write_text(f"{os.getpid()}\n")


def cleanup_pid_file(pid_file: Path) -> None:
    try:
        if pid_file.exists() and pid_file.read_text().strip() == str(os.getpid()):
            pid_file.unlink()
    except FileNotFoundError:
        pass


def clear_error_file(error_file: Path) -> None:
    try:
        error_file.unlink()
    except FileNotFoundError:
        pass


def write_error_file(error_file: Path, payload: dict[str, Any]) -> None:
    error_file.parent.mkdir(parents=True, exist_ok=True)
    error_file.write_text(json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n")


def watchdog_pass(args: argparse.Namespace) -> dict[str, Any]:
    wd = python_json(
        WATCHDOG,
        [
            "--db-url", args.db_url,
            "--psql", args.psql,
            "--complete-after-minutes", str(args.complete_after_minutes),
            "--nudge-after-minutes", str(args.nudge_after_minutes),
            "--nudge-cooldown-minutes", str(args.nudge_cooldown_minutes),
            "--fail-after-minutes", str(args.fail_after_minutes),
            "--apply-completions",
        ],
    )

    nudge_results = []
    failure_results = []
    errors = []
    now_iso = datetime.now(timezone.utc).isoformat()

    for finding in wd.get("findings", []):
        run_id = finding.get("research_run_id")
        state = finding.get("state")
        try:
            if state == "nudge_candidate" and finding.get("nudge_payload"):
                send_result = sessions_send(finding["nudge_payload"])
                patch_result = patch_notes(
                    args,
                    run_id,
                    {
                        "watchdog_last_nudged_at": now_iso,
                        "watchdog_last_nudge_reason": "idle_progress_check",
                    },
                )
                nudge_results.append(
                    {
                        "research_run_id": run_id,
                        "persona": finding.get("persona"),
                        "send_result": send_result,
                        "patch_result": patch_result,
                    }
                )
            elif state == "fail_candidate" and args.apply_failures and finding.get("fail_patch"):
                fail_result = apply_fail_patch(args, finding["fail_patch"])
                failure_results.append(
                    {
                        "research_run_id": run_id,
                        "persona": finding.get("persona"),
                        "result": fail_result,
                    }
                )
        except Exception as exc:  # noqa: BLE001
            errors.append(
                {
                    "research_run_id": run_id,
                    "persona": finding.get("persona"),
                    "state": state,
                    "error": str(exc),
                }
            )

    return {
        "status": "ok",
        "watchdog": wd,
        "nudge_results": nudge_results,
        "failure_results": failure_results,
        "errors": errors,
    }


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    if not args.db_url:
        print("ERROR: --db-url or PREDQUANT_ORCHESTRATOR_URL is required", file=sys.stderr)
        return 1

    pid_file = Path(args.pid_file).expanduser().resolve()
    error_file = Path(args.error_file).expanduser().resolve()
    write_pid_file(pid_file)
    clear_error_file(error_file)

    passes = []
    exit_reason = "requested"
    try:
        while True:
            result = watchdog_pass(args)
            result["ran_at"] = datetime.now(timezone.utc).isoformat()
            passes.append(result)
            if result.get("errors"):
                write_error_file(
                    error_file,
                    {
                        "kind": "runtime_loop_pass_errors",
                        "at": result["ran_at"],
                        "errors": result.get("errors"),
                        "nudge_results": result.get("nudge_results"),
                        "failure_results": result.get("failure_results"),
                    },
                )
            else:
                clear_error_file(error_file)
            running_count = ((result.get("watchdog") or {}).get("running_count") or 0)
            if args.once:
                exit_reason = "once"
                break
            if running_count == 0 and not args.stay_alive_when_idle:
                exit_reason = "idle"
                break
            time.sleep(max(1.0, args.interval_seconds))
    except KeyboardInterrupt:
        exit_reason = "keyboard_interrupt"
    except Exception as exc:  # noqa: BLE001
        write_error_file(
            error_file,
            {
                "kind": "runtime_loop_exception",
                "at": datetime.now(timezone.utc).isoformat(),
                "error": str(exc),
                "traceback": traceback.format_exc(),
            },
        )
        cleanup_pid_file(pid_file)
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    finally:
        cleanup_pid_file(pid_file)

    output = {
        "status": "ok",
        "mode": "once" if args.once else "loop",
        "exit_reason": exit_reason,
        "pass_count": len(passes),
        "last_pass": passes[-1] if passes else None,
    }
    if args.pretty:
        print(json.dumps(output, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(output, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
