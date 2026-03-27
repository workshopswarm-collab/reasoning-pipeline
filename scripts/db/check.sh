#!/usr/bin/env bash
set -euo pipefail

DB_URL="${DB_URL:-${PREDQUANT_ADMIN_URL:-}}"

if [[ -z "${DB_URL}" ]]; then
  echo "DB_URL or PREDQUANT_ADMIN_URL is required" >&2
  exit 1
fi

/opt/homebrew/opt/postgresql@16/bin/psql "$DB_URL" -v ON_ERROR_STOP=1 -c "select current_user, current_database(), now();"
/opt/homebrew/opt/postgresql@16/bin/psql "$DB_URL" -v ON_ERROR_STOP=1 -c "\dt"
