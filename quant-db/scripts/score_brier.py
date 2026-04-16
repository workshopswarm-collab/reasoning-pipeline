#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import statistics
import subprocess
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

SQL = r'''
WITH params AS (
  SELECT
    NULLIF(:'platform', '') AS platform,
    NULLIF(:'contract_id', '') AS contract_id,
    NULLIF(:'market_id', '') AS market_id,
    NULLIF(:'since_ts', '')::timestamptz AS since_ts,
    NULLIF(:'until_ts', '')::timestamptz AS until_ts
),
resolved_all AS (
  SELECT fdr.*
  FROM public.forecast_decisions_with_resolution fdr
  CROSS JOIN params p
  WHERE fdr.resolution_status = 'resolved'
    AND fdr.resolved_value IS NOT NULL
    AND (p.platform IS NULL OR fdr.forecast_platform = p.platform)
    AND (p.contract_id IS NULL OR fdr.contract_id = p.contract_id)
    AND (p.market_id IS NULL OR fdr.market_id = p.market_id)
    AND (p.since_ts IS NULL OR fdr.decision_ts >= p.since_ts)
    AND (p.until_ts IS NULL OR fdr.decision_ts <= p.until_ts)
),
resolved_latest AS (
  SELECT lfd.*
  FROM public.latest_forecast_decisions lfd
  CROSS JOIN params p
  WHERE lfd.resolution_status = 'resolved'
    AND lfd.resolved_value IS NOT NULL
    AND (p.platform IS NULL OR lfd.forecast_platform = p.platform)
    AND (p.contract_id IS NULL OR lfd.contract_id = p.contract_id)
    AND (p.market_id IS NULL OR lfd.market_id = p.market_id)
    AND (p.since_ts IS NULL OR lfd.decision_ts >= p.since_ts)
    AND (p.until_ts IS NULL OR lfd.decision_ts <= p.until_ts)
),
resolved_initial AS (
  SELECT ifd.*
  FROM public.initial_forecast_decisions ifd
  CROSS JOIN params p
  WHERE ifd.resolution_status = 'resolved'
    AND ifd.resolved_value IS NOT NULL
    AND (p.platform IS NULL OR ifd.forecast_platform = p.platform)
    AND (p.contract_id IS NULL OR ifd.contract_id = p.contract_id)
    AND (p.market_id IS NULL OR ifd.market_id = p.market_id)
    AND (p.since_ts IS NULL OR ifd.decision_ts >= p.since_ts)
    AND (p.until_ts IS NULL OR ifd.decision_ts <= p.until_ts)
),
all_metrics AS (
  SELECT
    COUNT(*) AS n,
    AVG(POWER(forecast_prob - resolved_value, 2)) AS brier,
    AVG(forecast_prob) AS avg_forecast_prob,
    AVG(resolved_value) AS avg_resolved_value,
    MIN(decision_ts) AS min_decision_ts,
    MAX(decision_ts) AS max_decision_ts
  FROM resolved_all
),
latest_metrics AS (
  SELECT
    COUNT(*) AS n,
    AVG(POWER(forecast_prob - resolved_value, 2)) AS brier,
    AVG(forecast_prob) AS avg_forecast_prob,
    AVG(resolved_value) AS avg_resolved_value,
    MIN(decision_ts) AS min_decision_ts,
    MAX(decision_ts) AS max_decision_ts
  FROM resolved_latest
),
initial_metrics AS (
  SELECT
    COUNT(*) AS n,
    AVG(POWER(forecast_prob - resolved_value, 2)) AS brier,
    AVG(forecast_prob) AS avg_forecast_prob,
    AVG(resolved_value) AS avg_resolved_value,
    MIN(decision_ts) AS min_decision_ts,
    MAX(decision_ts) AS max_decision_ts
  FROM resolved_initial
),
per_market_latest AS (
  SELECT json_agg(json_build_object(
    'forecast_id', forecast_id,
    'market_id', market_id,
    'contract_id', contract_id,
    'decision_ts', decision_ts,
    'forecast_prob', forecast_prob,
    'resolved_value', resolved_value,
    'brier_component', POWER(forecast_prob - resolved_value, 2)
  ) ORDER BY decision_ts DESC, forecast_id DESC) AS rows
  FROM resolved_latest
)
SELECT json_build_object(
  'filters', json_build_object(
    'platform', (SELECT platform FROM params),
    'contract_id', (SELECT contract_id FROM params),
    'market_id', (SELECT market_id FROM params),
    'since_ts', (SELECT since_ts FROM params),
    'until_ts', (SELECT until_ts FROM params)
  ),
  'initial', (SELECT row_to_json(x) FROM initial_metrics x),
  'latest', (SELECT row_to_json(x) FROM latest_metrics x),
  'all_rows', (SELECT row_to_json(x) FROM all_metrics x),
  'latest_rows', COALESCE((SELECT rows FROM per_market_latest), '[]'::json)
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compute Brier scores for forecast decisions")
    parser.add_argument("--platform", default="polymarket")
    parser.add_argument("--contract-id", default="")
    parser.add_argument("--market-id", default="")
    parser.add_argument("--since", dest="since_ts", default="")
    parser.add_argument("--until", dest="until_ts", default="")
    parser.add_argument("--cohort-min-yes", type=float, default=0.70)
    parser.add_argument("--cohort-max-yes", type=float, default=0.98)
    parser.add_argument("--cohort-min-volume-usd", type=float, default=10000.0)
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_EVALUATOR_URL") or os.getenv("PREDQUANT_ORCHESTRATOR_URL") or os.getenv("PREDQUANT_ADMIN_URL", ""))
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL))
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def exec_sql(psql_bin: str, db_url: str, sql: str, variables: dict[str, str]) -> dict[str, Any]:
    if not db_url:
        raise ValueError("--db-url, PREDQUANT_EVALUATOR_URL, PREDQUANT_ORCHESTRATOR_URL, or PREDQUANT_ADMIN_URL is required")
    cmd = [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1"]
    for key, value in variables.items():
        cmd.extend(["-v", f"{key}={value}"])
    cmd.extend(["-f", "-"])
    proc = subprocess.run(cmd, input=sql, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    if not stdout:
        return {}
    return json.loads(stdout.splitlines()[-1])


def mean_brier(rows: list[dict[str, Any]], probability: float) -> float | None:
    values = []
    for row in rows:
        resolved = row.get("resolved_value")
        if resolved is None:
            continue
        try:
            resolved_value = float(resolved)
        except Exception:
            continue
        values.append((resolved_value - probability) ** 2)
    if not values:
        return None
    return sum(values) / len(values)


def filtered_cohort_benchmarks(payload: dict[str, Any], *, cohort_min_yes: float, cohort_max_yes: float, cohort_min_volume_usd: float) -> dict[str, Any]:
    metrics = payload.get("metrics") if isinstance(payload.get("metrics"), dict) else payload
    latest_rows = metrics.get("latest_rows") or []
    latest_metric = metrics.get("latest") or {}
    actual_brier = latest_metric.get("brier")
    midpoint = round((cohort_min_yes + cohort_max_yes) / 2.0, 4)
    avg_forecast_prob = latest_metric.get("avg_forecast_prob")
    latest_probs = []
    for row in latest_rows:
        try:
            latest_probs.append(float(row.get("forecast_prob")))
        except Exception:
            pass

    baseline_defs = [
        ("gate_floor", cohort_min_yes, False),
        ("gate_midpoint", midpoint, False),
        ("gate_ceiling", cohort_max_yes, False),
    ]
    if avg_forecast_prob is not None:
        baseline_defs.append(("latest_cohort_mean_forecast", float(avg_forecast_prob), True))
    if latest_probs:
        baseline_defs.append(("latest_cohort_median_forecast", float(statistics.median(latest_probs)), True))

    baselines = []
    for label, probability, ex_post in baseline_defs:
        brier = mean_brier(latest_rows, probability)
        baselines.append({
            "label": label,
            "probability": round(float(probability), 6),
            "brier": brier,
            "pipeline_advantage_vs_baseline": None if brier is None or actual_brier is None else round(float(brier) - float(actual_brier), 10),
            "ex_post_descriptive": ex_post,
        })

    return {
        "filtered_cohort_latest": {
            "assumed_gate": {
                "min_volume_usd": cohort_min_volume_usd,
                "yes_probability_min": cohort_min_yes,
                "yes_probability_max": cohort_max_yes,
                "yes_probability_midpoint": midpoint,
            },
            "latest_sample_n": latest_metric.get("n"),
            "actual_latest_brier": actual_brier,
            "latest_avg_forecast_prob": avg_forecast_prob,
            "latest_avg_resolved_value": latest_metric.get("avg_resolved_value"),
            "baselines": baselines,
            "notes": [
                "gate_floor/midpoint/ceiling are simple constant-probability baselines tied to the assumed filtered cohort.",
                "latest_cohort_mean_forecast and latest_cohort_median_forecast are descriptive ex-post baselines for sanity checking, not pure ex-ante trading baselines.",
                "Positive pipeline_advantage_vs_baseline means the pipeline beat that baseline on Brier; negative means the baseline was better."
            ],
        }
    }


def main() -> int:
    args = parse_args()
    payload = exec_sql(
        args.psql,
        args.db_url,
        SQL,
        {
            "platform": args.platform,
            "contract_id": args.contract_id,
            "market_id": args.market_id,
            "since_ts": args.since_ts,
            "until_ts": args.until_ts,
        },
    )
    payload["benchmarks"] = filtered_cohort_benchmarks(
        payload,
        cohort_min_yes=args.cohort_min_yes,
        cohort_max_yes=args.cohort_max_yes,
        cohort_min_volume_usd=args.cohort_min_volume_usd,
    )
    print(json.dumps(payload, indent=2 if args.pretty else None, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
