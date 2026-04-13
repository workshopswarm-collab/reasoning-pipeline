#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / 'scripts') not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / 'scripts'))

from automation_control import DEFAULT_CONTROL_FILE, load_control_file, resolve_watchdog_policy  # noqa: E402
from automation_runtime_support import exclusive_lock  # noqa: E402
from case_pipeline_status import list_case_pipeline_statuses, summarize_case_pipeline_status, update_case_pipeline_status_with_followups as update_case_pipeline_status  # noqa: E402
from pipeline_automation_actions import (  # noqa: E402
    REPO_ROOT as ACTION_REPO_ROOT,
    finalize_decision,
    launch_decision_maker,
    launch_synthesis_if_needed,
    load_json_if_exists,
    reconcile_decision,
    reconcile_swarm,
    resume_swarm,
    synthesis_status_file,
)

DEFAULT_LOCK = REPO_ROOT / 'scripts' / '.runtime-state' / 'pipeline-watchdog.lock'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Watch active pipeline cases and conservatively reconcile existing in-flight work')
    parser.add_argument('--poll-seconds', type=float, default=60.0, help='Sleep interval between passes when looping')
    parser.add_argument('--stale-seconds', type=float, default=900.0, help='Staleness threshold forwarded to swarm reconciliation')
    parser.add_argument('--loop', action='store_true', help='Run continuously instead of a single pass')
    parser.add_argument('--apply', action='store_true', help='Allow bounded repair actions on existing in-flight cases')
    parser.add_argument('--allow-resume-swarm', action='store_true', help='When --apply is set, allow same-dispatch swarm recovery')
    parser.add_argument('--allow-launch-synthesis', action='store_true', help='When --apply is set, allow synthesis launch for already-open cases')
    parser.add_argument('--allow-launch-decision', action='store_true', help='When --apply is set, allow Decision-Maker launch for already-open cases')
    parser.add_argument('--allow-finalize-decision', action='store_true', help='When --apply is set, allow decision-stage status finalization from already-valid artifacts')
    parser.add_argument('--allow-finalize-pipeline', action='store_true', help='When --apply is set, allow pipeline-status finalization from already-ready decision artifacts')
    parser.add_argument('--case-key', action='append', default=[], help='Limit monitoring to one or more specific case keys')
    parser.add_argument('--control-managed', action='store_true', help='Load repair/apply policy from the persisted automation control file each pass')
    parser.add_argument('--control-file', default=str(DEFAULT_CONTROL_FILE), help='Automation control file path used with --control-managed')
    parser.add_argument('--lock-file', default=str(DEFAULT_LOCK), help='Process lock to prevent concurrent watchdog loops')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def finalize_pipeline(case_key: str, *, decision_payload: dict[str, object], summary: dict[str, object]) -> dict[str, object]:
    outputs = decision_payload.get('outputs') or {}
    outputs = outputs if isinstance(outputs, dict) else {}
    packet_path_text = str(outputs.get('packet_json_path') or '').strip()
    packet_payload = load_json_if_exists(ACTION_REPO_ROOT / packet_path_text) if packet_path_text else {}
    decision_block = packet_payload.get('decision') or {}
    decision_block = decision_block if isinstance(decision_block, dict) else {}
    updated = update_case_pipeline_status(
        case_key=case_key,
        dispatch_id=str(summary.get('dispatch_id') or '').strip(),
        market_id=str(summary.get('market_id') or '').strip(),
        market_title=str(summary.get('market_title') or '').strip(),
        status='pipeline_completed',
        current_stage='decision',
        stage_status_patch={
            'swarm': 'completed',
            'synthesis': 'completed',
            'decision': 'completed',
        },
        runner_id='watch_pipeline',
        message='Watchdog finalized pipeline from ready decision artifacts',
        terminal_summary_patch={
            'decision_packet_json': packet_path_text or None,
            'decision_packet_markdown': str(outputs.get('packet_markdown_path') or '').strip() or None,
            'decision_readiness': str(decision_block.get('decision_readiness') or '').strip() or None,
            'recommended_side': str(decision_block.get('side') or '').strip() or None,
            'trade_authorization': str(decision_block.get('trade_authorization') or '').strip() or None,
            'position_policy': str(decision_block.get('position_policy') or '').strip() or None,
        },
    )
    return {'ok': True, 'payload': updated}


def effective_watchdog_policy(args: argparse.Namespace) -> dict[str, object]:
    policy: dict[str, object] = {
        'enabled': True,
        'apply': bool(args.apply),
        'allow_resume_swarm': bool(args.apply and args.allow_resume_swarm),
        'allow_launch_synthesis': bool(args.apply and args.allow_launch_synthesis),
        'allow_launch_decision': bool(args.apply and args.allow_launch_decision),
        'allow_finalize_decision': bool(args.apply and args.allow_finalize_decision),
        'allow_finalize_pipeline': bool(args.apply and args.allow_finalize_pipeline),
        'control_managed': bool(args.control_managed),
        'control_file': str(Path(args.control_file).expanduser().resolve()),
    }
    if args.control_managed:
        control = load_control_file(Path(args.control_file).expanduser().resolve())
        control_policy = resolve_watchdog_policy(control)
        policy.update({
            'enabled': bool(control_policy.get('enabled')),
            'apply': bool(control_policy.get('apply')) or bool(policy['apply']),
            'allow_resume_swarm': bool(control_policy.get('allow_resume_swarm')) or bool(policy['allow_resume_swarm']),
            'allow_launch_synthesis': bool(control_policy.get('allow_launch_synthesis')) or bool(policy['allow_launch_synthesis']),
            'allow_launch_decision': bool(control_policy.get('allow_launch_decision')) or bool(policy['allow_launch_decision']),
            'allow_finalize_decision': bool(control_policy.get('allow_finalize_decision')) or bool(policy['allow_finalize_decision']),
            'allow_finalize_pipeline': bool(control_policy.get('allow_finalize_pipeline')) or bool(policy['allow_finalize_pipeline']),
            'control_snapshot': control,
        })
    return policy


def selected_cases(case_filters: list[str]) -> list[dict[str, object]]:
    summaries = list_case_pipeline_statuses(include_terminal=False)
    if not case_filters:
        return summaries
    allow = set(case_filters)
    return [summary for summary in summaries if str(summary.get('case_key') or '') in allow]


def watch_case(summary: dict[str, object], *, args: argparse.Namespace, policy: dict[str, object]) -> dict[str, object]:
    case_key = str(summary.get('case_key') or '').strip()
    if not case_key:
        return {'ok': False, 'error': 'missing_case_key', 'case_summary': summary}

    stage_statuses = summary.get('stage_statuses') or {}
    stage_statuses = stage_statuses if isinstance(stage_statuses, dict) else {}
    case_result: dict[str, object] = {
        'case_key': case_key,
        'before': summary,
        'proposed_actions': [],
        'executed_actions': [],
    }

    swarm_result = reconcile_swarm(case_key, stale_seconds=args.stale_seconds, check_only=not bool(policy['apply']), pretty=args.pretty)
    case_result['swarm_reconcile'] = swarm_result
    swarm_payload = swarm_result.get('payload') or {}
    swarm_payload = swarm_payload if isinstance(swarm_payload, dict) else {}
    swarm_status = str(swarm_payload.get('status') or '').strip()
    if swarm_status == 'stale':
        case_result['proposed_actions'].append('resume_swarm_same_dispatch')
        if policy['apply'] and policy['allow_resume_swarm']:
            action = resume_swarm(case_key, pretty=args.pretty)
            case_result['executed_actions'].append({'name': 'resume_swarm_same_dispatch', 'result': action})
    elif swarm_status == 'ready_for_synthesis':
        case_result['proposed_actions'].append('launch_synthesis_for_existing_case')
        if policy['apply'] and policy['allow_launch_synthesis']:
            action = resume_swarm(case_key, pretty=args.pretty)
            case_result['executed_actions'].append({'name': 'launch_synthesis_for_existing_case', 'result': action})

    summary_after_swarm = summarize_case_pipeline_status(case_key)
    stage_statuses = summary_after_swarm.get('stage_statuses') or stage_statuses
    stage_statuses = stage_statuses if isinstance(stage_statuses, dict) else {}
    synthesis_completed = stage_statuses.get('synthesis') == 'completed' or str(swarm_payload.get('synthesis_status') or '').strip() == 'synthesis_completed'
    decision_pending = stage_statuses.get('decision') in {'pending', ''}

    if not synthesis_completed and decision_pending:
        if synthesis_status_file(case_key) is not None:
            case_result['proposed_actions'].append('check_synthesis_launch_gate')
            if policy['apply'] and policy['allow_launch_synthesis']:
                action = launch_synthesis_if_needed(case_key, pretty=args.pretty)
                case_result['executed_actions'].append({'name': 'check_synthesis_launch_gate', 'result': action})
                summary_after_swarm = summarize_case_pipeline_status(case_key)
                stage_statuses = summary_after_swarm.get('stage_statuses') or stage_statuses
                stage_statuses = stage_statuses if isinstance(stage_statuses, dict) else {}
                synthesis_completed = stage_statuses.get('synthesis') == 'completed'
                decision_pending = stage_statuses.get('decision') in {'pending', ''}

    if synthesis_completed or stage_statuses.get('decision') in {'pending', 'in_progress', 'failed'}:
        decision_result = reconcile_decision(case_key, pretty=args.pretty)
        case_result['decision_reconcile'] = decision_result
        decision_payload = decision_result.get('payload') or {}
        decision_payload = decision_payload if isinstance(decision_payload, dict) else {}
        decision_health = str(decision_payload.get('health') or '').strip()
        if decision_health == 'ready' and summary_after_swarm.get('status') != 'pipeline_completed':
            case_result['proposed_actions'].append('finalize_pipeline_from_ready_decision')
            if policy['apply'] and policy['allow_finalize_pipeline']:
                action = finalize_pipeline(case_key, decision_payload=decision_payload, summary=summary_after_swarm)
                case_result['executed_actions'].append({'name': 'finalize_pipeline_from_ready_decision', 'result': action})
        if decision_health == 'stale_status':
            case_result['proposed_actions'].append('finalize_decision_status_from_existing_packet')
            if policy['apply'] and policy['allow_finalize_decision']:
                action = finalize_decision(case_key, pretty=args.pretty)
                case_result['executed_actions'].append({'name': 'finalize_decision_status_from_existing_packet', 'result': action})
        elif decision_health == 'not_started' and decision_pending:
            case_result['proposed_actions'].append('launch_decision_for_existing_case')
            if policy['apply'] and policy['allow_launch_decision']:
                action = launch_decision_maker(case_key, pretty=args.pretty)
                case_result['executed_actions'].append({'name': 'launch_decision_for_existing_case', 'result': action})

    case_result['after'] = summarize_case_pipeline_status(case_key)
    case_result['ok'] = True
    return case_result


def watchdog_pass(args: argparse.Namespace) -> dict[str, object]:
    policy = effective_watchdog_policy(args)
    if not policy.get('enabled', True):
        return {
            'ok': True,
            'mode': {**policy, 'claims_new_cases': False},
            'active_case_count': 0,
            'results': [],
            'status': 'watchdog_disabled_by_control',
        }
    cases = selected_cases(args.case_key)
    results = [watch_case(summary, args=args, policy=policy) for summary in cases]
    return {
        'ok': all(result.get('ok', False) for result in results),
        'mode': {**policy, 'claims_new_cases': False},
        'active_case_count': len(cases),
        'results': results,
    }


def main() -> None:
    args = parse_args()
    lock_path = Path(args.lock_file).expanduser().resolve()
    with exclusive_lock(lock_path, error_message=f'another watchdog instance already holds {lock_path}'):
        if not args.loop:
            summary = watchdog_pass(args)
            print(json.dumps(summary, indent=2 if args.pretty else None))
            if not summary.get('ok'):
                raise SystemExit(1)
            return

        while True:
            summary = watchdog_pass(args)
            print(json.dumps(summary, indent=2 if args.pretty else None), flush=True)
            time.sleep(args.poll_seconds)


if __name__ == '__main__':
    main()
