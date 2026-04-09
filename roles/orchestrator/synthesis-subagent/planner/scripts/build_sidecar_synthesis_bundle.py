#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from statistics import median
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import WORKSPACE_ROOT, load_json, normalize_probability, relative_to_workspace, write_json  # noqa: E402
from validation import reasoning_sidecar_core_payload, validate_reasoning_sidecar_artifact  # noqa: E402

BUILD_BUNDLE = SUBAGENT_DIR / "planner" / "scripts" / "build_synthesis_bundle.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the structured synthesis bundle directly from validated researcher sidecars")
    parser.add_argument("--bundle-json", help="Existing raw synthesis bundle JSON")
    parser.add_argument("--dispatch-id", help="Dispatch id to build from if bundle is not supplied")
    parser.add_argument("--case-key", help="Optional case key to disambiguate dispatch lookup")
    parser.add_argument("--allow-partial", action="store_true", help="Allow missing persona sidecars and emit a partial sidecar bundle")
    parser.add_argument("--out", help="Optional output path for sidecar-synthesis-bundle.json")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def run_json(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(cmd, cwd=str(WORKSPACE_ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(
            f"command failed ({proc.returncode}): {' '.join(cmd)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
        )
    stdout = proc.stdout.strip()
    return json.loads(stdout) if stdout else {}


def ensure_bundle(args: argparse.Namespace) -> Path:
    if args.bundle_json:
        bundle_path = Path(args.bundle_json)
        if not bundle_path.is_absolute():
            bundle_path = WORKSPACE_ROOT / bundle_path
        return bundle_path
    if not args.dispatch_id:
        raise SystemExit("either --bundle-json or --dispatch-id is required")
    cmd = [sys.executable, str(BUILD_BUNDLE), "--dispatch-id", args.dispatch_id]
    if args.case_key:
        cmd.extend(["--case-key", args.case_key])
    if args.pretty:
        cmd.append("--pretty")
    return WORKSPACE_ROOT / run_json(cmd)["bundle_path"]


def provisional_swarm_skepticism(bundle: dict[str, Any], probability_estimates: list[dict[str, Any]]) -> dict[str, Any]:
    market = normalize_probability(bundle.get("market_implied_probability"))
    probs = [normalize_probability(item.get("own_probability")) for item in probability_estimates]
    numeric_probs = sorted(prob for prob in probs if prob is not None)
    if market is None or not numeric_probs:
        return {
            "persona_probability_estimate_count": len(numeric_probs),
            "provisional_swarm_probability_low": None,
            "provisional_swarm_probability_high": None,
            "provisional_swarm_probability_median": None,
            "provisional_swarm_edge_vs_market_pct_points": None,
            "provisional_edge_verification_bar": "unknown",
        }
    median_prob = round(float(median(numeric_probs)), 4)
    low_prob = round(float(numeric_probs[0]), 4)
    high_prob = round(float(numeric_probs[-1]), 4)
    edge = round((median_prob - market) * 100.0, 1)
    abs_edge = abs(edge)
    if abs_edge < 3.0:
        bar = "normal"
    elif abs_edge < 7.0:
        bar = "elevated"
    elif abs_edge < 12.0:
        bar = "high"
    else:
        bar = "very_high"
    return {
        "persona_probability_estimate_count": len(numeric_probs),
        "provisional_swarm_probability_low": low_prob,
        "provisional_swarm_probability_high": high_prob,
        "provisional_swarm_probability_median": median_prob,
        "provisional_swarm_edge_vs_market_pct_points": edge,
        "provisional_edge_verification_bar": bar,
    }


def main() -> None:
    args = parse_args()
    bundle_path = ensure_bundle(args)
    bundle = load_json(bundle_path)

    sidecars = []
    missing_personas: list[str] = []
    invalid_sidecars: list[dict[str, Any]] = []
    probability_estimates = []
    reasoning_mode_counter: Counter[str] = Counter()
    recommended_weight_counter: Counter[str] = Counter()

    for persona_entry in bundle.get("persona_findings", []):
        persona = str(persona_entry.get("persona") or "").strip()
        sidecar_path_rel = str(persona_entry.get("reasoning_sidecar_path") or "").strip()
        if not sidecar_path_rel:
            missing_personas.append(persona)
            continue
        sidecar_path = WORKSPACE_ROOT / sidecar_path_rel if not Path(sidecar_path_rel).is_absolute() else Path(sidecar_path_rel)
        if not sidecar_path.exists():
            missing_personas.append(persona)
            continue
        payload = load_json(sidecar_path)
        validation = validate_reasoning_sidecar_artifact(
            payload,
            persona_finding_path=str(persona_entry.get("path") or ""),
            source_persona_sha256=str(persona_entry.get("sha256") or ""),
            persona=persona,
        )
        if not validation["ok"]:
            invalid_sidecars.append({
                "persona": persona,
                "path": relative_to_workspace(sidecar_path),
                "errors": validation["errors"],
                "warnings": validation["warnings"],
            })
            continue
        core_payload = reasoning_sidecar_core_payload(payload)
        sidecar_entry = {
            "persona": persona,
            "path": relative_to_workspace(sidecar_path),
            "payload": core_payload,
            "runtime_metadata": payload.get("runtime_metadata") if isinstance(payload, dict) else None,
            "persona_finding_path": persona_entry.get("path", ""),
            "assumption_artifact_paths": [artifact.get("path", "") for artifact in bundle.get("supporting_artifacts", []) if artifact.get("kind") == "assumption" and artifact.get("persona") == persona],
            "evidence_artifact_paths": [artifact.get("path", "") for artifact in bundle.get("supporting_artifacts", []) if artifact.get("kind") == "evidence" and artifact.get("persona") == persona],
        }
        sidecars.append(sidecar_entry)
        if core_payload.get("own_probability") not in (None, ""):
            probability_estimates.append({
                "persona": persona,
                "own_probability": core_payload.get("own_probability"),
            })
        for mode in core_payload.get("reasoning_mode", []):
            reasoning_mode_counter[str(mode)] += 1
        recommended_weight_counter[str(core_payload.get("recommended_weight") or "")] += 1

    if invalid_sidecars:
        print(json.dumps({
            "ok": False,
            "error": "invalid reasoning sidecars",
            "invalid_sidecars": invalid_sidecars,
            "bundle_json": relative_to_workspace(bundle_path),
        }, indent=2 if args.pretty else None))
        raise SystemExit(1)

    if missing_personas and not args.allow_partial:
        print(json.dumps({
            "ok": False,
            "error": "missing reasoning sidecars",
            "missing_personas": missing_personas,
            "bundle_json": relative_to_workspace(bundle_path),
        }, indent=2 if args.pretty else None))
        raise SystemExit(1)

    skepticism = provisional_swarm_skepticism(bundle, probability_estimates)
    sidecar_bundle = {
        "artifact_type": "sidecar_synthesis_bundle",
        "case_key": bundle.get("case_key", ""),
        "dispatch_id": bundle.get("dispatch_id", ""),
        "analysis_date": bundle.get("analysis_date", ""),
        "question": bundle.get("question", ""),
        "market_implied_probability": bundle.get("market_implied_probability"),
        "market_snapshot_time": bundle.get("market_snapshot_time", ""),
        "coverage_status": "partial" if missing_personas else "complete",
        "source_bundle_path": relative_to_workspace(bundle_path),
        "available_personas": [entry["persona"] for entry in sidecars],
        "missing_personas": missing_personas,
        "sidecar_count": len(sidecars),
        "reasoning_mode_counts": dict(sorted(reasoning_mode_counter.items())),
        "recommended_weight_counts": {k: v for k, v in sorted(recommended_weight_counter.items()) if k},
        "persona_probability_estimates": probability_estimates,
        **skepticism,
        "sidecars": sidecars,
    }

    out_path = Path(args.out) if args.out else bundle_path.with_name("sidecar-synthesis-bundle.json")
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    write_json(out_path, sidecar_bundle, pretty=args.pretty)

    summary = {
        "ok": True,
        "bundle_json": relative_to_workspace(bundle_path),
        "sidecar_bundle_path": relative_to_workspace(out_path),
        "sidecar_count": len(sidecars),
        "missing_personas": missing_personas,
        "coverage_status": sidecar_bundle["coverage_status"],
    }
    print(json.dumps(summary, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
