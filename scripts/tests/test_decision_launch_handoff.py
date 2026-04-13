from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

SCRIPTS_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

MODULE_PATH = SCRIPTS_DIR / 'pipeline_automation_actions.py'


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


pipeline_automation_actions = load_module('pipeline_automation_actions_for_tests', MODULE_PATH)


class DecisionLaunchHandoffTests(unittest.TestCase):
    def test_launch_decision_maker_returns_already_completed(self) -> None:
        with patch.object(
            pipeline_automation_actions,
            'reconcile_decision',
            return_value={'ok': True, 'payload': {'health': 'ready'}},
        ), patch.object(pipeline_automation_actions, 'run_python_script') as run_script:
            result = pipeline_automation_actions.launch_decision_maker('case-test', pretty=False)

        self.assertTrue(result['ok'])
        self.assertEqual(result['launch_status'], 'already_completed')
        run_script.assert_not_called()

    def test_launch_decision_maker_returns_already_running(self) -> None:
        with patch.object(
            pipeline_automation_actions,
            'reconcile_decision',
            return_value={'ok': True, 'payload': {'health': 'in_progress'}},
        ), patch.object(pipeline_automation_actions, 'run_python_script') as run_script:
            result = pipeline_automation_actions.launch_decision_maker('case-test', pretty=False)

        self.assertTrue(result['ok'])
        self.assertEqual(result['launch_status'], 'already_running')
        run_script.assert_not_called()

    def test_launch_decision_maker_prepares_and_spawns_background_worker(self) -> None:
        prepare_payload = {
            'decision_context_path': 'roles/decision-maker/runtime/artifacts/case-test/context.json',
            'prompt_path': 'roles/decision-maker/runtime/artifacts/case-test/prompt.md',
            'decision_stage_status_path': 'qualitative-db/40-research/cases/case-test/decision-maker/artifacts/decision-stage-status.json',
        }
        with patch.object(
            pipeline_automation_actions,
            'reconcile_decision',
            return_value={'ok': True, 'payload': {'health': 'not_started'}},
        ), patch.object(
            pipeline_automation_actions,
            'run_python_script',
            return_value={'ok': True, 'payload': prepare_payload},
        ) as run_script, patch.object(
            pipeline_automation_actions,
            'spawn_background_decision_runner',
            return_value={
                'pid': 4242,
                'log_path': pipeline_automation_actions.REPO_ROOT / 'scripts/.runtime-state/decision-maker-launches/case-test.log',
                'proc': SimpleNamespace(poll=lambda: None),
            },
        ) as spawn_runner, patch.object(
            pipeline_automation_actions,
            'record_decision_launch_claim',
        ) as record_claim, patch.object(
            pipeline_automation_actions,
            'summarize_case_pipeline_status',
            return_value={'dispatch_id': 'dispatch-test', 'market_id': 'market-test', 'market_title': 'Test market'},
        ), patch.object(
            pipeline_automation_actions,
            'update_case_pipeline_status',
        ) as update_status, patch.object(pipeline_automation_actions.time, 'sleep', return_value=None):
            result = pipeline_automation_actions.launch_decision_maker('case-test', pretty=False)

        self.assertTrue(result['ok'])
        self.assertEqual(result['launch_status'], 'started')
        self.assertEqual(result['runner_pid'], 4242)
        run_script.assert_called_once()
        spawn_runner.assert_called_once()
        record_claim.assert_called_once()
        update_status.assert_called_once()

    def test_launch_decision_maker_reports_immediate_worker_failure(self) -> None:
        prepare_payload = {
            'decision_context_path': 'roles/decision-maker/runtime/artifacts/case-test/context.json',
            'prompt_path': 'roles/decision-maker/runtime/artifacts/case-test/prompt.md',
            'decision_stage_status_path': 'qualitative-db/40-research/cases/case-test/decision-maker/artifacts/decision-stage-status.json',
        }
        with patch.object(
            pipeline_automation_actions,
            'reconcile_decision',
            return_value={'ok': True, 'payload': {'health': 'not_started'}},
        ), patch.object(
            pipeline_automation_actions,
            'run_python_script',
            return_value={'ok': True, 'payload': prepare_payload},
        ), patch.object(
            pipeline_automation_actions,
            'spawn_background_decision_runner',
            return_value={
                'pid': 4343,
                'log_path': pipeline_automation_actions.REPO_ROOT / 'scripts/.runtime-state/decision-maker-launches/case-test.log',
                'proc': SimpleNamespace(poll=lambda: 1),
            },
        ), patch.object(
            pipeline_automation_actions,
            'record_decision_launch_claim',
        ), patch.object(
            pipeline_automation_actions,
            'record_decision_launch_immediate_failure',
        ) as record_failure, patch.object(
            pipeline_automation_actions,
            'summarize_case_pipeline_status',
            return_value={'dispatch_id': 'dispatch-test', 'market_id': 'market-test', 'market_title': 'Test market'},
        ), patch.object(
            pipeline_automation_actions,
            'update_case_pipeline_status',
        ), patch.object(pipeline_automation_actions.time, 'sleep', return_value=None):
            result = pipeline_automation_actions.launch_decision_maker('case-test', pretty=False)

        self.assertFalse(result['ok'])
        self.assertEqual(result['launch_status'], 'retryable_transient_failure')
        record_failure.assert_called_once()


if __name__ == '__main__':
    unittest.main()
