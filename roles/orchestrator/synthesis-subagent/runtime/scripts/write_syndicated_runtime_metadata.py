#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import (  # noqa: E402
    RUNTIME_METADATA_FIELDS,
    WORKSPACE_ROOT,
    case_synthesis_markdown_path_for,
    load_json,
    relative_to_workspace,
    runtime_json_path_for,
    write_json,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write syndicated-finding runtime metadata sidecar JSON")
    parser.add_argument("--bundle-json", required=True)
    parser.add_argument("--artifact-path", required=True, help="Rendered syndicated-finding markdown path")
    parser.add_argument("--out", help="Optional explicit sidecar output path")
    parser.add_argument("--generated-by", default="orchestrator")
    parser.add_argument("--synthesis-method", default="dispatch_bundle_v1")
    parser.add_argument("--synthesis-status", default="rendered")
    parser.add_argument("--write-current", action="store_true", help="Also write the canonical case-level sidecar under cases/<case-key>/synthesizer-agent/")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def build_sidecar(bundle: dict, artifact_path: Path, args: argparse.Namespace) -> OrderedDict[str, object]:
    artifact_rel = relative_to_workspace(artifact_path)
    data = OrderedDict()
    values = {
        "artifact_type": "syndicated_finding_runtime_metadata",
        "artifact_path": artifact_rel,
        "case_key": bundle.get("case_key", ""),
        "dispatch_id": bundle.get("dispatch_id", ""),
        "question": bundle.get("question", ""),
        "generated_by": args.generated_by,
        "synthesis_method": args.synthesis_method,
        "synthesis_status": args.synthesis_status,
        "market_snapshot_time": bundle.get("market_snapshot_time", ""),
        "source_personas": bundle.get("source_personas", []),
        "missing_personas": bundle.get("missing_personas", []),
        "source_finding_paths": bundle.get("source_finding_paths", []),
        "source_supporting_artifacts": bundle.get("source_supporting_artifacts", []),
        "source_persona_count": bundle.get("source_persona_count", 0),
        "missing_persona_count": bundle.get("missing_persona_count", 0),
        "supporting_artifact_count": bundle.get("supporting_artifact_count", 0),
        "upstream_inputs": bundle.get("upstream_inputs", []),
        "downstream_uses": bundle.get("downstream_uses", []),
    }
    for key in RUNTIME_METADATA_FIELDS:
        data[key] = values.get(key, "")
    return data


def main() -> None:
    args = parse_args()
    bundle_path = Path(args.bundle_json)
    artifact_path = Path(args.artifact_path)
    if not bundle_path.is_absolute():
        bundle_path = WORKSPACE_ROOT / bundle_path
    if not artifact_path.is_absolute():
        artifact_path = WORKSPACE_ROOT / artifact_path

    bundle = load_json(bundle_path)
    sidecar = build_sidecar(bundle, artifact_path, args)

    out_path = Path(args.out) if args.out else runtime_json_path_for(artifact_path)
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    write_json(out_path, sidecar, pretty=args.pretty)

    current_sidecar_path = None
    if args.write_current:
        current_artifact_path = case_synthesis_markdown_path_for(bundle["case_key"])
        current_sidecar_path = runtime_json_path_for(current_artifact_path)
        current_sidecar = build_sidecar(bundle, current_artifact_path, args)
        write_json(current_sidecar_path, current_sidecar, pretty=args.pretty)

    summary = {
        "ok": True,
        "bundle_json": relative_to_workspace(bundle_path),
        "artifact_path": relative_to_workspace(artifact_path),
        "sidecar_path": relative_to_workspace(out_path),
        "current_sidecar_path": relative_to_workspace(current_sidecar_path) if current_sidecar_path else "",
    }
    print(json.dumps(summary, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
