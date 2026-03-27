BEGIN;

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS markets (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  platform TEXT NOT NULL,
  external_market_id TEXT NOT NULL,
  slug TEXT,
  title TEXT NOT NULL,
  description TEXT,
  category TEXT,
  status TEXT NOT NULL DEFAULT 'open',
  outcome_type TEXT,
  closes_at TIMESTAMPTZ,
  resolves_at TIMESTAMPTZ,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(platform, external_market_id)
);

CREATE INDEX IF NOT EXISTS idx_markets_platform ON markets(platform);
CREATE INDEX IF NOT EXISTS idx_markets_status ON markets(status);
CREATE INDEX IF NOT EXISTS idx_markets_closes_at ON markets(closes_at);

CREATE TABLE IF NOT EXISTS market_snapshots (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  market_id UUID NOT NULL REFERENCES markets(id) ON DELETE CASCADE,
  observed_at TIMESTAMPTZ NOT NULL,
  last_price NUMERIC(10,6),
  best_bid NUMERIC(10,6),
  best_ask NUMERIC(10,6),
  yes_price NUMERIC(10,6),
  no_price NUMERIC(10,6),
  volume NUMERIC(20,6),
  open_interest NUMERIC(20,6),
  raw_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_market_snapshots_market_observed ON market_snapshots(market_id, observed_at DESC);

CREATE TABLE IF NOT EXISTS cases (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  market_id UUID NOT NULL REFERENCES markets(id) ON DELETE RESTRICT,
  case_key TEXT UNIQUE,
  status TEXT NOT NULL DEFAULT 'open',
  priority TEXT NOT NULL DEFAULT 'normal',
  opened_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  closed_at TIMESTAMPTZ,
  created_by TEXT,
  orchestration_notes JSONB NOT NULL DEFAULT '{}'::jsonb
);

CREATE INDEX IF NOT EXISTS idx_cases_market_id ON cases(market_id);
CREATE INDEX IF NOT EXISTS idx_cases_status ON cases(status);

CREATE TABLE IF NOT EXISTS research_runs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
  run_label TEXT,
  agent_label TEXT NOT NULL,
  runtime TEXT,
  status TEXT NOT NULL DEFAULT 'queued',
  started_at TIMESTAMPTZ,
  completed_at TIMESTAMPTZ,
  workspace_note_path TEXT,
  notes JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_research_runs_case_id ON research_runs(case_id);
CREATE INDEX IF NOT EXISTS idx_research_runs_status ON research_runs(status);

CREATE TABLE IF NOT EXISTS agent_predictions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  research_run_id UUID NOT NULL REFERENCES research_runs(id) ON DELETE CASCADE,
  case_id UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
  market_id UUID NOT NULL REFERENCES markets(id) ON DELETE RESTRICT,
  predicted_probability NUMERIC(7,6) NOT NULL CHECK (predicted_probability >= 0 AND predicted_probability <= 1),
  confidence NUMERIC(7,6) CHECK (confidence IS NULL OR (confidence >= 0 AND confidence <= 1)),
  time_horizon TEXT,
  thesis_summary TEXT,
  note_path TEXT,
  assumptions JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_agent_predictions_case_id ON agent_predictions(case_id);
CREATE INDEX IF NOT EXISTS idx_agent_predictions_market_id ON agent_predictions(market_id);
CREATE INDEX IF NOT EXISTS idx_agent_predictions_run_id ON agent_predictions(research_run_id);

CREATE TABLE IF NOT EXISTS decision_packets (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
  market_id UUID NOT NULL REFERENCES markets(id) ON DELETE RESTRICT,
  version INTEGER NOT NULL DEFAULT 1,
  status TEXT NOT NULL DEFAULT 'draft',
  side TEXT,
  target_probability NUMERIC(7,6) CHECK (target_probability IS NULL OR (target_probability >= 0 AND target_probability <= 1)),
  action_zone JSONB NOT NULL DEFAULT '{}'::jsonb,
  constraints JSONB NOT NULL DEFAULT '{}'::jsonb,
  invalidation JSONB NOT NULL DEFAULT '{}'::jsonb,
  reasoning_summary TEXT,
  note_path TEXT,
  created_by TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(case_id, version)
);

CREATE INDEX IF NOT EXISTS idx_decision_packets_case_id ON decision_packets(case_id);
CREATE INDEX IF NOT EXISTS idx_decision_packets_market_id ON decision_packets(market_id);
CREATE INDEX IF NOT EXISTS idx_decision_packets_status ON decision_packets(status);

CREATE TABLE IF NOT EXISTS paper_executions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  decision_packet_id UUID REFERENCES decision_packets(id) ON DELETE SET NULL,
  case_id UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
  market_id UUID NOT NULL REFERENCES markets(id) ON DELETE RESTRICT,
  execution_status TEXT NOT NULL DEFAULT 'proposed',
  side TEXT,
  size NUMERIC(20,6),
  price NUMERIC(10,6),
  observed_at TIMESTAMPTZ NOT NULL,
  executed_at TIMESTAMPTZ,
  rationale TEXT,
  raw_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_paper_executions_case_id ON paper_executions(case_id);
CREATE INDEX IF NOT EXISTS idx_paper_executions_market_id ON paper_executions(market_id);
CREATE INDEX IF NOT EXISTS idx_paper_executions_decision_packet_id ON paper_executions(decision_packet_id);

CREATE TABLE IF NOT EXISTS outcomes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  market_id UUID NOT NULL REFERENCES markets(id) ON DELETE CASCADE,
  resolved_outcome TEXT NOT NULL,
  resolved_value NUMERIC(7,6),
  resolved_at TIMESTAMPTZ NOT NULL,
  source TEXT,
  raw_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE (market_id)
);

CREATE INDEX IF NOT EXISTS idx_outcomes_market_id ON outcomes(market_id);

CREATE TABLE IF NOT EXISTS retrospectives (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
  market_id UUID NOT NULL REFERENCES markets(id) ON DELETE RESTRICT,
  status TEXT NOT NULL DEFAULT 'open',
  summary TEXT,
  note_path TEXT,
  lessons JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  completed_at TIMESTAMPTZ
);

CREATE INDEX IF NOT EXISTS idx_retrospectives_case_id ON retrospectives(case_id);
CREATE INDEX IF NOT EXISTS idx_retrospectives_market_id ON retrospectives(market_id);

COMMIT;
