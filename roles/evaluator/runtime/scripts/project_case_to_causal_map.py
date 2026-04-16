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

from lib.causal_map import build_edge_record, build_node_record, edge_note_paths, listify, node_note_paths  # noqa: E402
from lib.causal_projection import assign_projection_significance, projection_metrics, projection_significance  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.interventions import build_intervention_record, intervention_note_paths  # noqa: E402
from lib.io import parse_frontmatter, read_json, read_text, split_markdown_sections, write_json  # noqa: E402
from lib.paths import (  # noqa: E402
    case_causal_projection_path,
    case_review_markdown_path,
    ensure_parent,
    learning_packet_path,
    signal_packet_path,
    to_repo_relative,
)

PROJECTION_VERSION = 'v2'
PROJECTED_BY = 'roles/evaluator/runtime/scripts/project_case_to_causal_map.py'
MAX_REQUIRED_CHECKS = 5

UPSERT_SQL = r'''
INSERT INTO public.case_causal_projections (
  case_key,
  case_id,
  review_path,
  projection_path,
  active_nodes,
  candidate_edges,
  contested_edges,
  required_checks,
  projection_version,
  projection_metadata,
  updated_at
)
VALUES (
  :'case_key',
  NULLIF(:'case_id', '')::uuid,
  :'review_path',
  :'projection_path',
  COALESCE(NULLIF(:'active_nodes_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'candidate_edges_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'contested_edges_json', ''), '[]')::jsonb,
  COALESCE(NULLIF(:'required_checks_json', ''), '[]')::jsonb,
  :'projection_version',
  COALESCE(NULLIF(:'projection_metadata_json', ''), '{}')::jsonb,
  NOW()
)
ON CONFLICT (case_key) DO UPDATE SET
  case_id = EXCLUDED.case_id,
  review_path = EXCLUDED.review_path,
  projection_path = EXCLUDED.projection_path,
  active_nodes = EXCLUDED.active_nodes,
  candidate_edges = EXCLUDED.candidate_edges,
  contested_edges = EXCLUDED.contested_edges,
  required_checks = EXCLUDED.required_checks,
  projection_version = EXCLUDED.projection_version,
  projection_metadata = EXCLUDED.projection_metadata,
  updated_at = NOW()
RETURNING json_build_object(
  'case_key', case_key,
  'case_id', case_id,
  'projection_version', projection_version,
  'active_node_count', jsonb_array_length(active_nodes),
  'candidate_edge_count', jsonb_array_length(candidate_edges)
)::text;
'''


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_text(value: str) -> str:
    return ' '.join((value or '').lower().split())


def add_hit(hits: dict[str, list[str]], key: str, reason: str) -> None:
    bucket = hits.setdefault(key, [])
    if reason not in bucket:
        bucket.append(reason)


def evidence_channel_for_reason(reason: str) -> str:
    normalized = str(reason or '').strip().lower()
    if normalized.startswith('text:'):
        return 'review_text'
    if normalized.startswith('signal:'):
        return 'signal_packet'
    if normalized.startswith('frontmatter:') or normalized.startswith('context:'):
        return 'frontmatter'
    if normalized.startswith('edge_evidence:') or normalized in {'source_node_active', 'target_node_active', 'edge_evidence_match'}:
        return 'existing_edge_evidence'
    if normalized.startswith('intervention_active:'):
        return 'linked_intervention_active'
    if normalized.startswith('intervention_draft:'):
        return 'linked_intervention_draft'
    if normalized.startswith('intervention_'):
        return 'linked_intervention_draft'
    if normalized.startswith('heuristic:') or normalized.startswith('mechanism_risk:') or normalized.startswith('contested_edge:'):
        return 'heuristic'
    return 'review_text'



def summarize_reason_channels(reasons: list[str]) -> list[str]:
    channels = {evidence_channel_for_reason(reason) for reason in (reasons or []) if str(reason).strip()}
    return sorted(channels)



def has_any(text: str, phrases: list[str]) -> list[str]:
    text_norm = normalize_text(text)
    matched: list[str] = []
    for phrase in phrases:
        phrase_norm = normalize_text(phrase)
        if phrase_norm and phrase_norm in text_norm and phrase not in matched:
            matched.append(phrase)
    return matched


def overlaps(values: list[str], candidates: list[str]) -> list[str]:
    left = {normalize_text(item): item for item in values if str(item).strip()}
    matched: list[str] = []
    for candidate in candidates:
        key = normalize_text(candidate)
        if key in left and left[key] not in matched:
            matched.append(left[key])
    return matched


def load_case_inputs(case_key: str, *, review_path: Path | None = None, signal_path: Path | None = None, packet_path: Path | None = None) -> tuple[Path, Path, Path, str, dict[str, Any], dict[str, Any], dict[str, str], dict[str, Any]]:
    review_path = review_path or case_review_markdown_path(case_key)
    signal_path = signal_path or signal_packet_path(case_key)
    packet_path = packet_path or learning_packet_path(case_key)

    review_text = read_text(review_path)
    signal_packet = read_json(signal_path, default={}) or {}
    learning_packet = read_json(packet_path, default={}) or {}
    sections = split_markdown_sections(review_text)
    frontmatter = parse_frontmatter(review_text)
    return review_path, signal_path, packet_path, review_text, signal_packet, learning_packet, sections, frontmatter


def infer_case_context(*, review_text: str, frontmatter: dict[str, Any], signal_packet: dict[str, Any], learning_packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, list[str]], str]:
    packet_title = str(learning_packet.get('title') or learning_packet.get('question') or '')
    packet_description = str(learning_packet.get('description') or '')
    signal_excerpts = '\n'.join(str(item.get('evidence_excerpt') or '') for item in (signal_packet.get('signals') or []))
    combined_text = '\n'.join([review_text, packet_title, packet_description, signal_excerpts])
    review_text_norm = normalize_text(review_text)
    signal_text_norm = normalize_text(signal_excerpts)
    text_norm = normalize_text(combined_text)

    feature_hits: dict[str, list[str]] = {}

    domain_values = listify(frontmatter.get('domain'))
    subdomain_values = listify(frontmatter.get('subdomain'))
    tag_values = listify(frontmatter.get('tags'))
    related_entities = listify(frontmatter.get('related_entities'))
    related_drivers = listify(frontmatter.get('related_drivers'))

    threshold_touch_phrases = [
        'touch-style market',
        'touch/high-style market',
        'touch/high-style',
        'any qualifying touch',
        'threshold-touch',
        'intraperiod high',
        '1-minute high',
        'touch-friendly settlement',
        'reach $2,400',
    ]
    near_threshold_phrases = [
        'threshold proximity',
        'near-touch territory',
        'within roughly half a percent',
        'only about $8-$13 below the threshold',
        'already in near-touch territory',
        'only $11-$13 below the threshold',
        'tiny remaining distance',
        'sub-1% distance',
        'few dollars below the threshold',
    ]
    multi_day_phrases = [
        'several days left',
        'multiple days remained',
        'multiple remaining trading days',
        'multi-day residual window',
        'time remaining in a 24/7 market',
        'remaining-time path risk',
        'days remained in a continuously traded market',
    ]
    source_specific_phrases = [
        'binance 1-minute high',
        'governing resolution surface',
        'governing source',
        'governing surface',
        'venue-specific',
        'specific governing source',
        'settlement wording',
        'named primary source',
    ]
    resolution_ambiguity_phrases = [
        'not yet verified',
        'missing deterministic reconstruction',
        'exact qualifying binance 1-minute high',
        'proof acquisition',
        'structured proof capture',
        'event may already have occurred but has not been verified',
        'source-of-truth wording incomplete',
        'exact qualifying',
    ]
    caution_phrases = [
        'verification caution',
        'operationally sensible',
        'not yet verified on governing source',
        'withheld confidence because proof capture is incomplete',
        'caution was somewhat overstretched',
        'source-of-truth wording incomplete',
    ]
    underconfidence_phrases = [
        'underconfidence',
        'pulled fair value down',
        'below the market',
        'too expensive relative to case difficulty',
        'too expensive relative to the short remaining distance',
        'overstretched in pricing',
        'deserve less weight',
        'generic resistance concern mattered less',
        'mildly underconfident',
    ]
    publication_phrases = [
        'official publication',
        'scheduled data release',
        'publication window',
        'scheduled publication',
        'official report',
        'publication timing',
    ]
    reporting_state_phrases = [
        'not yet updated',
        'not yet finalized',
        'propagated clearly',
        'reporting state',
        'official reporting surface',
        'lagged reporting',
    ]

    def record_phrase_hits(feature_key: str, phrases: list[str]) -> None:
        for phrase in phrases:
            phrase_norm = normalize_text(phrase)
            if phrase_norm and phrase_norm in review_text_norm:
                add_hit(feature_hits, feature_key, f'text:{phrase}')
            if phrase_norm and phrase_norm in signal_text_norm:
                add_hit(feature_hits, feature_key, f'signal:{phrase}')

    record_phrase_hits('threshold_touch_case', threshold_touch_phrases)
    if overlaps(subdomain_values, ['threshold_touch_markets']):
        add_hit(feature_hits, 'threshold_touch_case', 'frontmatter:subdomain=threshold_touch_markets')
    if overlaps(tag_values, ['threshold-touch']):
        add_hit(feature_hits, 'threshold_touch_case', 'frontmatter:tag=threshold-touch')
    if overlaps(related_drivers, ['touch-style settlement mechanics']):
        add_hit(feature_hits, 'threshold_touch_case', 'frontmatter:related_driver=touch-style settlement mechanics')

    record_phrase_hits('near_threshold', near_threshold_phrases)
    if overlaps(related_drivers, ['threshold proximity']):
        add_hit(feature_hits, 'near_threshold', 'frontmatter:related_driver=threshold proximity')

    record_phrase_hits('multi_day_window', multi_day_phrases)

    record_phrase_hits('source_specific_settlement', source_specific_phrases)
    if overlaps(related_entities, ['binance']):
        add_hit(feature_hits, 'source_specific_settlement', 'frontmatter:related_entity=binance')
    if overlaps(related_drivers, ['verification-surface caution']):
        add_hit(feature_hits, 'source_specific_settlement', 'frontmatter:related_driver=verification-surface caution')

    record_phrase_hits('resolution_ambiguity', resolution_ambiguity_phrases)
    record_phrase_hits('verification_caution', caution_phrases)
    record_phrase_hits('underconfidence_discount', underconfidence_phrases)
    if normalize_text(str(frontmatter.get('error_pattern') or '')) == 'underconfidence_on_nearby_touch_market':
        add_hit(feature_hits, 'underconfidence_discount', 'frontmatter:error_pattern=underconfidence_on_nearby_touch_market')

    record_phrase_hits('publication_timing', publication_phrases)
    record_phrase_hits('reporting_state_uncertainty', reporting_state_phrases)

    question_mechanics: list[str] = []
    if feature_hits.get('threshold_touch_case'):
        question_mechanics.extend(['threshold-touch', 'intraperiod-high-low'])
    if feature_hits.get('publication_timing'):
        question_mechanics.extend(['publication-timing', 'scheduled-publication'])

    source_of_truth_class: list[str] = []
    if feature_hits.get('source_specific_settlement'):
        source_of_truth_class.append('authoritative_with_fallback')
    elif feature_hits.get('publication_timing'):
        source_of_truth_class.append('consensus_reporting_primary')

    categories: list[str] = []
    if overlaps(domain_values, ['crypto']):
        categories.append('crypto')

    case_context = {
        'platform': str(learning_packet.get('platform') or frontmatter.get('market_category') or ''),
        'category': str(learning_packet.get('category') or frontmatter.get('market_category') or ''),
        'domain': domain_values,
        'subdomain': subdomain_values,
        'related_entities': related_entities,
        'related_drivers': related_drivers,
        'tags': tag_values,
        'question_mechanics': list(dict.fromkeys(question_mechanics)),
        'source_of_truth_class': list(dict.fromkeys(source_of_truth_class)),
        'categories': list(dict.fromkeys(categories)),
        'error_pattern': str(frontmatter.get('error_pattern') or ''),
    }
    return case_context, feature_hits, combined_text


def load_registry() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    nodes = {record['node_key']: record for record in (build_node_record(path) for path in node_note_paths())}
    edges = {record['edge_key']: record for record in (build_edge_record(path) for path in edge_note_paths())}
    interventions = {record['intervention_key']: record for record in (build_intervention_record(path) for path in intervention_note_paths())}
    return nodes, edges, interventions


def activate_nodes(*, case_key: str, case_context: dict[str, Any], feature_hits: dict[str, list[str]], nodes: dict[str, dict[str, Any]], edges: dict[str, dict[str, Any]]) -> tuple[list[str], dict[str, list[str]]]:
    active_nodes: list[str] = []
    node_reasons: dict[str, list[str]] = {}

    def activate(node_key: str, reason_list: list[str]) -> None:
        if node_key not in nodes:
            return
        if node_key not in active_nodes:
            active_nodes.append(node_key)
        bucket = node_reasons.setdefault(node_key, [])
        for reason in reason_list:
            if reason not in bucket:
                bucket.append(reason)

    if feature_hits.get('threshold_touch_case') and feature_hits.get('near_threshold'):
        activate('price-near-threshold', feature_hits['threshold_touch_case'] + feature_hits['near_threshold'])
    if feature_hits.get('multi_day_window'):
        activate('time-remaining-nontrivial', feature_hits['multi_day_window'])
    if feature_hits.get('threshold_touch_case') and (feature_hits.get('near_threshold') or feature_hits.get('multi_day_window')):
        activate('touch-probability', (feature_hits.get('threshold_touch_case') or []) + (feature_hits.get('near_threshold') or []) + (feature_hits.get('multi_day_window') or []))
    if feature_hits.get('source_specific_settlement'):
        activate('settlement-source-specificity', feature_hits['source_specific_settlement'])
    if feature_hits.get('resolution_ambiguity') or (feature_hits.get('source_specific_settlement') and feature_hits.get('verification_caution')):
        activate('resolution-surface-ambiguity', (feature_hits.get('resolution_ambiguity') or []) + (feature_hits.get('source_specific_settlement') or []) + (feature_hits.get('verification_caution') or []))
    if feature_hits.get('verification_caution') or (feature_hits.get('resolution_ambiguity') and feature_hits.get('source_specific_settlement')):
        activate('verification-caution', (feature_hits.get('verification_caution') or []) + (feature_hits.get('resolution_ambiguity') or []))
    if feature_hits.get('underconfidence_discount') or (feature_hits.get('verification_caution') and 'watch_only' in normalize_text(' '.join(case_context.get('tags') or []))):
        activate('fair-value-discounting-pressure', (feature_hits.get('underconfidence_discount') or []) + (feature_hits.get('verification_caution') or []))
    if feature_hits.get('publication_timing'):
        activate('publication-window-timing', feature_hits['publication_timing'])
    if feature_hits.get('reporting_state_uncertainty') or (feature_hits.get('publication_timing') and feature_hits.get('resolution_ambiguity')):
        activate('reporting-state-uncertainty', (feature_hits.get('reporting_state_uncertainty') or []) + (feature_hits.get('publication_timing') or []))

    for edge in edges.values():
        for row in edge.get('evidence_rows') or []:
            if row.get('case_key') != case_key:
                continue
            activate(edge['source_node_key'], [f'edge_evidence:{edge["edge_key"]}'])
            activate(edge['target_node_key'], [f'edge_evidence:{edge["edge_key"]}'])

    return sorted(active_nodes), node_reasons


def edge_context_reasons(edge: dict[str, Any], case_context: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    contexts = edge.get('contexts') or {}
    if overlaps(case_context.get('question_mechanics') or [], listify(contexts.get('question_mechanics'))):
        reasons.append('context:question_mechanics')
    if overlaps(case_context.get('source_of_truth_class') or [], listify(contexts.get('source_of_truth_class'))):
        reasons.append('context:source_of_truth_class')
    if overlaps(case_context.get('categories') or [], listify(contexts.get('categories'))):
        reasons.append('context:categories')
    return reasons


def candidate_edges_for_case(*, case_key: str, active_nodes: list[str], case_context: dict[str, Any], edges: dict[str, dict[str, Any]]) -> tuple[list[str], dict[str, list[str]]]:
    candidate_edges: list[str] = []
    edge_reasons: dict[str, list[str]] = {}
    active_set = set(active_nodes)
    for edge_key, edge in edges.items():
        reasons: list[str] = []
        if edge.get('source_node_key') in active_set:
            reasons.append('source_node_active')
        if edge.get('target_node_key') in active_set:
            reasons.append('target_node_active')
        for row in edge.get('evidence_rows') or []:
            if row.get('case_key') == case_key:
                reasons.append('edge_evidence_match')
                break
        reasons.extend(edge_context_reasons(edge, case_context))
        include = False
        if 'edge_evidence_match' in reasons:
            include = True
        elif edge.get('source_node_key') in active_set and edge.get('target_node_key') in active_set:
            include = True
        elif edge.get('source_node_key') in active_set and any(reason.startswith('context:') for reason in reasons):
            include = True
        if include:
            candidate_edges.append(edge_key)
            edge_reasons[edge_key] = list(dict.fromkeys(reasons))
    return sorted(candidate_edges), edge_reasons


def contested_edges_for_case(*, candidate_edges: list[str], combined_text: str) -> tuple[list[str], dict[str, list[str]]]:
    contested: list[str] = []
    contested_reasons: dict[str, list[str]] = {}
    text_norm = normalize_text(combined_text)
    overstretch_markers = [
        'overstretched in pricing',
        'pulled fair value down',
        'too expensive relative to case difficulty',
        'deserve less weight',
        'mildly underconfident',
        'generic resistance concern mattered less',
    ]
    for edge_key in candidate_edges:
        reasons: list[str] = []
        if edge_key == 'verification-caution__increases__fair-value-discounting-pressure':
            for marker in overstretch_markers:
                if normalize_text(marker) in text_norm:
                    reasons.append(f'text:{marker}')
        if reasons:
            contested.append(edge_key)
            contested_reasons[edge_key] = reasons
    return sorted(contested), contested_reasons



def build_context_snapshot(case_context: dict[str, Any]) -> dict[str, list[str]]:
    domains = [str(item).strip() for item in (case_context.get('domain') or []) if str(item).strip()]
    categories = []
    for item in [case_context.get('category')] + list(case_context.get('categories') or []):
        text = str(item or '').strip()
        if text and text not in categories:
            categories.append(text)
    platforms = []
    for item in [case_context.get('platform')]:
        text = str(item or '').strip()
        if text and text not in platforms:
            platforms.append(text)
    question_mechanics = [str(item).strip() for item in (case_context.get('question_mechanics') or []) if str(item).strip()]
    source_of_truth_class = [str(item).strip() for item in (case_context.get('source_of_truth_class') or []) if str(item).strip()]
    return {
        'platforms': platforms,
        'categories': categories,
        'question_mechanics': question_mechanics,
        'source_of_truth_class': source_of_truth_class,
        'domains': domains,
    }



def build_node_details(active_nodes: list[str], node_reasons: dict[str, list[str]], nodes: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    details: list[dict[str, Any]] = []
    for node_key in active_nodes:
        record = nodes.get(node_key) or {}
        reasons = node_reasons.get(node_key) or []
        channels = summarize_reason_channels(reasons)
        details.append(
            {
                'node_key': node_key,
                'node_type': record.get('node_type') or '',
                'mechanism_family': record.get('mechanism_family') or 'unassigned',
                'reasons': reasons,
                'evidence_channels': channels,
                'has_non_intervention_evidence': bool(set(channels) & {'review_text', 'signal_packet', 'frontmatter', 'existing_edge_evidence'}),
            }
        )
    return details



def build_edge_details(
    edge_keys: list[str],
    edge_reasons: dict[str, list[str]],
    edges: dict[str, dict[str, Any]],
    linked_interventions: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    details: list[dict[str, Any]] = []
    linked_interventions = linked_interventions or {}
    for edge_key in edge_keys:
        record = edges.get(edge_key) or {}
        reasons = edge_reasons.get(edge_key) or []
        channels = summarize_reason_channels(reasons)
        intervention_statuses = sorted(
            {
                str((linked_interventions.get(key) or {}).get('status') or '').strip()
                for key in (record.get('linked_intervention_keys') or [])
                if str((linked_interventions.get(key) or {}).get('status') or '').strip()
            }
        )
        details.append(
            {
                'edge_key': edge_key,
                'source_node_key': record.get('source_node_key') or '',
                'target_node_key': record.get('target_node_key') or '',
                'effect_sign': record.get('effect_sign') or '',
                'mechanism_family': record.get('mechanism_family') or 'unassigned',
                'reasons': reasons,
                'evidence_channels': channels,
                'intervention_statuses': intervention_statuses,
                'has_non_intervention_evidence': bool(set(channels) & {'review_text', 'signal_packet', 'frontmatter', 'existing_edge_evidence'}),
            }
        )
    return details



def intervention_checks_for_edges(candidate_edges: list[str], edges: dict[str, dict[str, Any]], interventions: dict[str, dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    check_rows: list[dict[str, Any]] = []
    linked_interventions: dict[str, Any] = {}

    def add_check(check_key: str, reason: str, source: str, *, intervention_status: str = '', support_strength: str = 'weak') -> None:
        normalized = {
            'identify_primary_governing_source': 'verify_primary_resolution_source',
        }.get(check_key, check_key)
        channel = 'linked_intervention_active' if intervention_status == 'active' else 'linked_intervention_draft'
        row = {
            'check_key': normalized,
            'reason': reason,
            'source': source,
            'evidence_channels': [channel],
            'intervention_status': intervention_status,
            'support_strength': support_strength,
        }
        if row not in check_rows:
            check_rows.append(row)

    for edge_key in candidate_edges:
        edge = edges.get(edge_key) or {}
        for intervention_key in edge.get('linked_intervention_keys') or []:
            intervention = interventions.get(intervention_key)
            if not intervention:
                continue
            intervention_status = str(intervention.get('status') or '')
            linked_interventions[intervention_key] = {
                'path': intervention.get('path'),
                'status': intervention_status,
                'application_surface': intervention.get('application_surface'),
            }
            payload = intervention.get('change_payload') or {}
            support_strength = 'medium' if intervention_status == 'active' else 'weak'
            for check in payload.get('required_checks') or []:
                if str(check).strip():
                    reason = f'intervention_{intervention_status}:{intervention_key}' if intervention_status else f'linked_intervention:{intervention_key}'
                    add_check(str(check).strip(), reason, f'intervention:{intervention_key}', intervention_status=intervention_status, support_strength=support_strength)
            for label in payload.get('required_labels') or []:
                label_key = f'label_{str(label).strip()}'
                reason = f'intervention_{intervention_status}:{intervention_key}' if intervention_status else f'linked_intervention:{intervention_key}'
                add_check(label_key, reason, f'intervention:{intervention_key}', intervention_status=intervention_status, support_strength=support_strength)
    return check_rows, linked_interventions


def prioritize_required_checks(*, check_rows: list[dict[str, Any]], active_nodes: list[str], contested_edges: list[str]) -> list[dict[str, Any]]:
    def add_if_missing(check_key: str, reason: str, source: str, *, support_strength: str = 'weak') -> None:
        row = {
            'check_key': check_key,
            'reason': reason,
            'source': source,
            'evidence_channels': ['heuristic'],
            'support_strength': support_strength,
        }
        if row not in check_rows:
            check_rows.append(row)

    active_set = set(active_nodes)
    contested_set = set(contested_edges)
    if 'settlement-source-specificity' in active_set or 'resolution-surface-ambiguity' in active_set:
        add_if_missing('verify_primary_resolution_source', 'mechanism_risk:source_specific_settlement', 'heuristic:source_specific_settlement')
        add_if_missing('capture_governing_source_proof_when_event_near_complete', 'mechanism_risk:resolution_surface_ambiguity', 'heuristic:resolution_surface_ambiguity')
    if 'price-near-threshold' in active_set or 'touch-probability' in active_set:
        add_if_missing('confirm_any_qualifying_touch_resolves_yes', 'mechanism_risk:touch_mechanics', 'heuristic:touch_mechanics')
        add_if_missing('evaluate_distance_to_threshold', 'mechanism_risk:threshold_proximity', 'heuristic:threshold_proximity')
        add_if_missing('evaluate_time_remaining_and_path_volatility', 'mechanism_risk:residual_window', 'heuristic:residual_window')
    if 'verification-caution__increases__fair-value-discounting-pressure' in contested_set:
        add_if_missing('separate_resolution_risk_from_path_probability', 'contested_edge:verification_caution__increases__fair-value-discounting-pressure', 'heuristic:contested_edge')
        add_if_missing('label_unverified_vs_not_occurred_distinctly', 'contested_edge:verification_caution__increases__fair-value-discounting-pressure', 'heuristic:contested_edge')
        add_if_missing('justify_any_resistance_discount_explicitly', 'contested_edge:verification_caution__increases__fair-value-discounting-pressure', 'heuristic:contested_edge')

    priority = {
        'verify_primary_resolution_source': 10,
        'capture_governing_source_proof_when_event_near_complete': 20,
        'separate_resolution_risk_from_path_probability': 30,
        'label_unverified_vs_not_occurred_distinctly': 40,
        'confirm_any_qualifying_touch_resolves_yes': 50,
        'evaluate_distance_to_threshold': 60,
        'evaluate_time_remaining_and_path_volatility': 70,
        'justify_any_resistance_discount_explicitly': 80,
        'label_event_state': 90,
        'label_verification_state': 100,
    }
    strength_priority = {'strong': 0, 'medium': 1, 'weak': 2}
    ordered = sorted(
        check_rows,
        key=lambda row: (
            strength_priority.get(str(row.get('support_strength') or 'weak'), 9),
            priority.get(str(row.get('check_key') or ''), 999),
            str(row.get('check_key') or ''),
        ),
    )
    deduped: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row in ordered:
        key = str(row.get('check_key') or '').strip()
        if not key or key in seen:
            continue
        seen.add(key)
        normalized = dict(row)
        normalized['evidence_channels'] = sorted({str(item).strip() for item in (row.get('evidence_channels') or []) if str(item).strip()})
        deduped.append(normalized)
        if len(deduped) >= MAX_REQUIRED_CHECKS:
            break
    return deduped


def build_projection(*, case_key: str, review_path: Path, signal_path: Path, packet_path: Path) -> dict[str, Any]:
    review_path, signal_path, packet_path, review_text, signal_packet, learning_packet, sections, frontmatter = load_case_inputs(
        case_key,
        review_path=review_path,
        signal_path=signal_path,
        packet_path=packet_path,
    )
    case_context, feature_hits, combined_text = infer_case_context(
        review_text=review_text,
        frontmatter=frontmatter,
        signal_packet=signal_packet,
        learning_packet=learning_packet,
    )
    nodes, edges, interventions = load_registry()

    active_nodes, node_reasons = activate_nodes(
        case_key=case_key,
        case_context=case_context,
        feature_hits=feature_hits,
        nodes=nodes,
        edges=edges,
    )
    candidate_edges, edge_reasons = candidate_edges_for_case(
        case_key=case_key,
        active_nodes=active_nodes,
        case_context=case_context,
        edges=edges,
    )
    contested_edges, contested_edge_reasons = contested_edges_for_case(
        candidate_edges=candidate_edges,
        combined_text=combined_text,
    )
    check_rows, linked_interventions = intervention_checks_for_edges(candidate_edges, edges, interventions)
    required_checks = prioritize_required_checks(
        check_rows=check_rows,
        active_nodes=active_nodes,
        contested_edges=contested_edges,
    )
    active_node_details = build_node_details(active_nodes, node_reasons, nodes)
    candidate_edge_details = build_edge_details(candidate_edges, edge_reasons, edges, linked_interventions)
    contested_edge_details = build_edge_details(contested_edges, contested_edge_reasons, edges, linked_interventions)
    evidence_channel_summary: dict[str, int] = {}
    for row in active_node_details + candidate_edge_details + contested_edge_details + required_checks:
        for channel in row.get('evidence_channels') or []:
            evidence_channel_summary[channel] = evidence_channel_summary.get(channel, 0) + 1

    projection_path = case_causal_projection_path(case_key)
    projection = {
        'artifact_type': 'case_causal_projection',
        'schema_version': 'v2',
        'case_key': case_key,
        'review_path': to_repo_relative(review_path),
        'signal_packet_path': to_repo_relative(signal_path),
        'learning_packet_path': to_repo_relative(packet_path),
        'active_nodes': active_nodes,
        'candidate_edges': candidate_edges,
        'contested_edges': contested_edges,
        'required_checks': required_checks,
        'projection_metadata': {
            'projected_by': PROJECTED_BY,
            'projected_at': utc_now_iso(),
            'projection_version': PROJECTION_VERSION,
            'case_context': case_context,
            'context_snapshot': build_context_snapshot(case_context),
            'feature_hits': feature_hits,
            'node_reasons': node_reasons,
            'edge_reasons': edge_reasons,
            'contested_edge_reasons': contested_edge_reasons,
            'active_node_details': active_node_details,
            'candidate_edge_details': candidate_edge_details,
            'contested_edge_details': contested_edge_details,
            'linked_interventions': linked_interventions,
            'evidence_channel_summary': dict(sorted(evidence_channel_summary.items())),
            'sections_present': sorted(sections.keys()),
            'signal_count': signal_packet.get('signal_count'),
            'graph_snapshot': {
                'node_count': len(nodes),
                'edge_count': len(edges),
            },
            'projection_path': to_repo_relative(projection_path),
        },
    }
    assign_projection_significance(projection)
    return projection


def persist_projection(projection: dict[str, Any], *, learning_packet: dict[str, Any], db_url: str = '', psql_bin: str = DEFAULT_PSQL) -> dict[str, Any]:
    resolved_db_url = resolve_db_url(db_url)
    table_present = table_exists('case_causal_projections', db_url=resolved_db_url, psql_bin=psql_bin) if resolved_db_url else False
    result: dict[str, Any] = {
        'persisted': False,
        'table_present': table_present,
    }
    if resolved_db_url and table_present:
        payload = exec_sql(
            psql_bin,
            resolved_db_url,
            UPSERT_SQL,
            {
                'case_key': projection['case_key'],
                'case_id': str(learning_packet.get('case_id') or ''),
                'review_path': projection['review_path'],
                'projection_path': projection['projection_metadata']['projection_path'],
                'active_nodes_json': json.dumps(projection.get('active_nodes') or []),
                'candidate_edges_json': json.dumps(projection.get('candidate_edges') or []),
                'contested_edges_json': json.dumps(projection.get('contested_edges') or []),
                'required_checks_json': json.dumps(projection.get('required_checks') or []),
                'projection_version': PROJECTION_VERSION,
                'projection_metadata_json': json.dumps(projection.get('projection_metadata') or {}),
            },
        )
        result['persisted'] = True
        result['db_result'] = payload
    elif resolved_db_url and not table_present:
        result['warning'] = 'case_causal_projections table not present; apply roles/evaluator/sql/023_case_causal_projections.sql to enable persistence'
    else:
        result['warning'] = 'db url unavailable; emitting projection artifact only'
    return result


def project_case_to_causal_map(
    case_key: str,
    *,
    review_path: Path | None = None,
    signal_path: Path | None = None,
    packet_path: Path | None = None,
    db_url: str = '',
    psql_bin: str = DEFAULT_PSQL,
    dry_run: bool = False,
) -> dict[str, Any]:
    review_path = review_path or case_review_markdown_path(case_key)
    signal_path = signal_path or signal_packet_path(case_key)
    packet_path = packet_path or learning_packet_path(case_key)

    projection = build_projection(case_key=case_key, review_path=review_path, signal_path=signal_path, packet_path=packet_path)
    out_path = case_causal_projection_path(case_key)
    artifact_write: dict[str, Any] = {
        'status': 'dry_run' if dry_run else 'written',
        'path': to_repo_relative(out_path),
    }
    if not dry_run:
        ensure_parent(out_path)
        write_json(out_path, projection, pretty=True)
    learning_packet = read_json(packet_path, default={}) or {}
    persist_result = {'persisted': False, 'table_present': False, 'warning': 'dry_run'} if dry_run else persist_projection(projection, learning_packet=learning_packet, db_url=db_url, psql_bin=psql_bin)
    metrics = projection_metrics(projection)
    significance = projection_significance(projection)

    return {
        'ok': True,
        'case_key': case_key,
        'projection_path': to_repo_relative(out_path),
        'artifact_write': artifact_write,
        **metrics,
        'significance': significance,
        'projection': projection,
        'persistence': persist_result,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Project one reviewed case bundle into the causal map substrate')
    parser.add_argument('--case-key', required=True)
    parser.add_argument('--review-path', default='')
    parser.add_argument('--signal-path', default='')
    parser.add_argument('--packet-path', default='')
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = project_case_to_causal_map(
        args.case_key,
        review_path=Path(args.review_path) if args.review_path else None,
        signal_path=Path(args.signal_path) if args.signal_path else None,
        packet_path=Path(args.packet_path) if args.packet_path else None,
        db_url=args.db_url,
        psql_bin=args.psql,
        dry_run=args.dry_run,
    )
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
