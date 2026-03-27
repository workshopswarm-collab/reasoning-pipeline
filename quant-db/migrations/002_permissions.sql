BEGIN;

DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_admin') THEN
    ALTER DATABASE predquant OWNER TO pq_admin;
  END IF;
END$$;

DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_deviceb_ingest') THEN
    GRANT CONNECT ON DATABASE predquant TO pq_deviceb_ingest;
    GRANT USAGE ON SCHEMA public TO pq_deviceb_ingest;
    GRANT SELECT, INSERT, UPDATE ON markets TO pq_deviceb_ingest;
    GRANT SELECT, INSERT ON market_snapshots TO pq_deviceb_ingest;
  END IF;
END$$;

DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_orchestrator') THEN
    GRANT CONNECT ON DATABASE predquant TO pq_orchestrator;
    GRANT USAGE ON SCHEMA public TO pq_orchestrator;
    GRANT SELECT ON markets, market_snapshots, outcomes TO pq_orchestrator;
    GRANT SELECT, INSERT, UPDATE ON cases, research_runs, agent_predictions, retrospectives TO pq_orchestrator;
  END IF;
END$$;

DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_decision') THEN
    GRANT CONNECT ON DATABASE predquant TO pq_decision;
    GRANT USAGE ON SCHEMA public TO pq_decision;
    GRANT SELECT ON markets, market_snapshots, cases, research_runs, agent_predictions, outcomes TO pq_decision;
    GRANT SELECT, INSERT, UPDATE ON decision_packets TO pq_decision;
  END IF;
END$$;

DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_deviceb_exec') THEN
    GRANT CONNECT ON DATABASE predquant TO pq_deviceb_exec;
    GRANT USAGE ON SCHEMA public TO pq_deviceb_exec;
    GRANT SELECT ON markets, market_snapshots, cases, decision_packets, outcomes TO pq_deviceb_exec;
    GRANT SELECT, INSERT, UPDATE ON paper_executions TO pq_deviceb_exec;
  END IF;
END$$;

DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_evaluator') THEN
    GRANT CONNECT ON DATABASE predquant TO pq_evaluator;
    GRANT USAGE ON SCHEMA public TO pq_evaluator;
    GRANT SELECT ON markets, market_snapshots, cases, research_runs, agent_predictions, decision_packets, paper_executions, outcomes TO pq_evaluator;
    GRANT SELECT, INSERT, UPDATE ON retrospectives TO pq_evaluator;
  END IF;
END$$;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO pq_deviceb_ingest, pq_orchestrator, pq_decision, pq_deviceb_exec, pq_evaluator;

COMMIT;
