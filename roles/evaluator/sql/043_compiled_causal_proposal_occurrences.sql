BEGIN;

CREATE TABLE IF NOT EXISTS public.compiled_causal_proposal_occurrences (
  packet_key text PRIMARY KEY,
  proposal_key text NOT NULL,
  candidate_slug text NOT NULL,
  candidate_label text NOT NULL DEFAULT '',
  normalized_family text NOT NULL DEFAULT 'unassigned',
  proposal_source text NOT NULL DEFAULT 'driver_occurrence_compiler',
  candidate_type text NOT NULL DEFAULT 'packet',
  packet_path text NOT NULL DEFAULT '',
  packet_hash text NOT NULL DEFAULT '',
  compiler_run_id text NOT NULL DEFAULT '',
  source_occurrence_count integer NOT NULL DEFAULT 0 CHECK (source_occurrence_count >= 0),
  distinct_case_count integer NOT NULL DEFAULT 0 CHECK (distinct_case_count >= 0),
  distinct_persona_count integer NOT NULL DEFAULT 0 CHECK (distinct_persona_count >= 0),
  source_mix jsonb NOT NULL DEFAULT '{}'::jsonb,
  compiler_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT NOW(),
  updated_at timestamptz NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_compiled_causal_proposal_occurrences_family
  ON public.compiled_causal_proposal_occurrences (normalized_family);

CREATE INDEX IF NOT EXISTS idx_compiled_causal_proposal_occurrences_run
  ON public.compiled_causal_proposal_occurrences (compiler_run_id, updated_at DESC);

GRANT SELECT, INSERT, UPDATE ON public.compiled_causal_proposal_occurrences TO pq_evaluator;
GRANT SELECT ON public.compiled_causal_proposal_occurrences TO pq_orchestrator;
GRANT SELECT ON public.compiled_causal_proposal_occurrences TO pq_decision;

COMMIT;
