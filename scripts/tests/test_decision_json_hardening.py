from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / 'roles' / 'decision-maker' / 'runtime' / 'scripts' / 'run_decision_maker.py'
DECISION_RUNTIME_SCRIPTS_DIR = MODULE_PATH.parent
DECISION_RUNTIME_DIR = DECISION_RUNTIME_SCRIPTS_DIR.parent
SCRIPTS_DIR = REPO_ROOT / 'scripts'

for candidate in [DECISION_RUNTIME_SCRIPTS_DIR, DECISION_RUNTIME_DIR, SCRIPTS_DIR]:
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


run_decision_maker = load_module('run_decision_maker_for_tests', MODULE_PATH)


class DecisionJsonHardeningTests(unittest.TestCase):
    def test_retry_prompt_includes_error_and_validation_details(self) -> None:
        prompt = run_decision_maker.retry_prompt(
            "Return a decision packet.",
            error="could not parse JSON object from decision-maker response text",
            validation_errors=["missing decision.trade_authorization", "missing audit"],
        )
        self.assertIn("IMPORTANT RETRY INSTRUCTION", prompt)
        self.assertIn("Previous failure", prompt)
        self.assertIn("missing decision.trade_authorization", prompt)
        self.assertIn("Return a decision packet.", prompt)

    def test_attempt_suffix_paths_are_stable(self) -> None:
        path = run_decision_maker.decision_raw_response_text_path('case-test', 'dispatch-test', attempt=2)
        self.assertTrue(str(path).endswith('decision-response-dispatch-test-attempt-2.raw.txt'))

    def test_extract_json_payload_accepts_fenced_json_with_prose(self) -> None:
        text = """
Here is the completed packet.

```json
{"decision": {"decision_readiness": "ready"}, "audit": {"notes": "ok"}}
```

Use the packet above.
"""
        payload = run_decision_maker.extract_json_payload(text)
        self.assertEqual(payload['decision']['decision_readiness'], 'ready')

    def test_extract_json_payload_accepts_prose_wrapped_object(self) -> None:
        text = """Decision packet follows:

{"decision": {"decision_readiness": "ready"}, "audit": {"notes": "ok"}}

Thanks.
"""
        payload = run_decision_maker.extract_json_payload(text)
        self.assertEqual(payload['audit']['notes'], 'ok')

    def test_write_decision_parse_failure_artifact_persists_debug_context(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            prompt_path = tmp / 'prompt.md'
            raw_text_path = tmp / 'response.raw.txt'
            gateway_path = tmp / 'gateway.json'
            artifact_path = tmp / 'decision-parse-failure.json'
            prompt_path.write_text('prompt')
            raw_text_path.write_text('not json')
            gateway_path.write_text('{"status":"accepted"}')

            with patch.object(run_decision_maker, 'decision_parse_failure_artifact_path', return_value=artifact_path):
                written = run_decision_maker.write_decision_parse_failure_artifact(
                    case_key='case-test',
                    dispatch_id='dispatch-test',
                    prompt_path=prompt_path,
                    error='could not parse JSON object from decision-maker response text',
                    raw_text_path=raw_text_path,
                    gateway_response_path=gateway_path,
                    tool_usage={'tool_activity_detected': True, 'tool_names': ['web_search']},
                )

            self.assertEqual(written, artifact_path)
            payload = json.loads(artifact_path.read_text())
            self.assertEqual(payload['artifact_type'], 'decision_parse_failure')
            self.assertEqual(payload['case_key'], 'case-test')
            self.assertEqual(payload['dispatch_id'], 'dispatch-test')
            self.assertEqual(payload['error'], 'could not parse JSON object from decision-maker response text')
            self.assertTrue(payload['raw_text_path'].endswith('response.raw.txt'))
            self.assertTrue(payload['gateway_response_path'].endswith('gateway.json'))
            self.assertEqual(payload['tool_usage']['tool_names'], ['web_search'])


if __name__ == '__main__':
    unittest.main()
