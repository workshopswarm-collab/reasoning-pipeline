from __future__ import annotations

import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .causal_family_policy import family_policy_for, load_family_policies
from .contract_surface import family_signals_from_contract_surface, load_case_contract_surface
from .io import write_json
from .paths import CAUSAL_MAP_ROOT, ensure_parent, to_repo_relative
from .proposed_driver_occurrence_compiler import packet_json_path

PROVISIONAL_FAMILY_REGISTRY_JSON_PATH = CAUSAL_MAP_ROOT / 'generated' / 'provisional-family-registry.json'
PROVISIONAL_FAMILY_REGISTRY_MD_PATH = CAUSAL_MAP_ROOT / 'generated' / 'provisional-family-registry.md'

RAW_FAMILY_ALIAS_MAP = {
    'publication-timing': 'publication_timing',
    'publication_timing': 'publication_timing',
    'release-window-demand': 'publication_timing',
    'release_window_demand': 'publication_timing',
    'resolution-mapping': 'source_resolution',
    'resolution_mapping': 'source_resolution',
    'source-resolution': 'source_resolution',
    'source_resolution': 'source_resolution',
    'threshold-touch': 'threshold_touch',
    'threshold_touch': 'threshold_touch',
    'workflow-pricing': 'workflow_pricing',
    'workflow_pricing': 'workflow_pricing',
}

GENERIC_RAW_FAMILY_SLUGS = {
    'resolution-mechanics',
}

CANONICAL_FAMILY_SIGNAL_WEIGHTS: dict[str, list[tuple[str, int]]] = {
    'source_resolution': [
        ('source of truth', 5),
        ('source-of-truth', 5),
        ('settlement', 4),
        ('verification', 4),
        ('timestamp', 4),
        ('mapping', 3),
        ('contract', 2),
        ('benchmark', 2),
        ('governing surface', 4),
        ('surface ambiguity', 3),
        ('resolution source', 4),
        ('settlement source', 4),
        ('official source', 2),
    ],
    'workflow_pricing': [
        ('pricing', 4),
        ('bookmaker', 4),
        ('favorite', 3),
        ('odds', 3),
        ('fair value', 4),
        ('fair-value', 4),
        ('valuation', 3),
        ('tracking', 3),
        ('consensus', 2),
        ('implied', 2),
        ('market data integrity', 2),
        ('box office', 1),
    ],
    'threshold_touch': [
        ('threshold', 4),
        ('touch', 4),
        ('wick', 3),
        ('barrier', 3),
        ('volatility', 2),
        ('liquidation', 2),
        ('proximity', 2),
        ('breakout', 2),
        ('intraday', 1),
        ('distance', 1),
        ('path risk', 2),
        ('price path', 2),
        ('touch style', 3),
    ],
    'publication_timing': [
        ('publication', 4),
        ('reporting', 3),
        ('release', 3),
        ('timing', 3),
        ('deadline', 3),
        ('calendar', 2),
        ('window', 2),
        ('announcement', 2),
        ('disclosure', 2),
        ('schedule', 2),
        ('update', 1),
    ],
}



def now_utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')



def normalize_family_key(value: str | None) -> str:
    text = str(value or '').strip().lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_') or 'unassigned'



def normalize_slug(value: str | None) -> str:
    text = str(value or '').strip().lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-') or 'unassigned'



def normalize_text(value: str | None) -> str:
    text = str(value or '').strip().lower()
    text = re.sub(r'[^a-z0-9]+', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()



def label_for_slug(value: str | None) -> str:
    slug = normalize_slug(value)
    if slug == 'unassigned':
        return 'Unassigned'
    return ' '.join(part.capitalize() for part in slug.split('-') if part)



def sort_packets_by_support(packets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        packets,
        key=lambda packet: (
            -int(((packet.get('source_summary') or {}).get('source_occurrence_count') or 0)),
            -int(((packet.get('source_summary') or {}).get('distinct_case_count') or 0)),
            -int(((packet.get('source_summary') or {}).get('distinct_persona_count') or 0)),
            str(packet.get('candidate_slug') or ''),
        ),
    )



def build_packet_signal_text(packet: dict[str, Any]) -> str:
    raw_family_slug = normalize_slug(packet.get('normalized_family'))
    support = packet.get('support') or {}
    values: list[str] = [
        str(packet.get('candidate_slug') or ''),
        str(packet.get('candidate_label') or ''),
    ]
    if raw_family_slug not in GENERIC_RAW_FAMILY_SLUGS:
        values.append(raw_family_slug)
    values.extend([str(item) for item in (support.get('related_canonical_drivers') or [])])
    values.extend([str(item) for item in (support.get('canonical_driver_suggestions') or [])])
    deduped: list[str] = []
    seen: set[str] = set()
    for value in values:
        normalized = normalize_text(value)
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(normalized)
    return ' | '.join(deduped)



def summarize_packet_contract_surface_signals(
    packet: dict[str, Any],
    *,
    case_surface_cache: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    support = packet.get('support') or {}
    case_keys = [str(value).strip() for value in (support.get('case_keys') or []) if str(value).strip()]
    cache = case_surface_cache if isinstance(case_surface_cache, dict) else {}
    family_hits: dict[str, list[str]] = defaultdict(list)
    family_weights: dict[str, float] = defaultdict(float)
    reviewed_case_count = 0
    for case_key in case_keys:
        surface = cache.get(case_key)
        if not isinstance(surface, dict):
            surface = load_case_contract_surface(case_key)
            cache[case_key] = surface
        signals = family_signals_from_contract_surface(surface)
        if signals:
            reviewed_case_count += 1
        for family_key, hits in signals.items():
            for hit_name, weight in hits:
                family_hits[family_key].append(hit_name)
                family_weights[family_key] += float(weight)
    return {
        'reviewed_case_count': reviewed_case_count,
        'family_hit_counts': {family: dict(Counter(hits)) for family, hits in family_hits.items()},
        'family_weight_sums': {family: round(weight, 3) for family, weight in family_weights.items()},
    }



def score_packet_against_canonical_families(
    packet: dict[str, Any],
    *,
    case_surface_cache: dict[str, dict[str, Any]] | None = None,
) -> dict[str, dict[str, Any]]:
    signal_text = build_packet_signal_text(packet)
    contract_surface_summary = summarize_packet_contract_surface_signals(packet, case_surface_cache=case_surface_cache)
    scores: dict[str, dict[str, Any]] = {}
    for family_key, phrases in CANONICAL_FAMILY_SIGNAL_WEIGHTS.items():
        phrase_hits: list[str] = []
        phrase_score = 0.0
        for phrase, weight in phrases:
            normalized_phrase = normalize_text(phrase)
            if normalized_phrase and normalized_phrase in signal_text:
                phrase_hits.append(phrase)
                phrase_score += float(weight)
        structured_hit_counts = (contract_surface_summary.get('family_hit_counts') or {}).get(family_key, {})
        structured_hits = list(structured_hit_counts.keys()) if isinstance(structured_hit_counts, dict) else []
        structured_score = float((contract_surface_summary.get('family_weight_sums') or {}).get(family_key, 0.0) or 0.0)
        scores[family_key] = {
            'score': round(phrase_score + structured_score, 3),
            'phrase_score': round(phrase_score, 3),
            'structured_score': round(structured_score, 3),
            'hits': phrase_hits + structured_hits,
            'phrase_hits': phrase_hits,
            'structured_hits': structured_hits,
            'signal_text': signal_text,
            'contract_surface_summary': contract_surface_summary,
        }
    return scores



def bridge_packet_to_provisional_family(
    packet: dict[str, Any],
    *,
    loaded_policies: dict[str, dict[str, Any]] | None = None,
    case_surface_cache: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    policy_rows = loaded_policies or load_family_policies()
    raw_family_slug = normalize_slug(packet.get('normalized_family'))
    raw_family_key = normalize_family_key(raw_family_slug)
    candidate_slug = normalize_slug(packet.get('candidate_slug'))

    canonical_family = 'unassigned'
    bridge_status = 'novel_provisional'
    bridge_confidence = 0.15
    bridge_reason = ['no_strong_canonical_match']
    score_breakdown = score_packet_against_canonical_families(packet, case_surface_cache=case_surface_cache)

    if raw_family_key in policy_rows and raw_family_key != 'unassigned':
        canonical_family = raw_family_key
        bridge_status = 'canonical_seed'
        bridge_confidence = 1.0
        bridge_reason = ['exact_policy_family_match']
    else:
        alias_family = RAW_FAMILY_ALIAS_MAP.get(raw_family_slug) or RAW_FAMILY_ALIAS_MAP.get(raw_family_key)
        if alias_family and alias_family in policy_rows and alias_family != 'unassigned':
            canonical_family = alias_family
            bridge_status = 'mapped_provisional'
            bridge_confidence = 0.92
            bridge_reason = [f'raw_family_alias:{raw_family_slug}']
        else:
            ranked = sorted(
                score_breakdown.items(),
                key=lambda item: (-float(item[1].get('score') or 0.0), item[0]),
            )
            top_family, top_payload = ranked[0]
            second_score = float(ranked[1][1].get('score') or 0.0) if len(ranked) > 1 else 0.0
            top_score = float(top_payload.get('score') or 0.0)
            if top_score >= 3.0 and top_score >= second_score + 1.0:
                canonical_family = top_family
                bridge_status = 'mapped_provisional'
                bridge_confidence = min(0.9, 0.55 + 0.05 * top_score)
                bridge_reason = list(top_payload.get('hits') or ['heuristic_score'])

    if canonical_family != 'unassigned' and raw_family_key == canonical_family:
        family_key = canonical_family
        family_state = 'canonical_seed'
    elif canonical_family != 'unassigned':
        family_key = f'prov:{canonical_family}:{raw_family_slug}'
        family_state = 'provisional'
    else:
        basis_slug = raw_family_slug or candidate_slug
        family_key = f'prov:novel:{basis_slug}'
        family_state = 'provisional'

    canonical_policy = family_policy_for(canonical_family, loaded=policy_rows)
    raw_family_label = label_for_slug(raw_family_slug)
    if family_key == canonical_family:
        family_label = label_for_slug(canonical_family)
    elif canonical_family != 'unassigned':
        family_label = f"{label_for_slug(canonical_family)} / {raw_family_label}"
    else:
        family_label = f"Novel provisional / {raw_family_label}"

    return {
        'family_key': family_key,
        'family_label': family_label,
        'family_state': family_state,
        'canonical_family': canonical_family,
        'lineage_parent_family_key': canonical_family if family_key != canonical_family else None,
        'source_family_slug': raw_family_slug,
        'source_family_label': raw_family_label,
        'bridge_status': bridge_status,
        'bridge_confidence': round(float(bridge_confidence), 3),
        'bridge_reason': bridge_reason,
        'score_breakdown': score_breakdown,
        'manual_policy_enabled': bool(canonical_policy.get('enabled', False)),
        'manual_policy_family': canonical_family,
    }



def build_provisional_family_registry(
    packets: list[dict[str, Any]],
    *,
    loaded_policies: dict[str, dict[str, Any]] | None = None,
    case_surface_cache: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    policy_rows = loaded_policies or load_family_policies()
    resolved_case_surface_cache = case_surface_cache if isinstance(case_surface_cache, dict) else {}
    grouped: dict[str, dict[str, Any]] = {}
    members: list[dict[str, Any]] = []
    canonical_summary: dict[str, dict[str, Any]] = defaultdict(lambda: {
        'family_key': 'unassigned',
        'family_count': 0,
        'candidate_count': 0,
        'source_occurrence_count': 0,
        'distinct_case_keys': set(),
        'distinct_personas': set(),
    })

    for packet in sort_packets_by_support(packets):
        bridge = bridge_packet_to_provisional_family(
            packet,
            loaded_policies=policy_rows,
            case_surface_cache=resolved_case_surface_cache,
        )
        family_key = bridge['family_key']
        source_summary = packet.get('source_summary') or {}
        support = packet.get('support') or {}
        source_occurrence_count = int(source_summary.get('source_occurrence_count') or 0)
        distinct_case_count = int(source_summary.get('distinct_case_count') or len(support.get('case_keys') or []))
        distinct_persona_count = int(source_summary.get('distinct_persona_count') or len(support.get('personas') or []))
        bucket = grouped.setdefault(
            family_key,
            {
                'family_key': family_key,
                'family_label': bridge['family_label'],
                'family_state': bridge['family_state'],
                'canonical_family': bridge['canonical_family'],
                'lineage_parent_family_key': bridge['lineage_parent_family_key'],
                'source_family_slug': bridge['source_family_slug'],
                'source_family_label': bridge['source_family_label'],
                'bridge_status': bridge['bridge_status'],
                'bridge_confidence_max': 0.0,
                'bridge_reasons': Counter(),
                'manual_policy_enabled': bridge['manual_policy_enabled'],
                'manual_policy_family': bridge['manual_policy_family'],
                'source_lane': 'public.proposed_driver_occurrences',
                'candidate_count': 0,
                'source_occurrence_count': 0,
                'distinct_case_keys': set(),
                'distinct_personas': set(),
                'top_candidates': [],
                'candidate_labels': Counter(),
                'score_breakdown_examples': [],
            },
        )
        bucket['candidate_count'] += 1
        bucket['source_occurrence_count'] += source_occurrence_count
        bucket['distinct_case_keys'].update(support.get('case_keys') or [])
        bucket['distinct_personas'].update(support.get('personas') or [])
        bucket['bridge_confidence_max'] = max(float(bucket['bridge_confidence_max']), float(bridge['bridge_confidence']))
        for reason in bridge['bridge_reason']:
            bucket['bridge_reasons'][reason] += 1
        bucket['candidate_labels'][str(packet.get('candidate_label') or packet.get('candidate_slug') or '')] += 1
        bucket['top_candidates'].append(
            {
                'candidate_slug': packet.get('candidate_slug'),
                'candidate_label': packet.get('candidate_label'),
                'packet_key': packet.get('packet_key'),
                'packet_path': to_repo_relative(packet_json_path(str(packet.get('candidate_slug') or ''))),
                'source_occurrence_count': source_occurrence_count,
                'distinct_case_count': distinct_case_count,
                'distinct_persona_count': distinct_persona_count,
                'bridge_confidence': bridge['bridge_confidence'],
                'bridge_reason': bridge['bridge_reason'],
            }
        )
        if len(bucket['score_breakdown_examples']) < 3:
            bucket['score_breakdown_examples'].append(
                {
                    'candidate_slug': packet.get('candidate_slug'),
                    'candidate_label': packet.get('candidate_label'),
                    'scores': bridge['score_breakdown'],
                }
            )

        canonical_bucket = canonical_summary[bridge['canonical_family']]
        canonical_bucket['family_key'] = bridge['canonical_family']
        canonical_bucket['candidate_count'] += 1
        canonical_bucket['source_occurrence_count'] += source_occurrence_count
        canonical_bucket['distinct_case_keys'].update(support.get('case_keys') or [])
        canonical_bucket['distinct_personas'].update(support.get('personas') or [])

        members.append(
            {
                'family_key': family_key,
                'candidate_slug': str(packet.get('candidate_slug') or ''),
                'packet_key': str(packet.get('packet_key') or ''),
                'membership_score': round(float(bridge['bridge_confidence']), 3),
                'membership_role': 'canonical_seed' if bucket['family_state'] == 'canonical_seed' else 'provisional_seed',
                'member_metadata': {
                    'candidate_label': packet.get('candidate_label'),
                    'packet_path': to_repo_relative(packet_json_path(str(packet.get('candidate_slug') or ''))),
                    'packet_hash': packet.get('packet_hash'),
                    'raw_family_slug': bridge['source_family_slug'],
                    'canonical_family': bridge['canonical_family'],
                    'bridge_status': bridge['bridge_status'],
                    'bridge_reason': bridge['bridge_reason'],
                    'source_occurrence_count': source_occurrence_count,
                    'distinct_case_count': distinct_case_count,
                    'distinct_persona_count': distinct_persona_count,
                },
            }
        )

    family_rows: list[dict[str, Any]] = []
    for canonical_family, row in canonical_summary.items():
        row['family_count'] = sum(1 for family in grouped.values() if family['canonical_family'] == canonical_family)

    for family_key, bucket in grouped.items():
        top_candidates = sorted(
            bucket['top_candidates'],
            key=lambda row: (-int(row['source_occurrence_count']), -int(row['distinct_case_count']), row['candidate_slug']),
        )[:12]
        family_rows.append(
            {
                'family_key': family_key,
                'family_label': bucket['family_label'],
                'family_state': bucket['family_state'],
                'canonical_family': bucket['canonical_family'],
                'lineage_parent_family_key': bucket['lineage_parent_family_key'],
                'source_family_slug': bucket['source_family_slug'],
                'source_family_label': bucket['source_family_label'],
                'bridge_status': bucket['bridge_status'],
                'bridge_confidence_max': round(float(bucket['bridge_confidence_max']), 3),
                'bridge_reasons': [reason for reason, _ in bucket['bridge_reasons'].most_common(8)],
                'manual_policy_family': bucket['manual_policy_family'],
                'manual_policy_enabled': bucket['manual_policy_enabled'],
                'source_lane': bucket['source_lane'],
                'candidate_count': bucket['candidate_count'],
                'source_occurrence_count': bucket['source_occurrence_count'],
                'distinct_case_count': len(bucket['distinct_case_keys']),
                'distinct_persona_count': len(bucket['distinct_personas']),
                'candidate_labels': [label for label, _ in bucket['candidate_labels'].most_common(10)],
                'top_candidates': top_candidates,
                'score_breakdown_examples': bucket['score_breakdown_examples'],
            }
        )

    canonical_rows = [
        {
            'canonical_family': family_key,
            'family_count': row['family_count'],
            'candidate_count': row['candidate_count'],
            'source_occurrence_count': row['source_occurrence_count'],
            'distinct_case_count': len(row['distinct_case_keys']),
            'distinct_persona_count': len(row['distinct_personas']),
            'manual_policy_enabled': family_policy_for(family_key, loaded=policy_rows).get('enabled', False),
        }
        for family_key, row in canonical_summary.items()
    ]
    canonical_rows = sorted(canonical_rows, key=lambda row: (-int(row['source_occurrence_count']), row['canonical_family']))
    family_rows = sorted(family_rows, key=lambda row: (-int(row['source_occurrence_count']), row['family_key']))
    member_rows = sorted(members, key=lambda row: (row['family_key'], row['candidate_slug']))

    return {
        'type': 'provisional_family_registry',
        'generated_at': now_utc_iso(),
        'packet_root': to_repo_relative(packet_json_path('example').parent),
        'family_count': len(family_rows),
        'member_count': len(member_rows),
        'canonical_seed_count': sum(1 for row in family_rows if row['family_state'] == 'canonical_seed'),
        'provisional_count': sum(1 for row in family_rows if row['family_state'] != 'canonical_seed'),
        'novel_provisional_count': sum(1 for row in family_rows if row['canonical_family'] == 'unassigned'),
        'families': family_rows,
        'members': member_rows,
        'canonical_families': canonical_rows,
    }



def render_provisional_family_registry_markdown(payload: dict[str, Any]) -> str:
    lines = [
        '---',
        'type: provisional_family_registry',
        f"generated_at: {payload.get('generated_at')}",
        '---',
        '',
        '# Provisional family registry',
        '',
        '## Summary',
        f"- family_count: `{payload.get('family_count')}`",
        f"- member_count: `{payload.get('member_count')}`",
        f"- canonical_seed_count: `{payload.get('canonical_seed_count')}`",
        f"- provisional_count: `{payload.get('provisional_count')}`",
        f"- novel_provisional_count: `{payload.get('novel_provisional_count')}`",
        '',
        '## Canonical family bridge',
    ]
    canonical_rows = payload.get('canonical_families') or []
    if not canonical_rows:
        lines.append('- none')
    else:
        for row in canonical_rows:
            lines.append(
                f"- `{row.get('canonical_family')}` "
                f"(families: `{row.get('family_count')}`, candidates: `{row.get('candidate_count')}`, "
                f"occurrences: `{row.get('source_occurrence_count')}`, cases: `{row.get('distinct_case_count')}`)"
            )
    lines.extend(['', '## Top provisional families'])
    families = payload.get('families') or []
    if not families:
        lines.append('- none')
    else:
        for row in families[:20]:
            lines.append(
                f"- `{row.get('family_key')}` -> canonical `{row.get('canonical_family')}` "
                f"(state: `{row.get('family_state')}`, candidates: `{row.get('candidate_count')}`, "
                f"occurrences: `{row.get('source_occurrence_count')}`, cases: `{row.get('distinct_case_count')}`)"
            )
            if row.get('bridge_reasons'):
                lines.append(f"  - bridge_reasons: {', '.join(row.get('bridge_reasons') or [])}")
            top_candidates = row.get('top_candidates') or []
            for candidate in top_candidates[:3]:
                lines.append(
                    f"  - `{candidate.get('candidate_label')}` "
                    f"(occurrences: `{candidate.get('source_occurrence_count')}`, cases: `{candidate.get('distinct_case_count')}`)"
                )
    lines.append('')
    return '\n'.join(lines)



def write_provisional_family_registry_artifacts(payload: dict[str, Any]) -> None:
    write_json(ensure_parent(PROVISIONAL_FAMILY_REGISTRY_JSON_PATH), payload)
    ensure_parent(PROVISIONAL_FAMILY_REGISTRY_MD_PATH).write_text(
        render_provisional_family_registry_markdown(payload),
        encoding='utf-8',
    )
