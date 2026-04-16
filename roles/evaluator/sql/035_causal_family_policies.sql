BEGIN;

CREATE TABLE IF NOT EXISTS public.causal_family_policies (
  mechanism_family text PRIMARY KEY,
  description text NOT NULL DEFAULT '',
  enabled boolean NOT NULL DEFAULT true,
  max_shadow_candidates integer NOT NULL DEFAULT 6 CHECK (max_shadow_candidates >= 0),
  max_trial_candidates integer NOT NULL DEFAULT 2 CHECK (max_trial_candidates >= 0),
  max_active_nodes integer NOT NULL DEFAULT 6 CHECK (max_active_nodes >= 0),
  max_active_edges integer NOT NULL DEFAULT 4 CHECK (max_active_edges >= 0),
  min_shadow_judged_count_for_trial integer NOT NULL DEFAULT 4 CHECK (min_shadow_judged_count_for_trial >= 0),
  min_shadow_helpful_count_for_trial integer NOT NULL DEFAULT 1 CHECK (min_shadow_helpful_count_for_trial >= 0),
  min_shadow_mean_score_for_trial numeric NOT NULL DEFAULT 0.5,
  min_non_intervention_support_cases_for_trial integer NOT NULL DEFAULT 2 CHECK (min_non_intervention_support_cases_for_trial >= 0),
  max_genericity_for_trial numeric NOT NULL DEFAULT 0.25,
  max_duplicate_similarity_for_trial numeric NOT NULL DEFAULT 0.85,
  max_promotion_ready_candidates integer NOT NULL DEFAULT 1 CHECK (max_promotion_ready_candidates >= 0),
  min_trial_judged_count_for_promotion integer NOT NULL DEFAULT 2 CHECK (min_trial_judged_count_for_promotion >= 0),
  min_trial_helpful_count_for_promotion integer NOT NULL DEFAULT 1 CHECK (min_trial_helpful_count_for_promotion >= 0),
  min_trial_shrunken_utility_for_promotion numeric NOT NULL DEFAULT 0.25,
  max_trial_harmful_rate_for_promotion numeric NOT NULL DEFAULT 0.34,
  max_contest_case_count_for_promotion integer NOT NULL DEFAULT 1 CHECK (max_contest_case_count_for_promotion >= 0),
  max_genericity_for_promotion numeric NOT NULL DEFAULT 0.22,
  notes jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT NOW(),
  updated_at timestamptz NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_causal_family_policies_enabled
  ON public.causal_family_policies (enabled);

GRANT SELECT, INSERT, UPDATE ON public.causal_family_policies TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.causal_family_policies TO pq_orchestrator;
GRANT SELECT ON public.causal_family_policies TO pq_decision;

COMMIT;
