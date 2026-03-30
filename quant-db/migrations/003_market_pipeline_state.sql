BEGIN;

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'processing_status') THEN
    CREATE TYPE processing_status AS ENUM (
      'new',
      'pending_research',
      'researching',
      'ignored',
      'executed',
      'closed'
    );
  END IF;
END$$;

ALTER TABLE markets
  ADD COLUMN IF NOT EXISTS current_price NUMERIC(10,6),
  ADD COLUMN IF NOT EXISTS last_reasoned_price NUMERIC(10,6),
  ADD COLUMN IF NOT EXISTS pipeline_status processing_status NOT NULL DEFAULT 'new';

CREATE INDEX IF NOT EXISTS idx_markets_pipeline_status ON markets(pipeline_status);
CREATE INDEX IF NOT EXISTS idx_markets_pipeline_status_closes_at ON markets(pipeline_status, closes_at);

COMMIT;
