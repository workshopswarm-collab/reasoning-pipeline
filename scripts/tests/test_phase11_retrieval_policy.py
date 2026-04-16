from __future__ import annotations

import importlib
import importlib.util
import json
import sys
import tempfile
import types
import unittest
from unittest.mock import patch
from pathlib import Path

TEST_DIR = Path(__file__).resolve().parent
REPO_ROOT = TEST_DIR.parents[1]
PLANNER_SCRIPTS_DIR = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'planner' / 'scripts'
RUNTIME_ROOT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime'

for candidate in [PLANNER_SCRIPTS_DIR, RUNTIME_ROOT]:
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


generate_lmd_bundle = load_module(
    'generate_lmd_bundle_for_phase11_tests',
    PLANNER_SCRIPTS_DIR / 'generate_lmd_bundle.py',
)
trial_selection = importlib.import_module('lib.proposed_causal_trial_selection')


class Phase11RetrievalPolicyTests(unittest.TestCase):
    def make_args(self) -> types.SimpleNamespace:
        return types.SimpleNamespace(
            title='Will the official report be released this week?',
            description='Resolution depends on an official publication timing window and a named governing source.',
            focus_hints_json='[]',
            source_of_truth_class='authoritative_with_fallback',
            current_price='',
            closes_at='',
            resolves_at='',
            extra_verification_required='true',
            run_kind='novel',
            rerun_scope='',
            prior_dispatch_count=0,
            prior_case_count=0,
            difficulty_class='',
            resolution_risk='',
            category='macro',
            platform='kalshi',
            experiment_arm='treatment',
            live_graph_trial_mode='auto',
            shadow_limit=0,
            trial_limit=0,
            generator_version=generate_lmd_bundle.GENERATOR_VERSION,
            policy_version=generate_lmd_bundle.POLICY_VERSION,
            db_url='',
            psql='/opt/homebrew/opt/postgresql@16/bin/psql',
        )

    def test_infer_live_query_context_sorts_metadata_by_phase11_score(self) -> None:
        args = self.make_args()
        nodes = {
            'settlement-source-specificity': {
                'node_key': 'settlement-source-specificity',
                'node_label': 'Settlement source specificity',
                'lifecycle_stage': 'active',
                'status': 'active',
                'mechanism_family': 'resolution_surface',
                'source_kind': 'seed',
                'path': 'qualitative-db/60-causal-map/nodes/settlement-source-specificity.md',
            },
            'resolution-surface-ambiguity': {
                'node_key': 'resolution-surface-ambiguity',
                'node_label': 'Resolution-surface ambiguity',
                'lifecycle_stage': 'active',
                'status': 'active',
                'mechanism_family': 'resolution_surface',
                'source_kind': 'seed',
                'path': 'qualitative-db/60-causal-map/nodes/resolution-surface-ambiguity.md',
            },
            'verification-caution': {
                'node_key': 'verification-caution',
                'node_label': 'Verification caution',
                'lifecycle_stage': 'active',
                'status': 'active',
                'mechanism_family': 'resolution_surface',
                'source_kind': 'seed',
                'path': 'qualitative-db/60-causal-map/nodes/verification-caution.md',
            },
            'publication-window-timing': {
                'node_key': 'publication-window-timing',
                'node_label': 'Publication window timing',
                'lifecycle_stage': 'trial',
                'status': 'active',
                'mechanism_family': 'publication_timing',
                'source_kind': 'promoted_candidate',
                'path': 'qualitative-db/60-causal-map/nodes/publication-window-timing.md',
            },
            'reporting-state-uncertainty': {
                'node_key': 'reporting-state-uncertainty',
                'node_label': 'Reporting-state uncertainty',
                'lifecycle_stage': 'trial',
                'status': 'active',
                'mechanism_family': 'publication_timing',
                'source_kind': 'promoted_candidate',
                'path': 'qualitative-db/60-causal-map/nodes/reporting-state-uncertainty.md',
            },
        }
        edges = {
            'settlement-source-specificity__increases__resolution-surface-ambiguity': {
                'edge_key': 'settlement-source-specificity__increases__resolution-surface-ambiguity',
                'edge_label': 'Settlement source specificity increases resolution-surface ambiguity',
                'lifecycle_stage': 'active',
                'status': 'active',
                'mechanism_family': 'resolution_surface',
                'source_kind': 'seed',
                'path': 'qualitative-db/60-causal-map/edges/settlement-source-specificity__increases__resolution-surface-ambiguity.md',
            },
            'resolution-surface-ambiguity__increases__verification-caution': {
                'edge_key': 'resolution-surface-ambiguity__increases__verification-caution',
                'edge_label': 'Resolution-surface ambiguity increases verification caution',
                'lifecycle_stage': 'active',
                'status': 'active',
                'mechanism_family': 'resolution_surface',
                'source_kind': 'seed',
                'path': 'qualitative-db/60-causal-map/edges/resolution-surface-ambiguity__increases__verification-caution.md',
            },
            'publication-window-timing__increases__reporting-state-uncertainty': {
                'edge_key': 'publication-window-timing__increases__reporting-state-uncertainty',
                'edge_label': 'Publication window timing increases reporting-state uncertainty',
                'lifecycle_stage': 'trial',
                'status': 'active',
                'mechanism_family': 'publication_timing',
                'source_kind': 'promoted_candidate',
                'path': 'qualitative-db/60-causal-map/edges/publication-window-timing__increases__reporting-state-uncertainty.md',
            },
        }
        node_stats = {
            'settlement-source-specificity': {'learned_weight': 0.42, 'shrunken_uplift': 0.21, 'supporting_case_count': 3, 'helpful_case_count': 2, 'status': 'active'},
            'resolution-surface-ambiguity': {'learned_weight': 0.18, 'shrunken_uplift': 0.05, 'supporting_case_count': 2, 'helpful_case_count': 1, 'status': 'active'},
            'verification-caution': {'learned_weight': 0.06, 'shrunken_uplift': 0.01, 'supporting_case_count': 1, 'helpful_case_count': 0, 'status': 'active'},
            'publication-window-timing': {'learned_weight': 0.1, 'shrunken_uplift': 0.04, 'supporting_case_count': 1, 'helpful_case_count': 0, 'status': 'active'},
            'reporting-state-uncertainty': {'learned_weight': 0.08, 'shrunken_uplift': 0.03, 'supporting_case_count': 1, 'helpful_case_count': 0, 'status': 'active'},
        }
        edge_stats = {
            'settlement-source-specificity__increases__resolution-surface-ambiguity': {'learned_weight': 0.35, 'shrunken_uplift': 0.18, 'supporting_case_count': 3, 'status': 'active'},
            'resolution-surface-ambiguity__increases__verification-caution': {'learned_weight': 0.22, 'shrunken_uplift': 0.08, 'supporting_case_count': 2, 'status': 'active'},
            'publication-window-timing__increases__reporting-state-uncertainty': {'learned_weight': 0.12, 'shrunken_uplift': 0.03, 'supporting_case_count': 1, 'status': 'active'},
        }
        family_state = {
            'resolution_surface': {'trial_total': 0, 'active_nodes': 3, 'active_edges': 2},
            'publication_timing': {'trial_total': 2, 'active_nodes': 0, 'active_edges': 0},
        }
        family_policies = {
            'resolution_surface': {'enabled': True, 'max_trial_candidates': 2, 'max_active_nodes': 4, 'max_active_edges': 3},
            'publication_timing': {'enabled': True, 'max_trial_candidates': 2, 'max_active_nodes': 2, 'max_active_edges': 2},
            'unassigned': {'enabled': False, 'max_trial_candidates': 0, 'max_active_nodes': 0, 'max_active_edges': 0},
        }

        profile, _ = generate_lmd_bundle.infer_live_query_context(
            args,
            nodes,
            edges,
            trial_mode='treatment',
            node_stats=node_stats,
            edge_stats=edge_stats,
            family_state=family_state,
            family_policies=family_policies,
        )

        self.assertEqual(profile['candidate_edges'][0], 'settlement-source-specificity__increases__resolution-surface-ambiguity')
        self.assertEqual(profile['candidate_edge_metadata'][0]['phase11_trust_tier'], 'active_reviewed')
        self.assertGreater(
            profile['candidate_edge_metadata'][0]['phase11_retrieval_score'],
            profile['candidate_edge_metadata'][-1]['phase11_retrieval_score'],
        )
        self.assertIn('phase11_retrieval_score', profile['active_node_metadata'][0])
        self.assertEqual(profile['active_node_metadata'][0]['node_key'], 'settlement-source-specificity')


    def test_shortlist_active_interventions_emits_phase11_breakdown(self) -> None:
        query_profile = {
            'source_of_truth_class': 'authoritative_with_fallback',
            'question_mechanics': ['publication-timing'],
            'platform': 'kalshi',
            'category': 'macro',
            'required_checks': [{'check_key': 'governing_source'}],
            'active_nodes': ['settlement-source-specificity'],
            'active_node_metadata': [
                {
                    'node_key': 'settlement-source-specificity',
                    'phase11_retrieval_score': 1.2,
                    'phase11_trust_tier': 'active_reviewed',
                }
            ],
            'candidate_edges': ['publication-window-timing__increases__reporting-state-uncertainty'],
            'candidate_edge_metadata': [
                {
                    'edge_key': 'publication-window-timing__increases__reporting-state-uncertainty',
                    'phase11_retrieval_score': 0.8,
                    'phase11_trust_tier': 'trial_experimental',
                }
            ],
            'contested_edges': [],
        }

        records = {
            'alpha.md': {
                'intervention_key': 'alpha',
                'path': 'alpha.md',
                'status': 'active',
                'application_surface': 'researcher_prompt',
                'change_kind': 'verification_rule',
                'target_selector': {
                    'source_of_truth_classes': ['authoritative_with_fallback'],
                    'question_mechanics': ['publication-timing'],
                    'platforms': ['kalshi'],
                    'categories': ['macro'],
                },
                'change_payload': {'required_checks': ['governing_source']},
            },
            'beta.md': {
                'intervention_key': 'beta',
                'path': 'beta.md',
                'status': 'active',
                'application_surface': 'researcher_prompt',
                'change_kind': 'verification_rule',
                'target_selector': {
                    'source_of_truth_classes': ['authoritative_with_fallback'],
                    'question_mechanics': ['publication-timing'],
                    'platforms': ['kalshi'],
                    'categories': ['macro'],
                },
                'change_payload': {'required_checks': []},
            },
        }

        with patch.object(generate_lmd_bundle, 'intervention_note_paths', return_value=['alpha.md', 'beta.md']), patch.object(
            generate_lmd_bundle,
            'build_intervention_record',
            side_effect=lambda path: records[path],
        ):
            selected = generate_lmd_bundle.shortlist_active_interventions(query_profile, {})

        self.assertEqual(selected[0]['intervention_key'], 'alpha')
        self.assertIn('score_breakdown', selected[0])
        self.assertGreater(selected[0]['score_breakdown']['required_check_bonus'], 0.0)
        self.assertGreater(selected[0]['score_breakdown']['phase11_source_live_bonus'], 0.0)

    def test_select_aggregate_notes_emits_phase11_breakdown(self) -> None:
        query_profile = {
            'active_nodes': ['settlement-source-specificity', 'resolution-surface-ambiguity'],
            'active_node_metadata': [
                {
                    'node_key': 'settlement-source-specificity',
                    'phase11_retrieval_score': 1.3,
                    'phase11_trust_tier': 'active_reviewed',
                },
                {
                    'node_key': 'resolution-surface-ambiguity',
                    'phase11_retrieval_score': 0.9,
                    'phase11_trust_tier': 'active_reviewed',
                },
            ],
            'candidate_edges': ['settlement-source-specificity__increases__resolution-surface-ambiguity'],
            'candidate_edge_metadata': [
                {
                    'edge_key': 'settlement-source-specificity__increases__resolution-surface-ambiguity',
                    'phase11_retrieval_score': 0.7,
                    'phase11_trust_tier': 'active_reviewed',
                }
            ],
            'contested_edges': [],
        }
        notes = generate_lmd_bundle.select_aggregate_notes(query_profile, {})
        self.assertEqual(notes[0]['path'], 'qualitative-db/50-learnings/source-performance/generated-index.md')
        self.assertIn('score_breakdown', notes[0])
        self.assertGreater(notes[0]['score_breakdown']['phase11_source_live_bonus'], 0.0)

    def test_build_bundle_debug_includes_phase11_breakdowns(self) -> None:
        args = self.make_args()
        args.case_key = 'case-phase11-debug'
        args.market_id = 'test-market'
        args.db_url = ''
        args.psql = '/opt/homebrew/opt/postgresql@16/bin/psql'
        args.generator_version = generate_lmd_bundle.GENERATOR_VERSION
        args.policy_version = generate_lmd_bundle.POLICY_VERSION
        args.allow_same_case = False
        args.pretty = False
        args.dry_run = True
        args.prior_dispatch_count = 0
        args.prior_case_count = 0

        nodes = {
            'settlement-source-specificity': {
                'node_key': 'settlement-source-specificity',
                'node_label': 'Settlement source specificity',
                'lifecycle_stage': 'active',
                'status': 'active',
                'mechanism_family': 'resolution_surface',
                'source_kind': 'seed',
                'path': 'qualitative-db/60-causal-map/nodes/settlement-source-specificity.md',
            },
            'resolution-surface-ambiguity': {
                'node_key': 'resolution-surface-ambiguity',
                'node_label': 'Resolution surface ambiguity',
                'lifecycle_stage': 'active',
                'status': 'active',
                'mechanism_family': 'resolution_surface',
                'source_kind': 'seed',
                'path': 'qualitative-db/60-causal-map/nodes/resolution-surface-ambiguity.md',
            },
        }
        edges = {
            'settlement-source-specificity__increases__resolution-surface-ambiguity': {
                'edge_key': 'settlement-source-specificity__increases__resolution-surface-ambiguity',
                'edge_label': 'Settlement source specificity increases resolution surface ambiguity',
                'lifecycle_stage': 'active',
                'status': 'active',
                'mechanism_family': 'resolution_surface',
                'source_kind': 'seed',
                'path': 'qualitative-db/60-causal-map/edges/settlement-source-specificity__increases__resolution-surface-ambiguity.md',
            }
        }
        case_candidates = [
            {
                'case_key': 'resolved-1',
                'review_path': 'review.md',
                'packet_path': 'packet.md',
                'title_text': 'Official source ambiguity affected resolution',
                'active_nodes': ['settlement-source-specificity'],
                'candidate_edges': ['settlement-source-specificity__increases__resolution-surface-ambiguity'],
                'question_mechanics': [],
                'source_of_truth_class': ['authoritative_with_fallback'],
                'category': 'macro',
                'required_checks': [{'check_key': 'governing_source'}],
            }
        ]

        with patch.object(generate_lmd_bundle, 'load_graph', return_value=(nodes, edges)), patch.object(
            generate_lmd_bundle,
            'load_learned_stats',
            return_value=(
                {'case_review:resolved-1': {'learned_weight': 0.2, 'shrunken_uplift': 0.1, 'status': 'active'}},
                {'settlement-source-specificity__increases__resolution-surface-ambiguity': {'learned_weight': 0.3, 'shrunken_uplift': 0.12, 'supporting_case_count': 2, 'status': 'active'}},
                {
                    'settlement-source-specificity': {'learned_weight': 0.4, 'shrunken_uplift': 0.15, 'supporting_case_count': 2, 'helpful_case_count': 1, 'status': 'active'},
                    'resolution-surface-ambiguity': {'learned_weight': 0.2, 'shrunken_uplift': 0.08, 'supporting_case_count': 1, 'helpful_case_count': 0, 'status': 'active'},
                },
                {'candidate_stats': True, 'edge_stats': True, 'node_stats': True},
            ),
        ), patch.object(
            generate_lmd_bundle,
            'load_family_policies',
            return_value={
                'resolution_surface': {'enabled': True, 'max_trial_candidates': 2, 'max_active_nodes': 3, 'max_active_edges': 2},
                'unassigned': {'enabled': False, 'max_trial_candidates': 0, 'max_active_nodes': 0, 'max_active_edges': 0},
            },
        ), patch.object(
            generate_lmd_bundle,
            'load_case_review_candidates',
            return_value=case_candidates,
        ), patch.object(
            generate_lmd_bundle,
            'shortlist_active_interventions',
            return_value=[{'intervention_key': 'alpha', 'path': 'alpha.md', 'retrieval_score': 3.1, 'score_breakdown': {'selector_match_score': 2.0}, 'required_checks': []}],
        ), patch.object(
            generate_lmd_bundle,
            'select_aggregate_notes',
            return_value=[{'path': 'qualitative-db/50-learnings/source-performance/generated-index.md', 'retrieval_score': 2.4, 'score_breakdown': {'shared_source_family': 2.4}}],
        ), patch.object(
            generate_lmd_bundle,
            'compile_required_checks',
            return_value=[{'check_key': 'governing_source'}],
        ), patch.object(
            generate_lmd_bundle,
            'evaluate_trial_candidates',
            return_value={'enabled': True, 'preview_only': True, 'overlay_mode': 'preview_only', 'selection_caps': {}, 'selected_candidates': [], 'selected_count': 0},
        ):
            bundle = generate_lmd_bundle.build_bundle(args)

        phase11 = (bundle.get('debug') or {}).get('phase11') or {}
        self.assertIn('live_nodes_ranked', phase11)
        self.assertIn('case_review_scores', phase11)
        self.assertIn('intervention_scores', phase11)
        self.assertIn('aggregate_note_scores', phase11)
        self.assertIn('score_breakdown', phase11['case_review_scores'][0])
        self.assertIn('score_breakdown', phase11['intervention_scores'][0])
        self.assertIn('score_breakdown', phase11['aggregate_note_scores'][0])

    def test_trial_overlay_selection_uses_dynamic_caps_when_live_trial_items_present(self) -> None:
        bundle = {
            'query_profile': {
                'source_of_truth_class': 'authoritative_with_fallback',
                'platform': 'kalshi',
                'category': 'macro',
                'question_mechanics': ['publication-timing'],
            },
            'causal_context': {
                'active_nodes': ['publication-window-timing'],
                'active_node_metadata': [
                    {
                        'node_key': 'publication-window-timing',
                        'lifecycle_stage': 'trial',
                        'mechanism_family': 'publication_timing',
                    }
                ],
                'matched_edges': [],
                'matched_edge_metadata': [],
                'contested_edges': [],
                'required_checks': [],
            },
            'retrieval_policy': {
                'live_graph_family_state': {
                    'publication_timing': {'trial_total': 2, 'active_nodes': 0, 'active_edges': 0},
                    'resolution_surface': {'trial_total': 0, 'active_nodes': 1, 'active_edges': 1},
                },
                'live_graph_family_policy_caps': {
                    'publication_timing': {'max_trial_candidates': 2, 'max_active_nodes': 2, 'max_active_edges': 2},
                    'resolution_surface': {'max_trial_candidates': 2, 'max_active_nodes': 2, 'max_active_edges': 2},
                },
            },
        }
        proposals = {
            'proposals': [
                {
                    'proposal_id': 'p1',
                    'proposal_key': 'publication-timing-trial-a',
                    'candidate_type': 'node',
                    'mechanism_family': 'publication_timing',
                    'dominant_proposal_source': 'projection',
                    'promotion_status': 'trial_candidate',
                    'lifecycle_stage': 'trial_candidate',
                    'trial_readiness': {'eligible': True},
                    'merge_recommended': False,
                    'shadow_trial_score': 0.6,
                    'trial_shrunken_utility': 0.2,
                    'trial_helpful_count': 1,
                    'trial_harmful_rate': 0.0,
                    'shadow_helpful_count': 2,
                    'shadow_harmful_count': 0,
                    'shadow_judged_count': 2,
                    'non_intervention_support_case_count': 2,
                    'distinct_case_count': 3,
                    'genericity_penalty': 0.1,
                    'family_trial_rank': 1,
                    'stats_metadata': {'observed_active_nodes': ['publication-window-timing']},
                    'context_distribution': {'question_mechanics': {'publication-timing': 2}},
                },
                {
                    'proposal_id': 'p2',
                    'proposal_key': 'resolution-surface-trial-b',
                    'candidate_type': 'node',
                    'mechanism_family': 'resolution_surface',
                    'dominant_proposal_source': 'projection',
                    'promotion_status': 'trial_candidate',
                    'lifecycle_stage': 'trial_candidate',
                    'trial_readiness': {'eligible': True},
                    'merge_recommended': False,
                    'shadow_trial_score': 0.58,
                    'trial_shrunken_utility': 0.18,
                    'trial_helpful_count': 1,
                    'trial_harmful_rate': 0.0,
                    'shadow_helpful_count': 2,
                    'shadow_harmful_count': 0,
                    'shadow_judged_count': 2,
                    'non_intervention_support_case_count': 2,
                    'distinct_case_count': 3,
                    'genericity_penalty': 0.1,
                    'family_trial_rank': 1,
                    'stats_metadata': {'observed_active_nodes': ['publication-window-timing']},
                    'context_distribution': {'question_mechanics': {'publication-timing': 2}},
                },
            ]
        }
        with tempfile.TemporaryDirectory() as tmpdir:
            summary_path = Path(tmpdir) / 'summary.json'
            summary_path.write_text(json.dumps(proposals) + '\n', encoding='utf-8')
            overlay = trial_selection.evaluate_trial_candidates(bundle, limit=2, summary_path=summary_path)

        self.assertEqual(overlay['selection_caps']['current_live_trial_item_count'], 1)
        self.assertEqual(overlay['selection_caps']['max_selected_total'], 1)
        self.assertEqual(overlay['selected_count'], 1)
        self.assertEqual(overlay['selected_candidates'][0]['proposal_key'], 'resolution-surface-trial-b')


if __name__ == '__main__':
    unittest.main()
