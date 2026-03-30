#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
DB_URL="${DB_URL:-${PREDQUANT_ADMIN_URL:-}}"

if [[ -z "${DB_URL}" ]]; then
  echo "DB_URL or PREDQUANT_ADMIN_URL is required" >&2
  exit 1
fi

shopt -s nullglob
for file in "$ROOT_DIR"/quant-db/migrations/*.sql; do
  echo "Applying $(basename "$file")"
  /opt/homebrew/opt/postgresql@16/bin/psql "$DB_URL" -v ON_ERROR_STOP=1 -f "$file"
done
