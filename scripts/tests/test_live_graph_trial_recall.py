from __future__ import annotations

import importlib
import importlib.util
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path

TEST_DIR = Path(__file__).resolve().parent
REPO_ROOT = TEST_DIR.parents[1]
PLANNER_SCRIPTS_DIR = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'planner' / 'scripts'
RUNTIME_ROOT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime'
RUNTIME_SCRIPTS_DIR = RUNTIME_ROOT / 'scripts'

for candidate in [PLANNER_SCRIPTS_DIR, RUNTIME_ROOT, RUNTIME_SCRIPTS_DIR]:
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


generate_lmd_bundle = load_module(
    'generate_lmd_bundle_for_live_graph_trial_tests',
    PLANNER_SCRIPTS_DIR / 'generate_lmd_bundle.py',
)
build_researcher_prompt = load_module(
    'build_researcher_prompt_for_live_graph_trial_tests',
    PLANNER_SCRIPTS_DIR / 'build_researcher_prompt.py',
)
lmd_lib = importlib.import_module('lib.lmd')
elevate_live_graph_drafts = load_module(
    'elevate_live_graph_drafts_for_tests',
    RUNTIME_SCRIPTS_DIR / 'elevate_live_causal_graph_drafts_to_trial.py',
)


class LiveGraphTrialRecallTests(unittest.TestCase):
    def make_args(self) -> types.SimpleNamespace:
        return types.SimpleNamespace(
            title='Will the official report be released this week?',
            description='Resolution depends on an official publication timing window.',
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
            experiment_arm='control',
            live_graph_trial_mode='auto',
        )

    def test_trial_nodes_are_suppressed_outside_trial_modes(self) -> None:
        args = self.make_args()
        nodes = {
            'publication-window-timing': {
                'node_key': 'publication-window-timing',
                'node_label': 'Publication window timing',
                'lifecycle_stage': 'trial',
                'status': 'active',
                'source_kind': 'promoted_candidate',
                'path': 'qualitative-db/60-causal-map/nodes/publication-window-timing.md',
            },
            'reporting-state-uncertainty': {
                'node_key': 'reporting-state-uncertainty',
                'node_label': 'Reporting-state uncertainty',
                'lifecycle_stage': 'trial',
                'status': 'active',
                'source_kind': 'promoted_candidate',
                'path': 'qualitative-db/60-causal-map/nodes/reporting-state-uncertainty.md',
            },
        }
        edges = {
            'publication-window-timing__increases__reporting-state-uncertainty': {
                'edge_key': 'publication-window-timing__increases__reporting-state-uncertainty',
                'edge_label': 'Publication window timing increases reporting-state uncertainty',
                'lifecycle_stage': 'trial',
                'status': 'active',
                'source_kind': 'promoted_candidate',
                'path': 'qualitative-db/60-causal-map/edges/publication-window-timing__increases__reporting-state-uncertainty.md',
            }
        }

        profile, debug = generate_lmd_bundle.infer_live_query_context(args, nodes, edges, trial_mode='off')

        self.assertEqual(profile['active_nodes'], [])
        self.assertEqual(profile['candidate_edges'], [])
        self.assertFalse(profile['live_graph_trial_enabled'])
        self.assertEqual(profile['live_graph_recallable_stages'], ['active'])
        self.assertIn('publication-window-timing', debug['suppressed_node_reasons'])
        self.assertIn('reporting-state-uncertainty', debug['suppressed_node_reasons'])

    def test_trial_nodes_are_recalled_in_treatment_mode(self) -> None:
        args = self.make_args()
        nodes = {
            'publication-window-timing': {
                'node_key': 'publication-window-timing',
                'node_label': 'Publication window timing',
                'lifecycle_stage': 'trial',
                'status': 'active',
                'source_kind': 'promoted_candidate',
                'path': 'qualitative-db/60-causal-map/nodes/publication-window-timing.md',
            },
            'reporting-state-uncertainty': {
                'node_key': 'reporting-state-uncertainty',
                'node_label': 'Reporting-state uncertainty',
                'lifecycle_stage': 'trial',
                'status': 'active',
                'source_kind': 'promoted_candidate',
                'path': 'qualitative-db/60-causal-map/nodes/reporting-state-uncertainty.md',
            },
        }
        edges = {
            'publication-window-timing__increases__reporting-state-uncertainty': {
                'edge_key': 'publication-window-timing__increases__reporting-state-uncertainty',
                'edge_label': 'Publication window timing increases reporting-state uncertainty',
                'lifecycle_stage': 'trial',
                'status': 'active',
                'source_kind': 'promoted_candidate',
                'mechanism_family': 'publication_timing',
                'path': 'qualitative-db/60-causal-map/edges/publication-window-timing__increases__reporting-state-uncertainty.md',
            }
        }

        profile, debug = generate_lmd_bundle.infer_live_query_context(args, nodes, edges, trial_mode='treatment')

        self.assertEqual(
            profile['active_nodes'],
            ['publication-window-timing', 'reporting-state-uncertainty'],
        )
        self.assertEqual(
            profile['candidate_edges'],
            ['publication-window-timing__increases__reporting-state-uncertainty'],
        )
        self.assertTrue(profile['live_graph_trial_enabled'])
        self.assertEqual(profile['live_graph_recallable_stages'], ['active', 'trial'])
        self.assertEqual(profile['candidate_edge_metadata'][0]['lifecycle_stage'], 'trial')
        self.assertEqual(debug['suppressed_node_reasons'], {})
        self.assertEqual(debug['suppressed_edge_reasons'], {})

    def test_prompt_render_marks_trial_causal_focus(self) -> None:
        line = build_researcher_prompt.render_causal_focus_line(
            'publication-window-timing__increases__reporting-state-uncertainty',
            set(),
            {'lifecycle_stage': 'trial'},
        )
        self.assertIn('(trial)', line)

    def test_prompt_discloses_trial_node_without_trial_edge(self) -> None:
        section, _ = build_researcher_prompt.render_lmd_section(
            {
                'lmd_bundle': {
                    'lmd_used': True,
                    'results': {
                        'case_reviews': [],
                        'active_interventions': [],
                        'required_checks': [],
                    },
                    'causal_context': {
                        'active_nodes': ['publication-window-timing'],
                        'active_node_metadata': [
                            {
                                'node_key': 'publication-window-timing',
                                'node_label': 'Publication window timing',
                                'lifecycle_stage': 'trial',
                                'path': 'qualitative-db/60-causal-map/nodes/publication-window-timing.md',
                            }
                        ],
                        'matched_edges': [],
                        'matched_edge_metadata': [],
                        'contested_edges': [],
                    },
                }
            }
        )
        self.assertIn('experimental_trial_nodes:', section)
        self.assertIn('Publication window timing (trial)', section)

    def test_bundle_candidates_include_node_only_trial_matches(self) -> None:
        candidates = lmd_lib.bundle_candidates(
            {
                'results': {
                    'case_reviews': [],
                    'active_interventions': [],
                    'aggregate_notes': [],
                    'required_checks': [],
                },
                'causal_context': {
                    'active_nodes': ['publication-window-timing'],
                    'active_node_metadata': [
                        {
                            'node_key': 'publication-window-timing',
                            'node_label': 'Publication window timing',
                            'lifecycle_stage': 'trial',
                            'source_kind': 'promoted_candidate',
                            'mechanism_family': 'publication_timing',
                            'path': 'qualitative-db/60-causal-map/nodes/publication-window-timing.md',
                        }
                    ],
                    'matched_edges': [],
                    'matched_edge_metadata': [],
                    'contested_edges': [],
                },
            }
        )
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]['candidate_type'], 'node')
        self.assertEqual(candidates[0]['notes']['lifecycle_stage'], 'trial')
        self.assertTrue(candidates[0]['notes']['node_only_trial_disclosure'])

    def test_apply_transition_promotes_draft_note_and_sidecar(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            note_path = root / 'publication-window-timing.md'
            sidecar_path = root / 'publication-window-timing.json'
            note_path.write_text(
                '---\n'
                'type: causal_node\n'
                'node_key: publication-window-timing\n'
                'status: draft\n'
                'lifecycle_stage: draft\n'
                'source_kind: promoted_candidate\n'
                'evidence_status: experimental_draft\n'
                '---\n\n'
                '# Publication window timing\n\n'
                'Body text.\n',
                encoding='utf-8',
            )
            sidecar_path.write_text(
                json.dumps(
                    {
                        'artifact_type': 'causal_node',
                        'schema_version': 'v1',
                        'node_key': 'publication-window-timing',
                        'source_kind': 'promoted_candidate',
                        'lifecycle_stage': 'draft',
                        'evidence_status': 'experimental_draft',
                    }
                )
                + '\n',
                encoding='utf-8',
            )
            entry = {
                'entity_type': 'node',
                'note_path': note_path,
                'record': {
                    'node_key': 'publication-window-timing',
                    'status': 'draft',
                    'lifecycle_stage': 'draft',
                    'note_frontmatter': elevate_live_graph_drafts.parse_frontmatter(note_path.read_text(encoding='utf-8')),
                    'mechanism_family': 'publication_timing',
                    'source_kind': 'promoted_candidate',
                },
            }

            result = elevate_live_graph_drafts.apply_transition(
                entry,
                transitioned_at='2026-04-15T21:00:00Z',
                dry_run=False,
            )

            updated_frontmatter = elevate_live_graph_drafts.parse_frontmatter(note_path.read_text(encoding='utf-8'))
            updated_sidecar = json.loads(sidecar_path.read_text(encoding='utf-8'))

        self.assertEqual(result['status'], 'updated')
        self.assertEqual(updated_frontmatter['status'], 'active')
        self.assertEqual(updated_frontmatter['lifecycle_stage'], 'trial')
        self.assertEqual(updated_frontmatter['evidence_status'], 'experimental_trial')
        self.assertEqual(updated_sidecar['lifecycle_stage'], 'trial')
        self.assertEqual(updated_sidecar['status'], 'active')
        self.assertEqual(updated_sidecar['evidence_status'], 'experimental_trial')


if __name__ == '__main__':
    unittest.main()
