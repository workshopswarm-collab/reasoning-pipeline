BEGIN;

CREATE TABLE IF NOT EXISTS public.learning_case_reviews (
  review_path text PRIMARY KEY,
  packet_path text NOT NULL,
  case_key text NOT NULL,
  case_db_id text,
  market_id text,
  contract_id text,
  status text NOT NULL,
  category text,
  platform text,
  resolution_status text,
  resolved_value numeric(8,5),
  resolved_at timestamptz,
  error_pattern text,
  latest_forecast_prob numeric(8,5),
  latest_brier_component numeric(12,8),
  retrieval_tags jsonb NOT NULL DEFAULT '[]'::jsonb,
  source_paths jsonb NOT NULL DEFAULT '[]'::jsonb,
  review_frontmatter jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_learning_case_reviews_case_key
  ON public.learning_case_reviews (case_key);

CREATE INDEX IF NOT EXISTS idx_learning_case_reviews_status
  ON public.learning_case_reviews (status);

CREATE INDEX IF NOT EXISTS idx_learning_case_reviews_resolution_status
  ON public.learning_case_reviews (resolution_status);

CREATE INDEX IF NOT EXISTS idx_learning_case_reviews_market_id
  ON public.learning_case_reviews (market_id);

GRANT SELECT, INSERT, UPDATE ON public.learning_case_reviews TO pq_evaluator;
GRANT SELECT, INSERT, UPDATE ON public.learning_case_reviews TO pq_orchestrator;
GRANT SELECT ON public.learning_case_reviews TO pq_decision;

COMMIT;
