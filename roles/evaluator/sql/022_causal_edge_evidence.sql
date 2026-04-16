BEGIN;

CREATE TABLE IF NOT EXISTS public.causal_edge_evidence (
  id bigserial PRIMARY KEY,
  edge_key text NOT NULL REFERENCES public.causal_edges(edge_key) ON DELETE CASCADE,
  case_key text,
  review_path text,
  signal_kind text,
  signal_key text,
  evidence_path text,
  support_direction text NOT NULL,
  confidence numeric,
  notes jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_causal_edge_evidence_edge_key
  ON public.causal_edge_evidence (edge_key);

CREATE INDEX IF NOT EXISTS idx_causal_edge_evidence_case_key
  ON public.causal_edge_evidence (case_key);

CREATE INDEX IF NOT EXISTS idx_causal_edge_evidence_support_direction
  ON public.causal_edge_evidence (support_direction);

GRANT SELECT, INSERT, UPDATE, DELETE ON public.causal_edge_evidence TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.causal_edge_evidence TO pq_orchestrator;
GRANT SELECT ON public.causal_edge_evidence TO pq_decision;
GRANT USAGE, SELECT ON SEQUENCE public.causal_edge_evidence_id_seq TO pq_evaluator;
GRANT USAGE, SELECT ON SEQUENCE public.causal_edge_evidence_id_seq TO pq_orchestrator;

COMMIT;
