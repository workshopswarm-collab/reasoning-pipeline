from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .io import read_json
from .paths import CASES_ROOT, CAUSAL_MAP_ROOT, ORCHESTRATOR_ROOT, to_repo_relative

GENERATED_ROOT = CAUSAL_MAP_ROOT / 'generated'
POST_TREATMENT_REPORT_JSON = GENERATED_ROOT / 'post-treatment-feedback-cycle.json'
PHASE11_REPORT_JSON = GENERATED_ROOT / 'phase11-retrieval-policy-report.json'
RECONCILIATION_JSON = GENERATED_ROOT / 'lmd-causal-runtime-reconciliation.json'
STATUS_JSON = GENERATED_ROOT / 'lmd-causal-runtime-status.json'
GOVERNANCE_JSON = GENERATED_ROOT / 'causal-governance-report.json'
TRIAL_PACKETS_JSON = GENERATED_ROOT / 'proposed-causal-trial-packets.json'
SHADOW_VS_LIVE_JSON = GENERATED_ROOT / 'proposed-causal-shadow-vs-live.json'
TRIGGER_RETRY_QUEUE_PATH = GENERATED_ROOT / 'post-treatment-trigger-retry-queue.jsonl'
AUDIT_FILE_NAME = 'lmd-causal-audit.json'
AUDIT_PATH_RE = re.compile(r'(^|/)lmd-bundle\.json$')
PRIORITY_BONUS_BY_LABEL = {
    'high': 0.08,
    'medium': 0.03,
    'low': 0.0,
    'none': -0.05,
}
RISK_PENALTY_BY_LABEL = {
    'blocked': 0.35,
    'high': 0.12,
    'moderate': 0.0,
    'low': 0.0,
    'none': 0.0,
}
NEGATIVE_CHECK_TEXT = {
    'verify_primary_resolution_source': 'Do not rely on a secondary or assumed source when the contract depends on a specific governing resolution source.',
    'capture_governing_source_proof_when_event_near_complete': 'Do not let near-complete market appearance substitute for captured governing-source proof.',
    'separate_resolution_risk_from_path_probability': 'Do not collapse resolution ambiguity into a pure path-probability discount.',
    'label_unverified_vs_not_occurred_distinctly': 'Do not treat “unverified” as equivalent to “did not occur.”',
    'confirm_any_qualifying_touch_resolves_yes': 'Do not assume the touch mechanic without confirming the exact qualifying-touch rule.',
    'evaluate_distance_to_threshold': 'Do not ignore remaining distance to threshold when inferring touch probability.',
    'evaluate_time_remaining_and_path_volatility': 'Do not price a touch market without checking residual time and plausible path volatility.',
    'justify_any_resistance_discount_explicitly': 'Do not apply a resistance-style discount unless you can justify it explicitly from case evidence.',
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()



def coerce_string(value: Any) -> str:
    if value is None:
        return ''
    return str(value).strip()



def slugify(value: str) -> str:
    text = coerce_string(value).lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text



def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return int(default)



def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return float(default)



def stable_json_dumps(data: Any) -> str:
    return json.dumps(data, sort_keys=True, separators=(',', ':'), default=str)



def sha256_text(text: str) -> str:
    return hashlib.sha256((text or '').encode('utf-8')).hexdigest()



def sha256_jsonable(data: Any) -> str:
    return sha256_text(stable_json_dumps(data))



def resolve_repo_path(path_str: str) -> Path:
    path = Path(path_str)
    if not path.is_absolute():
        path = (ORCHESTRATOR_ROOT / path).resolve()
    return path



def audit_path_for_bundle(bundle_path: str | Path) -> Path:
    path = resolve_repo_path(str(bundle_path))
    return path.with_name(AUDIT_FILE_NAME)



def audit_path_for_bundle_relative(bundle_path: str | Path) -> str:
    return to_repo_relative(audit_path_for_bundle(bundle_path))



def bundle_path_to_repo_relative(bundle_path: str | Path) -> str:
    return to_repo_relative(resolve_repo_path(str(bundle_path)))



def iter_audit_paths(limit: int = 0) -> list[Path]:
    paths = sorted(CASES_ROOT.rglob(AUDIT_FILE_NAME), key=lambda path: path.stat().st_mtime if path.exists() else 0, reverse=True)
    if limit > 0:
        return paths[:limit]
    return paths



def load_audit_rows(limit: int = 0) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in iter_audit_paths(limit=limit):
        payload = read_json(path, default={}) or {}
        if not isinstance(payload, dict):
            continue
        payload.setdefault('audit_path', to_repo_relative(path))
        rows.append(payload)
    return rows



def coverage_metrics_from_bundle(bundle: dict[str, Any]) -> dict[str, Any]:
    results = bundle.get('results') if isinstance(bundle.get('results'), dict) else {}
    causal_context = bundle.get('causal_context') if isinstance(bundle.get('causal_context'), dict) else {}
    counts = {
        'case_review_count': len([row for row in (results.get('case_reviews') or []) if isinstance(row, dict)]),
        'active_intervention_count': len([row for row in (results.get('active_interventions') or []) if isinstance(row, dict)]),
        'aggregate_note_count': len([row for row in (results.get('aggregate_notes') or []) if isinstance(row, dict)]),
        'required_check_count': len([row for row in (results.get('required_checks') or []) if isinstance(row, dict) or isinstance(row, str)]),
        'negative_check_count': len([row for row in (results.get('negative_checks') or []) if isinstance(row, dict) or isinstance(row, str)]),
        'active_node_count': len([row for row in (causal_context.get('active_nodes') or []) if coerce_string(row)]),
        'matched_edge_count': len([row for row in (causal_context.get('matched_edges') or []) if coerce_string(row)]),
        'contested_edge_count': len([row for row in (causal_context.get('contested_edges') or []) if coerce_string(row)]),
    }
    payload_count = counts['case_review_count'] + counts['active_intervention_count'] + counts['aggregate_note_count']
    live_context_count = counts['active_node_count'] + counts['matched_edge_count']
    gap_flags: list[str] = []
    if payload_count == 0:
        gap_flags.append('no_review_or_intervention_payload')
    if counts['case_review_count'] == 0:
        gap_flags.append('no_case_reviews')
    if counts['active_intervention_count'] == 0:
        gap_flags.append('no_active_interventions')
    if live_context_count == 0:
        gap_flags.append('no_live_graph_context')
    if counts['required_check_count'] == 0:
        gap_flags.append('no_required_checks')
    if counts['negative_check_count'] == 0:
        gap_flags.append('no_negative_checks')
    if payload_count == 0 and live_context_count == 0 and counts['required_check_count'] == 0:
        classification = 'empty'
    elif counts['case_review_count'] == 0 and counts['active_intervention_count'] == 0:
        classification = 'weak'
    elif payload_count >= 2 and (live_context_count >= 1 or counts['required_check_count'] >= 2):
        classification = 'strong'
    else:
        classification = 'moderate'
    return {
        'classification': classification,
        'counts': counts,
        'gap_flags': gap_flags,
        'has_meaningful_payload': payload_count > 0,
        'has_live_context': live_context_count > 0,
    }



def case_mix_from_query_profile(profile: dict[str, Any] | None) -> dict[str, Any]:
    profile = profile or {}
    mechanics = sorted({slugify(item) for item in (profile.get('question_mechanics') or []) if slugify(str(item))})
    source_class = slugify(str(profile.get('source_of_truth_class') or ''))
    platform = slugify(str(profile.get('platform') or ''))
    category = slugify(str(profile.get('category') or ''))
    focus_hints = sorted({slugify(str(item)) for item in (profile.get('focus_hints') or []) if slugify(str(item))})
    tags: list[str] = []
    if 'threshold-touch' in mechanics or 'touch-probability' in mechanics:
        tags.append('touch_market')
    if source_class in {'source-specific', 'source_specific', 'governing-source', 'governing_source', 'official-publication', 'official_publication'}:
        tags.append('source_sensitive')
    if 'publication-window' in mechanics or category == 'news':
        tags.append('publication_timing')
    if 'verification-caution' in focus_hints or 'resolution-surface-ambiguity' in focus_hints:
        tags.append('verification_sensitive')
    difficulty = slugify(str(profile.get('difficulty_class') or ''))
    if difficulty:
        tags.append(f'difficulty:{difficulty}')
    resolution_risk = slugify(str(profile.get('resolution_risk') or ''))
    if resolution_risk:
        tags.append(f'resolution_risk:{resolution_risk}')
    return {
        'question_mechanics': mechanics,
        'source_of_truth_class': source_class or None,
        'platform': platform or None,
        'category': category or None,
        'focus_hints': focus_hints,
        'tags': tags,
    }



def negative_checks_from_required_checks(required_checks: list[Any] | None) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row in required_checks or []:
        if isinstance(row, dict):
            check_key = coerce_string(row.get('check_key'))
            reason = coerce_string(row.get('reason'))
            source = coerce_string(row.get('source'))
        else:
            check_key = coerce_string(row)
            reason = ''
            source = ''
        if not check_key or check_key in seen:
            continue
        seen.add(check_key)
        avoid_text = NEGATIVE_CHECK_TEXT.get(check_key, f'Do not skip required verification for {check_key.replace("_", " ")}.')
        out.append({
            'check_key': check_key,
            'avoid': avoid_text,
            'reason': reason or None,
            'source': source or None,
        })
    return out



def summarize_logging_result(payload: dict[str, Any] | None) -> dict[str, Any]:
    payload = payload if isinstance(payload, dict) else {}
    rows = payload.get('rows') if isinstance(payload.get('rows'), list) else None
    matches = payload.get('matches') if isinstance(payload.get('matches'), list) else None
    items = rows if rows is not None else (matches if matches is not None else [])
    inserted = safe_int(payload.get('inserted_count'))
    updated = safe_int(payload.get('updated_count'))
    logged = safe_int(payload.get('logged_count'))
    if items:
        inserted = sum(1 for row in items if isinstance(row, dict) and str(row.get('status') or row.get('action') or '').startswith('insert')) or inserted
        updated = sum(1 for row in items if isinstance(row, dict) and str(row.get('status') or row.get('action') or '').startswith('update')) or updated
        logged = len(items) or logged
    warnings = payload.get('warnings') if isinstance(payload.get('warnings'), list) else []
    return {
        'ran': bool(payload),
        'inserted': inserted,
        'updated': updated,
        'logged_rows': logged,
        'warning_count': len(warnings),
        'warnings': warnings,
    }



def read_json_lines(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for raw in path.read_text(encoding='utf-8').splitlines():
        text = raw.strip()
        if not text:
            continue
        try:
            payload = json.loads(text)
        except Exception:
            continue
        if isinstance(payload, dict):
            rows.append(payload)
    return rows



def write_json_lines(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = '\n'.join(stable_json_dumps(row) for row in rows if isinstance(row, dict))
    if text:
        text += '\n'
    path.write_text(text, encoding='utf-8')



def read_report_generated_at(path: Path) -> str | None:
    payload = read_json(path, default={}) or {}
    if not isinstance(payload, dict):
        return None
    summary = payload.get('summary') if isinstance(payload.get('summary'), dict) else {}
    value = coerce_string(summary.get('generated_at') or payload.get('generated_at'))
    return value or None
