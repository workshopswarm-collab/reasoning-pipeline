BEGIN;

ALTER TABLE public.proposed_causal_trial_exposures
  ADD COLUMN IF NOT EXISTS outcome_label text,
  ADD COLUMN IF NOT EXISTS outcome_score numeric,
  ADD COLUMN IF NOT EXISTS outcome_favored boolean,
  ADD COLUMN IF NOT EXISTS judged_at timestamptz,
  ADD COLUMN IF NOT EXISTS judge_version text,
  ADD COLUMN IF NOT EXISTS outcome_metadata jsonb NOT NULL DEFAULT '{}'::jsonb;

CREATE INDEX IF NOT EXISTS idx_proposed_causal_trial_exposures_outcome_label
  ON public.proposed_causal_trial_exposures (outcome_label);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_trial_exposures_judged_at
  ON public.proposed_causal_trial_exposures (judged_at);

GRANT SELECT, INSERT, UPDATE ON public.proposed_causal_trial_exposures TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.proposed_causal_trial_exposures TO pq_orchestrator;
GRANT SELECT ON public.proposed_causal_trial_exposures TO pq_decision;

COMMIT;
