#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
DISPATCH_MANIFESTS_DIR = WORKSPACE_ROOT / "roles" / "orchestrator" / "researchers-swarm-subagents" / "runtime" / "dispatch-manifests"

SELECT_CANDIDATES_SQL = r'''
WITH ranked AS (
  SELECT
    fd.forecast_id,
    fd.dispatch_id,
    fd.market_id,
    fd.contract_id,
    fd.platform,
    fd.market_slug,
    fd.question,
    fd.decision_packet_path,
    fd.decision_ts,
    fd.created_at,
    m.external_market_id AS db_external_market_id,
    m.slug AS db_market_slug,
    m.platform AS db_platform
  FROM public.forecast_decisions fd
  LEFT JOIN public.market_resolutions mr
    ON fd.market_id = mr.market_id
   AND fd.contract_id = mr.contract_id
  LEFT JOIN public.markets m
    ON m.id::text = fd.market_id
  WHERE fd.platform = 'polymarket'
    AND fd.decision_status <> 'void'
    AND (mr.market_id IS NULL OR mr.resolution_status IN ('unresolved', 'disputed', 'error'))
)
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT DISTINCT ON (market_id, contract_id)
    forecast_id,
    dispatch_id,
    market_id,
    contract_id,
    platform,
    market_slug,
    question,
    decision_packet_path,
    decision_ts,
    created_at,
    db_external_market_id,
    db_market_slug,
    db_platform
  FROM ranked
  ORDER BY market_id, contract_id, decision_ts DESC, created_at DESC, forecast_id DESC
) t;
'''

UPDATE_FORECAST_IDENTITY_SQL = r'''
UPDATE public.forecast_decisions
SET market_id = :'canonical_market_id',
    platform = COALESCE(NULLIF(:'platform', ''), platform),
    market_slug = COALESCE(NULLIF(:'market_slug', ''), market_slug),
    updated_at = NOW()
WHERE forecast_id = :'forecast_id'
RETURNING json_build_object(
  'forecast_id', forecast_id,
  'market_id', market_id,
  'platform', platform,
  'market_slug', market_slug
)::text;
'''

UPSERT_RESOLUTION_SQL = r'''
INSERT INTO public.market_resolutions (
  market_id,
  contract_id,
  platform,
  resolution_status,
  resolved_outcome,
  resolved_value,
  resolved_ts,
  resolution_source,
  resolution_notes,
  updated_at
)
VALUES (
  :'market_id',
  :'contract_id',
  :'platform',
  :'resolution_status',
  NULLIF(:'resolved_outcome', ''),
  NULLIF(:'resolved_value', '')::numeric,
  NULLIF(:'resolved_ts', '')::timestamptz,
  NULLIF(:'resolution_source', ''),
  NULLIF(:'resolution_notes', ''),
  NOW()
)
ON CONFLICT (market_id, contract_id)
DO UPDATE SET
  platform = EXCLUDED.platform,
  resolution_status = EXCLUDED.resolution_status,
  resolved_outcome = EXCLUDED.resolved_outcome,
  resolved_value = EXCLUDED.resolved_value,
  resolved_ts = EXCLUDED.resolved_ts,
  resolution_source = EXCLUDED.resolution_source,
  resolution_notes = EXCLUDED.resolution_notes,
  updated_at = NOW()
RETURNING json_build_object(
  'market_id', market_id,
  'contract_id', contract_id,
  'resolution_status', resolution_status,
  'resolved_outcome', resolved_outcome,
  'resolved_value', resolved_value,
  'resolved_ts', resolved_ts,
  'resolution_source', resolution_source
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Automatically sync Polymarket market resolutions into quant-db")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""))
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL))
    parser.add_argument("--limit", type=int, default=0, help="Optional max number of distinct market/contract pairs to process")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and classify markets without writing DB updates")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def exec_sql(psql_bin: str, db_url: str, sql: str, variables: dict[str, str] | None = None) -> Any:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")
    cmd = [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1"]
    for key, value in (variables or {}).items():
        cmd.extend(["-v", f"{key}={value}"])
    cmd.extend(["-f", "-"])
    proc = subprocess.run(cmd, input=sql, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    if not stdout:
        return None
    return json.loads(stdout.splitlines()[-1])


def load_dispatch_manifest_market(dispatch_id: str) -> dict[str, Any]:
    if not dispatch_id:
        return {}
    path = DISPATCH_MANIFESTS_DIR / f"{dispatch_id}.json"
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}
    market = payload.get("market") if isinstance(payload, dict) else {}
    return dict(market) if isinstance(market, dict) else {}


def looks_like_uuid(value: str) -> bool:
    text = (value or "").strip().lower()
    parts = text.split("-")
    return len(parts) == 5 and [len(p) for p in parts] == [8, 4, 4, 4, 12]


def normalize_label(value: Any) -> str:
    text = "" if value is None else str(value).strip().lower()
    if text in {"yes", "no"}:
        return text
    return text


def parse_jsonish_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return []
        try:
            parsed = json.loads(text)
            return parsed if isinstance(parsed, list) else []
        except json.JSONDecodeError:
            return []
    return []


def parse_market_payload(payload: dict[str, Any]) -> dict[str, Any]:
    outcomes = [normalize_label(item) for item in parse_jsonish_list(payload.get("outcomes"))]
    raw_prices = parse_jsonish_list(payload.get("outcomePrices"))
    prices: list[float] = []
    for item in raw_prices:
        try:
            prices.append(float(item))
        except Exception:
            prices.append(float("nan"))

    uma_status = normalize_label(payload.get("umaResolutionStatus"))
    closed = bool(payload.get("closed"))
    archived = bool(payload.get("archived"))
    winner = normalize_label(payload.get("winner"))

    resolved_outcome = ""
    if winner and winner in outcomes:
        resolved_outcome = winner
    elif outcomes and len(outcomes) == len(prices):
        try:
            max_index = max(range(len(prices)), key=lambda idx: prices[idx])
            max_price = prices[max_index]
            min_price = min(prices)
        except Exception:
            max_index = -1
            max_price = float("nan")
            min_price = float("nan")
        if max_index >= 0 and (uma_status == "resolved" or closed) and max_price >= 0.999 and min_price <= 0.001:
            resolved_outcome = outcomes[max_index]

    if uma_status == "resolved" and resolved_outcome:
        resolution_status = "resolved"
    elif archived and not payload.get("active", False) and not resolved_outcome:
        resolution_status = "unresolved"
    elif closed and resolved_outcome:
        resolution_status = "resolved"
    else:
        resolution_status = "unresolved"

    resolved_ts = ""
    for key in ["closedTime", "updatedAt", "endDate"]:
        value = payload.get(key)
        if value:
            resolved_ts = str(value)
            break

    return {
        "resolution_status": resolution_status,
        "resolved_outcome": resolved_outcome,
        "resolved_ts": resolved_ts if resolution_status == "resolved" else "",
        "uma_resolution_status": uma_status,
        "closed": closed,
        "archived": archived,
        "outcomes": outcomes,
        "prices": prices,
    }


def resolved_value_for_contract(contract_id: str, resolved_outcome: str, outcomes: list[str]) -> str:
    contract = normalize_label(contract_id)
    if not resolved_outcome:
        return ""
    if contract == resolved_outcome:
        return "1.00000"
    if contract and contract in outcomes:
        return "0.00000"
    return ""


def fetch_polymarket_market_by_slug(slug: str) -> dict[str, Any]:
    url = f"https://gamma-api.polymarket.com/markets/slug/{slug}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode())


def canonicalize_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    market_id = str(candidate.get("market_id") or "").strip()
    contract_id = str(candidate.get("contract_id") or "").strip() or "yes"
    market_slug = str(candidate.get("market_slug") or "").strip()
    platform = str(candidate.get("platform") or candidate.get("db_platform") or "polymarket").strip() or "polymarket"
    external_market_id = str(candidate.get("db_external_market_id") or "").strip()
    dispatch_id = str(candidate.get("dispatch_id") or "").strip()
    manifest_market = load_dispatch_manifest_market(dispatch_id)

    canonical_market_id = market_id
    if not looks_like_uuid(canonical_market_id):
        manifest_market_id = str(manifest_market.get("market_id") or "").strip()
        if looks_like_uuid(manifest_market_id):
            canonical_market_id = manifest_market_id
    if not market_slug:
        market_slug = str(candidate.get("db_market_slug") or "").strip() or str(manifest_market.get("slug") or "").strip()
    if not external_market_id:
        external_market_id = str(manifest_market.get("external_market_id") or "").strip()
    if platform == "polymarket" and not market_slug:
        market_slug = str(manifest_market.get("slug") or "").strip()
    if not market_slug and external_market_id:
        # no documented direct path by external ID; keep slug-only fetch policy for now
        pass

    return {
        **candidate,
        "contract_id": contract_id,
        "canonical_market_id": canonical_market_id,
        "canonical_market_slug": market_slug,
        "canonical_platform": platform,
        "canonical_external_market_id": external_market_id,
        "manifest_market": manifest_market,
    }


def main() -> int:
    args = parse_args()
    candidates = exec_sql(args.psql, args.db_url, SELECT_CANDIDATES_SQL) or []
    if not isinstance(candidates, list):
        raise ValueError("candidate query returned non-list payload")
    if args.limit and args.limit > 0:
        candidates = candidates[: args.limit]

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    canonicalized: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    identity_updates: list[dict[str, Any]] = []
    resolution_writes: list[dict[str, Any]] = []
    fetch_errors: list[dict[str, Any]] = []

    for candidate in candidates:
        item = canonicalize_candidate(candidate)
        canonicalized.append(item)
        slug = str(item.get("canonical_market_slug") or "").strip()
        canonical_market_id = str(item.get("canonical_market_id") or "").strip()
        if not slug or not canonical_market_id:
            skipped.append({
                "forecast_id": item.get("forecast_id"),
                "dispatch_id": item.get("dispatch_id"),
                "market_id": item.get("market_id"),
                "canonical_market_id": canonical_market_id,
                "market_slug": slug,
                "reason": "missing canonical market identity for Polymarket lookup",
            })
            continue
        grouped[slug].append(item)

    fetched_market_payloads: dict[str, dict[str, Any]] = {}
    fetched_market_summaries: list[dict[str, Any]] = []

    for slug, items in grouped.items():
        try:
            payload = fetch_polymarket_market_by_slug(slug)
            fetched_market_payloads[slug] = payload
            parsed = parse_market_payload(payload)
            fetched_market_summaries.append({
                "slug": slug,
                "market_id": items[0].get("canonical_market_id"),
                "condition_id": payload.get("conditionId"),
                "uma_resolution_status": parsed.get("uma_resolution_status"),
                "resolution_status": parsed.get("resolution_status"),
                "resolved_outcome": parsed.get("resolved_outcome"),
            })
        except urllib.error.HTTPError as exc:
            fetch_errors.append({"slug": slug, "error": f"HTTP {exc.code}"})
            continue
        except Exception as exc:  # noqa: BLE001
            fetch_errors.append({"slug": slug, "error": str(exc)})
            continue

        for item in items:
            canonical_market_id = str(item.get("canonical_market_id") or "")
            if canonical_market_id and canonical_market_id != str(item.get("market_id") or ""):
                update_vars = {
                    "forecast_id": str(item.get("forecast_id") or ""),
                    "canonical_market_id": canonical_market_id,
                    "platform": str(item.get("canonical_platform") or "polymarket"),
                    "market_slug": str(item.get("canonical_market_slug") or ""),
                }
                if args.dry_run:
                    identity_updates.append({"dry_run": True, **update_vars})
                else:
                    updated = exec_sql(args.psql, args.db_url, UPDATE_FORECAST_IDENTITY_SQL, update_vars) or {}
                    identity_updates.append(updated)

        parsed = parse_market_payload(payload)
        if parsed.get("resolution_status") != "resolved":
            continue

        for item in items:
            resolved_value = resolved_value_for_contract(
                str(item.get("contract_id") or ""),
                str(parsed.get("resolved_outcome") or ""),
                list(parsed.get("outcomes") or []),
            )
            record = {
                "market_id": str(item.get("canonical_market_id") or ""),
                "contract_id": str(item.get("contract_id") or "yes"),
                "platform": str(item.get("canonical_platform") or "polymarket"),
                "resolution_status": "resolved",
                "resolved_outcome": str(parsed.get("resolved_outcome") or ""),
                "resolved_value": resolved_value,
                "resolved_ts": str(parsed.get("resolved_ts") or ""),
                "resolution_source": f"gamma-api.polymarket.com/markets/slug/{slug}",
                "resolution_notes": json.dumps({
                    "uma_resolution_status": parsed.get("uma_resolution_status"),
                    "condition_id": payload.get("conditionId"),
                    "closed": parsed.get("closed"),
                }, separators=(",", ":")),
            }
            if args.dry_run:
                resolution_writes.append({"dry_run": True, **record})
            else:
                persisted = exec_sql(args.psql, args.db_url, UPSERT_RESOLUTION_SQL, record) or {}
                resolution_writes.append(persisted)

    result = {
        "ok": True,
        "candidate_count": len(candidates),
        "group_count": len(grouped),
        "fetched_markets": fetched_market_summaries,
        "identity_updates": identity_updates,
        "resolution_writes": resolution_writes,
        "skipped": skipped,
        "fetch_errors": fetch_errors,
        "dry_run": args.dry_run,
    }
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
