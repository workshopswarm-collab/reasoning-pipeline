from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

TEST_DIR = Path(__file__).resolve().parent
REPO_ROOT = TEST_DIR.parents[1]
RUNTIME_ROOT = REPO_ROOT / 'roles' / 'evaluator' / 'runtime'
RUNTIME_SCRIPTS_DIR = RUNTIME_ROOT / 'scripts'

for candidate in [RUNTIME_ROOT, RUNTIME_SCRIPTS_DIR]:
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


trigger = load_module(
    'trigger_post_treatment_feedback_cycle_for_tests',
    RUNTIME_SCRIPTS_DIR / 'trigger_post_treatment_feedback_cycle.py',
)


class TriggerPostTreatmentFeedbackCycleTests(unittest.TestCase):
    def make_report(self, path: Path, *, generated_at: str, case_key: str, dispatch_id: str) -> None:
        payload = {
            'summary': {'generated_at': generated_at},
            'audits': [
                {
                    'case_key': case_key,
                    'dispatch_id': dispatch_id,
                }
            ],
        }
        path.write_text(json.dumps(payload), encoding='utf-8')

    def test_relevant_state_accepts_scalar_exec_sql_counts(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / 'post-treatment-feedback-cycle.json'
            with (
                patch.object(trigger, 'POST_TREATMENT_REPORT_JSON', report_path),
                patch.object(trigger, 'resolve_db_url', return_value='postgres://db'),
                patch.object(trigger, 'table_exists', side_effect=[True, True, True]),
                patch.object(
                    trigger,
                    'exec_sql',
                    side_effect=[
                        3,
                        2,
                        1,
                        '2026-04-16 10:43:06-04',
                        '2026-04-16 10:57:29-04',
                        '2026-04-16 11:05:00-04',
                    ],
                ),
            ):
                state = trigger.relevant_state(
                    db_url='postgres://db',
                    psql_bin='psql',
                    case_key='case-20260416-8bef05aa',
                    dispatch_id='dispatch-case-20260416-8bef05aa-20260416T144205Z',
                )
        self.assertEqual(state['lmd_exposure_rows'], 3)
        self.assertEqual(state['trial_exposure_rows'], 2)
        self.assertEqual(state['resolved_reviews'], 1)
        self.assertTrue(state['should_run'])
        self.assertFalse(state['report_fresh'])

    def test_relevant_state_skips_when_existing_report_is_fresh(self) -> None:
        case_key = 'case-20260416-8bef05aa'
        dispatch_id = 'dispatch-case-20260416-8bef05aa-20260416T144205Z'
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / 'post-treatment-feedback-cycle.json'
            self.make_report(
                report_path,
                generated_at='2026-04-16T15:15:00+00:00',
                case_key=case_key,
                dispatch_id=dispatch_id,
            )
            with (
                patch.object(trigger, 'POST_TREATMENT_REPORT_JSON', report_path),
                patch.object(trigger, 'resolve_db_url', return_value='postgres://db'),
                patch.object(trigger, 'table_exists', side_effect=[True, True, True]),
                patch.object(
                    trigger,
                    'exec_sql',
                    side_effect=[
                        3,
                        2,
                        1,
                        '2026-04-16 10:43:06-04',
                        '2026-04-16 10:57:29-04',
                        '2026-04-16 11:05:00-04',
                    ],
                ),
            ):
                state = trigger.relevant_state(
                    db_url='postgres://db',
                    psql_bin='psql',
                    case_key=case_key,
                    dispatch_id=dispatch_id,
                )
        self.assertFalse(state['should_run'])
        self.assertTrue(state['report_fresh'])
        self.assertEqual(state['skip_reason'], 'report_already_fresh')

    def test_relevant_state_force_refresh_overrides_fresh_report(self) -> None:
        case_key = 'case-20260416-8bef05aa'
        dispatch_id = 'dispatch-case-20260416-8bef05aa-20260416T144205Z'
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / 'post-treatment-feedback-cycle.json'
            self.make_report(
                report_path,
                generated_at='2026-04-16T15:15:00+00:00',
                case_key=case_key,
                dispatch_id=dispatch_id,
            )
            with (
                patch.object(trigger, 'POST_TREATMENT_REPORT_JSON', report_path),
                patch.object(trigger, 'resolve_db_url', return_value='postgres://db'),
                patch.object(trigger, 'table_exists', side_effect=[True, True, True]),
                patch.object(
                    trigger,
                    'exec_sql',
                    side_effect=[
                        3,
                        2,
                        1,
                        '2026-04-16 10:43:06-04',
                        '2026-04-16 10:57:29-04',
                        '2026-04-16 11:05:00-04',
                    ],
                ),
            ):
                state = trigger.relevant_state(
                    db_url='postgres://db',
                    psql_bin='psql',
                    case_key=case_key,
                    dispatch_id=dispatch_id,
                    force_refresh=True,
                )
        self.assertTrue(state['should_run'])
        self.assertTrue(state['force_refresh'])
        self.assertTrue(state['report_fresh'])


if __name__ == '__main__':
    unittest.main()
