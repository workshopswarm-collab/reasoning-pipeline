from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
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


pipeline_automation_actions = load_module('pipeline_automation_actions_synthesis_for_tests', MODULE_PATH)


class SynthesisLaunchHandoffTests(unittest.TestCase):
    def write_status(self, root: Path, payload: dict[str, object]) -> Path:
        status_path = root / 'qualitative-db/40-research/cases/case-test/researcher-analyses/2026-04-13/dispatch-case-test/synthesis-stage-status.json'
        status_path.parent.mkdir(parents=True, exist_ok=True)
        status_path.write_text(json.dumps(payload) + '\n')
        return status_path

    def test_launch_synthesis_if_needed_returns_already_completed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            status_path = self.write_status(repo, {'status': 'synthesis_completed'})
            with patch.object(pipeline_automation_actions, 'REPO_ROOT', repo), patch.object(
                pipeline_automation_actions,
                'summarize_case_pipeline_status',
                return_value={'dispatch_id': 'dispatch-test', 'market_id': 'market-test', 'market_title': 'Test market'},
            ), patch.object(
                pipeline_automation_actions,
                'update_case_pipeline_status',
            ) as update_status, patch.object(
                pipeline_automation_actions,
                'run_python_script',
                return_value={'ok': True, 'payload': {'reason': 'already_completed'}},
            ):
                result = pipeline_automation_actions.launch_synthesis_if_needed('case-test', pretty=False)

        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(result['launch_status'], 'already_completed')
        update_status.assert_called_once()
        self.assertEqual(result['status_file'], str(status_path.relative_to(repo)))

    def test_launch_synthesis_if_needed_returns_already_running(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            self.write_status(repo, {'status': 'final_synthesis_launched'})
            with patch.object(pipeline_automation_actions, 'REPO_ROOT', repo), patch.object(
                pipeline_automation_actions,
                'summarize_case_pipeline_status',
                return_value={'dispatch_id': 'dispatch-test', 'market_id': 'market-test', 'market_title': 'Test market'},
            ), patch.object(
                pipeline_automation_actions,
                'update_case_pipeline_status',
            ) as update_status, patch.object(
                pipeline_automation_actions,
                'run_python_script',
                return_value={'ok': True, 'payload': {'reason': 'already_running'}},
            ):
                result = pipeline_automation_actions.launch_synthesis_if_needed('case-test', pretty=False)

        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(result['launch_status'], 'already_running')
        update_status.assert_called_once()

    def test_launch_synthesis_if_needed_returns_started_and_marks_handoff_sent(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            status_path = self.write_status(repo, {'status': 'ready_for_final_synthesis'})
            with patch.object(pipeline_automation_actions, 'REPO_ROOT', repo), patch.object(
                pipeline_automation_actions,
                'summarize_case_pipeline_status',
                return_value={'dispatch_id': 'dispatch-test', 'market_id': 'market-test', 'market_title': 'Test market'},
            ), patch.object(
                pipeline_automation_actions,
                'update_case_pipeline_status',
            ) as update_status, patch.object(
                pipeline_automation_actions,
                'run_python_script',
                return_value={'ok': True, 'payload': {'status': 'final_synthesis_launched', 'pid': 999}},
            ), patch.object(
                pipeline_automation_actions,
                'load_json_if_exists',
                side_effect=[
                    {'status': 'ready_for_final_synthesis'},
                    {'status': 'final_synthesis_launching'},
                ],
            ):
                result = pipeline_automation_actions.launch_synthesis_if_needed('case-test', pretty=False)

        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(result['launch_status'], 'started')
        self.assertEqual(result['status_file'], str(status_path.relative_to(repo)))
        _, kwargs = update_status.call_args
        self.assertEqual(kwargs['stage_detail_patch']['synthesis'], 'handoff_sent')

    def test_launch_synthesis_if_needed_bootstraps_missing_status_file_via_kickoff(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir).resolve()
            status_path = self.write_status(repo, {'status': 'ready_for_final_synthesis'})
            def run_script_side_effect(script_path, *args, pretty=False, timeout_seconds=None):
                script_name = Path(script_path).name
                if script_name == 'kickoff_synthesis_after_swarm.py':
                    return {'ok': True, 'status_path': str(status_path.relative_to(repo))}
                return {'ok': True, 'payload': {'status': 'final_synthesis_launched', 'pid': 999}}

            with patch.object(pipeline_automation_actions, 'REPO_ROOT', repo), patch.object(
                pipeline_automation_actions,
                'summarize_case_pipeline_status',
                return_value={'dispatch_id': 'dispatch-test', 'market_id': 'market-test', 'market_title': 'Test market'},
            ), patch.object(
                pipeline_automation_actions,
                'synthesis_status_file',
                side_effect=[None, status_path],
            ), patch.object(
                pipeline_automation_actions,
                'update_case_pipeline_status',
            ) as update_status, patch.object(
                pipeline_automation_actions,
                'run_python_script',
                side_effect=run_script_side_effect,
            ), patch.object(
                pipeline_automation_actions,
                'load_json_if_exists',
                side_effect=[
                    {'status': 'ready_for_final_synthesis'},
                    {'status': 'final_synthesis_launching'},
                ],
            ):
                result = pipeline_automation_actions.launch_synthesis_if_needed('case-test', pretty=False)

        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(result['launch_status'], 'started')
        self.assertEqual(result['status_file'], str(status_path.relative_to(repo)))
        update_status.assert_called_once()

    def test_launch_synthesis_if_needed_marks_retryable_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            self.write_status(repo, {'status': 'ready_for_final_synthesis'})
            with patch.object(pipeline_automation_actions, 'REPO_ROOT', repo), patch.object(
                pipeline_automation_actions,
                'summarize_case_pipeline_status',
                return_value={'dispatch_id': 'dispatch-test', 'market_id': 'market-test', 'market_title': 'Test market'},
            ), patch.object(
                pipeline_automation_actions,
                'update_case_pipeline_status',
            ) as update_status, patch.object(
                pipeline_automation_actions,
                'run_python_script',
                return_value={'ok': False, 'stderr': 'transient boom', 'payload': {'status': 'ready_for_final_synthesis'}},
            ):
                result = pipeline_automation_actions.launch_synthesis_if_needed('case-test', pretty=False)

        self.assertIsNotNone(result)
        assert result is not None
        self.assertFalse(result['ok'])
        self.assertEqual(result['launch_status'], 'retryable_transient_failure')
        update_status.assert_called_once()


if __name__ == '__main__':
    unittest.main()
