BEGIN;

ALTER TABLE public.proposed_causal_candidate_occurrences
  ADD COLUMN IF NOT EXISTS mechanism_family text NOT NULL DEFAULT 'unassigned',
  ADD COLUMN IF NOT EXISTS proposal_source text NOT NULL DEFAULT 'rule_projection',
  ADD COLUMN IF NOT EXISTS evidence_channels jsonb NOT NULL DEFAULT '[]'::jsonb,
  ADD COLUMN IF NOT EXISTS intervention_dependency text NOT NULL DEFAULT 'none',
  ADD COLUMN IF NOT EXISTS normalized_cluster_key text,
  ADD COLUMN IF NOT EXISTS context_snapshot jsonb NOT NULL DEFAULT '{}'::jsonb;

ALTER TABLE public.proposed_causal_candidate_stats
  ADD COLUMN IF NOT EXISTS mechanism_family text NOT NULL DEFAULT 'unassigned',
  ADD COLUMN IF NOT EXISTS normalized_cluster_key text,
  ADD COLUMN IF NOT EXISTS proposal_source_mix jsonb NOT NULL DEFAULT '{}'::jsonb,
  ADD COLUMN IF NOT EXISTS dominant_proposal_source text,
  ADD COLUMN IF NOT EXISTS non_intervention_support_case_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS intervention_only_support_case_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS draft_intervention_support_case_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS active_intervention_support_case_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS heuristic_only_support_case_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS review_text_support_case_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS signal_packet_support_case_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS frontmatter_support_case_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS near_duplicate_keys jsonb NOT NULL DEFAULT '[]'::jsonb,
  ADD COLUMN IF NOT EXISTS near_live_graph_keys jsonb NOT NULL DEFAULT '[]'::jsonb,
  ADD COLUMN IF NOT EXISTS max_duplicate_similarity numeric,
  ADD COLUMN IF NOT EXISTS merge_candidate_key text,
  ADD COLUMN IF NOT EXISTS merge_recommended boolean NOT NULL DEFAULT false,
  ADD COLUMN IF NOT EXISTS distinct_platform_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS distinct_category_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS distinct_question_mechanics_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS distinct_source_of_truth_class_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS distinct_domain_count int NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS context_distribution jsonb NOT NULL DEFAULT '{}'::jsonb;

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_occurrences_mechanism_family
  ON public.proposed_causal_candidate_occurrences (mechanism_family);
CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_occurrences_proposal_source
  ON public.proposed_causal_candidate_occurrences (proposal_source);
CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_occurrences_cluster_key
  ON public.proposed_causal_candidate_occurrences (normalized_cluster_key);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_stats_mechanism_family
  ON public.proposed_causal_candidate_stats (mechanism_family);
CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_stats_cluster_key
  ON public.proposed_causal_candidate_stats (normalized_cluster_key);
CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_stats_merge_recommended
  ON public.proposed_causal_candidate_stats (merge_recommended);

GRANT SELECT, INSERT, UPDATE, DELETE ON public.proposed_causal_candidate_occurrences TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.proposed_causal_candidate_occurrences TO pq_orchestrator;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.proposed_causal_candidate_stats TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.proposed_causal_candidate_stats TO pq_orchestrator;

COMMIT;
