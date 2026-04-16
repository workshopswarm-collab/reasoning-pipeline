BEGIN;

CREATE TABLE IF NOT EXISTS public.causal_graph_lifecycle_events (
  id bigserial PRIMARY KEY,
  entity_type text NOT NULL,
  entity_key text NOT NULL,
  previous_stage text,
  new_stage text NOT NULL,
  event_kind text NOT NULL,
  reason text,
  related_entity_key text,
  event_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_causal_graph_lifecycle_events_entity
  ON public.causal_graph_lifecycle_events (entity_type, entity_key);

CREATE INDEX IF NOT EXISTS idx_causal_graph_lifecycle_events_new_stage
  ON public.causal_graph_lifecycle_events (new_stage);

CREATE INDEX IF NOT EXISTS idx_causal_graph_lifecycle_events_event_kind
  ON public.causal_graph_lifecycle_events (event_kind);

CREATE INDEX IF NOT EXISTS idx_causal_graph_lifecycle_events_created_at
  ON public.causal_graph_lifecycle_events (created_at DESC);

GRANT SELECT, INSERT, UPDATE ON public.causal_graph_lifecycle_events TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.causal_graph_lifecycle_events TO pq_orchestrator;
GRANT SELECT ON public.causal_graph_lifecycle_events TO pq_decision;
GRANT USAGE, SELECT ON SEQUENCE public.causal_graph_lifecycle_events_id_seq TO pq_evaluator;
GRANT USAGE, SELECT ON SEQUENCE public.causal_graph_lifecycle_events_id_seq TO pq_orchestrator;

COMMIT;
