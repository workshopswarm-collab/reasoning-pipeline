BEGIN;

ALTER TABLE public.causal_family_policies
  ADD COLUMN IF NOT EXISTS policy_source text NOT NULL DEFAULT 'file_bootstrap',
  ADD COLUMN IF NOT EXISTS policy_generated_at timestamptz,
  ADD COLUMN IF NOT EXISTS family_state text NOT NULL DEFAULT 'manual_seed',
  ADD COLUMN IF NOT EXISTS health_score numeric NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS evidence_mass numeric NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS quarantine_until timestamptz,
  ADD COLUMN IF NOT EXISTS decay_half_life_days integer NOT NULL DEFAULT 30,
  ADD COLUMN IF NOT EXISTS policy_notes jsonb NOT NULL DEFAULT '{}'::jsonb;

CREATE INDEX IF NOT EXISTS idx_causal_family_policies_policy_source
  ON public.causal_family_policies (policy_source);

GRANT SELECT, INSERT, UPDATE ON public.causal_family_policies TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.causal_family_policies TO pq_orchestrator;
GRANT SELECT ON public.causal_family_policies TO pq_decision;

COMMIT;
