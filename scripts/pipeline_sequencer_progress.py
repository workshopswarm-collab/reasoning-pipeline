from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any

from automation_control import load_control_file, resolve_watchdog_policy
from case_pipeline_status import pipeline_status_path, summarize_case_pipeline_status
from pipeline_automation_actions import watch_existing_case


TERMINAL_PIPELINE_STATUSES = {'pipeline_completed', 'pipeline_failed', 'pipeline_skipped'}


def resolve_internal_watchdog_policy(args: Any) -> dict[str, Any]:
    if args.control_managed:
        control_path = Path(args.control_file).expanduser().resolve()
        control = load_control_file(control_path)
        return {
            **resolve_watchdog_policy(control),
            'control_managed': True,
            'control_file': str(control_path),
            'control_snapshot': control,
        }
    return {
        'enabled': True,
        'apply': True,
        'allow_resume_swarm': True,
        'allow_launch_synthesis': True,
        'allow_launch_decision': True,
        'allow_finalize_decision': True,
        'allow_finalize_pipeline': True,
        'control_managed': False,
        'control_file': '',
    }


def wait_for_case(
    case_key: str,
    *,
    args: Any,
    poll_seconds: float,
    max_case_seconds: float,
    pretty: bool,
    progress_callback: Any | None = None,
) -> dict[str, Any]:
    path = pipeline_status_path(case_key)
    deadline = time.time() + max_case_seconds
    watchdog_passes = 0
    last_watchdog_result: dict[str, Any] | None = None
    watchdog_args = argparse.Namespace(stale_seconds=900.0, pretty=pretty)

    while time.time() < deadline:
        summary = summarize_case_pipeline_status(case_key)
        status = summary.get('status') or ''

        if pretty:
            print(json.dumps({
                'case_key': case_key,
                'pipeline_status_path': summary.get('path'),
                'status': status,
                'current_stage': summary.get('current_stage'),
                'stage_statuses': summary.get('stage_statuses') or {},
            }, indent=2))

        if progress_callback is not None:
            progress_callback(
                phase='monitor_case',
                message='Monitoring active case progress',
                case_key=case_key,
                market_id=str(summary.get('market_id') or '').strip(),
                dispatch_id=str(summary.get('dispatch_id') or '').strip(),
                details={
                    'pipeline_status': status,
                    'current_stage': str(summary.get('current_stage') or ''),
                    'stage_statuses': summary.get('stage_statuses') or {},
                    'watchdog_passes': watchdog_passes,
                },
            )

        if status in TERMINAL_PIPELINE_STATUSES:
            return {
                'ok': status == 'pipeline_completed',
                'case_key': case_key,
                'pipeline_summary': summary,
                'watchdog_passes': watchdog_passes,
                'last_watchdog_result': last_watchdog_result or {},
            }

        watchdog_policy = resolve_internal_watchdog_policy(args)
        last_watchdog_result = watch_existing_case(summary, args=watchdog_args, policy=watchdog_policy)
        watchdog_passes += 1
        action_failures = last_watchdog_result.get('action_failures') if isinstance(last_watchdog_result.get('action_failures'), list) else []
        if progress_callback is not None:
            after_for_progress = last_watchdog_result.get('after') if isinstance(last_watchdog_result.get('after'), dict) else summary
            executed_actions = last_watchdog_result.get('executed_actions') if isinstance(last_watchdog_result.get('executed_actions'), list) else []
            progress_callback(
                phase='watchdog_reconcile',
                message='Reconciling active case while waiting for terminal state',
                case_key=case_key,
                market_id=str(after_for_progress.get('market_id') or summary.get('market_id') or '').strip(),
                dispatch_id=str(after_for_progress.get('dispatch_id') or summary.get('dispatch_id') or '').strip(),
                details={
                    'watchdog_passes': watchdog_passes,
                    'pipeline_status': str(after_for_progress.get('status') or summary.get('status') or ''),
                    'current_stage': str(after_for_progress.get('current_stage') or summary.get('current_stage') or ''),
                    'stage_statuses': after_for_progress.get('stage_statuses') or summary.get('stage_statuses') or {},
                    'proposed_actions': last_watchdog_result.get('proposed_actions') or [],
                    'executed_actions': [
                        str((item.get('name') if isinstance(item, dict) else item) or '')
                        for item in executed_actions
                    ],
                    'action_failures': [
                        str(((item.get('name') if isinstance(item, dict) else item) or ''))
                        for item in action_failures
                    ],
                },
            )
        if action_failures:
            return {
                'ok': False,
                'case_key': case_key,
                'error': 'watchdog_action_failed',
                'watchdog_result': last_watchdog_result,
                'pipeline_summary': summarize_case_pipeline_status(case_key),
            }
        if not last_watchdog_result.get('ok', False):
            return {
                'ok': False,
                'case_key': case_key,
                'error': 'watchdog_reconcile_failed',
                'watchdog_result': last_watchdog_result,
                'pipeline_summary': summarize_case_pipeline_status(case_key),
            }

        after = last_watchdog_result.get('after') if isinstance(last_watchdog_result.get('after'), dict) else summarize_case_pipeline_status(case_key)
        after_status = str(after.get('status') or '')
        if after_status in TERMINAL_PIPELINE_STATUSES:
            return {
                'ok': after_status == 'pipeline_completed',
                'case_key': case_key,
                'pipeline_summary': after,
                'watchdog_passes': watchdog_passes,
                'last_watchdog_result': last_watchdog_result or {},
            }

        time.sleep(poll_seconds)

    return {
        'ok': False,
        'case_key': case_key,
        'error': 'pipeline_timeout',
        'pipeline_summary': summarize_case_pipeline_status(case_key),
        'pipeline_status_path': str(path),
        'watchdog_passes': watchdog_passes,
        'last_watchdog_result': last_watchdog_result or {},
    }
