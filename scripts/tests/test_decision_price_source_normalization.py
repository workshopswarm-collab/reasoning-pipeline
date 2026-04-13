from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

RUNTIME_SCRIPTS_DIR = Path(__file__).resolve().parents[2] / 'roles' / 'decision-maker' / 'runtime' / 'scripts'
MODULE_PATH = RUNTIME_SCRIPTS_DIR / 'run_decision_maker.py'
if str(RUNTIME_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(RUNTIME_SCRIPTS_DIR))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


runtime = load_module('run_decision_maker_for_tests', MODULE_PATH)


class DecisionPriceSourceNormalizationTests(unittest.TestCase):
    def test_load_repo_env_smoke(self) -> None:
        env = runtime.load_repo_env()
        self.assertIsInstance(env, dict)
        self.assertIn('PATH', env)

    def test_canonicalize_known_alias(self) -> None:
        value, note = runtime.canonicalize_price_source('runtime_market_snapshot')
        self.assertEqual(value, 'market_snapshot_quote')
        self.assertIn('normalized price_source', note or '')

    def test_canonicalize_annotated_market_snapshot_quote(self) -> None:
        value, note = runtime.canonicalize_price_source(
            'market_snapshot_quote_last_observed; live probe indicates acceptingOrders=false'
        )
        self.assertEqual(value, 'market_snapshot_quote')
        self.assertIn('normalized price_source', note or '')

    def test_hydrate_packet_replaces_invalid_price_source_with_canonical_enum(self) -> None:
        packet = {
            'decision': {
                'side': 'no',
                'trade_authorization': 'forbidden',
                'position_policy': 'flat',
                'decision_readiness': 'needs_more_research',
                'primary_crux': 'Need more research.',
                'secondary_cruxes': ['Missing direct verification.'],
                'thesis_class': 'not_decision_ready',
            },
            'valuation': {
                'fair_value_low': 0.1,
                'fair_value_high': 0.3,
                'fair_value_mid': 0.2,
                'market_reference_price': 0.96,
                'independent_verification_quality': 'medium',
                'compressed_toward_market_applied': True,
                'compression_reason': 'Missing direct verification.',
            },
            'execution_semantics': {
                'price_source': 'runtime_market_snapshot',
                'time_horizon': 'Election day through official seat ranking',
            },
            'risk_controls': {
                'confidence_level': 'low',
                'portfolio_constraints': [],
                'liquidity_caution': 'high',
            },
            'bands': runtime.default_band_shape('no'),
            'invalidation': {
                'thesis_breakers': ['x'],
                'market_structure_breakers': ['y'],
                'time_breakers': ['z'],
                'reversal_conditions': ['r'],
            },
            'epistemic_status': {
                'key_uncertainties': ['u'],
                'reasons_to_pass': ['p'],
                'what_would_change_my_mind': ['c'],
                'decision_quality': 'not_ready',
            },
            'audit': {
                'market_baseline_respected': True,
                'action_bias_check_passed': True,
                'self_preservation_bias_check_passed': True,
                'one_sentence_rationale': 'Need more research.',
                'notes': 'test',
            },
        }
        context = {
            'case_key': 'case-test',
            'dispatch_id': 'dispatch-test',
            'question': 'Test question?',
            'market': {
                'market_id': 'market-test',
                'market_title': 'Test question?',
                'market_reference_price': 0.96,
                'platform': 'polymarket',
                'primary_market_url': 'https://example.com/market',
            },
            'upstream': {
                'decision_handoff_path': 'handoff.md',
                'syndicated_finding_path': 'finding.md',
                'edge_independent_verification_quality': 'medium',
            },
            'recommended_runtime_defaults': {
                'price_source': 'market_snapshot_quote',
                'rebalance_threshold_fraction': 0.1,
                'allow_auto_reversal': False,
                'quote_staleness_seconds': 300,
            },
        }
        selected_bundle = {
            'structured_handoff_policy': {
                'structured_handoff_is_primary_starting_point': True,
            },
            'verification_enforcement': {
                'agent_tool_use_allowed': False,
            },
            'verification_budget': {},
            'verification_mode': 'not_ready_reopen_recommended',
        }

        hydrated = runtime.hydrate_packet_from_context(packet, context, selected_bundle, valid_hours=24)
        self.assertEqual(hydrated['execution_semantics']['price_source'], 'market_snapshot_quote')
        self.assertIn('normalized price_source', hydrated['audit']['additional_verification_notes'])
        self.assertTrue(runtime.validate_decision_packet_payload(hydrated)['ok'])


if __name__ == '__main__':
    unittest.main()
