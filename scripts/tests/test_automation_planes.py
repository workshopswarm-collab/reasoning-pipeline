from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[1] / 'automation_planes.py'


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


automation_planes = load_module('automation_planes', MODULE_PATH)


class AutomationPlanesTests(unittest.TestCase):
    def plane_states(self, *, sequencer: bool, watchdog: bool, watcher: bool) -> dict[str, dict[str, object]]:
        return {
            'sequencer': {'service': {'bootstrapped': sequencer}, 'heartbeat': {'stale': False}},
            'watchdog': {'service': {'bootstrapped': watchdog}, 'heartbeat': {'stale': False}},
            'decided_market_watcher': {'service': {'bootstrapped': watcher}, 'heartbeat': {'stale': False}},
        }

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
        summary = automation_planes.summarize(control, self.plane_states(sequencer=True, watchdog=True, watcher=True))
        self.assertTrue(summary['all_planes_enabled'])
        self.assertEqual(summary['decided_market_watcher_mode'], 'active')
        self.assertEqual(summary['sequencer_service_mode'], 'active')
        self.assertEqual(summary['watchdog_service_mode'], 'active')

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
        summary = automation_planes.summarize(control, self.plane_states(sequencer=True, watchdog=True, watcher=False))
        self.assertFalse(summary['all_planes_enabled'])
        self.assertEqual(summary['decided_market_watcher_mode'], 'inactive')

    def test_ensure_plane_running_kickstarts_stale_bootstrapped_service(self) -> None:
        plane_state = {
            'service': {'bootstrapped': True, 'launchctl_label': 'gui/501/example'},
            'heartbeat': {'exists': True, 'stale': True},
        }
        with patch.object(automation_planes, 'plane_status', return_value={'bootstrapped': True, 'launchctl_label': 'gui/501/example'}), patch.object(
            automation_planes,
            'kickstart_launchd',
            return_value={'ok': True, 'launchctl_label': 'gui/501/example'},
        ) as kickstart:
            result = automation_planes.ensure_plane_running('sequencer', automation_planes.SEQUENCER_HELPER, plane_state, restart_stale=True)

        kickstart.assert_called_once()
        self.assertEqual(result['actions'][0]['action'], 'kickstart_for_stale_heartbeat')


if __name__ == '__main__':
    unittest.main()
