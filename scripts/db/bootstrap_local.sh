#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
ENV_FILE="$ROOT_DIR/.env.postgres.local"
PSQL="/opt/homebrew/opt/postgresql@16/bin/psql"

command -v python3 >/dev/null 2>&1 || { echo "python3 is required" >&2; exit 1; }

randpw() {
  python3 - <<'PY'
import secrets
print(secrets.token_urlsafe(24))
PY
}

PQ_ADMIN_PW="$(randpw)"
PQ_INGEST_PW="$(randpw)"
PQ_ORCH_PW="$(randpw)"
PQ_DECISION_PW="$(randpw)"
PQ_EXEC_PW="$(randpw)"
PQ_EVAL_PW="$(randpw)"

$PSQL -d postgres -v ON_ERROR_STOP=1 <<SQL
DO \$\$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_admin') THEN
    CREATE ROLE pq_admin LOGIN PASSWORD '${PQ_ADMIN_PW}';
  ELSE
    ALTER ROLE pq_admin WITH LOGIN PASSWORD '${PQ_ADMIN_PW}';
  END IF;

  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_deviceb_ingest') THEN
    CREATE ROLE pq_deviceb_ingest LOGIN PASSWORD '${PQ_INGEST_PW}';
  ELSE
    ALTER ROLE pq_deviceb_ingest WITH LOGIN PASSWORD '${PQ_INGEST_PW}';
  END IF;

  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_orchestrator') THEN
    CREATE ROLE pq_orchestrator LOGIN PASSWORD '${PQ_ORCH_PW}';
  ELSE
    ALTER ROLE pq_orchestrator WITH LOGIN PASSWORD '${PQ_ORCH_PW}';
  END IF;

  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_decision') THEN
    CREATE ROLE pq_decision LOGIN PASSWORD '${PQ_DECISION_PW}';
  ELSE
    ALTER ROLE pq_decision WITH LOGIN PASSWORD '${PQ_DECISION_PW}';
  END IF;

  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_deviceb_exec') THEN
    CREATE ROLE pq_deviceb_exec LOGIN PASSWORD '${PQ_EXEC_PW}';
  ELSE
    ALTER ROLE pq_deviceb_exec WITH LOGIN PASSWORD '${PQ_EXEC_PW}';
  END IF;

  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_evaluator') THEN
    CREATE ROLE pq_evaluator LOGIN PASSWORD '${PQ_EVAL_PW}';
  ELSE
    ALTER ROLE pq_evaluator WITH LOGIN PASSWORD '${PQ_EVAL_PW}';
  END IF;
END\$\$;
SQL

if ! $PSQL -d postgres -Atqc "SELECT 1 FROM pg_database WHERE datname = 'predquant'" | grep -q 1; then
  $PSQL -d postgres -v ON_ERROR_STOP=1 -c "CREATE DATABASE predquant OWNER pq_admin"
else
  $PSQL -d postgres -v ON_ERROR_STOP=1 -c "ALTER DATABASE predquant OWNER TO pq_admin"
fi

cat > "$ENV_FILE" <<EOF
# Local PostgreSQL connection strings for predquant
# This file is gitignored.
export PREDQUANT_ADMIN_URL='postgresql://pq_admin:${PQ_ADMIN_PW}@localhost:5432/predquant'
export PREDQUANT_INGEST_URL='postgresql://pq_deviceb_ingest:${PQ_INGEST_PW}@localhost:5432/predquant'
export PREDQUANT_ORCHESTRATOR_URL='postgresql://pq_orchestrator:${PQ_ORCH_PW}@localhost:5432/predquant'
export PREDQUANT_DECISION_URL='postgresql://pq_decision:${PQ_DECISION_PW}@localhost:5432/predquant'
export PREDQUANT_EXEC_URL='postgresql://pq_deviceb_exec:${PQ_EXEC_PW}@localhost:5432/predquant'
export PREDQUANT_EVAL_URL='postgresql://pq_evaluator:${PQ_EVAL_PW}@localhost:5432/predquant'
EOF

chmod 600 "$ENV_FILE"

echo "Wrote $ENV_FILE"
echo "Next steps:"
echo "  source $ENV_FILE"
echo "  $ROOT_DIR/scripts/db/apply.sh"
echo "  $ROOT_DIR/scripts/db/check.sh"
