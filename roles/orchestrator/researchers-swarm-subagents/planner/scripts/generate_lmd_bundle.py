#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
SCRIPT_PATH = Path(__file__).resolve()
WORKSPACE_ROOT = SCRIPT_PATH.parents[5]
EVALUATOR_RUNTIME_ROOT = WORKSPACE_ROOT / "roles" / "evaluator" / "runtime"
if str(EVALUATOR_RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(EVALUATOR_RUNTIME_ROOT))

from lib.causal_map import build_edge_record, edge_note_paths, node_note_paths, build_node_record  # noqa: E402
from lib.db import DEFAULT_PSQL, exec_sql, resolve_db_url, table_exists  # noqa: E402
from lib.causal_family_policy import load_family_policies  # noqa: E402
from lib.phase11_retrieval_policy import DEFAULT_POLICY, load_phase11_retrieval_policy, phase11_weight  # noqa: E402
from lib.interventions import build_intervention_record, intervention_note_paths  # noqa: E402
from lib.io import parse_frontmatter, read_json, read_text, write_json  # noqa: E402
from lib.lmd_causal_runtime import (  # noqa: E402
    PRIORITY_BONUS_BY_LABEL,
    RISK_PENALTY_BY_LABEL,
    case_mix_from_query_profile,
    coverage_metrics_from_bundle,
    negative_checks_from_required_checks,
    sha256_jsonable,
)
from lib.paths import case_review_dir, to_repo_relative  # noqa: E402
from lib.proposed_causal_shadow import evaluate_shadow_candidates  # noqa: E402
from lib.proposed_causal_trial_selection import evaluate_trial_candidates  # noqa: E402

CASE_REVIEWS_ROOT = WORKSPACE_ROOT / "qualitative-db" / "50-learnings" / "case-reviews"
LEARNINGS_ROOT = WORKSPACE_ROOT / "qualitative-db" / "50-learnings"

STOPWORDS = {
    'the', 'a', 'an', 'and', 'or', 'of', 'to', 'in', 'on', 'for', 'by', 'at', 'with', 'will', 'be', 'is', 'are',
    'was', 'were', 'has', 'have', 'if', 'not', 'yes', 'no', 'from', 'into', 'only', 'however', 'also', 'again',
    'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'day',
    'week', 'month', 'year', 'end', 'market', 'resolve', 'resolves', 'resolved', 'resolution', 'source', 'sources',
    'specified', 'title', 'price', 'prices', 'higher', 'lower', 'currently', 'available', 'selected', 'please', 'note',
    'about', 'other', 'trading', 'pairs', 'precision', 'determined', 'number', 'timezone', 'date', 'minute', 'candle',
    'candles', 'close', 'final', 'value', 'official', 'general', 'reported', 'primary', 'information', 'effect', 'used',
    'using', 'case', 'cases', 'market', 'question', 'review', 'learning', 'analysis', 'contract',
}

SOURCE_SURFACE_TOKENS = {'binance', 'coinbase', 'cme', 'polymarket', 'kalshi', 'metaculus'}
PUBLICATION_TOKENS = {'report', 'publication', 'released', 'release', 'announce', 'announcement', 'official', 'data'}
MAX_CASE_REVIEWS = 2
MAX_INTERVENTIONS = 2
MAX_AGGREGATE_NOTES = 1
MAX_REQUIRED_CHECKS = 5
GENERATOR_VERSION = 'lmd-generator-v1'
POLICY_VERSION = 'lmd-policy-v1'
PHASE11_RETRIEVAL_POLICY_VERSION = 'phase11-learned-retrieval-v1'
DEFAULT_LIVE_GRAPH_TRIAL_MODE = 'auto'
DEFAULT_RECALLABLE_LIVE_STAGES = ('active',)
TRIAL_RECALLABLE_LIVE_STAGES = ('active', 'trial')
REVIEW_ONLY_LIVE_STAGES = ('draft',)
DISABLED_LIVE_STAGES = ('hold', 'retired', 'archived')

CANDIDATE_STATS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT candidate_id, candidate_type, learned_weight, shrunken_uplift, genericity_penalty, status, status_reason, stats_metadata
  FROM public.lmd_candidate_stats
) t;
'''

EDGE_STATS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT edge_key, learned_weight, shrunken_uplift, supporting_case_count, contested_case_count, genericity_penalty, status, status_reason, stats_metadata
  FROM public.causal_edge_stats
) t;
'''

NODE_STATS_SQL = r'''
SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)::text
FROM (
  SELECT node_key, mechanism_family, lifecycle_stage, learned_weight, shrunken_uplift, supporting_case_count, contested_case_count, helpful_case_count, decay_score, status, status_reason, stats_metadata
  FROM public.causal_node_stats
) t;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate a causal-aware LMD bundle for a research dispatch')
    parser.add_argument('--case-key', required=True)
    parser.add_argument('--market-id', required=True)
    parser.add_argument('--title', required=True)
    parser.add_argument('--description', default='')
    parser.add_argument('--category', default='')
    parser.add_argument('--platform', default='')
    parser.add_argument('--current-price', default='')
    parser.add_argument('--closes-at', default='')
    parser.add_argument('--resolves-at', default='')
    parser.add_argument('--run-kind', default='novel')
    parser.add_argument('--rerun-scope', default='')
    parser.add_argument('--prior-dispatch-count', type=int, default=0)
    parser.add_argument('--prior-case-count', type=int, default=0)
    parser.add_argument('--difficulty-class', default='')
    parser.add_argument('--resolution-risk', default='')
    parser.add_argument('--source-of-truth-class', default='')
    parser.add_argument('--focus-hints-json', default='[]')
    parser.add_argument('--extra-verification-required', default='')
    parser.add_argument('--experiment-arm', default='')
    parser.add_argument('--live-graph-trial-mode', default=DEFAULT_LIVE_GRAPH_TRIAL_MODE)
    parser.add_argument('--generator-version', default=GENERATOR_VERSION)
    parser.add_argument('--policy-version', default=POLICY_VERSION)
    parser.add_argument('--shadow-limit', type=int, default=5)
    parser.add_argument('--trial-limit', type=int, default=2)
    parser.add_argument('--db-url', default='')
    parser.add_argument('--psql', default=DEFAULT_PSQL)
    parser.add_argument('--phase11-policy-path', default='')
    parser.add_argument('--phase11-disable-learned-policy', action='store_true')
    parser.add_argument('--out', help='Optional output path for lmd-bundle.json')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def slugify(value: str) -> str:
    text = (value or '').strip().lower()
    text = text.replace('&', ' and ')
    text = re.sub(r'[\s_/]+', '-', text)
    text = re.sub(r'[^a-z0-9.-]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-.')
    return text


def normalize_tokens(text: str) -> set[str]:
    raw = re.findall(r"[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*", (text or '').lower())
    return {tok for tok in raw if tok not in STOPWORDS and len(tok) >= 3}


def listify(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return []
        if stripped.startswith('[') and stripped.endswith(']'):
            inner = stripped[1:-1].strip()
            if not inner:
                return []
            return [item.strip().strip('"').strip("'") for item in inner.split(',') if item.strip()]
        return [stripped]
    return [str(value).strip()]


def unique(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        stripped = str(item).strip()
        if not stripped or stripped in seen:
            continue
        seen.add(stripped)
        out.append(stripped)
    return out


def first_paragraph(text: str) -> str:
    lines: list[str] = []
    for raw in text.splitlines():
        stripped = raw.strip()
        if not stripped:
            if lines:
                break
            continue
        if stripped.startswith('#') or stripped.startswith('---'):
            continue
        lines.append(stripped.lstrip('- ').strip())
    return ' '.join(lines)[:280]


def parse_json_arg(text: str, default: Any) -> Any:
    try:
        return json.loads(text or '')
    except Exception:
        return default


def parse_boolish(value: str) -> bool:
    return str(value or '').strip().lower() in {'1', 'true', 'yes', 'on'}


def parse_iso(value: str) -> datetime | None:
    raw = str(value or '').strip()
    if not raw:
        return None
    raw = raw.replace('Z', '+00:00')
    try:
        dt = datetime.fromisoformat(raw)
    except Exception:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def hours_until(deadline: str) -> float | None:
    dt = parse_iso(deadline)
    if not dt:
        return None
    return (dt - datetime.now(timezone.utc)).total_seconds() / 3600.0


def parse_threshold_from_title(title: str) -> float | None:
    match = re.search(r'\$\s*([0-9][0-9,]*(?:\.\d+)?)', title or '')
    if not match:
        return None
    try:
        return float(match.group(1).replace(',', ''))
    except Exception:
        return None


def parse_float(value: str) -> float | None:
    raw = str(value or '').strip().replace(',', '')
    if not raw:
        return None
    try:
        return float(raw)
    except Exception:
        return None


def lifecycle_stage(record: dict[str, Any]) -> str:
    stage = slugify(str(record.get('lifecycle_stage') or ''))
    if stage:
        return stage
    status = slugify(str(record.get('status') or ''))
    allowed = set(DEFAULT_RECALLABLE_LIVE_STAGES) | set(TRIAL_RECALLABLE_LIVE_STAGES) | set(REVIEW_ONLY_LIVE_STAGES) | set(DISABLED_LIVE_STAGES)
    if status in allowed:
        return status
    return 'draft'


def resolve_live_graph_trial_mode(args: argparse.Namespace) -> str:
    requested = slugify(str(getattr(args, 'live_graph_trial_mode', DEFAULT_LIVE_GRAPH_TRIAL_MODE) or DEFAULT_LIVE_GRAPH_TRIAL_MODE))
    if requested in {'', 'auto'}:
        assignment_arm = slugify(str(getattr(args, 'experiment_arm', '') or ''))
        return 'treatment' if assignment_arm == 'treatment' else 'off'
    if requested in {'off', 'treatment', 'trial', 'shadow'}:
        return requested
    return 'off'


def recallable_live_stages(trial_mode: str) -> set[str]:
    if trial_mode in {'treatment', 'trial', 'shadow'}:
        return set(TRIAL_RECALLABLE_LIVE_STAGES)
    return set(DEFAULT_RECALLABLE_LIVE_STAGES)


def stage_counts(records: dict[str, dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for record in records.values():
        stage = lifecycle_stage(record)
        counts[stage] = counts.get(stage, 0) + 1
    return {key: counts[key] for key in sorted(counts)}


def build_node_metadata(node_key: str, record: dict[str, Any]) -> dict[str, Any]:
    return {
        'node_key': node_key,
        'node_label': str(record.get('node_label') or record.get('label') or node_key).strip(),
        'lifecycle_stage': lifecycle_stage(record),
        'status': str(record.get('status') or '').strip(),
        'source_kind': str(record.get('source_kind') or '').strip(),
        'mechanism_family': str(record.get('mechanism_family') or '').strip(),
        'path': str(record.get('path') or '').strip(),
    }


def build_edge_metadata(edge_key: str, record: dict[str, Any]) -> dict[str, Any]:
    return {
        'edge_key': edge_key,
        'edge_label': str(record.get('edge_label') or record.get('label') or edge_key).strip(),
        'lifecycle_stage': lifecycle_stage(record),
        'status': str(record.get('status') or '').strip(),
        'source_kind': str(record.get('source_kind') or '').strip(),
        'mechanism_family': str(record.get('mechanism_family') or '').strip(),
        'confidence_mode': str(record.get('confidence_mode') or '').strip(),
        'path': str(record.get('path') or '').strip(),
    }


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



def family_priority_bonus(policy: dict[str, Any] | None) -> float:
    notes = (policy or {}).get('notes') or {}
    priority = slugify(str(notes.get('priority') or ''))
    return float(PRIORITY_BONUS_BY_LABEL.get(priority, 0.0))



def family_risk_penalty(policy: dict[str, Any] | None) -> float:
    notes = (policy or {}).get('notes') or {}
    risk = slugify(str(notes.get('default_risk') or ''))
    return float(RISK_PENALTY_BY_LABEL.get(risk, 0.0))



def quantile(values: list[float], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * fraction))))
    return float(ordered[idx])


def build_metric_profile(values: list[float]) -> dict[str, float]:
    clean = sorted(float(value) for value in values if value is not None)
    if not clean:
        return {'count': 0, 'min': 0.0, 'p10': 0.0, 'p25': 0.0, 'p50': 0.0, 'p75': 0.0, 'p90': 0.0, 'max': 0.0, 'mean': 0.0}
    return {
        'count': float(len(clean)),
        'min': float(clean[0]),
        'p10': quantile(clean, 0.10),
        'p25': quantile(clean, 0.25),
        'p50': quantile(clean, 0.50),
        'p75': quantile(clean, 0.75),
        'p90': quantile(clean, 0.90),
        'max': float(clean[-1]),
        'mean': float(sum(clean) / len(clean)),
    }


def normalized_reward(value: float, profile: dict[str, float] | None) -> float:
    numeric = float(value)
    if numeric <= 0:
        return 0.0
    profile = profile or {}
    low = max(0.0, safe_float(profile.get('p25'), profile.get('p50')))
    high = max(low + 1e-6, safe_float(profile.get('p90'), profile.get('max')))
    if high <= low + 1e-6:
        fallback = max(1.0, abs(numeric), safe_float(profile.get('max')))
        return round(min(1.5, max(0.0, numeric / fallback)), 3)
    return round(min(1.5, max(0.0, (numeric - low) / (high - low))), 3)


def normalized_penalty(value: float, profile: dict[str, float] | None) -> float:
    numeric = float(value)
    if numeric <= 0:
        return 0.0
    profile = profile or {}
    low = max(0.0, safe_float(profile.get('p50'), profile.get('p25')))
    high = max(low + 1e-6, safe_float(profile.get('p90'), profile.get('max')))
    if high <= low + 1e-6:
        fallback = max(1.0, abs(numeric), safe_float(profile.get('max')))
        return round(min(1.5, max(0.0, numeric / fallback)), 3)
    return round(min(1.5, max(0.0, (numeric - low) / (high - low))), 3)


def build_stats_distribution_profiles(
    candidate_stats: dict[str, dict[str, Any]],
    edge_stats: dict[str, dict[str, Any]],
    node_stats: dict[str, dict[str, Any]],
) -> dict[str, dict[str, dict[str, float]]]:
    def positive_values(rows: list[dict[str, Any]], field: str) -> list[float]:
        out: list[float] = []
        for row in rows:
            value = safe_float(row.get(field))
            if value > 0:
                out.append(value)
        return out

    def negative_magnitudes(rows: list[dict[str, Any]], field: str) -> list[float]:
        out: list[float] = []
        for row in rows:
            value = safe_float(row.get(field))
            if value < 0:
                out.append(abs(value))
        return out

    def field_values(rows: list[dict[str, Any]], field: str) -> list[float]:
        out: list[float] = []
        for row in rows:
            value = row.get(field)
            if value in (None, ''):
                continue
            out.append(safe_float(value))
        return out

    candidate_rows = list(candidate_stats.values())
    edge_rows = list(edge_stats.values())
    node_rows = list(node_stats.values())

    return {
        'candidate': {
            'positive_learned_weight': build_metric_profile(positive_values(candidate_rows, 'learned_weight')),
            'positive_shrunken_uplift': build_metric_profile(positive_values(candidate_rows, 'shrunken_uplift')),
            'genericity_penalty': build_metric_profile(field_values(candidate_rows, 'genericity_penalty')),
        },
        'edge': {
            'positive_learned_weight': build_metric_profile(positive_values(edge_rows, 'learned_weight')),
            'negative_learned_weight': build_metric_profile(negative_magnitudes(edge_rows, 'learned_weight')),
            'positive_shrunken_uplift': build_metric_profile(positive_values(edge_rows, 'shrunken_uplift')),
            'negative_shrunken_uplift': build_metric_profile(negative_magnitudes(edge_rows, 'shrunken_uplift')),
            'supporting_case_count': build_metric_profile(field_values(edge_rows, 'supporting_case_count')),
            'contested_case_count': build_metric_profile(field_values(edge_rows, 'contested_case_count')),
            'decay_score': build_metric_profile(field_values(edge_rows, 'decay_score')),
        },
        'node': {
            'positive_learned_weight': build_metric_profile(positive_values(node_rows, 'learned_weight')),
            'negative_learned_weight': build_metric_profile(negative_magnitudes(node_rows, 'learned_weight')),
            'positive_shrunken_uplift': build_metric_profile(positive_values(node_rows, 'shrunken_uplift')),
            'negative_shrunken_uplift': build_metric_profile(negative_magnitudes(node_rows, 'shrunken_uplift')),
            'supporting_case_count': build_metric_profile(field_values(node_rows, 'supporting_case_count')),
            'contested_case_count': build_metric_profile(field_values(node_rows, 'contested_case_count')),
            'helpful_case_count': build_metric_profile(field_values(node_rows, 'helpful_case_count')),
            'decay_score': build_metric_profile(field_values(node_rows, 'decay_score')),
        },
    }


def query_live_score_profile(query_profile: dict[str, Any]) -> dict[str, float]:
    values: list[float] = []
    for row in (query_profile.get('active_node_metadata') or []):
        if isinstance(row, dict):
            values.append(safe_float(row.get('phase11_retrieval_score')))
    for row in (query_profile.get('candidate_edge_metadata') or []):
        if isinstance(row, dict):
            values.append(safe_float(row.get('phase11_retrieval_score')))
    return build_metric_profile([value for value in values if value > 0])


def build_live_family_state(nodes: dict[str, dict[str, Any]], edges: dict[str, dict[str, Any]]) -> dict[str, dict[str, int]]:
    state: dict[str, dict[str, int]] = {}
    for record in list(nodes.values()) + list(edges.values()):
        family = str(record.get('mechanism_family') or 'unassigned').strip() or 'unassigned'
        stage = lifecycle_stage(record)
        row = state.setdefault(family, {'trial_total': 0, 'active_nodes': 0, 'active_edges': 0})
        if stage == 'trial':
            row['trial_total'] += 1
        if stage == 'active':
            if 'node_key' in record:
                row['active_nodes'] += 1
            else:
                row['active_edges'] += 1
    return {key: state[key] for key in sorted(state)}


def family_policy_caps_for_bundle(family_policies: dict[str, dict[str, Any]]) -> dict[str, dict[str, int]]:
    caps: dict[str, dict[str, int]] = {}
    for family, policy in family_policies.items():
        caps[family] = {
            'max_trial_candidates': safe_int(policy.get('max_trial_candidates')),
            'max_active_nodes': safe_int(policy.get('max_active_nodes')),
            'max_active_edges': safe_int(policy.get('max_active_edges')),
        }
    return caps


def family_crowding_metrics(
    family: str,
    *,
    stage: str,
    entity_type: str,
    family_state: dict[str, dict[str, int]],
    family_policies: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    policy = family_policies.get(family) or family_policies.get('unassigned') or {}
    counts = family_state.get(family) or {'trial_total': 0, 'active_nodes': 0, 'active_edges': 0}
    if stage == 'trial':
        current = safe_int(counts.get('trial_total'))
        limit = safe_int(policy.get('max_trial_candidates'))
    elif entity_type == 'node':
        current = safe_int(counts.get('active_nodes'))
        limit = safe_int(policy.get('max_active_nodes'))
    else:
        current = safe_int(counts.get('active_edges'))
        limit = safe_int(policy.get('max_active_edges'))
    if limit <= 0:
        penalty = 0.75 if current > 0 else 0.0
        ratio = None
    else:
        ratio = round(current / float(limit), 3)
        if ratio > 1.0:
            penalty = round(0.6 + (ratio - 1.0) * 0.35, 3)
        elif ratio >= 1.0:
            penalty = 0.35
        elif ratio >= 0.75:
            penalty = round(0.12 + (ratio - 0.75) * 0.48, 3)
        else:
            penalty = 0.0
    return {
        'current': current,
        'limit': limit,
        'ratio': ratio,
        'penalty': penalty,
        'enabled': bool(policy.get('enabled', True)),
    }


def live_graph_priority_metadata(
    *,
    entity_type: str,
    key: str,
    record: dict[str, Any],
    stats_row: dict[str, Any] | None,
    family_state: dict[str, dict[str, int]],
    family_policies: dict[str, dict[str, Any]],
    distribution_profiles: dict[str, dict[str, dict[str, float]]] | None = None,
    phase11_policy: dict[str, Any] | None = None,
) -> dict[str, Any]:
    stats = stats_row or {}
    stats_metadata = stats.get('stats_metadata') or {}
    if not isinstance(stats_metadata, dict):
        stats_metadata = {}
    distribution_profiles = distribution_profiles or {}
    phase11_policy = phase11_policy or {}
    entity_profiles = distribution_profiles.get(entity_type) or {}
    stage = lifecycle_stage(record)
    family = str(record.get('mechanism_family') or stats.get('mechanism_family') or 'unassigned').strip() or 'unassigned'
    support_count = safe_int(stats.get('supporting_case_count'), stats.get('matched_case_count'), stats.get('projected_case_count'))
    contested_count = safe_int(stats.get('contested_case_count'))
    helpful_count = safe_int(stats.get('helpful_case_count'), stats_metadata.get('helpful_case_count'))
    learned_weight = safe_float(stats.get('learned_weight'))
    shrunken_uplift = safe_float(stats.get('shrunken_uplift'))
    decay_score = safe_float(stats.get('decay_score'), record.get('decay_score'))
    stats_status = slugify(str(stats.get('status') or record.get('status') or ''))
    crowding = family_crowding_metrics(
        family,
        stage=stage,
        entity_type=entity_type,
        family_state=family_state,
        family_policies=family_policies,
    )
    family_policy = family_policies.get(family) or family_policies.get('unassigned') or {}
    trust_bonus = phase11_weight(phase11_policy, 'live_graph', entity_type, 'trust_tier_bonus', 'active_reviewed' if stage == 'active' else ('trial_experimental' if stage == 'trial' else 'review_only'), default=0.45 if stage == 'active' else (0.12 if stage == 'trial' else -0.18))
    status_penalty = 0.0 if stats_status in {'', stage, 'active'} else phase11_weight(phase11_policy, 'live_graph', entity_type, 'status_penalty', 'hold_or_draft' if stats_status in {'draft', 'hold'} else 'retired_or_archived', default=0.28 if stats_status in {'draft', 'hold'} else 0.45)
    breakdown = {
        'learned_weight_bonus': round(phase11_weight(phase11_policy, 'live_graph', entity_type, 'learned_weight_bonus', default=1.25) * normalized_reward(max(0.0, learned_weight), entity_profiles.get('positive_learned_weight')), 3),
        'negative_weight_penalty': round(phase11_weight(phase11_policy, 'live_graph', entity_type, 'negative_weight_penalty', default=1.35) * normalized_penalty(max(0.0, -learned_weight), entity_profiles.get('negative_learned_weight')), 3),
        'uplift_bonus': round(phase11_weight(phase11_policy, 'live_graph', entity_type, 'uplift_bonus', default=1.10) * normalized_reward(max(0.0, shrunken_uplift), entity_profiles.get('positive_shrunken_uplift')), 3),
        'negative_uplift_penalty': round(phase11_weight(phase11_policy, 'live_graph', entity_type, 'negative_uplift_penalty', default=1.15) * normalized_penalty(max(0.0, -shrunken_uplift), entity_profiles.get('negative_shrunken_uplift')), 3),
        'support_bonus': round(phase11_weight(phase11_policy, 'live_graph', entity_type, 'support_bonus', default=0.70) * normalized_reward(float(support_count), entity_profiles.get('supporting_case_count')), 3),
        'helpful_bonus': round(phase11_weight(phase11_policy, 'live_graph', entity_type, 'helpful_bonus', default=0.45) * normalized_reward(float(helpful_count), entity_profiles.get('helpful_case_count')), 3),
        'trust_tier_bonus': trust_bonus,
        'family_priority_bonus': round(family_priority_bonus(family_policy), 3),
        'contestation_penalty': round(phase11_weight(phase11_policy, 'live_graph', entity_type, 'contestation_penalty', default=0.80) * normalized_penalty(float(contested_count), entity_profiles.get('contested_case_count')), 3),
        'decay_penalty': round(phase11_weight(phase11_policy, 'live_graph', entity_type, 'decay_penalty', default=0.70) * normalized_penalty(decay_score, entity_profiles.get('decay_score')), 3),
        'family_crowding_penalty': round(phase11_weight(phase11_policy, 'live_graph', entity_type, 'family_crowding_penalty', default=0.90) * float(crowding.get('penalty') or 0.0), 3),
        'family_risk_penalty': round(family_risk_penalty(family_policy), 3),
        'status_penalty': round(status_penalty, 3),
    }
    score = round(
        breakdown['learned_weight_bonus']
        + breakdown['uplift_bonus']
        + breakdown['support_bonus']
        + breakdown['helpful_bonus']
        + breakdown['trust_tier_bonus']
        + breakdown['family_priority_bonus']
        - breakdown['negative_weight_penalty']
        - breakdown['negative_uplift_penalty']
        - breakdown['contestation_penalty']
        - breakdown['decay_penalty']
        - breakdown['family_crowding_penalty']
        - breakdown['family_risk_penalty']
        - breakdown['status_penalty'],
        3,
    )
    return {
        'phase11_retrieval_score': score,
        'phase11_score_breakdown': breakdown,
        'phase11_trust_tier': 'active_reviewed' if stage == 'active' else ('trial_experimental' if stage == 'trial' else 'review_only'),
        'phase11_family_crowding': crowding,
    }


def candidate_stat_bonus(
    stats_row: dict[str, Any] | None,
    distribution_profiles: dict[str, dict[str, dict[str, float]]] | None = None,
    phase11_policy: dict[str, Any] | None = None,
    *,
    profile_key: str = 'candidate',
) -> float:
    row = stats_row or {}
    distribution_profiles = distribution_profiles or {}
    phase11_policy = phase11_policy or {}
    profiles = distribution_profiles.get(profile_key) or {}
    learned_weight = safe_float(row.get('learned_weight'))
    shrunken_uplift = safe_float(row.get('shrunken_uplift'))
    genericity_penalty = safe_float(row.get('genericity_penalty'))
    status = slugify(str(row.get('status') or ''))
    status_penalty = phase11_weight(phase11_policy, 'candidate_bonus', 'status_penalty', default=0.18) if status in {'hold', 'retired', 'archived'} else 0.0
    return round(
        phase11_weight(phase11_policy, 'candidate_bonus', 'learned_weight_bonus', default=0.95) * normalized_reward(max(0.0, learned_weight), profiles.get('positive_learned_weight'))
        + phase11_weight(phase11_policy, 'candidate_bonus', 'shrunken_uplift_bonus', default=0.70) * normalized_reward(max(0.0, shrunken_uplift), profiles.get('positive_shrunken_uplift'))
        - phase11_weight(phase11_policy, 'candidate_bonus', 'genericity_penalty', default=0.35) * normalized_penalty(genericity_penalty, profiles.get('genericity_penalty'))
        - status_penalty,
        3,
    )


def metadata_score_lookup(rows: list[dict[str, Any]], key_field: str) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        key = str(row.get(key_field) or '').strip()
        if key:
            out[key] = row
    return out


def infer_live_query_context(
    args: argparse.Namespace,
    nodes: dict[str, dict[str, Any]],
    edges: dict[str, dict[str, Any]],
    *,
    trial_mode: str = 'off',
    node_stats: dict[str, dict[str, Any]] | None = None,
    edge_stats: dict[str, dict[str, Any]] | None = None,
    family_state: dict[str, dict[str, int]] | None = None,
    family_policies: dict[str, dict[str, Any]] | None = None,
    distribution_profiles: dict[str, dict[str, dict[str, float]]] | None = None,
    phase11_policy: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    title = args.title or ''
    description = args.description or ''
    text = f"{title}\n{description}"
    text_lower = text.lower()
    focus_hints = [str(item).strip() for item in parse_json_arg(args.focus_hints_json, []) if str(item).strip()]
    source_truth = str(args.source_of_truth_class or '').strip()
    threshold = parse_threshold_from_title(title)
    current_price = parse_float(args.current_price)
    hours_left = hours_until(args.closes_at or args.resolves_at or '')
    recallable_stages = recallable_live_stages(trial_mode)

    question_mechanics: list[str] = []
    if any(token in text_lower for token in ['reach $', 'reach ', 'touch ', 'hit $', '1-minute high', '1 minute high']):
        question_mechanics.extend(['threshold-touch', 'intraperiod-high-low'])
    if any(token in text_lower for token in PUBLICATION_TOKENS):
        question_mechanics.extend(['publication-timing', 'scheduled-publication'])
    question_mechanics = unique(question_mechanics)

    active_nodes: list[str] = []
    node_reasons: dict[str, list[str]] = {}
    suppressed_node_reasons: dict[str, list[str]] = {}

    def activate(node_key: str, reason: str) -> None:
        if node_key not in nodes:
            return
        stage = lifecycle_stage(nodes[node_key])
        if stage not in recallable_stages:
            suppressed_node_reasons.setdefault(node_key, [])
            rendered = f"{reason} [stage={stage}]"
            if rendered not in suppressed_node_reasons[node_key]:
                suppressed_node_reasons[node_key].append(rendered)
            return
        if node_key not in active_nodes:
            active_nodes.append(node_key)
        node_reasons.setdefault(node_key, [])
        if reason not in node_reasons[node_key]:
            node_reasons[node_key].append(reason)

    near_threshold = False
    if threshold is not None and current_price is not None and threshold > 0:
        gap_ratio = abs(current_price - threshold) / threshold
        if gap_ratio <= 0.015:
            near_threshold = True
    if near_threshold and 'threshold-touch' in question_mechanics:
        activate('price-near-threshold', 'current_price_within_1.5pct_of_threshold')
    if hours_left is not None and hours_left >= 12:
        activate('time-remaining-nontrivial', f'hours_until_close={round(hours_left,1)}')
    if 'threshold-touch' in question_mechanics and (near_threshold or (hours_left is not None and hours_left >= 12)):
        activate('touch-probability', 'threshold_touch_with_near_threshold_or_time_window')

    source_specific = False
    if source_truth.startswith('authoritative') or any(tok in text_lower for tok in SOURCE_SURFACE_TOKENS):
        source_specific = True
        activate('settlement-source-specificity', 'authoritative_source_or_named_surface')
    extra_verification = parse_boolish(args.extra_verification_required) or any(
        hint in {'source_of_truth_check', 'extra_verification'} for hint in focus_hints
    )
    if source_specific and extra_verification:
        activate('resolution-surface-ambiguity', 'source_specific_with_extra_verification')
        activate('verification-caution', 'source_specific_with_extra_verification')

    if 'publication-timing' in question_mechanics:
        activate('publication-window-timing', 'publication_tokens_in_title_or_description')
        if extra_verification or 'authoritative' in source_truth or 'consensus' in source_truth:
            activate('reporting-state-uncertainty', 'publication_timing_with_reporting_surface_uncertainty')

    candidate_edges: list[str] = []
    contested_edges: list[str] = []
    suppressed_edge_reasons: dict[str, list[str]] = {}

    def edge_if_present(edge_key: str, condition: bool, reason: str) -> None:
        if not condition or edge_key not in edges:
            return
        stage = lifecycle_stage(edges[edge_key])
        if stage not in recallable_stages:
            suppressed_edge_reasons.setdefault(edge_key, [])
            rendered = f"{reason} [stage={stage}]"
            if rendered not in suppressed_edge_reasons[edge_key]:
                suppressed_edge_reasons[edge_key].append(rendered)
            return
        if edge_key not in candidate_edges:
            candidate_edges.append(edge_key)
    edge_if_present('price-near-threshold__increases__touch-probability', 'price-near-threshold' in active_nodes, 'node_active')
    edge_if_present('time-remaining-nontrivial__increases__touch-probability', 'time-remaining-nontrivial' in active_nodes and 'touch-probability' in active_nodes, 'node_active')
    edge_if_present('settlement-source-specificity__increases__resolution-surface-ambiguity', 'settlement-source-specificity' in active_nodes and 'resolution-surface-ambiguity' in active_nodes, 'node_active')
    edge_if_present('resolution-surface-ambiguity__increases__verification-caution', 'resolution-surface-ambiguity' in active_nodes and 'verification-caution' in active_nodes, 'node_active')
    edge_if_present('verification-caution__increases__fair-value-discounting-pressure', 'verification-caution' in active_nodes and 'threshold-touch' in question_mechanics and near_threshold, 'heuristic:possible_overdiscount_risk')
    edge_if_present('publication-window-timing__increases__reporting-state-uncertainty', 'publication-window-timing' in active_nodes and 'reporting-state-uncertainty' in active_nodes, 'node_active')

    if 'verification-caution__increases__fair-value-discounting-pressure' in candidate_edges:
        contested_edges.append('verification-caution__increases__fair-value-discounting-pressure')

    required_checks: list[dict[str, Any]] = []
    def add_check(check_key: str, reason: str, source: str) -> None:
        row = {'check_key': check_key, 'reason': reason, 'source': source}
        if row not in required_checks:
            required_checks.append(row)

    if 'settlement-source-specificity' in active_nodes or 'resolution-surface-ambiguity' in active_nodes:
        add_check('verify_primary_resolution_source', 'mechanism_risk:source_specific_settlement', 'heuristic:source_specific_settlement')
        add_check('capture_governing_source_proof_when_event_near_complete', 'mechanism_risk:resolution_surface_ambiguity', 'heuristic:resolution_surface_ambiguity')
    if 'price-near-threshold' in active_nodes or 'touch-probability' in active_nodes:
        add_check('confirm_any_qualifying_touch_resolves_yes', 'mechanism_risk:touch_mechanics', 'heuristic:touch_mechanics')
        add_check('evaluate_distance_to_threshold', 'mechanism_risk:threshold_proximity', 'heuristic:threshold_proximity')
        add_check('evaluate_time_remaining_and_path_volatility', 'mechanism_risk:residual_window', 'heuristic:residual_window')
    if contested_edges:
        add_check('separate_resolution_risk_from_path_probability', 'contested_edge:verification-caution__increases__fair-value-discounting-pressure', 'heuristic:contested_edge')
        add_check('label_unverified_vs_not_occurred_distinctly', 'contested_edge:verification-caution__increases__fair-value-discounting-pressure', 'heuristic:contested_edge')
        add_check('justify_any_resistance_discount_explicitly', 'contested_edge:verification-caution__increases__fair-value-discounting-pressure', 'heuristic:contested_edge')

    priority = {
        'verify_primary_resolution_source': 10,
        'capture_governing_source_proof_when_event_near_complete': 20,
        'separate_resolution_risk_from_path_probability': 30,
        'label_unverified_vs_not_occurred_distinctly': 40,
        'confirm_any_qualifying_touch_resolves_yes': 50,
        'evaluate_distance_to_threshold': 60,
        'evaluate_time_remaining_and_path_volatility': 70,
        'justify_any_resistance_discount_explicitly': 80,
    }
    required_checks = sorted(required_checks, key=lambda row: (priority.get(row['check_key'], 999), row['check_key']))[:MAX_REQUIRED_CHECKS]

    node_stats = node_stats or {}
    edge_stats = edge_stats or {}
    family_state = family_state or {}
    family_policies = family_policies or {'unassigned': {'enabled': False}}
    distribution_profiles = distribution_profiles or {}
    phase11_policy = phase11_policy or {}

    active_node_metadata = []
    for node_key in active_nodes:
        if node_key not in nodes:
            continue
        metadata = build_node_metadata(node_key, nodes[node_key])
        metadata.update(
            live_graph_priority_metadata(
                entity_type='node',
                key=node_key,
                record=nodes[node_key],
                stats_row=node_stats.get(node_key),
                family_state=family_state,
                family_policies=family_policies,
                distribution_profiles=distribution_profiles,
                phase11_policy=phase11_policy,
            )
        )
        active_node_metadata.append(metadata)
    active_node_metadata.sort(key=lambda row: (-safe_float(row.get('phase11_retrieval_score')), row.get('node_key') or ''))
    active_nodes = [str(row.get('node_key') or '').strip() for row in active_node_metadata if str(row.get('node_key') or '').strip()]

    candidate_edge_metadata = []
    for edge_key in candidate_edges:
        if edge_key not in edges:
            continue
        metadata = build_edge_metadata(edge_key, edges[edge_key])
        metadata.update(
            live_graph_priority_metadata(
                entity_type='edge',
                key=edge_key,
                record=edges[edge_key],
                stats_row=edge_stats.get(edge_key),
                family_state=family_state,
                family_policies=family_policies,
                distribution_profiles=distribution_profiles,
                phase11_policy=phase11_policy,
            )
        )
        candidate_edge_metadata.append(metadata)
    candidate_edge_metadata.sort(key=lambda row: (-safe_float(row.get('phase11_retrieval_score')), row.get('edge_key') or ''))
    candidate_edges = [str(row.get('edge_key') or '').strip() for row in candidate_edge_metadata if str(row.get('edge_key') or '').strip()]

    query_profile = {
        'run_kind': args.run_kind,
        'rerun_scope': args.rerun_scope,
        'prior_dispatch_count': args.prior_dispatch_count,
        'prior_case_count': args.prior_case_count,
        'difficulty_class': args.difficulty_class,
        'resolution_risk': args.resolution_risk,
        'source_of_truth_class': source_truth,
        'focus_hints': focus_hints,
        'suppress_same_case': True,
        'question_mechanics': question_mechanics,
        'active_nodes': active_nodes,
        'active_node_metadata': active_node_metadata,
        'candidate_edges': candidate_edges,
        'candidate_edge_metadata': candidate_edge_metadata,
        'contested_edges': sorted(contested_edges),
        'required_checks': required_checks,
        'category': args.category,
        'platform': args.platform,
        'live_graph_trial_mode': trial_mode,
        'live_graph_trial_enabled': trial_mode in {'treatment', 'trial', 'shadow'},
        'live_graph_recallable_stages': sorted(recallable_stages),
    }
    query_profile['query_text'] = ' '.join(part for part in [title, description, ' '.join(focus_hints)] if part).strip()
    return query_profile, {
        'node_reasons': node_reasons,
        'suppressed_node_reasons': suppressed_node_reasons,
        'suppressed_edge_reasons': suppressed_edge_reasons,
        'hours_left': [str(round(hours_left, 1))] if hours_left is not None else [],
        'live_graph_trial_mode': trial_mode,
        'live_graph_stage_counts': {
            'nodes': stage_counts(nodes),
            'edges': stage_counts(edges),
        },
    }


def load_case_review_candidates(current_case_key: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    if not CASE_REVIEWS_ROOT.exists():
        return items
    for case_dir in sorted(path for path in CASE_REVIEWS_ROOT.iterdir() if path.is_dir() and path.name.startswith('case-')):
        review_path = case_dir / 'review.md'
        packet_path = case_dir / 'learning-packet.json'
        projection_path = case_dir / 'causal-projection.json'
        if not review_path.exists() or not packet_path.exists():
            continue
        review_text = read_text(review_path)
        frontmatter = parse_frontmatter(review_text)
        packet = read_json(packet_path, default={}) or {}
        case_key = str(packet.get('case_key') or frontmatter.get('case_key') or case_dir.name).strip()
        if case_key == current_case_key:
            continue
        tags = set(listify(frontmatter.get('tags')))
        status = 'draft' if 'evaluator/draft' in tags else ('reviewed' if (packet.get('market_truth') or {}).get('resolution_status') == 'resolved' else 'draft')
        if status not in {'reviewed', 'active'}:
            continue
        projection = read_json(projection_path, default={}) or {}
        projection_meta = projection.get('projection_metadata') or {}
        case_context = projection_meta.get('case_context') or {}
        topic = str(frontmatter.get('topic') or frontmatter.get('question') or packet.get('title') or '')
        summary = first_paragraph(review_text)
        items.append({
            'case_key': case_key,
            'status': status,
            'review_path': to_repo_relative(review_path),
            'packet_path': to_repo_relative(packet_path),
            'projection_path': to_repo_relative(projection_path) if projection_path.exists() else '',
            'error_pattern': str(frontmatter.get('error_pattern') or ''),
            'platform': str(packet.get('platform') or ''),
            'category': str(packet.get('category') or frontmatter.get('market_category') or ''),
            'question': str(frontmatter.get('question') or packet.get('title') or ''),
            'topic': topic,
            'summary': summary,
            'active_nodes': projection.get('active_nodes') or [],
            'candidate_edges': projection.get('candidate_edges') or [],
            'contested_edges': projection.get('contested_edges') or [],
            'required_checks': projection.get('required_checks') or [],
            'question_mechanics': case_context.get('question_mechanics') or listify(frontmatter.get('subdomain')),
            'source_of_truth_class': case_context.get('source_of_truth_class') or [],
            'related_drivers': listify(frontmatter.get('related_drivers')),
            'related_entities': listify(frontmatter.get('related_entities')),
            'title_text': ' '.join(part for part in [topic, summary, str(frontmatter.get('question') or '')] if part),
        })
    return items


def overlap_list(left: list[str], right: list[str]) -> list[str]:
    left_norm = {slugify(item): item for item in left if str(item).strip()}
    matched: list[str] = []
    for item in right:
        key = slugify(str(item))
        if key in left_norm and left_norm[key] not in matched:
            matched.append(left_norm[key])
    return matched


def semantic_similarity(query_text: str, candidate_text: str) -> float:
    q = normalize_tokens(query_text)
    c = normalize_tokens(candidate_text)
    if not q or not c:
        return 0.0
    overlap = len(q & c)
    denom = math.sqrt(len(q)) * math.sqrt(len(c))
    if denom <= 0:
        return 0.0
    surface_overlap = len((q & SOURCE_SURFACE_TOKENS) & (c & SOURCE_SURFACE_TOKENS))
    return round((overlap / denom) * 3.0 + surface_overlap * 0.5, 3)


def shortlist_case_reviews(
    query_profile: dict[str, Any],
    candidates: list[dict[str, Any]],
    candidate_stats: dict[str, dict[str, Any]],
    edge_stats: dict[str, dict[str, Any]],
    node_stats: dict[str, dict[str, Any]],
    distribution_profiles: dict[str, dict[str, dict[str, float]]] | None = None,
    phase11_policy: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    query_text = query_profile.get('query_text') or ''
    node_metadata = metadata_score_lookup(query_profile.get('active_node_metadata') or [], 'node_key')
    edge_metadata = metadata_score_lookup(query_profile.get('candidate_edge_metadata') or [], 'edge_key')
    results: list[dict[str, Any]] = []
    for candidate in candidates:
        shared_nodes = overlap_list(query_profile.get('active_nodes') or [], candidate.get('active_nodes') or [])
        shared_edges = overlap_list(query_profile.get('candidate_edges') or [], candidate.get('candidate_edges') or [])
        shared_mechanics = overlap_list(query_profile.get('question_mechanics') or [], candidate.get('question_mechanics') or [])
        shared_source = overlap_list([query_profile.get('source_of_truth_class') or ''], candidate.get('source_of_truth_class') or [])
        has_structural_match = bool(shared_nodes or shared_edges or shared_mechanics or shared_source)
        if not has_structural_match:
            continue
        mech_score = len(shared_nodes) * 3.0 + len(shared_edges) * 4.0
        source_score = len(shared_source) * 2.5
        mechanic_score = len(shared_mechanics) * 2.0
        category_score = 0.75 if slugify(candidate.get('category') or '') == slugify(query_profile.get('category') or '') else 0.0
        semantic_score = semantic_similarity(query_text, candidate.get('title_text') or '')
        node_weight_score = round(sum(max(0.0, safe_float((node_stats.get(node_key) or {}).get('learned_weight'))) for node_key in shared_nodes), 3)
        edge_weight_score = round(sum(max(0.0, safe_float((edge_stats.get(edge_key) or {}).get('learned_weight'))) for edge_key in shared_edges), 3)
        phase11_node_bonus = round(sum(max(0.0, safe_float((node_metadata.get(node_key) or {}).get('phase11_retrieval_score'))) * 0.2 for node_key in shared_nodes), 3)
        phase11_edge_bonus = round(sum(max(0.0, safe_float((edge_metadata.get(edge_key) or {}).get('phase11_retrieval_score'))) * 0.2 for edge_key in shared_edges), 3)
        candidate_bonus = candidate_stat_bonus(candidate_stats.get(f"case_review:{candidate.get('case_key')}"), distribution_profiles, phase11_policy)
        generic_penalty = 1.5 if candidate.get('error_pattern') in {'resolved_case_review_pending', 'settlement_or_path_review_pending'} else 0.0
        retrieval_score = round(mech_score + source_score + mechanic_score + category_score + semantic_score + node_weight_score + edge_weight_score + phase11_node_bonus + phase11_edge_bonus + candidate_bonus - generic_penalty, 3)
        reasons: list[str] = []
        if shared_nodes:
            reasons.append('shared nodes: ' + ', '.join(shared_nodes))
        if shared_edges:
            reasons.append('shared edges: ' + ', '.join(shared_edges))
        if shared_mechanics:
            reasons.append('shared mechanics: ' + ', '.join(shared_mechanics))
        if shared_source:
            reasons.append('shared source-of-truth: ' + ', '.join(shared_source))
        if semantic_score > 0.5:
            reasons.append('semantic overlap in title/review summary')
        if node_weight_score > 0:
            reasons.append(f'learned node-weight bonus: {node_weight_score:.2f}')
        if edge_weight_score > 0:
            reasons.append(f'learned edge-weight bonus: {edge_weight_score:.2f}')
        if phase11_node_bonus > 0 or phase11_edge_bonus > 0:
            reasons.append(f'phase11 live-graph bonus: {(phase11_node_bonus + phase11_edge_bonus):.2f}')
        if candidate_bonus > 0:
            reasons.append(f'learned candidate bonus: {candidate_bonus:.2f}')
        results.append({
            'case_key': candidate['case_key'],
            'review_path': candidate['review_path'],
            'packet_path': candidate['packet_path'],
            'retrieval_score': retrieval_score,
            'score_breakdown': {
                'mechanism_overlap': round(mech_score, 3),
                'source_overlap': round(source_score, 3),
                'mechanic_overlap': round(mechanic_score, 3),
                'category_overlap': round(category_score, 3),
                'semantic_similarity': round(semantic_score, 3),
                'node_weight_bonus': round(node_weight_score, 3),
                'edge_weight_bonus': round(edge_weight_score, 3),
                'phase11_node_bonus': round(phase11_node_bonus, 3),
                'phase11_edge_bonus': round(phase11_edge_bonus, 3),
                'candidate_bonus': round(candidate_bonus, 3),
                'generic_penalty': round(generic_penalty, 3),
            },
            'why_retrieved': '; '.join(reasons),
            'error_pattern': candidate.get('error_pattern') or None,
            'reusable_checks': [row.get('check_key') for row in (candidate.get('required_checks') or []) if isinstance(row, dict) and row.get('check_key')],
            '_sort': (-retrieval_score, candidate['case_key']),
        })
    results.sort(key=lambda item: item['_sort'])
    for item in results:
        item.pop('_sort', None)
    return results[:MAX_CASE_REVIEWS]


def selector_matches(query_profile: dict[str, Any], selector: dict[str, Any]) -> tuple[bool, list[str], float]:
    reasons: list[str] = []
    score = 0.0
    same = False
    platform_values = listify(selector.get('platforms'))
    if platform_values:
        shared = overlap_list([query_profile.get('platform') or ''], platform_values)
        if shared:
            same = True
            reasons.append('platform=' + ', '.join(shared))
            score += 1.5
    category_values = listify(selector.get('categories'))
    if category_values:
        shared = overlap_list([query_profile.get('category') or ''], category_values)
        if shared:
            same = True
            reasons.append('category=' + ', '.join(shared))
            score += 1.5
    mechanic_values = listify(selector.get('question_mechanics'))
    if mechanic_values:
        shared = overlap_list(query_profile.get('question_mechanics') or [], mechanic_values)
        if shared:
            same = True
            reasons.append('mechanics=' + ', '.join(shared))
            score += 2.5
    source_values = listify(selector.get('source_of_truth_classes')) or listify(selector.get('source_of_truth_class'))
    if source_values:
        shared = overlap_list([query_profile.get('source_of_truth_class') or ''], source_values)
        if shared:
            same = True
            reasons.append('source_of_truth_class=' + ', '.join(shared))
            score += 2.5
    resolution_values = listify(selector.get('resolution_risk'))
    if resolution_values:
        shared = overlap_list([query_profile.get('resolution_risk') or ''], resolution_values)
        if shared:
            same = True
            reasons.append('resolution_risk=' + ', '.join(shared))
            score += 1.0
    return same, reasons, score


def query_phase11_context(query_profile: dict[str, Any]) -> dict[str, Any]:
    node_metadata = metadata_score_lookup(query_profile.get('active_node_metadata') or [], 'node_key')
    edge_metadata = metadata_score_lookup(query_profile.get('candidate_edge_metadata') or [], 'edge_key')
    return {
        'node_metadata': node_metadata,
        'edge_metadata': edge_metadata,
        'active_node_keys': [str(item).strip() for item in (query_profile.get('active_nodes') or []) if str(item).strip()],
        'matched_edge_keys': [str(item).strip() for item in (query_profile.get('candidate_edges') or []) if str(item).strip()],
        'contested_edge_keys': [str(item).strip() for item in (query_profile.get('contested_edges') or []) if str(item).strip()],
        'required_check_keys': [
            str((row or {}).get('check_key') or '').strip()
            for row in (query_profile.get('required_checks') or [])
            if isinstance(row, dict) and str((row or {}).get('check_key') or '').strip()
        ],
    }


def live_score_total(metadata_by_key: dict[str, dict[str, Any]], keys: list[str] | set[str]) -> float:
    return round(sum(max(0.0, safe_float((metadata_by_key.get(key) or {}).get('phase11_retrieval_score'))) for key in keys), 3)


def source_family_live_score(context: dict[str, Any]) -> float:
    source_nodes = {'settlement-source-specificity', 'resolution-surface-ambiguity', 'verification-caution'}
    source_edges = {
        'settlement-source-specificity__increases__resolution-surface-ambiguity',
        'resolution-surface-ambiguity__increases__verification-caution',
    }
    return round(
        live_score_total(context['node_metadata'], source_nodes.intersection(set(context['active_node_keys'])))
        + live_score_total(context['edge_metadata'], source_edges.intersection(set(context['matched_edge_keys']))),
        3,
    )


def workflow_family_live_score(context: dict[str, Any]) -> float:
    workflow_nodes = {'price-near-threshold', 'touch-probability', 'verification-caution'}
    workflow_edges = {'verification-caution__increases__fair-value-discounting-pressure'}
    return round(
        live_score_total(context['node_metadata'], workflow_nodes.intersection(set(context['active_node_keys'])))
        + live_score_total(context['edge_metadata'], workflow_edges.intersection(set(context['matched_edge_keys']))),
        3,
    )


def intervention_phase11_breakdown(query_profile: dict[str, Any], selector: dict[str, Any], required_checks: list[str], phase11_policy: dict[str, Any] | None = None) -> dict[str, float]:
    context = query_phase11_context(query_profile)
    phase11_policy = phase11_policy or {}
    live_profile = query_live_score_profile(query_profile)
    selector_mechanics = listify(selector.get('question_mechanics'))
    selector_sources = listify(selector.get('source_of_truth_classes'))
    matched_mechanics = overlap_list(query_profile.get('question_mechanics') or [], selector_mechanics)
    matched_sources = overlap_list([query_profile.get('source_of_truth_class') or ''], selector_sources)
    matched_required_checks = overlap_list(context['required_check_keys'], required_checks)
    required_check_profile = {'count': 4.0, 'p25': 0.0, 'p50': 1.0, 'p90': 3.0, 'max': 3.0}
    breakdown = {
        'required_check_bonus': round(phase11_weight(phase11_policy, 'intervention', 'required_check_bonus', default=0.45) * normalized_reward(float(len(matched_required_checks)), required_check_profile), 3),
        'phase11_mechanic_live_bonus': round(phase11_weight(phase11_policy, 'intervention', 'mechanic_live_bonus', default=0.55) * normalized_reward(live_score_total(context['edge_metadata'], context['matched_edge_keys']), live_profile), 3) if matched_mechanics else 0.0,
        'phase11_source_live_bonus': round(phase11_weight(phase11_policy, 'intervention', 'source_live_bonus', default=0.75) * normalized_reward(source_family_live_score(context), live_profile), 3) if matched_sources else 0.0,
        'phase11_workflow_live_bonus': round(phase11_weight(phase11_policy, 'intervention', 'workflow_live_bonus', default=0.60) * normalized_reward(workflow_family_live_score(context), live_profile), 3) if matched_mechanics else 0.0,
    }
    breakdown['matched_required_checks'] = matched_required_checks  # type: ignore[index]
    breakdown['matched_mechanics'] = matched_mechanics  # type: ignore[index]
    breakdown['matched_sources'] = matched_sources  # type: ignore[index]
    return breakdown


def aggregate_note_candidates_phase11(
    query_profile: dict[str, Any],
    candidate_stats: dict[str, dict[str, Any]],
    distribution_profiles: dict[str, dict[str, dict[str, float]]] | None = None,
    phase11_policy: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    context = query_phase11_context(query_profile)
    phase11_policy = phase11_policy or {}
    live_profile = query_live_score_profile(query_profile)
    active_nodes = set(context['active_node_keys'])
    contested_edges = set(context['contested_edge_keys'])
    candidates: list[dict[str, Any]] = []

    workflow_shared_contested = 'verification-caution__increases__fair-value-discounting-pressure' in contested_edges
    workflow_threshold = bool({'price-near-threshold', 'touch-probability'}.intersection(active_nodes))
    if workflow_shared_contested or workflow_threshold:
        breakdown = {
            'shared_contested_workflow_edge': round(phase11_weight(phase11_policy, 'aggregate_note', 'shared_contested_workflow_edge', default=0.85) * normalized_reward(1.0 if workflow_shared_contested else 0.0, build_metric_profile([1.0])), 3),
            'threshold_workflow_family': round(phase11_weight(phase11_policy, 'aggregate_note', 'threshold_workflow_family', default=0.55) * normalized_reward(1.0 if workflow_threshold else 0.0, build_metric_profile([1.0])), 3),
            'phase11_workflow_live_bonus': round(phase11_weight(phase11_policy, 'aggregate_note', 'workflow_live_bonus', default=0.80) * normalized_reward(workflow_family_live_score(context), live_profile), 3),
            'candidate_bonus': candidate_stat_bonus(candidate_stats.get('aggregate_note:qualitative-db/50-learnings/workflow-performance/generated-index.md'), distribution_profiles, phase11_policy),
        }
        score = round(sum(float(v) for v in breakdown.values()), 3)
        reason_parts = []
        if workflow_shared_contested:
            reason_parts.append('shared contested workflow edge: verification-caution vs fair-value discounting')
        if workflow_threshold:
            reason_parts.append('shared threshold-touch workflow family')
        if breakdown['phase11_workflow_live_bonus'] > 0:
            reason_parts.append(f'phase11 workflow live bonus: {breakdown["phase11_workflow_live_bonus"]:.2f}')
        if breakdown['candidate_bonus'] > 0:
            reason_parts.append(f'learned candidate bonus: {breakdown["candidate_bonus"]:.2f}')
        candidates.append({
            'path': 'qualitative-db/50-learnings/workflow-performance/generated-index.md',
            'retrieval_score': score,
            'score_breakdown': breakdown,
            'why_retrieved': '; '.join(reason_parts),
            '_sort': (-score, 'workflow-performance'),
        })

    source_family = bool({'settlement-source-specificity', 'resolution-surface-ambiguity'}.intersection(active_nodes))
    if source_family:
        breakdown = {
            'shared_source_family': round(phase11_weight(phase11_policy, 'aggregate_note', 'shared_source_family', default=0.90) * normalized_reward(1.0, build_metric_profile([1.0])), 3),
            'phase11_source_live_bonus': round(phase11_weight(phase11_policy, 'aggregate_note', 'source_live_bonus', default=0.85) * normalized_reward(source_family_live_score(context), live_profile), 3),
            'candidate_bonus': candidate_stat_bonus(candidate_stats.get('aggregate_note:qualitative-db/50-learnings/source-performance/generated-index.md'), distribution_profiles, phase11_policy),
        }
        score = round(sum(float(v) for v in breakdown.values()), 3)
        reason_parts = ['shared source-of-truth / settlement ambiguity family']
        if breakdown['phase11_source_live_bonus'] > 0:
            reason_parts.append(f'phase11 source-family live bonus: {breakdown["phase11_source_live_bonus"]:.2f}')
        if breakdown['candidate_bonus'] > 0:
            reason_parts.append(f'learned candidate bonus: {breakdown["candidate_bonus"]:.2f}')
        candidates.append({
            'path': 'qualitative-db/50-learnings/source-performance/generated-index.md',
            'retrieval_score': score,
            'score_breakdown': breakdown,
            'why_retrieved': '; '.join(reason_parts),
            '_sort': (-score, 'source-performance'),
        })

    candidates.sort(key=lambda item: item['_sort'])
    return candidates


def shortlist_active_interventions(
    query_profile: dict[str, Any],
    candidate_stats: dict[str, dict[str, Any]],
    distribution_profiles: dict[str, dict[str, dict[str, float]]] | None = None,
    phase11_policy: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for path in intervention_note_paths():
        record = build_intervention_record(path)
        if record.get('status') != 'active':
            continue
        selector = record.get('target_selector') or {}
        matched, reasons, score = selector_matches(query_profile, selector)
        if not matched:
            continue
        payload = record.get('change_payload') or {}
        required_checks = [str(item).strip() for item in (payload.get('required_checks') or []) if str(item).strip()]
        for label in payload.get('required_labels') or []:
            label_key = f'label_{str(label).strip()}'
            if label_key not in required_checks:
                required_checks.append(label_key)
        phase11 = intervention_phase11_breakdown(query_profile, selector, required_checks, phase11_policy)
        candidate_bonus = candidate_stat_bonus(candidate_stats.get(f"intervention:{record['intervention_key']}"), distribution_profiles, phase11_policy)
        score_breakdown = {
            'selector_match_score': round(score, 3),
            'candidate_bonus': candidate_bonus,
            'required_check_bonus': round(float(phase11.get('required_check_bonus') or 0.0), 3),
            'phase11_mechanic_live_bonus': round(float(phase11.get('phase11_mechanic_live_bonus') or 0.0), 3),
            'phase11_source_live_bonus': round(float(phase11.get('phase11_source_live_bonus') or 0.0), 3),
            'phase11_workflow_live_bonus': round(float(phase11.get('phase11_workflow_live_bonus') or 0.0), 3),
        }
        total_score = round(sum(float(v) for v in score_breakdown.values()), 3)
        why = 'active selector match: ' + '; '.join(reasons)
        if phase11.get('matched_required_checks'):
            why += '; matched required checks: ' + ', '.join(phase11['matched_required_checks'])
        if candidate_bonus > 0:
            why += f'; learned candidate bonus: {candidate_bonus:.2f}'
        live_bonus_total = score_breakdown['phase11_mechanic_live_bonus'] + score_breakdown['phase11_source_live_bonus'] + score_breakdown['phase11_workflow_live_bonus']
        if live_bonus_total > 0:
            why += f'; phase11 live-context bonus: {live_bonus_total:.2f}'
        results.append({
            'intervention_key': record['intervention_key'],
            'path': record['path'],
            'application_surface': record.get('application_surface') or 'researcher_prompt',
            'change_kind': record.get('change_kind') or 'verification_rule',
            'retrieval_score': total_score,
            'score_breakdown': score_breakdown,
            'why_retrieved': why,
            'required_checks': required_checks,
            '_sort': (-total_score, record['intervention_key']),
        })
    results.sort(key=lambda item: item['_sort'])
    for item in results:
        item.pop('_sort', None)
    return results[:MAX_INTERVENTIONS]


def select_aggregate_notes(
    query_profile: dict[str, Any],
    candidate_stats: dict[str, dict[str, Any]],
    distribution_profiles: dict[str, dict[str, dict[str, float]]] | None = None,
    phase11_policy: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    candidates = aggregate_note_candidates_phase11(query_profile, candidate_stats, distribution_profiles, phase11_policy)
    for item in candidates:
        item.pop('_sort', None)
    return candidates[:MAX_AGGREGATE_NOTES]


def compile_required_checks(query_profile: dict[str, Any], active_interventions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = [dict(item) for item in (query_profile.get('required_checks') or [])]
    for intervention in active_interventions:
        for check_key in intervention.get('required_checks') or []:
            row = {
                'check_key': check_key,
                'reason': 'active intervention + mechanism overlap',
                'source': f"intervention:{intervention['intervention_key']}",
            }
            if row not in rows:
                rows.append(row)
    dedup: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row in rows:
        key = str(row.get('check_key') or '').strip()
        if not key or key in seen:
            continue
        seen.add(key)
        dedup.append(row)
    return dedup[:MAX_REQUIRED_CHECKS]


def load_graph() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    nodes = {record['node_key']: record for record in (build_node_record(path) for path in node_note_paths())}
    edges = {record['edge_key']: record for record in (build_edge_record(path) for path in edge_note_paths())}
    return nodes, edges


def load_learned_stats(*, db_url: str, psql_bin: str) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, bool]]:
    resolved_db_url = resolve_db_url(db_url)
    if not resolved_db_url:
        return {}, {}, {}, {'candidate_stats': False, 'edge_stats': False, 'node_stats': False}
    candidate_present = table_exists('lmd_candidate_stats', db_url=resolved_db_url, psql_bin=psql_bin)
    edge_present = table_exists('causal_edge_stats', db_url=resolved_db_url, psql_bin=psql_bin)
    node_present = table_exists('causal_node_stats', db_url=resolved_db_url, psql_bin=psql_bin)
    candidate_rows = exec_sql(psql_bin, resolved_db_url, CANDIDATE_STATS_SQL, {}) if candidate_present else []
    edge_rows = exec_sql(psql_bin, resolved_db_url, EDGE_STATS_SQL, {}) if edge_present else []
    node_rows = exec_sql(psql_bin, resolved_db_url, NODE_STATS_SQL, {}) if node_present else []
    if not isinstance(candidate_rows, list):
        candidate_rows = []
    if not isinstance(edge_rows, list):
        edge_rows = []
    if not isinstance(node_rows, list):
        node_rows = []
    return (
        {str(row.get('candidate_id') or ''): row for row in candidate_rows if str(row.get('candidate_id') or '').strip()},
        {str(row.get('edge_key') or ''): row for row in edge_rows if str(row.get('edge_key') or '').strip()},
        {str(row.get('node_key') or ''): row for row in node_rows if str(row.get('node_key') or '').strip()},
        {'candidate_stats': candidate_present, 'edge_stats': edge_present, 'node_stats': node_present},
    )


def resolve_phase11_policy(args: argparse.Namespace, override: dict[str, Any] | None = None) -> dict[str, Any]:
    if override is not None:
        return override
    if bool(getattr(args, 'phase11_disable_learned_policy', False)):
        policy = json.loads(json.dumps(DEFAULT_POLICY))
        policy['loaded_from_file'] = False
        policy['source_path'] = 'DEFAULT_POLICY'
        return policy
    raw_path = str(getattr(args, 'phase11_policy_path', '') or '').strip()
    if raw_path:
        policy_path = Path(raw_path)
        if not policy_path.is_absolute():
            policy_path = (WORKSPACE_ROOT / raw_path).resolve()
        return load_phase11_retrieval_policy(policy_path)
    return load_phase11_retrieval_policy()



def build_bundle(args: argparse.Namespace, *, phase11_policy: dict[str, Any] | None = None) -> dict[str, Any]:
    nodes, edges = load_graph()
    candidate_stats, edge_stats, node_stats, stats_presence = load_learned_stats(db_url=args.db_url, psql_bin=args.psql)
    stats_distribution_profiles = build_stats_distribution_profiles(candidate_stats, edge_stats, node_stats)
    phase11_policy = resolve_phase11_policy(args, override=phase11_policy)
    family_policies = load_family_policies()
    family_state = build_live_family_state(nodes, edges)
    family_policy_caps = family_policy_caps_for_bundle(family_policies)
    live_graph_trial_mode = resolve_live_graph_trial_mode(args)
    query_profile, debug_info = infer_live_query_context(
        args,
        nodes,
        edges,
        trial_mode=live_graph_trial_mode,
        node_stats=node_stats,
        edge_stats=edge_stats,
        family_state=family_state,
        family_policies=family_policies,
        distribution_profiles=stats_distribution_profiles,
        phase11_policy=phase11_policy,
    )
    active_interventions = shortlist_active_interventions(query_profile, candidate_stats, stats_distribution_profiles, phase11_policy)
    case_review_candidates = load_case_review_candidates(args.case_key)
    case_reviews = shortlist_case_reviews(query_profile, case_review_candidates, candidate_stats, edge_stats, node_stats, stats_distribution_profiles, phase11_policy)
    aggregate_notes = select_aggregate_notes(query_profile, candidate_stats, stats_distribution_profiles, phase11_policy)
    required_checks = compile_required_checks(query_profile, active_interventions)

    assignment_arm = str(args.experiment_arm or '').strip().lower()
    has_payload = bool(case_reviews or active_interventions or aggregate_notes or required_checks)
    support_gate = {
        'min_case_reviews': 1,
        'min_structural_support': 1,
        'min_required_checks': 2,
    }
    structural_support_count = len(query_profile.get('candidate_edges') or []) + len(active_interventions)
    meets_support_gate = (
        len(case_reviews) >= support_gate['min_case_reviews']
        and structural_support_count >= support_gate['min_structural_support']
        and len(required_checks) >= support_gate['min_required_checks']
    )
    lmd_used = assignment_arm == 'treatment' and has_payload and meets_support_gate
    if assignment_arm == 'control':
        status = 'control_preview'
    elif assignment_arm == 'treatment' and has_payload and meets_support_gate:
        status = 'treatment_ready'
    elif assignment_arm == 'treatment' and has_payload and not meets_support_gate:
        status = 'support_gated_off'
    elif assignment_arm == 'treatment':
        status = 'no_matches'
    else:
        status = 'preview'
    lmd_tier = 'tier1' if has_payload else 'tier0'

    result_paths = unique(
        [item['review_path'] for item in case_reviews]
        + [item['path'] for item in active_interventions]
        + [item['path'] for item in aggregate_notes]
    )

    bundle = {
        'status': status,
        'lmd_used': lmd_used,
        'usage_mode': 'prompt_injected' if lmd_used else 'prepared_not_injected',
        'assignment_arm': assignment_arm or None,
        'lmd_tier': lmd_tier,
        'query_profile': {
            'run_kind': query_profile.get('run_kind'),
            'rerun_scope': query_profile.get('rerun_scope'),
            'difficulty_class': query_profile.get('difficulty_class'),
            'resolution_risk': query_profile.get('resolution_risk'),
            'source_of_truth_class': query_profile.get('source_of_truth_class'),
            'platform': query_profile.get('platform'),
            'category': query_profile.get('category'),
            'focus_hints': query_profile.get('focus_hints') or [],
            'question_mechanics': query_profile.get('question_mechanics') or [],
            'suppress_same_case': True,
        },
        'retrieval_policy': {
            'reviewed_only': True,
            'active_interventions_only': True,
            'canon_first': False,
            'max_case_reviews': MAX_CASE_REVIEWS,
            'max_interventions': MAX_INTERVENTIONS,
            'max_aggregate_notes': MAX_AGGREGATE_NOTES,
            'max_required_checks': MAX_REQUIRED_CHECKS,
            'structured_shortlist_then_semantic_rerank': True,
            'phase11_learned_ranking_enabled': True,
            'phase11_retrieval_policy_version': PHASE11_RETRIEVAL_POLICY_VERSION,
            'phase11_learned_policy_version': phase11_policy.get('policy_version'),
            'phase11_learned_policy_loaded': bool(phase11_policy.get('loaded_from_file')),
            'phase11_learned_policy_source': phase11_policy.get('source_path'),
            'live_graph_default_recall_stages': list(DEFAULT_RECALLABLE_LIVE_STAGES),
            'live_graph_trial_recall_stages': list(TRIAL_RECALLABLE_LIVE_STAGES),
            'live_graph_review_only_stages': list(REVIEW_ONLY_LIVE_STAGES),
            'live_graph_disabled_stages': list(DISABLED_LIVE_STAGES),
            'live_graph_trial_mode': query_profile.get('live_graph_trial_mode'),
            'live_graph_trial_recall_enabled': bool(query_profile.get('live_graph_trial_enabled')),
            'live_graph_recallable_stages': query_profile.get('live_graph_recallable_stages') or [],
            'live_graph_family_state': family_state,
            'live_graph_family_policy_caps': family_policy_caps,
        },
        'causal_context': {
            'active_nodes': query_profile.get('active_nodes') or [],
            'active_node_metadata': query_profile.get('active_node_metadata') or [],
            'matched_edges': query_profile.get('candidate_edges') or [],
            'matched_edge_metadata': query_profile.get('candidate_edge_metadata') or [],
            'contested_edges': query_profile.get('contested_edges') or [],
            'required_checks': [row['check_key'] for row in required_checks],
            'live_graph_trial_mode': query_profile.get('live_graph_trial_mode'),
            'live_graph_trial_enabled': bool(query_profile.get('live_graph_trial_enabled')),
            'live_graph_recallable_stages': query_profile.get('live_graph_recallable_stages') or [],
        },
        'case_mix': case_mix_from_query_profile(query_profile),
        'results': {
            'case_reviews': case_reviews,
            'active_interventions': active_interventions,
            'aggregate_notes': aggregate_notes,
            'required_checks': required_checks,
            'negative_checks': negative_checks_from_required_checks(required_checks),
        },
        'result_paths': result_paths,
        'generator_version': args.generator_version,
        'policy_version': args.policy_version,
        'debug': {
            'active_case_review_candidates': len(case_review_candidates),
            'node_reason_count': sum(len(v) for v in (debug_info.get('node_reasons') or {}).values()),
            'node_reasons': debug_info.get('node_reasons') or {},
            'suppressed_node_reasons': debug_info.get('suppressed_node_reasons') or {},
            'suppressed_edge_reasons': debug_info.get('suppressed_edge_reasons') or {},
            'live_graph_trial_mode': debug_info.get('live_graph_trial_mode'),
            'live_graph_stage_counts': debug_info.get('live_graph_stage_counts') or {},
            'live_graph_family_state': family_state,
            'phase11': {
                'live_nodes_ranked': [
                    {
                        'node_key': row.get('node_key'),
                        'score': row.get('phase11_retrieval_score'),
                        'trust_tier': row.get('phase11_trust_tier'),
                        'family_crowding': row.get('phase11_family_crowding'),
                        'score_breakdown': row.get('phase11_score_breakdown'),
                    }
                    for row in (query_profile.get('active_node_metadata') or [])
                ],
                'live_edges_ranked': [
                    {
                        'edge_key': row.get('edge_key'),
                        'score': row.get('phase11_retrieval_score'),
                        'trust_tier': row.get('phase11_trust_tier'),
                        'family_crowding': row.get('phase11_family_crowding'),
                        'score_breakdown': row.get('phase11_score_breakdown'),
                    }
                    for row in (query_profile.get('candidate_edge_metadata') or [])
                ],
                'case_review_scores': [
                    {
                        'case_key': row.get('case_key'),
                        'retrieval_score': row.get('retrieval_score'),
                        'score_breakdown': row.get('score_breakdown'),
                    }
                    for row in case_reviews
                ],
                'intervention_scores': [
                    {
                        'intervention_key': row.get('intervention_key'),
                        'retrieval_score': row.get('retrieval_score'),
                        'score_breakdown': row.get('score_breakdown'),
                    }
                    for row in active_interventions
                ],
                'aggregate_note_scores': [
                    {
                        'path': row.get('path'),
                        'retrieval_score': row.get('retrieval_score'),
                        'score_breakdown': row.get('score_breakdown'),
                    }
                    for row in aggregate_notes
                ],
                'stats_distribution_profiles': stats_distribution_profiles,
                'learned_policy': phase11_policy,
            },
            'stats_presence': stats_presence,
            'support_gate': {
                **support_gate,
                'structural_support_count': structural_support_count,
                'meets_support_gate': meets_support_gate,
            },
        },
    }
    bundle['shadow_evaluation'] = evaluate_shadow_candidates(bundle, limit=max(0, int(args.shadow_limit or 0)))
    trial_overlay = evaluate_trial_candidates(bundle, limit=max(0, int(args.trial_limit or 0)), phase11_policy=phase11_policy)
    bundle['trial_overlay'] = finalize_trial_overlay(bundle, trial_overlay)
    bundle['coverage'] = coverage_metrics_from_bundle(bundle)
    bundle['provenance'] = {
        'generator_version': args.generator_version,
        'policy_version': args.policy_version,
        'phase11_policy_version': phase11_policy.get('policy_version'),
        'phase11_policy_loaded_from_file': bool(phase11_policy.get('loaded_from_file')),
        'phase11_policy_source': phase11_policy.get('source_path'),
        'bundle_input_hash': sha256_jsonable({
            'case_key': args.case_key,
            'market_id': args.market_id,
            'title': args.title,
            'description': args.description,
            'category': args.category,
            'platform': args.platform,
            'current_price': args.current_price,
            'closes_at': args.closes_at,
            'resolves_at': args.resolves_at,
            'run_kind': args.run_kind,
            'rerun_scope': args.rerun_scope,
            'prior_dispatch_count': args.prior_dispatch_count,
            'prior_case_count': args.prior_case_count,
            'difficulty_class': args.difficulty_class,
            'resolution_risk': args.resolution_risk,
            'source_of_truth_class': args.source_of_truth_class,
            'focus_hints_json': args.focus_hints_json,
            'extra_verification_required': args.extra_verification_required,
            'experiment_arm': args.experiment_arm,
            'live_graph_trial_mode': args.live_graph_trial_mode,
        }),
        'family_policy_hash': sha256_jsonable(family_policies),
        'phase11_policy_hash': sha256_jsonable(phase11_policy),
        'live_graph_snapshot_hash': sha256_jsonable({
            'active_nodes': query_profile.get('active_nodes') or [],
            'active_node_metadata': query_profile.get('active_node_metadata') or [],
            'candidate_edges': query_profile.get('candidate_edge_metadata') or [],
            'contested_edges': query_profile.get('contested_edges') or [],
            'required_checks': required_checks,
        }),
        'result_paths_hash': sha256_jsonable(result_paths),
    }
    return bundle


def finalize_trial_overlay(bundle: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    assignment_arm = str(bundle.get('assignment_arm') or '').strip().lower()
    selected = [dict(row) for row in (overlay.get('selected_candidates') or []) if isinstance(row, dict)]
    inject = bool(selected) and assignment_arm == 'treatment'
    overlay_mode = 'treatment_injected' if inject else 'preview_only'
    finalized_selected = []
    for row in selected:
        finalized_selected.append({
            **row,
            'preview_only': not inject,
            'injected': inject,
            'overlay_mode': overlay_mode,
        })
    return {
        **overlay,
        'preview_only': not inject,
        'used': inject,
        'injected': inject,
        'overlay_mode': overlay_mode,
        'injection_policy': {
            'allowed_assignment_arms': ['treatment'],
            'treatment_only': True,
            'experimental_not_canon': True,
            'prompt_injection_enabled': inject,
        },
        'selected_count': len(finalized_selected),
        'selected_candidates': finalized_selected,
    }



def write_bundle(path_str: str, bundle: dict[str, Any], *, dry_run: bool) -> dict[str, Any]:
    if not path_str:
        return {'status': 'skipped'}
    if dry_run:
        return {'status': 'dry_run', 'path': path_str}
    path = Path(path_str)
    if not path.is_absolute():
        path = (WORKSPACE_ROOT / path_str).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    write_json(path, bundle, pretty=True)
    try:
        rendered_path = str(path.relative_to(WORKSPACE_ROOT))
    except ValueError:
        rendered_path = str(path)
    return {'status': 'written', 'path': rendered_path}


def main() -> int:
    args = parse_args()
    bundle = build_bundle(args)
    bundle_write = write_bundle(args.out or '', bundle, dry_run=args.dry_run)
    result = {
        'ok': True,
        'bundle_path': bundle_write.get('path') if bundle_write.get('status') in {'written', 'dry_run'} else None,
        'bundle_write': bundle_write,
        'bundle': bundle,
    }
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
