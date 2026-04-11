#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR.parent
SUBAGENT_DIR = SCRIPTS_DIR.parents[1]
for path in [SCRIPTS_DIR, SUBAGENT_DIR]:
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from common import WORKSPACE_ROOT, load_json, relative_to_workspace  # noqa: E402
from status import append_stage_event, locked_status  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Repair synthesis-stage structured bundle path to the canonical sidecar bundle")
    parser.add_argument("--status-file", required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def resolve_workspace_path(path_str: str) -> Path | None:
    if not path_str:
        return None
    path = Path(path_str)
    if not path.is_absolute():
        path = WORKSPACE_ROOT / path
    return path


def valid_sidecar_bundle(path: Path | None) -> bool:
    if path is None or not path.exists():
        return False
    try:
        payload = load_json(path)
    except Exception:
        return False
    return (
        isinstance(payload, dict)
        and str(payload.get("artifact_type") or "").strip() == "sidecar_synthesis_bundle"
        and isinstance(payload.get("sidecars"), list)
        and bool(payload.get("sidecars"))
    )


def find_candidate(status_path: Path, status: dict[str, Any]) -> Path | None:
    candidates: list[Path] = []
    structured_value = str(status.get("structured_bundle_path") or "").strip()
    if structured_value:
        structured_path = resolve_workspace_path(structured_value)
        if structured_path is not None:
            candidates.append(structured_path)
            candidates.append(structured_path.with_name("sidecar-synthesis-bundle.json"))
    bundle_value = str(status.get("bundle_path") or "").strip()
    if bundle_value:
        bundle_path = resolve_workspace_path(bundle_value)
        if bundle_path is not None:
            candidates.append(bundle_path.with_name("sidecar-synthesis-bundle.json"))
    candidates.append(status_path.with_name("sidecar-synthesis-bundle.json"))

    seen: set[str] = set()
    for candidate in candidates:
        key = str(candidate)
        if key in seen:
            continue
        seen.add(key)
        if valid_sidecar_bundle(candidate):
            return candidate
    return None


def main() -> int:
    args = parse_args()
    status_path = Path(args.status_file).expanduser().resolve()
    status = load_json(status_path)
    candidate = find_candidate(status_path, status)
    current_value = str(status.get("structured_bundle_path") or "").strip()
    current_artifact_type = str(status.get("structured_bundle_artifact_type") or "").strip()
    candidate_rel = relative_to_workspace(candidate) if candidate else ""
    drift_detected = bool(candidate_rel and (current_value != candidate_rel or current_artifact_type != "sidecar_synthesis_bundle"))

    if args.apply and candidate_rel:
        with locked_status(status_path) as locked:
            locked["structured_bundle_path"] = candidate_rel
            locked["structured_bundle_artifact_type"] = "sidecar_synthesis_bundle"
            append_stage_event(
                locked,
                stage="structured_bundle_repair",
                state="applied",
                message="Repaired synthesis-stage structured bundle path to canonical sidecar bundle",
                extra={"structured_bundle_path": candidate_rel},
            )
    elif args.apply and not candidate_rel:
        return 1

    out = {
        "ok": bool(candidate_rel),
        "status_file": relative_to_workspace(status_path),
        "apply_requested": args.apply,
        "current_structured_bundle_path": current_value,
        "current_structured_bundle_artifact_type": current_artifact_type,
        "resolved_structured_bundle_path": candidate_rel,
        "resolved_structured_bundle_artifact_type": "sidecar_synthesis_bundle" if candidate_rel else "",
        "drift_detected": drift_detected,
        "applied": bool(args.apply and candidate_rel),
    }
    print(json.dumps(out, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
