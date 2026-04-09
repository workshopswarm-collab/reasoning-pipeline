BEGIN;

CREATE TABLE IF NOT EXISTS public.proposed_driver_occurrences (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  occurred_at timestamptz NOT NULL DEFAULT now(),

  case_id uuid,
  case_key text NOT NULL,
  market_id uuid,
  dispatch_id text,
  research_run_id uuid,

  persona text,
  artifact_kind text NOT NULL,
  artifact_path text NOT NULL,

  proposed_driver_label text NOT NULL,
  proposed_driver_slug text NOT NULL,

  canonical_driver_suggestions jsonb NOT NULL DEFAULT '[]'::jsonb,
  related_entities jsonb NOT NULL DEFAULT '[]'::jsonb,
  related_canonical_drivers jsonb NOT NULL DEFAULT '[]'::jsonb,

  difficulty_class text,
  source_of_truth_class text,

  status text NOT NULL DEFAULT 'active',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_proposed_driver_occurrence_artifact_slug
  ON public.proposed_driver_occurrences (artifact_path, proposed_driver_slug);

CREATE INDEX IF NOT EXISTS idx_proposed_driver_occurrences_slug
  ON public.proposed_driver_occurrences (proposed_driver_slug);

CREATE INDEX IF NOT EXISTS idx_proposed_driver_occurrences_case_key
  ON public.proposed_driver_occurrences (case_key);

CREATE INDEX IF NOT EXISTS idx_proposed_driver_occurrences_dispatch_id
  ON public.proposed_driver_occurrences (dispatch_id);

CREATE INDEX IF NOT EXISTS idx_proposed_driver_occurrences_occurred_at
  ON public.proposed_driver_occurrences (occurred_at);

GRANT SELECT, INSERT, UPDATE ON public.proposed_driver_occurrences TO pq_orchestrator;

COMMIT;
