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


repair = load_module(
    'repair_causal_graph_for_tests',
    RUNTIME_SCRIPTS_DIR / 'repair_causal_graph.py',
)


class RepairCausalGraphTests(unittest.TestCase):
    def make_entry(self, *, entity_type: str, key: str, stage: str, status: str | None = None, sidecar_path: str = 'present.json') -> dict:
        if entity_type == 'node':
            record = {
                'node_key': key,
                'status': status or ('draft' if stage == 'draft' else ('active' if stage in {'trial', 'active'} else stage)),
                'lifecycle_stage': stage,
                'mechanism_family': 'publication_timing',
                'path': f'qualitative-db/60-causal-map/nodes/{key}.md',
                'sidecar_path': sidecar_path,
            }
        else:
            record = {
                'edge_key': key,
                'status': status or ('draft' if stage == 'draft' else ('active' if stage in {'trial', 'active'} else stage)),
                'lifecycle_stage': stage,
                'mechanism_family': 'publication_timing',
                'path': f'qualitative-db/60-causal-map/edges/{key}.md',
                'sidecar_path': sidecar_path,
            }
        return {
            'entity_type': entity_type,
            'note_path': Path('/tmp') / f'{key}.md',
            'record': record,
        }

    def make_violation(self, *, entity_type: str, key: str, kind: str, severity: str = 'medium') -> dict:
        return {
            'entity_type': entity_type,
            'entity_key': key,
            'violation_kind': kind,
            'severity': severity,
            'status': 'open',
            'details': {},
        }

    def test_build_repair_plan_marks_live_item_hold(self) -> None:
        entry = self.make_entry(entity_type='edge', key='publication-window-timing__increases__reporting-state-uncertainty', stage='active')
        repairs, deferred = repair.build_repair_plan(
            [entry],
            [
                self.make_violation(
                    entity_type='causal_edge',
                    key='publication-window-timing__increases__reporting-state-uncertainty',
                    kind='utility_negative_live_item',
                    severity='medium',
                )
            ],
        )
        self.assertEqual(len(repairs), 1)
        self.assertEqual(repairs[0]['repair_kind'], 'mark_hold')
        self.assertEqual(repairs[0]['target_stage'], 'hold')
        self.assertEqual(deferred, [])

    def test_build_repair_plan_holds_live_edge_with_missing_review_paths(self) -> None:
        entry = self.make_entry(entity_type='edge', key='publication-window-timing__increases__reporting-state-uncertainty', stage='trial')
        repairs, _ = repair.build_repair_plan(
            [entry],
            [
                self.make_violation(
                    entity_type='causal_edge',
                    key='publication-window-timing__increases__reporting-state-uncertainty',
                    kind='evidence_missing_review_paths',
                    severity='medium',
                )
            ],
        )
        self.assertEqual(repairs[0]['repair_kind'], 'mark_hold')
        self.assertEqual(repairs[0]['target_stage'], 'hold')

    def test_build_repair_plan_retires_stale_hold_item(self) -> None:
        entry = self.make_entry(entity_type='node', key='publication-window-timing', stage='hold')
        repairs, _ = repair.build_repair_plan(
            [entry],
            [
                self.make_violation(
                    entity_type='causal_node',
                    key='publication-window-timing',
                    kind='freshness_stale_hold_candidate',
                    severity='low',
                )
            ],
        )
        self.assertEqual(len(repairs), 1)
        self.assertEqual(repairs[0]['repair_kind'], 'retire_stale_item')
        self.assertEqual(repairs[0]['target_stage'], 'retired')

    def test_build_repair_plan_aligns_status_mismatch(self) -> None:
        entry = self.make_entry(entity_type='node', key='verification-caution', stage='active', status='draft')
        repairs, deferred = repair.build_repair_plan(
            [entry],
            [
                self.make_violation(
                    entity_type='causal_node',
                    key='verification-caution',
                    kind='structural_status_stage_mismatch',
                    severity='low',
                )
            ],
        )
        self.assertEqual(len(repairs), 1)
        self.assertEqual(repairs[0]['repair_kind'], 'align_status_to_stage')
        self.assertEqual(deferred, [])

    def test_build_repair_plan_regenerates_missing_sidecar(self) -> None:
        entry = self.make_entry(entity_type='node', key='verification-caution', stage='active', sidecar_path='')
        repairs, deferred = repair.build_repair_plan(
            [entry],
            [
                self.make_violation(
                    entity_type='causal_node',
                    key='verification-caution',
                    kind='structural_missing_sidecar',
                    severity='low',
                )
            ],
        )
        self.assertEqual(len(repairs), 1)
        self.assertEqual(repairs[0]['repair_kind'], 'regenerate_sidecar')
        self.assertEqual(deferred, [])

    def test_build_repair_plan_cascades_edge_hold_when_endpoint_nodes_are_demoted(self) -> None:
        source = self.make_entry(entity_type='node', key='verification-caution', stage='active')
        target = self.make_entry(entity_type='node', key='fair-value-discounting-pressure', stage='active')
        edge = self.make_entry(
            entity_type='edge',
            key='verification-caution__increases__fair-value-discounting-pressure',
            stage='active',
        )
        edge['record']['source_node_key'] = 'verification-caution'
        edge['record']['target_node_key'] = 'fair-value-discounting-pressure'
        repairs, deferred = repair.build_repair_plan(
            [source, target, edge],
            [
                self.make_violation(
                    entity_type='causal_node',
                    key='verification-caution',
                    kind='utility_live_stage_conflicts_with_stats',
                    severity='high',
                ),
                self.make_violation(
                    entity_type='causal_node',
                    key='fair-value-discounting-pressure',
                    kind='utility_live_stage_conflicts_with_stats',
                    severity='high',
                ),
            ],
        )
        repair_map = {repair['entry']['record'].get('node_key') or repair['entry']['record'].get('edge_key'): repair for repair in repairs}
        self.assertEqual(repair_map['verification-caution']['repair_kind'], 'mark_hold')
        self.assertEqual(repair_map['fair-value-discounting-pressure']['repair_kind'], 'mark_hold')
        self.assertEqual(repair_map['verification-caution__increases__fair-value-discounting-pressure']['repair_kind'], 'mark_hold')
        self.assertEqual(repair_map['verification-caution__increases__fair-value-discounting-pressure']['target_stage'], 'hold')
        self.assertEqual(deferred, [])

    def test_simulate_repairs_updates_stage_and_status(self) -> None:
        entry = self.make_entry(entity_type='node', key='publication-window-timing', stage='trial')
        simulated = repair.simulate_repairs(
            [entry],
            [
                {
                    'entry': entry,
                    'repair_kind': 'mark_hold',
                    'target_stage': 'hold',
                    'reason': 'test-reason',
                    'severity': 'medium',
                    'triggering_violations': [],
                }
            ],
        )
        record = simulated[0]['record']
        self.assertEqual(record['lifecycle_stage'], 'hold')
        self.assertEqual(record['status'], 'hold')
        self.assertEqual(record['repair_reason'], 'test-reason')

    def test_simulate_align_status_and_regenerate_sidecar(self) -> None:
        entry = self.make_entry(entity_type='node', key='verification-caution', stage='active', status='draft', sidecar_path='')
        simulated = repair.simulate_repairs(
            [entry],
            [
                {
                    'entry': entry,
                    'repair_kind': 'align_status_to_stage',
                    'target_stage': 'active',
                    'reason': 'align',
                    'severity': 'low',
                    'triggering_violations': [],
                }
            ],
        )
        record = simulated[0]['record']
        self.assertEqual(record['status'], 'active')
        self.assertTrue(record['sidecar_path'])


if __name__ == '__main__':
    unittest.main()
