#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import (  # noqa: E402
    WORKSPACE_ROOT,
    coerce_string,
    load_dispatch_manifest_market,
    load_json,
    normalize_probability,
    relative_to_workspace,
)
from validation import validate_decision_packet_payload  # noqa: E402

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"


def looks_like_uuid(value: str) -> bool:
    text = (value or "").strip().lower()
    parts = text.split("-")
    return len(parts) == 5 and [len(p) for p in parts] == [8, 4, 4, 4, 12]


PERSIST_SQL = r'''
WITH latest_existing AS (
  SELECT fd.forecast_id
  FROM public.forecast_decisions fd
  WHERE fd.market_id = :'market_id'
    AND fd.contract_id = :'contract_id'
    AND fd.forecast_id <> :'forecast_id'
  ORDER BY fd.decision_ts DESC, fd.created_at DESC
  LIMIT 1
),
upserted AS (
  INSERT INTO public.forecast_decisions (
    forecast_id,
    decision_ts,
    case_id,
    dispatch_id,
    market_id,
    contract_id,
    platform,
    market_slug,
    question,
    forecast_prob,
    forecast_direction,
    confidence_label,
    confidence_score,
    time_horizon_label,
    verification_mode,
    decision_status,
    rationale_summary,
    decision_packet_path,
    decision_handoff_path,
    syndicated_finding_path,
    supersedes_forecast_id,
    updated_at
  )
  VALUES (
    :'forecast_id',
    NULLIF(:'decision_ts', '')::timestamptz,
    NULLIF(:'case_id', ''),
    NULLIF(:'dispatch_id', ''),
    :'market_id',
    :'contract_id',
    :'platform',
    NULLIF(:'market_slug', ''),
    :'question',
    NULLIF(:'forecast_prob', '')::numeric,
    NULLIF(:'forecast_direction', ''),
    NULLIF(:'confidence_label', ''),
    NULLIF(:'confidence_score', '')::numeric,
    NULLIF(:'time_horizon_label', ''),
    NULLIF(:'verification_mode', ''),
    :'decision_status',
    NULLIF(:'rationale_summary', ''),
    :'decision_packet_path',
    NULLIF(:'decision_handoff_path', ''),
    NULLIF(:'syndicated_finding_path', ''),
    (SELECT forecast_id FROM latest_existing),
    NOW()
  )
  ON CONFLICT (forecast_id)
  DO UPDATE SET
    decision_ts = EXCLUDED.decision_ts,
    case_id = EXCLUDED.case_id,
    dispatch_id = EXCLUDED.dispatch_id,
    market_id = EXCLUDED.market_id,
    contract_id = EXCLUDED.contract_id,
    platform = EXCLUDED.platform,
    market_slug = EXCLUDED.market_slug,
    question = EXCLUDED.question,
    forecast_prob = EXCLUDED.forecast_prob,
    forecast_direction = EXCLUDED.forecast_direction,
    confidence_label = EXCLUDED.confidence_label,
    confidence_score = EXCLUDED.confidence_score,
    time_horizon_label = EXCLUDED.time_horizon_label,
    verification_mode = EXCLUDED.verification_mode,
    decision_status = EXCLUDED.decision_status,
    rationale_summary = EXCLUDED.rationale_summary,
    decision_packet_path = EXCLUDED.decision_packet_path,
    decision_handoff_path = EXCLUDED.decision_handoff_path,
    syndicated_finding_path = EXCLUDED.syndicated_finding_path,
    supersedes_forecast_id = (SELECT forecast_id FROM latest_existing),
    updated_at = NOW()
  RETURNING forecast_id, market_id, contract_id, forecast_prob, decision_status, decision_packet_path, supersedes_forecast_id
),
superseded AS (
  UPDATE public.forecast_decisions fd
  SET decision_status = 'superseded',
      updated_at = NOW()
  WHERE fd.market_id = :'market_id'
    AND fd.contract_id = :'contract_id'
    AND fd.forecast_id <> :'forecast_id'
    AND fd.decision_status IN ('recorded', 'superseded')
  RETURNING fd.forecast_id
),
market_state AS (
  UPDATE public.markets m
  SET last_reasoned_price = NULLIF(:'forecast_prob', '')::numeric,
      pipeline_status = CASE
        WHEN :'decision_status' = 'recorded' AND m.status = 'open' THEN 'executed'::processing_status
        ELSE m.pipeline_status
      END,
      updated_at = NOW()
  WHERE m.id::text = :'market_id'
  RETURNING m.id::text AS market_id, m.current_price, m.last_reasoned_price, m.pipeline_status
)
SELECT json_build_object(
  'forecast_id', (SELECT forecast_id FROM upserted),
  'market_id', (SELECT market_id FROM upserted),
  'contract_id', (SELECT contract_id FROM upserted),
  'forecast_prob', (SELECT forecast_prob FROM upserted),
  'decision_status', (SELECT decision_status FROM upserted),
  'decision_packet_path', (SELECT decision_packet_path FROM upserted),
  'supersedes_forecast_id', (SELECT supersedes_forecast_id FROM upserted),
  'superseded_forecast_ids', COALESCE((SELECT json_agg(s.forecast_id) FROM superseded s), '[]'::json),
  'market_state', COALESCE((SELECT row_to_json(ms) FROM market_state ms), '{}'::json)
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Persist a validated decision packet into quant-db forecast_decisions")
    parser.add_argument("--packet-json", required=True)
    parser.add_argument("--contract-id", default="")
    parser.add_argument("--platform", default="polymarket")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_DECISION_URL", ""))
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL))
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def exec_sql(psql_bin: str, db_url: str, sql: str, variables: dict[str, str]) -> dict[str, Any] | None:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_DECISION_URL is required")
    cmd = [psql_bin, db_url, '-X', '-qAt', '-v', 'ON_ERROR_STOP=1']
    for key, value in variables.items():
        cmd.extend(['-v', f'{key}={value}'])
    cmd.extend(['-f', '-'])
    proc = subprocess.run(cmd, input=sql, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'psql failed')
    stdout = proc.stdout.strip()
    if not stdout:
        return None
    try:
        return json.loads(stdout.splitlines()[-1])
    except json.JSONDecodeError:
        return {"raw": stdout}


def decision_status_from_packet(packet: dict[str, Any]) -> str:
    decision = packet.get("decision") if isinstance(packet.get("decision"), dict) else {}
    readiness = coerce_string(decision.get("decision_readiness"))
    if readiness == "ready":
        return "recorded"
    if readiness in {"needs_more_research", "needs_market_update"}:
        return "void"
    return "error"


def build_record(packet: dict[str, Any], packet_path: Path, contract_id_override: str, platform_override: str) -> dict[str, str]:
    context = packet.get("context") if isinstance(packet.get("context"), dict) else {}
    decision = packet.get("decision") if isinstance(packet.get("decision"), dict) else {}
    valuation = packet.get("valuation") if isinstance(packet.get("valuation"), dict) else {}
    execution = packet.get("execution_semantics") if isinstance(packet.get("execution_semantics"), dict) else {}
    audit = packet.get("audit") if isinstance(packet.get("audit"), dict) else {}

    case_key = coerce_string(context.get("case_key"))
    dispatch_id = coerce_string(context.get("dispatch_id"))
    manifest_market = load_dispatch_manifest_market(dispatch_id)
    context_market_id = coerce_string(context.get("market_id"))
    manifest_market_id = coerce_string(manifest_market.get("market_id"))
    market_id = (
        manifest_market_id if looks_like_uuid(manifest_market_id)
        else context_market_id if looks_like_uuid(context_market_id)
        else manifest_market_id
        or context_market_id
        or case_key
    )
    contract_id = contract_id_override.strip() or coerce_string(context.get("contract_id")) or "yes"
    question = coerce_string(context.get("question")) or coerce_string(context.get("market_title")) or coerce_string(manifest_market.get("title"))
    forecast_prob = normalize_probability(valuation.get("fair_value_mid"))
    confidence_label = coerce_string(valuation.get("independent_verification_quality"))
    rationale_summary = coerce_string(audit.get("one_sentence_rationale"))
    verification_mode = coerce_string(audit.get("verification_mode_used"))
    time_horizon_label = coerce_string(execution.get("time_horizon"))
    decision_packet_path = relative_to_workspace(packet_path)
    decision_handoff_path = coerce_string(context.get("source_decision_handoff_path"))
    syndicated_finding_path = coerce_string(context.get("source_syndicated_finding_path"))
    generated_at = coerce_string(packet.get("generated_at"))
    forecast_direction = coerce_string(decision.get("side"))

    if not market_id:
        raise ValueError("packet context missing market_id")
    if not contract_id:
        raise ValueError("contract_id missing; provide context.contract_id or --contract-id")
    if not question:
        raise ValueError("packet context missing question")
    if forecast_prob is None:
        raise ValueError("packet valuation.fair_value_mid missing or invalid")
    if not generated_at:
        raise ValueError("packet generated_at missing")

    forecast_id = dispatch_id or f"{case_key}:{market_id}:{contract_id}:{generated_at}"

    return {
        "forecast_id": forecast_id,
        "decision_ts": generated_at,
        "case_id": case_key,
        "dispatch_id": dispatch_id,
        "market_id": market_id,
        "contract_id": contract_id,
        "platform": coerce_string(context.get("platform")) or platform_override.strip() or coerce_string(manifest_market.get("platform")) or "polymarket",
        "market_slug": coerce_string(context.get("market_slug")) or coerce_string(manifest_market.get("slug")),
        "question": question,
        "forecast_prob": str(forecast_prob),
        "forecast_direction": forecast_direction,
        "confidence_label": confidence_label,
        "confidence_score": "",
        "time_horizon_label": time_horizon_label,
        "verification_mode": verification_mode,
        "decision_status": decision_status_from_packet(packet),
        "rationale_summary": rationale_summary,
        "decision_packet_path": decision_packet_path,
        "decision_handoff_path": decision_handoff_path,
        "syndicated_finding_path": syndicated_finding_path,
    }


def main() -> int:
    args = parse_args()
    packet_path = Path(args.packet_json)
    if not packet_path.is_absolute():
        packet_path = WORKSPACE_ROOT / packet_path
    packet = load_json(packet_path)
    validation = validate_decision_packet_payload(packet)
    if not validation.get("ok"):
        print(json.dumps({
            "ok": False,
            "packet_json": relative_to_workspace(packet_path),
            "errors": validation.get("errors", []),
            "warnings": validation.get("warnings", []),
        }, indent=2 if args.pretty else None))
        return 1

    record = build_record(packet, packet_path, args.contract_id, args.platform)
    result = exec_sql(args.psql, args.db_url, PERSIST_SQL, record) or {}
    print(json.dumps({
        "ok": True,
        "packet_json": relative_to_workspace(packet_path),
        "persisted": result,
        "record": record,
        "warnings": validation.get("warnings", []),
    }, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
