BEGIN;

CREATE TABLE IF NOT EXISTS public.learning_interventions (
  intervention_key text PRIMARY KEY,
  path text NOT NULL UNIQUE,
  intervention_label text NOT NULL,
  status text NOT NULL,
  application_surface text NOT NULL,
  change_kind text NOT NULL,
  target_selector jsonb NOT NULL DEFAULT '{}'::jsonb,
  change_payload jsonb NOT NULL DEFAULT '{}'::jsonb,
  hypothesis text,
  evidence_paths jsonb NOT NULL DEFAULT '[]'::jsonb,
  metric_definition jsonb NOT NULL DEFAULT '{}'::jsonb,
  retrieval_tags jsonb NOT NULL DEFAULT '[]'::jsonb,
  note_frontmatter jsonb NOT NULL DEFAULT '{}'::jsonb,
  activated_at timestamptz,
  ended_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_learning_interventions_status
  ON public.learning_interventions (status);

CREATE INDEX IF NOT EXISTS idx_learning_interventions_surface
  ON public.learning_interventions (application_surface);

CREATE INDEX IF NOT EXISTS idx_learning_interventions_change_kind
  ON public.learning_interventions (change_kind);

GRANT SELECT, INSERT, UPDATE ON public.learning_interventions TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.learning_interventions TO pq_orchestrator;
GRANT SELECT ON public.learning_interventions TO pq_decision;

COMMIT;
