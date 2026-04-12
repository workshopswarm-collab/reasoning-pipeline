#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in os.sys.path:
    os.sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    case_light_refresh_brief_json_path,
    case_light_refresh_brief_markdown_path,
    coerce_string,
    normalize_probability,
    percent_points_from_prob_delta,
    relative_to_workspace,
    utc_now_iso,
    write_json,
)

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

SQL = r'''
WITH target_case AS (
  SELECT
    c.id::text AS case_db_id,
    c.case_key,
    c.status AS case_status,
    m.id::text AS market_id,
    m.platform,
    m.external_market_id,
    m.slug,
    m.title,
    m.description,
    m.category,
    m.status AS market_status,
    m.outcome_type,
    m.current_price,
    m.last_reasoned_price,
    m.closes_at,
    m.resolves_at,
    m.updated_at AS market_updated_at
  FROM public.cases c
  JOIN public.markets m ON m.id = c.market_id
  WHERE c.case_key = :'case_key'
  ORDER BY c.opened_at DESC
  LIMIT 1
),
latest_forecast AS (
  SELECT
    lfd.forecast_id,
    lfd.case_id,
    lfd.dispatch_id,
    lfd.market_id,
    lfd.contract_id,
    lfd.question,
    lfd.forecast_prob,
    lfd.forecast_direction,
    lfd.confidence_label,
    lfd.decision_status,
    lfd.rationale_summary,
    lfd.decision_packet_path,
    lfd.decision_ts,
    lfd.created_at,
    lfd.resolution_status,
    lfd.resolved_outcome,
    lfd.resolved_value,
    lfd.resolved_ts
  FROM public.latest_forecast_decisions lfd
  JOIN target_case tc ON tc.market_id = lfd.market_id
  WHERE lfd.contract_id = COALESCE(NULLIF(:'contract_id', ''), 'yes')
  ORDER BY lfd.decision_ts DESC, lfd.created_at DESC
  LIMIT 1
),
snapshot_rows AS (
  SELECT
    observed_at,
    last_price,
    yes_price,
    no_price,
    best_bid,
    best_ask,
    volume,
    open_interest,
    COALESCE(yes_price, last_price) AS reference_price
  FROM public.market_snapshots ms
  JOIN target_case tc ON tc.market_id::uuid = ms.market_id
  ORDER BY observed_at DESC
  LIMIT 12
),
snapshot_summary AS (
  SELECT
    COUNT(*) AS snapshot_count,
    MIN(reference_price) AS min_reference_price,
    MAX(reference_price) AS max_reference_price,
    AVG(reference_price) AS avg_reference_price,
    MIN(observed_at) AS oldest_observed_at,
    MAX(observed_at) AS latest_observed_at
  FROM snapshot_rows
)
SELECT json_build_object(
  'case', (SELECT row_to_json(tc) FROM target_case tc),
  'latest_forecast', (SELECT row_to_json(lf) FROM latest_forecast lf),
  'snapshot_summary', (SELECT row_to_json(ss) FROM snapshot_summary ss),
  'recent_snapshots', COALESCE((SELECT json_agg(row_to_json(sr) ORDER BY sr.observed_at DESC) FROM snapshot_rows sr), '[]'::json)
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a lightweight refresh brief for Decision-Maker prior updates")
    parser.add_argument("--case-key", required=True)
    parser.add_argument("--contract-id", default="yes")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL") or os.getenv("PREDQUANT_ADMIN_URL", ""))
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL))
    parser.add_argument("--full-refresh-price-delta", type=float, default=0.12)
    parser.add_argument("--full-refresh-close-hours", type=float, default=12.0)
    parser.add_argument("--full-refresh-stale-hours", type=float, default=12.0)
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def exec_sql(psql_bin: str, db_url: str, sql: str, variables: dict[str, str]) -> dict[str, Any]:
    if not db_url:
        raise ValueError("--db-url, PREDQUANT_ORCHESTRATOR_URL, or PREDQUANT_ADMIN_URL is required")
    cmd = [psql_bin, db_url, "-X", "-qAt", "-v", "ON_ERROR_STOP=1"]
    for key, value in variables.items():
        cmd.extend(["-v", f"{key}={value}"])
    cmd.extend(["-f", "-"])
    proc = subprocess.run(cmd, input=sql, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "psql failed")
    stdout = proc.stdout.strip()
    if not stdout:
        return {}
    return json.loads(stdout.splitlines()[-1])


def parse_iso(value: Any) -> datetime | None:
    text = coerce_string(value)
    if not text:
        return None
    text = text.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def hours_between(start: datetime | None, end: datetime | None) -> float | None:
    if start is None or end is None:
        return None
    return round((end - start).total_seconds() / 3600.0, 2)


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


def fetch_gamma_market(slug: str) -> dict[str, Any]:
    if not slug:
        return {}
    url = f"https://gamma-api.polymarket.com/markets/slug/{slug}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        payload = json.loads(response.read().decode())
    return payload if isinstance(payload, dict) else {}


def classify_refresh(*, price_delta: float | None, hours_to_close: float | None, hours_since_last_forecast: float | None, full_refresh_price_delta: float, full_refresh_close_hours: float, full_refresh_stale_hours: float) -> tuple[str, list[str]]:
    reasons: list[str] = []
    if price_delta is not None and price_delta >= full_refresh_price_delta:
        reasons.append("large_price_move")
    if hours_to_close is not None and hours_to_close <= full_refresh_close_hours:
        reasons.append("near_close")
    if hours_since_last_forecast is not None and hours_since_last_forecast >= full_refresh_stale_hours:
        reasons.append("stale_forecast")
    if reasons:
        return "full", reasons
    if price_delta is not None and price_delta > 0:
        return "light", ["material_price_move"]
    return "light", ["refresh_requested"]


def safe_float(value: Any) -> float | None:
    try:
        numeric = float(value)
    except Exception:
        return None
    if math.isnan(numeric) or math.isinf(numeric):
        return None
    return numeric


def focused_questions(mode: str, reasons: list[str]) -> list[str]:
    questions = [
        "Did the market move invalidate the prior crux, or is this mainly repricing without new information?",
        "Does the new price imply the previous edge has materially compressed or inverted?",
        "Has time-to-close changed the appropriate confidence or action threshold?",
    ]
    if mode == "full" or "near_close" in reasons:
        questions.append("Is there a fresh catalyst, resolution-mechanics update, or contract-interpretation issue that now requires broader re-research?")
    else:
        questions.append("Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?")
    return questions


def build_markdown(brief: dict[str, Any]) -> str:
    market = brief.get("market") or {}
    latest = brief.get("latest_forecast") or {}
    assessment = brief.get("refresh_assessment") or {}
    snapshot_summary = brief.get("snapshot_summary") or {}
    live_probe = brief.get("live_market_probe") or {}
    lines = [
        "# Light refresh brief",
        "",
        f"- case_key: `{brief.get('case_key', '')}`",
        f"- built_at: `{brief.get('built_at', '')}`",
        f"- recommended_mode: `{assessment.get('recommended_mode', '')}`",
        f"- refresh_reasons: `{', '.join(assessment.get('reasons') or [])}`",
        f"- market: `{market.get('title', '')}` (`{market.get('market_id', '')}`)",
        f"- current_price: `{market.get('current_price', '')}`",
        f"- last_reasoned_price: `{market.get('last_reasoned_price', '')}`",
        f"- price_delta_pct_points: `{assessment.get('price_delta_pct_points', '')}`",
        f"- hours_since_last_forecast: `{assessment.get('hours_since_last_forecast', '')}`",
        f"- hours_to_close: `{assessment.get('hours_to_close', '')}`",
        "",
        "## Latest forecast",
        "",
        f"- forecast_id: `{latest.get('forecast_id', '')}`",
        f"- forecast_prob: `{latest.get('forecast_prob', '')}`",
        f"- decision_ts: `{latest.get('decision_ts', '')}`",
        f"- rationale_summary: {latest.get('rationale_summary', '')}",
        "",
        "## Recent market snapshot summary",
        "",
        f"- snapshot_count: `{snapshot_summary.get('snapshot_count', 0)}`",
        f"- min_reference_price: `{snapshot_summary.get('min_reference_price', '')}`",
        f"- max_reference_price: `{snapshot_summary.get('max_reference_price', '')}`",
        f"- avg_reference_price: `{snapshot_summary.get('avg_reference_price', '')}`",
        "",
        "## Live Polymarket probe",
        "",
        f"- slug: `{live_probe.get('slug', '')}`",
        f"- closed: `{live_probe.get('closed', '')}`",
        f"- archived: `{live_probe.get('archived', '')}`",
        f"- acceptingOrders: `{live_probe.get('acceptingOrders', '')}`",
        f"- umaResolutionStatus: `{live_probe.get('umaResolutionStatus', '')}`",
        f"- outcomePrices: `{live_probe.get('outcomePrices', [])}`",
        "",
        "## Focused refresh questions",
        "",
    ]
    for item in brief.get("focused_questions") or []:
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    payload = exec_sql(args.psql, args.db_url, SQL, {"case_key": args.case_key, "contract_id": args.contract_id})
    market = payload.get("case") or {}
    latest = payload.get("latest_forecast") or {}
    if not market:
        raise ValueError(f"case not found: {args.case_key}")
    if not latest:
        raise ValueError(f"no latest forecast found for case={args.case_key} contract_id={args.contract_id}")

    now = datetime.now(timezone.utc)
    current_price = normalize_probability(market.get("current_price"))
    last_reasoned_price = normalize_probability(market.get("last_reasoned_price"))
    price_delta = abs((current_price or 0.0) - (last_reasoned_price or 0.0)) if current_price is not None and last_reasoned_price is not None else None
    decision_ts = parse_iso(latest.get("decision_ts"))
    closes_at = parse_iso(market.get("closes_at"))
    quote_timestamp = parse_iso((payload.get("snapshot_summary") or {}).get("latest_observed_at")) or parse_iso(market.get("market_updated_at"))
    hours_since_last_forecast = hours_between(decision_ts, now)
    hours_to_close = hours_between(now, closes_at)
    mode, reasons = classify_refresh(
        price_delta=price_delta,
        hours_to_close=hours_to_close,
        hours_since_last_forecast=hours_since_last_forecast,
        full_refresh_price_delta=args.full_refresh_price_delta,
        full_refresh_close_hours=args.full_refresh_close_hours,
        full_refresh_stale_hours=args.full_refresh_stale_hours,
    )

    try:
        live_probe_raw = fetch_gamma_market(coerce_string(market.get("slug"))) if coerce_string(market.get("platform")) == "polymarket" else {}
    except Exception:
        live_probe_raw = {}
    live_probe = {
        "slug": coerce_string(live_probe_raw.get("slug")) or coerce_string(market.get("slug")),
        "question": coerce_string(live_probe_raw.get("question")) or coerce_string(market.get("title")),
        "closed": bool(live_probe_raw.get("closed")),
        "archived": bool(live_probe_raw.get("archived")),
        "acceptingOrders": bool(live_probe_raw.get("acceptingOrders")),
        "automaticallyResolved": bool(live_probe_raw.get("automaticallyResolved")),
        "umaResolutionStatus": coerce_string(live_probe_raw.get("umaResolutionStatus")),
        "endDate": coerce_string(live_probe_raw.get("endDate")),
        "updatedAt": coerce_string(live_probe_raw.get("updatedAt")),
        "outcomes": parse_jsonish_list(live_probe_raw.get("outcomes")),
        "outcomePrices": parse_jsonish_list(live_probe_raw.get("outcomePrices")),
        "oneDayPriceChange": safe_float(live_probe_raw.get("oneDayPriceChange")),
        "oneHourPriceChange": safe_float(live_probe_raw.get("oneHourPriceChange")),
        "volumeNum": safe_float(live_probe_raw.get("volumeNum")),
        "liquidityNum": safe_float(live_probe_raw.get("liquidityNum")),
    }

    snapshot_summary = payload.get("snapshot_summary") or {}
    brief = {
        "artifact_type": "light_refresh_brief",
        "schema_version": "light-refresh/v1",
        "built_at": utc_now_iso(),
        "case_key": args.case_key,
        "market": {
            "market_id": coerce_string(market.get("market_id")),
            "platform": coerce_string(market.get("platform")),
            "external_market_id": coerce_string(market.get("external_market_id")),
            "slug": coerce_string(market.get("slug")),
            "title": coerce_string(market.get("title")),
            "description": coerce_string(market.get("description")),
            "category": coerce_string(market.get("category")),
            "status": coerce_string(market.get("market_status")),
            "current_price": current_price,
            "last_reasoned_price": last_reasoned_price,
            "closes_at": coerce_string(market.get("closes_at")),
            "resolves_at": coerce_string(market.get("resolves_at")),
            "quote_timestamp": quote_timestamp.isoformat() if quote_timestamp else "",
        },
        "latest_forecast": latest,
        "snapshot_summary": snapshot_summary,
        "recent_snapshots": payload.get("recent_snapshots") or [],
        "live_market_probe": live_probe,
        "refresh_assessment": {
            "recommended_mode": mode,
            "reasons": reasons,
            "price_delta": round(price_delta, 6) if price_delta is not None else None,
            "price_delta_pct_points": percent_points_from_prob_delta(price_delta) if price_delta is not None else None,
            "hours_since_last_forecast": hours_since_last_forecast,
            "hours_to_close": hours_to_close,
            "forecast_vs_market_gap_pct_points": percent_points_from_prob_delta((normalize_probability(latest.get("forecast_prob")) or 0.0) - (current_price or 0.0)) if normalize_probability(latest.get("forecast_prob")) is not None and current_price is not None else None,
        },
        "focused_questions": focused_questions(mode, reasons),
    }

    json_path = case_light_refresh_brief_json_path(args.case_key)
    markdown_path = case_light_refresh_brief_markdown_path(args.case_key)
    write_json(json_path, brief, pretty=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(build_markdown(brief))

    result = {
        "ok": True,
        "case_key": args.case_key,
        "market_id": brief["market"]["market_id"],
        "market_title": brief["market"]["title"],
        "current_price": brief["market"]["current_price"],
        "quote_timestamp": brief["market"]["quote_timestamp"],
        "recommended_mode": brief["refresh_assessment"]["recommended_mode"],
        "reasons": brief["refresh_assessment"]["reasons"],
        "light_refresh_brief_json": relative_to_workspace(json_path),
        "light_refresh_brief_markdown": relative_to_workspace(markdown_path),
    }
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
