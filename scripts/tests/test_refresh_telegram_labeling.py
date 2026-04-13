from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

PLANNER = Path(__file__).resolve().parents[2] / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'planner' / 'scripts' / 'dispatch_case_research.py'


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


planner = load_module('dispatch_case_research_for_tests', PLANNER)


class RefreshTelegramLabelingTests(unittest.TestCase):
    def test_non_refresh_mode_has_no_refresh_markers(self) -> None:
        start, finish = planner.build_refresh_controller_markers(
            case_key='case-20260413-deadbeef',
            market_title='Example market',
            dispatch_id='dispatch-case-20260413-deadbeef-20260413T150000Z',
            refresh_mode='novel',
            refresh_reasons=[],
        )
        self.assertEqual(start, '')
        self.assertEqual(finish, '')

    def test_full_refresh_mode_has_refresh_markers(self) -> None:
        start, finish = planner.build_refresh_controller_markers(
            case_key='case-20260413-deadbeef',
            market_title='Example market',
            dispatch_id='dispatch-case-20260413-deadbeef-20260413T150000Z',
            refresh_mode='full',
            refresh_reasons=['large_price_move'],
        )
        self.assertIn('STARTING FULL REFRESH', start)
        self.assertIn('reasons=large_price_move', start)
        self.assertIn('FINISHED FULL REFRESH SWARM', finish)


if __name__ == '__main__':
    unittest.main()
