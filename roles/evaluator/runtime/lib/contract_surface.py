from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .paths import case_dir


def normalize_contract_text(value: str | None) -> str:
    text = str(value or '').strip().lower()
    text = text.replace('-', ' ').replace('_', ' ')
    text = re.sub(r'[^a-z0-9.$: ]+', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()


DAY_OR_MONTH_PATTERN = re.compile(
    r'\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday|january|february|march|april|may|june|july|august|september|october|november|december|noon|midnight)\b'
)
THRESHOLD_PATTERN = re.compile(
    r'\b(above|below|over|under|higher than|lower than|at least|at most|reach|reaches|reached|exceed|exceeds)\s+\$?([0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?)'
)


def _contains_any_phrase(text: str, phrases: list[str]) -> bool:
    return any(normalize_contract_text(phrase) in text for phrase in phrases)



def parse_case_contract_surface_text(text: str | None) -> dict[str, Any]:
    normalized = normalize_contract_text(text)
    threshold_match = THRESHOLD_PATTERN.search(normalized)
    comparator = threshold_match.group(1) if threshold_match else ''
    threshold_value = threshold_match.group(2).replace(',', '') if threshold_match else ''

    source_references: list[str] = []
    for phrase, label in [
        ('binance', 'binance'),
        ('official', 'official'),
        ('source of truth', 'source_of_truth'),
        ('resolution source', 'resolution_source'),
        ('settlement source', 'settlement_source'),
        ('governing surface', 'governing_surface'),
    ]:
        if normalize_contract_text(phrase) in normalized:
            source_references.append(label)

    settlement_fields: list[str] = []
    for phrase, label in [
        ('close price', 'close'),
        ('final close', 'close'),
        ('high price', 'high'),
        ('low price', 'low'),
        ('closing price', 'close'),
    ]:
        if normalize_contract_text(phrase) in normalized:
            settlement_fields.append(label)

    time_resolution = ''
    if _contains_any_phrase(normalized, ['1 minute candle', '1m candle', '1m and candles selected', 'candles selected on the top bar']):
        time_resolution = '1m_candle'

    publication_markers: list[str] = []
    for phrase, label in [
        ('opening weekend', 'opening_weekend'),
        ('opening day', 'opening_day'),
        ('release date', 'release_date'),
        ('release window', 'release_window'),
        ('publication date', 'publication_date'),
        ('announcement date', 'announcement_date'),
        ('report date', 'report_date'),
        ('box office', 'box_office'),
        ('earnings', 'earnings'),
        ('reporting', 'reporting'),
        ('announcement', 'announcement'),
        ('publication', 'publication'),
        ('data release', 'data_release'),
        ('premiere', 'premiere'),
        ('opens in theaters', 'opens_in_theaters'),
    ]:
        if normalize_contract_text(phrase) in normalized:
            publication_markers.append(label)

    timing_constraint = bool(
        _contains_any_phrase(normalized, ['deadline', 'schedule', 'calendar', 'window', 'timing'])
        or DAY_OR_MONTH_PATTERN.search(normalized)
    )
    dated_window = bool(
        _contains_any_phrase(normalized, ['weekend', 'window', 'schedule'])
        and DAY_OR_MONTH_PATTERN.search(normalized)
    )

    return {
        'normalized_text': normalized,
        'comparator': comparator,
        'threshold_value': threshold_value,
        'source_references': sorted(set(source_references)),
        'settlement_fields': sorted(set(settlement_fields)),
        'time_resolution': time_resolution,
        'publication_markers': sorted(set(publication_markers)),
        'timing_constraint': timing_constraint,
        'dated_window': dated_window,
    }



def load_case_contract_surface(case_key: str) -> dict[str, Any]:
    case_markdown_path = case_dir(case_key) / 'case.md'
    case_markdown_text = ''
    if case_markdown_path.exists():
        try:
            case_markdown_text = case_markdown_path.read_text(encoding='utf-8')
        except Exception:
            case_markdown_text = ''
    surface = parse_case_contract_surface_text(case_markdown_text)
    surface['case_key'] = case_key
    surface['case_markdown_path'] = case_markdown_path
    return surface



def family_signals_from_contract_surface(surface: dict[str, Any] | None) -> dict[str, list[tuple[str, float]]]:
    surface = surface or {}
    signals: dict[str, list[tuple[str, float]]] = {
        'threshold_touch': [],
        'publication_timing': [],
        'source_resolution': [],
    }

    comparator = str(surface.get('comparator') or '').strip()
    threshold_value = str(surface.get('threshold_value') or '').strip()
    source_references = {str(value or '').strip() for value in (surface.get('source_references') or [])}
    settlement_fields = {str(value or '').strip() for value in (surface.get('settlement_fields') or [])}
    time_resolution = str(surface.get('time_resolution') or '').strip()
    publication_markers = {str(value or '').strip() for value in (surface.get('publication_markers') or [])}
    timing_constraint = bool(surface.get('timing_constraint'))
    dated_window = bool(surface.get('dated_window'))

    strong_publication_surface_markers = publication_markers & {
        'opening_weekend',
        'opening_day',
        'release_date',
        'release_window',
        'publication_date',
        'report_date',
        'premiere',
        'box_office',
        'earnings',
        'publication',
        'data_release',
        'opens_in_theaters',
    }
    supporting_publication_markers = publication_markers & {
        'announcement',
        'announcement_date',
        'reporting',
    }
    has_strong_publication_surface = bool(strong_publication_surface_markers)
    has_publication_family_anchor = has_strong_publication_surface or bool(
        publication_markers & {'announcement_date'}
    )

    if comparator and threshold_value:
        signals['threshold_touch'].append(('threshold_contract_surface', 3.0))
    if time_resolution == '1m_candle':
        signals['threshold_touch'].append(('minute_candle_surface', 2.0))
    if settlement_fields & {'close', 'high', 'low'}:
        signals['threshold_touch'].append(('candle_resolution_surface', 2.0))
    if 'binance' in source_references:
        signals['threshold_touch'].append(('benchmark_exchange_reference', 1.0))
    if comparator in {'above', 'below', 'over', 'under', 'higher than', 'lower than'}:
        signals['threshold_touch'].append(('threshold_directionality', 1.0))

    if strong_publication_surface_markers & {'opening_weekend', 'opening_day', 'release_date', 'release_window', 'publication_date', 'report_date', 'premiere'}:
        signals['publication_timing'].append(('scheduled_event_surface', 3.0))
    if has_publication_family_anchor and timing_constraint:
        signals['publication_timing'].append(('timing_constraint_language', 2.0))
    if strong_publication_surface_markers & {'box_office', 'earnings', 'publication', 'data_release', 'opens_in_theaters'}:
        signals['publication_timing'].append(('timed_information_event', 2.0))
    elif supporting_publication_markers & {'announcement'} and has_strong_publication_surface:
        signals['publication_timing'].append(('timed_information_event', 1.0))
    if has_publication_family_anchor and dated_window:
        signals['publication_timing'].append(('dated_window_reference', 1.0))

    explicit_source_surface_markers = source_references & {
        'source_of_truth',
        'resolution_source',
        'settlement_source',
        'governing_surface',
    }
    if explicit_source_surface_markers:
        signals['source_resolution'].append(('source_surface_reference', 2.0))
    elif 'official' in source_references and (settlement_fields or time_resolution == '1m_candle'):
        signals['source_resolution'].append(('source_surface_reference', 1.0))
    if settlement_fields:
        signals['source_resolution'].append(('settlement_field_reference', 1.0))
    if time_resolution == '1m_candle' and 'binance' in source_references:
        signals['source_resolution'].append(('exchange_resolution_mapping', 1.0))

    return {family: hits for family, hits in signals.items() if hits}
