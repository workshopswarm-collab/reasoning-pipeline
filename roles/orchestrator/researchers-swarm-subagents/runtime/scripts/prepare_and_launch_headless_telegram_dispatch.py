#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
PREPARE = BASE_DIR / "prepare_headless_telegram_dispatch.py"
LAUNCH = BASE_DIR / "launch_dispatch_with_stateful_posts.py"
DEFAULT_MANIFEST_DIR = BASE_DIR.parent / "dispatch-manifests"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare and immediately launch a headless Telegram dispatch")
    parser.add_argument("--case-id", help="Existing case UUID to dispatch; if omitted, auto-select next eligible market")
    parser.add_argument("--allow-when-busy", action="store_true", help="Bypass the global sequential-processing gate when auto-selecting the next market")
    parser.add_argument("--model", default="openai-codex/gpt-5.4")
    parser.add_argument("--thinking", default="medium")
    parser.add_argument("--run-timeout-seconds", type=int, default=0)
    parser.add_argument("--manifest-dir", default=str(DEFAULT_MANIFEST_DIR))
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""))
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", "/opt/homebrew/opt/postgresql@16/bin/psql"))
    parser.add_argument("--pretty", action="store_true")
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


def manifest_candidates(manifest_dir: Path) -> dict[str, float]:
    if not manifest_dir.exists():
        return {}
    return {str(p.resolve()): p.stat().st_mtime for p in manifest_dir.glob("dispatch-case-*.json") if p.is_file()}


def resolve_manifest_path(*, prepare_result: dict[str, Any], manifest_dir: Path, before: dict[str, float], after: dict[str, float]) -> str:
    dispatch = prepare_result.get("dispatch") or {}

    for explicit in [
        prepare_result.get("manifest_path"),
        dispatch.get("manifest_path"),
    ]:
        if explicit:
            return str((Path(explicit) if Path(explicit).is_absolute() else (Path.cwd() / explicit)).resolve())

    for dispatch_id in [
        prepare_result.get("dispatch_id"),
        dispatch.get("dispatch_id"),
    ]:
        if not dispatch_id:
            continue
        direct = (manifest_dir / f"{dispatch_id}.json").resolve()
        if direct.exists():
            return str(direct)

    new_paths = [path for path in after if path not in before]
    if len(new_paths) == 1:
        return new_paths[0]
    if new_paths:
        return max(new_paths, key=lambda p: after[p])

    changed_paths = [path for path in after if before.get(path) != after.get(path)]
    if changed_paths:
        return max(changed_paths, key=lambda p: after[p])

    manifest_dir.mkdir(parents=True, exist_ok=True)
    candidates = sorted(manifest_dir.glob("dispatch-case-*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if candidates:
        return str(candidates[0].resolve())

    raise ValueError("unable to determine manifest path from prepare step")


def main() -> int:
    args = parse_args()
    manifest_dir = Path(args.manifest_dir).resolve()
    before = manifest_candidates(manifest_dir)

    prepare_cmd = [
        sys.executable,
        str(PREPARE),
        "--model", args.model,
        "--thinking", args.thinking,
        "--run-timeout-seconds", str(args.run_timeout_seconds),
        "--manifest-dir", str(manifest_dir),
        "--db-url", args.db_url,
        "--psql", args.psql,
        "--pretty",
    ]
    if args.case_id:
        prepare_cmd.extend(["--case-id", args.case_id])
    if args.allow_when_busy:
        prepare_cmd.append("--allow-when-busy")

    prepare_proc = subprocess.run(prepare_cmd, text=True, capture_output=True)
    prepare_result = parse_json_output(prepare_proc.stdout)
    if prepare_proc.returncode != 0:
        error_payload = {
            "status": "prepare_failed",
            "prepare_returncode": prepare_proc.returncode,
            "prepare_stdout": prepare_proc.stdout,
            "prepare_stderr": prepare_proc.stderr,
        }
        print(json.dumps(error_payload, indent=2 if args.pretty else None))
        return prepare_proc.returncode

    time.sleep(0.2)
    after = manifest_candidates(manifest_dir)
    try:
        manifest_path = resolve_manifest_path(prepare_result=prepare_result, manifest_dir=manifest_dir, before=before, after=after)
    except Exception as exc:  # noqa: BLE001
        error_payload = {
            "status": "manifest_resolution_failed",
            "error": str(exc),
            "prepare_result": prepare_result,
            "prepare_stdout": prepare_proc.stdout,
            "prepare_stderr": prepare_proc.stderr,
        }
        print(json.dumps(error_payload, indent=2 if args.pretty else None))
        return 1

    launch_cmd = [
        sys.executable,
        str(LAUNCH),
        "--manifest-path", manifest_path,
        "--pretty",
    ]
    launch_proc = subprocess.run(launch_cmd, text=True, capture_output=True)
    launch_result = parse_json_output(launch_proc.stdout)

    payload = {
        "status": "ok" if launch_proc.returncode == 0 else "launch_failed",
        "manifest_path": manifest_path,
        "prepare_result": prepare_result,
        "launch_result": launch_result,
        "prepare_stdout": prepare_proc.stdout,
        "prepare_stderr": prepare_proc.stderr,
        "launch_stdout": launch_proc.stdout,
        "launch_stderr": launch_proc.stderr,
    }
    print(json.dumps(payload, indent=2 if args.pretty else None))
    return launch_proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
