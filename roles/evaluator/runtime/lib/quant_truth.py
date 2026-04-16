from __future__ import annotations

from typing import Any

from .db import DEFAULT_PSQL, exec_sql, resolve_db_url

SQL = r'''
WITH target_case AS (
  SELECT
    c.id::text AS case_db_id,
    c.case_key,
    c.status AS case_status,
    c.opened_at,
    c.closed_at,
    m.id::text AS market_id,
    m.platform,
    m.external_market_id,
    m.slug,
    m.title,
    m.description,
    m.category,
    m.status AS market_status,
    m.outcome_type,
    m.current_price,
    m.last_reasoned_price,
    m.closes_at,
    m.resolves_at,
    m.updated_at AS market_updated_at
  FROM public.cases c
  JOIN public.markets m ON m.id = c.market_id
  WHERE c.case_key = :'case_key'
  ORDER BY c.opened_at DESC
  LIMIT 1
),
forecast_rows AS (
  SELECT
    fdr.forecast_id,
    fdr.case_id,
    fdr.dispatch_id,
    fdr.market_id,
    fdr.contract_id,
    fdr.forecast_platform,
    fdr.market_slug,
    fdr.question,
    fdr.forecast_prob,
    fdr.forecast_direction,
    fdr.confidence_label,
    fdr.confidence_score,
    fdr.time_horizon_label,
    fdr.verification_mode,
    fdr.decision_status,
    fdr.rationale_summary,
    fdr.decision_packet_path,
    fdr.decision_handoff_path,
    fdr.syndicated_finding_path,
    fdr.supersedes_forecast_id,
    fdr.decision_ts,
    fdr.created_at,
    fdr.updated_at,
    fdr.resolution_status,
    fdr.resolved_outcome,
    fdr.resolved_value,
    fdr.resolved_ts,
    fdr.resolution_source,
    fdr.resolution_notes,
    CASE
      WHEN fdr.resolved_value IS NULL THEN NULL
      ELSE POWER(fdr.forecast_prob - fdr.resolved_value, 2)
    END AS brier_component
  FROM public.forecast_decisions_with_resolution fdr
  JOIN target_case tc ON tc.market_id = fdr.market_id
  WHERE fdr.contract_id = COALESCE(NULLIF(:'contract_id', ''), 'yes')
),
initial_forecast AS (
  SELECT *
  FROM forecast_rows
  ORDER BY decision_ts ASC, created_at ASC, forecast_id ASC
  LIMIT 1
),
latest_forecast AS (
  SELECT *
  FROM forecast_rows
  ORDER BY decision_ts DESC, created_at DESC, forecast_id DESC
  LIMIT 1
),
snapshot_rows AS (
  SELECT
    observed_at,
    last_price,
    yes_price,
    no_price,
    best_bid,
    best_ask,
    volume,
    open_interest,
    COALESCE(yes_price, last_price) AS reference_price
  FROM public.market_snapshots ms
  JOIN target_case tc ON tc.market_id::uuid = ms.market_id
  ORDER BY observed_at DESC
  LIMIT 48
),
snapshot_summary AS (
  SELECT
    COUNT(*) AS snapshot_count,
    MIN(reference_price) AS min_reference_price,
    MAX(reference_price) AS max_reference_price,
    AVG(reference_price) AS avg_reference_price,
    MIN(observed_at) AS oldest_observed_at,
    MAX(observed_at) AS latest_observed_at
  FROM snapshot_rows
),
forecast_summary AS (
  SELECT
    COUNT(*) AS forecast_count,
    COUNT(*) FILTER (WHERE resolved_value IS NOT NULL) AS resolved_forecast_count,
    MIN(decision_ts) AS first_decision_ts,
    MAX(decision_ts) AS latest_decision_ts,
    AVG(forecast_prob) AS avg_forecast_prob
  FROM forecast_rows
)
SELECT json_build_object(
  'db_available', true,
  'case', (SELECT row_to_json(tc) FROM target_case tc),
  'initial_forecast', (SELECT row_to_json(x) FROM initial_forecast x),
  'latest_forecast', (SELECT row_to_json(x) FROM latest_forecast x),
  'forecast_summary', (SELECT row_to_json(x) FROM forecast_summary x),
  'forecast_rows', COALESCE((SELECT json_agg(row_to_json(fr) ORDER BY fr.decision_ts ASC, fr.created_at ASC, fr.forecast_id ASC) FROM forecast_rows fr), '[]'::json),
  'snapshot_summary', (SELECT row_to_json(ss) FROM snapshot_summary ss),
  'recent_snapshots', COALESCE((SELECT json_agg(row_to_json(sr) ORDER BY sr.observed_at DESC) FROM snapshot_rows sr), '[]'::json)
)::text;
'''


def load_case_quant_truth(
    case_key: str,
    *,
    contract_id: str = "yes",
    db_url: str | None = None,
    psql_bin: str = DEFAULT_PSQL,
) -> dict[str, Any]:
    resolved_db_url = resolve_db_url(db_url)
    payload = exec_sql(
        psql_bin,
        resolved_db_url,
        SQL,
        {
            "case_key": case_key,
            "contract_id": contract_id or "yes",
        },
    )
    if not isinstance(payload, dict):
        return {"db_available": True}
    payload.setdefault("db_available", True)
    return payload
