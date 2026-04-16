BEGIN;

CREATE TABLE IF NOT EXISTS public.lmd_candidate_stats (
  candidate_id text PRIMARY KEY,
  candidate_type text NOT NULL,
  n_exposed int NOT NULL DEFAULT 0,
  distinct_case_count int NOT NULL DEFAULT 0,
  treatment_case_count int NOT NULL DEFAULT 0,
  control_case_count int NOT NULL DEFAULT 0,
  treatment_mean_brier numeric,
  control_mean_brier numeric,
  raw_uplift numeric,
  shrunken_uplift numeric,
  cost_adjusted_uplift numeric,
  genericity_penalty numeric NOT NULL DEFAULT 0,
  learned_weight numeric NOT NULL DEFAULT 0,
  status text NOT NULL,
  status_reason text,
  stats_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_lmd_candidate_stats_candidate_type
  ON public.lmd_candidate_stats (candidate_type);

CREATE INDEX IF NOT EXISTS idx_lmd_candidate_stats_status
  ON public.lmd_candidate_stats (status);

GRANT SELECT, INSERT, UPDATE ON public.lmd_candidate_stats TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.lmd_candidate_stats TO pq_orchestrator;
GRANT SELECT ON public.lmd_candidate_stats TO pq_decision;

COMMIT;
