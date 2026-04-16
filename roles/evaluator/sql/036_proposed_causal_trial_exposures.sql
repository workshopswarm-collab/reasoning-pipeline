BEGIN;

CREATE TABLE IF NOT EXISTS public.proposed_causal_trial_exposures (
  id bigserial PRIMARY KEY,
  proposal_id text NOT NULL,
  proposal_key text NOT NULL,
  candidate_type text NOT NULL,
  mechanism_family text NOT NULL DEFAULT 'unassigned',
  case_key text NOT NULL,
  dispatch_id text,
  research_run_id text,
  experiment_id text,
  experiment_arm text,
  trial_rank int,
  shadow_trial_score numeric,
  family_trial_rank int,
  overlay_score numeric,
  preview_only boolean NOT NULL DEFAULT true,
  injected boolean NOT NULL DEFAULT false,
  overlay_mode text NOT NULL DEFAULT 'preview_only',
  matched_active_nodes jsonb NOT NULL DEFAULT '[]'::jsonb,
  matched_candidate_edges jsonb NOT NULL DEFAULT '[]'::jsonb,
  matched_required_checks jsonb NOT NULL DEFAULT '[]'::jsonb,
  notes jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_trial_exposures_proposal_id
  ON public.proposed_causal_trial_exposures (proposal_id);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_trial_exposures_case_key
  ON public.proposed_causal_trial_exposures (case_key);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_trial_exposures_dispatch_id
  ON public.proposed_causal_trial_exposures (dispatch_id);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_trial_exposures_experiment_id
  ON public.proposed_causal_trial_exposures (experiment_id);

GRANT SELECT, INSERT, UPDATE ON public.proposed_causal_trial_exposures TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.proposed_causal_trial_exposures TO pq_orchestrator;
GRANT SELECT ON public.proposed_causal_trial_exposures TO pq_decision;
GRANT USAGE, SELECT ON SEQUENCE public.proposed_causal_trial_exposures_id_seq TO pq_evaluator;
GRANT USAGE, SELECT ON SEQUENCE public.proposed_causal_trial_exposures_id_seq TO pq_orchestrator;

COMMIT;
