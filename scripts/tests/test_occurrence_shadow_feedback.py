from __future__ import annotations

import argparse
import importlib
import importlib.util
import sys
import unittest
from pathlib import Path

TEST_DIR = Path(__file__).resolve().parent
REPO_ROOT = TEST_DIR.parents[1]
RUNTIME_ROOT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime'
SCRIPTS_ROOT = RUNTIME_ROOT / 'scripts'

if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))


def load_script_module(name: str, filename: str):
    path = SCRIPTS_ROOT / filename
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


score_script = load_script_module('score_proposed_causal_shadow_outcomes_test', 'score_proposed_causal_shadow_outcomes.py')
report_script = load_script_module('report_occurrence_bridge_shadow_evidence_test', 'report_occurrence_bridge_shadow_evidence.py')
shadow_outcomes = importlib.import_module('lib.proposed_causal_shadow_outcomes')


class OccurrenceShadowFeedbackTests(unittest.TestCase):
    def test_cross_case_occurrence_support_can_escape_unclear_without_review_artifact(self) -> None:
        judgment = shadow_outcomes.judge_shadow_row(
            {
                'case_key': 'case-x',
                'proposal_key': 'threshold-proximity',
                'would_inject': True,
                'retrieval_score': 0.97,
                'notes': {'candidate_notes': {}},
                'matched_active_nodes': [],
                'matched_candidate_edges': [],
                'matched_contested_edges': [],
                'matched_required_checks': [],
            },
            occurrence_rows=[
                {
                    'evidence_channels': ['signal_packet'],
                    'intervention_dependency': 'none',
                    'support_direction': 'supports',
                    'proposal_metadata': {'canonical_family': 'threshold_touch'},
                }
            ],
            case_artifacts={
                'review_exists': False,
                'review_summary': {'summary': 'Market is sitting near an important threshold and intraday volatility remains elevated.'},
                'projection': {},
                'canonical_suggestions': {},
            },
            occurrence_scope='cross_case',
        )
        self.assertIn(judgment['outcome_label'], {'neutral', 'helpful'})
        self.assertIn('family_specific_signal:threshold_touch', judgment['outcome_metadata']['reasons'])
        self.assertEqual(judgment['outcome_metadata']['family_signal']['canonical_family'], 'threshold_touch')
        self.assertGreater(judgment['outcome_metadata']['family_signal']['hit_weight'], 0)
        self.assertEqual(judgment['outcome_metadata']['occurrence_scope'], 'cross_case')

    def test_occurrence_rows_match_filters_respects_proposal_and_bridge_source(self) -> None:
        args = argparse.Namespace(
            case_key='',
            proposal_id='',
            dispatch_id='',
            proposal_source='driver_occurrence_compiler',
            bridge_source='occurrence_packet_shadow_bridge',
            only_unjudged=True,
            db_url='',
            psql='psql',
            dry_run=False,
            pretty=False,
        )
        rows = [
            {
                'proposal_source': 'driver_occurrence_compiler',
                'proposal_metadata': {'bridge_source': 'occurrence_packet_shadow_bridge'},
            }
        ]
        self.assertTrue(score_script.occurrence_rows_match_filters(rows, args))
        bad_rows = [
            {
                'proposal_source': 'rule_projection',
                'proposal_metadata': {'bridge_source': 'other_bridge'},
            }
        ]
        self.assertFalse(score_script.occurrence_rows_match_filters(bad_rows, args))

    def test_report_sort_rows_prefers_judged_then_match_count(self) -> None:
        rows = [
            {'proposal_key': 'beta', 'shadow_judged_count': 1, 'shadow_match_count': 2, 'promotion_score': 0.4},
            {'proposal_key': 'alpha', 'shadow_judged_count': 2, 'shadow_match_count': 1, 'promotion_score': 0.1},
            {'proposal_key': 'gamma', 'shadow_judged_count': 2, 'shadow_match_count': 3, 'promotion_score': 0.2},
        ]
        ordered = report_script.sort_rows(rows)
        self.assertEqual([row['proposal_key'] for row in ordered], ['gamma', 'alpha', 'beta'])


if __name__ == '__main__':
    unittest.main()
