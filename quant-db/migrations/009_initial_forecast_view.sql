BEGIN;

CREATE OR REPLACE VIEW public.initial_forecast_decisions AS
SELECT DISTINCT ON (fdr.market_id, fdr.contract_id)
  fdr.*
FROM public.forecast_decisions_with_resolution fdr
ORDER BY
  fdr.market_id,
  fdr.contract_id,
  fdr.decision_ts ASC,
  fdr.created_at ASC,
  fdr.forecast_id ASC;

GRANT SELECT ON public.initial_forecast_decisions TO pq_orchestrator;
GRANT SELECT ON public.initial_forecast_decisions TO pq_decision;
GRANT SELECT ON public.initial_forecast_decisions TO pq_deviceb_exec;
GRANT SELECT ON public.initial_forecast_decisions TO pq_evaluator;

COMMIT;
