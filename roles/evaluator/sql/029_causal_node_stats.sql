BEGIN;

CREATE TABLE IF NOT EXISTS public.causal_node_stats (
  node_key text PRIMARY KEY REFERENCES public.causal_nodes(node_key) ON DELETE CASCADE,
  mechanism_family text NOT NULL DEFAULT 'unassigned',
  lifecycle_stage text NOT NULL DEFAULT 'draft',
  projected_case_count int NOT NULL DEFAULT 0,
  matched_case_count int NOT NULL DEFAULT 0,
  exposure_count int NOT NULL DEFAULT 0,
  injection_count int NOT NULL DEFAULT 0,
  helpful_case_count int NOT NULL DEFAULT 0,
  supporting_case_count int NOT NULL DEFAULT 0,
  contested_case_count int NOT NULL DEFAULT 0,
  raw_uplift numeric,
  shrunken_uplift numeric,
  learned_weight numeric NOT NULL DEFAULT 0,
  decay_score numeric NOT NULL DEFAULT 0,
  status text NOT NULL,
  status_reason text,
  stats_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_causal_node_stats_status
  ON public.causal_node_stats (status);

CREATE INDEX IF NOT EXISTS idx_causal_node_stats_mechanism_family
  ON public.causal_node_stats (mechanism_family);

CREATE INDEX IF NOT EXISTS idx_causal_node_stats_lifecycle_stage
  ON public.causal_node_stats (lifecycle_stage);

GRANT SELECT, INSERT, UPDATE ON public.causal_node_stats TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.causal_node_stats TO pq_orchestrator;
GRANT SELECT ON public.causal_node_stats TO pq_decision;

COMMIT;
