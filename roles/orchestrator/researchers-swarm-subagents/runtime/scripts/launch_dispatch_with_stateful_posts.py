#!/usr/bin/env python3
from __future__ import annotations

"""Execute a Telegram persistent-lane dispatch end-to-end with immediate state patching.

Canonical runtime behavior:
1. bootstrap/reuse controller + persona topics
2. materialize each persona topic session and deliver the assignment via `sessions.send`
3. immediately patch each successful handoff to `running` via `update_research_run.py`
4. let `update_research_run.py` auto-post visible STARTING markers from stored metadata
5. ensure the Telegram swarm runtime loop is running once research begins
6. return a delivery summary with per-run patch outcomes

This removes normal-path dependence on a later/manual replay step. Replay/finalize
helpers remain available as repair/backstop tools.

Important runtime note:
- internal handoff execution is performed through the bundled Node helper
  `openclaw_sessions_send.mjs`, which calls the confirmed Gateway RPC
  method `sessions.send`
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = BASE_DIR.parent
PIPELINE_DIR = RUNTIME_DIR.parent
WORKSPACE_ROOT = PIPELINE_DIR.parents[2]
BOOTSTRAP_TOPICS = BASE_DIR / "internal" / "bootstrap_telegram_topics.py"
RUNTIME_HELPER = BASE_DIR / "internal" / "runtime_execute_dispatch.py"
UPDATE_RUN = BASE_DIR / "update_research_run.py"
SESSIONS_SEND_HELPER = BASE_DIR / "internal" / "openclaw_sessions_send.mjs"
LOG_LEARNING_INTERVENTIONS = WORKSPACE_ROOT / "roles" / "evaluator" / "runtime" / "scripts" / "log_learning_intervention_application.py"
LOG_PROPOSED_CAUSAL_SHADOW_MATCHES = WORKSPACE_ROOT / "roles" / "evaluator" / "runtime" / "scripts" / "log_proposed_causal_shadow_matches.py"
LOG_PROPOSED_CAUSAL_TRIAL_EXPOSURES = WORKSPACE_ROOT / "roles" / "evaluator" / "runtime" / "scripts" / "log_proposed_causal_trial_exposure.py"
LOG_LMD_BUNDLE_EXPOSURES = WORKSPACE_ROOT / "roles" / "evaluator" / "runtime" / "scripts" / "log_lmd_bundle_exposure.py"
WRITE_LMD_CAUSAL_AUDIT = WORKSPACE_ROOT / "roles" / "evaluator" / "runtime" / "scripts" / "write_lmd_causal_dispatch_audit.py"
TRIGGER_POST_TREATMENT_FEEDBACK = WORKSPACE_ROOT / "roles" / "evaluator" / "runtime" / "scripts" / "trigger_post_treatment_feedback_cycle.py"
RUNTIME_LOOP = BASE_DIR / "run_telegram_swarm_runtime_loop.py"
STATE_DIR = BASE_DIR / ".runtime-state"
RUNTIME_LOOP_PID = STATE_DIR / "telegram_swarm_runtime_loop.pid"
RUNTIME_LOOP_ERROR = STATE_DIR / "telegram_swarm_runtime_loop.error.json"
DEFAULT_ENV_PATH = WORKSPACE_ROOT / ".env"


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
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch a dispatch with immediate running-state patching")
    parser.add_argument("--manifest-path", required=True, help="Dispatch manifest JSON path")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def parse_json_lines(raw: str) -> dict[str, Any]:
    stdout = (raw or "").strip()
    if not stdout:
        return {}
    try:
        parsed = json.loads(stdout)
        if isinstance(parsed, dict):
            return parsed
        raise RuntimeError(f"expected top-level JSON object, got {type(parsed).__name__}")
    except json.JSONDecodeError:
        pass
    for line in reversed([line for line in stdout.splitlines() if line.strip()]):
        try:
            parsed = json.loads(line)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            continue
    raise RuntimeError("unable to parse JSON object from command output")


def python_json(script: Path, args: list[str]) -> dict[str, Any]:
    proc = subprocess.run([sys.executable, str(script), *args], text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"{script.name} failed")
    return parse_json_lines(proc.stdout)



def summarize_logging_result(payload: dict[str, Any] | None) -> dict[str, Any]:
    data = payload or {}
    counts = {
        'inserted': 0,
        'updated': 0,
        'existing': 0,
        'skipped': 0,
    }
    rows: list[dict[str, Any]] = []
    for key in ['rows', 'matches', 'candidates', 'applications']:
        values = data.get(key) or []
        if isinstance(values, list) and values:
            rows = [row for row in values if isinstance(row, dict)]
            break
    for row in rows:
        status = str((row or {}).get('status') or '')
        if 'insert' in status:
            counts['inserted'] += 1
        elif 'update' in status:
            counts['updated'] += 1
        elif 'existing' in status:
            counts['existing'] += 1
        elif 'skip' in status or 'dry_run' in status:
            counts['skipped'] += 1
        elif 'upsert' in status:
            counts['updated'] += 1
    counts['logged_rows'] = int(data.get('logged_rows') or data.get('logged_count') or len(rows))
    counts['candidate_count'] = int(data.get('candidate_count') or data.get('candidate_count_considered') or data.get('proposal_count_considered') or len(rows))
    return counts



def load_manifest(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def manifest_run_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    runs = manifest.get("runs") or manifest.get("persona_runs") or []
    return {
        run["research_run_id"]: run
        for run in runs
        if isinstance(run, dict) and isinstance(run.get("research_run_id"), str)
    }


def sessions_send(payload: dict[str, Any]) -> dict[str, Any]:
    payload_json = json.dumps(payload, separators=(",", ":"))
    proc = subprocess.run(
        ["node", str(SESSIONS_SEND_HELPER), "--payload-json", payload_json],
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "sessions.send helper failed")
    return parse_json_lines(proc.stdout)


def send_visible_telegram_message(*, chat_id: str, topic_id: str, message: str) -> dict[str, Any]:
    proc = subprocess.run(
        [
            'openclaw', 'message', 'send',
            '--channel', 'telegram',
            '--target', str(chat_id),
            '--thread-id', str(topic_id),
            '--message', message,
            '--json',
        ],
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or 'telegram visible send failed')
    return parse_json_lines(proc.stdout)


def apply_patch(patch_payload: dict[str, Any], db_url: str) -> dict[str, Any]:
    cmd = [
        sys.executable,
        str(UPDATE_RUN),
        "--research-run-id", patch_payload["research_run_id"],
        "--status", patch_payload["status"],
        "--workspace-note-path", patch_payload["workspace_note_path"],
        "--notes-json", json.dumps(patch_payload.get("notes", {}), separators=(",", ":")),
    ]
    if patch_payload.get("mark_started"):
        cmd.append("--mark-started")
    if db_url:
        cmd.extend(["--db-url", db_url])
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "update_research_run.py failed")
    return parse_json_lines(proc.stdout)


def log_learning_intervention_applications(*, case_key: str, research_run_id: str, notes: dict[str, Any], db_url: str) -> dict[str, Any] | None:
    intervention_keys = [str(item) for item in (notes.get("learning_intervention_keys") or []) if str(item).strip()]
    intervention_paths = [str(item) for item in (notes.get("learning_intervention_paths") or []) if str(item).strip()]
    if not intervention_keys and not intervention_paths:
        return None
    if not LOG_LEARNING_INTERVENTIONS.exists():
        raise RuntimeError(f"learning intervention logger missing: {LOG_LEARNING_INTERVENTIONS}")

    cmd = [
        sys.executable,
        str(LOG_LEARNING_INTERVENTIONS),
        "--case-key", case_key,
        "--research-run-id", research_run_id,
        "--application-surface", str(notes.get("learning_intervention_application_surface") or "researcher_prompt"),
        "--dispatch-id", str(notes.get("dispatch_id") or ""),
        "--notes-json", json.dumps({
            "runtime_surface": notes.get("runtime_surface"),
            "persona": notes.get("persona"),
            "dispatch_id": notes.get("dispatch_id"),
            "learning_interventions_used": notes.get("learning_interventions_used", False),
            "learning_intervention_required_checks": notes.get("learning_intervention_required_checks") or [],
            "qmd_used": notes.get("qmd_used", False),
            "qmd_bundle_path": notes.get("qmd_bundle_path"),
        }, separators=(",", ":")),
    ]
    bundle_path = str(notes.get("learning_intervention_bundle_path") or "").strip()
    if bundle_path:
        cmd.extend(["--bundle-path", bundle_path])
    for item in intervention_keys:
        cmd.extend(["--intervention-key", item])
    for item in intervention_paths:
        cmd.extend(["--intervention-path", item])
    if db_url:
        cmd.extend(["--db-url", db_url])

    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "log_learning_intervention_application.py failed")
    return parse_json_lines(proc.stdout)


def log_proposed_causal_shadow_matches(*, case_key: str, research_run_id: str, notes: dict[str, Any], db_url: str) -> dict[str, Any] | None:
    bundle_path = str(notes.get("lmd_bundle_path") or "").strip()
    dispatch_id = str(notes.get("dispatch_id") or "").strip()
    if not bundle_path or not dispatch_id:
        return None
    if not LOG_PROPOSED_CAUSAL_SHADOW_MATCHES.exists():
        raise RuntimeError(f"shadow logger missing: {LOG_PROPOSED_CAUSAL_SHADOW_MATCHES}")

    cmd = [
        sys.executable,
        str(LOG_PROPOSED_CAUSAL_SHADOW_MATCHES),
        "--case-key", case_key,
        "--dispatch-id", dispatch_id,
        "--research-run-id", research_run_id,
        "--bundle-path", bundle_path,
        "--experiment-id", str(notes.get("lmd_experiment_id") or ""),
        "--notes-json", json.dumps({
            "runtime_surface": notes.get("runtime_surface"),
            "trigger_persona": notes.get("persona"),
            "dispatch_id": dispatch_id,
            "lmd_used": notes.get("lmd_used", False),
            "lmd_bundle_status": notes.get("lmd_bundle_status"),
            "lmd_assignment_arm": notes.get("lmd_experiment_arm"),
            "lmd_tier": notes.get("lmd_tier"),
            "lmd_required_checks": notes.get("lmd_required_checks") or [],
            "qmd_used": notes.get("qmd_used", False),
            "qmd_bundle_path": notes.get("qmd_bundle_path"),
        }, separators=(",", ":")),
    ]
    if db_url:
        cmd.extend(["--db-url", db_url])

    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "log_proposed_causal_shadow_matches.py failed")
    return parse_json_lines(proc.stdout)



def log_proposed_causal_trial_exposures(*, case_key: str, research_run_id: str, notes: dict[str, Any], db_url: str) -> dict[str, Any] | None:
    bundle_path = str(notes.get("lmd_bundle_path") or "").strip()
    dispatch_id = str(notes.get("dispatch_id") or "").strip()
    if not bundle_path or not dispatch_id:
        return None
    if not LOG_PROPOSED_CAUSAL_TRIAL_EXPOSURES.exists():
        raise RuntimeError(f"trial exposure logger missing: {LOG_PROPOSED_CAUSAL_TRIAL_EXPOSURES}")

    cmd = [
        sys.executable,
        str(LOG_PROPOSED_CAUSAL_TRIAL_EXPOSURES),
        "--case-key", case_key,
        "--dispatch-id", dispatch_id,
        "--research-run-id", research_run_id,
        "--bundle-path", bundle_path,
        "--experiment-id", str(notes.get("lmd_experiment_id") or ""),
        "--experiment-arm", str(notes.get("lmd_experiment_arm") or ""),
        "--notes-json", json.dumps({
            "runtime_surface": notes.get("runtime_surface"),
            "trigger_persona": notes.get("persona"),
            "dispatch_id": dispatch_id,
            "trial_overlay_enabled": notes.get("trial_overlay_enabled", False),
            "trial_overlay_used": notes.get("trial_overlay_used", False),
            "trial_overlay_mode": notes.get("trial_overlay_mode"),
            "trial_overlay_preview_only": notes.get("trial_overlay_preview_only", True),
            "trial_overlay_selected_count": notes.get("trial_overlay_selected_count", 0),
            "trial_overlay_injected_count": notes.get("trial_overlay_injected_count", 0),
            "trial_overlay_candidate_ids": notes.get("trial_overlay_candidate_ids") or [],
            "lmd_used": notes.get("lmd_used", False),
            "lmd_tier": notes.get("lmd_tier"),
            "lmd_required_checks": notes.get("lmd_required_checks") or [],
            "qmd_used": notes.get("qmd_used", False),
            "qmd_bundle_path": notes.get("qmd_bundle_path"),
        }, separators=(",", ":")),
    ]
    if db_url:
        cmd.extend(["--db-url", db_url])

    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "log_proposed_causal_trial_exposure.py failed")
    return parse_json_lines(proc.stdout)



def log_lmd_bundle_exposures(*, case_key: str, research_run_id: str, notes: dict[str, Any], db_url: str) -> dict[str, Any] | None:
    if not notes.get("lmd_used"):
        return None
    bundle_path = str(notes.get("lmd_bundle_path") or "").strip()
    dispatch_id = str(notes.get("dispatch_id") or "").strip()
    if not bundle_path or not dispatch_id:
        return None
    if not LOG_LMD_BUNDLE_EXPOSURES.exists():
        raise RuntimeError(f"lmd exposure logger missing: {LOG_LMD_BUNDLE_EXPOSURES}")

    cmd = [
        sys.executable,
        str(LOG_LMD_BUNDLE_EXPOSURES),
        "--case-key", case_key,
        "--dispatch-id", dispatch_id,
        "--research-run-id", research_run_id,
        "--bundle-path", bundle_path,
        "--experiment-id", str(notes.get("lmd_experiment_id") or ""),
        "--arm", str(notes.get("lmd_experiment_arm") or ""),
        "--generator-version", str(notes.get("lmd_generator_version") or ""),
        "--policy-version", str(notes.get("lmd_policy_version") or ""),
        "--notes-json", json.dumps({
            "runtime_surface": notes.get("runtime_surface"),
            "persona": notes.get("persona"),
            "dispatch_id": dispatch_id,
            "lmd_used": notes.get("lmd_used", False),
            "lmd_tier": notes.get("lmd_tier"),
            "lmd_required_checks": notes.get("lmd_required_checks") or [],
            "qmd_used": notes.get("qmd_used", False),
            "qmd_bundle_path": notes.get("qmd_bundle_path"),
        }, separators=(",", ":")),
    ]
    if db_url:
        cmd.extend(["--db-url", db_url])

    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "log_lmd_bundle_exposure.py failed")
    return parse_json_lines(proc.stdout)



def write_lmd_causal_dispatch_audit(*, case_key: str, research_run_id: str, notes: dict[str, Any], shadow_logging: dict[str, Any] | None, trial_exposure_logging: dict[str, Any] | None, lmd_exposure_logging: dict[str, Any] | None, post_treatment_feedback: dict[str, Any] | None) -> dict[str, Any] | None:
    bundle_path = str(notes.get("lmd_bundle_path") or "").strip()
    dispatch_id = str(notes.get("dispatch_id") or "").strip()
    if not bundle_path or not dispatch_id:
        return None
    if not WRITE_LMD_CAUSAL_AUDIT.exists():
        raise RuntimeError(f"lmd causal audit writer missing: {WRITE_LMD_CAUSAL_AUDIT}")
    return python_json(
        WRITE_LMD_CAUSAL_AUDIT,
        [
            "--case-key", case_key,
            "--dispatch-id", dispatch_id,
            "--research-run-id", research_run_id,
            "--bundle-path", bundle_path,
            "--notes-json", json.dumps({
                "runtime_surface": notes.get("runtime_surface"),
                "persona": notes.get("persona"),
                "dispatch_gate_status": notes.get("dispatch_gate_status") or {},
            }, separators=(",", ":")),
            "--shadow-logging-json", json.dumps(shadow_logging or {}, separators=(",", ":")),
            "--trial-logging-json", json.dumps(trial_exposure_logging or {}, separators=(",", ":")),
            "--lmd-logging-json", json.dumps(lmd_exposure_logging or {}, separators=(",", ":")),
            "--trigger-json", json.dumps(post_treatment_feedback or {}, separators=(",", ":")),
        ],
    )


def runtime_loop_status() -> dict[str, Any]:
    pid_file = RUNTIME_LOOP_PID
    if not pid_file.exists():
        return {"active": False}
    try:
        pid = int(pid_file.read_text().strip())
    except Exception:
        return {"active": False, "stale_pid_file": True}
    try:
        os.kill(pid, 0)
    except OSError:
        return {"active": False, "pid": pid, "stale_pid_file": True}
    return {"active": True, "pid": pid, "pid_file": str(pid_file)}


def ensure_runtime_loop(db_url: str) -> dict[str, Any]:
    status = runtime_loop_status()
    if status.get("active"):
        return {"status": "already_running", **status, "error_file": str(RUNTIME_LOOP_ERROR)}
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    if db_url:
        env.setdefault("PREDQUANT_ORCHESTRATOR_URL", db_url)
    cmd = [
        sys.executable,
        str(RUNTIME_LOOP),
        "--db-url", db_url,
        "--pid-file", str(RUNTIME_LOOP_PID),
        "--error-file", str(RUNTIME_LOOP_ERROR),
    ]
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        start_new_session=True,
        env=env,
    )
    return {
        "status": "started",
        "pid": proc.pid,
        "pid_file": str(RUNTIME_LOOP_PID),
        "error_file": str(RUNTIME_LOOP_ERROR),
    }


def main() -> int:
    maybe_load_workspace_env()
    args = parse_args()
    try:
        manifest_path = Path(args.manifest_path).expanduser().resolve()
        manifest = load_manifest(manifest_path)
        run_map = manifest_run_map(manifest)

        bootstrap = python_json(BOOTSTRAP_TOPICS, ["--manifest-path", str(manifest_path), "--apply"])
        steps = ((bootstrap.get("parallel_handoff_group") or {}).get("steps") or [])

        controller_topic = bootstrap.get('controller_topic') or {}
        controller_visible_messages = controller_topic.get('visible_launch_messages') or []
        controller_visible_results: list[dict[str, Any]] = []
        controller_chat_id = str(bootstrap.get('chat_id') or '')
        controller_topic_id = str(controller_topic.get('topic_id') or '')
        if controller_chat_id and controller_topic_id:
            for message in controller_visible_messages:
                if not str(message or '').strip():
                    continue
                controller_visible_results.append(
                    send_visible_telegram_message(chat_id=controller_chat_id, topic_id=controller_topic_id, message=str(message))
                )

        delivered_results: list[dict[str, Any]] = []
        failures: list[dict[str, Any]] = []
        shadow_logging = None
        shadow_logging_error = None
        shadow_logging_done = False
        trial_exposure_logging = None
        trial_exposure_logging_error = None
        trial_exposure_logging_done = False
        post_treatment_feedback = None
        post_treatment_feedback_error = None
        post_treatment_feedback_done = False

        for step in steps:
            research_run_id = step["research_run_id"]
            persona = step["persona"]
            internal = step.get("internal_handoff_step") or {}
            payload = internal.get("payload")
            delivered_template = dict(step.get("delivered_result_template") or {})
            run_info = run_map.get(research_run_id) or {}

            if not payload:
                failures.append({
                    "research_run_id": research_run_id,
                    "persona": persona,
                    "status": "failed",
                    "error": "missing_sessions_send_payload",
                })
                continue

            try:
                send_result = sessions_send(payload)
                run_status = send_result.get("status")
                if run_status not in {"ok", "done", "success", "timeout", "started"}:
                    raise RuntimeError(f"unexpected sessions_send status: {run_status}")

                target_session_key = payload.get("sessionKey")
                if not target_session_key:
                    raise RuntimeError("sessions_send payload missing sessionKey")

                patch_payload = python_json(
                    RUNTIME_HELPER,
                    [
                        "--file", str(manifest_path),
                        "--action", "build-patch",
                        "--research-run-id", research_run_id,
                        "--target-session-key", target_session_key,
                        "--delivery-chat-id", delivered_template.get("delivery_chat_id") or "",
                        "--delivery-topic-id", delivered_template.get("delivery_topic_id") or "",
                        "--delivery-topic-title", delivered_template.get("delivery_topic_title") or "",
                        "--controller-topic-id", delivered_template.get("controller_topic_id") or "",
                        "--controller-topic-title", delivered_template.get("controller_topic_title") or "",
                    ],
                )
                patch_result = apply_patch(patch_payload, args.db_url)

                logging_notes = {
                    **(patch_payload.get("notes") or {}),
                    "persona": persona,
                }
                case_key = str((manifest.get("case") or {}).get("case_key") or "")

                if not shadow_logging_done:
                    try:
                        shadow_logging = log_proposed_causal_shadow_matches(
                            case_key=case_key,
                            research_run_id=research_run_id,
                            notes=logging_notes,
                            db_url=args.db_url,
                        )
                    except Exception as shadow_exc:  # noqa: BLE001
                        shadow_logging_error = str(shadow_exc)
                    shadow_logging_done = True

                if not trial_exposure_logging_done:
                    try:
                        trial_exposure_logging = log_proposed_causal_trial_exposures(
                            case_key=case_key,
                            research_run_id=research_run_id,
                            notes=logging_notes,
                            db_url=args.db_url,
                        )
                    except Exception as trial_exc:  # noqa: BLE001
                        trial_exposure_logging_error = str(trial_exc)
                    trial_exposure_logging_done = True

                intervention_logging = None
                intervention_logging_error = None
                try:
                    intervention_logging = log_learning_intervention_applications(
                        case_key=case_key,
                        research_run_id=research_run_id,
                        notes=logging_notes,
                        db_url=args.db_url,
                    )
                except Exception as intervention_exc:  # noqa: BLE001
                    intervention_logging_error = str(intervention_exc)

                lmd_exposure_logging = None
                lmd_exposure_logging_error = None
                try:
                    lmd_exposure_logging = log_lmd_bundle_exposures(
                        case_key=case_key,
                        research_run_id=research_run_id,
                        notes=logging_notes,
                        db_url=args.db_url,
                    )
                except Exception as lmd_exc:  # noqa: BLE001
                    lmd_exposure_logging_error = str(lmd_exc)

                if not post_treatment_feedback_done:
                    try:
                        post_treatment_feedback = python_json(
                            TRIGGER_POST_TREATMENT_FEEDBACK,
                            [
                                "--case-key", case_key,
                                "--dispatch-id", str(logging_notes.get("dispatch_id") or ""),
                                "--trigger-source", "launch_dispatch_with_stateful_posts",
                                "--repair-missing-logs",
                                "--db-url", args.db_url,
                            ],
                        )
                    except Exception as feedback_exc:  # noqa: BLE001
                        post_treatment_feedback_error = str(feedback_exc)
                    post_treatment_feedback_done = True

                lmd_causal_audit = None
                lmd_causal_audit_error = None
                try:
                    lmd_causal_audit = write_lmd_causal_dispatch_audit(
                        case_key=case_key,
                        research_run_id=research_run_id,
                        notes=logging_notes,
                        shadow_logging=shadow_logging,
                        trial_exposure_logging=trial_exposure_logging,
                        lmd_exposure_logging=lmd_exposure_logging,
                        post_treatment_feedback=post_treatment_feedback,
                    )
                except Exception as audit_exc:  # noqa: BLE001
                    lmd_causal_audit_error = str(audit_exc)

                delivered = dict(delivered_template)
                delivered.update(
                    {
                        "status": "delivered",
                        "target_session_key": target_session_key,
                        "workspace_note_path": run_info.get("workspace_note_path"),
                        "sessions_send_result": send_result,
                        "patch_result": patch_result,
                        "shadow_logging": shadow_logging,
                        "shadow_logging_error": shadow_logging_error,
                        "shadow_logging_summary": summarize_logging_result(shadow_logging),
                        "trial_exposure_logging": trial_exposure_logging,
                        "trial_exposure_logging_error": trial_exposure_logging_error,
                        "trial_exposure_logging_summary": summarize_logging_result(trial_exposure_logging),
                        "intervention_logging": intervention_logging,
                        "intervention_logging_error": intervention_logging_error,
                        "intervention_logging_summary": summarize_logging_result(intervention_logging),
                        "lmd_exposure_logging": lmd_exposure_logging,
                        "lmd_exposure_logging_error": lmd_exposure_logging_error,
                        "lmd_exposure_logging_summary": summarize_logging_result(lmd_exposure_logging),
                        "post_treatment_feedback": post_treatment_feedback,
                        "post_treatment_feedback_error": post_treatment_feedback_error,
                        "lmd_causal_audit": lmd_causal_audit,
                        "lmd_causal_audit_error": lmd_causal_audit_error,
                    }
                )
                delivered_results.append(delivered)
            except Exception as exc:  # noqa: BLE001
                failures.append(
                    {
                        "research_run_id": research_run_id,
                        "persona": persona,
                        "status": "failed",
                        "workspace_note_path": run_info.get("workspace_note_path"),
                        "error": str(exc),
                    }
                )

        summary = python_json(
            RUNTIME_HELPER,
            [
                "--file", str(manifest_path),
                "--action", "finalize-summary",
                "--run-results-json", json.dumps(delivered_results + failures, separators=(",", ":")),
            ],
        )

        runtime_loop = None
        if delivered_results:
            runtime_loop = ensure_runtime_loop(args.db_url)

        result = {
            "status": "ok",
            "manifest_path": str(manifest_path),
            "bootstrap": bootstrap,
            "controller_visible_results": controller_visible_results,
            "delivered_results": delivered_results,
            "failures": failures,
            "summary": summary,
            "runtime_loop": runtime_loop,
            "post_treatment_feedback": post_treatment_feedback,
            "post_treatment_feedback_error": post_treatment_feedback_error,
        }
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(result, separators=(",", ":"), default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
