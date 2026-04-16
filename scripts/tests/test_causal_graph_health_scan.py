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


health_scan = load_module(
    'scan_causal_graph_health_for_tests',
    RUNTIME_SCRIPTS_DIR / 'scan_causal_graph_health.py',
)


class CausalGraphHealthScanTests(unittest.TestCase):
    def make_node_entry(
        self,
        *,
        key: str,
        stage: str,
        status: str | None = None,
        family: str = 'publication_timing',
        source_kind: str = 'seed',
        decay: float = 0.0,
        last_seen_at: str = '',
        last_matched_at: str = '',
        last_injected_at: str = '',
        last_helpful_at: str = '',
    ) -> dict:
        return {
            'entity_type': 'node',
            'note_path': Path('/tmp') / f'{key}.md',
            'record': {
                'node_key': key,
                'status': status or ('draft' if stage == 'draft' else ('active' if stage in {'trial', 'active'} else stage)),
                'lifecycle_stage': stage,
                'mechanism_family': family,
                'source_kind': source_kind,
                'decay_score': decay,
                'path': f'qualitative-db/60-causal-map/nodes/{key}.md',
                'sidecar_path': f'qualitative-db/60-causal-map/nodes/{key}.json',
                'last_seen_at': last_seen_at,
                'last_matched_at': last_matched_at,
                'last_injected_at': last_injected_at,
                'last_helpful_at': last_helpful_at,
            },
        }

    def make_edge_entry(
        self,
        *,
        key: str,
        stage: str,
        status: str | None = None,
        family: str = 'publication_timing',
        source_kind: str = 'seed',
        confidence_mode: str = 'reviewed',
        source_node_key: str = 'source-node',
        target_node_key: str = 'target-node',
        evidence_paths: list[str] | None = None,
        evidence_rows: list[dict] | None = None,
        decay: float = 0.0,
    ) -> dict:
        return {
            'entity_type': 'edge',
            'note_path': Path('/tmp') / f'{key}.md',
            'record': {
                'edge_key': key,
                'status': status or ('draft' if stage == 'draft' else ('active' if stage in {'trial', 'active'} else stage)),
                'lifecycle_stage': stage,
                'mechanism_family': family,
                'source_kind': source_kind,
                'confidence_mode': confidence_mode,
                'source_node_key': source_node_key,
                'target_node_key': target_node_key,
                'evidence_paths': evidence_paths or [],
                'evidence_rows': evidence_rows or [],
                'decay_score': decay,
                'path': f'qualitative-db/60-causal-map/edges/{key}.md',
                'sidecar_path': f'qualitative-db/60-causal-map/edges/{key}.json',
                'last_seen_at': '',
                'last_matched_at': '',
                'last_injected_at': '',
                'last_helpful_at': '',
            },
        }

    def test_detect_structural_missing_edge_endpoint(self) -> None:
        edge = self.make_edge_entry(
            key='publication-window-timing__increases__reporting-state-uncertainty',
            stage='active',
            source_node_key='publication-window-timing',
            target_node_key='reporting-state-uncertainty',
        )
        violations = health_scan.detect_structural_violations([edge])
        self.assertEqual(violations[0]['violation_kind'], 'structural_missing_edge_endpoint')
        self.assertEqual(violations[0]['severity'], 'high')

    def test_detect_evidence_reviewed_live_edge_without_support(self) -> None:
        edge = self.make_edge_entry(
            key='publication-window-timing__increases__reporting-state-uncertainty',
            stage='active',
            confidence_mode='reviewed',
            evidence_paths=[],
            evidence_rows=[],
        )
        violations = health_scan.detect_evidence_violations(
            [edge],
            {},
            {'publication-window-timing__increases__reporting-state-uncertainty': {'supporting_case_count': 0}},
        )
        self.assertEqual(violations[0]['violation_kind'], 'evidence_reviewed_live_edge_without_support')
        self.assertEqual(violations[0]['severity'], 'high')

    def test_detect_utility_live_stage_conflicts_with_stats(self) -> None:
        node = self.make_node_entry(key='verification-caution', stage='active')
        violations = health_scan.detect_utility_violations(
            [node],
            {
                'verification-caution': {
                    'status': 'hold',
                    'status_reason': 'negative_or_contested_weight',
                    'learned_weight': -0.04,
                    'supporting_case_count': 1,
                    'contested_case_count': 1,
                    'exposure_count': 0,
                }
            },
            {},
        )
        self.assertEqual(violations[0]['violation_kind'], 'utility_live_stage_conflicts_with_stats')
        self.assertEqual(violations[0]['severity'], 'high')

    def test_detect_freshness_promoted_live_item_stale(self) -> None:
        node = self.make_node_entry(
            key='experimental-publication-window-timing',
            stage='trial',
            source_kind='promoted_candidate',
            decay=0.95,
        )
        violations = health_scan.detect_freshness_violations(
            [node],
            {'experimental-publication-window-timing': {'supporting_case_count': 0, 'exposure_count': 0}},
            {},
            stale_activity_days=45.0,
            live_decay_threshold=0.9,
            hold_decay_threshold=0.95,
        )
        self.assertEqual(violations[0]['violation_kind'], 'freshness_promoted_live_item_stale')
        self.assertEqual(violations[0]['severity'], 'medium')


if __name__ == '__main__':
    unittest.main()
