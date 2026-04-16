BEGIN;

CREATE TABLE IF NOT EXISTS public.lmd_experiment_assignments (
  id bigserial PRIMARY KEY,
  case_id uuid,
  case_key text NOT NULL,
  experiment_id text NOT NULL,
  arm text NOT NULL,
  generator_version text NOT NULL,
  policy_version text NOT NULL,
  assignment_unit text NOT NULL DEFAULT 'case_key',
  assignment_hash text NOT NULL,
  assignment_fraction numeric NOT NULL,
  treatment_ratio numeric NOT NULL DEFAULT 0.5,
  notes jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (case_key, experiment_id)
);

CREATE INDEX IF NOT EXISTS idx_lmd_experiment_assignments_case_key
  ON public.lmd_experiment_assignments (case_key);

CREATE INDEX IF NOT EXISTS idx_lmd_experiment_assignments_experiment_id
  ON public.lmd_experiment_assignments (experiment_id);

CREATE INDEX IF NOT EXISTS idx_lmd_experiment_assignments_arm
  ON public.lmd_experiment_assignments (arm);

GRANT SELECT, INSERT, UPDATE ON public.lmd_experiment_assignments TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.lmd_experiment_assignments TO pq_orchestrator;
GRANT SELECT ON public.lmd_experiment_assignments TO pq_decision;
GRANT USAGE, SELECT ON SEQUENCE public.lmd_experiment_assignments_id_seq TO pq_evaluator;
GRANT USAGE, SELECT ON SEQUENCE public.lmd_experiment_assignments_id_seq TO pq_orchestrator;

COMMIT;
