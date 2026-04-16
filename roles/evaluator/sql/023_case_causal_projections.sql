BEGIN;

CREATE TABLE IF NOT EXISTS public.case_causal_projections (
  case_key text PRIMARY KEY,
  case_id uuid,
  review_path text NOT NULL,
  projection_path text NOT NULL UNIQUE,
  active_nodes jsonb NOT NULL DEFAULT '[]'::jsonb,
  candidate_edges jsonb NOT NULL DEFAULT '[]'::jsonb,
  contested_edges jsonb NOT NULL DEFAULT '[]'::jsonb,
  required_checks jsonb NOT NULL DEFAULT '[]'::jsonb,
  projection_version text NOT NULL,
  projection_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_case_causal_projections_case_id
  ON public.case_causal_projections (case_id);

CREATE INDEX IF NOT EXISTS idx_case_causal_projections_projection_version
  ON public.case_causal_projections (projection_version);

GRANT SELECT, INSERT, UPDATE ON public.case_causal_projections TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.case_causal_projections TO pq_orchestrator;
GRANT SELECT ON public.case_causal_projections TO pq_decision;

COMMIT;
