from __future__ import annotations

import importlib
import importlib.util
import json
import sys
import tempfile
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNTIME_ROOT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime'
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))

AGGREGATE_SCRIPT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime' / 'scripts' / 'aggregate_causal_candidate_proposals.py'
spec = importlib.util.spec_from_file_location('aggregate_causal_candidate_proposals_for_tests', AGGREGATE_SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError(f'could not import aggregate script from {AGGREGATE_SCRIPT}')
aggregate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aggregate)

trial_selection = importlib.import_module('lib.proposed_causal_trial_selection')


class ProposedCausalTrialGateTests(unittest.TestCase):
    def test_exploratory_trial_lane_can_promote_single_family_candidate(self) -> None:
        proposal = {
            'proposal_id': 'p1',
            'proposal_key': 'governing-source-proof-capture',
            'candidate_type': 'node',
            'mechanism_family': 'source_resolution',
            'promotion_status': 'insufficient_support',
            'occurrence_count': 1,
            'shadow_match_count': 4,
            'shadow_judged_count': 4,
            'shadow_helpful_count': 0,
            'shadow_harmful_count': 0,
            'shadow_score_sum': 0.0,
            'non_intervention_support_case_count': 1,
            'genericity_penalty': 0.14,
            'max_duplicate_similarity': 0.55,
            'duplicate_of_live_graph': False,
            'merge_recommended': False,
            'contest_case_count': 0,
            'trial_exposure_count': 0,
            'trial_helpful_count': 0,
            'trial_harmful_count': 0,
            'trial_score_sum': 0.0,
            'distinct_case_count': 1,
            'stats_metadata': {},
            'supporting_case_keys': [],
        }
        family_policies = {
            'source_resolution': {
                'mechanism_family': 'source_resolution',
                'enabled': True,
                'max_shadow_candidates': 6,
                'max_trial_candidates': 2,
                'max_active_nodes': 6,
                'max_active_edges': 5,
                'min_shadow_judged_count_for_trial': 4,
                'min_shadow_helpful_count_for_trial': 1,
                'min_shadow_mean_score_for_trial': 0.5,
                'min_non_intervention_support_cases_for_trial': 2,
                'max_genericity_for_trial': 0.28,
                'max_duplicate_similarity_for_trial': 0.88,
                'max_promotion_ready_candidates': 1,
                'min_trial_judged_count_for_promotion': 2,
                'min_trial_helpful_count_for_promotion': 1,
                'min_trial_shrunken_utility_for_promotion': 0.25,
                'max_trial_harmful_rate_for_promotion': 0.34,
                'max_contest_case_count_for_promotion': 1,
                'max_genericity_for_promotion': 0.24,
                'notes': {
                    'exploratory_trial': {
                        'enabled': True,
                        'max_candidates': 1,
                        'require_base_proposal_threshold': False,
                        'min_shadow_judged_count': 4,
                        'min_shadow_helpful_count': 0,
                        'min_non_intervention_support_cases': 1,
                        'min_shadow_trial_score': 0.0,
                    }
                },
            }
        }
        family_summary = aggregate.attach_family_policy_state(
            [proposal],
            family_policy_rows=family_policies,
            live_family_state={},
            open_health_violations_by_key={},
        )
        trial_readiness = proposal['trial_readiness']
        self.assertTrue(trial_readiness['eligible'])
        self.assertEqual(trial_readiness['eligibility_mode'], 'exploratory')
        self.assertEqual(trial_readiness['prospective_stage'], 'trial_candidate')
        self.assertEqual(trial_readiness['family_exploratory_trial_rank'], 1)
        self.assertIn('below_base_proposal_threshold', trial_readiness['standard_blockers'])
        self.assertEqual(family_summary['source_resolution']['proposal_counts']['exploratory_trial_candidates'], 1)

    def test_overlay_selection_reports_family_cap_blocker(self) -> None:
        bundle = {
            'query_profile': {
                'source_of_truth_class': 'authoritative_with_fallback',
                'platform': 'kalshi',
                'category': 'macro',
                'question_mechanics': ['publication-timing'],
            },
            'causal_context': {
                'active_nodes': ['publication-window-timing'],
                'active_node_metadata': [],
                'matched_edges': [],
                'matched_edge_metadata': [],
                'contested_edges': [],
                'required_checks': [],
            },
            'retrieval_policy': {
                'live_graph_family_state': {
                    'source_resolution': {'trial_total': 0, 'active_nodes': 0, 'active_edges': 0},
                },
                'live_graph_family_policy_caps': {
                    'source_resolution': {'max_trial_candidates': 2, 'max_active_nodes': 6, 'max_active_edges': 5},
                },
            },
        }
        proposals = {
            'proposals': [
                {
                    'proposal_id': 'p1',
                    'proposal_key': 'governing-source-proof-capture',
                    'candidate_type': 'node',
                    'mechanism_family': 'source_resolution',
                    'dominant_proposal_source': 'projection',
                    'promotion_status': 'proposed',
                    'lifecycle_stage': 'trial_candidate',
                    'trial_readiness': {'eligible': True, 'eligibility_mode': 'exploratory'},
                    'merge_recommended': False,
                    'shadow_trial_score': 0.4,
                    'trial_shrunken_utility': 0.0,
                    'trial_helpful_count': 0,
                    'trial_harmful_rate': 0.0,
                    'shadow_helpful_count': 0,
                    'shadow_harmful_count': 0,
                    'shadow_judged_count': 4,
                    'non_intervention_support_case_count': 1,
                    'distinct_case_count': 1,
                    'genericity_penalty': 0.14,
                    'family_trial_rank': None,
                    'stats_metadata': {'observed_active_nodes': ['publication-window-timing']},
                    'context_distribution': {'question_mechanics': {'publication-timing': 2}},
                    'family_policy': {},
                },
                {
                    'proposal_id': 'p2',
                    'proposal_key': 'primary-resolution-source-identification',
                    'candidate_type': 'node',
                    'mechanism_family': 'source_resolution',
                    'dominant_proposal_source': 'projection',
                    'promotion_status': 'proposed',
                    'lifecycle_stage': 'trial_candidate',
                    'trial_readiness': {'eligible': True, 'eligibility_mode': 'exploratory'},
                    'merge_recommended': False,
                    'shadow_trial_score': 0.35,
                    'trial_shrunken_utility': 0.0,
                    'trial_helpful_count': 0,
                    'trial_harmful_rate': 0.0,
                    'shadow_helpful_count': 0,
                    'shadow_harmful_count': 0,
                    'shadow_judged_count': 4,
                    'non_intervention_support_case_count': 1,
                    'distinct_case_count': 1,
                    'genericity_penalty': 0.15,
                    'family_trial_rank': None,
                    'stats_metadata': {'observed_active_nodes': ['publication-window-timing']},
                    'context_distribution': {'question_mechanics': {'publication-timing': 2}},
                    'family_policy': {},
                },
            ]
        }
        with tempfile.TemporaryDirectory() as tmpdir:
            summary_path = Path(tmpdir) / 'summary.json'
            summary_path.write_text(json.dumps(proposals), encoding='utf-8')
            overlay = trial_selection.evaluate_trial_candidates(bundle, limit=2, summary_path=summary_path)
        self.assertEqual(overlay['selected_count'], 1)
        self.assertEqual(overlay['selection_blocker_counts'].get('dispatch_family_cap_reached'), 1)
        skipped = overlay['skipped_candidates']
        self.assertEqual(len(skipped), 1)
        self.assertIn('dispatch_family_cap_reached', skipped[0]['selection_blockers'])


if __name__ == '__main__':
    unittest.main()
