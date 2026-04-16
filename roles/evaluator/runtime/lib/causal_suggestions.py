from __future__ import annotations

import re
from typing import Any

from .causal_candidates import all_rules, default_threshold_profile
from .causal_map import normalize_key
from .causal_projection import projection_significance
from .io import extract_bullets, split_markdown_sections
from .proposed_causal_metadata import normalize_cluster_key, similarity

TARGET_REVIEW_SECTIONS = [
    'Driver and mechanism takeaways',
    'Source / input / workflow takeaways',
    'What was missing',
    'Promotion candidates for stable layers',
    'How this should be reused later',
    'Proposed intervention or hold decision',
]

FAMILY_KEYWORDS = {
    'threshold_touch': [
        'threshold', 'touch', 'binance 1-minute high', 'distance to threshold', 'sub-1%', 'hazard-rate',
        'hazard rate', 'remaining window', 'volatility', 'near-touch', 'near threshold', 'residual window',
    ],
    'source_resolution': [
        'governing source', 'resolution surface', 'source-of-truth', 'source of truth', 'settlement', 'verification',
        'proof capture', 'not been verified', 'event-state', 'verification-state', 'primary source',
    ],
    'workflow_pricing': [
        'fair value', 'discount', 'underconfidence', 'resistance', 'assimilation', 'post-resolution', 'pricing',
        'path probability', 'resolution risk', 'path risk',
    ],
    'publication_timing': [
        'publication', 'reporting', 'official report', 'scheduled release', 'publication window', 'lagged reporting',
    ],
}

SUGGESTION_TEMPLATES: list[dict[str, Any]] = [
    {
        'template_id': 'primary-resolution-source-identification',
        'candidate_type': 'node',
        'proposal_key_hint': 'primary-resolution-source-identification',
        'candidate_label': 'Primary resolution source identification',
        'node_type': 'workflow_condition',
        'mechanism_family': 'source_resolution',
        'genericity_penalty': 0.16,
        'keyword_groups': [
            ['governing source'],
            ['primary source'],
            ['identify the primary', 'resolution source'],
            ['identify the', 'source of truth'],
        ],
    },
    {
        'template_id': 'governing-source-proof-capture',
        'candidate_type': 'node',
        'proposal_key_hint': 'governing-source-proof-capture',
        'candidate_label': 'Governing source proof capture',
        'node_type': 'workflow_condition',
        'mechanism_family': 'source_resolution',
        'genericity_penalty': 0.15,
        'keyword_groups': [
            ['proof capture'],
            ['structured proof capture'],
            ['capture', 'governing source', 'proof'],
            ['decisive proof'],
        ],
    },
    {
        'template_id': 'verification-state-separation',
        'candidate_type': 'node',
        'proposal_key_hint': 'verification-state-separation',
        'candidate_label': 'Verification-state separation',
        'node_type': 'workflow_condition',
        'mechanism_family': 'source_resolution',
        'genericity_penalty': 0.14,
        'keyword_groups': [
            ['split into two separate concepts'],
            ['event not yet occurred', 'not been verified'],
            ['verification-state'],
            ['event-state'],
            ['not yet observed', 'not been verified'],
        ],
    },
    {
        'template_id': 'resolution-risk-path-separation',
        'candidate_type': 'node',
        'proposal_key_hint': 'resolution-risk-path-separation',
        'candidate_label': 'Resolution-risk / path-risk separation',
        'node_type': 'workflow_condition',
        'mechanism_family': 'workflow_pricing',
        'genericity_penalty': 0.14,
        'keyword_groups': [
            ['separate', 'resolution risk', 'path probability'],
            ['separate', 'verification risk', 'path probability'],
            ['path risk', 'resolution risk'],
        ],
    },
    {
        'template_id': 'threshold-distance-scaling',
        'candidate_type': 'node',
        'proposal_key_hint': 'threshold-distance-scaling',
        'candidate_label': 'Threshold-distance scaling',
        'node_type': 'market_state',
        'mechanism_family': 'threshold_touch',
        'genericity_penalty': 0.17,
        'keyword_groups': [
            ['distance to threshold'],
            ['remaining price distance'],
            ['sub-1%'],
            ['fraction of a percent'],
            ['tiny remaining distance'],
            ['near threshold'],
        ],
    },
    {
        'template_id': 'path-volatility-pressure',
        'candidate_type': 'node',
        'proposal_key_hint': 'path-volatility-pressure',
        'candidate_label': 'Path volatility pressure',
        'node_type': 'risk_state',
        'mechanism_family': 'threshold_touch',
        'genericity_penalty': 0.18,
        'keyword_groups': [
            ['ordinary volatility'],
            ['remaining-time path risk'],
            ['residual window'],
            ['multi-day', 'window'],
            ['path volatility'],
        ],
    },
    {
        'template_id': 'resistance-discount-justification',
        'candidate_type': 'node',
        'proposal_key_hint': 'resistance-discount-justification',
        'candidate_label': 'Resistance discount justification',
        'node_type': 'workflow_condition',
        'mechanism_family': 'workflow_pricing',
        'genericity_penalty': 0.2,
        'keyword_groups': [
            ['generic resistance'],
            ['resistance narratives'],
            ['round-number resistance'],
            ['deserve less weight'],
            ['justify', 'discount'],
        ],
    },
    {
        'template_id': 'hazard-rate-touch-framing',
        'candidate_type': 'node',
        'proposal_key_hint': 'hazard-rate-touch-framing',
        'candidate_label': 'Hazard-rate touch framing',
        'node_type': 'workflow_condition',
        'mechanism_family': 'threshold_touch',
        'genericity_penalty': 0.19,
        'keyword_groups': [
            ['hazard-rate problems'],
            ['hazard rate'],
            ['touch probability model'],
        ],
    },
    {
        'template_id': 'ex-post-assimilation-labeling',
        'candidate_type': 'node',
        'proposal_key_hint': 'ex-post-assimilation-labeling',
        'candidate_label': 'Ex-post assimilation labeling',
        'node_type': 'workflow_condition',
        'mechanism_family': 'workflow_pricing',
        'genericity_penalty': 0.2,
        'keyword_groups': [
            ['explicitly labeled as assimilation'],
            ['post-resolution', 'assimilation'],
            ['post-resolution forecast updates'],
        ],
    },
    {
        'template_id': 'settlement-source-specificity__increases__primary-resolution-source-identification',
        'candidate_type': 'edge',
        'proposal_key_hint': 'settlement-source-specificity__increases__primary-resolution-source-identification',
        'candidate_label': 'Settlement source specificity increases primary resolution source identification',
        'source_node_key': 'settlement-source-specificity',
        'target_node_key': 'primary-resolution-source-identification',
        'effect_sign': 'increases',
        'mechanism_family': 'source_resolution',
        'genericity_penalty': 0.18,
        'keyword_groups': [
            ['source-of-truth mechanics', 'source of truth'],
            ['governing source', 'identify'],
            ['source-specific settlement'],
        ],
    },
    {
        'template_id': 'resolution-surface-ambiguity__increases__governing-source-proof-capture',
        'candidate_type': 'edge',
        'proposal_key_hint': 'resolution-surface-ambiguity__increases__governing-source-proof-capture',
        'candidate_label': 'Resolution surface ambiguity increases governing source proof capture',
        'source_node_key': 'resolution-surface-ambiguity',
        'target_node_key': 'governing-source-proof-capture',
        'effect_sign': 'increases',
        'mechanism_family': 'source_resolution',
        'genericity_penalty': 0.16,
        'keyword_groups': [
            ['missing deterministic reconstruction'],
            ['proof acquisition'],
            ['structured proof capture'],
            ['capture', 'governing source', 'proof'],
        ],
    },
    {
        'template_id': 'resolution-surface-ambiguity__increases__verification-state-separation',
        'candidate_type': 'edge',
        'proposal_key_hint': 'resolution-surface-ambiguity__increases__verification-state-separation',
        'candidate_label': 'Resolution surface ambiguity increases verification-state separation',
        'source_node_key': 'resolution-surface-ambiguity',
        'target_node_key': 'verification-state-separation',
        'effect_sign': 'increases',
        'mechanism_family': 'source_resolution',
        'genericity_penalty': 0.15,
        'keyword_groups': [
            ['split into two separate concepts'],
            ['not yet occurred', 'not been verified'],
            ['verification-state separation'],
        ],
    },
    {
        'template_id': 'verification-caution__conditions__resolution-risk-path-separation',
        'candidate_type': 'edge',
        'proposal_key_hint': 'verification-caution__conditions__resolution-risk-path-separation',
        'candidate_label': 'Verification caution conditions resolution-risk / path-risk separation',
        'source_node_key': 'verification-caution',
        'target_node_key': 'resolution-risk-path-separation',
        'effect_sign': 'conditions',
        'mechanism_family': 'workflow_pricing',
        'genericity_penalty': 0.15,
        'keyword_groups': [
            ['separate', 'path probability'],
            ['verification risk', 'path probability'],
            ['resolution risk', 'path probability'],
        ],
    },
    {
        'template_id': 'price-near-threshold__increases__threshold-distance-scaling',
        'candidate_type': 'edge',
        'proposal_key_hint': 'price-near-threshold__increases__threshold-distance-scaling',
        'candidate_label': 'Price near threshold increases threshold-distance scaling',
        'source_node_key': 'price-near-threshold',
        'target_node_key': 'threshold-distance-scaling',
        'effect_sign': 'increases',
        'mechanism_family': 'threshold_touch',
        'genericity_penalty': 0.17,
        'keyword_groups': [
            ['near threshold'],
            ['distance to threshold'],
            ['remaining price distance'],
        ],
    },
    {
        'template_id': 'time-remaining-nontrivial__increases__path-volatility-pressure',
        'candidate_type': 'edge',
        'proposal_key_hint': 'time-remaining-nontrivial__increases__path-volatility-pressure',
        'candidate_label': 'Time remaining increases path volatility pressure',
        'source_node_key': 'time-remaining-nontrivial',
        'target_node_key': 'path-volatility-pressure',
        'effect_sign': 'increases',
        'mechanism_family': 'threshold_touch',
        'genericity_penalty': 0.18,
        'keyword_groups': [
            ['multi-day residual window'],
            ['multiple days remained'],
            ['ordinary volatility'],
            ['remaining-time path risk'],
        ],
    },
]

GENERIC_REJECTION_PHRASES = {
    'none yet',
    'promotion should wait',
    're-open this note',
    'use this note',
    'no obvious missing inputs',
    'current case status',
    'resolution status',
    'platform',
    'high signal',
    'incomplete',
}


def slugify(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', (value or '').strip().lower()).strip('-')



def normalize_text(value: str) -> str:
    return ' '.join((value or '').lower().split())



def infer_mechanism_family(text: str) -> str:
    norm = normalize_text(text)
    best_family = 'unassigned'
    best_score = 0
    for family, keywords in FAMILY_KEYWORDS.items():
        score = sum(1 for keyword in keywords if normalize_text(keyword) in norm)
        if score > best_score:
            best_family = family
            best_score = score
    return best_family



def default_node_type(mechanism_family: str) -> str:
    if mechanism_family == 'threshold_touch':
        return 'market_state'
    if mechanism_family == 'publication_timing':
        return 'workflow_condition'
    return 'workflow_condition'



def passage_rows(review_text: str, signal_packet: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    sections = split_markdown_sections(review_text)
    seen: set[tuple[str, str]] = set()
    for section_name in TARGET_REVIEW_SECTIONS:
        section_text = sections.get(section_name) or ''
        if not section_text:
            continue
        for bullet in extract_bullets(section_text):
            excerpt = bullet.strip()
            key = ('review_text', excerpt)
            if excerpt and key not in seen:
                seen.add(key)
                rows.append({'channel': 'review_text', 'section': section_name, 'excerpt': excerpt})
        cleaned = ' '.join(line.strip() for line in section_text.splitlines() if line.strip() and not line.strip().startswith('- '))
        if cleaned:
            key = ('review_text', cleaned)
            if key not in seen:
                seen.add(key)
                rows.append({'channel': 'review_text', 'section': section_name, 'excerpt': cleaned})
    for signal in (signal_packet.get('signals') or []):
        if not isinstance(signal, dict):
            continue
        section = str((signal.get('metadata') or {}).get('section') or '').strip()
        if section and section not in TARGET_REVIEW_SECTIONS and section not in {'Which inputs were high signal', 'Which inputs were misleading'}:
            continue
        excerpt = str(signal.get('evidence_excerpt') or '').strip()
        if not excerpt:
            continue
        key = ('signal_packet', excerpt)
        if key in seen:
            continue
        seen.add(key)
        rows.append({'channel': 'signal_packet', 'section': section or 'signal_packet', 'excerpt': excerpt})
    return rows



def template_matches(text: str, template: dict[str, Any]) -> bool:
    norm = normalize_text(text)
    for group in template.get('keyword_groups') or []:
        if all(normalize_text(keyword) in norm for keyword in group):
            return True
    return False



def should_emit_fallback(text: str) -> bool:
    norm = normalize_text(text)
    if not norm:
        return False
    if any(phrase in norm for phrase in GENERIC_REJECTION_PHRASES):
        return False
    explicit_markers = [
        'useful reusable driver candidate',
        'candidate to monitor',
        'separate workflow improvement candidate',
        'recommended follow-up instead',
        'another takeaway',
    ]
    if any(token in norm for token in explicit_markers):
        return True
    return '**' in text or '“' in text or '"' in text



def fallback_label(text: str) -> str:
    emphasized = re.findall(r'\*\*(.+?)\*\*', text)
    for chunk in emphasized:
        cleaned = re.sub(r'[`"]', '', chunk).strip()
        if 2 <= len(cleaned.split()) <= 8 and len(cleaned) <= 72:
            return cleaned
    quoted = re.findall(r'["“](.+?)["”]', text)
    for chunk in quoted:
        cleaned = re.sub(r'[`"]', '', chunk).strip()
        if 2 <= len(cleaned.split()) <= 8 and len(cleaned) <= 72:
            return cleaned
    cleaned = text.strip()
    cleaned = re.sub(r'^another takeaway:\s*', '', cleaned, flags=re.I)
    cleaned = re.sub(r'^candidate to monitor[^:]*:\s*', '', cleaned, flags=re.I)
    cleaned = re.sub(r'^separate workflow improvement candidate:\s*', '', cleaned, flags=re.I)
    cleaned = re.sub(r'^useful reusable driver candidate is:\s*', '', cleaned, flags=re.I)
    cleaned = re.sub(r'^recommended follow-up instead:\s*', '', cleaned, flags=re.I)
    cleaned = re.sub(r'\*\*', '', cleaned)
    cleaned = re.sub(r'[`"]', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip(' .;:-')
    if len(cleaned.split()) > 10:
        return ''
    if len(cleaned) > 72:
        return ''
    if ',' in cleaned or ';' in cleaned:
        return ''
    return cleaned



def is_generic_label(label: str) -> bool:
    text = normalize_text(label)
    if not text or len(text) < 8:
        return True
    if any(phrase in text for phrase in GENERIC_REJECTION_PHRASES):
        return True
    words = text.split()
    if len(words) < 2 or len(words) > 10:
        return True
    if len(text) > 72:
        return True
    if re.search(r'\d', text):
        return True
    if re.search(r'[,:;]', label):
        return True
    if re.search(r'\b(case|market|note|pipeline|review|follow-up|candidate|workflow)\b', text) and len(words) <= 4:
        return True
    return False



def extract_case_suggestions(
    *,
    case_key: str,
    review_text: str,
    signal_packet: dict[str, Any],
    learning_packet: dict[str, Any],
    projection: dict[str, Any],
) -> dict[str, Any]:
    context_snapshot = ((projection.get('projection_metadata') or {}).get('context_snapshot') or {})
    current_projection_significance = projection_significance(projection)
    suggestions: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()

    for row in passage_rows(review_text, signal_packet):
        excerpt = str(row['excerpt']).strip()
        if not excerpt:
            continue
        for template in SUGGESTION_TEMPLATES:
            if not template_matches(excerpt, template):
                continue
            item = {
                'suggestion_id': f"{case_key}:{template['template_id']}:{slugify(excerpt)[:24]}",
                'candidate_type': template['candidate_type'],
                'candidate_label': template['candidate_label'],
                'proposal_key_hint': template.get('proposal_key_hint') or '',
                'mechanism_family': template.get('mechanism_family') or infer_mechanism_family(excerpt),
                'node_type': template.get('node_type') or '',
                'source_node_key': template.get('source_node_key') or '',
                'target_node_key': template.get('target_node_key') or '',
                'effect_sign': template.get('effect_sign') or '',
                'proposal_source': 'case_extractor',
                'evidence_excerpt': excerpt,
                'evidence_channels': [row['channel']],
                'source_sections': [row['section']],
                'context_snapshot': context_snapshot,
                'genericity_penalty': template.get('genericity_penalty', 0.2),
                'template_id': template['template_id'],
                'threshold_profile': default_threshold_profile(template['candidate_type']),
            }
            key = (item['candidate_type'], item['candidate_label'], item['evidence_excerpt'])
            if key not in seen:
                seen.add(key)
                suggestions.append(item)
        if row['channel'] == 'review_text' and should_emit_fallback(excerpt):
            label = fallback_label(excerpt)
            family = infer_mechanism_family(label or excerpt)
            if not is_generic_label(label) and family != 'unassigned':
                item = {
                    'suggestion_id': f"{case_key}:fallback:{slugify(label)[:32]}",
                    'candidate_type': 'node',
                    'candidate_label': label,
                    'proposal_key_hint': '',
                    'mechanism_family': family,
                    'node_type': default_node_type(family),
                    'source_node_key': '',
                    'target_node_key': '',
                    'effect_sign': '',
                    'proposal_source': 'case_extractor',
                    'evidence_excerpt': excerpt,
                    'evidence_channels': [row['channel']],
                    'source_sections': [row['section']],
                    'context_snapshot': context_snapshot,
                    'genericity_penalty': 0.24,
                    'template_id': 'fallback',
                    'threshold_profile': default_threshold_profile('node'),
                }
                key = (item['candidate_type'], item['candidate_label'], item['evidence_excerpt'])
                if key not in seen:
                    seen.add(key)
                    suggestions.append(item)

    return {
        'artifact_type': 'case_causal_suggestions',
        'schema_version': 'v1',
        'case_key': case_key,
        'suggestion_source': 'phase3_case_extractor',
        'projection_significance': current_projection_significance,
        'context_snapshot': context_snapshot,
        'suggestions': suggestions,
    }



def proposal_catalog() -> dict[str, dict[str, Any]]:
    return {str(rule.get('proposal_key') or ''): rule for rule in all_rules() if str(rule.get('proposal_key') or '').strip()}



CANONICAL_ALIAS_MAP = {
    'structured-proof-capture': 'governing-source-proof-capture',
    'ordinary-volatility-plus-touch-friendly-settlement-rules': 'hazard-rate-touch-framing',
}



def canonicalize_suggestion(
    suggestion: dict[str, Any],
    *,
    live_nodes: dict[str, dict[str, Any]],
    live_edges: dict[str, dict[str, Any]],
    proposal_rules: dict[str, dict[str, Any]],
    generated_proposals: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    candidate_type = str(suggestion.get('candidate_type') or 'node')
    mechanism_family = str(suggestion.get('mechanism_family') or 'unassigned')
    label = str(suggestion.get('candidate_label') or '').strip()
    evidence_excerpt = str(suggestion.get('evidence_excerpt') or '').strip()
    proposal_key_hint = str(suggestion.get('proposal_key_hint') or '').strip()
    source_node_key = str(suggestion.get('source_node_key') or '').strip()
    target_node_key = str(suggestion.get('target_node_key') or '').strip()
    node_type = str(suggestion.get('node_type') or default_node_type(mechanism_family))
    effect_sign = str(suggestion.get('effect_sign') or '').strip()

    if is_generic_label(label) or mechanism_family == 'unassigned':
        return {
            **suggestion,
            'canonical_status': 'rejected_generic',
            'canonical_reason': 'generic_or_unassigned',
            'proposal_key': normalize_key(proposal_key_hint or label),
            'normalized_cluster_key': '',
            'threshold_profile': default_threshold_profile(candidate_type),
        }

    proposal_key = normalize_key(proposal_key_hint or label)
    proposal_key = CANONICAL_ALIAS_MAP.get(proposal_key, proposal_key)
    live_catalog = live_nodes if candidate_type == 'node' else live_edges
    live_labels = {key: str((record or {}).get('node_label') or (record or {}).get('edge_label') or key) for key, record in live_catalog.items()}

    if proposal_key in live_catalog:
        status = 'matches_live_graph'
        matched_key = proposal_key
        canonical_key = proposal_key
        reason = 'exact_live_graph_key'
    else:
        matched_key = ''
        best_live_score = 0.0
        for key, live_label in live_labels.items():
            score = max(similarity(label, live_label), similarity(proposal_key, key))
            if score > best_live_score:
                best_live_score = score
                matched_key = key
        if best_live_score >= 0.9 and matched_key:
            status = 'matches_live_graph'
            canonical_key = matched_key
            reason = f'live_graph_similarity:{best_live_score:.3f}'
        else:
            combined_proposals = dict(proposal_rules)
            combined_proposals.update(generated_proposals)
            if proposal_key in combined_proposals:
                status = 'matches_existing_proposal'
                canonical_key = proposal_key
                matched_key = proposal_key
                reason = 'exact_existing_proposal_key'
            else:
                best_prop_score = 0.0
                matched_prop_key = ''
                for key, record in combined_proposals.items():
                    candidate_label = str(record.get('candidate_label') or key)
                    score = max(similarity(label, candidate_label), similarity(proposal_key, key))
                    if score > best_prop_score:
                        best_prop_score = score
                        matched_prop_key = key
                if best_prop_score >= 0.82 and matched_prop_key:
                    status = 'matches_existing_proposal'
                    canonical_key = matched_prop_key
                    matched_key = matched_prop_key
                    reason = f'existing_proposal_similarity:{best_prop_score:.3f}'
                else:
                    status = 'new_candidate'
                    canonical_key = proposal_key
                    reason = 'new_canonical_candidate'

    cluster_key = normalize_cluster_key(
        candidate_type=candidate_type,
        proposal_key=canonical_key,
        mechanism_family=mechanism_family,
        candidate_label=label,
        source_node_key=source_node_key,
        target_node_key=target_node_key,
    )

    return {
        **suggestion,
        'proposal_key': canonical_key,
        'candidate_label': label,
        'mechanism_family': mechanism_family,
        'node_type': node_type,
        'effect_sign': effect_sign,
        'source_node_key': source_node_key,
        'target_node_key': target_node_key,
        'canonical_status': status,
        'canonical_reason': reason,
        'matched_key': matched_key,
        'normalized_cluster_key': cluster_key,
        'threshold_profile': suggestion.get('threshold_profile') or default_threshold_profile(candidate_type),
    }
