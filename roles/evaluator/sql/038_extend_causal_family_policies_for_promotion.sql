BEGIN;

ALTER TABLE public.causal_family_policies
  ADD COLUMN IF NOT EXISTS max_promotion_ready_candidates integer NOT NULL DEFAULT 1,
  ADD COLUMN IF NOT EXISTS min_trial_judged_count_for_promotion integer NOT NULL DEFAULT 2,
  ADD COLUMN IF NOT EXISTS min_trial_helpful_count_for_promotion integer NOT NULL DEFAULT 1,
  ADD COLUMN IF NOT EXISTS min_trial_shrunken_utility_for_promotion numeric NOT NULL DEFAULT 0.25,
  ADD COLUMN IF NOT EXISTS max_trial_harmful_rate_for_promotion numeric NOT NULL DEFAULT 0.34,
  ADD COLUMN IF NOT EXISTS max_contest_case_count_for_promotion integer NOT NULL DEFAULT 1,
  ADD COLUMN IF NOT EXISTS max_genericity_for_promotion numeric NOT NULL DEFAULT 0.22;

GRANT SELECT, INSERT, UPDATE ON public.causal_family_policies TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.causal_family_policies TO pq_orchestrator;
GRANT SELECT ON public.causal_family_policies TO pq_decision;

COMMIT;
