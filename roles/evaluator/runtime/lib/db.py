from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
DEFAULT_ENV_PATH = Path(__file__).resolve().parents[4] / ".env"


def maybe_load_workspace_env() -> None:
    if os.getenv("PREDQUANT_EVALUATOR_URL") or os.getenv("PREDQUANT_EVAL_URL") or os.getenv("PREDQUANT_ORCHESTRATOR_URL"):
        return
    if not DEFAULT_ENV_PATH.exists():
        return
    for raw_line in DEFAULT_ENV_PATH.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def resolve_db_url(explicit: str | None = None) -> str:
    maybe_load_workspace_env()
    return (
        explicit
        or os.getenv("PREDQUANT_EVALUATOR_URL")
        or os.getenv("PREDQUANT_EVAL_URL")
        or os.getenv("PREDQUANT_ORCHESTRATOR_URL")
        or os.getenv("PREDQUANT_ADMIN_URL")
        or ""
    )


def exec_sql(psql_bin: str, db_url: str, sql: str, variables: dict[str, str]) -> Any:
    if not db_url:
        raise ValueError(
            "--db-url, PREDQUANT_EVALUATOR_URL, PREDQUANT_EVAL_URL, PREDQUANT_ORCHESTRATOR_URL, or PREDQUANT_ADMIN_URL is required"
        )
    cmd = [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1"]
    for key, value in variables.items():
        cmd.extend(["-v", f"{key}={value}"])
    cmd.extend(["-f", "-"])
    proc = subprocess.run(cmd, input=sql, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    if not stdout:
        return {}
    return json.loads(stdout.splitlines()[-1])


def table_exists(table_name: str, *, db_url: str | None = None, psql_bin: str = DEFAULT_PSQL) -> bool:
    sql = "SELECT json_build_object('exists', to_regclass('public.' || :'table_name') IS NOT NULL)::text;"
    try:
        payload = exec_sql(psql_bin, resolve_db_url(db_url), sql, {"table_name": table_name})
    except Exception:
        return False
    return bool((payload or {}).get("exists"))


def missing_columns(table_name: str, column_names: list[str], *, db_url: str | None = None, psql_bin: str = DEFAULT_PSQL) -> list[str]:
    if not column_names:
        return []
    sql = r'''
WITH requested AS (
  SELECT json_array_elements_text(COALESCE(NULLIF(:'columns_json', ''), '[]')::json) AS column_name
),
missing AS (
  SELECT column_name
  FROM requested
  EXCEPT
  SELECT c.column_name
  FROM information_schema.columns AS c
  WHERE c.table_schema = 'public'
    AND c.table_name = :'table_name'
)
SELECT json_build_object('missing', COALESCE(json_agg(column_name ORDER BY column_name), '[]'::json))::text
FROM missing;
'''
    try:
        payload = exec_sql(psql_bin, resolve_db_url(db_url), sql, {"table_name": table_name, "columns_json": json.dumps(column_names)})
    except Exception:
        return column_names
    missing = (payload or {}).get("missing") or []
    if isinstance(missing, list):
        return [str(item) for item in missing]
    return column_names
