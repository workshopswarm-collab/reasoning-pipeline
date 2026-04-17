BEGIN;

CREATE TABLE IF NOT EXISTS public.causal_family_lifecycle_events (
  id bigserial PRIMARY KEY,
  family_key text NOT NULL,
  event_type text NOT NULL,
  from_state text,
  to_state text,
  event_source text NOT NULL DEFAULT 'system',
  notes jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_causal_family_lifecycle_events_family_created
  ON public.causal_family_lifecycle_events (family_key, created_at DESC);

GRANT SELECT, INSERT, UPDATE ON public.causal_family_lifecycle_events TO pq_evaluator;
GRANT SELECT ON public.causal_family_lifecycle_events TO pq_orchestrator;
GRANT SELECT ON public.causal_family_lifecycle_events TO pq_decision;

COMMIT;
