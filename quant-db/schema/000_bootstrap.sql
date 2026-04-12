-- Reference bootstrap schema snapshot for the minimal predquant database.
-- Apply ordered migrations from quant-db/migrations/ for live setup.

-- See:
--   quant-db/scripts/bootstrap_local.sh
--   quant-db/scripts/apply.sh

CREATE TABLE public.forecast_decisions (
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

CREATE INDEX idx_forecast_decisions_market_id
    ON public.forecast_decisions (market_id);

CREATE INDEX idx_forecast_decisions_market_contract
    ON public.forecast_decisions (market_id, contract_id);

CREATE INDEX idx_forecast_decisions_case_id
    ON public.forecast_decisions (case_id);

CREATE INDEX idx_forecast_decisions_decision_ts
    ON public.forecast_decisions (decision_ts);

CREATE INDEX idx_forecast_decisions_status
    ON public.forecast_decisions (decision_status);

CREATE INDEX idx_forecast_decisions_market_contract_ts
    ON public.forecast_decisions (market_id, contract_id, decision_ts DESC);

CREATE TABLE public.market_resolutions (
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

CREATE INDEX idx_market_resolutions_status
    ON public.market_resolutions (resolution_status);

CREATE INDEX idx_market_resolutions_resolved_ts
    ON public.market_resolutions (resolved_ts);

GRANT SELECT, INSERT, UPDATE ON public.forecast_decisions TO pq_orchestrator;
GRANT SELECT, INSERT, UPDATE ON public.forecast_decisions TO pq_decision;
GRANT SELECT, INSERT, UPDATE ON public.market_resolutions TO pq_orchestrator;
GRANT SELECT, INSERT, UPDATE ON public.market_resolutions TO pq_decision;
GRANT SELECT, UPDATE ON public.markets TO pq_decision;

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

GRANT SELECT ON public.forecast_decisions_with_resolution TO pq_orchestrator;
GRANT SELECT ON public.forecast_decisions_with_resolution TO pq_decision;
GRANT SELECT ON public.forecast_decisions_with_resolution TO pq_deviceb_exec;
GRANT SELECT ON public.forecast_decisions_with_resolution TO pq_evaluator;

GRANT SELECT ON public.latest_forecast_decisions TO pq_orchestrator;
GRANT SELECT ON public.latest_forecast_decisions TO pq_decision;
GRANT SELECT ON public.latest_forecast_decisions TO pq_deviceb_exec;
GRANT SELECT ON public.latest_forecast_decisions TO pq_evaluator;

GRANT SELECT ON public.initial_forecast_decisions TO pq_orchestrator;
GRANT SELECT ON public.initial_forecast_decisions TO pq_decision;
GRANT SELECT ON public.initial_forecast_decisions TO pq_deviceb_exec;
GRANT SELECT ON public.initial_forecast_decisions TO pq_evaluator;
