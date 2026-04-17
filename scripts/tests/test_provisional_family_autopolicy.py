from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

TEST_DIR = Path(__file__).resolve().parent
REPO_ROOT = TEST_DIR.parents[1]
RUNTIME_ROOT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime'

if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))

autopolicy = importlib.import_module('lib.provisional_family_autopolicy')

BASE_POLICIES = {
    'source_resolution': {
        'mechanism_family': 'source_resolution',
        'enabled': True,
        'max_shadow_candidates': 6,
        'max_trial_candidates': 2,
        'max_active_nodes': 6,
        'max_active_edges': 4,
        'notes': {},
    },
    'workflow_pricing': {
        'mechanism_family': 'workflow_pricing',
        'enabled': True,
        'max_shadow_candidates': 4,
        'max_trial_candidates': 2,
        'max_active_nodes': 4,
        'max_active_edges': 2,
        'notes': {},
    },
    'threshold_touch': {
        'mechanism_family': 'threshold_touch',
        'enabled': True,
        'max_shadow_candidates': 6,
        'max_trial_candidates': 2,
        'max_active_nodes': 6,
        'max_active_edges': 4,
        'notes': {'exploratory_trial': {'enabled': True, 'max_candidates': 1}},
    },
    'publication_timing': {
        'mechanism_family': 'publication_timing',
        'enabled': True,
        'max_shadow_candidates': 3,
        'max_trial_candidates': 1,
        'max_active_nodes': 3,
        'max_active_edges': 2,
        'notes': {},
    },
    'unassigned': {
        'mechanism_family': 'unassigned',
        'enabled': False,
        'max_shadow_candidates': 1,
        'max_trial_candidates': 0,
        'max_active_nodes': 0,
        'max_active_edges': 0,
        'notes': {},
    },
}


def make_family_row(**overrides: object) -> dict[str, object]:
    row = {
        'family_key': 'prov:threshold_touch:resolution-mechanics',
        'family_label': 'Threshold Touch / Resolution Mechanics',
        'family_state': 'provisional',
        'canonical_family': 'threshold_touch',
        'lineage_parent_family_key': 'threshold_touch',
        'source_family_slug': 'resolution-mechanics',
        'bridge_status': 'mapped_provisional',
        'bridge_confidence_max': 0.9,
        'bridge_reasons': ['threshold', 'touch'],
        'manual_policy_family': 'threshold_touch',
        'manual_policy_enabled': True,
        'candidate_count': 12,
        'source_occurrence_count': 40,
        'distinct_case_count': 8,
        'distinct_persona_count': 3,
    }
    row.update(overrides)
    return row


class ProvisionalFamilyAutopolicyTests(unittest.TestCase):
    def test_mapped_provisional_family_gets_enabled_shadow_only_policy(self) -> None:
        policy = autopolicy.build_generated_policy_row(make_family_row(), base_policies=BASE_POLICIES, generated_at='2026-04-16T23:59:00Z')
        self.assertEqual(policy['mechanism_family'], 'prov:threshold_touch:resolution-mechanics')
        self.assertTrue(policy['enabled'])
        self.assertGreater(policy['max_shadow_candidates'], 0)
        self.assertEqual(policy['max_trial_candidates'], 0)
        self.assertEqual(policy['max_promotion_ready_candidates'], 0)
        self.assertEqual(policy['policy_source'], 'generated_provisional_shadow')
        self.assertEqual(policy['family_state'], 'provisional')
        self.assertFalse(policy['notes']['exploratory_trial']['enabled'])

    def test_novel_low_support_family_stays_disabled(self) -> None:
        policy = autopolicy.build_generated_policy_row(
            make_family_row(
                family_key='prov:novel:alliance-cohesion',
                family_label='Novel provisional / Alliance Cohesion',
                canonical_family='unassigned',
                lineage_parent_family_key='unassigned',
                source_family_slug='alliance-cohesion',
                bridge_status='novel_provisional',
                manual_policy_family='unassigned',
                manual_policy_enabled=False,
                candidate_count=1,
                source_occurrence_count=3,
                distinct_case_count=1,
                distinct_persona_count=1,
            ),
            base_policies=BASE_POLICIES,
            generated_at='2026-04-16T23:59:00Z',
        )
        self.assertFalse(policy['enabled'])
        self.assertEqual(policy['max_shadow_candidates'], 0)
        self.assertIn('novel_occurrence_mass_below_minimum', policy['policy_notes']['disabled_reasons'])

    def test_strong_novel_family_can_earn_bounded_shadow_budget(self) -> None:
        policy = autopolicy.build_generated_policy_row(
            make_family_row(
                family_key='prov:novel:resolution-mechanics',
                family_label='Novel provisional / Resolution Mechanics',
                canonical_family='unassigned',
                lineage_parent_family_key='unassigned',
                source_family_slug='resolution-mechanics',
                bridge_status='novel_provisional',
                manual_policy_family='unassigned',
                manual_policy_enabled=False,
                candidate_count=20,
                source_occurrence_count=40,
                distinct_case_count=12,
                distinct_persona_count=4,
            ),
            base_policies=BASE_POLICIES,
            generated_at='2026-04-16T23:59:00Z',
        )
        self.assertTrue(policy['enabled'])
        self.assertEqual(policy['max_shadow_candidates'], 1)

    def test_payload_skips_canonical_seed_families(self) -> None:
        payload = autopolicy.build_generated_provisional_family_policies(
            {
                'generated_at': '2026-04-16T23:59:00Z',
                'families': [
                    make_family_row(),
                    {
                        'family_key': 'publication_timing',
                        'family_label': 'Publication Timing',
                        'family_state': 'canonical_seed',
                        'canonical_family': 'publication_timing',
                        'lineage_parent_family_key': None,
                        'source_family_slug': 'publication-timing',
                        'bridge_status': 'canonical_seed',
                        'bridge_confidence_max': 1.0,
                        'bridge_reasons': ['exact_policy_family_match'],
                        'manual_policy_family': 'publication_timing',
                        'manual_policy_enabled': True,
                        'candidate_count': 19,
                        'source_occurrence_count': 67,
                        'distinct_case_count': 23,
                        'distinct_persona_count': 4,
                    },
                ],
            },
            base_policies=BASE_POLICIES,
        )
        self.assertEqual(payload['policy_count'], 1)
        self.assertEqual(payload['skipped_canonical_seed_count'], 1)
        self.assertEqual(payload['policies'][0]['mechanism_family'], 'prov:threshold_touch:resolution-mechanics')


if __name__ == '__main__':
    unittest.main()
