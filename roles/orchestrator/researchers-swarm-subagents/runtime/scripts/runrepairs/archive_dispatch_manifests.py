#!/usr/bin/env python3
"""Retire old dispatch manifests out of the active manifest directory.

Default behavior is dry-run only.

Policy:
- active manifests live in runtime/dispatch-manifests/
- manifests older than N days can be moved out of the active queue into a
  Trash-backed staging area
- nothing is hard-deleted automatically
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
RUNREPAIRS_DIR = Path(__file__).resolve().parent
if str(RUNREPAIRS_DIR) not in sys.path:
    sys.path.insert(0, str(RUNREPAIRS_DIR))

from list_pending_dispatch_manifests import classify_manifest, load_manifest, maybe_load_workspace_env, run_psql  # noqa: E402

DEFAULT_MANIFEST_DIR = BASE_DIR / "dispatch-manifests"
DEFAULT_RETIRE_DIR = Path.home() / ".Trash" / "researchers-swarm-subagents-retired-manifests"


@dataclass
class MovePlan:
    source: str
    destination: str
    age_days: float
    dispatch_id: str | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Retire old dispatch manifests from the active queue")
    parser.add_argument("--manifest-dir", default=str(DEFAULT_MANIFEST_DIR), help="Active manifest directory")
    parser.add_argument("--retire-dir", default=str(DEFAULT_RETIRE_DIR), help="Trash-backed staging directory")
    parser.add_argument("--older-than-days", type=int, default=7, help="Retire manifests older than this many days")
    parser.add_argument("--terminal-older-than-hours", type=float, default=12.0, help="Also retire terminal manifests once they are older than this many hours")
    parser.add_argument("--db-url", default='', help="Optional Postgres connection URL used to classify terminal manifests more aggressively")
    parser.add_argument("--psql", default='/opt/homebrew/opt/postgresql@16/bin/psql', help="Path to psql binary used with --db-url or workspace env")
    parser.add_argument("--apply", action="store_true", help="Actually move files (default is dry-run)")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    manifest_dir = Path(args.manifest_dir).expanduser().resolve()
    retire_dir = Path(args.retire_dir).expanduser().resolve()
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.older_than_days)
    aggressive_terminal_cutoff = datetime.now(timezone.utc) - timedelta(hours=float(args.terminal_older_than_hours))
    db_url = args.db_url or os.getenv('PREDQUANT_ORCHESTRATOR_URL', '')

    manifest_dir.mkdir(parents=True, exist_ok=True)
    retire_dir.mkdir(parents=True, exist_ok=True)

    candidates: list[MovePlan] = []
    skipped: list[dict] = []

    now = datetime.now(timezone.utc)
    for path in sorted(manifest_dir.glob("*.json")):
        stat = path.stat()
        modified = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
        age_days = (now - modified).total_seconds() / 86400
        manifest = load_manifest(path)
        dispatch_id = manifest.get("dispatch_id") if isinstance(manifest, dict) else None
        classification = 'unclassified'
        counts: dict | None = None
        terminal_by_runtime = False
        if isinstance(manifest, dict):
            run_ids = [run.get('research_run_id') for run in (manifest.get('runs') or []) if isinstance(run, dict) and run.get('research_run_id')]
            if run_ids:
                try:
                    run_rows = run_psql(args.psql, db_url, {'research_run_ids': run_ids})
                except Exception:
                    run_rows = []
                if run_rows:
                    classification, counts = classify_manifest(run_rows)
                    terminal_by_runtime = classification == 'terminal'

        should_retire = False
        reason = ''
        if terminal_by_runtime and modified < aggressive_terminal_cutoff:
            should_retire = True
            reason = 'terminal_manifest_past_terminal_cutoff'
        elif modified < cutoff:
            should_retire = True
            reason = 'older_than_cutoff'

        if not should_retire:
            skipped.append({
                "path": str(path),
                "reason": reason or "newer_than_cutoff",
                "age_days": round(age_days, 2),
                "classification": classification,
                "counts": counts,
            })
            continue

        retire_bucket = modified.strftime("%Y-%m")
        destination = retire_dir / retire_bucket / path.name
        candidates.append(
            MovePlan(
                source=str(path),
                destination=str(destination),
                age_days=round(age_days, 2),
                dispatch_id=dispatch_id,
            )
        )

    moved: list[dict] = []
    if args.apply:
        for plan in candidates:
            dst = Path(plan.destination)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(plan.source, plan.destination)
            moved.append(asdict(plan))

    result = {
        "status": "applied" if args.apply else "dry_run",
        "manifest_dir": str(manifest_dir),
        "retire_dir": str(retire_dir),
        "older_than_days": args.older_than_days,
        "terminal_older_than_hours": float(args.terminal_older_than_hours),
        "candidate_count": len(candidates),
        "candidates": [asdict(plan) for plan in candidates],
        "moved": moved,
        "skipped": skipped,
        "policy": {
            "active_retention_days": args.older_than_days,
            "terminal_retention_hours": float(args.terminal_older_than_hours),
            "retire_location": str(retire_dir),
            "hard_delete": False,
        },
    }

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(json.dumps(result, separators=(",", ":"), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
