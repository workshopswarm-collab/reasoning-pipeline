BEGIN;

CREATE TABLE IF NOT EXISTS public.proposed_causal_candidate_occurrences (
  id bigserial PRIMARY KEY,
  proposal_id text NOT NULL,
  proposal_key text NOT NULL,
  candidate_type text NOT NULL,
  candidate_label text NOT NULL,
  mechanism_family text NOT NULL DEFAULT 'unassigned',
  proposal_source text NOT NULL DEFAULT 'rule_projection',
  case_key text NOT NULL,
  review_path text NOT NULL,
  projection_path text NOT NULL,
  source_node_key text,
  target_node_key text,
  node_type text,
  effect_sign text,
  support_direction text NOT NULL DEFAULT 'supports',
  occurrence_reason text,
  evidence_excerpt text,
  genericity_penalty numeric NOT NULL DEFAULT 0,
  evidence_channels jsonb NOT NULL DEFAULT '[]'::jsonb,
  intervention_dependency text NOT NULL DEFAULT 'none',
  normalized_cluster_key text,
  context_snapshot jsonb NOT NULL DEFAULT '{}'::jsonb,
  trigger_snapshot jsonb NOT NULL DEFAULT '{}'::jsonb,
  threshold_profile jsonb NOT NULL DEFAULT '{}'::jsonb,
  proposal_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (proposal_id, case_key)
);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_occurrences_candidate_type
  ON public.proposed_causal_candidate_occurrences (candidate_type);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_occurrences_proposal_key
  ON public.proposed_causal_candidate_occurrences (proposal_key);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_occurrences_mechanism_family
  ON public.proposed_causal_candidate_occurrences (mechanism_family);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_occurrences_proposal_source
  ON public.proposed_causal_candidate_occurrences (proposal_source);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_occurrences_cluster_key
  ON public.proposed_causal_candidate_occurrences (normalized_cluster_key);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_occurrences_case_key
  ON public.proposed_causal_candidate_occurrences (case_key);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_occurrences_updated_at
  ON public.proposed_causal_candidate_occurrences (updated_at);

GRANT SELECT, INSERT, UPDATE, DELETE ON public.proposed_causal_candidate_occurrences TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.proposed_causal_candidate_occurrences TO pq_orchestrator;
GRANT SELECT ON public.proposed_causal_candidate_occurrences TO pq_decision;
GRANT USAGE, SELECT ON SEQUENCE public.proposed_causal_candidate_occurrences_id_seq TO pq_evaluator;
GRANT USAGE, SELECT ON SEQUENCE public.proposed_causal_candidate_occurrences_id_seq TO pq_orchestrator;

COMMIT;
