#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.case_artifacts import discover_case_artifacts  # noqa: E402
from lib.db import DEFAULT_PSQL  # noqa: E402
from lib.paths import ensure_parent, learning_packet_path, to_repo_relative  # noqa: E402
from lib.io import write_json  # noqa: E402
from lib.quant_truth import load_case_quant_truth  # noqa: E402
from build_case_event_timeline import build_timeline  # noqa: E402


def _float_or_none(value: Any) -> float | None:
    try:
        return float(value)
    except Exception:
        return None


def _load_quant_truth(case_key: str, *, contract_id: str, db_url: str, psql_bin: str, warnings: list[str]) -> dict[str, Any]:
    try:
        payload = load_case_quant_truth(case_key, contract_id=contract_id, db_url=db_url, psql_bin=psql_bin)
    except Exception as exc:
        warnings.append(f"quant_truth_unavailable:{str(exc)}")
        return {"db_available": False, "error": str(exc)}
    if not payload.get("case"):
        warnings.append("quant_truth_case_not_found")
    return payload


def _append_quant_events(base_timeline: dict[str, Any], quant_truth: dict[str, Any]) -> dict[str, Any]:
    events = list((base_timeline or {}).get("events") or [])
    latest_forecast = quant_truth.get("latest_forecast") or {}
    initial_forecast = quant_truth.get("initial_forecast") or {}

    if initial_forecast:
        events.append(
            {
                "ts": initial_forecast.get("decision_ts"),
                "event_type": "forecast_recorded_initial",
                "observed": True,
                "summary": f"initial forecast recorded at {initial_forecast.get('forecast_prob')}",
                "source_paths": [initial_forecast.get("decision_packet_path")] if initial_forecast.get("decision_packet_path") else [],
                "metadata": {
                    "forecast_id": initial_forecast.get("forecast_id"),
                    "forecast_prob": initial_forecast.get("forecast_prob"),
                    "resolution_status": initial_forecast.get("resolution_status"),
                },
            }
        )
    if latest_forecast and latest_forecast.get("forecast_id") != initial_forecast.get("forecast_id"):
        events.append(
            {
                "ts": latest_forecast.get("decision_ts"),
                "event_type": "forecast_recorded_latest",
                "observed": True,
                "summary": f"latest forecast recorded at {latest_forecast.get('forecast_prob')}",
                "source_paths": [latest_forecast.get("decision_packet_path")] if latest_forecast.get("decision_packet_path") else [],
                "metadata": {
                    "forecast_id": latest_forecast.get("forecast_id"),
                    "forecast_prob": latest_forecast.get("forecast_prob"),
                    "resolution_status": latest_forecast.get("resolution_status"),
                    "brier_component": latest_forecast.get("brier_component"),
                },
            }
        )
    if latest_forecast.get("resolved_ts"):
        events.append(
            {
                "ts": latest_forecast.get("resolved_ts"),
                "event_type": "market_resolved",
                "observed": True,
                "summary": f"market resolution recorded as {latest_forecast.get('resolved_outcome') or latest_forecast.get('resolved_value')}",
                "source_paths": [],
                "metadata": {
                    "resolution_status": latest_forecast.get("resolution_status"),
                    "resolved_outcome": latest_forecast.get("resolved_outcome"),
                    "resolved_value": latest_forecast.get("resolved_value"),
                    "resolution_source": latest_forecast.get("resolution_source"),
                },
            }
        )

    merged = dict(base_timeline or {})
    merged["events"] = sorted(
        events,
        key=lambda item: ((item.get("ts") or ""), (item.get("event_type") or "")),
    )
    merged["event_count"] = len(merged["events"])
    if not quant_truth.get("db_available"):
        warnings = list(merged.get("warnings") or [])
        warnings.append("quant_truth_not_available_for_timeline")
        merged["warnings"] = warnings
    return merged


def compile_learning_packet(case_key: str, *, contract_id: str = "yes", db_url: str = "", psql_bin: str = DEFAULT_PSQL) -> dict[str, Any]:
    artifacts = discover_case_artifacts(case_key)
    case_markdown = artifacts["case_markdown"]
    frontmatter = case_markdown["frontmatter"]
    bullet_map = case_markdown["bullet_map"]
    current = artifacts.get("swarm_current") or {}
    current_bullets = current.get("bullet_map") or {}
    decision_packet = artifacts.get("decision_packet_json") or {}
    decision = decision_packet.get("decision") or {}
    valuation = decision_packet.get("valuation") or {}
    context = decision_packet.get("context") or {}
    synthesis_runtime = artifacts.get("synthesis_runtime") or {}
    persona_runs = artifacts.get("persona_runs") or []

    warnings: list[str] = []
    quant_truth = _load_quant_truth(case_key, contract_id=contract_id, db_url=db_url, psql_bin=psql_bin, warnings=warnings)
    quant_case = quant_truth.get("case") or {}
    initial_forecast = quant_truth.get("initial_forecast") or {}
    latest_forecast = quant_truth.get("latest_forecast") or {}
    forecast_rows = quant_truth.get("forecast_rows") or []
    snapshot_summary = quant_truth.get("snapshot_summary") or {}
    recent_snapshots = quant_truth.get("recent_snapshots") or []
    forecast_summary = quant_truth.get("forecast_summary") or {}

    timeline = _append_quant_events(build_timeline(case_key), quant_truth)

    title = next((line.strip()[2:].strip() for line in case_markdown["body"].splitlines() if line.startswith("# ")), None)
    description = ""
    capture = False
    for line in case_markdown["body"].splitlines():
        if line.strip() == "## Description":
            capture = True
            continue
        if capture and line.startswith("## "):
            break
        if capture and line.strip():
            description = (description + " " + line.strip()).strip()

    if (frontmatter.get("status") != "resolved") and latest_forecast.get("resolution_status") != "resolved":
        warnings.append("case_not_marked_resolved")
    if not decision_packet:
        warnings.append("missing_decision_packet_json")
    if not persona_runs:
        warnings.append("no_persona_sidecars_detected")

    own_probabilities = [item.get("own_probability") for item in persona_runs if isinstance(item.get("own_probability"), (int, float))]

    packet = {
        "artifact_type": "resolved_case_learning_packet",
        "schema_version": "v2-draft",
        "packet_status": "draft",
        "case_key": case_key,
        "case_id": quant_case.get("case_db_id") or frontmatter.get("case_id"),
        "market_id": quant_case.get("market_id") or frontmatter.get("market_id"),
        "contract_id": latest_forecast.get("contract_id") or contract_id or frontmatter.get("external_market_id"),
        "title": quant_case.get("title") or title,
        "description": quant_case.get("description") or description,
        "category": quant_case.get("category"),
        "platform": quant_case.get("platform") or frontmatter.get("platform"),
        "opened_at": quant_case.get("opened_at"),
        "resolved_at": latest_forecast.get("resolved_ts") or quant_case.get("closed_at"),
        "case_status": quant_case.get("case_status") or frontmatter.get("status"),
        "market_truth": {
            "platform": quant_case.get("platform") or frontmatter.get("platform"),
            "external_market_id": quant_case.get("external_market_id") or frontmatter.get("external_market_id"),
            "slug": quant_case.get("slug") or frontmatter.get("slug"),
            "current_price_at_case_note": _float_or_none(bullet_map.get("current_price")),
            "current_price_from_db": _float_or_none(quant_case.get("current_price")),
            "last_reasoned_price": _float_or_none(quant_case.get("last_reasoned_price")),
            "closes_at": quant_case.get("closes_at") or bullet_map.get("closes_at"),
            "resolves_at": quant_case.get("resolves_at") or bullet_map.get("resolves_at"),
            "resolution_source": latest_forecast.get("resolution_source") or context.get("primary_market_url"),
            "resolution_status": latest_forecast.get("resolution_status") or "unresolved",
            "resolved_outcome": latest_forecast.get("resolved_outcome"),
            "resolved_value": latest_forecast.get("resolved_value"),
            "resolved_ts": latest_forecast.get("resolved_ts"),
            "price_path_summary": {
                "current_price": _float_or_none(quant_case.get("current_price")) or _float_or_none(bullet_map.get("current_price")),
                "market_reference_price": valuation.get("market_reference_price"),
                "snapshot_count": snapshot_summary.get("snapshot_count"),
                "min_reference_price": _float_or_none(snapshot_summary.get("min_reference_price")),
                "max_reference_price": _float_or_none(snapshot_summary.get("max_reference_price")),
                "avg_reference_price": _float_or_none(snapshot_summary.get("avg_reference_price")),
                "oldest_observed_at": snapshot_summary.get("oldest_observed_at"),
                "latest_observed_at": snapshot_summary.get("latest_observed_at"),
                "major_move_windows": [],
            },
        },
        "quant_truth": {
            "db_available": quant_truth.get("db_available", False),
            "case": quant_case,
            "initial_forecast": initial_forecast,
            "latest_forecast": latest_forecast,
            "forecast_summary": forecast_summary,
            "forecast_rows": forecast_rows,
            "snapshot_summary": snapshot_summary,
            "recent_snapshots": recent_snapshots,
        },
        "forecast_summary": {
            "initial_forecast_prob": initial_forecast.get("forecast_prob"),
            "latest_forecast_prob": latest_forecast.get("forecast_prob"),
            "resolved_value": latest_forecast.get("resolved_value"),
            "initial_brier_component": initial_forecast.get("brier_component"),
            "latest_brier_component": latest_forecast.get("brier_component"),
            "decision_count": forecast_summary.get("forecast_count") or len(forecast_rows),
            "resolved_forecast_count": forecast_summary.get("resolved_forecast_count"),
            "first_decision_ts": forecast_summary.get("first_decision_ts"),
            "latest_decision_ts": forecast_summary.get("latest_decision_ts"),
        },
        "analysis_context": {
            "dispatch_id": artifacts.get("dispatch_id"),
            "dispatch_dir": artifacts.get("dispatch_dir_rel"),
            "pipeline_status": current_bullets.get("pipeline_status"),
            "current_stage": current_bullets.get("current_stage"),
            "expected_persona_count": current_bullets.get("expected_persona_count"),
            "completed_persona_count": current_bullets.get("completed_persona_count"),
            "difficulty_class": None,
            "resolution_risk": None,
            "evidence_floor": None,
        },
        "belief_evolution": {
            "persona_probabilities": [
                {"persona": item.get("persona"), "own_probability": item.get("own_probability")} for item in persona_runs
            ],
            "persona_probability_min": min(own_probabilities) if own_probabilities else None,
            "persona_probability_max": max(own_probabilities) if own_probabilities else None,
            "initial_forecast_prob": initial_forecast.get("forecast_prob"),
            "latest_forecast_prob": latest_forecast.get("forecast_prob"),
            "decision_fair_value_low": valuation.get("fair_value_low"),
            "decision_fair_value_high": valuation.get("fair_value_high"),
            "decision_fair_value_mid": valuation.get("fair_value_mid"),
            "market_reference_price": valuation.get("market_reference_price") or _float_or_none(quant_case.get("current_price")),
            "edge_mid_vs_market_pct_points": valuation.get("edge_mid_vs_market_pct_points"),
        },
        "research_summary": {
            "summary_path": artifacts.get("summary_path"),
            "dispatch_ids": [artifacts.get("dispatch_id")] if artifacts.get("dispatch_id") else [],
            "persona_runs": persona_runs,
            "source_note_paths": artifacts.get("source_note_paths") or [],
            "assumption_note_paths": artifacts.get("assumption_paths") or [],
            "evidence_map_paths": artifacts.get("evidence_paths") or [],
            "synthesis_path": to_repo_relative(artifacts.get("synthesis_runtime_path")) if artifacts.get("synthesis_runtime_path") and artifacts.get("synthesis_runtime_path").exists() else None,
            "refresh_packet_paths": artifacts.get("refresh_packet_paths") or [],
        },
        "decision_summary": {
            "decision_status": decision.get("decision_readiness"),
            "side": decision.get("side"),
            "trade_authorization": decision.get("trade_authorization"),
            "position_policy": decision.get("position_policy"),
            "target_probability": valuation.get("fair_value_mid"),
            "decision_packet_path": to_repo_relative(artifacts.get("decision_packet_json_path")) if artifacts.get("decision_packet_json_path") and artifacts.get("decision_packet_json_path").exists() else None,
            "primary_crux": decision.get("primary_crux"),
            "thesis_class": decision.get("thesis_class"),
        },
        "synthesis_summary": {
            "dispatch_id": synthesis_runtime.get("dispatch_id"),
            "synthesis_method": synthesis_runtime.get("synthesis_method"),
            "synthesis_status": synthesis_runtime.get("synthesis_status"),
            "market_snapshot_time": synthesis_runtime.get("market_snapshot_time"),
            "artifact_path": synthesis_runtime.get("artifact_path"),
        },
        "causal_attribution": {
            "observed_facts": [],
            "inferred_attributions": [],
            "note": "Evaluator distinguishes observed market/action facts from inferred causal attributions. Attribution population is intentionally left sparse until structured event + market-path reconstruction is implemented."
        },
        "event_timeline": timeline,
        "provenance_paths": {
            "case_markdown": to_repo_relative(case_markdown["path"]),
            "swarm_current": to_repo_relative(current.get("path")) if current.get("path") else None,
            "timeline_markdown": to_repo_relative(artifacts.get("timeline_path")) if artifacts.get("timeline_path") and artifacts.get("timeline_path").exists() else None,
            "decision_packet_json": to_repo_relative(artifacts.get("decision_packet_json_path")) if artifacts.get("decision_packet_json_path") and artifacts.get("decision_packet_json_path").exists() else None,
            "synthesis_runtime_json": to_repo_relative(artifacts.get("synthesis_runtime_path")) if artifacts.get("synthesis_runtime_path") and artifacts.get("synthesis_runtime_path").exists() else None,
        },
        "runtime_metadata": {
            "compiled_by": "roles/evaluator/runtime/scripts/compile_learning_packet.py",
            "compiler_version": "learning-packet-v2-draft",
            "db_url_source": "explicit_or_env" if (db_url or quant_truth.get("db_available")) else "none",
        },
        "warnings": warnings,
    }
    return packet


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compile a draft evaluator learning packet for one case")
    parser.add_argument("--case-key", required=True)
    parser.add_argument("--contract-id", default="yes")
    parser.add_argument("--db-url", default="")
    parser.add_argument("--psql", default=DEFAULT_PSQL)
    parser.add_argument("--out")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    packet = compile_learning_packet(
        args.case_key,
        contract_id=args.contract_id,
        db_url=args.db_url,
        psql_bin=args.psql,
    )
    out_path = Path(args.out) if args.out else learning_packet_path(args.case_key)
    ensure_parent(out_path)
    write_json(out_path, packet, pretty=True if args.pretty or True else False)
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
