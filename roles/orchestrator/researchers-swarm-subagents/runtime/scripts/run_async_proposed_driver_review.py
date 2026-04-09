#!/usr/bin/env python3
from __future__ import annotations

"""Run proposed-driver aggregation/review as a detached best-effort worker.

Design goals:
- never gate research-run terminal completion, swarm finalization, or synthesis kickoff
- serialize shared review-queue writes behind a lock
- keep review outputs eventually consistent via a per-run async job
- remain safe to trigger repeatedly; review scripts already support auto/unchanged skips
"""

import argparse
import fcntl
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
BASE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = BASE_DIR.parent
PIPELINE_DIR = RUNTIME_DIR.parent
WORKSPACE_ROOT = PIPELINE_DIR.parents[2]
DEFAULT_ENV_PATH = WORKSPACE_ROOT / ".env"
UPDATE_RUN = BASE_DIR / "update_research_run.py"
AGGREGATE_PROPOSED_DRIVER_CANDIDATES_SCRIPT = BASE_DIR / "aggregate_proposed_driver_candidates.py"
REVIEW_PROPOSED_DRIVER_FAMILIES_WITH_OLLAMA_SCRIPT = BASE_DIR / "review_proposed_driver_families_with_ollama.py"
REVIEW_PROVISIONAL_DRIVER_SYNTHESIS_WITH_OLLAMA_SCRIPT = BASE_DIR / "review_provisional_driver_synthesis_with_ollama.py"
STATE_DIR = BASE_DIR / ".runtime-state" / "proposed-driver-review"
LOCK_PATH = STATE_DIR / "global.lock"


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
    parser = argparse.ArgumentParser(description="Run proposed-driver aggregation/review asynchronously")
    parser.add_argument("--research-run-id", required=True, help="Research run id associated with this async review job")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def python_json(script: Path, args: list[str], *, timeout_seconds: float | None = None) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            [sys.executable, str(script), *args],
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"{script.name} timed out after {timeout_seconds}s") from exc
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


def update_research_run_notes(research_run_id: str, db_url: str, notes: dict[str, Any]) -> dict[str, Any]:
    args = [
        "--research-run-id", research_run_id,
        "--db-url", db_url,
        "--notes-json", json.dumps(notes, separators=(",", ":")),
    ]
    return python_json(UPDATE_RUN, args)


def review_timeout_seconds(env_key: str, default_seconds: int = 180, extra_grace_seconds: int = 30) -> int:
    raw = os.getenv(env_key, "").strip()
    try:
        base = int(raw) if raw else default_seconds
    except ValueError:
        base = default_seconds
    return max(1, base + extra_grace_seconds)


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    if not args.db_url:
        print("ERROR: --db-url or PREDQUANT_ORCHESTRATOR_URL is required", file=sys.stderr)
        return 1

    STATE_DIR.mkdir(parents=True, exist_ok=True)
    result_path = STATE_DIR / f"{args.research_run_id}.result.json"

    result: dict[str, Any] = {
        "status": "running",
        "research_run_id": args.research_run_id,
        "started_at": now_iso(),
        "aggregation_result": None,
        "family_review_result": None,
        "provisional_synthesis_result": None,
        "aggregation_changed": None,
        "errors": {},
    }

    try:
        update_research_run_notes(
            args.research_run_id,
            args.db_url,
            {
                "proposed_driver_review_job": {
                    "status": "running",
                    "started_at": result["started_at"],
                    "result_path": str(result_path.relative_to(WORKSPACE_ROOT)),
                }
            },
        )
    except Exception:
        pass

    try:
        with LOCK_PATH.open("a+") as lock_handle:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)

            aggregation_result = python_json(
                AGGREGATE_PROPOSED_DRIVER_CANDIDATES_SCRIPT,
                ["--db-url", args.db_url, "--psql", args.psql],
            )
            result["aggregation_result"] = aggregation_result

            write_outcomes = aggregation_result.get("write_outcomes") or {}
            aggregation_changed = bool(
                write_outcomes.get("candidate_written")
                or write_outcomes.get("index_written")
                or write_outcomes.get("candidate_removed")
                or write_outcomes.get("legacy_candidate_removed")
            )
            result["aggregation_changed"] = aggregation_changed

            should_run_family_review = os.getenv("ENABLE_DRIVER_FAMILY_REVIEW", "").strip().lower() in {"1", "true", "yes", "on"}
            should_run_provisional_synthesis = os.getenv("ENABLE_PROVISIONAL_DRIVER_SYNTHESIS_REVIEW", "").strip().lower() in {"1", "true", "yes", "on"}

            if should_run_family_review and aggregation_changed and REVIEW_PROPOSED_DRIVER_FAMILIES_WITH_OLLAMA_SCRIPT.exists():
                try:
                    result["family_review_result"] = python_json(
                        REVIEW_PROPOSED_DRIVER_FAMILIES_WITH_OLLAMA_SCRIPT,
                        [
                            "--run-ollama",
                            "--auto",
                            "--model", os.getenv("DRIVER_FAMILY_REVIEW_MODEL", "qwen3.5:9b"),
                            "--timeout-seconds", os.getenv("DRIVER_FAMILY_REVIEW_TIMEOUT_SECONDS", "180"),
                        ],
                        timeout_seconds=review_timeout_seconds("DRIVER_FAMILY_REVIEW_TIMEOUT_SECONDS"),
                    )
                except Exception as exc:  # noqa: BLE001
                    result["errors"]["family_review"] = str(exc)
            elif should_run_family_review:
                result["family_review_result"] = {
                    "status": "skipped",
                    "reason": "no_candidate_family_changes",
                }

            if should_run_provisional_synthesis and aggregation_changed and REVIEW_PROVISIONAL_DRIVER_SYNTHESIS_WITH_OLLAMA_SCRIPT.exists():
                try:
                    result["provisional_synthesis_result"] = python_json(
                        REVIEW_PROVISIONAL_DRIVER_SYNTHESIS_WITH_OLLAMA_SCRIPT,
                        [
                            "--run-ollama",
                            "--auto",
                            "--model", os.getenv("PROVISIONAL_DRIVER_SYNTHESIS_MODEL", "qwen3.5:9b"),
                            "--timeout-seconds", os.getenv("PROVISIONAL_DRIVER_SYNTHESIS_TIMEOUT_SECONDS", "180"),
                        ],
                        timeout_seconds=review_timeout_seconds("PROVISIONAL_DRIVER_SYNTHESIS_TIMEOUT_SECONDS"),
                    )
                except Exception as exc:  # noqa: BLE001
                    result["errors"]["provisional_synthesis"] = str(exc)
            elif should_run_provisional_synthesis:
                result["provisional_synthesis_result"] = {
                    "status": "skipped",
                    "reason": "no_candidate_family_changes",
                }

            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)

        result["status"] = "completed_with_errors" if result["errors"] else "completed"
    except Exception as exc:  # noqa: BLE001
        result["status"] = "failed"
        result["errors"]["worker"] = str(exc)

    result["finished_at"] = now_iso()
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True, default=str) + "\n")

    try:
        update_research_run_notes(
            args.research_run_id,
            args.db_url,
            {
                "proposed_driver_review_job": {
                    "status": result["status"],
                    "started_at": result["started_at"],
                    "finished_at": result["finished_at"],
                    "aggregation_changed": result.get("aggregation_changed"),
                    "result_path": str(result_path.relative_to(WORKSPACE_ROOT)),
                    "errors": result.get("errors") or {},
                }
            },
        )
    except Exception:
        pass

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(result, separators=(",", ":"), default=str))
    return 0 if result["status"] in {"completed", "completed_with_errors"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
