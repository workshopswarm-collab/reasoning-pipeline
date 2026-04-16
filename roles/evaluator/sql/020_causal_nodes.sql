BEGIN;

CREATE TABLE IF NOT EXISTS public.causal_nodes (
  node_key text PRIMARY KEY,
  path text NOT NULL UNIQUE,
  node_label text NOT NULL,
  node_type text NOT NULL,
  status text NOT NULL,
  mechanism_family text NOT NULL DEFAULT 'unassigned',
  source_kind text NOT NULL DEFAULT 'unknown',
  lifecycle_stage text NOT NULL DEFAULT 'draft',
  promotion_score numeric NOT NULL DEFAULT 0,
  description text,
  contexts jsonb NOT NULL DEFAULT '{}'::jsonb,
  tags jsonb NOT NULL DEFAULT '[]'::jsonb,
  linked_paths jsonb NOT NULL DEFAULT '{}'::jsonb,
  note_frontmatter jsonb NOT NULL DEFAULT '{}'::jsonb,
  sidecar_path text,
  last_seen_at timestamptz,
  last_matched_at timestamptz,
  last_injected_at timestamptz,
  last_helpful_at timestamptz,
  decay_score numeric NOT NULL DEFAULT 0,
  demotion_reason text,
  superseded_by_key text REFERENCES public.causal_nodes(node_key) ON DELETE SET NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_causal_nodes_status
  ON public.causal_nodes (status);

CREATE INDEX IF NOT EXISTS idx_causal_nodes_node_type
  ON public.causal_nodes (node_type);

CREATE INDEX IF NOT EXISTS idx_causal_nodes_mechanism_family
  ON public.causal_nodes (mechanism_family);

CREATE INDEX IF NOT EXISTS idx_causal_nodes_source_kind
  ON public.causal_nodes (source_kind);

CREATE INDEX IF NOT EXISTS idx_causal_nodes_lifecycle_stage
  ON public.causal_nodes (lifecycle_stage);

GRANT SELECT, INSERT, UPDATE ON public.causal_nodes TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.causal_nodes TO pq_orchestrator;
GRANT SELECT ON public.causal_nodes TO pq_decision;

COMMIT;
