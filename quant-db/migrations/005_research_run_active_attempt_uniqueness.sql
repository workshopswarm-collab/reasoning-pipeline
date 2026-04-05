BEGIN;

-- Enforce at most one active attempt per case/persona lane.
-- Apply only after auditing/cleaning existing duplicate queued/running rows.
CREATE UNIQUE INDEX IF NOT EXISTS uq_research_runs_active_case_agent
  ON research_runs(case_id, agent_label)
  WHERE status IN ('queued', 'running');

COMMIT;
