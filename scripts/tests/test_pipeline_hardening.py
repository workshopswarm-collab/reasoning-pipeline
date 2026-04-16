from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]

COMMON_PATH = REPO_ROOT / 'roles' / 'decision-maker' / 'common.py'
common_spec = importlib.util.spec_from_file_location('decision_common_for_tests', COMMON_PATH)
if common_spec is None or common_spec.loader is None:
    raise RuntimeError(f'could not import {COMMON_PATH}')
decision_common = importlib.util.module_from_spec(common_spec)
common_spec.loader.exec_module(decision_common)

LAUNCH_PATH = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / 'scripts' / 'launch_dispatch_with_stateful_posts.py'
launch_spec = importlib.util.spec_from_file_location('launch_dispatch_with_stateful_posts_for_tests', LAUNCH_PATH)
if launch_spec is None or launch_spec.loader is None:
    raise RuntimeError(f'could not import {LAUNCH_PATH}')
launch_script = importlib.util.module_from_spec(launch_spec)
launch_spec.loader.exec_module(launch_script)


class PipelineHardeningTests(unittest.TestCase):
    def test_default_decision_agent_session_key_is_case_scoped(self) -> None:
        session_key = decision_common.default_decision_agent_session_key('case-20260416-d529376c')
        self.assertEqual(session_key, 'agent:decision-maker:case:case-20260416-d529376c')

    def test_summarize_logging_result_understands_multiple_logger_shapes(self) -> None:
        summary = launch_script.summarize_logging_result(
            {
                'logged_count': 2,
                'matches': [
                    {'status': 'inserted_new_row'},
                    {'status': 'updated_existing_row'},
                ],
            }
        )
        self.assertEqual(summary['inserted'], 1)
        self.assertEqual(summary['updated'], 1)
        self.assertEqual(summary['logged_rows'], 2)
        self.assertEqual(summary['candidate_count'], 2)


if __name__ == '__main__':
    unittest.main()
