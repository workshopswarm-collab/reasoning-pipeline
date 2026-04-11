#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fcntl
import json
import os
import subprocess
import sys
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "scripts"))

from automation_control import DEFAULT_CONTROL_FILE, load_control_file, resolve_sequencer_policy  # noqa: E402
from case_pipeline_status import list_case_pipeline_statuses, pipeline_status_path, summarize_case_pipeline_status, update_case_pipeline_status  # noqa: E402

PREPARE_AND_LAUNCH = REPO_ROOT / "roles" / "orchestrator" / "researchers-swarm-subagents" / "runtime" / "scripts" / "prepare_and_launch_headless_telegram_dispatch.py"
RESUME_SWARM_STAGE = REPO_ROOT / "roles" / "orchestrator" / "researchers-swarm-subagents" / "runtime" / "scripts" / "resume_swarm_stage.py"
LAUNCH_SYNTHESIS_IF_READY = REPO_ROOT / "roles" / "orchestrator" / "synthesis-subagent" / "runtime" / "scripts" / "launch_synthesis_if_ready.py"
RUN_DECISION_MAKER = REPO_ROOT / "roles" / "decision-maker" / "runtime" / "scripts" / "run_decision_maker.py"
DEFAULT_LOCK = REPO_ROOT / "scripts" / ".runtime-state" / "pipeline-sequencer.lock"
NO_WORK_MARKERS = (
    'no eligible market found',
    'pipeline already busy with an open researching case',
)


class RunnerError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the reasoning pipeline sequentially over available markets")
    parser.add_argument("--max-cases", type=int, default=1, help="Maximum number of markets to process; use 0 to run until no more are available")
    parser.add_argument("--poll-seconds", type=float, default=15.0, help="Polling interval while watching pipeline status")
    parser.add_argument("--idle-seconds", type=float, default=60.0, help="Sleep interval between loop passes when idle/disabled")
    parser.add_argument("--max-case-seconds", type=float, default=7200.0, help="Maximum seconds to wait for one case before failing")
    parser.add_argument("--resume-existing", action="store_true", default=True, help="Resume the most recently updated non-terminal case before claiming a new one")
    parser.add_argument("--no-resume-existing", dest="resume_existing", action="store_false", help="Do not resume an existing non-terminal case")
    parser.add_argument("--loop", action="store_true", help="Run continuously instead of a single pass")
    parser.add_argument("--control-managed", action="store_true", help="Load sequencer behavior from the persisted automation control file each pass")
    parser.add_argument("--control-file", default=str(DEFAULT_CONTROL_FILE), help="Automation control file path used with --control-managed")
    parser.add_argument("--lock-file", default=str(DEFAULT_LOCK), help="Process lock to prevent concurrent sequencer loops")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def load_repo_env() -> dict[str, str]:
    env = dict(os.environ)
    env_file = REPO_ROOT / ".env"
    if not env_file.exists():
        return env
    for raw_line in env_file.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in env:
            env[key] = value
    return env


@contextmanager
def process_lock(path: Path) -> Iterator[None]:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+', encoding='utf-8') as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:  # noqa: PERF203
            raise RunnerError(f'another sequencer instance already holds {path}') from exc
        try:
            handle.seek(0)
            handle.truncate()
            handle.write(str(os.getpid()))
            handle.flush()
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def effective_sequencer_policy(args: argparse.Namespace) -> dict[str, Any]:
    policy = {
        'enabled': True,
        'resume_existing': bool(args.resume_existing),
        'allow_new_case_claims': True,
        'poll_seconds': float(args.poll_seconds),
        'idle_seconds': float(args.idle_seconds),
        'max_case_seconds': float(args.max_case_seconds),
        'control_managed': bool(args.control_managed),
        'control_file': str(Path(args.control_file).expanduser().resolve()),
    }
    if args.control_managed:
        control = load_control_file(Path(args.control_file).expanduser().resolve())
        control_policy = resolve_sequencer_policy(control)
        policy.update({
            'enabled': bool(control_policy.get('enabled')),
            'resume_existing': bool(control_policy.get('resume_existing')),
            'allow_new_case_claims': bool(control_policy.get('allow_new_case_claims')),
            'poll_seconds': float(control_policy.get('poll_seconds')),
            'idle_seconds': float(control_policy.get('idle_seconds')),
            'max_case_seconds': float(control_policy.get('max_case_seconds')),
            'control_snapshot': control,
            'automation_enabled': bool(control_policy.get('automation_enabled')),
        })
    return policy


def run_json_command(cmd: list[str]) -> tuple[int, dict[str, Any], str, str]:
    proc = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True, env=load_repo_env())
    payload: dict[str, Any] = {}
    text = (proc.stdout or "").strip()
    if text:
        try:
            parsed = json.loads(text)
            if isinstance(parsed, dict):
                payload = parsed
        except json.JSONDecodeError:
            payload = {}
    return proc.returncode, payload, proc.stdout, proc.stderr


def prepare_and_launch_case(pretty: bool) -> dict[str, Any] | None:
    cmd = [sys.executable, str(PREPARE_AND_LAUNCH)]
    if pretty:
        cmd.append("--pretty")
    code, payload, stdout, stderr = run_json_command(cmd)
    if code != 0:
        if payload:
            return {"ok": False, "payload": payload, "stdout": stdout, "stderr": stderr, "returncode": code}
        return None
    return {"ok": True, "payload": payload, "stdout": stdout, "stderr": stderr, "returncode": code}


def launch_decision_maker(case_key: str, pretty: bool) -> dict[str, Any]:
    cmd = [sys.executable, str(RUN_DECISION_MAKER), "--case-key", case_key]
    if pretty:
        cmd.append("--pretty")
    code, payload, stdout, stderr = run_json_command(cmd)
    return {
        "ok": code == 0,
        "payload": payload,
        "stdout": stdout,
        "stderr": stderr,
        "returncode": code,
    }


def resume_swarm_stage(case_key: str, pretty: bool) -> dict[str, Any]:
    cmd = [sys.executable, str(RESUME_SWARM_STAGE), '--case-key', case_key]
    if pretty:
        cmd.append('--pretty')
    code, payload, stdout, stderr = run_json_command(cmd)
    return {
        'ok': code == 0,
        'payload': payload,
        'stdout': stdout,
        'stderr': stderr,
        'returncode': code,
    }


def latest_dispatch_dir(case_key: str) -> Path | None:
    analyses_root = REPO_ROOT / "qualitative-db" / "40-research" / "cases" / case_key / "researcher-analyses"
    if not analyses_root.exists():
        return None
    candidates = sorted(analyses_root.glob("*/dispatch-case-*"), key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0] if candidates else None


def synthesis_status_file(case_key: str) -> Path | None:
    dispatch_dir = latest_dispatch_dir(case_key)
    if dispatch_dir is None:
        return None
    path = dispatch_dir / "synthesis-stage-status.json"
    return path if path.exists() else None


def launch_synthesis_if_needed(case_key: str, pretty: bool) -> dict[str, Any] | None:
    status_file = synthesis_status_file(case_key)
    if status_file is None:
        return None
    cmd = [sys.executable, str(LAUNCH_SYNTHESIS_IF_READY), "--status-file", str(status_file)]
    if pretty:
        cmd.append("--pretty")
    code, payload, stdout, stderr = run_json_command(cmd)
    return {
        "ok": code == 0,
        "payload": payload,
        "stdout": stdout,
        "stderr": stderr,
        "returncode": code,
        "status_file": str(status_file.relative_to(REPO_ROOT)),
    }


def wait_for_case(case_key: str, *, poll_seconds: float, max_case_seconds: float, pretty: bool) -> dict[str, Any]:
    path = pipeline_status_path(case_key)
    deadline = time.time() + max_case_seconds
    decision_launched = False
    decision_launch_result: dict[str, Any] | None = None
    swarm_resume_attempts = 0
    last_swarm_resume_result: dict[str, Any] | None = None
    synthesis_launch_attempts = 0
    last_synthesis_launch_result: dict[str, Any] | None = None

    while time.time() < deadline:
        summary = summarize_case_pipeline_status(case_key)
        stage_statuses = summary.get("stage_statuses") or {}
        status = summary.get("status") or ""

        if pretty:
            print(json.dumps({
                "case_key": case_key,
                "pipeline_status_path": summary.get("path"),
                "status": status,
                "current_stage": summary.get("current_stage"),
                "stage_statuses": stage_statuses,
            }, indent=2))

        if (
            stage_statuses.get("swarm") in {"pending", "in_progress", "failed", ""}
            and stage_statuses.get("synthesis") != "completed"
            and stage_statuses.get("decision") in {"pending", ""}
        ):
            swarm_result = resume_swarm_stage(case_key, pretty=pretty)
            last_swarm_resume_result = swarm_result
            swarm_resume_attempts += 1
            if not swarm_result.get('ok'):
                return {
                    'ok': False,
                    'case_key': case_key,
                    'error': 'swarm_resume_failed',
                    'swarm_resume_result': swarm_result,
                    'pipeline_summary': summarize_case_pipeline_status(case_key),
                }

        if (
            stage_statuses.get("synthesis") != "completed"
            and stage_statuses.get("decision") in {"pending", ""}
        ):
            synth_result = launch_synthesis_if_needed(case_key, pretty=pretty)
            if synth_result is not None:
                last_synthesis_launch_result = synth_result
                synthesis_launch_attempts += 1
                payload = synth_result.get("payload") or {}
                launch_status = str(payload.get("status") or "")
                if synth_result.get("returncode") != 0 and launch_status not in {"not_ready", "already_running", "already_completed"}:
                    return {
                        "ok": False,
                        "case_key": case_key,
                        "error": "synthesis_launch_failed",
                        "synthesis_launch_result": synth_result,
                        "pipeline_summary": summarize_case_pipeline_status(case_key),
                    }

        if (
            stage_statuses.get("synthesis") == "completed"
            and stage_statuses.get("decision") in {"pending", ""}
            and not decision_launched
        ):
            decision_launch_result = launch_decision_maker(case_key, pretty=pretty)
            decision_launched = True
            if not decision_launch_result.get("ok"):
                return {
                    "ok": False,
                    "case_key": case_key,
                    "error": "decision_maker_launch_failed",
                    "decision_launch_result": decision_launch_result,
                    "pipeline_summary": summarize_case_pipeline_status(case_key),
                }

        if status in {"pipeline_completed", "pipeline_failed", "pipeline_skipped"}:
            return {
                "ok": status == "pipeline_completed",
                "case_key": case_key,
                "pipeline_summary": summary,
                "decision_launch_result": decision_launch_result or {},
                "swarm_resume_attempts": swarm_resume_attempts,
                "last_swarm_resume_result": last_swarm_resume_result or {},
                "synthesis_launch_attempts": synthesis_launch_attempts,
                "last_synthesis_launch_result": last_synthesis_launch_result or {},
            }

        time.sleep(poll_seconds)

    return {
        "ok": False,
        "case_key": case_key,
        "error": "pipeline_timeout",
        "pipeline_summary": summarize_case_pipeline_status(case_key),
        "pipeline_status_path": str(path),
        "swarm_resume_attempts": swarm_resume_attempts,
        "last_swarm_resume_result": last_swarm_resume_result or {},
        "synthesis_launch_attempts": synthesis_launch_attempts,
        "last_synthesis_launch_result": last_synthesis_launch_result or {},
        "decision_launch_result": decision_launch_result or {},
    }


def pick_resumable_case() -> dict[str, Any] | None:
    active = list_case_pipeline_statuses(include_terminal=False)
    return active[0] if active else None


def classify_prepare_failure(prepared: dict[str, Any] | None) -> str:
    if prepared is None:
        return 'prepare_unknown_failure'
    payload = prepared.get('payload') or {}
    combined = '\n'.join([
        str(payload.get('status') or ''),
        str((payload.get('prepare_result') or {}).get('status') or ''),
        str(prepared.get('stdout') or ''),
        str(prepared.get('stderr') or ''),
        str(payload.get('prepare_stdout') or ''),
        str(payload.get('prepare_stderr') or ''),
    ]).lower()
    if 'pipeline already busy with an open researching case' in combined:
        return 'idle_pipeline_busy'
    if 'no eligible market found' in combined:
        return 'idle_no_eligible_market'
    return 'prepare_launch_failed'


def run_sequencer_pass(args: argparse.Namespace, policy: dict[str, Any]) -> dict[str, Any]:
    if not policy.get('enabled', True):
        return {
            'ok': True,
            'status': 'sequencer_disabled',
            'policy': policy,
        }

    resumable = pick_resumable_case() if policy.get('resume_existing') else None
    if resumable:
        case_key = str(resumable.get("case_key") or "").strip()
        if not case_key:
            raise RunnerError("resumable pipeline status is missing case_key")
        update_case_pipeline_status(
            case_key=case_key,
            dispatch_id=str(resumable.get("dispatch_id") or "").strip(),
            market_id=str(resumable.get("market_id") or "").strip(),
            market_title=str(resumable.get("market_title") or "").strip(),
            status=str(resumable.get("status") or "pipeline_in_progress"),
            current_stage=str(resumable.get("current_stage") or "swarm"),
            runner_id="run_sequential_market_pipeline",
            message="Sequential runner resumed existing in-flight case",
        )
        case_result = wait_for_case(
            case_key,
            poll_seconds=float(policy['poll_seconds']),
            max_case_seconds=float(policy['max_case_seconds']),
            pretty=args.pretty,
        )
        return {
            'ok': bool(case_result.get('ok')),
            'status': 'processed_existing_case',
            'policy': policy,
            'case_key': case_key,
            'case_result': case_result,
        }

    if not policy.get('allow_new_case_claims', False):
        return {
            'ok': True,
            'status': 'claims_disabled_idle',
            'policy': policy,
        }

    prepared = prepare_and_launch_case(pretty=args.pretty)
    if not prepared:
        return {
            'ok': False,
            'status': 'prepare_unknown_failure',
            'policy': policy,
        }

    payload = prepared.get("payload") or {}
    if not prepared.get("ok"):
        failure_kind = classify_prepare_failure(prepared)
        idle = failure_kind in {'idle_pipeline_busy', 'idle_no_eligible_market'}
        return {
            'ok': idle,
            'status': failure_kind,
            'policy': policy,
            'prepare_result': prepared,
        }

    prepare_result = payload.get("prepare_result") or {}
    case_payload = prepare_result.get("case") or {}
    market_payload = prepare_result.get("market") or {}
    dispatch_payload = prepare_result.get("dispatch") or {}
    case_key = str(case_payload.get("case_id") or "").strip()
    if not case_key:
        raise RunnerError("prepare_and_launch did not return a case_id")

    update_case_pipeline_status(
        case_key=case_key,
        dispatch_id=str(dispatch_payload.get("dispatch_id") or "").strip(),
        market_id=str(market_payload.get("market_id") or "").strip(),
        market_title=str(market_payload.get("market_title") or "").strip(),
        status="pipeline_started",
        current_stage="swarm",
        stage_status_patch={
            "dispatch": "launched",
            "swarm": "in_progress",
            "synthesis": "pending",
            "decision": "pending",
        },
        runner_id="run_sequential_market_pipeline",
        message="Sequential runner claimed case and is waiting for synthesis completion",
    )

    case_result = wait_for_case(
        case_key,
        poll_seconds=float(policy['poll_seconds']),
        max_case_seconds=float(policy['max_case_seconds']),
        pretty=args.pretty,
    )
    return {
        'ok': bool(case_result.get('ok')),
        'status': 'processed_new_case',
        'policy': policy,
        'case_key': case_key,
        'prepare_result': prepared,
        'case_result': case_result,
    }


def should_count_processed(result: dict[str, Any]) -> bool:
    return str(result.get('status') or '') in {'processed_existing_case', 'processed_new_case'}


def single_pass_summary(result: dict[str, Any]) -> dict[str, Any]:
    return {
        'ok': bool(result.get('ok')),
        'processed_cases': 1 if should_count_processed(result) else 0,
        'results': [result],
    }


def loop_pass_payload(result: dict[str, Any], processed_cases: int) -> dict[str, Any]:
    return {
        'ok': bool(result.get('ok')),
        'processed_cases': processed_cases,
        'pass_result': result,
    }


def main() -> None:
    args = parse_args()
    lock_path = Path(args.lock_file).expanduser().resolve()
    with process_lock(lock_path):
        if not args.loop:
            result = run_sequencer_pass(args, effective_sequencer_policy(args))
            summary = single_pass_summary(result)
            print(json.dumps(summary, indent=2 if args.pretty else None))
            if not summary['ok']:
                raise SystemExit(1)
            return

        processed = 0
        while args.max_cases == 0 or processed < args.max_cases:
            policy = effective_sequencer_policy(args)
            result = run_sequencer_pass(args, policy)
            if should_count_processed(result):
                processed += 1
            print(json.dumps(loop_pass_payload(result, processed), indent=2 if args.pretty else None), flush=True)
            if not result.get('ok'):
                raise SystemExit(1)
            if should_count_processed(result):
                continue
            time.sleep(float(policy.get('idle_seconds', args.idle_seconds)))


if __name__ == "__main__":
    main()
