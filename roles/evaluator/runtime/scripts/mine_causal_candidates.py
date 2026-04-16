#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.causal_candidates import all_rules, default_threshold_profile, proposal_id  # noqa: E402
from lib.causal_projection import projection_significance  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, missing_columns, resolve_db_url, table_exists  # noqa: E402
from lib.io import read_json, read_text, strip_frontmatter  # noqa: E402
from lib.paths import (  # noqa: E402
    CASE_REVIEWS_ROOT,
    case_canonical_causal_suggestions_path,
    to_repo_relative,
)
from lib.proposed_causal_metadata import classify_intervention_dependency, normalize_cluster_key  # noqa: E402

REQUIRED_COLUMNS = [
    'updated_at',
    'mechanism_family',
    'proposal_source',
    'evidence_channels',
    'intervention_dependency',
    'normalized_cluster_key',
    'context_snapshot',
]

DELETE_STALE_CASE_ROWS_SQL = r'''
WITH input AS (
  SELECT COALESCE(NULLIF(:'active_proposal_ids_json', ''), '[]')::jsonb AS active_ids
),
deleted AS (
  DELETE FROM public.proposed_causal_candidate_occurrences
  WHERE case_key = :'case_key'
    AND (
      jsonb_array_length((SELECT active_ids FROM input)) = 0
      OR proposal_id NOT IN (
        SELECT jsonb_array_elements_text((SELECT active_ids FROM input))
      )
    )
  RETURNING 1
)
SELECT json_build_object('deleted_count', COUNT(*))::text
FROM deleted;
'''

UPSERT_SQL = r'''
INSERT INTO public.proposed_causal_candidate_occurrences (
  proposal_id,
  proposal_key,
  candidate_type,
  candidate_label,
  mechanism_family,
  proposal_source,
  case_key,
  review_path,
  projection_path,
  source_node_key,
  target_node_key,
  node_type,
  effect_sign,
  support_direction,
  occurrence_reason,
  evidence_excerpt,
  genericity_penalty,
  evidence_channels,
  intervention_dependency,
  normalized_cluster_key,
  context_snapshot,
  trigger_snapshot,
  threshold_profile,
  proposal_metadata,
  updated_at
)
VALUES (
  :'proposal_id',
  :'proposal_key',
  :'candidate_type',
  :'candidate_label',
  COALESCE(NULLIF(:'mechanism_family', ''), 'unassigned'),
  COALESCE(NULLIF(:'proposal_source', ''), 'rule_projection'),
  :'case_key',
  :'review_path',
  :'projection_path',
  NULLIF(:'source_node_key', ''),
  NULLIF(:'target_node_key', ''),
  NULLIF(:'node_type', ''),
  NULLIF(:'effect_sign', ''),
  :'support_direction',
  NULLIF(:'occurrence_reason', ''),
  NULLIF(:'evidence_excerpt', ''),
  :'genericity_penalty'::numeric,
  COALESCE(NULLIF(:'evidence_channels_json', ''), '[]')::jsonb,
  :'intervention_dependency',
  NULLIF(:'normalized_cluster_key', ''),
  COALESCE(NULLIF(:'context_snapshot_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'trigger_snapshot_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'threshold_profile_json', ''), '{}')::jsonb,
  COALESCE(NULLIF(:'proposal_metadata_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (proposal_id, case_key) DO UPDATE SET
  proposal_key = EXCLUDED.proposal_key,
  candidate_type = EXCLUDED.candidate_type,
  candidate_label = EXCLUDED.candidate_label,
  mechanism_family = EXCLUDED.mechanism_family,
  proposal_source = EXCLUDED.proposal_source,
  review_path = EXCLUDED.review_path,
  projection_path = EXCLUDED.projection_path,
  source_node_key = EXCLUDED.source_node_key,
  target_node_key = EXCLUDED.target_node_key,
  node_type = EXCLUDED.node_type,
  effect_sign = EXCLUDED.effect_sign,
  support_direction = EXCLUDED.support_direction,
  occurrence_reason = EXCLUDED.occurrence_reason,
  evidence_excerpt = EXCLUDED.evidence_excerpt,
  genericity_penalty = EXCLUDED.genericity_penalty,
  evidence_channels = EXCLUDED.evidence_channels,
  intervention_dependency = EXCLUDED.intervention_dependency,
  normalized_cluster_key = EXCLUDED.normalized_cluster_key,
  context_snapshot = EXCLUDED.context_snapshot,
  trigger_snapshot = EXCLUDED.trigger_snapshot,
  threshold_profile = EXCLUDED.threshold_profile,
  proposal_metadata = EXCLUDED.proposal_metadata,
  updated_at = NOW()
RETURNING json_build_object(
  'proposal_id', proposal_id,
  'case_key', case_key,
  'candidate_type', candidate_type,
  'mechanism_family', mechanism_family,
  'intervention_dependency', intervention_dependency
)::text;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Mine proposed causal node/edge occurrences from case projections and canonicalized case suggestions')
    parser.add_argument('--case-key', action='append', help='Limit mining to one or more case keys')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()



def list_contains(values: list[str], candidates: list[str]) -> list[str]:
    left = {str(item).strip() for item in values if str(item).strip()}
    return [candidate for candidate in candidates if str(candidate).strip() in left]



def first_paragraph(text: str) -> str:
    lines: list[str] = []
    for raw in strip_frontmatter(text).splitlines():
        stripped = raw.strip()
        if not stripped:
            if lines:
                break
            continue
        if stripped.startswith('#'):
            continue
        lines.append(stripped.lstrip('- ').strip())
        if sum(len(item) for item in lines) > 300:
            break
    return ' '.join(lines)[:320]



def case_dirs(selected_case_keys: list[str] | None = None) -> list[Path]:
    selected = {case_key for case_key in (selected_case_keys or []) if case_key}
    out: list[Path] = []
    for case_dir in sorted(CASE_REVIEWS_ROOT.glob('case-*')):
        if not case_dir.is_dir():
            continue
        if selected and case_dir.name not in selected:
            continue
        if not (case_dir / 'causal-projection.json').exists():
            continue
        out.append(case_dir)
    return out



def current_projection_significance(projection: dict[str, Any]) -> dict[str, Any]:
    return projection_significance(projection)



def projection_is_significant(projection: dict[str, Any]) -> bool:
    return bool(current_projection_significance(projection).get('significant'))



def detail_index(rows: list[dict[str, Any]], key_name: str) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        key = str(row.get(key_name) or '').strip()
        if key:
            out[key] = row
    return out



def matching_check_rows(required_checks: list[dict[str, Any]], check_keys: list[str]) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    target = {str(key).strip() for key in check_keys if str(key).strip()}
    for row in required_checks:
        if not isinstance(row, dict):
            continue
        key = str(row.get('check_key') or '').strip()
        if key and key in target:
            selected.append(row)
    return selected



def channels_from_detail(row: dict[str, Any]) -> list[str]:
    raw = row.get('evidence_channels') or []
    if isinstance(raw, list):
        return sorted({str(item).strip() for item in raw if str(item).strip()})
    return []



def merge_occurrence_row(existing: dict[str, Any], new: dict[str, Any]) -> dict[str, Any]:
    merged = dict(existing)
    merged['proposal_source'] = existing['proposal_source'] if existing['proposal_source'] == new['proposal_source'] else 'mixed'
    merged['evidence_channels'] = sorted({*(existing.get('evidence_channels') or []), *(new.get('evidence_channels') or [])})
    merged['intervention_dependency'] = classify_intervention_dependency(merged['evidence_channels'])
    reasons = [part for part in [existing.get('occurrence_reason'), new.get('occurrence_reason')] if str(part or '').strip()]
    merged['occurrence_reason'] = ' | '.join(dict.fromkeys(reasons))
    excerpts = [part for part in [existing.get('evidence_excerpt'), new.get('evidence_excerpt')] if str(part or '').strip()]
    merged['evidence_excerpt'] = ' | '.join(dict.fromkeys(excerpts))[:2000]
    merged['genericity_penalty'] = round((float(existing.get('genericity_penalty') or 0) + float(new.get('genericity_penalty') or 0)) / 2.0, 4)
    trigger_snapshot = dict(existing.get('trigger_snapshot') or {})
    for key, value in (new.get('trigger_snapshot') or {}).items():
        if isinstance(value, list):
            trigger_snapshot[key] = sorted({str(item).strip() for item in (trigger_snapshot.get(key) or []) + value if str(item).strip()})
        else:
            trigger_snapshot[key] = value
    merged['trigger_snapshot'] = trigger_snapshot
    metadata = dict(existing.get('proposal_metadata') or {})
    new_metadata = dict(new.get('proposal_metadata') or {})
    source_list = sorted({*(metadata.get('source_list') or []), *(new_metadata.get('source_list') or [])})
    if source_list:
        metadata['source_list'] = source_list
    for key in ['description', 'canonical_status', 'canonical_reason', 'matched_key', 'template_ids', 'latest_projection_paths', 'linked_intervention_statuses']:
        old = metadata.get(key)
        fresh = new_metadata.get(key)
        if isinstance(old, list) or isinstance(fresh, list):
            metadata[key] = sorted({str(item).strip() for item in (old or []) + (fresh or []) if str(item).strip()})
        elif fresh not in (None, '', {}):
            metadata[key] = fresh
        elif old not in (None, '', {}):
            metadata[key] = old
    for key in ['evidence_channel_summary', 'projection_significance', 'context_snapshot']:
        if isinstance(new_metadata.get(key), dict):
            merged_map = dict(metadata.get(key) or {})
            merged_map.update(new_metadata.get(key) or {})
            metadata[key] = merged_map
    merged['proposal_metadata'] = metadata
    return merged



def rule_occurrence_rows(*, case_key: str, projection: dict[str, Any], projection_significance_row: dict[str, Any], review_excerpt: str, review_path: Path, projection_path: Path) -> list[dict[str, Any]]:
    meta = projection.get('projection_metadata') or {}
    linked_interventions = meta.get('linked_interventions') or {}
    active_nodes = projection.get('active_nodes') or []
    candidate_edges = projection.get('candidate_edges') or []
    contested_edges = projection.get('contested_edges') or []
    required_checks = [row for row in (projection.get('required_checks') or []) if isinstance(row, dict)]
    required_check_keys = [row.get('check_key') for row in required_checks if row.get('check_key')]
    active_node_details = detail_index(meta.get('active_node_details') or [], 'node_key')
    candidate_edge_details = detail_index(meta.get('candidate_edge_details') or [], 'edge_key')
    contested_edge_details = detail_index(meta.get('contested_edge_details') or [], 'edge_key')
    context_snapshot = meta.get('context_snapshot') if isinstance(meta.get('context_snapshot'), dict) else {}

    rows: list[dict[str, Any]] = []
    for rule in all_rules():
        matched: dict[str, list[str]] = {}
        evidence_channels: set[str] = set()
        linked_statuses: dict[str, str] = {}

        active_overlap = list_contains(active_nodes, rule.get('active_nodes_any') or [])
        if rule.get('active_nodes_any') and not active_overlap:
            continue
        if active_overlap:
            matched['active_nodes'] = active_overlap
            for key in active_overlap:
                evidence_channels.update(channels_from_detail(active_node_details.get(key) or {}))

        required_overlap = list_contains(required_check_keys, rule.get('required_checks_any') or [])
        if rule.get('required_checks_any') and not required_overlap:
            continue
        if required_overlap:
            matched['required_checks'] = required_overlap
            for row in matching_check_rows(required_checks, required_overlap):
                evidence_channels.update(channels_from_detail(row))

        contested_overlap = list_contains(contested_edges, rule.get('contested_edges_any') or [])
        if rule.get('contested_edges_any') and not contested_overlap:
            continue
        if contested_overlap:
            matched['contested_edges'] = contested_overlap
            for key in contested_overlap:
                evidence_channels.update(channels_from_detail(contested_edge_details.get(key) or {}))

        candidate_edge_overlap = list_contains(candidate_edges, rule.get('candidate_edges_any') or [])
        if rule.get('candidate_edges_any') and not candidate_edge_overlap:
            continue
        if candidate_edge_overlap:
            matched['candidate_edges'] = candidate_edge_overlap
            for key in candidate_edge_overlap:
                evidence_channels.update(channels_from_detail(candidate_edge_details.get(key) or {}))

        linked_overlap = list_contains(list(linked_interventions.keys()), rule.get('linked_intervention_keys_any') or [])
        if rule.get('linked_intervention_keys_any') and not linked_overlap:
            continue
        if linked_overlap:
            matched['linked_interventions'] = linked_overlap
            for key in linked_overlap:
                status = str((linked_interventions.get(key) or {}).get('status') or '').strip() or 'draft'
                linked_statuses[key] = status
                evidence_channels.add('linked_intervention_active' if status == 'active' else 'linked_intervention_draft')

        reason_parts = [f"{kind}={','.join(values)}" for kind, values in matched.items() if values]
        sorted_channels = sorted(evidence_channels)
        mechanism_family = str(rule.get('mechanism_family') or 'unassigned')
        rows.append(
            {
                'proposal_id': proposal_id(rule['candidate_type'], rule['proposal_key']),
                'proposal_key': rule['proposal_key'],
                'candidate_type': rule['candidate_type'],
                'candidate_label': rule['candidate_label'],
                'mechanism_family': mechanism_family,
                'proposal_source': str(rule.get('proposal_source') or 'rule_projection'),
                'case_key': case_key,
                'review_path': to_repo_relative(review_path),
                'projection_path': to_repo_relative(projection_path),
                'source_node_key': rule.get('source_node_key', ''),
                'target_node_key': rule.get('target_node_key', ''),
                'node_type': rule.get('node_type', ''),
                'effect_sign': rule.get('effect_sign', ''),
                'support_direction': 'supports',
                'occurrence_reason': '; '.join(reason_parts),
                'evidence_excerpt': review_excerpt,
                'genericity_penalty': rule.get('genericity_penalty', 0.2),
                'evidence_channels': sorted_channels,
                'intervention_dependency': classify_intervention_dependency(sorted_channels),
                'normalized_cluster_key': normalize_cluster_key(
                    candidate_type=rule['candidate_type'],
                    proposal_key=rule['proposal_key'],
                    mechanism_family=mechanism_family,
                    candidate_label=rule['candidate_label'],
                    source_node_key=rule.get('source_node_key', ''),
                    target_node_key=rule.get('target_node_key', ''),
                ),
                'context_snapshot': context_snapshot,
                'trigger_snapshot': matched,
                'threshold_profile': rule.get('threshold_profile') or {},
                'proposal_metadata': {
                    'description': rule.get('description', ''),
                    'source_list': [str(rule.get('proposal_source') or 'rule_projection')],
                    'active_nodes': active_nodes,
                    'candidate_edges': candidate_edges,
                    'contested_edges': contested_edges,
                    'required_checks': required_check_keys,
                    'linked_intervention_statuses': linked_statuses,
                    'evidence_channel_summary': meta.get('evidence_channel_summary') or {},
                    'projection_significance': projection_significance_row,
                    'latest_projection_paths': [to_repo_relative(projection_path)],
                },
            }
        )
    return rows



def extracted_occurrence_rows(*, case_key: str, review_path: Path, projection_path: Path, projection: dict[str, Any], projection_significance_row: dict[str, Any]) -> list[dict[str, Any]]:
    suggestions_payload = read_json(case_canonical_causal_suggestions_path(case_key), default={}) or {}
    if not suggestions_payload:
        return []
    context_snapshot = (suggestions_payload.get('context_snapshot') or {}) if isinstance(suggestions_payload.get('context_snapshot'), dict) else {}
    rows: list[dict[str, Any]] = []
    for suggestion in suggestions_payload.get('suggestions') or []:
        if not isinstance(suggestion, dict):
            continue
        status = str(suggestion.get('canonical_status') or '').strip()
        if status in {'matches_live_graph', 'rejected_generic'}:
            continue
        candidate_type = str(suggestion.get('candidate_type') or 'node')
        proposal_key = str(suggestion.get('proposal_key') or '').strip()
        if not proposal_key:
            continue
        mechanism_family = str(suggestion.get('mechanism_family') or 'unassigned')
        evidence_channels = sorted({str(item).strip() for item in (suggestion.get('evidence_channels') or []) if str(item).strip()})
        threshold_profile = suggestion.get('threshold_profile') or default_threshold_profile(candidate_type)
        rows.append(
            {
                'proposal_id': proposal_id(candidate_type, proposal_key),
                'proposal_key': proposal_key,
                'candidate_type': candidate_type,
                'candidate_label': str(suggestion.get('candidate_label') or proposal_key),
                'mechanism_family': mechanism_family,
                'proposal_source': 'case_extractor',
                'case_key': case_key,
                'review_path': to_repo_relative(review_path),
                'projection_path': to_repo_relative(projection_path),
                'source_node_key': str(suggestion.get('source_node_key') or ''),
                'target_node_key': str(suggestion.get('target_node_key') or ''),
                'node_type': str(suggestion.get('node_type') or ''),
                'effect_sign': str(suggestion.get('effect_sign') or ''),
                'support_direction': 'supports',
                'occurrence_reason': str(suggestion.get('canonical_reason') or 'canonicalized_case_suggestion'),
                'evidence_excerpt': str(suggestion.get('evidence_excerpt') or ''),
                'genericity_penalty': float(suggestion.get('genericity_penalty') or 0.24),
                'evidence_channels': evidence_channels,
                'intervention_dependency': classify_intervention_dependency(evidence_channels),
                'normalized_cluster_key': str(suggestion.get('normalized_cluster_key') or normalize_cluster_key(
                    candidate_type=candidate_type,
                    proposal_key=proposal_key,
                    mechanism_family=mechanism_family,
                    candidate_label=str(suggestion.get('candidate_label') or proposal_key),
                    source_node_key=str(suggestion.get('source_node_key') or ''),
                    target_node_key=str(suggestion.get('target_node_key') or ''),
                )),
                'context_snapshot': context_snapshot,
                'trigger_snapshot': {
                    'source_sections': suggestion.get('source_sections') or [],
                    'canonical_status': [status],
                },
                'threshold_profile': threshold_profile,
                'proposal_metadata': {
                    'source_list': ['case_extractor'],
                    'canonical_status': status,
                    'canonical_reason': str(suggestion.get('canonical_reason') or ''),
                    'matched_key': str(suggestion.get('matched_key') or ''),
                    'template_ids': [str(suggestion.get('template_id') or '')] if str(suggestion.get('template_id') or '').strip() else [],
                    'context_snapshot': context_snapshot,
                    'projection_significance': projection_significance_row,
                    'latest_projection_paths': [to_repo_relative(projection_path)],
                    'evidence_channel_summary': (projection.get('projection_metadata') or {}).get('evidence_channel_summary') or {},
                },
            }
        )
    return rows



def mine_case(case_dir: Path) -> list[dict[str, Any]]:
    case_key = case_dir.name
    projection_path = case_dir / 'causal-projection.json'
    projection = read_json(projection_path, default={}) or {}
    if not projection:
        return []
    significance = current_projection_significance(projection)
    if not bool(significance.get('significant')):
        return []
    metadata = projection.get('projection_metadata')
    if isinstance(metadata, dict):
        metadata['projection_significance'] = significance

    review_path = case_dir / 'review.md'
    review_excerpt = first_paragraph(read_text(review_path))
    combined_rows: dict[str, dict[str, Any]] = {}
    for row in rule_occurrence_rows(
        case_key=case_key,
        projection=projection,
        projection_significance_row=significance,
        review_excerpt=review_excerpt,
        review_path=review_path,
        projection_path=projection_path,
    ):
        combined_rows[row['proposal_id']] = row
    for row in extracted_occurrence_rows(
        case_key=case_key,
        review_path=review_path,
        projection_path=projection_path,
        projection=projection,
        projection_significance_row=significance,
    ):
        pid = row['proposal_id']
        if pid in combined_rows:
            combined_rows[pid] = merge_occurrence_row(combined_rows[pid], row)
        else:
            combined_rows[pid] = row
    return sorted(combined_rows.values(), key=lambda row: (row['candidate_type'], row['proposal_key']))



def main() -> int:
    args = parse_args()
    selected_case_keys = args.case_key or []
    cases = case_dirs(selected_case_keys)
    resolved_db_url = resolve_db_url(args.db_url)
    table_present = table_exists('proposed_causal_candidate_occurrences', db_url=resolved_db_url, psql_bin=args.psql) if resolved_db_url else False
    schema_missing: list[str] = []
    if resolved_db_url and table_present:
        schema_missing = missing_columns('proposed_causal_candidate_occurrences', REQUIRED_COLUMNS, db_url=resolved_db_url, psql_bin=args.psql)
        if schema_missing:
            table_present = False

    results: list[dict[str, Any]] = []
    persisted_count = 0
    for case_dir in cases:
        case_key = case_dir.name
        rows = mine_case(case_dir)
        active_proposal_ids = sorted({str(row.get('proposal_id') or '') for row in rows if str(row.get('proposal_id') or '').strip()})
        deleted = None
        if resolved_db_url and table_present:
            deleted = exec_sql(
                args.psql,
                resolved_db_url,
                DELETE_STALE_CASE_ROWS_SQL,
                {
                    'case_key': case_key,
                    'active_proposal_ids_json': json.dumps(active_proposal_ids),
                },
            )
        db_rows: list[Any] = []
        for row in rows:
            db_result = None
            if resolved_db_url and table_present:
                db_result = exec_sql(
                    args.psql,
                    resolved_db_url,
                    UPSERT_SQL,
                    {
                        'proposal_id': row['proposal_id'],
                        'proposal_key': row['proposal_key'],
                        'candidate_type': row['candidate_type'],
                        'candidate_label': row['candidate_label'],
                        'mechanism_family': row.get('mechanism_family') or '',
                        'proposal_source': row.get('proposal_source') or '',
                        'case_key': row['case_key'],
                        'review_path': row['review_path'],
                        'projection_path': row['projection_path'],
                        'source_node_key': row.get('source_node_key') or '',
                        'target_node_key': row.get('target_node_key') or '',
                        'node_type': row.get('node_type') or '',
                        'effect_sign': row.get('effect_sign') or '',
                        'support_direction': row.get('support_direction') or 'supports',
                        'occurrence_reason': row.get('occurrence_reason') or '',
                        'evidence_excerpt': row.get('evidence_excerpt') or '',
                        'genericity_penalty': str(row.get('genericity_penalty') or 0),
                        'evidence_channels_json': json.dumps(row.get('evidence_channels') or []),
                        'intervention_dependency': row.get('intervention_dependency') or 'none',
                        'normalized_cluster_key': row.get('normalized_cluster_key') or '',
                        'context_snapshot_json': json.dumps(row.get('context_snapshot') or {}),
                        'trigger_snapshot_json': json.dumps(row.get('trigger_snapshot') or {}),
                        'threshold_profile_json': json.dumps(row.get('threshold_profile') or {}),
                        'proposal_metadata_json': json.dumps(row.get('proposal_metadata') or {}),
                    },
                )
                persisted_count += 1
            db_rows.append(db_result)
        results.append(
            {
                'case_key': case_key,
                'occurrence_count': len(rows),
                'deleted_previous': deleted,
                'occurrences': rows,
                'db_results': db_rows,
            }
        )

    output: dict[str, Any] = {
        'ok': True,
        'case_count': len(cases),
        'persisted_count': persisted_count,
        'table_present': table_present,
        'results': results,
    }
    if not resolved_db_url:
        output['warning'] = 'db_url_unavailable'
    elif schema_missing:
        output['warning'] = 'proposed_causal_candidate_occurrences table is missing enriched evidence columns; apply roles/evaluator/sql/033_proposed_causal_candidate_evidence_metadata.sql'
        output['missing_columns'] = schema_missing
    elif not table_present:
        output['warning'] = 'proposed_causal_candidate_occurrences table not present; apply roles/evaluator/sql/024_proposed_causal_candidate_occurrences.sql and roles/evaluator/sql/033_proposed_causal_candidate_evidence_metadata.sql'
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
