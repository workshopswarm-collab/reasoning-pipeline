from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_SCRIPT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime' / 'scripts' / 'report_phase11_retrieval_policy.py'

spec = importlib.util.spec_from_file_location('phase11_retrieval_policy_report_for_tests', REPORT_SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError(f'could not import report script from {REPORT_SCRIPT}')
phase11_report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(phase11_report)


class Phase11RetrievalPolicyReportTests(unittest.TestCase):
    def test_compare_rankings_detects_score_only_change_without_top1_flip(self) -> None:
        baseline = [
            {'key': 'alpha', 'rank': 1, 'score': 2.0, 'score_breakdown': {}},
            {'key': 'beta', 'rank': 2, 'score': 1.0, 'score_breakdown': {}},
        ]
        learned = [
            {'key': 'alpha', 'rank': 1, 'score': 1.8, 'score_breakdown': {}},
            {'key': 'beta', 'rank': 2, 'score': 1.1, 'score_breakdown': {}},
        ]
        comparison = phase11_report.compare_rankings(baseline_rows=baseline, learned_rows=learned)
        self.assertFalse(comparison['top1_changed'])
        self.assertTrue(phase11_report.surface_has_any_change(comparison))
        self.assertEqual(comparison['baseline_top1'], 'alpha')
        self.assertEqual(comparison['learned_top1'], 'alpha')

    def test_surface_has_any_change_false_when_rankings_identical(self) -> None:
        rows = [
            {'key': 'alpha', 'rank': 1, 'score': 2.0, 'score_breakdown': {}},
            {'key': 'beta', 'rank': 2, 'score': 1.0, 'score_breakdown': {}},
        ]
        comparison = phase11_report.compare_rankings(baseline_rows=rows, learned_rows=rows)
        self.assertFalse(comparison['top1_changed'])
        self.assertFalse(phase11_report.surface_has_any_change(comparison))


if __name__ == '__main__':
    unittest.main()
