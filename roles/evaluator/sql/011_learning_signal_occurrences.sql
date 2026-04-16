BEGIN;

CREATE TABLE IF NOT EXISTS public.learning_signal_occurrences (
  id bigserial PRIMARY KEY,
  review_path text NOT NULL,
  packet_path text,
  case_key text NOT NULL,
  signal_kind text NOT NULL,
  signal_key text NOT NULL,
  signal_label text,
  direction text,
  confidence numeric(8,5),
  evidence_excerpt text,
  supporting_paths jsonb NOT NULL DEFAULT '[]'::jsonb,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (review_path, signal_kind, signal_key, evidence_excerpt)
);

CREATE INDEX IF NOT EXISTS idx_learning_signal_occurrences_case_key
  ON public.learning_signal_occurrences (case_key);

CREATE INDEX IF NOT EXISTS idx_learning_signal_occurrences_kind
  ON public.learning_signal_occurrences (signal_kind);

CREATE INDEX IF NOT EXISTS idx_learning_signal_occurrences_review_path
  ON public.learning_signal_occurrences (review_path);

GRANT SELECT, INSERT, UPDATE ON public.learning_signal_occurrences TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.learning_signal_occurrences TO pq_orchestrator;
GRANT SELECT ON public.learning_signal_occurrences TO pq_decision;
GRANT USAGE, SELECT ON SEQUENCE public.learning_signal_occurrences_id_seq TO pq_evaluator;
GRANT USAGE, SELECT ON SEQUENCE public.learning_signal_occurrences_id_seq TO pq_orchestrator;

COMMIT;
