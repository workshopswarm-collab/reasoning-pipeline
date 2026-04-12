#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
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
    append_case_timeline_entry,
    case_decision_packet_json_path,
    case_decision_packet_markdown_path,
    case_decision_stage_status_path,
    case_light_refresh_brief_json_path,
    case_light_refresh_brief_markdown_path,
    case_refresh_manifest_path,
    coerce_string,
    decision_case_refresh_dir,
    load_json,
    relative_to_workspace,
    utc_now_iso,
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


def resolve_workspace_path(path_like: str | Path | None) -> Path | None:
    text = coerce_string(path_like)
    if not text:
        return None
    path = Path(text)
    return path if path.is_absolute() else WORKSPACE_ROOT / path


def refresh_bundle_paths(case_key: str, refresh_id: str) -> dict[str, Path]:
    root = decision_case_refresh_dir(case_key, refresh_id)
    return {
        "root": root,
        "brief_json": root / "light-refresh-brief.json",
        "brief_markdown": root / "light-refresh-brief.md",
        "decision_context_json": root / "decision-context-light-refresh.json",
        "inputs_dir": root / "inputs",
        "outputs_dir": root / "outputs",
        "manifest": case_refresh_manifest_path(case_key, refresh_id),
    }


def copy_if_exists(source: Path | None, destination: Path) -> str:
    if source is None or not source.exists():
        return ""
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return relative_to_workspace(destination)


def append_refresh_timeline_entry(*, case_key: str, refresh_id: str, manifest_path: Path, packet_path: str = "") -> dict[str, Any]:
    manifest_rel = relative_to_workspace(manifest_path)
    entry = f"- logged light refresh `{refresh_id}` with manifest `{manifest_rel}`"
    if packet_path:
        entry += f" and packet `{packet_path}`"
    entry += "."
    token = f"light refresh `{refresh_id}` with manifest `{manifest_rel}`"
    appended = append_case_timeline_entry(case_key, entry, unique_token=token)
    return {
        "appended": appended,
        "entry": entry,
        "manifest_path": manifest_rel,
        "packet_path": packet_path,
    }


def write_refresh_manifest(*, case_key: str, refresh_id: str, contract_id: str, refresh_mode: str, brief_payload: dict[str, Any], paths: dict[str, Path], original_dispatch_id: str, copied_artifacts: dict[str, str], decision_result: dict[str, Any] | None, prepared_only: bool) -> dict[str, Any]:
    manifest = {
        "artifact_type": "decision_refresh_bundle",
        "schema_version": "decision-refresh/v1",
        "built_at": utc_now_iso(),
        "case_key": case_key,
        "refresh_id": refresh_id,
        "contract_id": contract_id,
        "prepared_only": prepared_only,
        "refresh_mode": refresh_mode,
        "refresh_reasons": ((brief_payload.get("refresh_assessment") or {}) if isinstance(brief_payload.get("refresh_assessment"), dict) else {}).get("reasons", []),
        "source_dispatch_id": original_dispatch_id,
        "canonical_paths": {
            "light_refresh_brief_json": relative_to_workspace(case_light_refresh_brief_json_path(case_key)),
            "light_refresh_brief_markdown": relative_to_workspace(case_light_refresh_brief_markdown_path(case_key)),
            "decision_packet_json": relative_to_workspace(case_decision_packet_json_path(case_key)),
            "decision_packet_markdown": relative_to_workspace(case_decision_packet_markdown_path(case_key)),
            "decision_stage_status_json": relative_to_workspace(case_decision_stage_status_path(case_key)),
        },
        "refresh_bundle": {
            "root": relative_to_workspace(paths["root"]),
            "light_refresh_brief_json": relative_to_workspace(paths["brief_json"]),
            "light_refresh_brief_markdown": relative_to_workspace(paths["brief_markdown"]),
            "decision_context_json": relative_to_workspace(paths["decision_context_json"]),
            "inputs_dir": relative_to_workspace(paths["inputs_dir"]),
            "outputs_dir": relative_to_workspace(paths["outputs_dir"]),
            "copied_artifacts": copied_artifacts,
        },
        "brief_summary": {
            "market_id": ((brief_payload.get("market") or {}) if isinstance(brief_payload.get("market"), dict) else {}).get("market_id", ""),
            "market_title": ((brief_payload.get("market") or {}) if isinstance(brief_payload.get("market"), dict) else {}).get("title", ""),
            "current_price": ((brief_payload.get("market") or {}) if isinstance(brief_payload.get("market"), dict) else {}).get("current_price"),
            "last_reasoned_price": ((brief_payload.get("market") or {}) if isinstance(brief_payload.get("market"), dict) else {}).get("last_reasoned_price"),
            "quote_timestamp": ((brief_payload.get("market") or {}) if isinstance(brief_payload.get("market"), dict) else {}).get("quote_timestamp", ""),
            "price_delta": ((brief_payload.get("refresh_assessment") or {}) if isinstance(brief_payload.get("refresh_assessment"), dict) else {}).get("price_delta"),
            "price_delta_pct_points": ((brief_payload.get("refresh_assessment") or {}) if isinstance(brief_payload.get("refresh_assessment"), dict) else {}).get("price_delta_pct_points"),
        },
        "decision_result": decision_result or {},
    }
    write_json(paths["manifest"], manifest, pretty=True)
    return manifest


def build_refresh_context(case_key: str, *, contract_id: str, refresh_id: str, pretty: bool) -> tuple[Path, dict[str, Any], dict[str, Any], dict[str, Path], str]:
    paths = refresh_bundle_paths(case_key, refresh_id)
    paths["root"].mkdir(parents=True, exist_ok=True)

    brief_proc = run_command([
        sys.executable,
        str(BUILD_LIGHT_REFRESH_BRIEF),
        "--case-key",
        case_key,
        "--contract-id",
        contract_id,
        *(["--pretty"] if pretty else []),
    ])
    brief_result = parse_json_stdout(brief_proc)

    canonical_brief_json = resolve_workspace_path(brief_result.get("light_refresh_brief_json")) or case_light_refresh_brief_json_path(case_key)
    canonical_brief_markdown = resolve_workspace_path(brief_result.get("light_refresh_brief_markdown")) or case_light_refresh_brief_markdown_path(case_key)
    brief_payload = load_json(canonical_brief_json)
    copy_if_exists(canonical_brief_json, paths["brief_json"])
    copy_if_exists(canonical_brief_markdown, paths["brief_markdown"])

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
        "--out",
        str(paths["decision_context_json"]),
        *(["--quote-timestamp", str(brief_result.get("quote_timestamp"))] if coerce_string(brief_result.get("quote_timestamp")) else []),
        *(["--pretty"] if pretty else []),
    ])
    context_result = parse_json_stdout(build_ctx_proc)
    context_path = paths["decision_context_json"]
    context_payload = load_json(context_path)

    original_dispatch_id = coerce_string(context_payload.get("dispatch_id"))
    context_payload["dispatch_id"] = refresh_id
    upstream = context_payload.get("upstream") if isinstance(context_payload.get("upstream"), dict) else {}
    upstream["light_refresh_brief_path"] = relative_to_workspace(paths["brief_json"])
    upstream["light_refresh_mode"] = coerce_string(((brief_payload.get("refresh_assessment") or {}) if isinstance(brief_payload.get("refresh_assessment"), dict) else {}).get("recommended_mode"))
    upstream["source_dispatch_id"] = original_dispatch_id
    upstream["source_decision_context_path"] = coerce_string(context_result.get("decision_context_path"))
    context_payload["upstream"] = upstream
    context_payload["light_refresh"] = brief_payload
    context_payload["refresh_bundle"] = {
        "refresh_id": refresh_id,
        "root": relative_to_workspace(paths["root"]),
        "light_refresh_brief_json": relative_to_workspace(paths["brief_json"]),
        "light_refresh_brief_markdown": relative_to_workspace(paths["brief_markdown"]),
        "decision_context_json": relative_to_workspace(context_path),
    }
    write_json(context_path, context_payload, pretty=True)
    return context_path, brief_result, brief_payload, paths, original_dispatch_id


def copy_refresh_artifacts(*, decision_result: dict[str, Any], paths: dict[str, Path]) -> dict[str, str]:
    copied: dict[str, str] = {}
    paths["inputs_dir"].mkdir(parents=True, exist_ok=True)
    paths["outputs_dir"].mkdir(parents=True, exist_ok=True)

    copied["verification_mode_json"] = copy_if_exists(
        resolve_workspace_path(decision_result.get("verification_mode_path")),
        paths["inputs_dir"] / "verification-mode.json",
    )
    copied["selected_input_bundle_json"] = copy_if_exists(
        resolve_workspace_path(decision_result.get("selected_input_bundle_path")),
        paths["inputs_dir"] / "selected-input-bundle.json",
    )
    copied["targeted_verification_pack_json"] = copy_if_exists(
        resolve_workspace_path(decision_result.get("targeted_verification_pack_path")),
        paths["inputs_dir"] / "targeted-verification-pack.json",
    )
    prompt_source = resolve_workspace_path(decision_result.get("prompt_path"))
    prompt_dest_name = prompt_source.name if prompt_source is not None else "decision-prompt.txt"
    copied["decision_prompt"] = copy_if_exists(prompt_source, paths["inputs_dir"] / prompt_dest_name)
    copied["decision_packet_json"] = copy_if_exists(
        resolve_workspace_path(decision_result.get("packet_json")),
        paths["outputs_dir"] / "decision-maker-packet.json",
    )
    copied["decision_packet_markdown"] = copy_if_exists(
        resolve_workspace_path(decision_result.get("decision_packet_path")),
        paths["outputs_dir"] / "decision-maker-packet.md",
    )
    copied["decision_stage_status_json"] = copy_if_exists(
        resolve_workspace_path(decision_result.get("decision_stage_status_path")),
        paths["outputs_dir"] / "decision-stage-status.json",
    )
    return copied


def main() -> int:
    args = parse_args()
    refresh_id = refresh_dispatch_id(args.case_key)
    context_path, brief_result, brief_payload, paths, original_dispatch_id = build_refresh_context(args.case_key, contract_id=args.contract_id, refresh_id=refresh_id, pretty=args.pretty)
    refresh_mode = coerce_string(((brief_payload.get("refresh_assessment") or {}) if isinstance(brief_payload.get("refresh_assessment"), dict) else {}).get("recommended_mode")) or "light"

    if args.prepare_only:
        manifest = write_refresh_manifest(
            case_key=args.case_key,
            refresh_id=refresh_id,
            contract_id=args.contract_id,
            refresh_mode=refresh_mode,
            brief_payload=brief_payload,
            paths=paths,
            original_dispatch_id=original_dispatch_id,
            copied_artifacts={},
            decision_result=None,
            prepared_only=True,
        )
        print(json.dumps({
            "ok": True,
            "prepared_only": True,
            "case_key": args.case_key,
            "contract_id": args.contract_id,
            "refresh_id": refresh_id,
            "refresh_mode": refresh_mode,
            "light_refresh_brief": brief_result,
            "decision_context_json": relative_to_workspace(context_path),
            "refresh_bundle_root": relative_to_workspace(paths["root"]),
            "refresh_manifest_json": relative_to_workspace(paths["manifest"]),
            "refresh_manifest": manifest,
        }, indent=2 if args.pretty else None))
        return 0

    decision_proc = run_command([
        sys.executable,
        str(RUN_DECISION_MAKER),
        "--decision-context-json",
        str(context_path),
        "--timeout-seconds",
        str(args.timeout_seconds),
        *(["--pretty"] if args.pretty else []),
    ])
    decision_result = parse_json_stdout(decision_proc)
    copied_artifacts = copy_refresh_artifacts(decision_result=decision_result, paths=paths)
    manifest = write_refresh_manifest(
        case_key=args.case_key,
        refresh_id=refresh_id,
        contract_id=args.contract_id,
        refresh_mode=refresh_mode,
        brief_payload=brief_payload,
        paths=paths,
        original_dispatch_id=original_dispatch_id,
        copied_artifacts=copied_artifacts,
        decision_result=decision_result,
        prepared_only=False,
    )
    timeline_update = append_refresh_timeline_entry(
        case_key=args.case_key,
        refresh_id=refresh_id,
        manifest_path=paths["manifest"],
        packet_path=str(copied_artifacts.get("decision_packet_markdown") or ""),
    )

    print(json.dumps({
        "ok": True,
        "case_key": args.case_key,
        "contract_id": args.contract_id,
        "refresh_id": refresh_id,
        "refresh_mode": refresh_mode,
        "light_refresh_brief": brief_result,
        "decision_context_json": relative_to_workspace(context_path),
        "decision_result": decision_result,
        "refresh_bundle_root": relative_to_workspace(paths["root"]),
        "refresh_manifest_json": relative_to_workspace(paths["manifest"]),
        "refresh_manifest": manifest,
        "refresh_bundle_artifacts": copied_artifacts,
        "timeline_update": timeline_update,
    }, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
