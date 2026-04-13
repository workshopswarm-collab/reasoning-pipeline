from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / 'automation_planes.py'


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


automation_planes = load_module('automation_planes', MODULE_PATH)


class AutomationPlanesTests(unittest.TestCase):
    def test_summary_reports_all_planes_enabled(self) -> None:
        control = {
            'control': {
                'automation_enabled': True,
                'watchdog': {'enabled': True, 'apply': True},
                'sequencer': {'enabled': True},
            },
            'summary': {
                'overall_mode': 'fully_automated_one_case_at_a_time',
                'sequencer_mode': 'claiming_new_cases',
                'watchdog_mode': 'repairing_existing_cases',
            },
        }
        watcher = {'bootstrapped': True, 'target_exists': True, 'launchctl_label': 'gui/501/example'}
        summary = automation_planes.summarize(control, watcher)
        self.assertTrue(summary['all_planes_enabled'])
        self.assertEqual(summary['decided_market_watcher_mode'], 'active')

    def test_summary_reports_missing_watcher_as_not_fully_enabled(self) -> None:
        control = {
            'control': {
                'automation_enabled': True,
                'watchdog': {'enabled': True, 'apply': True},
                'sequencer': {'enabled': True},
            },
            'summary': {
                'overall_mode': 'fully_automated_one_case_at_a_time',
                'sequencer_mode': 'claiming_new_cases',
                'watchdog_mode': 'repairing_existing_cases',
            },
        }
        watcher = {'bootstrapped': False, 'target_exists': False, 'launchctl_label': 'gui/501/example'}
        summary = automation_planes.summarize(control, watcher)
        self.assertFalse(summary['all_planes_enabled'])
        self.assertEqual(summary['decided_market_watcher_mode'], 'inactive')


if __name__ == '__main__':
    unittest.main()
