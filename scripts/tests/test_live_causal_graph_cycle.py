from __future__ import annotations

import argparse
import importlib.util
import sys
import unittest
from pathlib import Path

TEST_DIR = Path(__file__).resolve().parent
REPO_ROOT = TEST_DIR.parents[1]
RUNTIME_ROOT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime'
RUNTIME_SCRIPTS_DIR = RUNTIME_ROOT / 'scripts'

for candidate in [RUNTIME_ROOT, RUNTIME_SCRIPTS_DIR]:
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


cycle = load_module(
    'run_live_causal_graph_cycle_for_tests',
    RUNTIME_SCRIPTS_DIR / 'run_live_causal_graph_cycle.py',
)


class LiveCausalGraphCycleTests(unittest.TestCase):
    def make_args(self, **overrides) -> argparse.Namespace:
        values = {
            'experiment_id': 'researcher-lmd-v1',
            'shrinkage_k': 5.0,
            'node_key': [],
            'edge_key': [],
            'mechanism_family': [],
            'db_url': '',
            'psql': '/opt/homebrew/opt/postgresql@16/bin/psql',
            'controller_apply': False,
            'max_actions': 50,
            'skip_health_scan': False,
            'skip_repairs': False,
            'repair_apply': False,
            'repair_max_actions': 25,
            'dry_run': False,
            'pretty': False,
        }
        values.update(overrides)
        return argparse.Namespace(**values)

    def test_build_cycle_commands_includes_scan_repair_and_controller(self) -> None:
        args = self.make_args(mechanism_family=['publication_timing'])
        steps = cycle.build_cycle_commands(args)
        self.assertEqual([step['step'] for step in steps], [
            'update_causal_node_stats',
            'update_causal_edge_stats',
            'scan_causal_graph_health',
            'repair_causal_graph',
            'advance_live_causal_graph_items',
        ])
        scan_cmd = next(step['command'] for step in steps if step['step'] == 'scan_causal_graph_health')
        repair_cmd = next(step['command'] for step in steps if step['step'] == 'repair_causal_graph')
        controller_cmd = next(step['command'] for step in steps if step['step'] == 'advance_live_causal_graph_items')
        for cmd in [scan_cmd, repair_cmd, controller_cmd]:
            self.assertIn('--mechanism-family', cmd)
            self.assertIn('publication_timing', cmd)

    def test_build_cycle_commands_can_skip_repairs(self) -> None:
        args = self.make_args(skip_repairs=True)
        steps = cycle.build_cycle_commands(args)
        self.assertNotIn('repair_causal_graph', [step['step'] for step in steps])

    def test_build_cycle_commands_rejects_apply_with_dry_run(self) -> None:
        args = self.make_args(controller_apply=True, dry_run=True)
        with self.assertRaises(ValueError):
            cycle.build_cycle_commands(args)
        args = self.make_args(repair_apply=True, dry_run=True)
        with self.assertRaises(ValueError):
            cycle.build_cycle_commands(args)


if __name__ == '__main__':
    unittest.main()
