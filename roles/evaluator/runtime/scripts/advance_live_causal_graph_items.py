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

from lib.causal_family_policy import load_effective_family_policies  # noqa: E402
from lib.causal_map import build_edge_record, build_node_record, edge_note_paths, node_note_paths  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.io import parse_frontmatter, read_json, read_text, strip_frontmatter, write_json  # noqa: E402
from lib.paths import to_repo_relative  # noqa: E402
from scripts.upsert_causal_edges import persist_record as persist_edge_record  # noqa: E402
from scripts.upsert_causal_nodes import persist_record as persist_node_record  # noqa: E402

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    yaml = None

SCRIPT_NAME = SCRIPT_PATH.name
DEFAULT_MAX_ACTIONS = 50
STATUS_BY_STAGE = {
    'draft': 'draft',
    'trial': 'active',
    'active': 'active',
    'hold': 'hold',
    'retired': 'retired',
    'archived': 'archived',
}
EVENT_KIND_BY_TRANSITION = {
    ('draft', 'trial'): 'advanced_to_trial',
    ('trial', 'active'): 'promoted_to_active',
    ('active', 'hold'): 'demoted_to_hold',
    ('trial', 'hold'): 'demoted_to_hold',
    ('draft', 'hold'): 'demoted_to_hold',
    ('hold', 'retired'): 'retired',
    ('trial', 'retired'): 'retired',
    ('active', 'retired'): 'retired',
    ('retired', 'archived'): 'archived',
}

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
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY entity_type, entity_key), '[]'::json)::text
FROM (
  SELECT
    entity_type,
    entity_key,
    COUNT(*)::int AS open_violation_count,
    BOOL_OR(COALESCE(NULLIF(severity, ''), 'low') IN ('high', 'critical')) AS has_high_severity
  FROM public.causal_graph_health_violations
  WHERE COALESCE(NULLIF(status, ''), 'open') NOT IN ('resolved', 'closed')
  GROUP BY entity_type, entity_key
) t;
'''

EVENT_COLUMNS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t) ORDER BY ordinal_position), '[]'::json)::text
FROM (
  SELECT column_name, data_type, ordinal_position
  FROM information_schema.columns
  WHERE table_schema = 'public'
    AND table_name = 'causal_graph_lifecycle_events'
) t;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Advance live causal graph items through bounded lifecycle transitions')
    parser.add_argument('--node-key', action='append', default=[])
    parser.add_argument('--edge-key', action='append', default=[])
    parser.add_argument('--mechanism-family', action='append', default=[])
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--apply', action='store_true', help='Persist recommended transitions; default is preview only')
    parser.add_argument('--max-actions', type=int, default=DEFAULT_MAX_ACTIONS)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')



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



def entry_entity_type(entry: dict[str, Any]) -> str:
    return 'node' if entry.get('entity_type') == 'node' else 'edge'



def db_entity_type(entry: dict[str, Any]) -> str:
    return 'causal_node' if entry_entity_type(entry) == 'node' else 'causal_edge'



def entity_key(entry: dict[str, Any]) -> str:
    record = entry.get('record') or {}
    if entry_entity_type(entry) == 'node':
        return str(record.get('node_key') or '').strip()
    return str(record.get('edge_key') or '').strip()



def lifecycle_stage(record: dict[str, Any]) -> str:
    stage = str(record.get('lifecycle_stage') or '').strip().lower()
    if stage:
        return stage
    status = str(record.get('status') or '').strip().lower()
    if status in STATUS_BY_STAGE:
        return status
    return 'draft'



def family_key(record: dict[str, Any]) -> str:
    return str(record.get('mechanism_family') or 'unassigned').strip() or 'unassigned'



def stats_key(entry: dict[str, Any]) -> str:
    return entity_key(entry)



def helpful_case_count(stats: dict[str, Any]) -> int:
    metadata = stats.get('stats_metadata') or {}
    if not isinstance(metadata, dict):
        metadata = {}
    return safe_int(stats.get('helpful_case_count'), metadata.get('helpful_case_count'))



def harmful_case_count(stats: dict[str, Any]) -> int:
    metadata = stats.get('stats_metadata') or {}
    if not isinstance(metadata, dict):
        metadata = {}
    return safe_int(metadata.get('harmful_case_count'))



def judged_case_count(stats: dict[str, Any]) -> int:
    return max(safe_int(stats.get('exposure_count')), safe_int(stats.get('treatment_case_count')))



def support_case_count(stats: dict[str, Any]) -> int:
    return max(
        safe_int(stats.get('supporting_case_count')),
        safe_int(stats.get('matched_case_count')),
        safe_int(stats.get('projected_case_count')),
    )



def transition_rank(entry: dict[str, Any], stats: dict[str, Any]) -> float:
    score = 0.0
    score += safe_float(stats.get('learned_weight'))
    score += safe_float(stats.get('shrunken_uplift')) * 8.0
    score += support_case_count(stats) * 0.08
    score += helpful_case_count(stats) * 0.12
    score -= safe_int(stats.get('contested_case_count')) * 0.14
    score -= safe_float((entry.get('record') or {}).get('decay_score')) * 0.25
    score += safe_float((entry.get('record') or {}).get('promotion_score')) * 0.1
    return round(score, 6)



def build_family_state(entries: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    state: dict[str, dict[str, int]] = {}
    for entry in entries:
        record = entry.get('record') or {}
        family = family_key(record)
        stage = lifecycle_stage(record)
        row = state.setdefault(family, {'trial_total': 0, 'active_nodes': 0, 'active_edges': 0})
        if stage == 'trial':
            row['trial_total'] += 1
        if stage == 'active':
            if entry_entity_type(entry) == 'node':
                row['active_nodes'] += 1
            else:
                row['active_edges'] += 1
    return state



def apply_family_state_transition(state: dict[str, dict[str, int]], family: str, entity_type: str, from_stage: str, to_stage: str) -> None:
    row = state.setdefault(family, {'trial_total': 0, 'active_nodes': 0, 'active_edges': 0})
    if from_stage == 'trial':
        row['trial_total'] = max(0, row['trial_total'] - 1)
    if from_stage == 'active':
        key = 'active_nodes' if entity_type == 'node' else 'active_edges'
        row[key] = max(0, row[key] - 1)
    if to_stage == 'trial':
        row['trial_total'] += 1
    if to_stage == 'active':
        key = 'active_nodes' if entity_type == 'node' else 'active_edges'
        row[key] += 1



def slot_limit(policy: dict[str, Any], *, target_stage: str, entity_type: str) -> int:
    if target_stage == 'trial':
        return safe_int(policy.get('max_trial_candidates'))
    if target_stage == 'active':
        return safe_int(policy.get('max_active_nodes') if entity_type == 'node' else policy.get('max_active_edges'))
    return 0



def slot_key_for_target(target_stage: str, entity_type: str) -> str:
    if target_stage == 'trial':
        return 'trial_total'
    return 'active_nodes' if entity_type == 'node' else 'active_edges'



def open_violation_summary(violations: dict[tuple[str, str], dict[str, Any]], entry: dict[str, Any]) -> dict[str, Any]:
    return violations.get((db_entity_type(entry), entity_key(entry)), {'open_violation_count': 0, 'has_high_severity': False})



def qualifies_for_trial(entry: dict[str, Any], stats: dict[str, Any], policy: dict[str, Any], violation_summary: dict[str, Any]) -> list[str]:
    blockers: list[str] = []
    record = entry.get('record') or {}
    stage = lifecycle_stage(record)
    notes = policy.get('notes') if isinstance(policy.get('notes'), dict) else {}
    reactivation = notes.get('reactivation') if isinstance(notes.get('reactivation'), dict) else {}
    if stage not in {'draft', 'hold'}:
        blockers.append('not_in_draft_stage')
    if not bool(policy.get('enabled', True)):
        blockers.append('family_policy_disabled')
    if bool(notes.get('quarantined')) or bool(notes.get('freeze_promotions')):
        blockers.append('family_quarantined')
    if stage == 'hold' and not bool(reactivation.get('enabled')):
        blockers.append('hold_reactivation_disabled')
    if safe_int(violation_summary.get('open_violation_count')) > 0:
        blockers.append('open_health_violations')
    min_support = safe_int(policy.get('min_non_intervention_support_cases_for_trial'))
    if stage == 'hold' and reactivation:
        min_support = max(min_support, safe_int(reactivation.get('min_support_cases'), min_support))
    if support_case_count(stats) < min_support:
        blockers.append('insufficient_support_cases_for_trial')
    if max(safe_float(stats.get('learned_weight')), safe_float(stats.get('shrunken_uplift'))) <= 0:
        blockers.append('nonpositive_learned_weight')
    if safe_int(stats.get('contested_case_count')) > max(1, support_case_count(stats) // 2):
        blockers.append('too_much_contestation_for_trial')
    decay_limit = 0.8 if stage != 'hold' else safe_float(reactivation.get('max_decay_score'), 0.75)
    if safe_float(record.get('decay_score')) >= decay_limit:
        blockers.append('decay_too_high_for_trial')
    if str(record.get('superseded_by_key') or '').strip():
        blockers.append('superseded_by_key_present')
    return blockers



def qualifies_for_active(entry: dict[str, Any], stats: dict[str, Any], policy: dict[str, Any], violation_summary: dict[str, Any]) -> list[str]:
    blockers: list[str] = []
    record = entry.get('record') or {}
    notes = policy.get('notes') if isinstance(policy.get('notes'), dict) else {}
    if lifecycle_stage(record) != 'trial':
        blockers.append('not_in_trial_stage')
    if not bool(policy.get('enabled', True)):
        blockers.append('family_policy_disabled')
    if bool(notes.get('quarantined')) or bool(notes.get('freeze_promotions')):
        blockers.append('family_quarantined')
    if safe_int(violation_summary.get('open_violation_count')) > 0:
        blockers.append('open_health_violations')
    if judged_case_count(stats) < safe_int(policy.get('min_trial_judged_count_for_promotion')):
        blockers.append('insufficient_trial_judged_count')
    if helpful_case_count(stats) < safe_int(policy.get('min_trial_helpful_count_for_promotion')):
        blockers.append('insufficient_trial_helpful_count')
    if safe_float(stats.get('shrunken_uplift')) < safe_float(policy.get('min_trial_shrunken_utility_for_promotion')):
        blockers.append('trial_utility_below_threshold')
    judged = judged_case_count(stats)
    harmful_rate = (harmful_case_count(stats) / judged) if judged else 1.0
    if harmful_rate > safe_float(policy.get('max_trial_harmful_rate_for_promotion')):
        blockers.append('harmful_rate_too_high')
    if safe_int(stats.get('contested_case_count')) > safe_int(policy.get('max_contest_case_count_for_promotion')):
        blockers.append('contestation_above_active_threshold')
    if safe_float(record.get('decay_score')) >= 0.8:
        blockers.append('decay_too_high_for_active')
    if str(record.get('superseded_by_key') or '').strip():
        blockers.append('superseded_by_key_present')
    return blockers



def forced_transition(entry: dict[str, Any], stats: dict[str, Any], violation_summary: dict[str, Any]) -> tuple[str, str] | None:
    record = entry.get('record') or {}
    stage = lifecycle_stage(record)
    if not stage:
        return None
    superseded_by_key = str(record.get('superseded_by_key') or '').strip()
    if superseded_by_key and stage != 'retired':
        return 'retired', f'superseded_by:{superseded_by_key}'
    if stage in {'active', 'trial'} and safe_int(violation_summary.get('open_violation_count')) > 0:
        return 'hold', 'open_health_violations'
    if stage in {'active', 'trial'} and judged_case_count(stats) >= 3 and safe_float(stats.get('learned_weight')) < -0.08:
        return 'hold', 'negative_live_utility'
    if stage == 'hold' and (
        (judged_case_count(stats) >= 3 and safe_float(stats.get('learned_weight')) < -0.12)
        or (safe_float(record.get('decay_score')) >= 0.95 and support_case_count(stats) == 0)
    ):
        return 'retired', 'persistent_negative_or_stale_hold_state'
    if stage == 'active' and safe_float(record.get('decay_score')) >= 0.98 and support_case_count(stats) == 0 and judged_case_count(stats) == 0:
        return 'hold', 'stale_nonuse_signal'
    return None



def current_count(state: dict[str, dict[str, int]], family: str, *, target_stage: str, entity_type: str) -> int:
    row = state.get(family) or {'trial_total': 0, 'active_nodes': 0, 'active_edges': 0}
    return safe_int(row.get(slot_key_for_target(target_stage, entity_type)))



def select_ranked_promotions(
    candidates: list[dict[str, Any]],
    *,
    target_stage: str,
    family_state: dict[str, dict[str, int]],
    policies: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    selected: list[dict[str, Any]] = []
    blocked: list[dict[str, Any]] = []
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for candidate in candidates:
        entry = candidate['entry']
        family = family_key(entry.get('record') or {})
        entity_type = entry_entity_type(entry)
        group_key = (family, 'all' if target_stage == 'trial' else entity_type)
        grouped.setdefault(group_key, []).append(candidate)

    for (_, _), rows in grouped.items():
        rows = sorted(rows, key=lambda row: row['score'], reverse=True)
        if not rows:
            continue
        sample_entry = rows[0]['entry']
        family = family_key(sample_entry.get('record') or {})
        entity_type = entry_entity_type(sample_entry)
        policy = policies.get(family) or policies.get('unassigned') or {}
        limit = slot_limit(policy, target_stage=target_stage, entity_type=entity_type)
        already = current_count(family_state, family, target_stage=target_stage, entity_type=entity_type)
        available = max(0, limit - already)
        for row in rows:
            if available > 0:
                selected.append(row)
                available -= 1
                apply_family_state_transition(
                    family_state,
                    family,
                    entry_entity_type(row['entry']),
                    lifecycle_stage((row['entry'].get('record') or {})),
                    target_stage,
                )
            else:
                blocked.append({
                    'entry': row['entry'],
                    'target_stage': target_stage,
                    'reason': f'family_{target_stage}_slots_exhausted',
                    'score': row['score'],
                })
    return selected, blocked



def frontmatter_text(frontmatter: dict[str, Any]) -> str:
    if yaml is not None:
        return yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()

    def render_scalar(value: Any) -> str:
        if value is None:
            return '""'
        if isinstance(value, bool):
            return 'true' if value else 'false'
        if isinstance(value, (int, float)):
            return str(value)
        text = str(value)
        if not text or any(ch in text for ch in [':', '#', '[', ']', '{', '}', '\n']) or text.lower() in {'true', 'false', 'null', 'yes', 'no'}:
            return json.dumps(text)
        return text

    lines: list[str] = []
    for key, value in frontmatter.items():
        if isinstance(value, list):
            lines.append(f'{key}:')
            for item in value:
                lines.append(f'  - {render_scalar(item)}')
            continue
        lines.append(f'{key}: {render_scalar(value)}')
    return '\n'.join(lines)



def render_note(frontmatter: dict[str, Any], body: str) -> str:
    rendered_body = body.lstrip('\n')
    return f"---\n{frontmatter_text(frontmatter)}\n---\n\n{rendered_body}" if rendered_body else f"---\n{frontmatter_text(frontmatter)}\n---\n"



def fetch_event_columns(*, db_url: str, psql_bin: str) -> list[dict[str, Any]]:
    if not db_url or not table_exists('causal_graph_lifecycle_events', db_url=db_url, psql_bin=psql_bin):
        return []
    rows = exec_sql(psql_bin, db_url, EVENT_COLUMNS_SQL, {})
    return rows if isinstance(rows, list) else []



def maybe_log_lifecycle_event(
    *,
    entry: dict[str, Any],
    from_stage: str,
    to_stage: str,
    reason: str,
    transitioned_at: str,
    db_url: str,
    psql_bin: str,
    apply: bool,
) -> dict[str, Any] | None:
    resolved_db_url = resolve_db_url(db_url)
    columns = fetch_event_columns(db_url=resolved_db_url, psql_bin=psql_bin)
    if not columns:
        return None

    record = entry.get('record') or {}
    metadata = {
        'mechanism_family': record.get('mechanism_family'),
        'source_kind': record.get('source_kind'),
        'path': record.get('path'),
        'controller': SCRIPT_NAME,
        'reason': reason,
    }
    scalar_values: dict[str, Any] = {
        'entity_type': db_entity_type(entry),
        'entity_key': entity_key(entry),
        'event_type': EVENT_KIND_BY_TRANSITION.get((from_stage, to_stage), f'transition_{from_stage}_to_{to_stage}'),
        'event_kind': EVENT_KIND_BY_TRANSITION.get((from_stage, to_stage), f'transition_{from_stage}_to_{to_stage}'),
        'event_source': SCRIPT_NAME,
        'from_stage': from_stage,
        'to_stage': to_stage,
        'previous_stage': from_stage,
        'new_stage': to_stage,
        'old_stage': from_stage,
        'reason': reason,
        'created_at': transitioned_at,
        'occurred_at': transitioned_at,
        'recorded_at': transitioned_at,
        'mechanism_family': record.get('mechanism_family'),
        'source_kind': record.get('source_kind'),
        'note_path': record.get('path'),
        'related_entity_key': str(record.get('superseded_by_key') or '').strip(),
    }
    json_values = {
        'metadata': metadata,
        'event_metadata': metadata,
        'details': metadata,
        'notes': metadata,
        'payload': metadata,
    }

    insert_columns: list[str] = []
    value_sql: list[str] = []
    params: dict[str, Any] = {}
    for column in columns:
        name = str(column.get('column_name') or '')
        data_type = str(column.get('data_type') or '')
        if not name or name == 'id':
            continue
        if name in json_values and 'json' in data_type:
            insert_columns.append(name)
            param_name = f'{name}_json'
            value_sql.append(f"COALESCE(NULLIF(:'{param_name}', ''), '{{}}')::jsonb")
            params[param_name] = json.dumps(json_values[name])
            continue
        if name in scalar_values:
            insert_columns.append(name)
            value_sql.append(f":'{name}'")
            value = scalar_values[name]
            params[name] = '' if value is None else str(value)

    if not insert_columns:
        return None

    if not apply:
        return {
            'dry_run': True,
            'entity_key': entity_key(entry),
            'event_kind': scalar_values['event_kind'],
            'columns': insert_columns,
        }

    sql = (
        "WITH inserted AS ("
        f"INSERT INTO public.causal_graph_lifecycle_events ({', '.join(insert_columns)}) "
        f"VALUES ({', '.join(value_sql)}) RETURNING 1"
        ") "
        "SELECT json_build_object('entity_key', NULLIF(:'entity_key', ''), 'event_kind', NULLIF(:'event_kind', ''))::text FROM inserted;"
    )
    return exec_sql(psql_bin, resolved_db_url, sql, params)



def apply_transition(
    entry: dict[str, Any],
    *,
    target_stage: str,
    reason: str,
    transitioned_at: str,
    db_url: str,
    psql_bin: str,
    apply: bool,
) -> dict[str, Any]:
    record = entry.get('record') or {}
    entity_type = entry_entity_type(entry)
    key = entity_key(entry)
    current_stage = lifecycle_stage(record)
    note_path = Path(entry['note_path'])
    sidecar_path = note_path.with_suffix('.json')
    preview = {
        'entity_type': entity_type,
        'entity_key': key,
        'path': record.get('path') or to_repo_relative(note_path),
        'from_stage': current_stage,
        'to_stage': target_stage,
        'from_status': record.get('status'),
        'to_status': STATUS_BY_STAGE.get(target_stage, target_stage),
        'reason': reason,
        'transitioned_at': transitioned_at,
    }
    if current_stage == target_stage:
        preview['status'] = 'skipped'
        preview['skip_reason'] = 'already_in_target_stage'
        return preview

    note_text = read_text(note_path)
    frontmatter = parse_frontmatter(note_text)
    sidecar = read_json(sidecar_path, default={}) or {}
    frontmatter['status'] = STATUS_BY_STAGE.get(target_stage, target_stage)
    frontmatter['lifecycle_stage'] = target_stage
    frontmatter['lifecycle_stage_updated_at'] = transitioned_at
    frontmatter['lifecycle_stage_updated_by'] = SCRIPT_NAME
    frontmatter['lifecycle_transition'] = f'{current_stage}->{target_stage}'
    sidecar['status'] = STATUS_BY_STAGE.get(target_stage, target_stage)
    sidecar['lifecycle_stage'] = target_stage
    sidecar['lifecycle_stage_updated_at'] = transitioned_at
    sidecar['lifecycle_stage_updated_by'] = SCRIPT_NAME
    sidecar['last_stage_transition'] = {
        'event_kind': EVENT_KIND_BY_TRANSITION.get((current_stage, target_stage), f'transition_{current_stage}_to_{target_stage}'),
        'event_source': SCRIPT_NAME,
        'from_stage': current_stage,
        'to_stage': target_stage,
        'occurred_at': transitioned_at,
        'reason': reason,
    }
    sidecar['last_stage_transition_at'] = transitioned_at
    if current_stage == 'draft' and target_stage == 'trial' and str(frontmatter.get('evidence_status') or '').strip() == 'experimental_draft':
        frontmatter['evidence_status'] = 'experimental_trial'
        sidecar['evidence_status'] = 'experimental_trial'
    if target_stage in {'hold', 'retired', 'archived'}:
        frontmatter['demotion_reason'] = reason
        sidecar['demotion_reason'] = reason
    else:
        frontmatter.pop('demotion_reason', None)
        sidecar.pop('demotion_reason', None)

    if not apply:
        preview['status'] = 'dry_run'
        event_row = maybe_log_lifecycle_event(
            entry=entry,
            from_stage=current_stage,
            to_stage=target_stage,
            reason=reason,
            transitioned_at=transitioned_at,
            db_url=db_url,
            psql_bin=psql_bin,
            apply=False,
        )
        if event_row is not None:
            preview['lifecycle_event'] = event_row
        return preview

    note_path.write_text(render_note(frontmatter, strip_frontmatter(note_text)), encoding='utf-8')
    write_json(sidecar_path, sidecar, pretty=True)
    updated_record = build_node_record(note_path) if entity_type == 'node' else build_edge_record(note_path)
    persist_result = (
        persist_node_record(updated_record, db_url=db_url, psql_bin=psql_bin)
        if entity_type == 'node'
        else persist_edge_record(updated_record, db_url=db_url, psql_bin=psql_bin)
    )
    event_row = maybe_log_lifecycle_event(
        entry={'entity_type': entity_type, 'record': updated_record, 'note_path': note_path},
        from_stage=current_stage,
        to_stage=target_stage,
        reason=reason,
        transitioned_at=transitioned_at,
        db_url=db_url,
        psql_bin=psql_bin,
        apply=True,
    )
    preview['status'] = 'updated'
    preview['persist_result'] = persist_result
    if event_row is not None:
        preview['lifecycle_event'] = event_row
    entry['record'] = updated_record
    return preview



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



def controller_preview(entry: dict[str, Any], stats: dict[str, Any], violation_summary: dict[str, Any]) -> dict[str, Any]:
    record = entry.get('record') or {}
    return {
        'entity_type': entry_entity_type(entry),
        'entity_key': entity_key(entry),
        'mechanism_family': family_key(record),
        'current_stage': lifecycle_stage(record),
        'status': record.get('status'),
        'learned_weight': safe_float(stats.get('learned_weight')),
        'shrunken_uplift': safe_float(stats.get('shrunken_uplift')),
        'supporting_case_count': safe_int(stats.get('supporting_case_count')),
        'contested_case_count': safe_int(stats.get('contested_case_count')),
        'judged_case_count': judged_case_count(stats),
        'helpful_case_count': helpful_case_count(stats),
        'open_violation_count': safe_int(violation_summary.get('open_violation_count')),
        'decay_score': safe_float(record.get('decay_score')),
    }



def main() -> int:
    args = parse_args()
    transitioned_at = now_iso()
    if args.apply and args.max_actions <= 0:
        raise SystemExit('--max-actions must be positive when --apply is set')

    entries = load_entries(args)
    resolved_db_url = resolve_db_url(args.db_url)
    policies = load_effective_family_policies(db_url=resolved_db_url, psql_bin=args.psql)
    node_stats_present = bool(resolved_db_url) and table_exists('causal_node_stats', db_url=resolved_db_url, psql_bin=args.psql)
    edge_stats_present = bool(resolved_db_url) and table_exists('causal_edge_stats', db_url=resolved_db_url, psql_bin=args.psql)
    health_present = bool(resolved_db_url) and table_exists('causal_graph_health_violations', db_url=resolved_db_url, psql_bin=args.psql)
    node_stats_rows = load_db_rows(NODE_STATS_SQL, db_url=resolved_db_url, psql_bin=args.psql) if node_stats_present else []
    edge_stats_rows = load_db_rows(EDGE_STATS_SQL, db_url=resolved_db_url, psql_bin=args.psql) if edge_stats_present else []
    violation_rows = load_db_rows(OPEN_HEALTH_SQL, db_url=resolved_db_url, psql_bin=args.psql) if health_present else []

    node_stats = {str(row.get('node_key') or ''): row for row in node_stats_rows if str(row.get('node_key') or '').strip()}
    edge_stats = {str(row.get('edge_key') or ''): row for row in edge_stats_rows if str(row.get('edge_key') or '').strip()}
    violations = {
        (str(row.get('entity_type') or ''), str(row.get('entity_key') or '')): row
        for row in violation_rows
        if str(row.get('entity_type') or '').strip() and str(row.get('entity_key') or '').strip()
    }

    family_state = build_family_state(entries)
    recommendations: list[dict[str, Any]] = []
    blocked: list[dict[str, Any]] = []
    forced_keys: set[tuple[str, str]] = set()

    for entry in entries:
        key = (entry_entity_type(entry), entity_key(entry))
        stats = node_stats.get(stats_key(entry), {}) if entry_entity_type(entry) == 'node' else edge_stats.get(stats_key(entry), {})
        violation_summary = open_violation_summary(violations, entry)
        forced = forced_transition(entry, stats, violation_summary)
        if forced is None:
            continue
        target_stage, reason = forced
        recommendations.append({
            'entry': entry,
            'target_stage': target_stage,
            'reason': reason,
            'score': transition_rank(entry, stats),
            'preview': controller_preview(entry, stats, violation_summary),
            'transition_class': 'forced',
        })
        forced_keys.add(key)
        apply_family_state_transition(family_state, family_key(entry.get('record') or {}), entry_entity_type(entry), lifecycle_stage(entry.get('record') or {}), target_stage)

    # Active-slot crowding: lowest-ranked active items in overfull families move to hold.
    active_groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for entry in entries:
        key = (entry_entity_type(entry), entity_key(entry))
        if key in forced_keys:
            continue
        record = entry.get('record') or {}
        if lifecycle_stage(record) != 'active':
            continue
        group_key = (family_key(record), entry_entity_type(entry))
        active_groups.setdefault(group_key, []).append(entry)

    for (family, entity_type), group_entries in active_groups.items():
        policy = policies.get(family) or policies.get('unassigned') or {}
        limit = slot_limit(policy, target_stage='active', entity_type=entity_type)
        if limit <= 0:
            limit = 0
        if len(group_entries) <= limit:
            continue
        ranked = sorted(
            group_entries,
            key=lambda entry: transition_rank(
                entry,
                node_stats.get(stats_key(entry), {}) if entry_entity_type(entry) == 'node' else edge_stats.get(stats_key(entry), {}),
            ),
            reverse=True,
        )
        for overflow in ranked[limit:]:
            key = (entry_entity_type(overflow), entity_key(overflow))
            if key in forced_keys:
                continue
            stats = node_stats.get(stats_key(overflow), {}) if entry_entity_type(overflow) == 'node' else edge_stats.get(stats_key(overflow), {})
            violation_summary = open_violation_summary(violations, overflow)
            recommendations.append({
                'entry': overflow,
                'target_stage': 'hold',
                'reason': 'family_active_slot_crowding',
                'score': transition_rank(overflow, stats),
                'preview': controller_preview(overflow, stats, violation_summary),
                'transition_class': 'crowding',
            })
            forced_keys.add(key)
            apply_family_state_transition(family_state, family, entity_type, 'active', 'hold')

    active_candidates: list[dict[str, Any]] = []
    trial_candidates: list[dict[str, Any]] = []
    for entry in entries:
        key = (entry_entity_type(entry), entity_key(entry))
        if key in forced_keys:
            continue
        record = entry.get('record') or {}
        family = family_key(record)
        policy = policies.get(family) or policies.get('unassigned') or {}
        stats = node_stats.get(stats_key(entry), {}) if entry_entity_type(entry) == 'node' else edge_stats.get(stats_key(entry), {})
        violation_summary = open_violation_summary(violations, entry)
        preview = controller_preview(entry, stats, violation_summary)
        stage = lifecycle_stage(record)
        if stage == 'trial':
            blockers = qualifies_for_active(entry, stats, policy, violation_summary)
            if blockers:
                blocked.append({
                    'entity_type': entry_entity_type(entry),
                    'entity_key': entity_key(entry),
                    'target_stage': 'active',
                    'reason': blockers,
                    'preview': preview,
                })
            else:
                active_candidates.append({
                    'entry': entry,
                    'target_stage': 'active',
                    'reason': 'positive_trial_utility_and_family_slot',
                    'score': transition_rank(entry, stats),
                    'preview': preview,
                    'transition_class': 'promotion',
                })
        elif stage == 'draft':
            blockers = qualifies_for_trial(entry, stats, policy, violation_summary)
            if blockers:
                blocked.append({
                    'entity_type': entry_entity_type(entry),
                    'entity_key': entity_key(entry),
                    'target_stage': 'trial',
                    'reason': blockers,
                    'preview': preview,
                })
            else:
                trial_candidates.append({
                    'entry': entry,
                    'target_stage': 'trial',
                    'reason': 'support_and_weight_clear_trial_gate',
                    'score': transition_rank(entry, stats),
                    'preview': preview,
                    'transition_class': 'promotion',
                })

    selected_active, blocked_active = select_ranked_promotions(
        active_candidates,
        target_stage='active',
        family_state=family_state,
        policies=policies,
    )
    selected_trial, blocked_trial = select_ranked_promotions(
        trial_candidates,
        target_stage='trial',
        family_state=family_state,
        policies=policies,
    )
    recommendations.extend(selected_active)
    recommendations.extend(selected_trial)
    blocked.extend([
        {
            'entity_type': entry_entity_type(row['entry']),
            'entity_key': entity_key(row['entry']),
            'target_stage': row['target_stage'],
            'reason': row['reason'],
            'preview': controller_preview(
                row['entry'],
                node_stats.get(stats_key(row['entry']), {}) if entry_entity_type(row['entry']) == 'node' else edge_stats.get(stats_key(row['entry']), {}),
                open_violation_summary(violations, row['entry']),
            ),
        }
        for row in blocked_active + blocked_trial
    ])

    recommendations = sorted(recommendations, key=lambda row: (row['transition_class'] != 'forced', -row['score'], row['target_stage']))
    if args.apply and len(recommendations) > args.max_actions:
        print(json.dumps({
            'ok': False,
            'warning': 'recommended_action_count_exceeds_max_actions',
            'recommended_count': len(recommendations),
            'max_actions': args.max_actions,
        }, indent=2 if args.pretty else None))
        return 1

    applied: list[dict[str, Any]] = []
    for row in recommendations:
        applied.append(
            apply_transition(
                row['entry'],
                target_stage=row['target_stage'],
                reason=row['reason'],
                transitioned_at=transitioned_at,
                db_url=args.db_url,
                psql_bin=args.psql,
                apply=args.apply,
            )
        )

    output = {
        'ok': True,
        'apply': args.apply,
        'transitioned_at': transitioned_at,
        'entry_count': len(entries),
        'recommended_count': len(recommendations),
        'blocked_count': len(blocked),
        'family_state_after_selection': family_state,
        'recommendations': applied,
        'blocked': blocked,
        'stats_presence': {
            'causal_node_stats': node_stats_present,
            'causal_edge_stats': edge_stats_present,
            'causal_graph_health_violations': health_present,
        },
    }
    if not resolved_db_url:
        output['warning'] = 'db_url_unavailable'

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
