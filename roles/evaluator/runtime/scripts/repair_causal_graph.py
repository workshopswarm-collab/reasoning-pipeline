#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
SCRIPTS_DIR = SCRIPT_PATH.parent
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.append(str(SCRIPTS_DIR))

from lib.db import DEFAULT_PSQL, resolve_db_url, table_exists  # noqa: E402
from lib.io import parse_frontmatter, read_json, read_text, strip_frontmatter, write_json  # noqa: E402
import advance_live_causal_graph_items as live_controller  # noqa: E402
import scan_causal_graph_health as health_scan  # noqa: E402
import upsert_causal_edges  # noqa: E402
import upsert_causal_nodes  # noqa: E402

SCRIPT_NAME = SCRIPT_PATH.name
DEFAULT_MAX_ACTIONS = 25
DEFAULT_SCAN_FIRST = True
HOLD_TRIGGER_KINDS = {
    'structural_missing_edge_endpoint',
    'structural_edge_endpoint_stage_mismatch',
    'evidence_missing_review_paths',
    'evidence_reviewed_live_edge_without_support',
    'evidence_live_promoted_node_without_support',
    'evidence_live_promoted_edge_without_support',
    'utility_live_stage_conflicts_with_stats',
    'utility_negative_live_item',
    'freshness_promoted_live_item_stale',
    'freshness_activity_stale',
}
RETIRE_TRIGGER_KINDS = {
    'freshness_stale_hold_candidate',
}
ALIGN_STATUS_TRIGGER_KINDS = {
    'structural_status_stage_mismatch',
}
REGENERATE_SIDECAR_TRIGGER_KINDS = {
    'structural_missing_sidecar',
}
DEFERRED_SUGGESTIONS = {
    'evidence_missing_review_paths': 'manual_evidence_review',
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Apply low-risk repairs to live causal graph items based on current health-scan violations')
    parser.add_argument('--node-key', action='append', default=[])
    parser.add_argument('--edge-key', action='append', default=[])
    parser.add_argument('--mechanism-family', action='append', default=[])
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--stale-activity-days', type=float, default=health_scan.DEFAULT_STALE_ACTIVITY_DAYS)
    parser.add_argument('--live-decay-threshold', type=float, default=health_scan.DEFAULT_LIVE_DECAY_THRESHOLD)
    parser.add_argument('--hold-decay-threshold', type=float, default=health_scan.DEFAULT_HOLD_DECAY_THRESHOLD)
    parser.add_argument('--apply', action='store_true', help='Persist low-risk repairs; preview-only by default')
    parser.add_argument('--max-actions', type=int, default=DEFAULT_MAX_ACTIONS)
    parser.add_argument('--scan-first', action='store_true', default=DEFAULT_SCAN_FIRST, help='Refresh health-violation table after repairs (and preview those updates when not applying)')
    parser.add_argument('--skip-scan-first', dest='scan_first', action='store_false')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')



def entry_key(entry: dict[str, Any]) -> tuple[str, str]:
    return live_controller.db_entity_type(entry), live_controller.entity_key(entry)



def severity_rank(value: str) -> int:
    return health_scan.SEVERITY_RANK.get(str(value or 'low'), 1)



def summarize_violations(rows: list[dict[str, Any]]) -> dict[str, Any]:
    class_counts = Counter(str(row.get('violation_kind') or '').split('_', 1)[0] for row in rows)
    severity_counts = Counter(str(row.get('severity') or 'low') for row in rows)
    return {
        'violation_count': len(rows),
        'violation_class_counts': dict(sorted(class_counts.items())),
        'severity_counts': dict(sorted(severity_counts.items())),
    }



def load_stats_maps(*, db_url: str, psql_bin: str) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, bool]]:
    node_stats_present = bool(db_url) and table_exists('causal_node_stats', db_url=db_url, psql_bin=psql_bin)
    edge_stats_present = bool(db_url) and table_exists('causal_edge_stats', db_url=db_url, psql_bin=psql_bin)
    health_present = bool(db_url) and table_exists('causal_graph_health_violations', db_url=db_url, psql_bin=psql_bin)

    node_rows = health_scan.load_db_rows(health_scan.NODE_STATS_SQL, db_url=db_url, psql_bin=psql_bin) if node_stats_present else []
    edge_rows = health_scan.load_db_rows(health_scan.EDGE_STATS_SQL, db_url=db_url, psql_bin=psql_bin) if edge_stats_present else []
    node_stats = {str(row.get('node_key') or ''): row for row in node_rows if str(row.get('node_key') or '').strip()}
    edge_stats = {str(row.get('edge_key') or ''): row for row in edge_rows if str(row.get('edge_key') or '').strip()}
    return node_stats, edge_stats, {
        'causal_node_stats': node_stats_present,
        'causal_edge_stats': edge_stats_present,
        'causal_graph_health_violations': health_present,
    }



def current_violations(
    entries: list[dict[str, Any]],
    *,
    node_stats: dict[str, dict[str, Any]],
    edge_stats: dict[str, dict[str, Any]],
    args: argparse.Namespace,
) -> list[dict[str, Any]]:
    return health_scan.detect_violations(
        entries,
        node_stats,
        edge_stats,
        stale_activity_days=args.stale_activity_days,
        live_decay_threshold=args.live_decay_threshold,
        hold_decay_threshold=args.hold_decay_threshold,
    )



def highest_severity(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return 'low'
    return max((str(row.get('severity') or 'low') for row in rows), key=severity_rank)



def repair_reason(repair_kind: str, triggering_rows: list[dict[str, Any]]) -> str:
    kinds = sorted({str(row.get('violation_kind') or '') for row in triggering_rows if str(row.get('violation_kind') or '').strip()})
    rendered = '+'.join(kinds[:4]) if kinds else 'health_violation'
    return f'{SCRIPT_NAME}:{repair_kind}:{rendered}'



def sidecar_file_path(entry: dict[str, Any]) -> Path:
    return Path(entry['note_path']).with_suffix('.json')



def sidecar_preview_path(entry: dict[str, Any]) -> str:
    record = entry.get('record') or {}
    return str(record.get('sidecar_path') or '') or str(sidecar_file_path(entry))



def synthesize_sidecar(entry: dict[str, Any], record: dict[str, Any], existing: dict[str, Any] | None = None) -> dict[str, Any]:
    stage = live_controller.lifecycle_stage(record)
    status = str(record.get('status') or live_controller.STATUS_BY_STAGE.get(stage, stage)).strip()
    data = dict(existing or {})
    if live_controller.entry_entity_type(entry) == 'node':
        data.update({
            'artifact_type': 'causal_node',
            'schema_version': 'v1',
            'node_key': record.get('node_key'),
            'contexts': record.get('contexts') or {},
            'linked_paths': record.get('linked_paths') or {},
            'tags': record.get('tags') or [],
            'mechanism_family': record.get('mechanism_family') or 'unassigned',
            'source_kind': record.get('source_kind') or 'unknown',
            'lifecycle_stage': stage,
            'status': status,
            'promotion_score': record.get('promotion_score') if record.get('promotion_score') not in (None, '') else 0.0,
            'last_seen_at': record.get('last_seen_at') or '',
            'last_matched_at': record.get('last_matched_at') or '',
            'last_injected_at': record.get('last_injected_at') or '',
            'last_helpful_at': record.get('last_helpful_at') or '',
            'decay_score': record.get('decay_score') if record.get('decay_score') not in (None, '') else 0.0,
            'demotion_reason': record.get('demotion_reason') or '',
            'superseded_by_key': record.get('superseded_by_key') or '',
        })
        return data
    data.update({
        'artifact_type': 'causal_edge',
        'schema_version': 'v1',
        'edge_key': record.get('edge_key'),
        'source_node_key': record.get('source_node_key') or '',
        'target_node_key': record.get('target_node_key') or '',
        'effect_sign': record.get('effect_sign') or '',
        'contexts': record.get('contexts') or {},
        'linked_intervention_keys': record.get('linked_intervention_keys') or [],
        'evidence_paths': record.get('evidence_paths') or [],
        'evidence_rows': data.get('evidence_rows') if isinstance(data.get('evidence_rows'), list) else [],
        'mechanism_family': record.get('mechanism_family') or 'unassigned',
        'source_kind': record.get('source_kind') or 'unknown',
        'lifecycle_stage': stage,
        'status': status,
        'confidence_mode': record.get('confidence_mode') or '',
        'confidence_prior': record.get('confidence_prior') if record.get('confidence_prior') not in (None, '') else None,
        'promotion_score': record.get('promotion_score') if record.get('promotion_score') not in (None, '') else 0.0,
        'last_seen_at': record.get('last_seen_at') or '',
        'last_matched_at': record.get('last_matched_at') or '',
        'last_injected_at': record.get('last_injected_at') or '',
        'last_helpful_at': record.get('last_helpful_at') or '',
        'decay_score': record.get('decay_score') if record.get('decay_score') not in (None, '') else 0.0,
        'demotion_reason': record.get('demotion_reason') or '',
        'superseded_by_key': record.get('superseded_by_key') or '',
    })
    return data



def rebuild_entry_record(entry: dict[str, Any]) -> dict[str, Any]:
    note_path = Path(entry['note_path'])
    if live_controller.entry_entity_type(entry) == 'node':
        updated = live_controller.build_node_record(note_path)
    else:
        updated = live_controller.build_edge_record(note_path)
    entry['record'] = updated
    return updated



def persist_rebuilt_record(entry: dict[str, Any], *, db_url: str, psql_bin: str) -> dict[str, Any]:
    record = entry.get('record') or {}
    if live_controller.entry_entity_type(entry) == 'node':
        return upsert_causal_nodes.persist_record(record, db_url=db_url, psql_bin=psql_bin)
    return upsert_causal_edges.persist_record(record, db_url=db_url, psql_bin=psql_bin)



def apply_status_alignment(entry: dict[str, Any], *, reason: str, apply: bool, db_url: str, psql_bin: str) -> dict[str, Any]:
    record = entry.get('record') or {}
    current_stage = live_controller.lifecycle_stage(record)
    target_status = live_controller.STATUS_BY_STAGE.get(current_stage, current_stage)
    note_path = Path(entry['note_path'])
    sidecar_path = sidecar_file_path(entry)
    preview = {
        'status': 'dry_run' if not apply else 'updated',
        'target_status': target_status,
        'reason': reason,
        'sidecar_path': sidecar_preview_path(entry),
    }
    if not apply:
        return preview

    note_text = read_text(note_path)
    frontmatter = parse_frontmatter(note_text)
    frontmatter['status'] = target_status
    note_path.write_text(live_controller.render_note(frontmatter, strip_frontmatter(note_text)), encoding='utf-8')

    existing_sidecar = read_json(sidecar_path, default={}) or {}
    working_record = dict(record)
    working_record['status'] = target_status
    working_record['lifecycle_stage'] = current_stage
    write_json(sidecar_path, synthesize_sidecar(entry, working_record, existing_sidecar), pretty=True)

    updated_record = rebuild_entry_record(entry)
    preview['persist_result'] = persist_rebuilt_record(entry, db_url=db_url, psql_bin=psql_bin)
    preview['updated_record'] = {
        'status': updated_record.get('status'),
        'lifecycle_stage': updated_record.get('lifecycle_stage'),
        'sidecar_path': updated_record.get('sidecar_path'),
    }
    return preview



def apply_sidecar_regeneration(entry: dict[str, Any], *, reason: str, apply: bool, db_url: str, psql_bin: str) -> dict[str, Any]:
    record = entry.get('record') or {}
    sidecar_path = sidecar_file_path(entry)
    preview = {
        'status': 'dry_run' if not apply else 'updated',
        'reason': reason,
        'sidecar_path': str(sidecar_path),
    }
    if not apply:
        return preview

    existing_sidecar = read_json(sidecar_path, default={}) or {}
    write_json(sidecar_path, synthesize_sidecar(entry, record, existing_sidecar), pretty=True)
    updated_record = rebuild_entry_record(entry)
    preview['persist_result'] = persist_rebuilt_record(entry, db_url=db_url, psql_bin=psql_bin)
    preview['updated_record'] = {
        'status': updated_record.get('status'),
        'lifecycle_stage': updated_record.get('lifecycle_stage'),
        'sidecar_path': updated_record.get('sidecar_path'),
    }
    return preview



def cascade_edge_hold_repairs(entries: list[dict[str, Any]], planned: list[dict[str, Any]]) -> list[dict[str, Any]]:
    planned_by_key = {entry_key(row['entry']): row for row in planned}
    endpoint_repairs = {
        live_controller.entity_key(row['entry']): row
        for row in planned
        if live_controller.entry_entity_type(row['entry']) == 'node'
        and str(row.get('target_stage') or '').strip() in {'hold', 'retired', 'archived'}
    }
    cascaded: list[dict[str, Any]] = []
    if not endpoint_repairs:
        return cascaded

    for entry in entries:
        if live_controller.entry_entity_type(entry) != 'edge':
            continue
        key = entry_key(entry)
        if key in planned_by_key:
            continue
        record = entry.get('record') or {}
        if live_controller.lifecycle_stage(record) not in {'active', 'trial'}:
            continue
        endpoint_hits = [
            endpoint_key
            for endpoint_key in [
                str(record.get('source_node_key') or '').strip(),
                str(record.get('target_node_key') or '').strip(),
            ]
            if endpoint_key and endpoint_key in endpoint_repairs
        ]
        if not endpoint_hits:
            continue
        triggering = [
            {
                'entity_type': 'causal_edge',
                'entity_key': live_controller.entity_key(entry),
                'violation_kind': 'structural_edge_endpoint_stage_mismatch',
                'severity': endpoint_repairs[endpoint_key].get('severity') or 'medium',
                'status': 'open',
                'details': {
                    'category': 'structural',
                    'cascade_from_endpoint_key': endpoint_key,
                    'cascade_target_stage': endpoint_repairs[endpoint_key].get('target_stage'),
                },
            }
            for endpoint_key in sorted(set(endpoint_hits))
        ]
        cascaded.append({
            'entry': entry,
            'repair_kind': 'mark_hold',
            'target_stage': 'hold',
            'reason': f"{SCRIPT_NAME}:cascade_hold:endpoint_stage_change:{'+'.join(sorted(set(endpoint_hits))[:4])}",
            'severity': highest_severity(triggering),
            'triggering_violations': triggering,
        })
    return cascaded



def build_repair_plan(entries: list[dict[str, Any]], violations: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    entry_map = {entry_key(entry): entry for entry in entries if entry_key(entry)[1]}
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in violations:
        key = (str(row.get('entity_type') or ''), str(row.get('entity_key') or ''))
        if key in entry_map:
            grouped.setdefault(key, []).append(row)

    planned: list[dict[str, Any]] = []
    deferred: list[dict[str, Any]] = []
    for key, entry in entry_map.items():
        rows = grouped.get(key) or []
        if not rows:
            continue
        record = entry.get('record') or {}
        stage = live_controller.lifecycle_stage(record)
        kinds = {str(row.get('violation_kind') or '') for row in rows}
        severity = highest_severity(rows)

        if stage == 'hold' and RETIRE_TRIGGER_KINDS.intersection(kinds):
            triggering = [row for row in rows if str(row.get('violation_kind') or '') in RETIRE_TRIGGER_KINDS]
            planned.append({
                'entry': entry,
                'repair_kind': 'retire_stale_item',
                'target_stage': 'retired',
                'reason': repair_reason('retire_stale_item', triggering),
                'severity': highest_severity(triggering),
                'triggering_violations': triggering,
            })
            continue

        if stage in {'active', 'trial'} and HOLD_TRIGGER_KINDS.intersection(kinds):
            triggering = [row for row in rows if str(row.get('violation_kind') or '') in HOLD_TRIGGER_KINDS]
            planned.append({
                'entry': entry,
                'repair_kind': 'mark_hold',
                'target_stage': 'hold',
                'reason': repair_reason('mark_hold', triggering),
                'severity': highest_severity(triggering),
                'triggering_violations': triggering,
            })
            continue

        if ALIGN_STATUS_TRIGGER_KINDS.intersection(kinds):
            triggering = [row for row in rows if str(row.get('violation_kind') or '') in ALIGN_STATUS_TRIGGER_KINDS | REGENERATE_SIDECAR_TRIGGER_KINDS]
            planned.append({
                'entry': entry,
                'repair_kind': 'align_status_to_stage',
                'target_stage': stage,
                'reason': repair_reason('align_status_to_stage', triggering),
                'severity': highest_severity(triggering),
                'triggering_violations': triggering,
            })
            continue

        if REGENERATE_SIDECAR_TRIGGER_KINDS.intersection(kinds):
            triggering = [row for row in rows if str(row.get('violation_kind') or '') in REGENERATE_SIDECAR_TRIGGER_KINDS]
            planned.append({
                'entry': entry,
                'repair_kind': 'regenerate_sidecar',
                'target_stage': stage,
                'reason': repair_reason('regenerate_sidecar', triggering),
                'severity': highest_severity(triggering),
                'triggering_violations': triggering,
            })
            continue

        suggestions = sorted({
            DEFERRED_SUGGESTIONS[str(row.get('violation_kind') or '')]
            for row in rows
            if str(row.get('violation_kind') or '') in DEFERRED_SUGGESTIONS
        })
        if suggestions:
            deferred.append({
                'entity_type': key[0],
                'entity_key': key[1],
                'current_stage': stage,
                'severity': severity,
                'suggestions': suggestions,
                'violations': rows,
            })

    planned.extend(cascade_edge_hold_repairs(entries, planned))
    planned = sorted(
        planned,
        key=lambda row: (
            row['repair_kind'] not in {'retire_stale_item', 'mark_hold'},
            row['target_stage'] != 'retired',
            -severity_rank(row['severity']),
            entry_key(row['entry'])[0],
            entry_key(row['entry'])[1],
        ),
    )
    deferred = sorted(deferred, key=lambda row: (-severity_rank(row['severity']), row['entity_type'], row['entity_key']))
    return planned, deferred



def simulate_repairs(entries: list[dict[str, Any]], repairs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    copied = copy.deepcopy(entries)
    repair_by_key = {entry_key(row['entry']): row for row in repairs}
    for entry in copied:
        row = repair_by_key.get(entry_key(entry))
        if row is None:
            continue
        record = entry.setdefault('record', {})
        if row['repair_kind'] in {'mark_hold', 'retire_stale_item'}:
            target_stage = str(row.get('target_stage') or '').strip()
            if target_stage:
                record['lifecycle_stage'] = target_stage
                record['status'] = live_controller.STATUS_BY_STAGE.get(target_stage, target_stage)
        elif row['repair_kind'] == 'align_status_to_stage':
            stage = live_controller.lifecycle_stage(record)
            record['status'] = live_controller.STATUS_BY_STAGE.get(stage, stage)
        if row['repair_kind'] in {'align_status_to_stage', 'regenerate_sidecar', 'mark_hold', 'retire_stale_item'}:
            record['sidecar_path'] = sidecar_preview_path(entry)
        record['repair_reason'] = row.get('reason')
    return copied



def render_repair_preview(row: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    entry = row['entry']
    record = entry.get('record') or {}
    return {
        'repair_kind': row['repair_kind'],
        'entity_type': live_controller.db_entity_type(entry),
        'entity_key': live_controller.entity_key(entry),
        'mechanism_family': record.get('mechanism_family'),
        'from_stage': live_controller.lifecycle_stage(record),
        'to_stage': row.get('target_stage') or live_controller.lifecycle_stage(record),
        'severity': row['severity'],
        'reason': row['reason'],
        'triggering_violation_kinds': sorted({str(item.get('violation_kind') or '') for item in row.get('triggering_violations') or []}),
        'result': result,
    }



def apply_repairs(
    repairs: list[dict[str, Any]],
    *,
    db_url: str,
    psql_bin: str,
    apply: bool,
) -> list[dict[str, Any]]:
    transitioned_at = now_iso()
    out: list[dict[str, Any]] = []
    for row in repairs:
        if row['repair_kind'] in {'mark_hold', 'retire_stale_item'}:
            result = live_controller.apply_transition(
                row['entry'],
                target_stage=row['target_stage'],
                reason=row['reason'],
                transitioned_at=transitioned_at,
                db_url=db_url,
                psql_bin=psql_bin,
                apply=apply,
            )
        elif row['repair_kind'] == 'align_status_to_stage':
            result = apply_status_alignment(row['entry'], reason=row['reason'], apply=apply, db_url=db_url, psql_bin=psql_bin)
        elif row['repair_kind'] == 'regenerate_sidecar':
            result = apply_sidecar_regeneration(row['entry'], reason=row['reason'], apply=apply, db_url=db_url, psql_bin=psql_bin)
        else:
            result = {'status': 'skipped', 'reason': f'unknown_repair_kind:{row["repair_kind"]}'}
        out.append(render_repair_preview(row, result))
    return out



def main() -> int:
    args = parse_args()
    entries = health_scan.load_entries(args)
    resolved_db_url = resolve_db_url(args.db_url)
    if args.apply and not resolved_db_url:
        raise SystemExit('db_url unavailable; refusing to apply repairs without DB connectivity')

    node_stats, edge_stats, stats_presence = load_stats_maps(db_url=resolved_db_url, psql_bin=args.psql)
    warnings: list[str] = []
    if not resolved_db_url:
        warnings.append('db_url_unavailable')
    if resolved_db_url and not stats_presence['causal_node_stats']:
        warnings.append('causal_node_stats_table_missing')
    if resolved_db_url and not stats_presence['causal_edge_stats']:
        warnings.append('causal_edge_stats_table_missing')
    if resolved_db_url and not stats_presence['causal_graph_health_violations']:
        warnings.append('causal_graph_health_violations_table_missing')

    pre_violations = current_violations(entries, node_stats=node_stats, edge_stats=edge_stats, args=args)
    repairs, deferred = build_repair_plan(entries, pre_violations)

    if args.apply and len(repairs) > args.max_actions:
        print(json.dumps({
            'ok': False,
            'warning': 'recommended_repair_count_exceeds_max_actions',
            'repair_count': len(repairs),
            'max_actions': args.max_actions,
        }, indent=2 if args.pretty else None))
        return 1

    repair_results = apply_repairs(repairs, db_url=resolved_db_url, psql_bin=args.psql, apply=args.apply)
    post_entries = entries if args.apply else simulate_repairs(entries, repairs)
    post_violations = current_violations(post_entries, node_stats=node_stats, edge_stats=edge_stats, args=args)

    persistence = None
    if args.scan_first:
        persistence = health_scan.apply_violations(
            post_violations,
            scope=health_scan.violation_scope(post_entries),
            db_url=resolved_db_url,
            psql_bin=args.psql,
            dry_run=not args.apply,
        )

    output = {
        'ok': True,
        'apply': args.apply,
        'scan_first': args.scan_first,
        'entry_count': len(entries),
        'warnings': warnings,
        'stats_presence': stats_presence,
        'pre_repair': summarize_violations(pre_violations),
        'post_repair_projection': summarize_violations(post_violations),
        'repair_count': len(repairs),
        'deferred_count': len(deferred),
        'repairs': repair_results,
        'deferred': deferred,
        'violations_before': pre_violations,
        'violations_after_projection': post_violations,
        'health_table_reconciliation': persistence,
    }
    if not args.apply:
        output['note'] = 'preview mode only; projected post-repair violations are computed in memory and no lifecycle or health-table writes are persisted'
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
