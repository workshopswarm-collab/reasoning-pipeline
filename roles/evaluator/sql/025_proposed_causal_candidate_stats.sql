BEGIN;

CREATE TABLE IF NOT EXISTS public.proposed_causal_candidate_stats (
  proposal_id text PRIMARY KEY,
  proposal_key text NOT NULL,
  candidate_type text NOT NULL,
  candidate_label text NOT NULL,
  mechanism_family text NOT NULL DEFAULT 'unassigned',
  normalized_cluster_key text,
  source_node_key text,
  target_node_key text,
  node_type text,
  effect_sign text,
  occurrence_count int NOT NULL DEFAULT 0,
  distinct_case_count int NOT NULL DEFAULT 0,
  support_case_count int NOT NULL DEFAULT 0,
  contest_case_count int NOT NULL DEFAULT 0,
  non_intervention_support_case_count int NOT NULL DEFAULT 0,
  intervention_only_support_case_count int NOT NULL DEFAULT 0,
  draft_intervention_support_case_count int NOT NULL DEFAULT 0,
  active_intervention_support_case_count int NOT NULL DEFAULT 0,
  heuristic_only_support_case_count int NOT NULL DEFAULT 0,
  review_text_support_case_count int NOT NULL DEFAULT 0,
  signal_packet_support_case_count int NOT NULL DEFAULT 0,
  frontmatter_support_case_count int NOT NULL DEFAULT 0,
  duplicate_of_live_graph boolean NOT NULL DEFAULT false,
  genericity_penalty numeric NOT NULL DEFAULT 0,
  promotion_score numeric NOT NULL DEFAULT 0,
  promotion_status text NOT NULL,
  promotion_reason text,
  lifecycle_stage text NOT NULL DEFAULT 'observed',
  first_seen_at timestamptz,
  last_seen_at timestamptz,
  proposal_source_mix jsonb NOT NULL DEFAULT '{}'::jsonb,
  dominant_proposal_source text,
  evidence_channel_counts jsonb NOT NULL DEFAULT '{}'::jsonb,
  shadow_match_count int NOT NULL DEFAULT 0,
  shadow_positive_count int NOT NULL DEFAULT 0,
  stage_entered_at timestamptz,
  promotion_blockers jsonb NOT NULL DEFAULT '[]'::jsonb,
  near_duplicate_keys jsonb NOT NULL DEFAULT '[]'::jsonb,
  near_live_graph_keys jsonb NOT NULL DEFAULT '[]'::jsonb,
  max_duplicate_similarity numeric,
  merge_candidate_key text,
  merge_recommended boolean NOT NULL DEFAULT false,
  distinct_platform_count int NOT NULL DEFAULT 0,
  distinct_category_count int NOT NULL DEFAULT 0,
  distinct_question_mechanics_count int NOT NULL DEFAULT 0,
  distinct_source_of_truth_class_count int NOT NULL DEFAULT 0,
  distinct_domain_count int NOT NULL DEFAULT 0,
  context_distribution jsonb NOT NULL DEFAULT '{}'::jsonb,
  supporting_case_keys jsonb NOT NULL DEFAULT '[]'::jsonb,
  threshold_profile jsonb NOT NULL DEFAULT '{}'::jsonb,
  stats_metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_stats_candidate_type
  ON public.proposed_causal_candidate_stats (candidate_type);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_stats_promotion_status
  ON public.proposed_causal_candidate_stats (promotion_status);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_stats_lifecycle_stage
  ON public.proposed_causal_candidate_stats (lifecycle_stage);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_stats_mechanism_family
  ON public.proposed_causal_candidate_stats (mechanism_family);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_stats_cluster_key
  ON public.proposed_causal_candidate_stats (normalized_cluster_key);

CREATE INDEX IF NOT EXISTS idx_proposed_causal_candidate_stats_merge_recommended
  ON public.proposed_causal_candidate_stats (merge_recommended);

GRANT SELECT, INSERT, UPDATE, DELETE ON public.proposed_causal_candidate_stats TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.proposed_causal_candidate_stats TO pq_orchestrator;
GRANT SELECT ON public.proposed_causal_candidate_stats TO pq_decision;

COMMIT;
