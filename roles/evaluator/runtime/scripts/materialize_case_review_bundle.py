#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from compile_learning_packet import compile_learning_packet  # noqa: E402
from draft_case_review import build_review_markdown  # noqa: E402
from extract_learning_signals import build_signal_packet, persist_signal_packet  # noqa: E402
from project_case_to_causal_map import project_case_to_causal_map  # noqa: E402
from extract_case_causal_suggestions import extract_case_suggestions_flow  # noqa: E402
from canonicalize_causal_suggestions import canonicalize_case_suggestions  # noqa: E402
from run_evaluator_memory_upgrade import run_memory_upgrade_flow  # noqa: E402
from run_evaluator_review import run_review_flow  # noqa: E402
from upsert_learning_case_review_index import build_index_record, persist_index_record  # noqa: E402
from lib.io import write_json  # noqa: E402
from lib.db import DEFAULT_PSQL  # noqa: E402
from lib.paths import (  # noqa: E402
    case_canonical_causal_suggestions_path,
    case_review_markdown_path,
    ensure_parent,
    learning_packet_path,
    provenance_path,
    signal_packet_path,
    to_repo_relative,
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def build_provenance(
    *,
    case_key: str,
    packet: dict[str, Any],
    packet_path: Path,
    review_path: Path,
    signal_path: Path,
    index_record: dict[str, Any],
    signal_packet: dict[str, Any],
    causal_projection_path_str: str | None = None,
    causal_suggestions_path_str: str | None = None,
    causal_suggestions_canonical_path_str: str | None = None,
) -> dict[str, Any]:
    bundle_paths = {
        "learning_packet_path": to_repo_relative(packet_path),
        "review_path": to_repo_relative(review_path),
        "signal_packet_path": to_repo_relative(signal_path),
        "provenance_path": to_repo_relative(provenance_path(case_key)),
    }
    if causal_projection_path_str:
        bundle_paths["causal_projection_path"] = causal_projection_path_str
    if causal_suggestions_path_str:
        bundle_paths["causal_suggestions_path"] = causal_suggestions_path_str
    if causal_suggestions_canonical_path_str:
        bundle_paths["causal_suggestions_canonical_path"] = causal_suggestions_canonical_path_str
    return {
        "artifact_type": "learning_case_review_bundle_provenance",
        "schema_version": "v1",
        "generated_at": utc_now_iso(),
        "generated_by": "roles/evaluator/runtime/scripts/materialize_case_review_bundle.py",
        "case_key": case_key,
        "bundle_paths": bundle_paths,
        "upstream_paths": packet.get("provenance_paths") or {},
        "index_record_preview": index_record,
        "signal_packet_preview": {
            "signal_count": signal_packet.get("signal_count"),
            "first_signal": (signal_packet.get("signals") or [None])[0],
        },
    }


def materialize_case_review_bundle(
    case_key: str,
    *,
    contract_id: str = "yes",
    db_url: str = "",
    psql_bin: str = DEFAULT_PSQL,
    agent_review: bool = False,
    memory_upgrade: bool = False,
    causal_projection: bool = False,
    causal_suggestions: bool = False,
    session_key: str = 'agent:evaluator:main',
    agent_id: str | None = None,
    timeout_seconds: float = 480.0,
) -> dict[str, Any]:
    packet_path = ensure_parent(learning_packet_path(case_key))
    review_path = ensure_parent(case_review_markdown_path(case_key))
    signal_path = ensure_parent(signal_packet_path(case_key))
    provenance_out = ensure_parent(provenance_path(case_key))

    packet = compile_learning_packet(case_key, contract_id=contract_id, db_url=db_url, psql_bin=psql_bin)
    write_json(packet_path, packet, pretty=True)

    review_write_mode = 'preserved_existing' if review_path.exists() and not agent_review else 'draft_written'
    if not review_path.exists() or agent_review:
        review_markdown = build_review_markdown(packet)
        review_path.write_text(review_markdown, encoding="utf-8")

    agent_review_result = None
    if agent_review:
        agent_review_result = run_review_flow(
            case_key,
            packet_path=packet_path,
            review_path=review_path,
            session_key=session_key,
            agent_id=agent_id,
            timeout_seconds=timeout_seconds,
            contract_id=contract_id,
            db_url=db_url,
            psql_bin=psql_bin,
        )

    signal_packet = build_signal_packet(review_path, packet_path)
    write_json(signal_path, signal_packet, pretty=True)

    index_record = build_index_record(review_path, packet_path)
    index_persist = persist_index_record(index_record, db_url=db_url, psql_bin=psql_bin)
    signal_persist = persist_signal_packet(signal_packet, db_url=db_url, psql_bin=psql_bin)

    memory_upgrade_result = None
    if memory_upgrade:
        memory_upgrade_result = run_memory_upgrade_flow(
            case_key,
            review_path=review_path,
            signal_path=signal_path,
            packet_path=packet_path,
            session_key=session_key,
            agent_id=agent_id,
            timeout_seconds=timeout_seconds,
            db_url=db_url,
            psql_bin=psql_bin,
        )

    causal_projection_result = None
    if causal_projection or causal_suggestions:
        causal_projection_result = project_case_to_causal_map(
            case_key,
            review_path=review_path,
            signal_path=signal_path,
            packet_path=packet_path,
            db_url=db_url,
            psql_bin=psql_bin,
        )

    causal_suggestions_result = None
    if causal_suggestions:
        extract_result = extract_case_suggestions_flow(
            case_key,
            review_path=review_path,
            signal_path=signal_path,
            packet_path=packet_path,
            write_output=True,
        )
        canonicalize_result = canonicalize_case_suggestions([case_key], write_output=True)
        case_summary = ((canonicalize_result.get('summary') or {}).get('cases') or [{}])[0]
        causal_suggestions_result = {
            'raw': extract_result,
            'canonicalize': {
                'case_key': case_key,
                'suggestion_count': case_summary.get('suggestion_count'),
                'projection_significant': case_summary.get('projection_significant'),
                'summary_path': canonicalize_result.get('summary_path'),
                'index_path': canonicalize_result.get('index_path'),
            },
        }

    provenance = build_provenance(
        case_key=case_key,
        packet=packet,
        packet_path=packet_path,
        review_path=review_path,
        signal_path=signal_path,
        index_record=index_record,
        signal_packet=signal_packet,
        causal_projection_path_str=(causal_projection_result or {}).get("projection_path"),
        causal_suggestions_path_str=((causal_suggestions_result or {}).get('raw') or {}).get('out_path'),
        causal_suggestions_canonical_path_str=(
            to_repo_relative(case_canonical_causal_suggestions_path(case_key)) if causal_suggestions_result else None
        ),
    )
    write_json(provenance_out, provenance, pretty=True)

    return {
        "ok": True,
        "case_key": case_key,
        "paths": {
            "learning_packet_path": to_repo_relative(packet_path),
            "review_path": to_repo_relative(review_path),
            "signal_packet_path": to_repo_relative(signal_path),
            "provenance_path": to_repo_relative(provenance_out),
        },
        "resolution_status": (packet.get("market_truth") or {}).get("resolution_status"),
        "resolved_value": (packet.get("market_truth") or {}).get("resolved_value"),
        "review_write_mode": review_write_mode,
        "signal_count": signal_packet.get("signal_count"),
        "index_status": index_record.get("status"),
        "agent_review": agent_review_result,
        "memory_upgrade": memory_upgrade_result,
        "causal_projection": causal_projection_result,
        "causal_suggestions": causal_suggestions_result,
        "persistence": {
            "index": index_persist,
            "signals": signal_persist,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Materialize a canonical evaluator case-review bundle into qualitative-db/50-learnings")
    parser.add_argument("--case-key", required=True)
    parser.add_argument("--contract-id", default="yes")
    parser.add_argument("--db-url", default="")
    parser.add_argument("--psql", default=DEFAULT_PSQL)
    parser.add_argument("--agent-review", action="store_true")
    parser.add_argument("--memory-upgrade", action="store_true")
    parser.add_argument("--causal-projection", action="store_true")
    parser.add_argument("--causal-suggestions", action="store_true")
    parser.add_argument("--session-key", default="agent:evaluator:main")
    parser.add_argument("--agent-id")
    parser.add_argument("--timeout-seconds", type=float, default=480.0)
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = materialize_case_review_bundle(
        args.case_key,
        contract_id=args.contract_id,
        db_url=args.db_url,
        psql_bin=args.psql,
        agent_review=args.agent_review,
        memory_upgrade=args.memory_upgrade,
        causal_projection=args.causal_projection,
        causal_suggestions=args.causal_suggestions,
        session_key=args.session_key,
        agent_id=args.agent_id,
        timeout_seconds=args.timeout_seconds,
    )
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
