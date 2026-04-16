BEGIN;

CREATE TABLE IF NOT EXISTS public.proposed_causal_shadow_matches (
  id bigserial PRIMARY KEY,
  proposal_id text NOT NULL,
  proposal_key text NOT NULL,
  candidate_type text NOT NULL,
  case_key text NOT NULL,
  dispatch_id text,
  research_run_id text,
  experiment_id text,
  rank_position int,
  retrieval_score numeric,
  would_inject boolean NOT NULL DEFAULT false,
  matched_active_nodes jsonb NOT NULL DEFAULT '[]'::jsonb,
  matched_candidate_edges jsonb NOT NULL DEFAULT '[]'::jsonb,
  matched_required_checks jsonb NOT NULL DEFAULT '[]'::jsonb,
  notes jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_shadow_matches_proposal_id
  ON public.proposed_causal_shadow_matches (proposal_id);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_shadow_matches_case_key
  ON public.proposed_causal_shadow_matches (case_key);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_shadow_matches_experiment_id
  ON public.proposed_causal_shadow_matches (experiment_id);

GRANT SELECT, INSERT, UPDATE ON public.proposed_causal_shadow_matches TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.proposed_causal_shadow_matches TO pq_orchestrator;
GRANT SELECT ON public.proposed_causal_shadow_matches TO pq_decision;
GRANT USAGE, SELECT ON SEQUENCE public.proposed_causal_shadow_matches_id_seq TO pq_evaluator;
GRANT USAGE, SELECT ON SEQUENCE public.proposed_causal_shadow_matches_id_seq TO pq_orchestrator;

COMMIT;
