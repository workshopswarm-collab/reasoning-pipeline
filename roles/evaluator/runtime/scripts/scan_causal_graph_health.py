#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
REPO_ROOT = SCRIPT_PATH.parents[4]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.causal_map import build_edge_record, build_node_record, edge_note_paths, node_note_paths  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402

STATUS_BY_STAGE = {
    'draft': 'draft',
    'trial': 'active',
    'active': 'active',
    'hold': 'hold',
    'retired': 'retired',
    'archived': 'archived',
}
SEVERITY_RANK = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4}
DEFAULT_STALE_ACTIVITY_DAYS = 45.0
DEFAULT_LIVE_DECAY_THRESHOLD = 0.9
DEFAULT_HOLD_DECAY_THRESHOLD = 0.95

NODE_STATS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY node_key), '[]'::json)::text
FROM (
  SELECT *
  FROM public.causal_node_stats
) t;
'''

EDGE_STATS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY edge_key), '[]'::json)::text
FROM (
  SELECT *
  FROM public.causal_edge_stats
) t;
'''

OPEN_HEALTH_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY entity_type, entity_key, violation_kind), '[]'::json)::text
FROM (
  SELECT id, entity_type, entity_key, violation_kind, severity, status, details, detected_at, resolved_at
  FROM public.causal_graph_health_violations
  WHERE COALESCE(NULLIF(status, ''), 'open') NOT IN ('resolved', 'closed')
    AND entity_type IN ('causal_node', 'causal_edge')
) t;
'''

INSERT_VIOLATION_SQL = r'''
INSERT INTO public.causal_graph_health_violations (
  entity_type,
  entity_key,
  violation_kind,
  severity,
  status,
  details,
  detected_at,
  resolved_at
)
VALUES (
  :'entity_type',
  :'entity_key',
  :'violation_kind',
  :'severity',
  'open',
  COALESCE(NULLIF(:'details_json', ''), '{}')::jsonb,
  NOW(),
  NULL
)
RETURNING json_build_object(
  'id', id,
  'entity_type', entity_type,
  'entity_key', entity_key,
  'violation_kind', violation_kind,
  'severity', severity,
  'status', status
)::text;
'''

UPDATE_VIOLATION_SQL = r'''
UPDATE public.causal_graph_health_violations
SET severity = :'severity',
    status = 'open',
    details = COALESCE(NULLIF(:'details_json', ''), '{}')::jsonb,
    detected_at = NOW(),
    resolved_at = NULL
WHERE id = :'row_id'::bigint
RETURNING json_build_object(
  'id', id,
  'entity_type', entity_type,
  'entity_key', entity_key,
  'violation_kind', violation_kind,
  'severity', severity,
  'status', status
)::text;
'''

RESOLVE_VIOLATION_SQL = r'''
UPDATE public.causal_graph_health_violations
SET status = 'resolved',
    resolved_at = NOW()
WHERE id = :'row_id'::bigint
RETURNING json_build_object(
  'id', id,
  'entity_type', entity_type,
  'entity_key', entity_key,
  'violation_kind', violation_kind,
  'severity', severity,
  'status', status
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Scan live causal graph items for structural/evidence/utility/freshness violations')
    parser.add_argument('--node-key', action='append', default=[])
    parser.add_argument('--edge-key', action='append', default=[])
    parser.add_argument('--mechanism-family', action='append', default=[])
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--stale-activity-days', type=float, default=DEFAULT_STALE_ACTIVITY_DAYS)
    parser.add_argument('--live-decay-threshold', type=float, default=DEFAULT_LIVE_DECAY_THRESHOLD)
    parser.add_argument('--hold-decay-threshold', type=float, default=DEFAULT_HOLD_DECAY_THRESHOLD)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def unique(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        value = str(item or '').strip()
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out



def safe_int(*values: Any) -> int:
    for value in values:
        if value in (None, ''):
            continue
        try:
            return int(value)
        except Exception:
            continue
    return 0



def safe_float(*values: Any) -> float:
    for value in values:
        if value in (None, ''):
            continue
        try:
            return float(value)
        except Exception:
            continue
    return 0.0



def parse_iso(value: str | None) -> datetime | None:
    text = str(value or '').strip()
    if not text:
        return None
    if text.endswith('Z'):
        text = text[:-1] + '+00:00'
    try:
        parsed = datetime.fromisoformat(text)
    except Exception:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)



def activity_age_days(record: dict[str, Any]) -> float | None:
    timestamps = [
        parse_iso(record.get('last_helpful_at')),
        parse_iso(record.get('last_injected_at')),
        parse_iso(record.get('last_matched_at')),
        parse_iso(record.get('last_seen_at')),
    ]
    valid = [stamp for stamp in timestamps if stamp is not None]
    if not valid:
        return None
    newest = max(valid)
    return max(0.0, (datetime.now(timezone.utc) - newest).total_seconds() / 86400.0)



def has_any_activity(record: dict[str, Any]) -> bool:
    return any(str(record.get(field) or '').strip() for field in ['last_seen_at', 'last_matched_at', 'last_injected_at', 'last_helpful_at'])



def lifecycle_stage(record: dict[str, Any]) -> str:
    stage = str(record.get('lifecycle_stage') or '').strip().lower()
    if stage:
        return stage
    status = str(record.get('status') or '').strip().lower()
    if status in STATUS_BY_STAGE:
        return status
    return 'draft'



def entry_entity_type(entry: dict[str, Any]) -> str:
    return 'node' if entry.get('entity_type') == 'node' else 'edge'



def db_entity_type(entry: dict[str, Any]) -> str:
    return 'causal_node' if entry_entity_type(entry) == 'node' else 'causal_edge'



def entity_key(entry: dict[str, Any]) -> str:
    record = entry.get('record') or {}
    if entry_entity_type(entry) == 'node':
        return str(record.get('node_key') or '').strip()
    return str(record.get('edge_key') or '').strip()



def family_key(record: dict[str, Any]) -> str:
    return str(record.get('mechanism_family') or 'unassigned').strip() or 'unassigned'



def load_entries(args: argparse.Namespace) -> list[dict[str, Any]]:
    node_keys = set(unique(args.node_key or []))
    edge_keys = set(unique(args.edge_key or []))
    families = set(unique(args.mechanism_family or []))
    restrict_to_nodes = bool(node_keys) and not edge_keys and not families
    restrict_to_edges = bool(edge_keys) and not node_keys and not families
    out: list[dict[str, Any]] = []
    if not restrict_to_edges:
        for note_path in node_note_paths():
            record = build_node_record(note_path)
            if node_keys and str(record.get('node_key') or '') not in node_keys:
                continue
            if families and family_key(record) not in families:
                continue
            out.append({'entity_type': 'node', 'note_path': note_path, 'record': record})
    if not restrict_to_nodes:
        for note_path in edge_note_paths():
            record = build_edge_record(note_path)
            if edge_keys and str(record.get('edge_key') or '') not in edge_keys:
                continue
            if families and family_key(record) not in families:
                continue
            out.append({'entity_type': 'edge', 'note_path': note_path, 'record': record})
    return out



def load_db_rows(sql: str, *, db_url: str, psql_bin: str) -> list[dict[str, Any]]:
    if not db_url:
        return []
    rows = exec_sql(psql_bin, db_url, sql, {})
    return rows if isinstance(rows, list) else []



def support_case_count(stats: dict[str, Any]) -> int:
    return max(
        safe_int(stats.get('supporting_case_count')),
        safe_int(stats.get('matched_case_count')),
        safe_int(stats.get('projected_case_count')),
    )



def judged_case_count(stats: dict[str, Any]) -> int:
    return max(safe_int(stats.get('exposure_count')), safe_int(stats.get('treatment_case_count')))



def evidence_row_count(record: dict[str, Any]) -> int:
    return len([row for row in (record.get('evidence_rows') or []) if isinstance(row, dict)])



def evidence_paths_missing(record: dict[str, Any]) -> list[str]:
    missing: list[str] = []
    for rel_path in record.get('evidence_paths') or []:
        rel = str(rel_path or '').strip()
        if not rel:
            continue
        if not (REPO_ROOT / rel).exists():
            missing.append(rel)
    return missing



def violation(entity_type: str, entity_key: str, violation_kind: str, severity: str, details: dict[str, Any]) -> dict[str, Any]:
    return {
        'entity_type': entity_type,
        'entity_key': entity_key,
        'violation_kind': violation_kind,
        'severity': severity,
        'status': 'open',
        'details': details,
    }



def prefer_violation(current: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    if SEVERITY_RANK.get(str(candidate.get('severity') or 'low'), 1) > SEVERITY_RANK.get(str(current.get('severity') or 'low'), 1):
        return candidate
    return current



def dedupe_violations(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    deduped: dict[tuple[str, str, str], dict[str, Any]] = {}
    for row in rows:
        key = (str(row.get('entity_type') or ''), str(row.get('entity_key') or ''), str(row.get('violation_kind') or ''))
        if not all(key):
            continue
        if key in deduped:
            deduped[key] = prefer_violation(deduped[key], row)
        else:
            deduped[key] = row
    return [deduped[key] for key in sorted(deduped)]



def detect_structural_violations(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    node_map = {
        str(entry.get('record', {}).get('node_key') or ''): entry.get('record') or {}
        for entry in entries
        if entry_entity_type(entry) == 'node' and str(entry.get('record', {}).get('node_key') or '').strip()
    }
    rows: list[dict[str, Any]] = []
    for entry in entries:
        record = entry.get('record') or {}
        stage = lifecycle_stage(record)
        status = str(record.get('status') or '').strip().lower()
        entity_type = db_entity_type(entry)
        key = entity_key(entry)
        expected_status = STATUS_BY_STAGE.get(stage)
        if expected_status and status and status != expected_status:
            rows.append(
                violation(
                    entity_type,
                    key,
                    'structural_status_stage_mismatch',
                    'medium' if stage in {'active', 'trial'} else 'low',
                    {
                        'category': 'structural',
                        'lifecycle_stage': stage,
                        'status': status,
                        'expected_status': expected_status,
                        'path': record.get('path'),
                    },
                )
            )
        if not str(record.get('sidecar_path') or '').strip():
            rows.append(
                violation(
                    entity_type,
                    key,
                    'structural_missing_sidecar',
                    'low',
                    {
                        'category': 'structural',
                        'path': record.get('path'),
                    },
                )
            )
        if entry_entity_type(entry) != 'edge':
            continue
        source_node_key = str(record.get('source_node_key') or '').strip()
        target_node_key = str(record.get('target_node_key') or '').strip()
        missing_endpoints = [
            {
                'role': role,
                'node_key': node_key,
            }
            for role, node_key in [('source', source_node_key), ('target', target_node_key)]
            if not node_key or node_key not in node_map
        ]
        if missing_endpoints:
            rows.append(
                violation(
                    entity_type,
                    key,
                    'structural_missing_edge_endpoint',
                    'high',
                    {
                        'category': 'structural',
                        'path': record.get('path'),
                        'missing_endpoints': missing_endpoints,
                    },
                )
            )
            continue
        if stage in {'active', 'trial'}:
            endpoint_stages = {
                source_node_key: lifecycle_stage(node_map[source_node_key]),
                target_node_key: lifecycle_stage(node_map[target_node_key]),
            }
            lagging = {node_key: node_stage for node_key, node_stage in endpoint_stages.items() if node_stage in {'draft', 'hold', 'retired', 'archived'}}
            if lagging:
                rows.append(
                    violation(
                        entity_type,
                        key,
                        'structural_edge_endpoint_stage_mismatch',
                        'medium',
                        {
                            'category': 'structural',
                            'path': record.get('path'),
                            'edge_stage': stage,
                            'endpoint_stages': endpoint_stages,
                            'lagging_endpoints': lagging,
                        },
                    )
                )
    return dedupe_violations(rows)



def detect_evidence_violations(entries: list[dict[str, Any]], node_stats: dict[str, dict[str, Any]], edge_stats: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for entry in entries:
        record = entry.get('record') or {}
        stage = lifecycle_stage(record)
        entity_type = db_entity_type(entry)
        key = entity_key(entry)
        if entry_entity_type(entry) == 'node':
            stats = node_stats.get(key, {})
            if stage in {'active', 'trial'} and str(record.get('source_kind') or '').strip() == 'promoted_candidate' and support_case_count(stats) == 0:
                rows.append(
                    violation(
                        entity_type,
                        key,
                        'evidence_live_promoted_node_without_support',
                        'medium',
                        {
                            'category': 'evidence',
                            'path': record.get('path'),
                            'lifecycle_stage': stage,
                            'source_kind': record.get('source_kind'),
                            'supporting_case_count': support_case_count(stats),
                            'stats_status': stats.get('status'),
                        },
                    )
                )
            continue
        stats = edge_stats.get(key, {})
        missing_paths = evidence_paths_missing(record)
        if missing_paths:
            rows.append(
                violation(
                    entity_type,
                    key,
                    'evidence_missing_review_paths',
                    'medium',
                    {
                        'category': 'evidence',
                        'path': record.get('path'),
                        'missing_paths': missing_paths,
                    },
                )
            )
        if stage not in {'active', 'trial'}:
            continue
        if str(record.get('confidence_mode') or '').strip() == 'reviewed' and evidence_row_count(record) == 0 and support_case_count(stats) == 0:
            rows.append(
                violation(
                    entity_type,
                    key,
                    'evidence_reviewed_live_edge_without_support',
                    'high',
                    {
                        'category': 'evidence',
                        'path': record.get('path'),
                        'lifecycle_stage': stage,
                        'confidence_mode': record.get('confidence_mode'),
                        'supporting_case_count': support_case_count(stats),
                        'evidence_row_count': evidence_row_count(record),
                    },
                )
            )
        elif str(record.get('source_kind') or '').strip() == 'promoted_candidate' and support_case_count(stats) == 0:
            rows.append(
                violation(
                    entity_type,
                    key,
                    'evidence_live_promoted_edge_without_support',
                    'medium',
                    {
                        'category': 'evidence',
                        'path': record.get('path'),
                        'lifecycle_stage': stage,
                        'source_kind': record.get('source_kind'),
                        'supporting_case_count': support_case_count(stats),
                    },
                )
            )
    return dedupe_violations(rows)



def detect_utility_violations(entries: list[dict[str, Any]], node_stats: dict[str, dict[str, Any]], edge_stats: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for entry in entries:
        record = entry.get('record') or {}
        stage = lifecycle_stage(record)
        if stage not in {'active', 'trial'}:
            continue
        key = entity_key(entry)
        stats = node_stats.get(key, {}) if entry_entity_type(entry) == 'node' else edge_stats.get(key, {})
        if not stats:
            continue
        stats_status = str(stats.get('status') or '').strip().lower()
        learned_weight = safe_float(stats.get('learned_weight'))
        shrunken_uplift = safe_float(stats.get('shrunken_uplift'))
        if stats_status in {'hold', 'retired', 'draft'}:
            rows.append(
                violation(
                    db_entity_type(entry),
                    key,
                    'utility_live_stage_conflicts_with_stats',
                    'high' if stage == 'active' or stats_status == 'retired' else 'medium',
                    {
                        'category': 'utility',
                        'path': record.get('path'),
                        'lifecycle_stage': stage,
                        'stats_status': stats_status,
                        'stats_status_reason': stats.get('status_reason'),
                        'learned_weight': learned_weight,
                        'shrunken_uplift': shrunken_uplift,
                        'contested_case_count': safe_int(stats.get('contested_case_count')),
                        'supporting_case_count': support_case_count(stats),
                        'judged_case_count': judged_case_count(stats),
                    },
                )
            )
        elif judged_case_count(stats) >= 3 and learned_weight < -0.08:
            rows.append(
                violation(
                    db_entity_type(entry),
                    key,
                    'utility_negative_live_item',
                    'medium',
                    {
                        'category': 'utility',
                        'path': record.get('path'),
                        'lifecycle_stage': stage,
                        'stats_status': stats_status,
                        'learned_weight': learned_weight,
                        'shrunken_uplift': shrunken_uplift,
                        'judged_case_count': judged_case_count(stats),
                    },
                )
            )
    return dedupe_violations(rows)



def detect_freshness_violations(
    entries: list[dict[str, Any]],
    node_stats: dict[str, dict[str, Any]],
    edge_stats: dict[str, dict[str, Any]],
    *,
    stale_activity_days: float,
    live_decay_threshold: float,
    hold_decay_threshold: float,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for entry in entries:
        record = entry.get('record') or {}
        stage = lifecycle_stage(record)
        key = entity_key(entry)
        stats = node_stats.get(key, {}) if entry_entity_type(entry) == 'node' else edge_stats.get(key, {})
        source_kind = str(record.get('source_kind') or '').strip()
        decay_score = safe_float(record.get('decay_score'))
        support_count = support_case_count(stats)
        judged_count = judged_case_count(stats)
        activity_days = activity_age_days(record)
        if stage in {'active', 'trial'} and source_kind == 'promoted_candidate' and decay_score >= live_decay_threshold and support_count == 0 and judged_count == 0:
            rows.append(
                violation(
                    db_entity_type(entry),
                    key,
                    'freshness_promoted_live_item_stale',
                    'medium',
                    {
                        'category': 'freshness',
                        'path': record.get('path'),
                        'lifecycle_stage': stage,
                        'source_kind': source_kind,
                        'decay_score': decay_score,
                        'supporting_case_count': support_count,
                        'judged_case_count': judged_count,
                        'activity_age_days': activity_days,
                    },
                )
            )
        elif stage == 'hold' and decay_score >= hold_decay_threshold and support_count == 0 and judged_count == 0:
            rows.append(
                violation(
                    db_entity_type(entry),
                    key,
                    'freshness_stale_hold_candidate',
                    'low',
                    {
                        'category': 'freshness',
                        'path': record.get('path'),
                        'lifecycle_stage': stage,
                        'decay_score': decay_score,
                        'supporting_case_count': support_count,
                        'judged_case_count': judged_count,
                        'activity_age_days': activity_days,
                    },
                )
            )
        elif stage in {'active', 'trial'} and source_kind == 'promoted_candidate' and activity_days is not None and activity_days >= stale_activity_days and support_count == 0 and judged_count == 0:
            rows.append(
                violation(
                    db_entity_type(entry),
                    key,
                    'freshness_activity_stale',
                    'medium',
                    {
                        'category': 'freshness',
                        'path': record.get('path'),
                        'lifecycle_stage': stage,
                        'source_kind': source_kind,
                        'activity_age_days': round(activity_days, 2),
                        'stale_activity_days_threshold': stale_activity_days,
                        'supporting_case_count': support_count,
                        'judged_case_count': judged_count,
                    },
                )
            )
    return dedupe_violations(rows)



def detect_violations(
    entries: list[dict[str, Any]],
    node_stats: dict[str, dict[str, Any]],
    edge_stats: dict[str, dict[str, Any]],
    *,
    stale_activity_days: float = DEFAULT_STALE_ACTIVITY_DAYS,
    live_decay_threshold: float = DEFAULT_LIVE_DECAY_THRESHOLD,
    hold_decay_threshold: float = DEFAULT_HOLD_DECAY_THRESHOLD,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    rows.extend(detect_structural_violations(entries))
    rows.extend(detect_evidence_violations(entries, node_stats, edge_stats))
    rows.extend(detect_utility_violations(entries, node_stats, edge_stats))
    rows.extend(
        detect_freshness_violations(
            entries,
            node_stats,
            edge_stats,
            stale_activity_days=stale_activity_days,
            live_decay_threshold=live_decay_threshold,
            hold_decay_threshold=hold_decay_threshold,
        )
    )
    return dedupe_violations(rows)



def violation_scope(entries: list[dict[str, Any]]) -> set[tuple[str, str]]:
    return {(db_entity_type(entry), entity_key(entry)) for entry in entries if entity_key(entry)}



def apply_violations(
    violations: list[dict[str, Any]],
    *,
    scope: set[tuple[str, str]],
    db_url: str,
    psql_bin: str,
    dry_run: bool,
) -> dict[str, Any]:
    output = {
        'inserted_count': 0,
        'updated_count': 0,
        'resolved_count': 0,
        'db_actions': [],
    }
    if not db_url or not table_exists('causal_graph_health_violations', db_url=db_url, psql_bin=psql_bin):
        return output

    existing_rows = load_db_rows(OPEN_HEALTH_SQL, db_url=db_url, psql_bin=psql_bin)
    existing_map = {
        (
            str(row.get('entity_type') or ''),
            str(row.get('entity_key') or ''),
            str(row.get('violation_kind') or ''),
        ): row
        for row in existing_rows
        if (str(row.get('entity_type') or ''), str(row.get('entity_key') or '')) in scope
    }
    detected_map = {
        (
            str(row.get('entity_type') or ''),
            str(row.get('entity_key') or ''),
            str(row.get('violation_kind') or ''),
        ): row
        for row in violations
    }

    for key in sorted(detected_map):
        row = detected_map[key]
        existing = existing_map.get(key)
        action = 'update_open' if existing else 'insert_open'
        db_result = None
        if not dry_run:
            if existing:
                db_result = exec_sql(
                    psql_bin,
                    db_url,
                    UPDATE_VIOLATION_SQL,
                    {
                        'row_id': str(existing.get('id') or ''),
                        'severity': str(row.get('severity') or 'medium'),
                        'details_json': json.dumps(row.get('details') or {}),
                    },
                )
                output['updated_count'] += 1
            else:
                db_result = exec_sql(
                    psql_bin,
                    db_url,
                    INSERT_VIOLATION_SQL,
                    {
                        'entity_type': row['entity_type'],
                        'entity_key': row['entity_key'],
                        'violation_kind': row['violation_kind'],
                        'severity': row['severity'],
                        'details_json': json.dumps(row.get('details') or {}),
                    },
                )
                output['inserted_count'] += 1
        output['db_actions'].append({'action': action, 'key': key, 'db_result': db_result})

    for key in sorted(existing_map):
        if key in detected_map:
            continue
        existing = existing_map[key]
        db_result = None
        if not dry_run:
            db_result = exec_sql(
                psql_bin,
                db_url,
                RESOLVE_VIOLATION_SQL,
                {'row_id': str(existing.get('id') or '')},
            )
            output['resolved_count'] += 1
        output['db_actions'].append({'action': 'resolve', 'key': key, 'db_result': db_result})

    return output



def main() -> int:
    args = parse_args()
    entries = load_entries(args)
    resolved_db_url = resolve_db_url(args.db_url)
    node_stats_present = bool(resolved_db_url) and table_exists('causal_node_stats', db_url=resolved_db_url, psql_bin=args.psql)
    edge_stats_present = bool(resolved_db_url) and table_exists('causal_edge_stats', db_url=resolved_db_url, psql_bin=args.psql)
    health_present = bool(resolved_db_url) and table_exists('causal_graph_health_violations', db_url=resolved_db_url, psql_bin=args.psql)

    node_stats_rows = load_db_rows(NODE_STATS_SQL, db_url=resolved_db_url, psql_bin=args.psql) if node_stats_present else []
    edge_stats_rows = load_db_rows(EDGE_STATS_SQL, db_url=resolved_db_url, psql_bin=args.psql) if edge_stats_present else []
    node_stats = {str(row.get('node_key') or ''): row for row in node_stats_rows if str(row.get('node_key') or '').strip()}
    edge_stats = {str(row.get('edge_key') or ''): row for row in edge_stats_rows if str(row.get('edge_key') or '').strip()}

    violations = detect_violations(
        entries,
        node_stats,
        edge_stats,
        stale_activity_days=args.stale_activity_days,
        live_decay_threshold=args.live_decay_threshold,
        hold_decay_threshold=args.hold_decay_threshold,
    )

    warnings: list[str] = []
    if not resolved_db_url:
        warnings.append('db_url_unavailable')
    if resolved_db_url and not node_stats_present:
        warnings.append('causal_node_stats_table_missing')
    if resolved_db_url and not edge_stats_present:
        warnings.append('causal_edge_stats_table_missing')
    if resolved_db_url and not health_present:
        warnings.append('causal_graph_health_violations_table_missing')

    persistence = apply_violations(
        violations,
        scope=violation_scope(entries),
        db_url=resolved_db_url,
        psql_bin=args.psql,
        dry_run=args.dry_run,
    )

    class_counts = Counter(str(row.get('violation_kind') or '').split('_', 1)[0] for row in violations)
    severity_counts = Counter(str(row.get('severity') or 'low') for row in violations)
    output = {
        'ok': True,
        'dry_run': args.dry_run,
        'entry_count': len(entries),
        'violation_count': len(violations),
        'violation_class_counts': dict(sorted(class_counts.items())),
        'severity_counts': dict(sorted(severity_counts.items())),
        'stats_presence': {
            'causal_node_stats': node_stats_present,
            'causal_edge_stats': edge_stats_present,
            'causal_graph_health_violations': health_present,
        },
        'warnings': warnings,
        'violations': violations,
        'persistence': persistence,
    }
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
