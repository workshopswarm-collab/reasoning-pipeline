#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    case_light_refresh_brief_json_path,
    coerce_string,
    load_json,
    relative_to_workspace,
    write_json,
)

BUILD_LIGHT_REFRESH_BRIEF = SCRIPT_DIR / "build_light_refresh_brief.py"
BUILD_CONTEXT = SCRIPT_DIR / "build_decision_context.py"
RUN_DECISION_MAKER = SCRIPT_DIR / "run_decision_maker.py"


class LightRefreshError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a lightweight refresh update before Decision-Maker repricing")
    parser.add_argument("--case-key", required=True)
    parser.add_argument("--contract-id", default="yes")
    parser.add_argument("--timeout-seconds", type=float, default=600.0)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def run_command(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, cwd=str(WORKSPACE_ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        raise LightRefreshError(f"command failed ({proc.returncode}): {' '.join(cmd)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")
    return proc


def parse_json_stdout(proc: subprocess.CompletedProcess[str]) -> dict[str, Any]:
    stdout = proc.stdout.strip()
    if not stdout:
        return {}
    return json.loads(stdout)


def refresh_dispatch_id(case_key: str) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"refresh-{case_key}-{stamp}"


def build_refresh_context(case_key: str, *, contract_id: str, pretty: bool) -> tuple[Path, dict[str, Any], dict[str, Any]]:
    brief_proc = run_command([
        sys.executable,
        str(BUILD_LIGHT_REFRESH_BRIEF),
        "--case-key",
        case_key,
        "--contract-id",
        contract_id,
        *( ["--pretty"] if pretty else [] ),
    ])
    brief_result = parse_json_stdout(brief_proc)
    brief_path = case_light_refresh_brief_json_path(case_key)
    brief_payload = load_json(brief_path)

    build_ctx_proc = run_command([
        sys.executable,
        str(BUILD_CONTEXT),
        "--case-key",
        case_key,
        "--market-price",
        str(brief_result.get("current_price")),
        "--market-id",
        str(brief_result.get("market_id")),
        "--market-title",
        str(brief_result.get("market_title")),
        *( ["--quote-timestamp", str(brief_result.get("quote_timestamp"))] if coerce_string(brief_result.get("quote_timestamp")) else [] ),
        *( ["--pretty"] if pretty else [] ),
    ])
    context_result = parse_json_stdout(build_ctx_proc)
    base_context_path = Path(context_result["decision_context_path"])
    if not base_context_path.is_absolute():
        base_context_path = WORKSPACE_ROOT / base_context_path
    context_payload = load_json(base_context_path)

    original_dispatch_id = coerce_string(context_payload.get("dispatch_id"))
    synthetic_dispatch_id = refresh_dispatch_id(case_key)
    context_payload["dispatch_id"] = synthetic_dispatch_id
    upstream = context_payload.get("upstream") if isinstance(context_payload.get("upstream"), dict) else {}
    upstream["light_refresh_brief_path"] = relative_to_workspace(brief_path)
    upstream["light_refresh_mode"] = coerce_string(((brief_payload.get("refresh_assessment") or {}) if isinstance(brief_payload.get("refresh_assessment"), dict) else {}).get("recommended_mode"))
    upstream["source_dispatch_id"] = original_dispatch_id
    context_payload["upstream"] = upstream
    context_payload["light_refresh"] = brief_payload

    patched_context_path = base_context_path.with_name(f"decision-context-light-refresh-{synthetic_dispatch_id}.json")
    write_json(patched_context_path, context_payload, pretty=True)
    return patched_context_path, brief_result, brief_payload


def main() -> int:
    args = parse_args()
    context_path, brief_result, brief_payload = build_refresh_context(args.case_key, contract_id=args.contract_id, pretty=args.pretty)
    if args.prepare_only:
        print(json.dumps({
            "ok": True,
            "prepared_only": True,
            "case_key": args.case_key,
            "contract_id": args.contract_id,
            "refresh_mode": ((brief_payload.get("refresh_assessment") or {}) if isinstance(brief_payload.get("refresh_assessment"), dict) else {}).get("recommended_mode", "light"),
            "light_refresh_brief": brief_result,
            "decision_context_json": relative_to_workspace(context_path),
        }, indent=2 if args.pretty else None))
        return 0

    decision_proc = run_command([
        sys.executable,
        str(RUN_DECISION_MAKER),
        "--decision-context-json",
        str(context_path),
        "--timeout-seconds",
        str(args.timeout_seconds),
        *( ["--pretty"] if args.pretty else [] ),
    ])
    decision_result = parse_json_stdout(decision_proc)
    print(json.dumps({
        "ok": True,
        "case_key": args.case_key,
        "contract_id": args.contract_id,
        "refresh_mode": ((brief_payload.get("refresh_assessment") or {}) if isinstance(brief_payload.get("refresh_assessment"), dict) else {}).get("recommended_mode", "light"),
        "light_refresh_brief": brief_result,
        "decision_context_json": relative_to_workspace(context_path),
        "decision_result": decision_result,
    }, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
