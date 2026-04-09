#!/usr/bin/env python3
from __future__ import annotations

"""Reconcile a run completion back into research_runs.

Current behavior:
- resolve by `research_run_id`
- patch status to completed/failed
- set completed_at for successful completion
- store completion summary / error in notes
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
BASE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = BASE_DIR.parent
PIPELINE_DIR = RUNTIME_DIR.parent
WORKSPACE_ROOT = PIPELINE_DIR.parents[2]
SYNTHESIS_SUBAGENT_DIR = WORKSPACE_ROOT / "roles/orchestrator/synthesis-subagent"
if str(SYNTHESIS_SUBAGENT_DIR) not in sys.path:
    sys.path.insert(0, str(SYNTHESIS_SUBAGENT_DIR))
DEFAULT_ENV_PATH = WORKSPACE_ROOT / ".env"
VALIDATE_LINKAGES_SCRIPT = BASE_DIR / "validate_research_artifact_linkages.py"
UPSERT_PROPOSED_DRIVER_OCCURRENCES_SCRIPT = BASE_DIR / "upsert_proposed_driver_occurrences.py"
ASYNC_PROPOSED_DRIVER_REVIEW_WORKER = BASE_DIR / "run_async_proposed_driver_review.py"
ASYNC_PROPOSED_DRIVER_REVIEW_STATE_DIR = BASE_DIR / ".runtime-state" / "proposed-driver-review"

from validation import validate_reasoning_sidecar_artifact, validate_reasoning_sidecar_payload  # noqa: E402

SQL_LOOKUP = r'''
WITH input AS (
  SELECT (:'payload'::jsonb) AS j
)
SELECT json_build_object(
  'research_run_id', rr.id,
  'case_id', rr.case_id,
  'run_label', rr.run_label,
  'agent_label', rr.agent_label,
  'status', rr.status,
  'workspace_note_path', rr.workspace_note_path,
  'notes', rr.notes,
  'created_at', rr.created_at
)::text
FROM research_runs rr
CROSS JOIN input i
WHERE rr.id = NULLIF(i.j->>'research_run_id', '')::uuid
ORDER BY rr.created_at DESC
LIMIT 1;
'''


def maybe_load_workspace_env() -> None:
    if os.getenv("PREDQUANT_ORCHESTRATOR_URL"):
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reconcile completion event to research_runs")
    parser.add_argument("--file", default="-", help="Path to input JSON file, or - for stdin")
    parser.add_argument("--research-run-id", required=True, help="Primary completion join key for fixed-channel runs")
    parser.add_argument("--status", choices=["completed", "failed"], help="Final run status")
    parser.add_argument("--error", help="Optional error text when failed")
    parser.add_argument("--completion-summary", help="Optional completion summary text")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON result")
    return parser.parse_args()


def load_json(path_str: str):
    if path_str == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path_str).read_text()
    if not raw.strip():
        return {}
    return json.loads(raw)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def reasoning_sidecar_path_for(workspace_note_path: str) -> str:
    path = Path(workspace_note_path)
    if path.suffix == ".md":
        return str(path.with_suffix(".sidecar.json"))
    return str(path) + ".sidecar.json"


def build_payload(args: argparse.Namespace) -> dict:
    payload = load_json(args.file)
    if payload and not isinstance(payload, dict):
        raise ValueError("input JSON must be an object")
    payload = dict(payload or {})
    payload["research_run_id"] = args.research_run_id
    if args.status:
        payload["status"] = args.status
    if args.error:
        payload["error"] = args.error
    if args.completion_summary:
        payload["completion_summary"] = args.completion_summary
    if not payload.get("status"):
        raise ValueError("status is required")
    return payload


def validate_required_reasoning_sidecar(lookup: dict) -> dict:
    workspace_note_rel = lookup.get("workspace_note_path") or ""
    if not workspace_note_rel:
        raise ValueError("workspace_note_path is required for completed research runs")
    workspace_note_abs = Path(workspace_note_rel)
    if not workspace_note_abs.is_absolute():
        workspace_note_abs = WORKSPACE_ROOT / workspace_note_abs
    sidecar_rel = reasoning_sidecar_path_for(workspace_note_rel)
    sidecar_abs = Path(sidecar_rel)
    if not sidecar_abs.is_absolute():
        sidecar_abs = WORKSPACE_ROOT / sidecar_abs
    if not workspace_note_abs.exists():
        raise FileNotFoundError(f"workspace note missing: {workspace_note_rel}")
    if not sidecar_abs.exists():
        raise FileNotFoundError(f"reasoning sidecar missing: {sidecar_rel}")
    sidecar_payload = json.loads(sidecar_abs.read_text())
    validation = validate_reasoning_sidecar_payload(sidecar_payload)
    if not validation.get("ok"):
        raise ValueError(f"reasoning sidecar structurally invalid for completed run: {validation.get('errors') or []}")
    expected_persona = str(lookup.get("agent_label") or "").strip()
    if expected_persona and str(sidecar_payload.get("persona") or "").strip() != expected_persona:
        raise ValueError(f"reasoning sidecar persona mismatch: expected {expected_persona}, got {sidecar_payload.get('persona')!r}")
    return {
        "path": sidecar_rel,
        "warnings": validation.get("warnings") or [],
        "payload": sidecar_payload,
    }


def sync_reasoning_sidecar_metadata(lookup: dict, required_sidecar: dict) -> dict:
    workspace_note_rel = lookup.get("workspace_note_path") or ""
    workspace_note_abs = Path(workspace_note_rel)
    if not workspace_note_abs.is_absolute():
        workspace_note_abs = WORKSPACE_ROOT / workspace_note_abs
    sidecar_rel = required_sidecar["path"]
    sidecar_abs = Path(sidecar_rel)
    if not sidecar_abs.is_absolute():
        sidecar_abs = WORKSPACE_ROOT / sidecar_abs
    persona_text = workspace_note_abs.read_text()
    current_sha = sha256_text(persona_text)
    payload = dict(required_sidecar.get("payload") or json.loads(sidecar_abs.read_text()))
    runtime_metadata = dict(payload.get("runtime_metadata") or {})
    changed = False
    if runtime_metadata.get("source_persona_finding_path") != workspace_note_rel:
        runtime_metadata["source_persona_finding_path"] = workspace_note_rel
        changed = True
    if runtime_metadata.get("source_persona_sha256") != current_sha:
        runtime_metadata["source_persona_sha256"] = current_sha
        changed = True
    if changed:
        payload["runtime_metadata"] = runtime_metadata
        sidecar_abs.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    validation = validate_reasoning_sidecar_artifact(
        payload,
        persona_finding_path=workspace_note_rel,
        source_persona_sha256=current_sha,
        persona=lookup.get("agent_label"),
    )
    if not validation.get("ok"):
        raise ValueError(f"reasoning sidecar invalid after sync: {validation.get('errors') or []}")
    return {
        "path": sidecar_rel,
        "warnings": validation.get("warnings") or [],
        "metadata_synced": changed,
        "payload": payload,
    }


def run_psql(psql_bin: str, db_url: str, payload: dict, sql: str) -> dict:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")
    payload_json = json.dumps(payload, separators=(",", ":"))
    proc = subprocess.run(
        [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1", "-v", f"payload={payload_json}", "-f", "-"],
        input=sql,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    if not stdout:
        raise ValueError("lookup returned no result")
    return json.loads(stdout.splitlines()[-1])


def python_json(script: Path, args: list[str], stdin_payload=None, *, timeout_seconds: float | None = None) -> dict:
    try:
        proc = subprocess.run(
            [sys.executable, str(script), *args],
            input=(json.dumps(stdin_payload) if stdin_payload is not None else None),
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"{script.name} timed out after {timeout_seconds}s") from exc
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"{script.name} failed")
    stdout = proc.stdout.strip()
    if not stdout:
        raise RuntimeError(f"{script.name} returned empty stdout")
    for line in reversed([line for line in stdout.splitlines() if line.strip()]):
        try:
            return json.loads(line)
        except json.JSONDecodeError:
            continue
    return json.loads(stdout)


def update_research_run_record(
    update_script: Path,
    *,
    research_run_id: str,
    db_url: str,
    status: str | None = None,
    workspace_note_path: str | None = None,
    notes: dict | None = None,
    mark_completed: bool = False,
) -> dict:
    update_args = [
        "--research-run-id", research_run_id,
        "--db-url", db_url,
    ]
    if status:
        update_args.extend(["--status", status])
    if workspace_note_path is not None:
        update_args.extend(["--workspace-note-path", workspace_note_path])
    if notes:
        update_args.extend(["--notes-json", json.dumps(notes, separators=(",", ":"))])
    if mark_completed:
        update_args.append("--mark-completed")
    return python_json(update_script, update_args)


def launch_async_proposed_driver_review_job(
    *,
    research_run_id: str,
    db_url: str,
    psql: str,
) -> dict:
    if not ASYNC_PROPOSED_DRIVER_REVIEW_WORKER.exists():
        return {"status": "missing_worker"}
    ASYNC_PROPOSED_DRIVER_REVIEW_STATE_DIR.mkdir(parents=True, exist_ok=True)
    log_path = ASYNC_PROPOSED_DRIVER_REVIEW_STATE_DIR / f"{research_run_id}.log"
    env = dict(os.environ)
    if db_url:
        env.setdefault("PREDQUANT_ORCHESTRATOR_URL", db_url)
    cmd = [
        sys.executable,
        str(ASYNC_PROPOSED_DRIVER_REVIEW_WORKER),
        "--research-run-id", research_run_id,
        "--db-url", db_url,
        "--psql", psql,
    ]
    log_handle = log_path.open("a")
    try:
        proc = subprocess.Popen(
            cmd,
            cwd=str(WORKSPACE_ROOT),
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            stdin=subprocess.DEVNULL,
            text=True,
            start_new_session=True,
            env=env,
        )
    finally:
        log_handle.close()
    return {
        "status": "started",
        "pid": proc.pid,
        "log_path": str(log_path.relative_to(WORKSPACE_ROOT)),
    }


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    try:
        payload = build_payload(args)
        lookup = run_psql(args.psql, args.db_url, payload, SQL_LOOKUP)
        required_sidecar = None
        if payload["status"] == "completed":
            required_sidecar = validate_required_reasoning_sidecar(lookup)
        update_script = Path(__file__).resolve().parent / "update_research_run.py"
        notes = {
            "dispatch_stage": "completed" if payload["status"] == "completed" else "terminated",
        }
        if payload.get("error"):
            notes["error"] = payload["error"]
        if payload.get("completion_summary"):
            notes["completion_summary"] = payload["completion_summary"]
        if required_sidecar is not None:
            notes["reasoning_sidecar"] = {
                "path": required_sidecar["path"],
                "status": "required_present_and_structurally_valid",
                "warnings": required_sidecar["warnings"],
            }

        result = update_research_run_record(
            update_script,
            research_run_id=lookup["research_run_id"],
            status=payload["status"],
            workspace_note_path=lookup.get("workspace_note_path") or "",
            notes=notes,
            db_url=args.db_url,
            mark_completed=(payload["status"] == "completed"),
        )

        enrichment_notes: dict = {}
        enrichment_result = None
        if required_sidecar is not None:
            enrichment_notes["reasoning_sidecar_validation"] = {
                "status": "ok",
                "path": required_sidecar["path"],
                "warnings": required_sidecar["warnings"],
                "metadata_synced": False,
            }

        if payload["status"] == "completed" and lookup.get("workspace_note_path") and VALIDATE_LINKAGES_SCRIPT.exists():
            try:
                validation_result = python_json(
                    VALIDATE_LINKAGES_SCRIPT,
                    ["--artifact-path", lookup["workspace_note_path"], "--include-linked-artifacts"],
                )
                enrichment_notes["linkage_validation"] = {
                    "status": validation_result.get("status"),
                    "artifacts_checked": validation_result.get("artifacts_checked"),
                    "artifacts_changed": validation_result.get("artifacts_changed"),
                    "had_unresolved": validation_result.get("had_unresolved"),
                    "unresolved_entities": validation_result.get("unresolved_entities") or [],
                    "unresolved_drivers": validation_result.get("unresolved_drivers") or [],
                }
            except Exception as linkage_exc:  # noqa: BLE001
                enrichment_notes["linkage_validation"] = {
                    "status": "error",
                    "error": str(linkage_exc),
                }
            if required_sidecar is not None:
                try:
                    required_sidecar = sync_reasoning_sidecar_metadata(lookup, required_sidecar)
                    enrichment_notes["reasoning_sidecar_validation"] = {
                        "status": "ok",
                        "path": required_sidecar["path"],
                        "warnings": required_sidecar["warnings"],
                        "metadata_synced": required_sidecar.get("metadata_synced", False),
                    }
                except Exception as sidecar_sync_exc:  # noqa: BLE001
                    enrichment_notes["reasoning_sidecar_validation"] = {
                        "status": "error",
                        "path": required_sidecar["path"],
                        "metadata_synced": required_sidecar.get("metadata_synced", False),
                        "error": str(sidecar_sync_exc),
                    }
            if UPSERT_PROPOSED_DRIVER_OCCURRENCES_SCRIPT.exists():
                try:
                    occurrence_result = python_json(
                        UPSERT_PROPOSED_DRIVER_OCCURRENCES_SCRIPT,
                        [
                            "--research-run-id", lookup["research_run_id"],
                            "--artifact-path", lookup["workspace_note_path"],
                            "--include-linked-artifacts",
                            "--db-url", args.db_url,
                        ],
                    )
                    enrichment_notes["proposed_driver_occurrence_store"] = {
                        "status": occurrence_result.get("status"),
                        "artifact_count": occurrence_result.get("artifact_count"),
                        "upserted_occurrence_count": occurrence_result.get("upserted_occurrence_count"),
                    }
                except Exception as occurrence_exc:  # noqa: BLE001
                    enrichment_notes["proposed_driver_occurrence_store"] = {
                        "status": "error",
                        "error": str(occurrence_exc),
                    }
            if ASYNC_PROPOSED_DRIVER_REVIEW_WORKER.exists():
                try:
                    async_job = launch_async_proposed_driver_review_job(
                        research_run_id=lookup["research_run_id"],
                        db_url=args.db_url,
                        psql=args.psql,
                    )
                    enrichment_notes["proposed_driver_review_job"] = async_job
                except Exception as async_job_exc:  # noqa: BLE001
                    enrichment_notes["proposed_driver_review_job"] = {
                        "status": "error",
                        "error": str(async_job_exc),
                    }

        if enrichment_notes:
            enrichment_result = update_research_run_record(
                update_script,
                research_run_id=lookup["research_run_id"],
                notes=enrichment_notes,
                db_url=args.db_url,
            )
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    output = {
        "research_run_id": lookup["research_run_id"],
        "result": result,
        "enrichment_result": enrichment_result,
    }
    if args.pretty:
        print(json.dumps(output, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(output, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
