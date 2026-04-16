BEGIN;

CREATE TABLE IF NOT EXISTS public.lmd_bundle_exposures (
  id bigserial PRIMARY KEY,
  case_id uuid,
  case_key text NOT NULL,
  dispatch_id text NOT NULL,
  research_run_id text,
  experiment_id text,
  arm text,
  generator_version text,
  policy_version text,
  bundle_path text,
  bundle_sha256 text,
  candidate_id text NOT NULL,
  candidate_type text NOT NULL,
  candidate_path text,
  rank_position int,
  retrieval_score numeric,
  was_injected boolean NOT NULL DEFAULT true,
  required_check_keys jsonb NOT NULL DEFAULT '[]'::jsonb,
  token_cost_estimate numeric,
  notes jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (dispatch_id, candidate_id, candidate_type)
);

CREATE INDEX IF NOT EXISTS idx_lmd_bundle_exposures_case_key
  ON public.lmd_bundle_exposures (case_key);

CREATE INDEX IF NOT EXISTS idx_lmd_bundle_exposures_dispatch_id
  ON public.lmd_bundle_exposures (dispatch_id);

CREATE INDEX IF NOT EXISTS idx_lmd_bundle_exposures_research_run_id
  ON public.lmd_bundle_exposures (research_run_id);

CREATE INDEX IF NOT EXISTS idx_lmd_bundle_exposures_candidate_type
  ON public.lmd_bundle_exposures (candidate_type);

CREATE INDEX IF NOT EXISTS idx_lmd_bundle_exposures_experiment_id
  ON public.lmd_bundle_exposures (experiment_id);

GRANT SELECT, INSERT, UPDATE ON public.lmd_bundle_exposures TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.lmd_bundle_exposures TO pq_orchestrator;
GRANT SELECT ON public.lmd_bundle_exposures TO pq_decision;
GRANT USAGE, SELECT ON SEQUENCE public.lmd_bundle_exposures_id_seq TO pq_evaluator;
GRANT USAGE, SELECT ON SEQUENCE public.lmd_bundle_exposures_id_seq TO pq_orchestrator;

COMMIT;
