from __future__ import annotations

from pathlib import Path
from typing import Any

from .causal_projection import projection_significance
from .contract_surface import family_signals_from_contract_surface, parse_case_contract_surface_text
from .io import read_json
from .paths import (
    case_canonical_causal_suggestions_path,
    case_causal_projection_path,
    case_dir,
    case_review_markdown_path,
    to_repo_relative,
)
from .proposed_causal_metadata import INTERVENTION_CHANNELS, NON_INTERVENTION_CHANNELS, WEAK_CHANNELS

JUDGE_VERSION = 'proposed-causal-shadow-v4'

OUTCOME_THRESHOLDS = {
    'helpful_min_score': 3.0,
    'neutral_min_score': 1.0,
    'harmful_max_score': -2.0,
}

WEIGHTS = {
    'direct_non_intervention_support': 3.0,
    'direct_mixed_support': 2.25,
    'direct_weak_support': 1.0,
    'direct_contest': -4.0,
    'canonical_exact_support': 1.4,
    'canonical_merge_support': 0.6,
    'required_check_overlap': 0.9,
    'active_node_overlap': 0.25,
    'edge_overlap': 0.35,
    'significant_case_no_signal_penalty': -1.25,
    'merge_ambiguity_penalty': -0.35,
}



def _to_set(values: Any) -> set[str]:
    if isinstance(values, list):
        return {str(item).strip() for item in values if str(item).strip()}
    return set()



def _review_artifact_paths(case_key: str) -> dict[str, Path]:
    case_root = case_dir(case_key)
    return {
        'case_markdown_path': case_root / 'case.md',
        'review_path': case_review_markdown_path(case_key),
        'projection_path': case_causal_projection_path(case_key),
        'canonical_suggestions_path': case_canonical_causal_suggestions_path(case_key),
    }



def load_case_artifacts(case_key: str) -> dict[str, Any]:
    paths = _review_artifact_paths(case_key)
    case_markdown_exists = paths['case_markdown_path'].exists()
    review_exists = paths['review_path'].exists()
    projection = read_json(paths['projection_path'], default={}) if paths['projection_path'].exists() else {}
    canonical = read_json(paths['canonical_suggestions_path'], default={}) if paths['canonical_suggestions_path'].exists() else {}
    case_markdown_text = ''
    if case_markdown_exists:
        try:
            case_markdown_text = paths['case_markdown_path'].read_text(encoding='utf-8')
        except Exception:
            case_markdown_text = ''
    review_text = ''
    if review_exists:
        try:
            review_text = paths['review_path'].read_text(encoding='utf-8')
        except Exception:
            review_text = ''
    return {
        'case_markdown_exists': case_markdown_exists,
        'case_markdown_path': paths['case_markdown_path'],
        'case_markdown_text': case_markdown_text,
        'case_contract_surface': parse_case_contract_surface_text(case_markdown_text),
        'review_exists': review_exists,
        'review_path': paths['review_path'],
        'review_text': review_text,
        'projection': projection or {},
        'projection_path': paths['projection_path'],
        'canonical_suggestions': canonical or {},
        'canonical_suggestions_path': paths['canonical_suggestions_path'],
    }



def _deduped_channels(row: dict[str, Any]) -> set[str]:
    raw = row.get('evidence_channels') or []
    if isinstance(raw, list):
        return {str(item).strip() for item in raw if str(item).strip()}
    return set()



def _occurrence_support_profile(rows: list[dict[str, Any]]) -> dict[str, Any]:
    support_rows = [row for row in rows if str(row.get('support_direction') or 'supports') == 'supports']
    contest_rows = [row for row in rows if str(row.get('support_direction') or '') in {'contests', 'weakens'}]
    non_intervention_support = 0
    mixed_support = 0
    weak_support = 0
    support_channels: set[str] = set()
    contest_channels: set[str] = set()
    for row in support_rows:
        channels = _deduped_channels(row)
        support_channels.update(channels)
        if channels & NON_INTERVENTION_CHANNELS:
            non_intervention_support += 1
        elif channels & INTERVENTION_CHANNELS:
            mixed_support += 1
        elif channels <= WEAK_CHANNELS:
            weak_support += 1
        else:
            weak_support += 1
    for row in contest_rows:
        contest_channels.update(_deduped_channels(row))
    return {
        'support_count': len(support_rows),
        'contest_count': len(contest_rows),
        'non_intervention_support_count': non_intervention_support,
        'mixed_support_count': mixed_support,
        'weak_support_count': weak_support,
        'support_channels': sorted(support_channels),
        'contest_channels': sorted(contest_channels),
    }



def _canonical_support_profile(shadow_row: dict[str, Any], payload: dict[str, Any]) -> dict[str, Any]:
    proposal_key = str(shadow_row.get('proposal_key') or '').strip()
    candidate_type = str(shadow_row.get('candidate_type') or '').strip()
    notes = shadow_row.get('notes') or {}
    candidate_notes = notes.get('candidate_notes') if isinstance(notes, dict) else {}
    if not isinstance(candidate_notes, dict):
        candidate_notes = {}
    merge_candidate_key = str(candidate_notes.get('merge_candidate_key') or '').strip()

    exact_support_ids: list[str] = []
    merge_support_ids: list[str] = []
    for suggestion in payload.get('suggestions') or []:
        if not isinstance(suggestion, dict):
            continue
        if candidate_type and str(suggestion.get('candidate_type') or '').strip() != candidate_type:
            continue
        suggestion_key = str(suggestion.get('proposal_key') or '').strip()
        matched_key = str(suggestion.get('matched_key') or '').strip()
        canonical_status = str(suggestion.get('canonical_status') or '').strip()
        suggestion_id = str(suggestion.get('suggestion_id') or '').strip() or suggestion_key or matched_key
        if proposal_key and (suggestion_key == proposal_key or matched_key == proposal_key):
            exact_support_ids.append(suggestion_id)
            continue
        if merge_candidate_key and canonical_status in {'matches_live_graph', 'matches_existing_proposal'} and (suggestion_key == merge_candidate_key or matched_key == merge_candidate_key):
            merge_support_ids.append(suggestion_id)

    return {
        'exact_support_count': len(exact_support_ids),
        'merge_support_count': len(merge_support_ids),
        'exact_support_ids': sorted(exact_support_ids),
        'merge_support_ids': sorted(merge_support_ids),
    }



def _projection_overlap_profile(shadow_row: dict[str, Any], projection: dict[str, Any]) -> dict[str, Any]:
    if not projection:
        return {
            'active_node_overlap_count': 0,
            'edge_overlap_count': 0,
            'required_check_overlap_count': 0,
            'matched_active_nodes': [],
            'matched_edges': [],
            'matched_required_checks': [],
            'projection_significant': False,
            'projection_significance': {},
        }

    active_overlap = sorted(_to_set(shadow_row.get('matched_active_nodes')) & _to_set(projection.get('active_nodes')))
    shadow_edges = _to_set(shadow_row.get('matched_candidate_edges')) | _to_set(shadow_row.get('matched_contested_edges'))
    projection_edges = _to_set(projection.get('candidate_edges')) | _to_set(projection.get('contested_edges'))
    edge_overlap = sorted(shadow_edges & projection_edges)
    projection_required_checks = {
        str(item.get('check_key') or '').strip()
        for item in (projection.get('required_checks') or [])
        if isinstance(item, dict) and str(item.get('check_key') or '').strip()
    }
    required_overlap = sorted(_to_set(shadow_row.get('matched_required_checks')) & projection_required_checks)
    significance = projection_significance(projection)
    return {
        'active_node_overlap_count': len(active_overlap),
        'edge_overlap_count': len(edge_overlap),
        'required_check_overlap_count': len(required_overlap),
        'matched_active_nodes': active_overlap,
        'matched_edges': edge_overlap,
        'matched_required_checks': required_overlap,
        'projection_significant': bool(significance.get('significant')),
        'projection_significance': significance,
    }



FAMILY_EVIDENCE_PHRASES: dict[str, list[tuple[str, float]]] = {
    'threshold_touch': [
        ('threshold', 1.2),
        ('touch', 1.0),
        ('volatility', 0.8),
        ('barrier', 0.8),
        ('wick', 0.8),
        ('intraday', 0.6),
        ('price path', 1.0),
        ('proximity', 0.7),
        ('close', 0.4),
        ('range', 0.4),
        ('liquidation', 0.6),
    ],
    'publication_timing': [
        ('publication', 1.2),
        ('release', 1.0),
        ('timing', 1.0),
        ('schedule', 0.8),
        ('deadline', 0.8),
        ('reporting', 0.8),
        ('calendar', 0.8),
        ('window', 0.7),
        ('announcement', 0.7),
        ('data release', 1.0),
        ('report', 0.4),
    ],
    'source_resolution': [
        ('source of truth', 1.4),
        ('resolution', 1.2),
        ('verification', 1.1),
        ('settlement', 1.1),
        ('timestamp', 0.9),
        ('official', 0.7),
        ('benchmark', 0.7),
        ('criteria', 0.6),
        ('mapping', 0.6),
        ('methodology', 0.6),
        ('governing surface', 1.0),
    ],
}



def _shadow_collect_strings(value: Any, out: list[str]) -> None:
    if value is None:
        return
    if isinstance(value, str):
        text = value.strip()
        if text:
            out.append(text)
        return
    if isinstance(value, dict):
        for nested in value.values():
            _shadow_collect_strings(nested, out)
        return
    if isinstance(value, (list, tuple, set)):
        for nested in value:
            _shadow_collect_strings(nested, out)
        return



def _shadow_normalize_text(value: str) -> str:
    return ' '.join(str(value).lower().replace('-', ' ').replace('_', ' ').split())



def _canonical_family_for_occurrence_rows(occurrence_rows: list[dict[str, Any]]) -> str:
    for row in occurrence_rows:
        if not isinstance(row, dict):
            continue
        proposal_metadata = row.get('proposal_metadata') or {}
        if isinstance(proposal_metadata, dict):
            family = str(proposal_metadata.get('canonical_family') or '').strip()
            if family:
                return family
        context_snapshot = row.get('context_snapshot') or {}
        if isinstance(context_snapshot, dict):
            question_mechanics = context_snapshot.get('question_mechanics') or []
            for item in question_mechanics:
                family = str(item or '').strip()
                if family in FAMILY_EVIDENCE_PHRASES:
                    return family
    return ''



def _build_family_specific_signal(
    shadow_row: dict[str, Any],
    *,
    occurrence_rows: list[dict[str, Any]],
    case_artifacts: dict[str, Any],
) -> dict[str, Any]:
    canonical_family = _canonical_family_for_occurrence_rows(occurrence_rows)
    if canonical_family not in FAMILY_EVIDENCE_PHRASES:
        return {
            'canonical_family': canonical_family or '',
            'score_boost': 0.0,
            'neutral_gate': False,
            'helpful_gate': False,
            'hit_weight': 0.0,
            'phrase_hits': [],
            'text_preview': '',
        }
    strings: list[str] = []
    _shadow_collect_strings(case_artifacts.get('review_summary') or {}, strings)
    _shadow_collect_strings(case_artifacts.get('case_markdown_text') or '', strings)
    _shadow_collect_strings(case_artifacts.get('review_text') or '', strings)
    _shadow_collect_strings(case_artifacts.get('projection') or {}, strings)
    _shadow_collect_strings(case_artifacts.get('canonical_suggestions') or {}, strings)
    joined_text = _shadow_normalize_text(' | '.join(strings))
    hits: list[str] = []
    phrase_hit_weight = 0.0
    for phrase, weight in FAMILY_EVIDENCE_PHRASES[canonical_family]:
        normalized_phrase = _shadow_normalize_text(phrase)
        if normalized_phrase and normalized_phrase in joined_text:
            hits.append(phrase)
            phrase_hit_weight += float(weight)
    case_contract_surface = case_artifacts.get('case_contract_surface')
    if not isinstance(case_contract_surface, dict):
        case_contract_surface = parse_case_contract_surface_text(case_artifacts.get('case_markdown_text') or '')
    structured_hits = family_signals_from_contract_surface(case_contract_surface).get(canonical_family, [])
    structured_hit_names = [name for name, _ in structured_hits]
    structured_hit_weight = sum(weight for _, weight in structured_hits)
    combined_hit_weight = phrase_hit_weight + structured_hit_weight
    retrieval_score = float(shadow_row.get('retrieval_score') or 0.0)
    would_inject = bool(shadow_row.get('would_inject'))
    neutral_gate = bool(hits or structured_hits) and combined_hit_weight >= 1.0 and (would_inject or retrieval_score >= 0.88)
    helpful_gate = combined_hit_weight >= 3.4 and len(structured_hits) >= 2 and (would_inject or retrieval_score >= 0.96)
    score_boost = 0.0
    if neutral_gate:
        score_boost += min(1.6, 0.35 + 0.18 * combined_hit_weight)
    if helpful_gate:
        score_boost += 0.25
    return {
        'canonical_family': canonical_family,
        'score_boost': round(score_boost, 4),
        'neutral_gate': neutral_gate,
        'helpful_gate': helpful_gate,
        'hit_weight': round(combined_hit_weight, 4),
        'phrase_hit_weight': round(phrase_hit_weight, 4),
        'structured_hit_weight': round(structured_hit_weight, 4),
        'phrase_hits': hits,
        'structured_hits': structured_hit_names,
        'text_preview': joined_text[:400],
    }



def judge_shadow_row(
    shadow_row: dict[str, Any],
    *,
    occurrence_rows: list[dict[str, Any]] | None = None,
    case_artifacts: dict[str, Any] | None = None,
    occurrence_scope: str = 'same_case',
) -> dict[str, Any]:
    case_key = str(shadow_row.get('case_key') or '').strip()
    occurrence_rows = occurrence_rows or []
    case_artifacts = case_artifacts or load_case_artifacts(case_key)

    projection = case_artifacts.get('projection') or {}
    canonical = case_artifacts.get('canonical_suggestions') or {}
    case_markdown_text = str(case_artifacts.get('case_markdown_text') or '').strip()
    review_exists = bool(case_artifacts.get('review_exists'))
    review_text = str(case_artifacts.get('review_text') or '').strip()
    review_summary = case_artifacts.get('review_summary') or {}
    review_artifacts_present = review_exists or bool(case_markdown_text) or bool(review_text) or bool(review_summary) or bool(projection) or bool(canonical)

    occurrence_profile = _occurrence_support_profile(occurrence_rows)
    canonical_profile = _canonical_support_profile(shadow_row, canonical)
    projection_profile = _projection_overlap_profile(shadow_row, projection)
    family_signal = _build_family_specific_signal(
        shadow_row,
        occurrence_rows=occurrence_rows,
        case_artifacts=case_artifacts,
    )

    cross_case_support_multiplier = 0.45 if occurrence_scope != 'same_case' else 1.0
    positive_breakdown = {
        'direct_non_intervention_support': round((WEIGHTS['direct_non_intervention_support'] * cross_case_support_multiplier) if occurrence_profile['non_intervention_support_count'] > 0 else 0.0, 6),
        'direct_mixed_support': round((WEIGHTS['direct_mixed_support'] * cross_case_support_multiplier) if occurrence_profile['support_count'] > 0 and occurrence_profile['non_intervention_support_count'] <= 0 and occurrence_profile['mixed_support_count'] > 0 else 0.0, 6),
        'direct_weak_support': round((WEIGHTS['direct_weak_support'] * cross_case_support_multiplier) if occurrence_profile['support_count'] > 0 and occurrence_profile['non_intervention_support_count'] <= 0 and occurrence_profile['mixed_support_count'] <= 0 and occurrence_profile['weak_support_count'] > 0 else 0.0, 6),
        'canonical_exact_support': round(min(2, canonical_profile['exact_support_count']) * WEIGHTS['canonical_exact_support'], 6),
        'canonical_merge_support': round(min(2, canonical_profile['merge_support_count']) * WEIGHTS['canonical_merge_support'], 6),
        'required_check_overlap': round(min(2, projection_profile['required_check_overlap_count']) * WEIGHTS['required_check_overlap'], 6),
        'active_node_overlap': round(min(3, projection_profile['active_node_overlap_count']) * WEIGHTS['active_node_overlap'], 6),
        'edge_overlap': round(min(3, projection_profile['edge_overlap_count']) * WEIGHTS['edge_overlap'], 6),
        'family_specific_signal': float(family_signal.get('score_boost') or 0.0),
    }

    negative_breakdown = {
        'direct_contest': WEIGHTS['direct_contest'] if occurrence_profile['contest_count'] > 0 else 0.0,
        'merge_ambiguity_penalty': WEIGHTS['merge_ambiguity_penalty'] if bool(((shadow_row.get('notes') or {}).get('candidate_notes') or {}).get('merge_recommended')) else 0.0,
        'significant_case_no_signal_penalty': 0.0,
    }

    has_positive_signal = any(value > 0 for value in positive_breakdown.values())
    if projection_profile['projection_significant'] and bool(shadow_row.get('would_inject')) and not has_positive_signal:
        negative_breakdown['significant_case_no_signal_penalty'] = WEIGHTS['significant_case_no_signal_penalty']

    outcome_score = round(sum(positive_breakdown.values()) + sum(negative_breakdown.values()), 6)
    helpful_gate = (
        (occurrence_scope == 'same_case' and occurrence_profile['non_intervention_support_count'] > 0)
        or (occurrence_scope == 'same_case' and bool(family_signal.get('helpful_gate')))
        or (
            occurrence_profile['support_count'] > 0
            and (
                canonical_profile['exact_support_count'] > 0
                or (projection_profile['required_check_overlap_count'] + projection_profile['active_node_overlap_count'] + projection_profile['edge_overlap_count']) >= 2
            )
        )
    )
    cross_case_neutral_override = (
        occurrence_scope != 'same_case'
        and occurrence_profile['non_intervention_support_count'] > 0
        and bool(family_signal.get('neutral_gate'))
        and outcome_score >= OUTCOME_THRESHOLDS['neutral_min_score']
    )

    label = 'unclear'
    if occurrence_profile['contest_count'] > 0 or outcome_score <= OUTCOME_THRESHOLDS['harmful_max_score']:
        label = 'harmful'
    elif review_artifacts_present and outcome_score >= OUTCOME_THRESHOLDS['helpful_min_score'] and helpful_gate:
        label = 'helpful'
    elif (review_artifacts_present and outcome_score >= OUTCOME_THRESHOLDS['neutral_min_score']) or cross_case_neutral_override:
        label = 'neutral'
    else:
        label = 'unclear'

    reasons: list[str] = []
    if not review_artifacts_present:
        reasons.append('no_review_artifacts')
    support_prefix = 'same_case' if occurrence_scope == 'same_case' else 'cross_case'
    if occurrence_profile['non_intervention_support_count'] > 0:
        reasons.append(f'{support_prefix}_non_intervention_support')
    if occurrence_profile['mixed_support_count'] > 0:
        reasons.append(f'{support_prefix}_mixed_support')
    if occurrence_profile['weak_support_count'] > 0:
        reasons.append(f'{support_prefix}_weak_support')
    if occurrence_profile['contest_count'] > 0:
        reasons.append(f'{support_prefix}_contest')
    if canonical_profile['exact_support_count'] > 0:
        reasons.append('canonical_exact_support')
    if canonical_profile['merge_support_count'] > 0:
        reasons.append('canonical_merge_support')
    if projection_profile['required_check_overlap_count'] > 0:
        reasons.append('required_check_overlap')
    if projection_profile['active_node_overlap_count'] > 0:
        reasons.append('active_node_overlap')
    if projection_profile['edge_overlap_count'] > 0:
        reasons.append('edge_overlap')
    if negative_breakdown['significant_case_no_signal_penalty'] < 0:
        reasons.append('significant_case_no_signal')
    if negative_breakdown['merge_ambiguity_penalty'] < 0:
        reasons.append('merge_ambiguity_penalty')
    if float(family_signal.get('score_boost') or 0.0) > 0:
        reasons.append(f"family_specific_signal:{family_signal.get('canonical_family') or 'unknown'}")
    if bool(family_signal.get('neutral_gate')):
        reasons.append('family_specific_neutral_gate')
    if bool(family_signal.get('helpful_gate')) and helpful_gate:
        reasons.append('family_specific_helpful_gate')
    if cross_case_neutral_override:
        reasons.append('cross_case_neutral_override')

    return {
        'outcome_label': label,
        'outcome_score': outcome_score,
        'outcome_favored': True if label == 'helpful' else False,
        'judge_version': JUDGE_VERSION,
        'judged_at': None,
        'outcome_metadata': {
            'thresholds': OUTCOME_THRESHOLDS,
            'weights': WEIGHTS,
            'reasons': reasons,
            'review_artifacts_present': review_artifacts_present,
            'review_exists': review_exists,
            'case_markdown_path': to_repo_relative(case_artifacts['case_markdown_path']) if case_artifacts.get('case_markdown_path') and case_artifacts['case_markdown_path'].exists() else None,
            'case_contract_surface': case_artifacts.get('case_contract_surface') if isinstance(case_artifacts.get('case_contract_surface'), dict) else None,
            'review_path': to_repo_relative(case_artifacts['review_path']) if case_artifacts.get('review_path') else None,
            'projection_path': to_repo_relative(case_artifacts['projection_path']) if case_artifacts.get('projection_path') and case_artifacts['projection_path'].exists() else None,
            'canonical_suggestions_path': to_repo_relative(case_artifacts['canonical_suggestions_path']) if case_artifacts.get('canonical_suggestions_path') and case_artifacts['canonical_suggestions_path'].exists() else None,
            'occurrence_profile': occurrence_profile,
            'occurrence_scope': occurrence_scope,
            'canonical_profile': canonical_profile,
            'projection_profile': projection_profile,
            'positive_breakdown': positive_breakdown,
            'negative_breakdown': negative_breakdown,
            'helpful_gate': helpful_gate,
            'cross_case_neutral_override': cross_case_neutral_override,
            'family_signal': family_signal,
        },
    }
