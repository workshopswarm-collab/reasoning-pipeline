#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from statistics import median
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SUBAGENT_DIR = SCRIPT_DIR.parents[1]
if str(SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SUBAGENT_DIR))

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    load_json,
    normalize_probability,
    reasoning_extract_prompt_path_for,
    relative_to_workspace,
    write_json,
)
from validation import reasoning_extract_core_payload, validate_reasoning_extract_artifact  # noqa: E402

BUILD_BUNDLE = SUBAGENT_DIR / "planner" / "scripts" / "build_synthesis_bundle.py"
BUILD_JOBS = SUBAGENT_DIR / "planner" / "scripts" / "build_reasoning_extract_jobs.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the structured synthesis bundle from validated persona reasoning extracts")
    parser.add_argument("--bundle-json", help="Existing raw synthesis bundle JSON")
    parser.add_argument("--jobs-json", help="Existing reasoning-extract-jobs JSON")
    parser.add_argument("--dispatch-id", help="Dispatch id to build from if bundle/jobs are not supplied")
    parser.add_argument("--case-key", help="Optional case key to disambiguate dispatch lookup")
    parser.add_argument("--allow-partial", action="store_true", help="Allow missing persona extracts and emit a partial extracts bundle")
    parser.add_argument("--out", help="Optional output path for extracts-synthesis-bundle.json")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def run_json(cmd: list[str]) -> dict[str, Any]:
    import subprocess

    proc = subprocess.run(cmd, cwd=str(WORKSPACE_ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(
            f"command failed ({proc.returncode}): {' '.join(cmd)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
        )
    stdout = proc.stdout.strip()
    return json.loads(stdout) if stdout else {}


def ensure_bundle_and_jobs(args: argparse.Namespace) -> tuple[Path, Path]:
    if args.bundle_json:
        bundle_path = Path(args.bundle_json)
        if not bundle_path.is_absolute():
            bundle_path = WORKSPACE_ROOT / bundle_path
    else:
        if not args.dispatch_id:
            raise SystemExit("either --bundle-json or --dispatch-id is required")
        cmd = [sys.executable, str(BUILD_BUNDLE), "--dispatch-id", args.dispatch_id]
        if args.case_key:
            cmd.extend(["--case-key", args.case_key])
        if args.pretty:
            cmd.append("--pretty")
        bundle_path = WORKSPACE_ROOT / run_json(cmd)["bundle_path"]

    if args.jobs_json:
        jobs_path = Path(args.jobs_json)
        if not jobs_path.is_absolute():
            jobs_path = WORKSPACE_ROOT / jobs_path
    else:
        cmd = [sys.executable, str(BUILD_JOBS), "--bundle-json", str(bundle_path)]
        if args.pretty:
            cmd.append("--pretty")
        jobs_path = WORKSPACE_ROOT / run_json(cmd)["jobs_path"]
    return bundle_path, jobs_path


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
    bundle_path, jobs_path = ensure_bundle_and_jobs(args)
    bundle = load_json(bundle_path)
    jobs_payload = load_json(jobs_path)

    extracts = []
    missing_personas: list[str] = []
    invalid_extracts: list[dict[str, Any]] = []
    probability_estimates = []
    reasoning_mode_counter: Counter[str] = Counter()
    recommended_weight_counter: Counter[str] = Counter()

    for job in jobs_payload.get("jobs", []):
        persona = str(job.get("persona") or "").strip()
        extract_path_rel = str(job.get("reasoning_extract_path") or "").strip()
        extract_path = WORKSPACE_ROOT / extract_path_rel if extract_path_rel and not Path(extract_path_rel).is_absolute() else Path(extract_path_rel)
        if not extract_path_rel or not extract_path.exists():
            missing_personas.append(persona)
            continue
        payload = load_json(extract_path)
        prompt_path = reasoning_extract_prompt_path_for(jobs_path, persona)
        prompt_text = prompt_path.read_text() if prompt_path.exists() else None
        validation = validate_reasoning_extract_artifact(payload, job=job, prompt_text=prompt_text)
        if not validation["ok"]:
            invalid_extracts.append({
                "persona": persona,
                "path": relative_to_workspace(extract_path),
                "errors": validation["errors"],
                "warnings": validation["warnings"],
            })
            continue
        extract_entry = {
            "persona": persona,
            "path": relative_to_workspace(extract_path),
            "payload": reasoning_extract_core_payload(payload),
            "runtime_metadata": payload.get("runtime_metadata") if isinstance(payload, dict) else None,
            "persona_finding_path": job.get("persona_finding_path", ""),
            "assumption_artifact_paths": [artifact.get("path", "") for artifact in job.get("assumption_artifacts", [])],
            "evidence_artifact_paths": [artifact.get("path", "") for artifact in job.get("evidence_artifacts", [])],
        }
        extracts.append(extract_entry)
        core_payload = reasoning_extract_core_payload(payload)
        if core_payload.get("own_probability") not in (None, ""):
            probability_estimates.append({
                "persona": persona,
                "own_probability": core_payload.get("own_probability"),
            })
        for mode in core_payload.get("reasoning_mode", []):
            reasoning_mode_counter[str(mode)] += 1
        recommended_weight_counter[str(core_payload.get("recommended_weight") or "")] += 1

    if invalid_extracts:
        print(json.dumps({
            "ok": False,
            "error": "invalid reasoning extracts",
            "invalid_extracts": invalid_extracts,
            "bundle_json": relative_to_workspace(bundle_path),
            "jobs_json": relative_to_workspace(jobs_path),
        }, indent=2 if args.pretty else None))
        raise SystemExit(1)

    if missing_personas and not args.allow_partial:
        print(json.dumps({
            "ok": False,
            "error": "missing reasoning extracts",
            "missing_personas": missing_personas,
            "bundle_json": relative_to_workspace(bundle_path),
            "jobs_json": relative_to_workspace(jobs_path),
        }, indent=2 if args.pretty else None))
        raise SystemExit(1)

    skepticism = provisional_swarm_skepticism(bundle, probability_estimates)

    extracts_bundle = {
        "artifact_type": "extracts_synthesis_bundle",
        "case_key": bundle.get("case_key", ""),
        "dispatch_id": bundle.get("dispatch_id", ""),
        "analysis_date": bundle.get("analysis_date", ""),
        "question": bundle.get("question", ""),
        "market_implied_probability": bundle.get("market_implied_probability"),
        "market_snapshot_time": bundle.get("market_snapshot_time", ""),
        "coverage_status": "partial" if missing_personas else "complete",
        "source_bundle_path": relative_to_workspace(bundle_path),
        "source_jobs_path": relative_to_workspace(jobs_path),
        "support_mode": jobs_payload.get("support_mode", "metadata_and_summaries_only"),
        "available_personas": [entry["persona"] for entry in extracts],
        "missing_personas": missing_personas,
        "extract_count": len(extracts),
        "reasoning_mode_counts": dict(sorted(reasoning_mode_counter.items())),
        "recommended_weight_counts": {k: v for k, v in sorted(recommended_weight_counter.items()) if k},
        "persona_probability_estimates": probability_estimates,
        **skepticism,
        "extracts": extracts,
    }

    out_path = Path(args.out) if args.out else bundle_path.with_name("extracts-synthesis-bundle.json")
    if not out_path.is_absolute():
        out_path = WORKSPACE_ROOT / out_path
    write_json(out_path, extracts_bundle, pretty=args.pretty)

    summary = {
        "ok": True,
        "bundle_json": relative_to_workspace(bundle_path),
        "jobs_json": relative_to_workspace(jobs_path),
        "extracts_bundle_path": relative_to_workspace(out_path),
        "extract_count": len(extracts),
        "missing_personas": missing_personas,
        "coverage_status": extracts_bundle["coverage_status"],
    }
    print(json.dumps(summary, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
