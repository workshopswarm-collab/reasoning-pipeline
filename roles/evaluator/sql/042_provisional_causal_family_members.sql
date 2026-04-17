BEGIN;

CREATE TABLE IF NOT EXISTS public.provisional_causal_family_members (
  family_key text NOT NULL,
  candidate_slug text NOT NULL,
  packet_key text,
  membership_score numeric NOT NULL DEFAULT 0,
  membership_role text NOT NULL DEFAULT 'seed',
  member_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT NOW(),
  updated_at timestamptz NOT NULL DEFAULT NOW(),
  PRIMARY KEY (family_key, candidate_slug)
);

CREATE INDEX IF NOT EXISTS idx_provisional_causal_family_members_packet_key
  ON public.provisional_causal_family_members (packet_key);

GRANT SELECT, INSERT, UPDATE ON public.provisional_causal_family_members TO pq_evaluator;
GRANT SELECT ON public.provisional_causal_family_members TO pq_orchestrator;
GRANT SELECT ON public.provisional_causal_family_members TO pq_decision;

COMMIT;
