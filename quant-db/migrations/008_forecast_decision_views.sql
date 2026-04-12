BEGIN;

CREATE OR REPLACE VIEW public.forecast_decisions_with_resolution AS
SELECT
  fd.forecast_id,
  fd.decision_ts,
  fd.case_id,
  fd.dispatch_id,
  fd.market_id,
  fd.contract_id,
  fd.platform AS forecast_platform,
  fd.market_slug,
  fd.question,
  fd.forecast_prob,
  fd.forecast_direction,
  fd.confidence_label,
  fd.confidence_score,
  fd.time_horizon_label,
  fd.verification_mode,
  fd.decision_status,
  fd.rationale_summary,
  fd.decision_packet_path,
  fd.decision_handoff_path,
  fd.syndicated_finding_path,
  fd.supersedes_forecast_id,
  fd.created_at,
  fd.updated_at,
  mr.platform AS resolution_platform,
  mr.resolution_status,
  mr.resolved_outcome,
  mr.resolved_value,
  mr.resolved_ts,
  mr.resolution_source,
  mr.resolution_notes
FROM public.forecast_decisions fd
LEFT JOIN public.market_resolutions mr
  ON fd.market_id = mr.market_id
 AND fd.contract_id = mr.contract_id;

CREATE OR REPLACE VIEW public.latest_forecast_decisions AS
SELECT DISTINCT ON (fdr.market_id, fdr.contract_id)
  fdr.*
FROM public.forecast_decisions_with_resolution fdr
ORDER BY
  fdr.market_id,
  fdr.contract_id,
  fdr.decision_ts DESC,
  fdr.created_at DESC,
  fdr.forecast_id DESC;

GRANT SELECT ON public.forecast_decisions_with_resolution TO pq_orchestrator;
GRANT SELECT ON public.forecast_decisions_with_resolution TO pq_decision;
GRANT SELECT ON public.forecast_decisions_with_resolution TO pq_deviceb_exec;
GRANT SELECT ON public.forecast_decisions_with_resolution TO pq_evaluator;

GRANT SELECT ON public.latest_forecast_decisions TO pq_orchestrator;
GRANT SELECT ON public.latest_forecast_decisions TO pq_decision;
GRANT SELECT ON public.latest_forecast_decisions TO pq_deviceb_exec;
GRANT SELECT ON public.latest_forecast_decisions TO pq_evaluator;

COMMIT;
