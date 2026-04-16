#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DECISION_MAKER_DIR = SCRIPT_DIR.parents[1]
if str(DECISION_MAKER_DIR) not in sys.path:
    sys.path.insert(0, str(DECISION_MAKER_DIR))

from common import WORKSPACE_ROOT, coerce_string, load_json, relative_to_workspace, utc_now_iso, write_json  # noqa: E402

GENERATE_LMD_BUNDLE = WORKSPACE_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'planner' / 'scripts' / 'generate_lmd_bundle.py'
DEFAULT_PSQL = '/opt/homebrew/opt/postgresql@16/bin/psql'
MAX_CASE_REVIEWS = 1
MAX_INTERVENTIONS = 1
MAX_AGGREGATE_NOTES = 0
MAX_REQUIRED_CHECKS = 3
SOURCE_TOKENS = {'binance', 'coinbase', 'cme', 'official', 'settlement', 'source', 'sources', 'verification', 'verify', 'proof'}


class LightRefreshLmdError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Build a compact, read-only LMD overlay bundle for a light refresh decision run')
    parser.add_argument('--light-refresh-brief-json', required=True)
    parser.add_argument('--case-key', default='')
    parser.add_argument('--difficulty-class', default='')
    parser.add_argument('--resolution-risk', default='')
    parser.add_argument('--source-of-truth-class', default='')
    parser.add_argument('--focus-hints-json', default='')
    parser.add_argument('--extra-verification-required', default='')
    parser.add_argument('--out', default='')
    parser.add_argument('--generator-out', default='')
    parser.add_argument('--db-url', default=os.getenv('PREDQUANT_ORCHESTRATOR_URL', ''))
    parser.add_argument('--psql', default=os.getenv('PSQL_BIN', DEFAULT_PSQL))
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def parse_json_arg(text: str, default: Any) -> Any:
    raw = str(text or '').strip()
    if not raw:
        return default
    try:
        return json.loads(raw)
    except Exception:
        return default


def resolve_input_path(path_like: str) -> Path:
    path = Path(path_like)
    return path if path.is_absolute() else WORKSPACE_ROOT / path


def infer_case_key(args: argparse.Namespace, brief: dict[str, Any], brief_path: Path) -> str:
    case_key = coerce_string(args.case_key) or coerce_string(brief.get('case_key'))
    if case_key:
        return case_key
    candidate = brief_path.parts
    for item in candidate:
        if str(item).startswith('case-'):
            return str(item)
    raise LightRefreshLmdError('could not determine case_key from args or light-refresh brief')


def sibling_path(base: Path, name: str) -> Path:
    return base.with_name(name)


def default_wrapper_out(brief_path: Path) -> Path:
    return sibling_path(brief_path, 'light-refresh-lmd-bundle.json')


def default_generator_out(wrapper_out: Path) -> Path:
    stem = wrapper_out.stem
    suffix = wrapper_out.suffix or '.json'
    return wrapper_out.with_name(f'{stem}-source{suffix}')


def render_path(path: Path) -> str:
    return relative_to_workspace(path) if path.is_absolute() else str(path)


def parse_json_stdout(proc: subprocess.CompletedProcess[str]) -> dict[str, Any]:
    stdout = proc.stdout.strip()
    if not stdout:
        raise LightRefreshLmdError('generate_lmd_bundle.py returned empty stdout')
    lines = [line for line in stdout.splitlines() if line.strip()]
    for line in reversed(lines):
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return parsed
    try:
        parsed = json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise LightRefreshLmdError('generate_lmd_bundle.py returned non-JSON output') from exc
    if not isinstance(parsed, dict):
        raise LightRefreshLmdError('generate_lmd_bundle.py returned JSON but not an object')
    return parsed


def joined_brief_text(brief: dict[str, Any]) -> str:
    market = brief.get('market') if isinstance(brief.get('market'), dict) else {}
    questions = brief.get('focused_questions') if isinstance(brief.get('focused_questions'), list) else []
    parts = [
        coerce_string(market.get('title')),
        coerce_string(market.get('description')),
        ' '.join(str(item) for item in questions if str(item).strip()),
    ]
    return ' '.join(part for part in parts if part).lower()


def infer_focus_hints(brief: dict[str, Any], explicit_text: str) -> list[str]:
    explicit = parse_json_arg(explicit_text, [])
    if isinstance(explicit, list):
        parsed = [str(item).strip() for item in explicit if str(item).strip()]
        if parsed:
            return parsed
    text = joined_brief_text(brief)
    hints: list[str] = []
    if any(token in text for token in SOURCE_TOKENS):
        hints.extend(['source_of_truth_check', 'extra_verification'])
    dedup: list[str] = []
    seen: set[str] = set()
    for item in hints:
        if item in seen:
            continue
        seen.add(item)
        dedup.append(item)
    return dedup


def infer_source_of_truth_class(brief: dict[str, Any], explicit_value: str) -> str:
    explicit = coerce_string(explicit_value)
    if explicit:
        return explicit
    text = joined_brief_text(brief)
    if any(token in text for token in SOURCE_TOKENS):
        return 'authoritative_with_fallback'
    return ''


def infer_extra_verification_required(brief: dict[str, Any], explicit_value: str) -> bool:
    raw = coerce_string(explicit_value).lower()
    if raw in {'1', 'true', 'yes', 'on'}:
        return True
    if raw in {'0', 'false', 'no', 'off'}:
        return False
    text = joined_brief_text(brief)
    return any(token in text for token in SOURCE_TOKENS)


def compact_case_review_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    compact: list[dict[str, Any]] = []
    for row in rows[:MAX_CASE_REVIEWS]:
        compact.append({
            'case_key': coerce_string(row.get('case_key')),
            'review_path': coerce_string(row.get('review_path')),
            'packet_path': coerce_string(row.get('packet_path')),
            'retrieval_score': row.get('retrieval_score'),
            'why_retrieved': coerce_string(row.get('why_retrieved')),
            'error_pattern': coerce_string(row.get('error_pattern')) or None,
            'reusable_checks': [str(item).strip() for item in (row.get('reusable_checks') or []) if str(item).strip()][:MAX_REQUIRED_CHECKS],
        })
    return compact


def compact_intervention_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    compact: list[dict[str, Any]] = []
    for row in rows[:MAX_INTERVENTIONS]:
        compact.append({
            'intervention_key': coerce_string(row.get('intervention_key')),
            'path': coerce_string(row.get('path')),
            'application_surface': coerce_string(row.get('application_surface')),
            'change_kind': coerce_string(row.get('change_kind')),
            'retrieval_score': row.get('retrieval_score'),
            'why_retrieved': coerce_string(row.get('why_retrieved')),
            'required_checks': [str(item).strip() for item in (row.get('required_checks') or []) if str(item).strip()][:MAX_REQUIRED_CHECKS],
        })
    return compact


def compact_required_checks(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    compact: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row in rows:
        check_key = coerce_string(row.get('check_key'))
        if not check_key or check_key in seen:
            continue
        seen.add(check_key)
        compact.append({
            'check_key': check_key,
            'reason': coerce_string(row.get('reason')),
            'source': coerce_string(row.get('source')),
        })
        if len(compact) >= MAX_REQUIRED_CHECKS:
            break
    return compact


def compact_result_paths(case_reviews: list[dict[str, Any]], interventions: list[dict[str, Any]]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in case_reviews:
        path = coerce_string(item.get('review_path'))
        if path and path not in seen:
            seen.add(path)
            out.append(path)
    for item in interventions:
        path = coerce_string(item.get('path'))
        if path and path not in seen:
            seen.add(path)
            out.append(path)
    return out


def build_wrapper_bundle(*, case_key: str, brief: dict[str, Any], brief_path: Path, generator_path: Path, generator_result: dict[str, Any], source_out_path: Path) -> dict[str, Any]:
    raw_bundle = generator_result.get('bundle') if isinstance(generator_result.get('bundle'), dict) else {}
    raw_results = raw_bundle.get('results') if isinstance(raw_bundle.get('results'), dict) else {}
    raw_debug = raw_bundle.get('debug') if isinstance(raw_bundle.get('debug'), dict) else {}
    support_gate = raw_debug.get('support_gate') if isinstance(raw_debug.get('support_gate'), dict) else {}
    causal_context = raw_bundle.get('causal_context') if isinstance(raw_bundle.get('causal_context'), dict) else {}
    refresh_assessment = brief.get('refresh_assessment') if isinstance(brief.get('refresh_assessment'), dict) else {}
    refresh_mode = coerce_string(refresh_assessment.get('recommended_mode')) or 'light'

    case_reviews = compact_case_review_rows(list(raw_results.get('case_reviews') or []))
    active_interventions = compact_intervention_rows(list(raw_results.get('active_interventions') or []))
    required_checks = compact_required_checks(list(raw_results.get('required_checks') or []))
    matched_edges = [str(item).strip() for item in (causal_context.get('matched_edges') or []) if str(item).strip()]
    contested_edges = [str(item).strip() for item in (causal_context.get('contested_edges') or []) if str(item).strip()]
    active_nodes = [str(item).strip() for item in (causal_context.get('active_nodes') or []) if str(item).strip()]

    raw_support_ok = bool(support_gate.get('meets_support_gate'))
    compact_structural_support_count = len(active_interventions) + len(matched_edges)
    compact_support_gate = {
        'min_case_reviews': 1,
        'min_structural_support': 1,
        'min_required_checks': 1,
        'case_review_count': len(case_reviews),
        'structural_support_count': compact_structural_support_count,
        'required_check_count': len(required_checks),
    }
    compact_support_ok = (
        compact_support_gate['case_review_count'] >= compact_support_gate['min_case_reviews']
        and compact_support_gate['structural_support_count'] >= compact_support_gate['min_structural_support']
        and compact_support_gate['required_check_count'] >= compact_support_gate['min_required_checks']
    )

    warnings: list[str] = ['read_only_refresh_overlay_only', 'no_exposure_or_learning_logging']
    if refresh_mode != 'light':
        status = 'skipped_non_light_mode'
        overlay_used = False
        warnings.append(f'refresh_mode={refresh_mode}')
    elif not case_reviews and not active_interventions and not required_checks:
        status = 'no_matches'
        overlay_used = False
    elif raw_support_ok and compact_support_ok:
        status = 'overlay_ready'
        overlay_used = True
    else:
        status = 'support_gated_off'
        overlay_used = False

    return {
        'artifact_type': 'light_refresh_lmd_bundle',
        'schema_version': 'light-refresh-lmd/v1',
        'built_at': utc_now_iso(),
        'builder': 'roles/decision-maker/runtime/scripts/build_light_refresh_lmd_bundle.py',
        'case_key': case_key,
        'consumer_surface': 'decision_light_refresh',
        'usage_policy': 'read_only_refresh_overlay',
        'status': status,
        'overlay_used': overlay_used,
        'refresh_mode': refresh_mode,
        'source_light_refresh_brief_path': relative_to_workspace(brief_path),
        'source_generator_script': relative_to_workspace(generator_path),
        'source_generator_bundle_path': relative_to_workspace(source_out_path),
        'source_generator_bundle_status': coerce_string(raw_bundle.get('status')),
        'query_profile': raw_bundle.get('query_profile') or {},
        'compact_caps': {
            'max_case_reviews': MAX_CASE_REVIEWS,
            'max_interventions': MAX_INTERVENTIONS,
            'max_aggregate_notes': MAX_AGGREGATE_NOTES,
            'max_required_checks': MAX_REQUIRED_CHECKS,
        },
        'causal_context': {
            'active_nodes': active_nodes,
            'matched_edges': matched_edges,
            'contested_edges': contested_edges,
            'required_checks': [row['check_key'] for row in required_checks],
        },
        'results': {
            'case_reviews': case_reviews,
            'active_interventions': active_interventions,
            'aggregate_notes': [],
            'required_checks': required_checks,
        },
        'result_paths': compact_result_paths(case_reviews, active_interventions),
        'debug': {
            'generator_result_path': coerce_string(generator_result.get('bundle_path')),
            'raw_lmd_used': bool(raw_bundle.get('lmd_used')),
            'raw_support_gate': support_gate,
            'compact_support_gate': {**compact_support_gate, 'meets_compact_support_gate': compact_support_ok},
            'warnings': warnings,
        },
    }


def run_generator(*, case_key: str, brief: dict[str, Any], source_out_path: Path, db_url: str, psql_bin: str, difficulty_class: str, resolution_risk: str, source_of_truth_class: str, focus_hints: list[str], extra_verification_required: bool, dry_run: bool) -> dict[str, Any]:
    if not GENERATE_LMD_BUNDLE.exists():
        raise LightRefreshLmdError(f'missing generator script: {GENERATE_LMD_BUNDLE}')
    market = brief.get('market') if isinstance(brief.get('market'), dict) else {}
    cmd = [
        sys.executable,
        str(GENERATE_LMD_BUNDLE),
        '--case-key', case_key,
        '--market-id', coerce_string(market.get('market_id')) or case_key,
        '--title', coerce_string(market.get('title')) or case_key,
        '--description', coerce_string(market.get('description')),
        '--category', coerce_string(market.get('category')),
        '--platform', coerce_string(market.get('platform')),
        '--current-price', str(market.get('current_price') if market.get('current_price') is not None else ''),
        '--closes-at', coerce_string(market.get('closes_at')),
        '--resolves-at', coerce_string(market.get('resolves_at')),
        '--run-kind', 'rerun',
        '--rerun-scope', 'same_case',
        '--prior-dispatch-count', '1',
        '--prior-case-count', '0',
        '--difficulty-class', difficulty_class,
        '--resolution-risk', resolution_risk,
        '--source-of-truth-class', source_of_truth_class,
        '--focus-hints-json', json.dumps(focus_hints),
        '--extra-verification-required', json.dumps(bool(extra_verification_required)),
        '--db-url', db_url,
        '--psql', psql_bin,
        '--out', str(source_out_path),
        '--pretty',
    ]
    if dry_run:
        cmd.append('--dry-run')
    proc = subprocess.run(cmd, cwd=str(WORKSPACE_ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        raise LightRefreshLmdError(proc.stderr.strip() or proc.stdout.strip() or 'generate_lmd_bundle.py failed')
    return parse_json_stdout(proc)


def main() -> int:
    args = parse_args()
    brief_path = resolve_input_path(args.light_refresh_brief_json)
    if not brief_path.exists():
        raise SystemExit(f'light-refresh brief not found: {brief_path}')
    brief = load_json(brief_path)
    if not isinstance(brief, dict):
        raise SystemExit('light-refresh brief must decode to an object')

    case_key = infer_case_key(args, brief, brief_path)
    wrapper_out_path = resolve_input_path(args.out) if coerce_string(args.out) else default_wrapper_out(brief_path)
    source_out_path = resolve_input_path(args.generator_out) if coerce_string(args.generator_out) else default_generator_out(wrapper_out_path)
    refresh_assessment = brief.get('refresh_assessment') if isinstance(brief.get('refresh_assessment'), dict) else {}
    refresh_mode = coerce_string(refresh_assessment.get('recommended_mode')) or 'light'

    difficulty_class = coerce_string(args.difficulty_class)
    resolution_risk = coerce_string(args.resolution_risk)
    source_of_truth_class = infer_source_of_truth_class(brief, args.source_of_truth_class)
    focus_hints = infer_focus_hints(brief, args.focus_hints_json)
    extra_verification_required = infer_extra_verification_required(brief, args.extra_verification_required)

    output: dict[str, Any] = {
        'ok': True,
        'case_key': case_key,
        'refresh_mode': refresh_mode,
        'wrapper_bundle_path': render_path(wrapper_out_path),
        'generator_bundle_path': render_path(source_out_path),
        'consumer_surface': 'decision_light_refresh',
        'usage_policy': 'read_only_refresh_overlay',
        'persisted': False,
    }

    if refresh_mode != 'light':
        bundle = {
            'artifact_type': 'light_refresh_lmd_bundle',
            'schema_version': 'light-refresh-lmd/v1',
            'built_at': utc_now_iso(),
            'builder': 'roles/decision-maker/runtime/scripts/build_light_refresh_lmd_bundle.py',
            'case_key': case_key,
            'consumer_surface': 'decision_light_refresh',
            'usage_policy': 'read_only_refresh_overlay',
            'status': 'skipped_non_light_mode',
            'overlay_used': False,
            'refresh_mode': refresh_mode,
            'source_light_refresh_brief_path': relative_to_workspace(brief_path),
            'source_generator_script': relative_to_workspace(GENERATE_LMD_BUNDLE),
            'source_generator_bundle_path': relative_to_workspace(source_out_path),
            'source_generator_bundle_status': 'not_run',
            'query_profile': {},
            'compact_caps': {
                'max_case_reviews': MAX_CASE_REVIEWS,
                'max_interventions': MAX_INTERVENTIONS,
                'max_aggregate_notes': MAX_AGGREGATE_NOTES,
                'max_required_checks': MAX_REQUIRED_CHECKS,
            },
            'causal_context': {
                'active_nodes': [],
                'matched_edges': [],
                'contested_edges': [],
                'required_checks': [],
            },
            'results': {
                'case_reviews': [],
                'active_interventions': [],
                'aggregate_notes': [],
                'required_checks': [],
            },
            'result_paths': [],
            'debug': {
                'warnings': ['read_only_refresh_overlay_only', 'non_light_mode_skipped'],
            },
        }
        output['bundle'] = bundle
        if not args.dry_run:
            write_json(wrapper_out_path, bundle, pretty=True)
            output['persisted'] = True
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    try:
        generator_result = run_generator(
            case_key=case_key,
            brief=brief,
            source_out_path=source_out_path,
            db_url=args.db_url,
            psql_bin=args.psql,
            difficulty_class=difficulty_class,
            resolution_risk=resolution_risk,
            source_of_truth_class=source_of_truth_class,
            focus_hints=focus_hints,
            extra_verification_required=extra_verification_required,
            dry_run=args.dry_run,
        )
    except Exception as exc:  # noqa: BLE001
        output['ok'] = False
        output['error'] = str(exc)
        output['status'] = 'generator_error'
        print(json.dumps(output, indent=2 if args.pretty else None))
        return 0

    wrapper_bundle = build_wrapper_bundle(
        case_key=case_key,
        brief=brief,
        brief_path=brief_path,
        generator_path=GENERATE_LMD_BUNDLE,
        generator_result=generator_result,
        source_out_path=source_out_path,
    )
    output['status'] = wrapper_bundle.get('status')
    output['overlay_used'] = bool(wrapper_bundle.get('overlay_used'))
    output['bundle'] = wrapper_bundle
    output['generator_result'] = {
        'bundle_path': generator_result.get('bundle_path'),
        'bundle_write': generator_result.get('bundle_write'),
        'status': ((generator_result.get('bundle') or {}) if isinstance(generator_result.get('bundle'), dict) else {}).get('status'),
    }
    output['derived_generator_context'] = {
        'difficulty_class': difficulty_class,
        'resolution_risk': resolution_risk,
        'source_of_truth_class': source_of_truth_class,
        'focus_hints': focus_hints,
        'extra_verification_required': extra_verification_required,
    }

    if not args.dry_run:
        write_json(wrapper_out_path, wrapper_bundle, pretty=True)
        output['persisted'] = True

    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
