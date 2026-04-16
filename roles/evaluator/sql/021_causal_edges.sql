BEGIN;

CREATE TABLE IF NOT EXISTS public.causal_edges (
  edge_key text PRIMARY KEY,
  path text NOT NULL UNIQUE,
  edge_label text NOT NULL,
  source_node_key text NOT NULL REFERENCES public.causal_nodes(node_key) ON DELETE RESTRICT,
  target_node_key text NOT NULL REFERENCES public.causal_nodes(node_key) ON DELETE RESTRICT,
  effect_sign text NOT NULL,
  status text NOT NULL,
  mechanism_family text NOT NULL DEFAULT 'unassigned',
  source_kind text NOT NULL DEFAULT 'unknown',
  lifecycle_stage text NOT NULL DEFAULT 'draft',
  confidence_mode text NOT NULL,
  confidence_prior numeric,
  promotion_score numeric NOT NULL DEFAULT 0,
  description text,
  contexts jsonb NOT NULL DEFAULT '{}'::jsonb,
  linked_intervention_keys jsonb NOT NULL DEFAULT '[]'::jsonb,
  evidence_paths jsonb NOT NULL DEFAULT '[]'::jsonb,
  note_frontmatter jsonb NOT NULL DEFAULT '{}'::jsonb,
  sidecar_path text,
  last_seen_at timestamptz,
  last_matched_at timestamptz,
  last_injected_at timestamptz,
  last_helpful_at timestamptz,
  decay_score numeric NOT NULL DEFAULT 0,
  demotion_reason text,
  superseded_by_key text REFERENCES public.causal_edges(edge_key) ON DELETE SET NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_causal_edges_status
  ON public.causal_edges (status);

CREATE INDEX IF NOT EXISTS idx_causal_edges_source_node_key
  ON public.causal_edges (source_node_key);

CREATE INDEX IF NOT EXISTS idx_causal_edges_target_node_key
  ON public.causal_edges (target_node_key);

CREATE INDEX IF NOT EXISTS idx_causal_edges_effect_sign
  ON public.causal_edges (effect_sign);

CREATE INDEX IF NOT EXISTS idx_causal_edges_mechanism_family
  ON public.causal_edges (mechanism_family);

CREATE INDEX IF NOT EXISTS idx_causal_edges_source_kind
  ON public.causal_edges (source_kind);

CREATE INDEX IF NOT EXISTS idx_causal_edges_lifecycle_stage
  ON public.causal_edges (lifecycle_stage);

GRANT SELECT, INSERT, UPDATE ON public.causal_edges TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.causal_edges TO pq_orchestrator;
GRANT SELECT ON public.causal_edges TO pq_decision;

COMMIT;
