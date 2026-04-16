from __future__ import annotations

import difflib
import re
from collections import Counter
from typing import Any


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (value or "").strip().lower()).strip("-")


NON_INTERVENTION_CHANNELS = {
    'review_text',
    'signal_packet',
    'frontmatter',
    'existing_edge_evidence',
}
INTERVENTION_CHANNELS = {
    'linked_intervention_active',
    'linked_intervention_draft',
}
WEAK_CHANNELS = {
    'heuristic',
    'linked_intervention_draft',
}


def normalize_cluster_key(
    *,
    candidate_type: str,
    proposal_key: str,
    mechanism_family: str,
    candidate_label: str,
    source_node_key: str = '',
    target_node_key: str = '',
) -> str:
    if candidate_type == 'edge' and source_node_key and target_node_key:
        return f"{slugify(candidate_type)}:{slugify(mechanism_family)}:{slugify(source_node_key)}:{slugify(target_node_key)}"
    base = proposal_key or candidate_label
    return f"{slugify(candidate_type)}:{slugify(mechanism_family)}:{slugify(base)}"


def classify_intervention_dependency(evidence_channels: list[str]) -> str:
    channels = {str(item).strip() for item in evidence_channels if str(item).strip()}
    if not channels:
        return 'none'
    active = 'linked_intervention_active' in channels
    draft = 'linked_intervention_draft' in channels
    heuristic = channels <= {'heuristic'}
    non_intervention = bool(channels & NON_INTERVENTION_CHANNELS)
    if heuristic:
        return 'heuristic_only'
    if non_intervention and (active or draft):
        return 'mixed'
    if active and not draft and not non_intervention:
        return 'active_only'
    if draft and not active and not non_intervention:
        return 'draft_only'
    if active and draft and not non_intervention:
        return 'mixed'
    return 'none'


def proposal_source_mix(rows: list[dict[str, Any]]) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for row in rows:
        metadata = row.get('proposal_metadata') or {}
        source_list = metadata.get('source_list') if isinstance(metadata, dict) else None
        if isinstance(source_list, list) and source_list:
            for item in source_list:
                source = str(item).strip()
                if source:
                    counter[source] += 1
            continue
        source = str(row.get('proposal_source') or '').strip() or 'unknown'
        counter[source] += 1
    return dict(sorted(counter.items()))


def dominant_proposal_source(rows: list[dict[str, Any]]) -> str:
    mix = proposal_source_mix(rows)
    if not mix:
        return ''
    return sorted(mix.items(), key=lambda item: (-item[1], item[0]))[0][0]


def deduped_channels(row: dict[str, Any]) -> set[str]:
    raw = row.get('evidence_channels') or []
    if isinstance(raw, list):
        return {str(item).strip() for item in raw if str(item).strip()}
    return set()


def support_case_breakdown(rows: list[dict[str, Any]]) -> dict[str, int]:
    non_intervention_cases: set[str] = set()
    intervention_only_cases: set[str] = set()
    draft_intervention_cases: set[str] = set()
    active_intervention_cases: set[str] = set()
    heuristic_only_cases: set[str] = set()
    review_text_cases: set[str] = set()
    signal_packet_cases: set[str] = set()
    frontmatter_cases: set[str] = set()

    for row in rows:
        case_key = str(row.get('case_key') or '').strip()
        if not case_key or str(row.get('support_direction') or 'supports') != 'supports':
            continue
        channels = deduped_channels(row)
        if channels & NON_INTERVENTION_CHANNELS:
            non_intervention_cases.add(case_key)
        if 'linked_intervention_active' in channels:
            active_intervention_cases.add(case_key)
        if 'linked_intervention_draft' in channels:
            draft_intervention_cases.add(case_key)
        if channels <= (INTERVENTION_CHANNELS | {'heuristic'}) and channels & INTERVENTION_CHANNELS:
            intervention_only_cases.add(case_key)
        if channels <= WEAK_CHANNELS:
            heuristic_only_cases.add(case_key)
        if 'review_text' in channels:
            review_text_cases.add(case_key)
        if 'signal_packet' in channels:
            signal_packet_cases.add(case_key)
        if 'frontmatter' in channels:
            frontmatter_cases.add(case_key)

    return {
        'non_intervention_support_case_count': len(non_intervention_cases),
        'intervention_only_support_case_count': len(intervention_only_cases),
        'draft_intervention_support_case_count': len(draft_intervention_cases),
        'active_intervention_support_case_count': len(active_intervention_cases),
        'heuristic_only_support_case_count': len(heuristic_only_cases),
        'review_text_support_case_count': len(review_text_cases),
        'signal_packet_support_case_count': len(signal_packet_cases),
        'frontmatter_support_case_count': len(frontmatter_cases),
    }


def context_distribution(rows: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    buckets = {
        'platforms': Counter(),
        'categories': Counter(),
        'question_mechanics': Counter(),
        'source_of_truth_class': Counter(),
        'domains': Counter(),
    }
    for row in rows:
        context = row.get('context_snapshot') or {}
        if not isinstance(context, dict):
            continue
        for raw in context.get('platforms') or []:
            text = str(raw).strip()
            if text:
                buckets['platforms'][text] += 1
        for raw in context.get('categories') or []:
            text = str(raw).strip()
            if text:
                buckets['categories'][text] += 1
        for raw in context.get('question_mechanics') or []:
            text = str(raw).strip()
            if text:
                buckets['question_mechanics'][text] += 1
        for raw in context.get('source_of_truth_class') or []:
            text = str(raw).strip()
            if text:
                buckets['source_of_truth_class'][text] += 1
        for raw in context.get('domains') or []:
            text = str(raw).strip()
            if text:
                buckets['domains'][text] += 1
    return {key: dict(sorted(counter.items())) for key, counter in buckets.items()}


def context_breadth_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    distribution = context_distribution(rows)
    return {
        'distinct_platform_count': len(distribution['platforms']),
        'distinct_category_count': len(distribution['categories']),
        'distinct_question_mechanics_count': len(distribution['question_mechanics']),
        'distinct_source_of_truth_class_count': len(distribution['source_of_truth_class']),
        'distinct_domain_count': len(distribution['domains']),
    }


def similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()


def collect_nearby_keys(
    *,
    proposal_key: str,
    candidate_label: str,
    proposal_keys: list[str],
    live_keys: list[str],
    live_labels: dict[str, str] | None = None,
    threshold: float = 0.55,
) -> tuple[list[str], list[str], float, str, bool]:
    near_duplicates: list[tuple[float, str]] = []
    near_live: list[tuple[float, str]] = []

    key_basis = proposal_key or candidate_label
    for other in proposal_keys:
        if other == proposal_key:
            continue
        score = max(similarity(key_basis, other), similarity(candidate_label, other))
        if score >= threshold:
            near_duplicates.append((score, other))

    best_live_score = 0.0
    best_live_key = ''
    live_labels = live_labels or {}
    for live_key in live_keys:
        live_label = live_labels.get(live_key, '')
        score = max(similarity(key_basis, live_key), similarity(candidate_label, live_label or live_key))
        if score >= threshold:
            near_live.append((score, live_key))
        if score > best_live_score:
            best_live_score = score
            best_live_key = live_key

    near_duplicates.sort(key=lambda item: (-item[0], item[1]))
    near_live.sort(key=lambda item: (-item[0], item[1]))
    merge_recommended = best_live_score >= 0.88 and bool(best_live_key)
    return (
        [key for _, key in near_duplicates[:10]],
        [key for _, key in near_live[:10]],
        round(best_live_score, 6),
        best_live_key if merge_recommended else '',
        merge_recommended,
    )
