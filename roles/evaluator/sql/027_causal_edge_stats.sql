BEGIN;

CREATE TABLE IF NOT EXISTS public.causal_edge_stats (
  edge_key text PRIMARY KEY REFERENCES public.causal_edges(edge_key) ON DELETE CASCADE,
  exposure_count int NOT NULL DEFAULT 0,
  projected_case_count int NOT NULL DEFAULT 0,
  supporting_case_count int NOT NULL DEFAULT 0,
  contested_case_count int NOT NULL DEFAULT 0,
  treatment_case_count int NOT NULL DEFAULT 0,
  control_case_count int NOT NULL DEFAULT 0,
  treatment_mean_brier numeric,
  control_mean_brier numeric,
  raw_uplift numeric,
  shrunken_uplift numeric,
  genericity_penalty numeric NOT NULL DEFAULT 0,
  learned_weight numeric NOT NULL DEFAULT 0,
  status text NOT NULL,
  status_reason text,
  stats_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_causal_edge_stats_status
  ON public.causal_edge_stats (status);

GRANT SELECT, INSERT, UPDATE ON public.causal_edge_stats TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.causal_edge_stats TO pq_orchestrator;
GRANT SELECT ON public.causal_edge_stats TO pq_decision;

COMMIT;
