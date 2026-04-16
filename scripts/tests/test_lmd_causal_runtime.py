from __future__ import annotations

import sys
import unittest
from pathlib import Path

TEST_DIR = Path(__file__).resolve().parent
REPO_ROOT = TEST_DIR.parents[1]
RUNTIME_ROOT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime'
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))

from lib.lmd_causal_runtime import audit_path_for_bundle, case_mix_from_query_profile, coverage_metrics_from_bundle, negative_checks_from_required_checks


class LmdCausalRuntimeTests(unittest.TestCase):
    def test_negative_checks_from_required_checks_maps_known_keys(self) -> None:
        rows = negative_checks_from_required_checks([
            {'check_key': 'label_unverified_vs_not_occurred_distinctly', 'reason': 'contested_edge', 'source': 'heuristic'},
        ])
        self.assertEqual(len(rows), 1)
        self.assertIn('Do not treat', rows[0]['avoid'])
        self.assertEqual(rows[0]['check_key'], 'label_unverified_vs_not_occurred_distinctly')

    def test_coverage_metrics_classifies_strong_bundle(self) -> None:
        metrics = coverage_metrics_from_bundle(
            {
                'results': {
                    'case_reviews': [{'case_key': 'a'}],
                    'active_interventions': [{'intervention_key': 'i'}],
                    'aggregate_notes': [{'path': 'x.md'}],
                    'required_checks': [{'check_key': 'verify_primary_resolution_source'}],
                    'negative_checks': [{'check_key': 'verify_primary_resolution_source', 'avoid': 'Do not rely on a secondary source.'}],
                },
                'causal_context': {
                    'active_nodes': ['resolution-surface-ambiguity'],
                    'matched_edges': ['resolution-surface-ambiguity__increases__verification-caution'],
                    'contested_edges': [],
                },
            }
        )
        self.assertEqual(metrics['classification'], 'strong')
        self.assertTrue(metrics['has_live_context'])
        self.assertEqual(metrics['counts']['case_review_count'], 1)

    def test_case_mix_from_query_profile_tags_touch_and_source_sensitive(self) -> None:
        case_mix = case_mix_from_query_profile(
            {
                'question_mechanics': ['threshold-touch'],
                'source_of_truth_class': 'governing_source',
                'difficulty_class': 'hard',
                'resolution_risk': 'high',
            }
        )
        self.assertIn('touch_market', case_mix['tags'])
        self.assertIn('source_sensitive', case_mix['tags'])
        self.assertIn('difficulty:hard', case_mix['tags'])

    def test_audit_path_for_bundle_swaps_filename(self) -> None:
        path = audit_path_for_bundle('qualitative-db/40-research/cases/case-x/researcher-analyses/2026-01-01/dispatch/lmd-bundle.json')
        self.assertEqual(path.name, 'lmd-causal-audit.json')


if __name__ == '__main__':
    unittest.main()
