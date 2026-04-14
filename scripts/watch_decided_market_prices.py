#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fcntl
import json
import os
import random
import subprocess
import sys
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV_FILE = REPO_ROOT / '.env.postgres.local'
DEFAULT_LOCK_FILE = REPO_ROOT / 'scripts' / '.runtime-state' / 'decided-market-watcher.lock'
DEFAULT_REPORT_FILE = REPO_ROOT / 'scripts' / '.runtime-state' / 'decided-market-watcher-heartbeat.json'
DEFAULT_PSQL = '/opt/homebrew/opt/postgresql@16/bin/psql'
GAMMA_MARKETS_URL = 'https://gamma-api.polymarket.com/markets'
DEFAULT_PRICE_DELTA = 0.05
DEFAULT_BATCH_SIZE = 50
DEFAULT_GAMMA_TIMEOUT_SECONDS = 30.0
DEFAULT_GAMMA_MAX_ATTEMPTS = 3
DEFAULT_GAMMA_BACKOFF_SECONDS = 1.0
DEFAULT_DECIDED_MARKET_WATCHER_FAILURE_BUDGET = 2

TRACKED_MARKETS_SQL = r'''
WITH tracked AS (
  SELECT
    m.id::text AS market_id,
    m.external_market_id AS condition_id,
    m.slug,
    m.title,
    m.status AS market_status,
    m.pipeline_status::text AS pipeline_status,
    m.current_price,
    m.last_reasoned_price,
    m.closes_at,
    m.resolves_at,
    lfd.forecast_id,
    lfd.decision_ts,
    lfd.case_id AS case_key,
    lfd.contract_id,
    lfd.market_slug,
    lfd.question,
    lfd.decision_status
  FROM public.latest_forecast_decisions lfd
  JOIN public.markets m
    ON m.id::text = lfd.market_id
  LEFT JOIN public.market_resolutions mr
    ON mr.market_id = lfd.market_id
   AND mr.contract_id = lfd.contract_id
   AND mr.resolution_status = 'resolved'
  WHERE m.platform = 'polymarket'
    AND m.status = 'open'
    AND m.pipeline_status IN ('ignored', 'executed', 'closed')
    AND m.last_reasoned_price IS NOT NULL
    AND COALESCE(m.external_market_id, '') <> ''
    AND COALESCE(lfd.decision_status, '') = 'recorded'
    AND mr.market_id IS NULL
)
SELECT COALESCE(json_agg(row_to_json(tracked) ORDER BY decision_ts DESC), '[]'::json)::text
FROM tracked;
'''

UPSERT_SNAPSHOTS_SQL = r'''
WITH incoming AS (
  SELECT
    (item->>'market_id')::uuid AS market_id,
    NULLIF(item->>'observed_at', '')::timestamptz AS observed_at,
    NULLIF(item->>'last_price', '')::numeric AS last_price,
    NULLIF(item->>'best_bid', '')::numeric AS best_bid,
    NULLIF(item->>'best_ask', '')::numeric AS best_ask,
    NULLIF(item->>'yes_price', '')::numeric AS yes_price,
    NULLIF(item->>'no_price', '')::numeric AS no_price,
    NULLIF(item->>'volume', '')::numeric AS volume,
    NULLIF(item->>'open_interest', '')::numeric AS open_interest,
    COALESCE(item->'raw_payload', '{}'::jsonb) AS raw_payload
  FROM jsonb_array_elements(:'payload'::jsonb) AS item
), updated_markets AS (
  UPDATE public.markets m
  SET current_price = i.yes_price,
      updated_at = NOW(),
      pipeline_status = CASE
        WHEN (
          (m.closes_at IS NOT NULL AND m.closes_at <= NOW())
          OR (m.resolves_at IS NOT NULL AND m.resolves_at <= NOW())
        )
        AND m.pipeline_status IN ('new', 'pending_research')
        THEN 'closed'::processing_status
        WHEN (
          (m.closes_at IS NOT NULL AND m.closes_at <= NOW())
          OR (m.resolves_at IS NOT NULL AND m.resolves_at <= NOW())
        )
        AND m.pipeline_status = 'researching'
        AND NOT EXISTS (
          SELECT 1
          FROM public.cases c
          WHERE c.market_id = m.id
            AND c.status = 'open'
        )
        THEN 'closed'::processing_status
        WHEN m.pipeline_status IN ('ignored', 'executed', 'closed')
             AND ABS(COALESCE(m.last_reasoned_price, 0) - i.yes_price) >= :'min_price_delta'::numeric
        THEN 'pending_research'::processing_status
        ELSE m.pipeline_status
      END
  FROM incoming i
  WHERE m.id = i.market_id
  RETURNING m.id::text AS market_id, m.pipeline_status::text AS new_pipeline_status, m.current_price
), inserted_snapshots AS (
  INSERT INTO public.market_snapshots (
    market_id,
    observed_at,
    last_price,
    best_bid,
    best_ask,
    yes_price,
    no_price,
    volume,
    open_interest,
    raw_payload
  )
  SELECT
    i.market_id,
    COALESCE(i.observed_at, NOW()),
    i.last_price,
    i.best_bid,
    i.best_ask,
    i.yes_price,
    i.no_price,
    i.volume,
    i.open_interest,
    i.raw_payload
  FROM incoming i
  RETURNING market_id::text AS market_id
)
SELECT json_build_object(
  'updated_market_count', (SELECT COUNT(*) FROM updated_markets),
  'pending_research_count', (SELECT COUNT(*) FROM updated_markets WHERE new_pipeline_status = 'pending_research'),
  'snapshot_count', (SELECT COUNT(*) FROM inserted_snapshots),
  'pending_research_market_ids', COALESCE((SELECT json_agg(market_id ORDER BY market_id) FROM updated_markets WHERE new_pipeline_status = 'pending_research'), '[]'::json)
)::text;
'''


class WatcherError(RuntimeError):
    def __init__(self, message: str, *, http_status: int | None = None, retryable: bool = False, benign: bool = False) -> None:
        super().__init__(message)
        self.http_status = http_status
        self.retryable = retryable
        self.benign = benign


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Watch already-decided open markets for material price changes and reopen them for refresh review')
    parser.add_argument('--env-file', default=str(DEFAULT_ENV_FILE))
    parser.add_argument('--db-url', default=os.getenv('PREDQUANT_ADMIN_URL', ''))
    parser.add_argument('--psql', default=os.getenv('PSQL_BIN', DEFAULT_PSQL))
    parser.add_argument('--lock-file', default=str(DEFAULT_LOCK_FILE))
    parser.add_argument('--report-file', default=str(DEFAULT_REPORT_FILE))
    parser.add_argument('--min-price-delta', type=float, default=DEFAULT_PRICE_DELTA)
    parser.add_argument('--batch-size', type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument('--gamma-timeout-seconds', type=float, default=DEFAULT_GAMMA_TIMEOUT_SECONDS)
    parser.add_argument('--gamma-max-attempts', type=int, default=DEFAULT_GAMMA_MAX_ATTEMPTS)
    parser.add_argument('--gamma-backoff-seconds', type=float, default=DEFAULT_GAMMA_BACKOFF_SECONDS)
    parser.add_argument('--apply', action='store_true', help='Persist watched prices/snapshots and reopen materially moved markets')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def load_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    env: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        if line.startswith('export '):
            line = line[len('export '):].strip()
        key, value = line.split('=', 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


@contextmanager
def process_lock(path: Path) -> Iterator[None]:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+', encoding='utf-8') as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise WatcherError(f'decided-market watcher already running (lock: {path})', benign=True) from exc
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def run_psql(psql_bin: str, db_url: str, sql: str, variables: dict[str, str] | None = None) -> dict[str, Any]:
    cmd = [psql_bin, db_url, '-X', '-qAt', '-v', 'ON_ERROR_STOP=1']
    for key, value in (variables or {}).items():
        cmd.extend(['-v', f'{key}={value}'])
    proc = subprocess.run(cmd + ['-f', '-'], input=sql, text=True, capture_output=True, check=False)
    if proc.returncode != 0:
        raise WatcherError(proc.stderr.strip() or proc.stdout.strip() or 'psql failed')
    stdout = proc.stdout.strip()
    if not stdout:
        return {}
    return json.loads(stdout.splitlines()[-1])


def resolve_db_url(args: argparse.Namespace) -> str:
    direct = str(args.db_url or '').strip()
    if direct:
        return direct
    env = load_env_file(Path(args.env_file).expanduser().resolve())
    return str(env.get('PREDQUANT_ADMIN_URL') or env.get('PREDQUANT_ORCHESTRATOR_URL') or '').strip()


def fetch_tracked_markets(*, psql_bin: str, db_url: str) -> list[dict[str, Any]]:
    payload = run_psql(psql_bin, db_url, TRACKED_MARKETS_SQL)
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and 'items' in payload and isinstance(payload['items'], list):
        return payload['items']
    return payload if isinstance(payload, list) else []


def chunked(items: list[Any], size: int) -> Iterator[list[Any]]:
    for i in range(0, len(items), max(1, size)):
        yield items[i:i + max(1, size)]


def gamma_request_headers() -> dict[str, str]:
    return {
        'User-Agent': 'Mozilla/5.0 (compatible; OpenClaw decided-market watcher)',
        'Accept': 'application/json',
    }


def should_retry_http_status(status: int | None) -> bool:
    return status in {403, 408, 409, 425, 429, 500, 502, 503, 504}


def fetch_gamma_market_batch(
    condition_ids: list[str],
    *,
    timeout_seconds: float,
    max_attempts: int,
    backoff_seconds: float,
) -> list[dict[str, Any]]:
    params: list[tuple[str, str]] = [('closed', 'false'), ('limit', str(max(len(condition_ids), 1)))]
    for cid in condition_ids:
        params.append(('condition_ids', cid))
    url = f"{GAMMA_MARKETS_URL}?{urlencode(params, doseq=True)}"
    last_error: WatcherError | None = None
    attempts = max(1, int(max_attempts))
    for attempt in range(1, attempts + 1):
        request = Request(url, headers=gamma_request_headers())
        try:
            with urlopen(request, timeout=max(1.0, float(timeout_seconds))) as response:  # noqa: S310
                status = getattr(response, 'status', 200)
                if status >= 400:
                    raise WatcherError(f'Gamma request failed with HTTP {status}', http_status=status, retryable=should_retry_http_status(status))
                payload = json.loads(response.read().decode('utf-8'))
                return payload if isinstance(payload, list) else []
        except HTTPError as exc:
            body = ''
            try:
                body = exc.read().decode('utf-8', 'replace')
            except Exception:
                body = ''
            detail = f'Gamma request failed with HTTP {exc.code}'
            if body.strip():
                detail += f': {body.strip()[:300]}'
            last_error = WatcherError(detail, http_status=int(exc.code), retryable=should_retry_http_status(int(exc.code)))
        except URLError as exc:
            last_error = WatcherError(f'Gamma request failed: {exc.reason}', retryable=True)
        except TimeoutError as exc:
            last_error = WatcherError(f'Gamma request timed out: {exc}', retryable=True)
        except json.JSONDecodeError as exc:
            raise WatcherError(f'Gamma response was not valid JSON: {exc}') from exc
        if not last_error or not last_error.retryable or attempt >= attempts:
            break
        sleep_seconds = max(0.0, float(backoff_seconds)) * (2 ** (attempt - 1)) + random.uniform(0.0, 0.25)
        if sleep_seconds > 0.0:
            time.sleep(sleep_seconds)
    raise last_error or WatcherError('Gamma request failed')


def fetch_gamma_markets(
    condition_ids: list[str],
    *,
    timeout_seconds: float,
    max_attempts: int,
    backoff_seconds: float,
) -> list[dict[str, Any]]:
    if not condition_ids:
        return []
    try:
        return fetch_gamma_market_batch(
            condition_ids,
            timeout_seconds=timeout_seconds,
            max_attempts=max_attempts,
            backoff_seconds=backoff_seconds,
        )
    except WatcherError as exc:
        if len(condition_ids) <= 1 or exc.http_status not in {403, 414}:
            raise
        midpoint = max(1, len(condition_ids) // 2)
        left = fetch_gamma_markets(
            condition_ids[:midpoint],
            timeout_seconds=timeout_seconds,
            max_attempts=max_attempts,
            backoff_seconds=backoff_seconds,
        )
        right = fetch_gamma_markets(
            condition_ids[midpoint:],
            timeout_seconds=timeout_seconds,
            max_attempts=max_attempts,
            backoff_seconds=backoff_seconds,
        )
        return [*left, *right]


def coerce_float(value: Any) -> float | None:
    if value in (None, ''):
        return None
    try:
        return float(value)
    except Exception:
        return None


def parse_outcome_price(market: dict[str, Any], *, contract_id: str) -> float | None:
    outcomes_raw = market.get('outcomes', '[]')
    prices_raw = market.get('outcomePrices', '[]')
    try:
        outcomes = json.loads(outcomes_raw) if isinstance(outcomes_raw, str) else outcomes_raw
        prices = json.loads(prices_raw) if isinstance(prices_raw, str) else prices_raw
        if not isinstance(outcomes, list) or not isinstance(prices, list):
            return None
    except Exception:
        return None
    target = 'yes' if str(contract_id or '').strip().lower() in {'', 'yes'} else str(contract_id).strip().lower()
    if target == 'yes':
        for idx, outcome in enumerate(outcomes):
            if str(outcome).strip().lower() == 'yes':
                return coerce_float(prices[idx]) if idx < len(prices) else None
    if target == 'no':
        for idx, outcome in enumerate(outcomes):
            if str(outcome).strip().lower() == 'no':
                return coerce_float(prices[idx]) if idx < len(prices) else None
    return None


def snapshot_from_market(raw: dict[str, Any], tracked: dict[str, Any]) -> dict[str, Any] | None:
    yes_price = parse_outcome_price(raw, contract_id=str(tracked.get('contract_id') or 'yes'))
    if yes_price is None:
        return None
    observed_at = utc_now_iso()
    liquidity = coerce_float(raw.get('liquidity'))
    volume = coerce_float(raw.get('volume'))
    best_bid = coerce_float(raw.get('bestBid'))
    best_ask = coerce_float(raw.get('bestAsk'))
    return {
        'market_id': str(tracked.get('market_id') or ''),
        'condition_id': str(tracked.get('condition_id') or ''),
        'observed_at': observed_at,
        'last_price': yes_price,
        'best_bid': best_bid,
        'best_ask': best_ask,
        'yes_price': yes_price,
        'no_price': round(1.0 - yes_price, 6),
        'volume': volume,
        'open_interest': liquidity,
        'raw_payload': {
            'source': 'decided-market-watcher',
            'market': raw,
            'tracked_case_key': tracked.get('case_key'),
            'tracked_forecast_id': tracked.get('forecast_id'),
        },
    }


def persist_snapshots(*, psql_bin: str, db_url: str, snapshots: list[dict[str, Any]], min_price_delta: float) -> dict[str, Any]:
    if not snapshots:
        return {'updated_market_count': 0, 'pending_research_count': 0, 'snapshot_count': 0, 'pending_research_market_ids': []}
    return run_psql(
        psql_bin,
        db_url,
        UPSERT_SNAPSHOTS_SQL,
        variables={
            'payload': json.dumps(snapshots),
            'min_price_delta': f'{float(min_price_delta):.6f}',
        },
    )


def load_existing_report(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def merge_report_history(report: dict[str, Any], previous: dict[str, Any]) -> dict[str, Any]:
    previous_success = str(previous.get('last_success_at') or previous.get('completed_at') or '').strip() if isinstance(previous, dict) else ''
    previous_failures = int(previous.get('consecutive_failures') or 0) if isinstance(previous, dict) else 0
    previous_failure_at = str(previous.get('last_failure_at') or '').strip() if isinstance(previous, dict) else ''
    previous_failure_streak_started_at = str(previous.get('failure_streak_started_at') or '').strip() if isinstance(previous, dict) else ''
    if report.get('noop'):
        report['last_success_at'] = previous_success
        report['last_failure_at'] = previous_failure_at
        report['consecutive_failures'] = previous_failures
        report['failure_streak_started_at'] = previous_failure_streak_started_at
    elif report.get('ok'):
        report['last_success_at'] = str(report.get('completed_at') or '')
        report['last_failure_at'] = ''
        report['consecutive_failures'] = 0
        report['failure_streak_started_at'] = ''
    else:
        report['last_success_at'] = previous_success
        report['last_failure_at'] = str(report.get('completed_at') or '')
        report['consecutive_failures'] = previous_failures + 1
        if previous_failures > 0 and previous_failure_streak_started_at:
            report['failure_streak_started_at'] = previous_failure_streak_started_at
        else:
            report['failure_streak_started_at'] = str(report.get('started_at') or report.get('completed_at') or '')
    return report


def write_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')


def main() -> int:
    args = parse_args()
    db_url = resolve_db_url(args)
    if not db_url:
        raise SystemExit('No Postgres URL available via --db-url or .env.postgres.local')

    started_at = utc_now_iso()
    started_monotonic = time.monotonic()
    lock_file = Path(args.lock_file).expanduser().resolve()
    report_file = Path(args.report_file).expanduser().resolve()
    previous_report = load_existing_report(report_file)
    report: dict[str, Any] = {
        'artifact_type': 'decided_market_watcher_heartbeat',
        'schema_version': 'decided-market-watcher/v1',
        'ok': False,
        'started_at': started_at,
        'completed_at': '',
        'duration_seconds': None,
        'apply': bool(args.apply),
        'min_price_delta': float(args.min_price_delta),
        'batch_size': int(args.batch_size),
        'gamma_markets_url': GAMMA_MARKETS_URL,
        'gamma_timeout_seconds': float(args.gamma_timeout_seconds),
        'gamma_max_attempts': int(args.gamma_max_attempts),
        'gamma_backoff_seconds': float(args.gamma_backoff_seconds),
        'tracked_market_count': 0,
        'fetched_market_count': 0,
        'snapshot_count': 0,
        'pending_research_count': 0,
        'reopened_markets': [],
        'missing_condition_ids': [],
        'market_samples': [],
        'last_success_at': str(previous_report.get('last_success_at') or previous_report.get('completed_at') or ''),
        'last_failure_at': str(previous_report.get('last_failure_at') or ''),
        'consecutive_failures': int(previous_report.get('consecutive_failures') or 0),
        'failure_streak_started_at': str(previous_report.get('failure_streak_started_at') or ''),
    }

    try:
        with process_lock(lock_file):
            tracked = fetch_tracked_markets(psql_bin=str(args.psql), db_url=db_url)
            report['tracked_market_count'] = len(tracked)
            if not tracked:
                report['ok'] = True
            else:
                by_condition = {str(item.get('condition_id') or ''): item for item in tracked if str(item.get('condition_id') or '').strip()}
                fetched: list[dict[str, Any]] = []
                for batch in chunked(list(by_condition.keys()), int(args.batch_size)):
                    fetched.extend(fetch_gamma_markets(
                        batch,
                        timeout_seconds=float(args.gamma_timeout_seconds),
                        max_attempts=int(args.gamma_max_attempts),
                        backoff_seconds=float(args.gamma_backoff_seconds),
                    ))
                report['fetched_market_count'] = len(fetched)
                fetched_by_condition = {str(item.get('conditionId') or ''): item for item in fetched if str(item.get('conditionId') or '').strip()}
                report['missing_condition_ids'] = sorted([cid for cid in by_condition if cid not in fetched_by_condition])
                snapshots: list[dict[str, Any]] = []
                samples: list[dict[str, Any]] = []
                for cid, tracked_item in by_condition.items():
                    raw = fetched_by_condition.get(cid)
                    if raw is None:
                        continue
                    snapshot = snapshot_from_market(raw, tracked_item)
                    if snapshot is None:
                        continue
                    snapshots.append(snapshot)
                    last_reasoned = coerce_float(tracked_item.get('last_reasoned_price'))
                    delta = abs((last_reasoned or 0.0) - float(snapshot['yes_price'])) if last_reasoned is not None else None
                    samples.append({
                        'market_id': tracked_item.get('market_id'),
                        'condition_id': cid,
                        'case_key': tracked_item.get('case_key'),
                        'title': tracked_item.get('title'),
                        'pipeline_status': tracked_item.get('pipeline_status'),
                        'last_reasoned_price': last_reasoned,
                        'watched_price': snapshot['yes_price'],
                        'price_delta': round(delta, 6) if delta is not None else None,
                    })
                report['market_samples'] = samples[:10]
                if args.apply:
                    persist_result = persist_snapshots(
                        psql_bin=str(args.psql),
                        db_url=db_url,
                        snapshots=snapshots,
                        min_price_delta=float(args.min_price_delta),
                    )
                else:
                    pending = [s for s in samples if s.get('price_delta') is not None and float(s['price_delta']) >= float(args.min_price_delta)]
                    persist_result = {
                        'updated_market_count': len(snapshots),
                        'snapshot_count': len(snapshots),
                        'pending_research_count': len(pending),
                        'pending_research_market_ids': [item['market_id'] for item in pending],
                    }
                report['snapshot_count'] = int(persist_result.get('snapshot_count') or 0)
                report['pending_research_count'] = int(persist_result.get('pending_research_count') or 0)
                report['reopened_markets'] = persist_result.get('pending_research_market_ids') or []
                report['persist_result'] = persist_result
                report['ok'] = True
    except Exception as exc:  # noqa: BLE001
        report['error'] = str(exc)
        if isinstance(exc, WatcherError):
            if exc.http_status is not None:
                report['http_status'] = int(exc.http_status)
            if exc.benign:
                report['noop'] = True
                report['ok'] = True
                report['reason'] = 'already_running'
    finally:
        report['completed_at'] = utc_now_iso()
        report['duration_seconds'] = round(time.monotonic() - started_monotonic, 3)
        merge_report_history(report, previous_report)
        write_report(report_file, report)

    print(json.dumps(report, indent=2 if args.pretty else None))
    return 0 if report.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
