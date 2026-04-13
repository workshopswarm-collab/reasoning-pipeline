from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

TEST_DIR = Path(__file__).resolve().parent
PLANNER_DIR = TEST_DIR.parent
SCRIPT_PATH = PLANNER_DIR / 'scripts' / 'classify_research_difficulty.py'
if str(SCRIPT_PATH.parent) not in sys.path:
    sys.path.insert(0, str(SCRIPT_PATH.parent))

spec = importlib.util.spec_from_file_location('classify_research_difficulty', SCRIPT_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

FIXTURES = TEST_DIR / 'fixtures'


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text())


class ResearchDifficultyClassifierTests(unittest.TestCase):
    def test_heuristic_snapshot_authoritative_direct(self) -> None:
        payload = load_fixture('official_youtube_release_low.json')
        result = module.classify(payload, mode='heuristic', endpoint='http://127.0.0.1:11434', model='ignored', timeout_seconds=1.0)
        profile = result['difficulty_profile']
        self.assertEqual(profile['difficulty_class'], 'low')
        self.assertEqual(profile['resolution_risk'], 'low')
        self.assertEqual(profile['evidence_floor'], '1_authoritative')
        self.assertFalse(profile['extra_verification_required'])
        self.assertEqual(profile['source_of_truth_class'], 'authoritative_direct')
        self.assertEqual(profile['focus_hints'], [
            'official_source_verification',
            'authoritative_source_first',
            'date_timing_check',
        ])
        self.assertEqual(profile['difficulty_rationale'], [
            'authoritative_source_available',
            'date_sensitive_resolution',
        ])
        self.assertEqual(result['heuristic_summary']['heuristic_confidence'], 'high')
        self.assertFalse(result['heuristic_summary']['needs_model_review'])

    def test_merge_profiles_preserves_high_confidence_heuristic_details(self) -> None:
        heuristic_profile = {
            'difficulty_class': 'low',
            'resolution_risk': 'low',
            'evidence_floor': '1_authoritative',
            'extra_verification_required': False,
            'focus_hints': ['official_source_verification', 'authoritative_source_first'],
            'difficulty_rationale': ['authoritative_source_available'],
            'source_of_truth_class': 'authoritative_direct',
            'classifier_source': 'heuristic',
            'classifier_model': None,
            'classifier_version': 'v3-hybrid-ready',
        }
        model_profile = {
            'difficulty_class': 'medium',
            'resolution_risk': 'medium',
            'evidence_floor': '2_meaningful',
            'extra_verification_required': True,
            'focus_hints': ['independent_confirmation', 'source_of_truth_check'],
            'difficulty_rationale': ['consensus_reporting_dependency', 'ambiguous_source_of_truth'],
            'source_of_truth_class': 'multi_source_ambiguous',
            'classifier_source': 'hybrid',
            'classifier_model': 'qwen3.5:9b',
            'classifier_version': 'v3-hybrid',
        }
        merged = module.merge_profiles(
            heuristic_profile,
            model_profile,
            heuristic_confidence='high',
            model_confidence='high',
        )
        self.assertEqual(merged['source_of_truth_class'], 'authoritative_direct')
        self.assertEqual(merged['focus_hints'], ['official_source_verification', 'authoritative_source_first'])
        self.assertEqual(merged['difficulty_rationale'], ['authoritative_source_available'])
        self.assertEqual(merged['difficulty_class'], 'medium')
        self.assertEqual(merged['resolution_risk'], 'medium')
        self.assertEqual(merged['evidence_floor'], '2_meaningful')
        self.assertTrue(merged['extra_verification_required'])

    def test_low_confidence_ambiguous_source_can_refine_from_model(self) -> None:
        heuristic_profile = {
            'difficulty_class': 'low',
            'resolution_risk': 'low',
            'evidence_floor': '2_meaningful',
            'extra_verification_required': False,
            'focus_hints': ['source_of_truth_check'],
            'difficulty_rationale': ['ambiguous_source_of_truth'],
            'source_of_truth_class': 'multi_source_ambiguous',
            'classifier_source': 'heuristic',
            'classifier_model': None,
            'classifier_version': 'v3-hybrid-ready',
        }
        model_profile = {
            'difficulty_class': 'low',
            'resolution_risk': 'low',
            'evidence_floor': '1_authoritative',
            'extra_verification_required': False,
            'focus_hints': ['authoritative_direct'],
            'difficulty_rationale': ['single authoritative source resolves cleanly'],
            'source_of_truth_class': 'authoritative_direct',
            'classifier_source': 'hybrid',
            'classifier_model': 'qwen3.5:9b',
            'classifier_version': 'v3-hybrid',
        }
        merged = module.merge_profiles(
            heuristic_profile,
            model_profile,
            heuristic_confidence='low',
            model_confidence='high',
        )
        self.assertEqual(merged['source_of_truth_class'], 'authoritative_direct')
        self.assertEqual(merged['focus_hints'], [
            'official_source_verification',
            'authoritative_source_first',
            'source_of_truth_check',
        ])
        self.assertEqual(merged['difficulty_rationale'], [
            'authoritative_source_available',
            'ambiguous_source_of_truth',
        ])
        self.assertEqual(merged['evidence_floor'], '1_authoritative')

    def test_hybrid_replay_normalizes_variant_model_outputs(self) -> None:
        payload = load_fixture('btc_threshold_settlement_medium.json')
        first_model = {
            'difficulty_class': 'medium',
            'resolution_risk': 'medium',
            'evidence_floor': '2_meaningful',
            'extra_verification_required': True,
            'focus_hints': ['verify_utc_conversion', 'check_binance_candle_close', 'exclude_other_exchanges'],
            'difficulty_rationale': ['single authoritative exchange price with settlement-time verification'],
            'source_of_truth_class': 'authoritative_direct',
            'model_confidence': 'high',
        }
        second_model = {
            'difficulty_class': 'medium',
            'resolution_risk': 'medium',
            'evidence_floor': '2_meaningful',
            'extra_verification_required': True,
            'focus_hints': ['check_et_1200_utc_alignment', 'confirm_close_price_logic', 'verify_exact_btc/usdt_pair'],
            'difficulty_rationale': ['resolution depends on structured settlement mechanics rather than a simple point-in-time reading'],
            'source_of_truth_class': 'authoritative_direct',
            'model_confidence': 'high',
        }
        with patch.object(module, 'model_available', return_value=(True, None)):
            with patch.object(module, 'ollama_generate', return_value=first_model):
                first = module.classify(payload, mode='hybrid', endpoint='http://127.0.0.1:11434', model='qwen3.5:9b', timeout_seconds=1.0)
            with patch.object(module, 'ollama_generate', return_value=second_model):
                second = module.classify(payload, mode='hybrid', endpoint='http://127.0.0.1:11434', model='qwen3.5:9b', timeout_seconds=1.0)
        self.assertEqual(first['difficulty_profile'], second['difficulty_profile'])
        self.assertEqual(first['difficulty_profile']['difficulty_class'], 'high')
        self.assertEqual(first['difficulty_profile']['resolution_risk'], 'high')
        self.assertEqual(first['difficulty_profile']['focus_hints'], [
            'date_timing_check',
            'resolution_audit',
            'multi_condition_check',
            'independent_confirmation',
            'disconfirming_source_required',
        ])
        self.assertEqual(first['difficulty_profile']['difficulty_rationale'], [
            'date_sensitive_resolution',
            'explicit_exclusion_rules',
            'multi_condition_contract',
        ])


if __name__ == '__main__':
    unittest.main()
