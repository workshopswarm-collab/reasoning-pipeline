#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
SCRIPTS_DIR = SCRIPT_PATH.parent
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.db import DEFAULT_PSQL  # noqa: E402

NODE_STATS_SCRIPT = SCRIPTS_DIR / 'update_causal_node_stats.py'
EDGE_STATS_SCRIPT = SCRIPTS_DIR / 'update_causal_edge_stats.py'
HEALTH_SCAN_SCRIPT = SCRIPTS_DIR / 'scan_causal_graph_health.py'
REPAIR_SCRIPT = SCRIPTS_DIR / 'repair_causal_graph.py'
CONTROLLER_SCRIPT = SCRIPTS_DIR / 'advance_live_causal_graph_items.py'
DEFAULT_EXPERIMENT_ID = 'researcher-lmd-v1'
DEFAULT_SHRINKAGE_K = 5.0
DEFAULT_MAX_ACTIONS = 50
DEFAULT_REPAIR_MAX_ACTIONS = 25


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Refresh live causal-graph stats/health, run bounded repairs, and invoke the lifecycle controller')
    parser.add_argument('--experiment-id', default=DEFAULT_EXPERIMENT_ID)
    parser.add_argument('--shrinkage-k', type=float, default=DEFAULT_SHRINKAGE_K)
    parser.add_argument('--node-key', action='append', default=[])
    parser.add_argument('--edge-key', action='append', default=[])
    parser.add_argument('--mechanism-family', action='append', default=[])
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--controller-apply', action='store_true', help='Allow the lifecycle controller to persist transitions')
    parser.add_argument('--max-actions', type=int, default=DEFAULT_MAX_ACTIONS)
    parser.add_argument('--skip-health-scan', action='store_true')
    parser.add_argument('--skip-repairs', action='store_true')
    parser.add_argument('--repair-apply', action='store_true', help='Allow the repair step to persist low-risk repairs')
    parser.add_argument('--repair-max-actions', type=int, default=DEFAULT_REPAIR_MAX_ACTIONS)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def unique(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        value = str(item or '').strip()
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out



def add_common_db_args(cmd: list[str], args: argparse.Namespace, *, include_dry_run: bool = True) -> None:
    cmd.extend(['--psql', args.psql])
    if args.db_url:
        cmd.extend(['--db-url', args.db_url])
    if include_dry_run and args.dry_run:
        cmd.append('--dry-run')



def add_entity_filters(cmd: list[str], args: argparse.Namespace) -> None:
    for value in unique(args.node_key or []):
        cmd.extend(['--node-key', value])
    for value in unique(args.edge_key or []):
        cmd.extend(['--edge-key', value])
    for value in unique(args.mechanism_family or []):
        cmd.extend(['--mechanism-family', value])



def build_cycle_commands(args: argparse.Namespace) -> list[dict[str, Any]]:
    if args.controller_apply and args.dry_run:
        raise ValueError('--controller-apply cannot be combined with --dry-run')
    if args.repair_apply and args.dry_run:
        raise ValueError('--repair-apply cannot be combined with --dry-run')

    steps: list[dict[str, Any]] = []

    node_cmd = [sys.executable, str(NODE_STATS_SCRIPT), '--experiment-id', args.experiment_id, '--shrinkage-k', str(args.shrinkage_k)]
    add_common_db_args(node_cmd, args)
    steps.append({'step': 'update_causal_node_stats', 'command': node_cmd})

    edge_cmd = [sys.executable, str(EDGE_STATS_SCRIPT), '--experiment-id', args.experiment_id, '--shrinkage-k', str(args.shrinkage_k)]
    add_common_db_args(edge_cmd, args)
    steps.append({'step': 'update_causal_edge_stats', 'command': edge_cmd})

    if not args.skip_health_scan:
        scan_cmd = [sys.executable, str(HEALTH_SCAN_SCRIPT)]
        add_common_db_args(scan_cmd, args)
        add_entity_filters(scan_cmd, args)
        steps.append({'step': 'scan_causal_graph_health', 'command': scan_cmd})

    if not args.skip_repairs:
        repair_cmd = [sys.executable, str(REPAIR_SCRIPT), '--max-actions', str(args.repair_max_actions)]
        if args.repair_apply and not args.dry_run:
            repair_cmd.append('--apply')
        add_common_db_args(repair_cmd, args, include_dry_run=False)
        add_entity_filters(repair_cmd, args)
        steps.append({'step': 'repair_causal_graph', 'command': repair_cmd})

    controller_cmd = [sys.executable, str(CONTROLLER_SCRIPT), '--max-actions', str(args.max_actions)]
    if args.controller_apply and not args.dry_run:
        controller_cmd.append('--apply')
    add_common_db_args(controller_cmd, args, include_dry_run=False)
    add_entity_filters(controller_cmd, args)
    steps.append({'step': 'advance_live_causal_graph_items', 'command': controller_cmd})

    return steps



def run_step(step_name: str, command: list[str]) -> dict[str, Any]:
    proc = subprocess.run(command, text=True, capture_output=True)
    if proc.returncode != 0:
        return {
            'step': step_name,
            'ok': False,
            'returncode': proc.returncode,
            'command': command,
            'stderr': proc.stderr.strip(),
            'stdout': proc.stdout.strip(),
        }
    try:
        payload = json.loads(proc.stdout)
    except Exception as exc:  # noqa: BLE001
        return {
            'step': step_name,
            'ok': False,
            'returncode': proc.returncode,
            'command': command,
            'stderr': f'failed to parse JSON output: {exc}',
            'stdout': proc.stdout.strip(),
        }
    return {
        'step': step_name,
        'ok': True,
        'returncode': proc.returncode,
        'command': command,
        'payload': payload,
    }



def summarize_step(step_name: str, payload: dict[str, Any]) -> dict[str, Any]:
    if step_name == 'update_causal_node_stats':
        return {
            'step': step_name,
            'node_count': payload.get('node_count'),
            'persisted_count': payload.get('persisted_count'),
            'warning': payload.get('warning'),
        }
    if step_name == 'update_causal_edge_stats':
        return {
            'step': step_name,
            'edge_count': payload.get('edge_count'),
            'persisted_count': payload.get('persisted_count'),
            'warning': payload.get('warning'),
        }
    if step_name == 'scan_causal_graph_health':
        persistence = payload.get('persistence') or {}
        return {
            'step': step_name,
            'violation_count': payload.get('violation_count'),
            'violation_class_counts': payload.get('violation_class_counts') or {},
            'inserted_count': persistence.get('inserted_count'),
            'updated_count': persistence.get('updated_count'),
            'resolved_count': persistence.get('resolved_count'),
            'warnings': payload.get('warnings') or [],
        }
    if step_name == 'repair_causal_graph':
        return {
            'step': step_name,
            'repair_count': payload.get('repair_count'),
            'deferred_count': payload.get('deferred_count'),
            'pre_repair': payload.get('pre_repair') or {},
            'post_repair_projection': payload.get('post_repair_projection') or {},
            'warnings': payload.get('warnings') or [],
        }
    if step_name == 'advance_live_causal_graph_items':
        return {
            'step': step_name,
            'recommended_count': payload.get('recommended_count'),
            'blocked_count': payload.get('blocked_count'),
            'warning': payload.get('warning'),
            'stats_presence': payload.get('stats_presence') or {},
        }
    return {'step': step_name}



def main() -> int:
    args = parse_args()
    try:
        steps = build_cycle_commands(args)
    except ValueError as exc:
        raise SystemExit(str(exc))

    step_results: list[dict[str, Any]] = []
    summaries: list[dict[str, Any]] = []
    for step in steps:
        result = run_step(step['step'], step['command'])
        step_results.append(result)
        if not result.get('ok'):
            print(json.dumps({'ok': False, 'failed_step': result}, indent=2 if args.pretty else None))
            return 1
        summaries.append(summarize_step(step['step'], result.get('payload') or {}))

    output = {
        'ok': True,
        'dry_run': args.dry_run,
        'repair_apply': args.repair_apply,
        'controller_apply': args.controller_apply,
        'step_count': len(step_results),
        'summaries': summaries,
        'steps': [
            {
                'step': result['step'],
                'payload': result.get('payload') or {},
            }
            for result in step_results
        ],
    }
    if args.dry_run:
        output['note'] = 'node/edge stats and health scan are previewed without persistence; downstream repair/controller steps still read the currently persisted DB state rather than ephemeral dry-run outputs'
    elif not args.repair_apply:
        output['note'] = 'repair step ran in preview mode; enable --repair-apply for automatic low-risk repairs during the cycle'
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
