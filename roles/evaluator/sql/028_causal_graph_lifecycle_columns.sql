BEGIN;

ALTER TABLE public.causal_nodes
  ADD COLUMN IF NOT EXISTS mechanism_family text NOT NULL DEFAULT 'unassigned',
  ADD COLUMN IF NOT EXISTS source_kind text NOT NULL DEFAULT 'unknown',
  ADD COLUMN IF NOT EXISTS lifecycle_stage text NOT NULL DEFAULT 'draft',
  ADD COLUMN IF NOT EXISTS promotion_score numeric NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS last_seen_at timestamptz,
  ADD COLUMN IF NOT EXISTS last_matched_at timestamptz,
  ADD COLUMN IF NOT EXISTS last_injected_at timestamptz,
  ADD COLUMN IF NOT EXISTS last_helpful_at timestamptz,
  ADD COLUMN IF NOT EXISTS decay_score numeric NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS demotion_reason text,
  ADD COLUMN IF NOT EXISTS superseded_by_key text;

ALTER TABLE public.causal_nodes
  DROP CONSTRAINT IF EXISTS causal_nodes_superseded_by_key_fkey;

ALTER TABLE public.causal_nodes
  ADD CONSTRAINT causal_nodes_superseded_by_key_fkey
  FOREIGN KEY (superseded_by_key) REFERENCES public.causal_nodes(node_key) ON DELETE SET NULL;

UPDATE public.causal_nodes
SET lifecycle_stage = CASE
  WHEN status = 'active' THEN 'active'
  WHEN status = 'draft' THEN 'draft'
  WHEN status = 'retired' THEN 'retired'
  WHEN status = 'paused' THEN 'hold'
  ELSE lifecycle_stage
END
WHERE lifecycle_stage IS NULL OR lifecycle_stage = 'draft';

ALTER TABLE public.causal_edges
  ADD COLUMN IF NOT EXISTS mechanism_family text NOT NULL DEFAULT 'unassigned',
  ADD COLUMN IF NOT EXISTS source_kind text NOT NULL DEFAULT 'unknown',
  ADD COLUMN IF NOT EXISTS lifecycle_stage text NOT NULL DEFAULT 'draft',
  ADD COLUMN IF NOT EXISTS promotion_score numeric NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS last_seen_at timestamptz,
  ADD COLUMN IF NOT EXISTS last_matched_at timestamptz,
  ADD COLUMN IF NOT EXISTS last_injected_at timestamptz,
  ADD COLUMN IF NOT EXISTS last_helpful_at timestamptz,
  ADD COLUMN IF NOT EXISTS decay_score numeric NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS demotion_reason text,
  ADD COLUMN IF NOT EXISTS superseded_by_key text;

ALTER TABLE public.causal_edges
  DROP CONSTRAINT IF EXISTS causal_edges_superseded_by_key_fkey;

ALTER TABLE public.causal_edges
  ADD CONSTRAINT causal_edges_superseded_by_key_fkey
  FOREIGN KEY (superseded_by_key) REFERENCES public.causal_edges(edge_key) ON DELETE SET NULL;

UPDATE public.causal_edges
SET lifecycle_stage = CASE
  WHEN status = 'active' THEN 'active'
  WHEN status = 'draft' THEN 'draft'
  WHEN status = 'retired' THEN 'retired'
  WHEN status = 'paused' THEN 'hold'
  ELSE lifecycle_stage
END
WHERE lifecycle_stage IS NULL OR lifecycle_stage = 'draft';

ALTER TABLE public.proposed_causal_candidate_occurrences
  ADD COLUMN IF NOT EXISTS updated_at timestamptz NOT NULL DEFAULT now();

UPDATE public.proposed_causal_candidate_occurrences
SET updated_at = COALESCE(updated_at, created_at, now());

ALTER TABLE public.proposed_causal_candidate_stats
  ADD COLUMN IF NOT EXISTS lifecycle_stage text NOT NULL DEFAULT 'observed',
  ADD COLUMN IF NOT EXISTS first_seen_at timestamptz,
  ADD COLUMN IF NOT EXISTS last_seen_at timestamptz,
  ADD COLUMN IF NOT EXISTS evidence_channel_counts jsonb NOT NULL DEFAULT '{}'::jsonb,
  ADD COLUMN IF NOT EXISTS shadow_match_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS shadow_positive_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS stage_entered_at timestamptz,
  ADD COLUMN IF NOT EXISTS promotion_blockers jsonb NOT NULL DEFAULT '[]'::jsonb;

UPDATE public.proposed_causal_candidate_stats
SET lifecycle_stage = CASE
  WHEN promotion_status = 'duplicate_of_live_graph' THEN 'duplicate_of_live_graph'
  ELSE 'aggregated'
END,
first_seen_at = COALESCE(first_seen_at, updated_at, now()),
last_seen_at = COALESCE(last_seen_at, updated_at, now()),
stage_entered_at = COALESCE(stage_entered_at, updated_at, now())
WHERE lifecycle_stage IS NULL OR lifecycle_stage = 'observed';

CREATE INDEX IF NOT EXISTS idx_causal_nodes_mechanism_family
  ON public.causal_nodes (mechanism_family);
CREATE INDEX IF NOT EXISTS idx_causal_nodes_source_kind
  ON public.causal_nodes (source_kind);
CREATE INDEX IF NOT EXISTS idx_causal_nodes_lifecycle_stage
  ON public.causal_nodes (lifecycle_stage);

CREATE INDEX IF NOT EXISTS idx_causal_edges_mechanism_family
  ON public.causal_edges (mechanism_family);
CREATE INDEX IF NOT EXISTS idx_causal_edges_source_kind
  ON public.causal_edges (source_kind);
CREATE INDEX IF NOT EXISTS idx_causal_edges_lifecycle_stage
  ON public.causal_edges (lifecycle_stage);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_occurrences_updated_at
  ON public.proposed_causal_candidate_occurrences (updated_at);
CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_stats_lifecycle_stage
  ON public.proposed_causal_candidate_stats (lifecycle_stage);

COMMIT;
