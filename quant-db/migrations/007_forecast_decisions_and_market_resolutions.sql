BEGIN;

CREATE TABLE IF NOT EXISTS public.forecast_decisions (
  forecast_id text PRIMARY KEY,
  decision_ts timestamptz NOT NULL,
  case_id text,
  dispatch_id text,
  market_id text NOT NULL,
  contract_id text NOT NULL,
  platform text NOT NULL,
  market_slug text,
  question text NOT NULL,
  forecast_prob numeric(6,5) NOT NULL CHECK (forecast_prob >= 0 AND forecast_prob <= 1),
  forecast_direction text,
  confidence_label text,
  confidence_score numeric(6,5) CHECK (
    confidence_score IS NULL OR (confidence_score >= 0 AND confidence_score <= 1)
  ),
  time_horizon_label text,
  verification_mode text,
  decision_status text NOT NULL CHECK (
    decision_status IN ('recorded', 'superseded', 'resolved', 'void', 'error')
  ),
  rationale_summary text,
  decision_packet_path text NOT NULL,
  decision_handoff_path text,
  syndicated_finding_path text,
  supersedes_forecast_id text REFERENCES public.forecast_decisions(forecast_id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_forecast_decisions_market_id
  ON public.forecast_decisions (market_id);

CREATE INDEX IF NOT EXISTS idx_forecast_decisions_market_contract
  ON public.forecast_decisions (market_id, contract_id);

CREATE INDEX IF NOT EXISTS idx_forecast_decisions_case_id
  ON public.forecast_decisions (case_id);

CREATE INDEX IF NOT EXISTS idx_forecast_decisions_decision_ts
  ON public.forecast_decisions (decision_ts);

CREATE INDEX IF NOT EXISTS idx_forecast_decisions_status
  ON public.forecast_decisions (decision_status);

CREATE INDEX IF NOT EXISTS idx_forecast_decisions_market_contract_ts
  ON public.forecast_decisions (market_id, contract_id, decision_ts DESC);

CREATE TABLE IF NOT EXISTS public.market_resolutions (
  market_id text NOT NULL,
  contract_id text NOT NULL,
  platform text NOT NULL,
  resolution_status text NOT NULL CHECK (
    resolution_status IN ('unresolved', 'resolved', 'canceled', 'disputed', 'error')
  ),
  resolved_outcome text,
  resolved_value numeric(6,5) CHECK (
    resolved_value IS NULL OR (resolved_value >= 0 AND resolved_value <= 1)
  ),
  resolved_ts timestamptz,
  resolution_source text,
  resolution_notes text,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (market_id, contract_id)
);

CREATE INDEX IF NOT EXISTS idx_market_resolutions_status
  ON public.market_resolutions (resolution_status);

CREATE INDEX IF NOT EXISTS idx_market_resolutions_resolved_ts
  ON public.market_resolutions (resolved_ts);

GRANT SELECT, INSERT, UPDATE ON public.forecast_decisions TO pq_orchestrator;
GRANT SELECT, INSERT, UPDATE ON public.forecast_decisions TO pq_decision;
GRANT SELECT, INSERT, UPDATE ON public.market_resolutions TO pq_orchestrator;
GRANT SELECT, INSERT, UPDATE ON public.market_resolutions TO pq_decision;

COMMIT;
