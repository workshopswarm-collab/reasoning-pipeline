-- Ensure exact-once / idempotent logging keys exist for runtime learning surfaces.

CREATE UNIQUE INDEX IF NOT EXISTS idx_proposed_causal_shadow_matches_dispatch_proposal_candidate
  ON public.proposed_causal_shadow_matches (dispatch_id, proposal_id, candidate_type)
  WHERE NULLIF(dispatch_id, '') IS NOT NULL;

CREATE UNIQUE INDEX IF NOT EXISTS idx_proposed_causal_trial_exposures_dispatch_proposal_candidate
  ON public.proposed_causal_trial_exposures (dispatch_id, proposal_id, candidate_type)
  WHERE NULLIF(dispatch_id, '') IS NOT NULL;

CREATE UNIQUE INDEX IF NOT EXISTS idx_learning_intervention_applications_run_key_surface
  ON public.learning_intervention_applications (intervention_key, research_run_id, application_surface)
  WHERE NULLIF(research_run_id, '') IS NOT NULL;
