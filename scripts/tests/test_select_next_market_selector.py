from __future__ import annotations

import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SELECT_NEXT_MARKET = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'planner' / 'scripts' / 'select_next_market.py'


class SelectNextMarketSelectorTests(unittest.TestCase):
    def test_selector_does_not_gate_pending_research_on_prior_case_history(self) -> None:
        text = SELECT_NEXT_MARKET.read_text()
        self.assertIn("pipeline_status IN ('new', 'pending_research')", text)
        self.assertNotIn('FROM cases c_prior', text)
        self.assertNotIn('WHERE c_prior.market_id = m.id', text)


if __name__ == '__main__':
    unittest.main()
