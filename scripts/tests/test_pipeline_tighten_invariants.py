from __future__ import annotations

import importlib.util
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

TEST_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = TEST_DIR.parent
RUNTIME_SCRIPTS_DIR = SCRIPTS_DIR.parent / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / 'scripts'
PLANNER_SCRIPTS_DIR = SCRIPTS_DIR.parent / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'planner' / 'scripts'


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


prepare_and_launch = load_module(
    'prepare_and_launch_headless_telegram_dispatch',
    RUNTIME_SCRIPTS_DIR / 'prepare_and_launch_headless_telegram_dispatch.py',
)
pipeline_sequencer_candidates = load_module(
    'pipeline_sequencer_candidates',
    SCRIPTS_DIR / 'pipeline_sequencer_candidates.py',
)
pipeline_sequencer_runner = load_module(
    'pipeline_sequencer_runner',
    SCRIPTS_DIR / 'pipeline_sequencer_runner.py',
)
select_refresh_case_module = load_module(
    'select_refresh_case',
    PLANNER_SCRIPTS_DIR / 'select_refresh_case.py',
)
case_artifact_contract_audit = load_module(
    'case_artifact_contract_audit',
    SCRIPTS_DIR / 'case_artifact_contract_audit.py',
)
check_pipeline_health = load_module(
    'check_pipeline_health',
    SCRIPTS_DIR / 'check_pipeline_health.py',
)


class PipelineTightenInvariantTests(unittest.TestCase):
    def make_args(self) -> types.SimpleNamespace:
        return types.SimpleNamespace(
            pretty=False,
            resume_existing=True,
            control_managed=False,
            control_file='scripts/.runtime-state/pipeline-automation-control.json',
            poll_seconds=15.0,
            idle_seconds=60.0,
            max_case_seconds=7200.0,
            loop=False,
            max_cases=0,
            quarantine_file='scripts/.runtime-state/pipeline-quarantine.json',
            heartbeat_file='scripts/.runtime-state/pipeline-heartbeat.json',
            lock_file='scripts/.runtime-state/pipeline-sequencer.lock',
            brier_output_dir='scripts/.runtime-state/brier',
            resolution_sync_seconds=0.0,
            brier_snapshot_seconds=0.0,
            quarantine_seconds=600.0,
        )

    def test_launch_status_message_uses_fresh_default(self) -> None:
        message = prepare_and_launch.launch_status_message(
            prepare_result={
                'dispatch': {
                    'dispatch_id': 'dispatch-case-20260413-deadbeef',
                }
            }
        )
        self.assertEqual(message, 'Fresh case claimed and dispatch launched')

    def test_launch_status_message_uses_refresh_stage(self) -> None:
        message = prepare_and_launch.launch_status_message(
            prepare_result={
                'dispatch': {
                    'dispatch_id': 'dispatch-case-20260413-deadbeef',
                    'dispatch_stage': 'refresh',
                }
            }
        )
        self.assertEqual(message, 'Refresh case dispatch launched')

    def test_decide_refresh_mode_preserves_light_path_for_material_move(self) -> None:
        result = pipeline_sequencer_candidates.decide_refresh_mode({
            'price_delta': 0.07,
            'hours_since_last_forecast': 2,
            'hours_to_close': 48,
        })
        self.assertEqual(result['mode'], 'light')
        self.assertEqual(result['reasons'], ['material_price_move'])

    def test_decide_refresh_mode_escalates_to_full_for_large_move(self) -> None:
        result = pipeline_sequencer_candidates.decide_refresh_mode({
            'price_delta': 0.15,
            'hours_since_last_forecast': 2,
            'hours_to_close': 48,
        })
        self.assertEqual(result['mode'], 'full')
        self.assertIn('large_price_move', result['reasons'])

    def test_decide_refresh_mode_escalates_to_full_for_stale_forecast(self) -> None:
        result = pipeline_sequencer_candidates.decide_refresh_mode({
            'price_delta': 0.06,
            'hours_since_last_forecast': 18,
            'hours_to_close': 48,
        })
        self.assertEqual(result['mode'], 'full')
        self.assertIn('stale_forecast', result['reasons'])

    def test_decide_refresh_mode_escalates_to_full_near_close(self) -> None:
        result = pipeline_sequencer_candidates.decide_refresh_mode({
            'price_delta': 0.06,
            'hours_since_last_forecast': 2,
            'hours_to_close': 6,
        })
        self.assertEqual(result['mode'], 'full')
        self.assertIn('near_close', result['reasons'])

    def test_duplicate_launch_marker_detection_ignores_single_canonical_launch(self) -> None:
        duplicated, messages = case_artifact_contract_audit._timeline_has_duplicate_launch_markers({
            'timeline': [
                {'message': 'Fresh case claimed and dispatch launched'},
                {'message': 'Decision-Maker completed and packet rendered'},
            ]
        })
        self.assertFalse(duplicated)
        self.assertEqual(messages, ['Fresh case claimed and dispatch launched'])

    def test_duplicate_launch_marker_detection_flags_multiple_launches(self) -> None:
        duplicated, messages = case_artifact_contract_audit._timeline_has_duplicate_launch_markers({
            'timeline': [
                {'message': 'Fresh case claimed and dispatch launched'},
                {'message': 'Sequential runner claimed case and is waiting for synthesis completion'},
            ]
        })
        self.assertTrue(duplicated)
        self.assertEqual(
            messages,
            [
                'Fresh case claimed and dispatch launched',
                'Sequential runner claimed case and is waiting for synthesis completion',
            ],
        )

    def test_artifact_contract_reports_multiple_active_canonical_cases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for case_key in ['case-20260413-deadbeef', 'case-20260413-feedface']:
                case_dir = root / case_key
                case_dir.mkdir(parents=True, exist_ok=True)
                (case_dir / 'pipeline-status.json').write_text(
                    '{"case_key": "%s", "dispatch_id": "dispatch-%s", "timeline": []}\n' % (case_key, case_key)
                )

            with patch.object(
                case_artifact_contract_audit,
                'list_case_pipeline_statuses',
                return_value=[
                    {'case_key': 'case-20260413-deadbeef', 'status': 'pipeline_started', 'current_stage': 'swarm'},
                    {'case_key': 'case-20260413-feedface', 'status': 'pipeline_in_progress', 'current_stage': 'decision'},
                ],
            ):
                report = case_artifact_contract_audit.evaluate_case_artifact_contract(root, report_file=None)

        issue_codes = {issue['code'] for issue in report['issues']}
        self.assertIn('multiple_active_canonical_cases', issue_codes)
        self.assertEqual(report['status'], 'error')

    def test_prepare_launch_contract_requires_case_key(self) -> None:
        with self.assertRaisesRegex(ValueError, 'missing case_key/case_id'):
            prepare_and_launch.assert_prepare_launch_contract(
                prepare_result={'dispatch': {'dispatch_id': 'dispatch-case-20260413-deadbeef'}},
                manifest_path='/tmp/dispatch-case-20260413-deadbeef.json',
            )

    def test_prepare_launch_contract_requires_dispatch_id(self) -> None:
        with self.assertRaisesRegex(ValueError, 'missing dispatch_id'):
            prepare_and_launch.assert_prepare_launch_contract(
                prepare_result={'case': {'case_key': 'case-20260413-deadbeef'}},
                manifest_path='/tmp/dispatch-case-20260413-deadbeef.json',
            )

    def test_prepare_launch_contract_requires_manifest_path(self) -> None:
        with self.assertRaisesRegex(ValueError, 'manifest_path is empty'):
            prepare_and_launch.assert_prepare_launch_contract(
                prepare_result={
                    'case': {'case_key': 'case-20260413-deadbeef'},
                    'dispatch': {'dispatch_id': 'dispatch-case-20260413-deadbeef'},
                },
                manifest_path='',
            )

    def test_sequencer_launch_boundary_requires_case_key(self) -> None:
        with self.assertRaisesRegex(RuntimeError, 'canonical launch path returned no case key'):
            pipeline_sequencer_runner.assert_sequencer_launch_boundary(
                prepare_result={'payload': {'prepare_result': {'case': {}}}},
                mode='new_case',
            )

    def test_classify_prepare_failure_detects_timeout(self) -> None:
        prepared = {
            'ok': False,
            'payload': {'status': 'timeout'},
            'stderr': 'command timed out after 120.0s',
        }
        self.assertEqual(pipeline_sequencer_candidates.classify_prepare_failure(prepared), 'prepare_launch_timed_out')

    def test_sequencer_new_case_timeout_recovers_to_active_case(self) -> None:
        args = self.make_args()
        policy = {
            'enabled': True,
            'resume_existing': False,
            'allow_new_case_claims': True,
            'poll_seconds': 15.0,
            'idle_seconds': 60.0,
            'max_case_seconds': 7200.0,
        }
        prepared = {
            'ok': False,
            'payload': {'status': 'timeout'},
            'stderr': 'command timed out after 120.0s',
        }
        waited = {'ok': True, 'pipeline_summary': {'status': 'pipeline_completed'}}
        resumable = {'case_key': 'case-20260413-timeoutbeef', 'status': 'pipeline_started'}

        with patch.object(pipeline_sequencer_runner, 'select_resumable_case', return_value=resumable), \
             patch.object(pipeline_sequencer_runner, 'select_refresh_case', return_value={'ok': False}), \
             patch.object(pipeline_sequencer_runner, 'manual_launch_next', return_value=prepared), \
             patch.object(pipeline_sequencer_runner, 'wait_for_case', return_value=waited) as wait_mock:
            result = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())

        self.assertEqual(result['status'], 'processed_new_case_after_launch_timeout')
        self.assertTrue(result['launch_timeout_recovered'])
        wait_mock.assert_called_once()
        self.assertEqual(wait_mock.call_args.args[0], 'case-20260413-timeoutbeef')

    def test_sequencer_defers_nonterminal_existing_case_failure_without_quarantine(self) -> None:
        args = self.make_args()
        policy = {
            'enabled': True,
            'resume_existing': True,
            'allow_new_case_claims': True,
            'poll_seconds': 15.0,
            'idle_seconds': 60.0,
            'max_case_seconds': 7200.0,
        }
        resumable = {
            'case_key': 'case-20260413-deferbeef',
            'market_id': 'market-defer',
            'dispatch_id': 'dispatch-case-20260413-deferbeef-20260413T000000Z',
            'status': 'pipeline_in_progress',
        }
        waited = {
            'ok': False,
            'error': 'watchdog_reconcile_failed',
            'pipeline_summary': {
                'case_key': 'case-20260413-deferbeef',
                'status': 'pipeline_in_progress',
                'current_stage': 'decision',
            },
        }

        with tempfile.TemporaryDirectory() as tmpdir, \
             patch.object(pipeline_sequencer_runner, 'STAGE_RETRY_REGISTRY_PATH', Path(tmpdir) / 'stage-launch-retries.json'), \
             patch.object(pipeline_sequencer_runner, 'select_resumable_case', return_value=resumable), \
             patch.object(pipeline_sequencer_runner, 'wait_for_case', return_value=waited) as wait_mock:
            result = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())

        wait_mock.assert_called_once()
        self.assertTrue(result['ok'])
        self.assertEqual(result['status'], 'existing_case_deferred')
        self.assertTrue(result['deferred_because_nonterminal'])
        self.assertEqual(result['deferred_error'], 'watchdog_reconcile_failed')

    def test_sequencer_new_case_defers_nonterminal_transient_failure_without_quarantine(self) -> None:
        args = self.make_args()
        policy = {
            'enabled': True,
            'resume_existing': False,
            'allow_new_case_claims': True,
            'poll_seconds': 15.0,
            'idle_seconds': 60.0,
            'max_case_seconds': 7200.0,
        }
        prepared = {
            'ok': True,
            'payload': {
                'prepare_result': {
                    'case': {'case_key': 'case-20260413-newdefer'},
                }
            },
        }
        waited = {
            'ok': False,
            'error': 'watchdog_action_failed',
            'pipeline_summary': {
                'case_key': 'case-20260413-newdefer',
                'status': 'pipeline_in_progress',
                'current_stage': 'synthesis',
            },
        }

        with tempfile.TemporaryDirectory() as tmpdir, \
             patch.object(pipeline_sequencer_runner, 'STAGE_RETRY_REGISTRY_PATH', Path(tmpdir) / 'stage-launch-retries.json'), \
             patch.object(pipeline_sequencer_runner, 'select_resumable_case', return_value=None), \
             patch.object(pipeline_sequencer_runner, 'select_refresh_case', return_value={'ok': False}), \
             patch.object(pipeline_sequencer_runner, 'manual_launch_next', return_value=prepared), \
             patch.object(pipeline_sequencer_runner, 'wait_for_case', return_value=waited):
            result = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())

        self.assertTrue(result['ok'])
        self.assertEqual(result['status'], 'new_case_deferred')
        self.assertTrue(result['deferred_because_nonterminal'])
        self.assertEqual(result['deferred_error'], 'watchdog_action_failed')

    def test_sequencer_new_case_timeout_does_not_defer_forever(self) -> None:
        args = self.make_args()
        policy = {
            'enabled': True,
            'resume_existing': False,
            'allow_new_case_claims': True,
            'poll_seconds': 15.0,
            'idle_seconds': 60.0,
            'max_case_seconds': 7200.0,
        }
        prepared = {
            'ok': True,
            'payload': {
                'prepare_result': {
                    'case': {'case_key': 'case-20260413-timeoutnew'},
                }
            },
        }
        waited = {
            'ok': False,
            'error': 'pipeline_timeout',
            'pipeline_summary': {
                'case_key': 'case-20260413-timeoutnew',
                'status': 'pipeline_in_progress',
                'current_stage': 'decision',
                'started_at': '2000-01-01T00:00:00+00:00',
            },
        }

        with patch.object(pipeline_sequencer_runner, 'select_resumable_case', return_value=None), \
             patch.object(pipeline_sequencer_runner, 'select_refresh_case', return_value={'ok': False}), \
             patch.object(pipeline_sequencer_runner, 'manual_launch_next', return_value=prepared), \
             patch.object(pipeline_sequencer_runner, 'wait_for_case', return_value=waited):
            result = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())

        self.assertFalse(result['ok'])
        self.assertEqual(result['status'], 'processed_new_case')

    def test_stage_launch_retry_budget_escalates_to_stuck(self) -> None:
        args = self.make_args()
        policy = {
            'enabled': True,
            'resume_existing': False,
            'allow_new_case_claims': True,
            'poll_seconds': 15.0,
            'idle_seconds': 60.0,
            'max_case_seconds': 7200.0,
            'defer_retry_budget': 2,
        }
        prepared = {
            'ok': True,
            'payload': {
                'prepare_result': {
                    'case': {'case_key': 'case-20260413-stuckbeef'},
                }
            },
        }
        waited = {
            'ok': False,
            'error': 'watchdog_action_failed',
            'pipeline_summary': {
                'case_key': 'case-20260413-stuckbeef',
                'status': 'pipeline_in_progress',
                'current_stage': 'synthesis',
            },
            'watchdog_result': {
                'action_failures': [
                    {'name': 'launch_synthesis_for_existing_case', 'result': {'ok': False}}
                ]
            },
        }

        with tempfile.TemporaryDirectory() as tmpdir, \
             patch.object(pipeline_sequencer_runner, 'STAGE_RETRY_REGISTRY_PATH', Path(tmpdir) / 'stage-launch-retries.json'), \
             patch.object(pipeline_sequencer_runner, 'select_resumable_case', return_value=None), \
             patch.object(pipeline_sequencer_runner, 'select_refresh_case', return_value={'ok': False}), \
             patch.object(pipeline_sequencer_runner, 'manual_launch_next', return_value=prepared), \
             patch.object(pipeline_sequencer_runner, 'wait_for_case', return_value=waited):
            first = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())
            second = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())
            third = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())

        self.assertTrue(first['ok'])
        self.assertEqual(first['status'], 'new_case_deferred')
        self.assertTrue(second['ok'])
        self.assertEqual(second['status'], 'new_case_deferred')
        self.assertFalse(third['ok'])
        self.assertEqual(third['status'], 'stage_launch_stuck')
        self.assertEqual(third['retry_entry']['attempts'], 3)

    def test_sequencer_sleep_plan_uses_short_retry_after_defer(self) -> None:
        args = self.make_args()
        plan = pipeline_sequencer_runner.sequencer_sleep_plan(
            {'status': 'new_case_deferred'},
            policy={'poll_seconds': 15.0, 'idle_seconds': 60.0},
            args=args,
        )
        self.assertTrue(plan['deferred'])
        self.assertEqual(plan['heartbeat_state'], 'deferred_retry_sleep')
        self.assertEqual(plan['sleep_seconds'], 10.0)

    def test_sequencer_debounced_light_refresh_falls_through_to_new_case_claim(self) -> None:
        args = self.make_args()
        policy = {
            'enabled': True,
            'resume_existing': False,
            'allow_new_case_claims': True,
            'poll_seconds': 15.0,
            'idle_seconds': 60.0,
            'max_case_seconds': 7200.0,
        }
        refresh_candidate = {
            'ok': True,
            'payload': {
                'case_key': 'case-20260413-refreshbeef',
                'latest_forecast_case_key': 'case-20260413-refreshbeef',
                'market_id': 'market-refresh',
                'current_price': 0.79,
                'last_reasoned_price': 0.71,
                'price_delta': 0.08,
            },
        }
        prepared = {
            'ok': True,
            'payload': {
                'prepare_result': {
                    'case': {'case_key': 'case-20260413-freshbeef'},
                }
            },
        }
        waited = {'ok': True, 'pipeline_summary': {'status': 'pipeline_completed'}}

        with patch.object(pipeline_sequencer_runner, 'select_resumable_case', return_value=None), \
             patch.object(pipeline_sequencer_runner, 'select_refresh_case', return_value=refresh_candidate), \
             patch.object(pipeline_sequencer_runner, 'load_refresh_watermarks', return_value={'entries': {'market-refresh': {'trigger_market_price': 0.79}}}), \
             patch.object(pipeline_sequencer_runner, 'manual_launch_next', return_value=prepared) as launch_mock, \
             patch.object(pipeline_sequencer_runner, 'wait_for_case', return_value=waited):
            result = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())

        launch_mock.assert_called_once_with(pretty=False)
        self.assertTrue(result['ok'])
        self.assertEqual(result['status'], 'processed_new_case')
        self.assertEqual(result['case_key'], 'case-20260413-freshbeef')

    def test_sequencer_new_case_uses_manual_launch_then_waits_without_local_launch_write(self) -> None:
        args = self.make_args()
        policy = {
            'enabled': True,
            'resume_existing': False,
            'allow_new_case_claims': True,
            'poll_seconds': 15.0,
            'idle_seconds': 60.0,
            'max_case_seconds': 7200.0,
        }
        prepared = {
            'ok': True,
            'payload': {
                'prepare_result': {
                    'case': {'case_key': 'case-20260413-deadbeef'},
                }
            },
        }
        waited = {'ok': True, 'pipeline_summary': {'status': 'pipeline_completed'}}

        with patch.object(pipeline_sequencer_runner, 'select_resumable_case', return_value=None), \
             patch.object(pipeline_sequencer_runner, 'select_refresh_case', return_value={'ok': False}), \
             patch.object(pipeline_sequencer_runner, 'manual_launch_next', return_value=prepared) as launch_mock, \
             patch.object(pipeline_sequencer_runner, 'wait_for_case', return_value=waited) as wait_mock:
            result = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())

        launch_mock.assert_called_once_with(pretty=False)
        wait_mock.assert_called_once()
        self.assertEqual(wait_mock.call_args.args[0], 'case-20260413-deadbeef')
        self.assertEqual(result['status'], 'processed_new_case')
        self.assertNotIn('launch_status_write', result)

    def test_sequencer_full_refresh_uses_manual_launch_case_then_waits(self) -> None:
        args = self.make_args()
        policy = {
            'enabled': True,
            'resume_existing': False,
            'allow_new_case_claims': True,
            'poll_seconds': 15.0,
            'idle_seconds': 60.0,
            'max_case_seconds': 7200.0,
        }
        refresh_candidate = {
            'ok': True,
            'payload': {
                'case_id': '1234',
                'case_key': 'case-20260413-feedface',
                'market_id': 'market-1',
                'price_delta': 0.2,
                'hours_since_last_forecast': 1,
                'hours_to_close': 24,
            },
        }
        prepared = {
            'ok': True,
            'payload': {
                'prepare_result': {
                    'case': {'case_key': 'case-20260413-feedface'},
                }
            },
        }
        waited = {'ok': True, 'pipeline_summary': {'status': 'pipeline_completed'}}

        with patch.object(pipeline_sequencer_runner, 'select_resumable_case', return_value=None), \
             patch.object(pipeline_sequencer_runner, 'select_refresh_case', return_value=refresh_candidate), \
             patch.object(pipeline_sequencer_runner, 'manual_launch_case', return_value=prepared) as launch_case_mock, \
             patch.object(pipeline_sequencer_runner, 'manual_launch_market') as launch_market_mock, \
             patch.object(pipeline_sequencer_runner, 'wait_for_case', return_value=waited) as wait_mock:
            result = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())

        launch_case_mock.assert_called_once()
        self.assertEqual(launch_case_mock.call_args.args[0], '1234')
        self.assertEqual(launch_case_mock.call_args.kwargs.get('pretty'), False)
        self.assertEqual(launch_case_mock.call_args.kwargs.get('refresh_mode'), 'full')
        self.assertEqual(launch_case_mock.call_args.kwargs.get('refresh_reasons'), ['large_price_move'])
        launch_market_mock.assert_not_called()
        wait_mock.assert_called_once()
        self.assertEqual(wait_mock.call_args.args[0], 'case-20260413-feedface')
        self.assertEqual(result['status'], 'processed_refresh_case')

    def test_sequencer_debounces_same_regime_light_refresh_candidate(self) -> None:
        args = self.make_args()
        policy = {
            'enabled': True,
            'resume_existing': False,
            'allow_new_case_claims': True,
            'poll_seconds': 15.0,
            'idle_seconds': 60.0,
            'max_case_seconds': 7200.0,
        }
        refresh_candidate = {
            'ok': True,
            'payload': {
                'case_key': 'case-20260413-cafebabe',
                'market_id': 'market-2',
                'contract_id': 'contract-2',
                'current_price': 0.77,
                'last_reasoned_price': 0.70,
                'price_delta': 0.07,
                'hours_since_last_forecast': 0.05,
                'hours_to_close': 36,
            },
        }
        watermark = {
            'entries': {
                'market-2:contract-2': {
                    'trigger_market_price': 0.76,
                    'case_key': 'case-20260413-cafebabe'
                }
            },
            'updated_at': ''
        }

        no_eligible_prepare = {
            'ok': False,
            'manual_status': 'idle_no_eligible_market',
            'payload': {},
            'stdout': 'ERROR: no eligible market found',
            'stderr': '',
        }

        with patch.object(pipeline_sequencer_runner, 'select_resumable_case', return_value=None), \
             patch.object(pipeline_sequencer_runner, 'select_refresh_case', return_value=refresh_candidate), \
             patch.object(pipeline_sequencer_runner, 'load_refresh_watermarks', return_value=watermark), \
             patch.object(pipeline_sequencer_runner, 'manual_launch_next', return_value=no_eligible_prepare), \
             patch.object(pipeline_sequencer_runner, 'run_light_refresh_update') as light_mock:
            result = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())

        light_mock.assert_not_called()
        self.assertEqual(result['status'], 'debounced_light_refresh_candidate')
        self.assertTrue(result['ok'])

    def test_sequencer_retriggers_light_refresh_after_new_incremental_move(self) -> None:
        args = self.make_args()
        policy = {
            'enabled': True,
            'resume_existing': False,
            'allow_new_case_claims': True,
            'poll_seconds': 15.0,
            'idle_seconds': 60.0,
            'max_case_seconds': 7200.0,
        }
        refresh_candidate = {
            'ok': True,
            'payload': {
                'case_key': 'case-20260413-cafebabe',
                'market_id': 'market-2',
                'contract_id': 'contract-2',
                'current_price': 0.80,
                'last_reasoned_price': 0.70,
                'price_delta': 0.10,
                'hours_since_last_forecast': 0.05,
                'hours_to_close': 36,
            },
        }
        watermark = {
            'entries': {
                'market-2:contract-2': {
                    'trigger_market_price': 0.76,
                    'case_key': 'case-20260413-cafebabe'
                }
            },
            'updated_at': ''
        }

        with patch.object(pipeline_sequencer_runner, 'select_resumable_case', return_value=None), \
             patch.object(pipeline_sequencer_runner, 'select_refresh_case', return_value=refresh_candidate), \
             patch.object(pipeline_sequencer_runner, 'load_refresh_watermarks', return_value=watermark), \
             patch.object(pipeline_sequencer_runner, 'record_refresh_watermark'), \
             patch.object(pipeline_sequencer_runner, 'run_light_refresh_update', return_value={'ok': True}) as light_mock:
            result = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())

        light_mock.assert_called_once_with('case-20260413-cafebabe', pretty=False)
        self.assertEqual(result['status'], 'processed_light_refresh_case')
        self.assertTrue(result['ok'])

    def test_sequencer_light_refresh_uses_direct_light_refresh_path_not_manual_launch(self) -> None:
        args = self.make_args()
        policy = {
            'enabled': True,
            'resume_existing': False,
            'allow_new_case_claims': True,
            'poll_seconds': 15.0,
            'idle_seconds': 60.0,
            'max_case_seconds': 7200.0,
        }
        refresh_candidate = {
            'ok': True,
            'payload': {
                'case_key': 'case-20260413-cafebabe',
                'market_id': 'market-2',
                'price_delta': 0.07,
                'hours_since_last_forecast': 2,
                'hours_to_close': 36,
            },
        }

        with patch.object(pipeline_sequencer_runner, 'select_resumable_case', return_value=None), \
             patch.object(pipeline_sequencer_runner, 'select_refresh_case', return_value=refresh_candidate), \
             patch.object(pipeline_sequencer_runner, 'run_light_refresh_update', return_value={'ok': True}) as light_mock, \
             patch.object(pipeline_sequencer_runner, 'manual_launch_case') as launch_case_mock, \
             patch.object(pipeline_sequencer_runner, 'manual_launch_market') as launch_market_mock, \
             patch.object(pipeline_sequencer_runner, 'wait_for_case') as wait_mock:
            result = pipeline_sequencer_runner.run_sequencer_pass(args, policy, excluded_case_keys=set(), excluded_market_ids=set())

        light_mock.assert_called_once_with('case-20260413-cafebabe', pretty=False)
        launch_case_mock.assert_not_called()
        launch_market_mock.assert_not_called()
        wait_mock.assert_not_called()
        self.assertEqual(result['status'], 'processed_light_refresh_case')

    def test_select_refresh_case_gate_blocks_when_canonical_active_case_exists(self) -> None:
        with patch.object(
            select_refresh_case_module,
            'first_active_nonterminal_case',
            return_value={'case_key': 'case-20260413-deadbeef', 'status': 'pipeline_in_progress', 'current_stage': 'swarm'},
        ), patch.object(
            select_refresh_case_module,
            'first_blocking_case_without_completed_decision_packet',
            return_value={},
        ):
            with self.assertRaisesRegex(ValueError, 'pipeline already busy with a canonical non-terminal case'):
                select_refresh_case_module.enforce_canonical_case_gate(allow_when_busy=False)

    def test_select_refresh_case_gate_blocks_when_prior_case_not_cleanly_finished(self) -> None:
        with patch.object(
            select_refresh_case_module,
            'first_active_nonterminal_case',
            return_value={},
        ), patch.object(
            select_refresh_case_module,
            'first_blocking_case_without_completed_decision_packet',
            return_value={'case_key': 'case-20260413-feedface', 'status': 'pipeline_completed'},
        ):
            with self.assertRaisesRegex(ValueError, 'pipeline blocked by prior canonical case without clean decision-packet completion'):
                select_refresh_case_module.enforce_canonical_case_gate(allow_when_busy=False)

    def test_select_refresh_case_gate_allows_override_when_busy(self) -> None:
        with patch.object(
            select_refresh_case_module,
            'first_active_nonterminal_case',
            return_value={'case_key': 'case-20260413-deadbeef', 'status': 'pipeline_in_progress', 'current_stage': 'swarm'},
        ):
            select_refresh_case_module.enforce_canonical_case_gate(allow_when_busy=True)

    def test_pipeline_health_surfaces_duplicate_launch_marker_drift(self) -> None:
        args = types.SimpleNamespace(
            heartbeat_file='scripts/.runtime-state/pipeline-heartbeat.json',
            quarantine_file='scripts/.runtime-state/pipeline-quarantine.json',
            report_file='scripts/.runtime-state/pipeline-health-report.json',
            control_file='scripts/.runtime-state/pipeline-automation-control.json',
            max_heartbeat_age_seconds=1800.0,
            max_resolution_sync_age_seconds=5400.0,
            max_brier_age_seconds=172800.0,
            max_quarantine_count=10,
            artifact_contract_root='qualitative-db/40-research/cases',
            artifact_contract_report_file='scripts/.runtime-state/pipeline-artifact-contract-report.json',
            skip_artifact_contract_check=False,
            decided_market_watcher_heartbeat_file='scripts/.runtime-state/decided-market-watcher-heartbeat.json',
            max_decided_market_watcher_age_seconds=120.0,
            skip_decided_market_watcher_check=True,
            market_checker_env_file='.env.postgres.local',
            market_checker_db_url='',
            market_checker_psql='/opt/homebrew/opt/postgresql@16/bin/psql',
            max_market_snapshot_age_seconds=3600.0,
            skip_market_checker_check=True,
            synthesis_parse_failure_lookback_hours=24.0,
            max_synthesis_parse_failures=2,
            pretty=False,
        )
        artifact_report = {
            'status': 'warn',
            'exit_code': 1,
            'issues': [
                {
                    'level': 'warn',
                    'code': 'duplicate_launch_timeline_markers',
                    'case_key': 'case-20260413-deadbeef',
                    'message': 'Canonical case pipeline-status.json contains multiple launch/start timeline markers; launch status writing may be duplicated',
                }
            ],
        }

        with patch.object(check_pipeline_health, 'load_control_file', return_value={}), \
             patch.object(check_pipeline_health, 'resolve_sequencer_policy', return_value={'enabled': False, 'resume_existing': True, 'allow_new_case_claims': False}), \
             patch.object(check_pipeline_health, 'load_json_file', return_value={}), \
             patch.object(check_pipeline_health, 'evaluate_case_artifact_contract', return_value=artifact_report), \
             patch.object(check_pipeline_health, 'write_json_file'):
            report = check_pipeline_health.evaluate(args)

        issue_codes = {issue['code'] for issue in report['issues']}
        self.assertIn('artifact_contract_duplicate_launch_timeline_markers', issue_codes)
        self.assertIn('duplicate_launch_marker_drift', issue_codes)
        drift_issue = next(issue for issue in report['issues'] if issue['code'] == 'duplicate_launch_marker_drift')
        self.assertEqual(drift_issue['case_keys'], ['case-20260413-deadbeef'])

    def test_select_refresh_case_run_query_serializes_exclusions(self) -> None:
        captured: dict[str, object] = {}

        def fake_run(cmd, input, text, capture_output):
            captured['cmd'] = cmd
            return types.SimpleNamespace(returncode=0, stdout='{}\n', stderr='')

        with patch.object(select_refresh_case_module.subprocess, 'run', side_effect=fake_run):
            select_refresh_case_module.run_query(
                'psql',
                'postgres://example',
                'select 1;',
                allow_when_busy=False,
                platform='polymarket',
                contract_id='yes',
                min_price_delta='0.05',
                excluded_market_ids=['m2', 'm1', 'm2'],
                excluded_case_keys=['c2', 'c1', 'c2'],
            )

        cmd = captured['cmd']
        self.assertIn('excluded_market_ids=["m1","m2"]', cmd)
        self.assertIn('excluded_case_keys=["c1","c2"]', cmd)


if __name__ == '__main__':
    unittest.main()
