from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

TEST_DIR = Path(__file__).resolve().parent
REPO_ROOT = TEST_DIR.parents[1]
RUNTIME_ROOT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime'
RUNTIME_SCRIPTS_DIR = RUNTIME_ROOT / 'scripts'

for candidate in [RUNTIME_ROOT, RUNTIME_SCRIPTS_DIR]:
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


controller = load_module(
    'advance_live_causal_graph_items_for_tests',
    RUNTIME_SCRIPTS_DIR / 'advance_live_causal_graph_items.py',
)


class LiveCausalGraphControllerTests(unittest.TestCase):
    def make_policy(self) -> dict:
        return {
            'enabled': True,
            'max_trial_candidates': 1,
            'max_active_nodes': 1,
            'max_active_edges': 1,
            'min_non_intervention_support_cases_for_trial': 2,
            'min_trial_judged_count_for_promotion': 2,
            'min_trial_helpful_count_for_promotion': 1,
            'min_trial_shrunken_utility_for_promotion': 0.25,
            'max_trial_harmful_rate_for_promotion': 0.34,
            'max_contest_case_count_for_promotion': 1,
            'notes': {},
        }

    def make_entry(self, *, entity_type: str, key: str, stage: str, family: str = 'publication_timing', decay: float = 0.0, superseded_by_key: str = '') -> dict:
        if entity_type == 'node':
            record = {
                'node_key': key,
                'status': 'draft' if stage == 'draft' else ('active' if stage in {'trial', 'active'} else stage),
                'lifecycle_stage': stage,
                'mechanism_family': family,
                'decay_score': decay,
                'promotion_score': 0.0,
                'superseded_by_key': superseded_by_key,
                'path': f'qualitative-db/60-causal-map/nodes/{key}.md',
            }
        else:
            record = {
                'edge_key': key,
                'status': 'draft' if stage == 'draft' else ('active' if stage in {'trial', 'active'} else stage),
                'lifecycle_stage': stage,
                'mechanism_family': family,
                'decay_score': decay,
                'promotion_score': 0.0,
                'superseded_by_key': superseded_by_key,
                'path': f'qualitative-db/60-causal-map/edges/{key}.md',
            }
        return {
            'entity_type': entity_type,
            'note_path': Path('/tmp') / f'{key}.md',
            'record': record,
        }

    def test_qualifies_for_trial_with_support_and_weight(self) -> None:
        entry = self.make_entry(entity_type='node', key='publication-window-timing', stage='draft')
        blockers = controller.qualifies_for_trial(
            entry,
            {
                'supporting_case_count': 2,
                'matched_case_count': 2,
                'contested_case_count': 0,
                'learned_weight': 0.18,
                'shrunken_uplift': 0.0,
            },
            self.make_policy(),
            {'open_violation_count': 0, 'has_high_severity': False},
        )
        self.assertEqual(blockers, [])

    def test_qualifies_for_active_with_trial_utility_and_helpful_cases(self) -> None:
        entry = self.make_entry(entity_type='node', key='publication-window-timing', stage='trial')
        blockers = controller.qualifies_for_active(
            entry,
            {
                'exposure_count': 2,
                'supporting_case_count': 2,
                'contested_case_count': 0,
                'shrunken_uplift': 0.31,
                'stats_metadata': {'helpful_case_count': 1, 'harmful_case_count': 0},
            },
            self.make_policy(),
            {'open_violation_count': 0, 'has_high_severity': False},
        )
        self.assertEqual(blockers, [])

    def test_forced_transition_holds_active_item_with_health_violation(self) -> None:
        entry = self.make_entry(entity_type='edge', key='publication-window-timing__increases__reporting-state-uncertainty', stage='active')
        forced = controller.forced_transition(
            entry,
            {'exposure_count': 1, 'learned_weight': 0.12},
            {'open_violation_count': 1, 'has_high_severity': True},
        )
        self.assertEqual(forced, ('hold', 'open_health_violations'))

    def test_forced_transition_retires_superseded_item(self) -> None:
        entry = self.make_entry(
            entity_type='node',
            key='publication-window-timing',
            stage='hold',
            superseded_by_key='new-publication-window-timing',
        )
        forced = controller.forced_transition(
            entry,
            {'exposure_count': 0, 'learned_weight': 0.0},
            {'open_violation_count': 0, 'has_high_severity': False},
        )
        self.assertEqual(forced, ('retired', 'superseded_by:new-publication-window-timing'))

    def test_hold_item_can_reenter_trial_when_reactivation_enabled(self) -> None:
        entry = self.make_entry(entity_type='node', key='publication-window-timing', stage='hold')
        entry['record']['decay_score'] = 0.2
        policy = self.make_policy()
        policy['notes'] = {'reactivation': {'enabled': True, 'min_support_cases': 2, 'max_decay_score': 0.9}}
        blockers = controller.qualifies_for_trial(
            entry,
            {
                'supporting_case_count': 2,
                'matched_case_count': 2,
                'contested_case_count': 0,
                'learned_weight': 0.15,
                'shrunken_uplift': 0.0,
            },
            policy,
            {'open_violation_count': 0, 'has_high_severity': False},
        )
        self.assertEqual(blockers, [])

    def test_family_quarantine_blocks_trial_advancement(self) -> None:
        entry = self.make_entry(entity_type='node', key='publication-window-timing', stage='draft')
        policy = self.make_policy()
        policy['notes'] = {'quarantined': True}
        blockers = controller.qualifies_for_trial(
            entry,
            {
                'supporting_case_count': 2,
                'matched_case_count': 2,
                'contested_case_count': 0,
                'learned_weight': 0.18,
                'shrunken_uplift': 0.0,
            },
            policy,
            {'open_violation_count': 0, 'has_high_severity': False},
        )
        self.assertIn('family_quarantined', blockers)

    def test_select_ranked_promotions_respects_family_slots(self) -> None:
        policy = self.make_policy()
        family_state = {'publication_timing': {'trial_total': 0, 'active_nodes': 0, 'active_edges': 0}}
        candidate_a = {
            'entry': self.make_entry(entity_type='node', key='a', stage='draft'),
            'score': 0.8,
        }
        candidate_b = {
            'entry': self.make_entry(entity_type='node', key='b', stage='draft'),
            'score': 0.3,
        }
        selected, blocked = controller.select_ranked_promotions(
            [candidate_a, candidate_b],
            target_stage='trial',
            family_state=family_state,
            policies={'publication_timing': policy, 'unassigned': policy},
        )
        self.assertEqual([controller.entity_key(row['entry']) for row in selected], ['a'])
        self.assertEqual(blocked[0]['reason'], 'family_trial_slots_exhausted')


if __name__ == '__main__':
    unittest.main()
