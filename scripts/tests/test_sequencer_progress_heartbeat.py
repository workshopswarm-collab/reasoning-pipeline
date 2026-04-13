from __future__ import annotations

import unittest
from types import SimpleNamespace
from unittest.mock import patch

import scripts.pipeline_sequencer_progress as progress


class SequencerProgressHeartbeatTests(unittest.TestCase):
    def test_wait_for_case_emits_progress_updates_while_monitoring(self) -> None:
        in_progress_summary = {
            'case_key': 'case-test',
            'path': 'qualitative-db/40-research/cases/case-test/pipeline-status.json',
            'status': 'pipeline_in_progress',
            'current_stage': 'decision',
            'stage_statuses': {
                'dispatch': 'launched',
                'swarm': 'completed',
                'synthesis': 'completed',
                'decision': 'pending',
            },
            'dispatch_id': 'dispatch-test',
            'market_id': 'market-test',
        }
        completed_summary = {
            **in_progress_summary,
            'status': 'pipeline_completed',
            'stage_statuses': {
                **in_progress_summary['stage_statuses'],
                'decision': 'completed',
            },
        }
        watchdog_result = {
            'ok': True,
            'proposed_actions': ['launch_decision_for_existing_case'],
            'executed_actions': [{'name': 'launch_decision_for_existing_case'}],
            'after': completed_summary,
        }
        events: list[dict[str, object]] = []

        with patch.object(progress, 'summarize_case_pipeline_status', return_value=in_progress_summary), patch.object(
            progress,
            'watch_existing_case',
            return_value=watchdog_result,
        ):
            result = progress.wait_for_case(
                'case-test',
                args=SimpleNamespace(control_managed=False),
                poll_seconds=0.0,
                max_case_seconds=5.0,
                pretty=False,
                progress_callback=lambda **kwargs: events.append(kwargs),
            )

        self.assertTrue(result['ok'])
        self.assertEqual([event['phase'] for event in events], ['monitor_case', 'watchdog_reconcile'])
        self.assertEqual(events[0]['case_key'], 'case-test')
        self.assertEqual(events[1]['details']['executed_actions'], ['launch_decision_for_existing_case'])

    def test_wait_for_case_fails_fast_when_watchdog_action_fails(self) -> None:
        in_progress_summary = {
            'case_key': 'case-test',
            'path': 'qualitative-db/40-research/cases/case-test/pipeline-status.json',
            'status': 'pipeline_in_progress',
            'current_stage': 'decision',
            'stage_statuses': {
                'dispatch': 'launched',
                'swarm': 'completed',
                'synthesis': 'completed',
                'decision': 'pending',
            },
            'dispatch_id': 'dispatch-test',
            'market_id': 'market-test',
        }
        watchdog_result = {
            'ok': True,
            'proposed_actions': ['launch_decision_for_existing_case'],
            'executed_actions': [{'name': 'launch_decision_for_existing_case'}],
            'action_failures': [{'name': 'launch_decision_for_existing_case', 'result': {'ok': False, 'returncode': 1}}],
            'after': in_progress_summary,
        }

        with patch.object(progress, 'summarize_case_pipeline_status', return_value=in_progress_summary), patch.object(
            progress,
            'watch_existing_case',
            return_value=watchdog_result,
        ):
            result = progress.wait_for_case(
                'case-test',
                args=SimpleNamespace(control_managed=False),
                poll_seconds=0.0,
                max_case_seconds=5.0,
                pretty=False,
            )

        self.assertFalse(result['ok'])
        self.assertEqual(result['error'], 'watchdog_action_failed')
        self.assertEqual(result['watchdog_result']['action_failures'][0]['name'], 'launch_decision_for_existing_case')


if __name__ == '__main__':
    unittest.main()
