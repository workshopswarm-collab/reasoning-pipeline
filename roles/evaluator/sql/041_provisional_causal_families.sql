BEGIN;

CREATE TABLE IF NOT EXISTS public.provisional_causal_families (
  family_key text PRIMARY KEY,
  family_label text NOT NULL DEFAULT '',
  source_family_slug text,
  family_state text NOT NULL DEFAULT 'provisional',
  source_lane text NOT NULL DEFAULT 'public.proposed_driver_occurrences',
  seed_candidate_count integer NOT NULL DEFAULT 0 CHECK (seed_candidate_count >= 0),
  distinct_case_count integer NOT NULL DEFAULT 0 CHECK (distinct_case_count >= 0),
  distinct_persona_count integer NOT NULL DEFAULT 0 CHECK (distinct_persona_count >= 0),
  evidence_mass numeric NOT NULL DEFAULT 0,
  lineage_parent_family_key text,
  family_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  compiler_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT NOW(),
  updated_at timestamptz NOT NULL DEFAULT NOW(),
  last_reinforced_at timestamptz NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_provisional_causal_families_state
  ON public.provisional_causal_families (family_state);

GRANT SELECT, INSERT, UPDATE ON public.provisional_causal_families TO pq_evaluator;
GRANT SELECT ON public.provisional_causal_families TO pq_orchestrator;
GRANT SELECT ON public.provisional_causal_families TO pq_decision;

COMMIT;
