from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / 'scripts'
RUNTIME_SCRIPTS_DIR = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / 'scripts'

for candidate in [SCRIPTS_DIR, RUNTIME_SCRIPTS_DIR]:
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


reconcile_swarm_stage = load_module('reconcile_swarm_stage_for_tests', RUNTIME_SCRIPTS_DIR / 'reconcile_swarm_stage.py')
resume_swarm_stage = load_module('resume_swarm_stage_for_tests', RUNTIME_SCRIPTS_DIR / 'resume_swarm_stage.py')


class SwarmStateRegressionTests(unittest.TestCase):
    def test_reconcile_swarm_stage_preserves_terminal_canonical_status(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            dispatch_dir = tmp / 'dispatch-case-test'
            (dispatch_dir / 'personas').mkdir(parents=True)
            for name in reconcile_swarm_stage.EXPECTED_PERSONAS:
                (dispatch_dir / 'personas' / f'{name}.md').write_text('done')
            (dispatch_dir / 'summary.md').write_text('summary')
            (dispatch_dir / 'synthesis-stage-status.json').write_text(json.dumps({'status': 'synthesis_completed'}))
            out_path = dispatch_dir / 'swarm-stage-status.json'

            argv = ['reconcile_swarm_stage.py', '--case-key', 'case-test', '--dispatch-dir', str(dispatch_dir), '--out', str(out_path), '--pretty']
            with mock.patch.object(sys, 'argv', argv), \
                 mock.patch.object(reconcile_swarm_stage, 'summarize_case_pipeline_status', return_value={'status': 'pipeline_completed'}), \
                 mock.patch.object(reconcile_swarm_stage, 'update_case_pipeline_status') as update_mock:
                reconcile_swarm_stage.main()

            update_mock.assert_not_called()
            payload = json.loads(out_path.read_text())
            self.assertTrue(payload['canonical_update_skipped'])
            self.assertEqual(payload['canonical_status_preserved'], 'pipeline_completed')

    def test_resume_swarm_stage_preserves_terminal_canonical_status(self) -> None:
        swarm_status = {
            'case_key': 'case-test',
            'dispatch_id': 'dispatch-case-test',
            'status': 'completed',
            'manifest_path': 'roles/orchestrator/researchers-swarm-subagents/runtime/dispatch-manifests/dispatch-case-test.json',
            'synthesis_status_path': 'qualitative-db/40-research/cases/case-test/researcher-analyses/2026-04-14/dispatch-case-test/synthesis-stage-status.json',
        }
        argv = ['resume_swarm_stage.py', '--case-key', 'case-test', '--pretty']
        with mock.patch.object(sys, 'argv', argv), \
             mock.patch.object(resume_swarm_stage, 'run_json', return_value=(0, swarm_status, '', '')), \
             mock.patch.object(resume_swarm_stage, 'summarize_case_pipeline_status', return_value={'status': 'pipeline_completed'}), \
             mock.patch.object(resume_swarm_stage, 'update_case_pipeline_status') as update_mock:
            with mock.patch('builtins.print') as print_mock:
                resume_swarm_stage.main()

        update_mock.assert_not_called()
        printed = ''.join(str(call.args[0]) for call in print_mock.call_args_list if call.args)
        self.assertIn('canonical_update_skipped', printed)
        self.assertIn('pipeline_completed', printed)


if __name__ == '__main__':
    unittest.main()
