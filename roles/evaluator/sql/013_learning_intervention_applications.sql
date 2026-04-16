BEGIN;

CREATE TABLE IF NOT EXISTS public.learning_intervention_applications (
  id bigserial PRIMARY KEY,
  intervention_key text NOT NULL REFERENCES public.learning_interventions(intervention_key) ON DELETE CASCADE,
  case_id uuid,
  case_key text NOT NULL,
  research_run_id text,
  application_surface text NOT NULL,
  bundle_path text,
  dispatch_id text,
  notes jsonb NOT NULL DEFAULT '{}'::jsonb,
  applied_at timestamptz NOT NULL DEFAULT now(),
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (intervention_key, research_run_id, application_surface)
);

CREATE INDEX IF NOT EXISTS idx_learning_intervention_applications_case_key
  ON public.learning_intervention_applications (case_key);

CREATE INDEX IF NOT EXISTS idx_learning_intervention_applications_intervention_key
  ON public.learning_intervention_applications (intervention_key);

CREATE INDEX IF NOT EXISTS idx_learning_intervention_applications_surface
  ON public.learning_intervention_applications (application_surface);

CREATE INDEX IF NOT EXISTS idx_learning_intervention_applications_research_run_id
  ON public.learning_intervention_applications (research_run_id);

CREATE INDEX IF NOT EXISTS idx_learning_intervention_applications_applied_at
  ON public.learning_intervention_applications (applied_at);

GRANT SELECT, INSERT, UPDATE ON public.learning_intervention_applications TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.learning_intervention_applications TO pq_orchestrator;
GRANT SELECT ON public.learning_intervention_applications TO pq_decision;
GRANT USAGE, SELECT ON SEQUENCE public.learning_intervention_applications_id_seq TO pq_evaluator;
GRANT USAGE, SELECT ON SEQUENCE public.learning_intervention_applications_id_seq TO pq_orchestrator;

COMMIT;
