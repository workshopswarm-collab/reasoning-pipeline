from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import types
import unittest
from unittest import mock
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError

TEST_DIR = Path(__file__).resolve().parent
REPO_ROOT = TEST_DIR.parents[1]
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


case_pipeline_status = load_module('case_pipeline_status_for_hardening_tests', SCRIPTS_DIR / 'case_pipeline_status.py')
watch_decided_market_prices = load_module('watch_decided_market_prices_for_hardening_tests', SCRIPTS_DIR / 'watch_decided_market_prices.py')
check_pipeline_health = load_module('check_pipeline_health_for_hardening_tests', SCRIPTS_DIR / 'check_pipeline_health.py')
pipeline_sequencer_runner = load_module('pipeline_sequencer_runner_for_hardening_tests', SCRIPTS_DIR / 'pipeline_sequencer_runner.py')
manual_batch_controller = load_module('manual_batch_controller_for_hardening_tests', RUNTIME_SCRIPTS_DIR / 'manual_batch_controller.py')


class FakeResponse:
    def __init__(self, payload: object, *, status: int = 200) -> None:
        self.payload = payload
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self) -> bytes:
        return json.dumps(self.payload).encode('utf-8')


class PipelineHardeningRegressionTests(unittest.TestCase):
    def test_first_blocking_case_ignores_quarantined_pipeline_failed_and_skipped(self) -> None:
        with mock.patch.object(
            case_pipeline_status,
            'list_case_pipeline_statuses',
            return_value=[
                {'case_key': 'case-1', 'status': 'pipeline_failed', 'terminal_summary': {'quarantined': True}},
                {'case_key': 'case-2', 'status': 'pipeline_skipped', 'terminal_summary': {}},
                {'case_key': 'case-3', 'status': 'pipeline_completed', 'terminal_summary': {'decision_packet_markdown': 'done'}},
            ],
        ):
            self.assertEqual(case_pipeline_status.first_blocking_case_without_completed_decision_packet(), {})

    def test_fetch_gamma_markets_retries_retryable_403_and_sets_limit(self) -> None:
        requests: list[str] = []

        def fake_urlopen(request, timeout=0):
            requests.append(request.full_url)
            if len(requests) == 1:
                raise HTTPError(request.full_url, 403, 'Forbidden', hdrs=None, fp=None)
            return FakeResponse([
                {'conditionId': 'cond-1', 'outcomes': '["Yes","No"]', 'outcomePrices': '["0.61","0.39"]'}
            ])

        with mock.patch.object(watch_decided_market_prices, 'urlopen', side_effect=fake_urlopen), \
             mock.patch.object(watch_decided_market_prices.time, 'sleep'), \
             mock.patch.object(watch_decided_market_prices.random, 'uniform', return_value=0.0):
            payload = watch_decided_market_prices.fetch_gamma_markets(
                ['cond-1', 'cond-2'],
                timeout_seconds=1.0,
                max_attempts=2,
                backoff_seconds=0.01,
            )

        self.assertEqual(len(payload), 1)
        self.assertEqual(len(requests), 2)
        self.assertIn('limit=2', requests[0])
        self.assertIn('condition_ids=cond-1', requests[0])
        self.assertIn('condition_ids=cond-2', requests[0])

    def test_watcher_noop_preserves_failure_history(self) -> None:
        report = {'ok': True, 'noop': True}
        previous = {
            'last_success_at': '2026-04-14T14:00:43Z',
            'last_failure_at': '2026-04-14T14:01:13Z',
            'consecutive_failures': 4,
            'failure_streak_started_at': '2026-04-14T14:01:13Z',
        }
        merged = watch_decided_market_prices.merge_report_history(report, previous)
        self.assertEqual(merged['last_success_at'], '2026-04-14T14:00:43Z')
        self.assertEqual(merged['consecutive_failures'], 4)
        self.assertEqual(merged['last_failure_at'], '2026-04-14T14:01:13Z')

    def test_healthcheck_warns_on_single_recent_watcher_failure(self) -> None:
        now = datetime.now(timezone.utc)
        heartbeat_payload = {'state': 'sleeping', 'loop_mode': True, 'last_loop_completed_at': now.isoformat().replace('+00:00', 'Z')}
        watcher_payload = {
            'ok': False,
            'tracked_market_count': 8,
            'completed_at': now.isoformat().replace('+00:00', 'Z'),
            'last_success_at': (now - timedelta(seconds=30)).isoformat().replace('+00:00', 'Z'),
            'consecutive_failures': 1,
            'error': 'HTTP Error 403: Forbidden',
        }
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
            skip_artifact_contract_check=True,
            decided_market_watcher_heartbeat_file='scripts/.runtime-state/decided-market-watcher-heartbeat.json',
            max_decided_market_watcher_age_seconds=120.0,
            max_decided_market_watcher_consecutive_failures=2,
            skip_decided_market_watcher_check=False,
            market_checker_env_file='.env.postgres.local',
            market_checker_db_url='',
            market_checker_psql='/opt/homebrew/opt/postgresql@16/bin/psql',
            max_market_snapshot_age_seconds=3600.0,
            skip_market_checker_check=True,
            synthesis_parse_failure_lookback_hours=24.0,
            max_synthesis_parse_failures=2,
            pretty=False,
        )

        def fake_load_json(path: Path):
            name = Path(path).name
            if name == 'pipeline-heartbeat.json':
                return heartbeat_payload
            if name == 'pipeline-quarantine.json':
                return {'entries': []}
            if name == 'decided-market-watcher-heartbeat.json':
                return watcher_payload
            return {}

        with mock.patch.object(check_pipeline_health, 'load_control_file', return_value={}), \
             mock.patch.object(check_pipeline_health, 'resolve_sequencer_policy', return_value={'enabled': False, 'resume_existing': True, 'allow_new_case_claims': False}), \
             mock.patch.object(check_pipeline_health, 'load_json_file', side_effect=fake_load_json), \
             mock.patch.object(check_pipeline_health, 'write_json_file'):
            report = check_pipeline_health.evaluate(args)

        issue_codes = {issue['code'] for issue in report['issues']}
        self.assertEqual(report['status'], 'warn')
        self.assertIn('decided_market_watcher_recent_failure', issue_codes)
        self.assertNotIn('decided_market_watcher_failed', issue_codes)

    def test_stage_retry_registry_prunes_stale_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            registry_path = Path(tmpdir) / 'stage-launch-retries.json'
            fresh_at = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
            stale_at = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat().replace('+00:00', 'Z')
            registry_path.write_text(json.dumps({
                'schema_version': 'pipeline-stage-retries/v1',
                'entries': {
                    'fresh': {'case_key': 'case-fresh', 'last_seen_at': fresh_at, 'attempts': 1},
                    'stale': {'case_key': 'case-stale', 'last_seen_at': stale_at, 'attempts': 99},
                },
                'updated_at': stale_at,
            }))

            payload = pipeline_sequencer_runner.load_stage_retry_registry(registry_path)

        self.assertIn('fresh', payload['entries'])
        self.assertNotIn('stale', payload['entries'])

    def test_manual_batch_controller_resolves_db_url_from_env_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            env_file = root / '.env.postgres.local'
            env_file.write_text('PREDQUANT_ORCHESTRATOR_URL=postgres://example/db\n')
            repo_env = manual_batch_controller.build_repo_env(root=root, env_file=str(env_file))
            args = types.SimpleNamespace(db_url='', psql='', env_file=str(env_file))

        self.assertEqual(manual_batch_controller.resolve_db_url(args=args, repo_env=repo_env), 'postgres://example/db')


if __name__ == '__main__':
    unittest.main()
