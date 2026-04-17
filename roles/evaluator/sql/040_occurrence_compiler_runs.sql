BEGIN;

CREATE TABLE IF NOT EXISTS public.occurrence_compiler_runs (
  run_id text PRIMARY KEY,
  compiler_version text NOT NULL DEFAULT '',
  source_root text NOT NULL DEFAULT 'public.proposed_driver_occurrences',
  packet_root text NOT NULL DEFAULT '',
  status text NOT NULL DEFAULT 'completed',
  source_occurrence_count integer NOT NULL DEFAULT 0 CHECK (source_occurrence_count >= 0),
  grouped_candidate_count integer NOT NULL DEFAULT 0 CHECK (grouped_candidate_count >= 0),
  compiled_packet_count integer NOT NULL DEFAULT 0 CHECK (compiled_packet_count >= 0),
  rejected_count integer NOT NULL DEFAULT 0 CHECK (rejected_count >= 0),
  error_count integer NOT NULL DEFAULT 0 CHECK (error_count >= 0),
  summary jsonb NOT NULL DEFAULT '{}'::jsonb,
  started_at timestamptz NOT NULL DEFAULT NOW(),
  completed_at timestamptz NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_occurrence_compiler_runs_completed_at
  ON public.occurrence_compiler_runs (completed_at DESC);

GRANT SELECT, INSERT, UPDATE ON public.occurrence_compiler_runs TO pq_evaluator;
GRANT SELECT ON public.occurrence_compiler_runs TO pq_orchestrator;
GRANT SELECT ON public.occurrence_compiler_runs TO pq_decision;

COMMIT;
