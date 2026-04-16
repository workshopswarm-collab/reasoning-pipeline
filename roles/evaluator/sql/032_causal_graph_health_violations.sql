BEGIN;

CREATE TABLE IF NOT EXISTS public.causal_graph_health_violations (
  id bigserial PRIMARY KEY,
  entity_type text NOT NULL,
  entity_key text NOT NULL,
  violation_kind text NOT NULL,
  severity text NOT NULL,
  status text NOT NULL DEFAULT 'open',
  details jsonb NOT NULL DEFAULT '{}'::jsonb,
  detected_at timestamptz NOT NULL DEFAULT now(),
  resolved_at timestamptz
);

CREATE INDEX IF NOT EXISTS idx_causal_graph_health_violations_status
  ON public.causal_graph_health_violations (status);

CREATE INDEX IF NOT EXISTS idx_causal_graph_health_violations_severity
  ON public.causal_graph_health_violations (severity);

CREATE INDEX IF NOT EXISTS idx_causal_graph_health_violations_entity
  ON public.causal_graph_health_violations (entity_type, entity_key);

CREATE INDEX IF NOT EXISTS idx_causal_graph_health_violations_violation_kind
  ON public.causal_graph_health_violations (violation_kind);

GRANT SELECT, INSERT, UPDATE ON public.causal_graph_health_violations TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.causal_graph_health_violations TO pq_orchestrator;
GRANT SELECT ON public.causal_graph_health_violations TO pq_decision;
GRANT USAGE, SELECT ON SEQUENCE public.causal_graph_health_violations_id_seq TO pq_evaluator;
GRANT USAGE, SELECT ON SEQUENCE public.causal_graph_health_violations_id_seq TO pq_orchestrator;

COMMIT;
