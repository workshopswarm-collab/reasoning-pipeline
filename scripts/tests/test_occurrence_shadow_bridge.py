from __future__ import annotations

import importlib
import importlib.util
import sys
import unittest
from pathlib import Path

TEST_DIR = Path(__file__).resolve().parent
REPO_ROOT = TEST_DIR.parents[1]
RUNTIME_ROOT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime'

if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))

bridge = importlib.import_module('lib.occurrence_shadow_bridge')
CLAMP_SCRIPT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime' / 'scripts' / 'clamp_occurrence_bridge_screening.py'
clamp_spec = importlib.util.spec_from_file_location('clamp_occurrence_bridge_screening_for_tests', CLAMP_SCRIPT)
if clamp_spec is None or clamp_spec.loader is None:
    raise RuntimeError(f'could not import clamp script from {CLAMP_SCRIPT}')
clamp = importlib.util.module_from_spec(clamp_spec)
clamp_spec.loader.exec_module(clamp)
REPORT_SCRIPT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime' / 'scripts' / 'report_occurrence_bridge_shadow_evidence.py'
report_spec = importlib.util.spec_from_file_location('report_occurrence_bridge_shadow_evidence_for_tests', REPORT_SCRIPT)
if report_spec is None or report_spec.loader is None:
    raise RuntimeError(f'could not import report script from {REPORT_SCRIPT}')
report = importlib.util.module_from_spec(report_spec)
report_spec.loader.exec_module(report)


class OccurrenceShadowBridgeTests(unittest.TestCase):
    def test_build_shadow_bridge_rows_only_includes_enabled_generated_families(self) -> None:
        packets = [
            {
                'candidate_slug': 'threshold-proximity',
                'candidate_label': 'threshold-proximity',
                'packet_key': 'occurrence-packet:threshold-proximity',
                'packet_hash': 'hash-threshold',
                'compiler_version': 'test',
                'candidate_note_path': 'qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/generated-driver-candidate-threshold-proximity.md',
                'source_summary': {
                    'source_occurrence_count': 5,
                    'distinct_case_count': 2,
                    'distinct_persona_count': 2,
                },
                'source_occurrences': [
                    {
                        'case_key': 'case-1',
                        'artifact_path': 'reviews/case-1/review.md',
                        'persona': 'base',
                        'artifact_kind': 'research_note',
                        'proposed_driver_label': 'threshold proximity',
                        'source_of_truth_class': 'price_path',
                    },
                    {
                        'case_key': 'case-2',
                        'artifact_path': 'reviews/case-2/review.md',
                        'persona': 'skeptic',
                        'artifact_kind': 'research_note',
                        'proposed_driver_label': 'threshold proximity',
                        'source_of_truth_class': 'price_path',
                    },
                ],
            },
            {
                'candidate_slug': 'alliance-cohesion',
                'candidate_label': 'alliance-cohesion',
                'packet_key': 'occurrence-packet:alliance-cohesion',
                'packet_hash': 'hash-alliance',
                'compiler_version': 'test',
                'candidate_note_path': 'candidate-notes/generated-driver-candidate-alliance-cohesion.md',
                'source_summary': {
                    'source_occurrence_count': 2,
                    'distinct_case_count': 1,
                    'distinct_persona_count': 1,
                },
                'source_occurrences': [
                    {
                        'case_key': 'case-3',
                        'artifact_path': 'reviews/case-3/review.md',
                        'persona': 'base',
                        'artifact_kind': 'research_note',
                        'proposed_driver_label': 'alliance cohesion',
                        'source_of_truth_class': 'qualitative',
                    }
                ],
            },
        ]
        registry_payload = {
            'families': [
                {
                    'family_key': 'prov:threshold_touch:resolution-mechanics',
                    'family_state': 'provisional',
                    'canonical_family': 'threshold_touch',
                    'source_family_slug': 'resolution-mechanics',
                    'bridge_status': 'mapped_provisional',
                    'distinct_case_count': 8,
                    'candidate_count': 4,
                    'source_occurrence_count': 25,
                },
                {
                    'family_key': 'prov:novel:alliance-cohesion',
                    'family_state': 'provisional',
                    'canonical_family': 'unassigned',
                    'source_family_slug': 'alliance-cohesion',
                    'bridge_status': 'novel_provisional',
                    'distinct_case_count': 1,
                    'candidate_count': 1,
                    'source_occurrence_count': 2,
                },
            ],
            'members': [
                {'family_key': 'prov:threshold_touch:resolution-mechanics', 'candidate_slug': 'threshold-proximity'},
                {'family_key': 'prov:novel:alliance-cohesion', 'candidate_slug': 'alliance-cohesion'},
            ],
        }
        generated_policy_payload = {
            'policies': [
                {
                    'mechanism_family': 'prov:threshold_touch:resolution-mechanics',
                    'enabled': True,
                    'max_shadow_candidates': 2,
                    'policy_source': 'generated_provisional_shadow',
                    'health_score': 0.71,
                    'evidence_mass': 25,
                    'policy_notes': {'canonical_family': 'threshold_touch', 'lineage_parent_family_key': 'threshold_touch'},
                },
                {
                    'mechanism_family': 'prov:novel:alliance-cohesion',
                    'enabled': False,
                    'max_shadow_candidates': 0,
                    'policy_source': 'generated_provisional_shadow',
                    'health_score': 0.12,
                    'evidence_mass': 2,
                    'policy_notes': {'canonical_family': 'unassigned', 'lineage_parent_family_key': 'unassigned'},
                },
            ]
        }

        payload = bridge.build_shadow_bridge_rows(
            packets=packets,
            registry_payload=registry_payload,
            generated_policies_payload=generated_policy_payload,
        )

        self.assertEqual(payload['row_count'], 2)
        self.assertEqual(payload['enabled_family_count'], 1)
        self.assertEqual(payload['bridged_family_counts'], {'prov:threshold_touch:resolution-mechanics': 2})
        self.assertEqual(payload['allowed_candidate_counts'], {'prov:threshold_touch:resolution-mechanics': 1})
        rows = payload['rows']
        self.assertEqual({row['case_key'] for row in rows}, {'case-1', 'case-2'})
        self.assertTrue(all(row['mechanism_family'] == 'prov:threshold_touch:resolution-mechanics' for row in rows))
        self.assertTrue(all(row['candidate_type'] == 'node' for row in rows))
        self.assertTrue(all(row['proposal_id'] == 'node:threshold-proximity' for row in rows))
        self.assertEqual(rows[0]['candidate_label'], 'Threshold Proximity')
        self.assertEqual(rows[0]['context_snapshot']['question_mechanics'], ['threshold_touch'])
        self.assertEqual(rows[0]['proposal_metadata']['bridge_source'], 'occurrence_packet_shadow_bridge')
        self.assertEqual(rows[0]['proposal_metadata']['family_shadow_budget'], 2)
        self.assertTrue(any(item['reason'] == 'family_policy_not_enabled' for item in payload['skipped']))

    def test_build_shadow_bridge_rows_respects_family_shadow_budget(self) -> None:
        packets = [
            {
                'candidate_slug': 'threshold-proximity',
                'candidate_label': 'threshold-proximity',
                'packet_key': 'occurrence-packet:threshold-proximity',
                'packet_hash': 'hash-threshold',
                'compiler_version': 'test',
                'candidate_note_path': 'candidate-notes/generated-driver-candidate-threshold-proximity.md',
                'source_summary': {
                    'source_occurrence_count': 7,
                    'distinct_case_count': 3,
                    'distinct_persona_count': 2,
                },
                'source_occurrences': [
                    {
                        'case_key': 'case-1',
                        'artifact_path': 'reviews/case-1/review.md',
                        'persona': 'base',
                        'artifact_kind': 'research_note',
                        'proposed_driver_label': 'threshold proximity',
                        'source_of_truth_class': 'price_path',
                    }
                ],
            },
            {
                'candidate_slug': 'threshold-close-mechanics',
                'candidate_label': 'threshold-close-mechanics',
                'packet_key': 'occurrence-packet:threshold-close-mechanics',
                'packet_hash': 'hash-threshold-close',
                'compiler_version': 'test',
                'candidate_note_path': 'candidate-notes/generated-driver-candidate-threshold-close-mechanics.md',
                'source_summary': {
                    'source_occurrence_count': 4,
                    'distinct_case_count': 2,
                    'distinct_persona_count': 1,
                },
                'source_occurrences': [
                    {
                        'case_key': 'case-2',
                        'artifact_path': 'reviews/case-2/review.md',
                        'persona': 'skeptic',
                        'artifact_kind': 'research_note',
                        'proposed_driver_label': 'threshold close mechanics',
                        'source_of_truth_class': 'price_path',
                    }
                ],
            },
        ]
        registry_payload = {
            'families': [
                {
                    'family_key': 'prov:threshold_touch:resolution-mechanics',
                    'family_state': 'provisional',
                    'canonical_family': 'threshold_touch',
                    'source_family_slug': 'resolution-mechanics',
                    'bridge_status': 'mapped_provisional',
                    'distinct_case_count': 8,
                    'candidate_count': 2,
                    'source_occurrence_count': 18,
                },
            ],
            'members': [
                {'family_key': 'prov:threshold_touch:resolution-mechanics', 'candidate_slug': 'threshold-proximity'},
                {'family_key': 'prov:threshold_touch:resolution-mechanics', 'candidate_slug': 'threshold-close-mechanics'},
            ],
        }
        generated_policy_payload = {
            'policies': [
                {
                    'mechanism_family': 'prov:threshold_touch:resolution-mechanics',
                    'enabled': True,
                    'max_shadow_candidates': 1,
                    'policy_source': 'generated_provisional_shadow',
                    'health_score': 0.82,
                    'evidence_mass': 18,
                    'policy_notes': {'canonical_family': 'threshold_touch', 'lineage_parent_family_key': 'threshold_touch'},
                },
            ]
        }

        payload = bridge.build_shadow_bridge_rows(
            packets=packets,
            registry_payload=registry_payload,
            generated_policies_payload=generated_policy_payload,
        )

        self.assertEqual(payload['row_count'], 1)
        self.assertEqual(payload['allowed_candidate_counts'], {'prov:threshold_touch:resolution-mechanics': 1})
        self.assertEqual([row['proposal_key'] for row in payload['rows']], ['threshold-proximity'])
        self.assertTrue(any(item['reason'] == 'family_shadow_budget_exhausted' and item['candidate_slug'] == 'threshold-close-mechanics' for item in payload['skipped']))

    def test_clamp_demotes_judged_non_positive_bridge_rows_back_to_aggregated(self) -> None:
        row = {
            'lifecycle_stage': 'shadow_candidate',
            'shadow_match_count': 2,
            'shadow_judged_count': 2,
            'shadow_positive_count': 0,
        }
        self.assertEqual(clamp.clamped_lifecycle_stage(row), 'aggregated')

    def test_clamp_keeps_pending_unjudged_bridge_rows_in_shadow_stage(self) -> None:
        row = {
            'lifecycle_stage': 'shadow_candidate',
            'shadow_match_count': 2,
            'shadow_judged_count': 0,
            'shadow_positive_count': 0,
        }
        self.assertEqual(clamp.clamped_lifecycle_stage(row), 'shadow_candidate')

    def test_report_marks_bridge_dominant_rows(self) -> None:
        row = {
            'dominant_proposal_source': report.PROPOSAL_SOURCE,
            'proposal_source_mix': {
                report.PROPOSAL_SOURCE: 3,
                'case_extractor': 1,
            },
        }
        self.assertEqual(report.bridge_membership(row), 'bridge_dominant')

    def test_report_marks_mixed_source_bridge_rows_as_participants(self) -> None:
        row = {
            'dominant_proposal_source': 'case_extractor',
            'proposal_source_mix': {
                report.PROPOSAL_SOURCE: 1,
                'case_extractor': 2,
            },
        }
        self.assertEqual(report.bridge_membership(row), 'bridge_participant')


if __name__ == '__main__':
    unittest.main()
