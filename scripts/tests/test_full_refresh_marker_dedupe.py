from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[2] / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / 'scripts' / 'runrepairs' / 'finalize_dispatch_after_swarm.py'
MODULE_DIR = MODULE_PATH.parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


finalize_dispatch_after_swarm = load_module('finalize_dispatch_after_swarm_for_tests', MODULE_PATH)


class FullRefreshMarkerDedupeTests(unittest.TestCase):
    def test_refresh_finish_marker_sent_only_once_per_dispatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            manifest_path = tmp / 'dispatch.json'
            registry_path = tmp / 'controller-marker-registry.json'
            manifest = {
                'runtime_defaults': {
                    'refresh_finish_marker': 'FULL REFRESH SWARM COMPLETED | case=case-test | dispatch_id=dispatch-test | next_stage=synthesis'
                },
                'bootstrap_state': {
                    'chat_id': '123',
                    'controller_topic': {'topic_id': '456'},
                },
            }
            manifest_path.write_text(json.dumps(manifest) + '\n')

            with patch.object(finalize_dispatch_after_swarm, 'MARKER_REGISTRY_PATH', registry_path), patch.object(
                finalize_dispatch_after_swarm,
                'send_visible_telegram_message',
                return_value={'ok': True, 'sentAt': '2026-04-14T02:44:00Z'},
            ) as send_mock:
                first_result, first_error = finalize_dispatch_after_swarm.maybe_send_refresh_finish_marker(
                    manifest=manifest,
                    manifest_path=manifest_path,
                    dispatch_id='dispatch-test',
                )
                second_result, second_error = finalize_dispatch_after_swarm.maybe_send_refresh_finish_marker(
                    manifest=manifest,
                    manifest_path=manifest_path,
                    dispatch_id='dispatch-test',
                )

        self.assertIsNone(first_error)
        self.assertIsNotNone(first_result)
        self.assertIsNone(second_error)
        self.assertIsNone(second_result)
        send_mock.assert_called_once()
        saved_manifest = json.loads(manifest_path.read_text())
        self.assertEqual(
            saved_manifest['bootstrap_state']['refresh_finish_marker_sent_at'],
            '2026-04-14T02:44:00Z',
        )
        saved_registry = json.loads(registry_path.read_text())
        self.assertIn('dispatch-test:refresh_finish', saved_registry['entries'])


if __name__ == '__main__':
    unittest.main()
