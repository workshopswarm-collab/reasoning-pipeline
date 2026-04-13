from __future__ import annotations

import importlib.util
import sys
import tempfile
import types
import unittest
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[2] / 'roles' / 'orchestrator' / 'synthesis-subagent' / 'runtime' / 'scripts'
HEALTH_PATH = Path(__file__).resolve().parents[1] / 'check_pipeline_health.py'
EXECUTOR_PATH = SCRIPTS_DIR / 'run_synthesis_executor.py'
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


executor = load_module('run_synthesis_executor_for_tests', EXECUTOR_PATH)
health = load_module('check_pipeline_health_for_tests', HEALTH_PATH)


class SynthesisJsonHardeningTests(unittest.TestCase):
    def test_extract_json_payload_accepts_plain_json(self) -> None:
        payload = executor.extract_json_payload('{"answer":"yes","confidence":0.8}')
        self.assertEqual(payload['answer'], 'yes')

    def test_extract_json_payload_recovers_from_markdown_fence(self) -> None:
        payload = executor.extract_json_payload('```json\n{"answer":"yes"}\n```')
        self.assertEqual(payload['answer'], 'yes')

    def test_extract_json_payload_recovers_from_leading_and_trailing_prose(self) -> None:
        payload = executor.extract_json_payload('Here is the result:\n{"answer":"yes","confidence":0.8}\nThanks.')
        self.assertEqual(payload['answer'], 'yes')

    def test_retry_prompt_adds_strict_json_footer(self) -> None:
        prompt = executor.retry_prompt('original prompt')
        self.assertIn('IMPORTANT RETRY INSTRUCTION', prompt)
        self.assertIn('Return exactly one valid JSON object', prompt)

    def test_collect_recent_synthesis_parse_failures_finds_retry_events(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            status_path = root / 'case-20260413-deadbeef' / 'researcher-analyses' / '2026-04-13' / 'dispatch-case-20260413-deadbeef-20260413T150000Z' / 'synthesis-stage-status.json'
            status_path.parent.mkdir(parents=True, exist_ok=True)
            now = datetime.now(timezone.utc)
            status_path.write_text('{"stage_events":[{"at":"%s","state":"final_synthesis_parse_failed_retrying","error":"bad json"}]}' % now.isoformat().replace('+00:00', 'Z'))
            results = health.collect_recent_synthesis_parse_failures(root, now=now, lookback_hours=24.0)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['case_key'], 'case-20260413-deadbeef')


if __name__ == '__main__':
    unittest.main()
