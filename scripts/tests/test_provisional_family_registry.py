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

registry = importlib.import_module('lib.provisional_family_registry')

POLICY_ROWS = {
    'source_resolution': {'mechanism_family': 'source_resolution', 'enabled': True},
    'workflow_pricing': {'mechanism_family': 'workflow_pricing', 'enabled': True},
    'threshold_touch': {'mechanism_family': 'threshold_touch', 'enabled': True},
    'publication_timing': {'mechanism_family': 'publication_timing', 'enabled': True},
    'unassigned': {'mechanism_family': 'unassigned', 'enabled': False},
}


def make_packet(*, slug: str, label: str, family: str, occurrences: int, cases: list[str], personas: list[str]) -> dict:
    return {
        'packet_key': f'occurrence-packet:{slug}',
        'packet_hash': f'hash-{slug}',
        'candidate_slug': slug,
        'candidate_label': label,
        'normalized_family': family,
        'source_summary': {
            'source_occurrence_count': occurrences,
            'distinct_case_count': len(cases),
            'distinct_persona_count': len(personas),
        },
        'support': {
            'case_keys': cases,
            'personas': personas,
            'related_canonical_drivers': [],
            'canonical_driver_suggestions': [],
        },
    }


class ProvisionalFamilyRegistryTests(unittest.TestCase):
    def test_threshold_candidate_maps_into_threshold_touch_provisional_family(self) -> None:
        packet = make_packet(
            slug='threshold-proximity',
            label='threshold proximity',
            family='resolution-mechanics',
            occurrences=42,
            cases=['case-1', 'case-2'],
            personas=['base', 'skeptic'],
        )
        bridge = registry.bridge_packet_to_provisional_family(packet, loaded_policies=POLICY_ROWS)
        self.assertEqual(bridge['canonical_family'], 'threshold_touch')
        self.assertEqual(bridge['family_key'], 'prov:threshold_touch:resolution-mechanics')
        self.assertEqual(bridge['bridge_status'], 'mapped_provisional')

    def test_publication_family_exact_match_reuses_manual_family_key(self) -> None:
        packet = make_packet(
            slug='macro-event-timing',
            label='macro event timing',
            family='publication-timing',
            occurrences=5,
            cases=['case-1'],
            personas=['base'],
        )
        bridge = registry.bridge_packet_to_provisional_family(packet, loaded_policies=POLICY_ROWS)
        self.assertEqual(bridge['canonical_family'], 'publication_timing')
        self.assertEqual(bridge['family_key'], 'publication_timing')
        self.assertEqual(bridge['family_state'], 'canonical_seed')

    def test_unmatched_candidate_stays_novel_under_unassigned_parent(self) -> None:
        packet = make_packet(
            slug='team-strength-gap',
            label='team strength gap',
            family='team-strength-gap',
            occurrences=7,
            cases=['case-1', 'case-2', 'case-3'],
            personas=['base', 'skeptic'],
        )
        bridge = registry.bridge_packet_to_provisional_family(packet, loaded_policies=POLICY_ROWS)
        self.assertEqual(bridge['canonical_family'], 'unassigned')
        self.assertEqual(bridge['family_key'], 'prov:novel:team-strength-gap')
        self.assertEqual(bridge['lineage_parent_family_key'], 'unassigned')

    def test_build_registry_groups_candidates_by_bridged_family_key(self) -> None:
        packets = [
            make_packet(
                slug='threshold-proximity',
                label='threshold proximity',
                family='resolution-mechanics',
                occurrences=42,
                cases=['case-1', 'case-2'],
                personas=['base', 'skeptic'],
            ),
            make_packet(
                slug='intraday-volatility',
                label='intraday volatility',
                family='resolution-mechanics',
                occurrences=39,
                cases=['case-3', 'case-4'],
                personas=['base', 'skeptic'],
            ),
            make_packet(
                slug='macro-event-timing',
                label='macro event timing',
                family='publication-timing',
                occurrences=5,
                cases=['case-5'],
                personas=['base'],
            ),
            make_packet(
                slug='team-strength-gap',
                label='team strength gap',
                family='team-strength-gap',
                occurrences=7,
                cases=['case-6', 'case-7'],
                personas=['base'],
            ),
        ]
        payload = registry.build_provisional_family_registry(packets, loaded_policies=POLICY_ROWS)
        families = {row['family_key']: row for row in payload['families']}
        self.assertIn('prov:threshold_touch:resolution-mechanics', families)
        self.assertEqual(families['prov:threshold_touch:resolution-mechanics']['candidate_count'], 2)
        self.assertEqual(families['prov:threshold_touch:resolution-mechanics']['source_occurrence_count'], 81)
        self.assertIn('publication_timing', families)
        self.assertIn('prov:novel:team-strength-gap', families)
        canonical_rows = {row['canonical_family']: row for row in payload['canonical_families']}
        self.assertEqual(canonical_rows['threshold_touch']['candidate_count'], 2)
        self.assertEqual(canonical_rows['publication_timing']['family_count'], 1)
        self.assertEqual(payload['family_count'], 3)
        self.assertEqual(payload['member_count'], 4)


if __name__ == '__main__':
    unittest.main()
