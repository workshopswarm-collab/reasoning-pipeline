from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

TEST_DIR = Path(__file__).resolve().parent
REPO_ROOT = TEST_DIR.parents[1]
RUNTIME_ROOT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime'

if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))

compiler = importlib.import_module('lib.proposed_driver_occurrence_compiler')


class OccurrenceBackedCompilerTests(unittest.TestCase):
    def test_resolve_occurrence_source_db_url_prefers_orchestrator_lane(self) -> None:
        with patch.object(compiler, 'maybe_load_workspace_env', lambda: None):
            with patch.dict(
                'os.environ',
                {
                    'PREDQUANT_EVAL_URL': 'postgres://eval-role/predquant',
                    'PREDQUANT_ORCHESTRATOR_URL': 'postgres://orchestrator-role/predquant',
                },
                clear=True,
            ):
                self.assertEqual(
                    compiler.resolve_occurrence_source_db_url(),
                    'postgres://orchestrator-role/predquant',
                )

    def test_compile_occurrence_packets_prefers_generated_index_family_hint(self) -> None:
        rows = [
            {
                'artifact_path': 'cases/case-1/notes/a.md',
                'proposed_driver_label': 'Publication timing uncertainty',
                'proposed_driver_slug': 'publication-timing-uncertainty',
                'case_key': 'case-1',
                'dispatch_id': 'dispatch-1',
                'research_run_id': 'run-1',
                'persona': 'skeptic',
                'artifact_kind': 'research_note',
                'related_entities': ['fed'],
                'related_canonical_drivers': ['publication_timing'],
                'canonical_driver_suggestions': ['publication_timing'],
                'difficulty_class': 'medium',
                'source_of_truth_class': 'authoritative_with_fallback',
                'status': 'active',
                'occurred_at': '2026-04-16T20:00:00Z',
            },
            {
                'artifact_path': 'cases/case-2/notes/b.md',
                'proposed_driver_label': 'Publication timing uncertainty',
                'proposed_driver_slug': 'publication-timing-uncertainty',
                'case_key': 'case-2',
                'dispatch_id': 'dispatch-2',
                'research_run_id': 'run-2',
                'persona': 'base',
                'artifact_kind': 'research_note',
                'related_entities': ['bls'],
                'related_canonical_drivers': ['publication_timing'],
                'canonical_driver_suggestions': ['publication_timing'],
                'difficulty_class': 'medium',
                'source_of_truth_class': 'authoritative_with_fallback',
                'status': 'active',
                'occurred_at': '2026-04-16T21:00:00Z',
            },
        ]
        index_payload = {
            'candidates': [
                {
                    'candidate_slug': 'publication-timing-uncertainty',
                    'candidate_label': 'Publication timing uncertainty',
                    'candidate_note_path': 'candidate-notes/generated-driver-candidate-publication-timing-uncertainty.md',
                    'normalized_family': 'publication_timing',
                    'canon_coverage_status': 'matched',
                    'canon_coverage_driver': 'publication_timing',
                }
            ]
        }

        packets = compiler.compile_occurrence_packets(rows, index_payload)
        self.assertEqual(len(packets), 1)
        packet = packets[0]
        self.assertEqual(packet['normalized_family'], 'publication_timing')
        self.assertEqual(packet['family_assignment_source'], 'generated_index')
        self.assertEqual(packet['source_summary']['distinct_case_count'], 2)
        self.assertEqual(packet['source_summary']['distinct_persona_count'], 2)
        self.assertEqual(packet['candidate_note_path'], 'candidate-notes/generated-driver-candidate-publication-timing-uncertainty.md')

    def test_compile_occurrence_packets_falls_back_to_slug_when_no_hint(self) -> None:
        rows = [
            {
                'artifact_path': 'cases/case-1/notes/a.md',
                'proposed_driver_label': 'Verification-state separation',
                'proposed_driver_slug': 'verification-state-separation',
                'case_key': 'case-1',
                'dispatch_id': 'dispatch-1',
                'research_run_id': 'run-1',
                'persona': 'base',
                'artifact_kind': 'research_note',
                'related_entities': [],
                'related_canonical_drivers': [],
                'canonical_driver_suggestions': [],
                'difficulty_class': '',
                'source_of_truth_class': '',
                'status': 'active',
                'occurred_at': '2026-04-16T20:00:00Z',
            }
        ]

        packets = compiler.compile_occurrence_packets(rows, {})
        self.assertEqual(len(packets), 1)
        packet = packets[0]
        self.assertEqual(packet['normalized_family'], 'verification-state-separation')
        self.assertEqual(packet['family_assignment_source'], 'slug_fallback')
        self.assertFalse(packet['routing']['shadow_eligible'])

    def test_build_status_payload_summarizes_top_families(self) -> None:
        packets = [
            {
                'candidate_slug': 'alpha',
                'candidate_label': 'Alpha',
                'normalized_family': 'family_one',
                'family_assignment_source': 'generated_index',
                'packet_key': 'occurrence-packet:alpha',
                'proposal_key': 'driver-mechanism:alpha',
                'packet_hash': 'hash-alpha',
                'source_summary': {'source_occurrence_count': 3, 'distinct_case_count': 2, 'distinct_persona_count': 1},
                'support': {'case_keys': ['case-1', 'case-2'], 'personas': ['base']},
            },
            {
                'candidate_slug': 'beta',
                'candidate_label': 'Beta',
                'normalized_family': 'family_one',
                'family_assignment_source': 'slug_fallback',
                'packet_key': 'occurrence-packet:beta',
                'proposal_key': 'driver-mechanism:beta',
                'packet_hash': 'hash-beta',
                'source_summary': {'source_occurrence_count': 1, 'distinct_case_count': 1, 'distinct_persona_count': 1},
                'support': {'case_keys': ['case-3'], 'personas': ['skeptic']},
            },
            {
                'candidate_slug': 'gamma',
                'candidate_label': 'Gamma',
                'normalized_family': 'family_two',
                'family_assignment_source': 'generated_index',
                'packet_key': 'occurrence-packet:gamma',
                'proposal_key': 'driver-mechanism:gamma',
                'packet_hash': 'hash-gamma',
                'source_summary': {'source_occurrence_count': 2, 'distinct_case_count': 2, 'distinct_persona_count': 2},
                'support': {'case_keys': ['case-4', 'case-5'], 'personas': ['base', 'skeptic']},
            },
        ]

        status = compiler.build_status_payload(
            rows=[{}, {}, {}, {}, {}, {}],
            packets=packets,
            write_outcomes={'packet_json_written': 3},
            index_payload={'source_counts': {'db_occurrence_count': 6, 'markdown_fallback_occurrence_count': 0}, 'summary': {'generated_candidate_count': 3, 'normalized_family_count': 2}},
            warnings=[],
            run_id='occurrence-compiler-test',
        )

        self.assertEqual(status['candidate_count'], 3)
        self.assertEqual(status['family_count'], 2)
        self.assertEqual(status['fallback_family_assignment_count'], 1)
        self.assertEqual(status['top_families'][0]['family_key'], 'family_one')
        self.assertEqual(status['top_families'][0]['source_occurrence_count'], 4)


if __name__ == '__main__':
    unittest.main()
