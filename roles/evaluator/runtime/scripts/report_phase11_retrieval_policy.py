#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
RUNTIME_ROOT = SCRIPT_PATH.parents[1]
WORKSPACE_ROOT = SCRIPT_PATH.parents[4]
PLANNER_SCRIPT = WORKSPACE_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'planner' / 'scripts' / 'generate_lmd_bundle.py'
CASES_ROOT = WORKSPACE_ROOT / 'qualitative-db' / '40-research' / 'cases'
DEFAULT_JSON_PATH = WORKSPACE_ROOT / 'qualitative-db' / '60-causal-map' / 'generated' / 'phase11-retrieval-policy-report.json'
DEFAULT_MD_PATH = WORKSPACE_ROOT / 'qualitative-db' / '60-causal-map' / 'generated' / 'phase11-retrieval-policy-report.md'
DEFAULT_MAX_CASES = 5

if str(RUNTIME_ROOT) not in sys.path:
    sys.path.append(str(RUNTIME_ROOT))

from lib.io import extract_bullet_kv, parse_frontmatter, read_json, read_text, split_markdown_sections, write_json  # noqa: E402
from lib.phase11_retrieval_policy import DEFAULT_POLICY, POLICY_PATH, load_phase11_retrieval_policy  # noqa: E402


def load_generate_lmd_bundle_module():
    spec = importlib.util.spec_from_file_location('generate_lmd_bundle_for_phase11_report', PLANNER_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'could not import planner script from {PLANNER_SCRIPT}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Compare default-vs-learned Phase 11 retrieval outcomes on real case inputs')
    parser.add_argument('--case-key', action='append', default=[])
    parser.add_argument('--max-cases', type=int, default=DEFAULT_MAX_CASES)
    parser.add_argument('--policy-path', default=str(POLICY_PATH))
    parser.add_argument('--db-url', default=os.getenv('PREDQUANT_ORCHESTRATOR_URL', ''))
    parser.add_argument('--psql', default=os.getenv('PSQL_BIN', '/opt/homebrew/opt/postgresql@16/bin/psql'))
    parser.add_argument('--json-out', default=str(DEFAULT_JSON_PATH))
    parser.add_argument('--md-out', default=str(DEFAULT_MD_PATH))
    parser.add_argument('--pretty', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    return parser.parse_args()


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def relative_to_workspace(path: Path) -> str:
    try:
        return str(path.relative_to(WORKSPACE_ROOT))
    except ValueError:
        return str(path)


def coerce_string(value: Any) -> str:
    if value is None:
        return ''
    return str(value).strip()


def parse_h1(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith('# '):
            return stripped[2:].strip()
    return ''


def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return float(default)


def recent_case_keys(limit: int) -> list[str]:
    case_dirs = [path for path in CASES_ROOT.iterdir() if path.is_dir() and path.name.startswith('case-') and (path / 'case.md').exists()]
    case_dirs.sort(key=lambda path: path.stat().st_mtime, reverse=True)
    return [path.name for path in case_dirs[: max(0, int(limit))]]


def load_case_context(case_key: str) -> dict[str, Any]:
    case_dir = CASES_ROOT / case_key
    case_md = case_dir / 'case.md'
    if not case_md.exists():
        raise FileNotFoundError(f'missing case.md for {case_key}')
    text = read_text(case_md)
    frontmatter = parse_frontmatter(text)
    bullet_kv = extract_bullet_kv(text)
    sections = split_markdown_sections(text)
    light_refresh = read_json(case_dir / 'decision-maker' / 'artifacts' / 'light-refresh-brief.json', default={})
    market = light_refresh.get('market') if isinstance(light_refresh.get('market'), dict) else {}
    refresh_assessment = light_refresh.get('refresh_assessment') if isinstance(light_refresh.get('refresh_assessment'), dict) else {}

    title = coerce_string(market.get('title')) or parse_h1(text)
    description = coerce_string(market.get('description')) or coerce_string(sections.get('Description'))
    return {
        'case_key': case_key,
        'market_id': coerce_string(market.get('market_id')) or coerce_string(frontmatter.get('market_id')),
        'title': title,
        'description': description,
        'category': coerce_string(market.get('category')),
        'platform': coerce_string(market.get('platform')) or coerce_string(frontmatter.get('platform')),
        'current_price': market.get('current_price') if market.get('current_price') is not None else coerce_string(bullet_kv.get('current_price')),
        'closes_at': coerce_string(market.get('closes_at')) or coerce_string(bullet_kv.get('closes_at')),
        'resolves_at': coerce_string(market.get('resolves_at')) or coerce_string(bullet_kv.get('resolves_at')),
        'run_kind': 'refresh' if refresh_assessment else 'novel',
        'rerun_scope': 'light_refresh' if refresh_assessment else '',
        'difficulty_class': '',
        'resolution_risk': '',
        'source_of_truth_class': '',
        'focus_hints_json': '[]',
        'extra_verification_required': '',
        'experiment_arm': 'control',
        'light_refresh_brief_path': relative_to_workspace(case_dir / 'decision-maker' / 'artifacts' / 'light-refresh-brief.json') if (case_dir / 'decision-maker' / 'artifacts' / 'light-refresh-brief.json').exists() else None,
        'case_md_path': relative_to_workspace(case_md),
    }


def build_lmd_args(case_context: dict[str, Any], cli_args: argparse.Namespace) -> argparse.Namespace:
    return argparse.Namespace(
        case_key=case_context['case_key'],
        market_id=case_context['market_id'],
        title=case_context['title'],
        description=case_context['description'],
        category=case_context['category'],
        platform=case_context['platform'],
        current_price=case_context['current_price'],
        closes_at=case_context['closes_at'],
        resolves_at=case_context['resolves_at'],
        run_kind=case_context['run_kind'],
        rerun_scope=case_context['rerun_scope'],
        prior_dispatch_count=0,
        prior_case_count=0,
        difficulty_class=case_context['difficulty_class'],
        resolution_risk=case_context['resolution_risk'],
        source_of_truth_class=case_context['source_of_truth_class'],
        focus_hints_json=case_context['focus_hints_json'],
        extra_verification_required=case_context['extra_verification_required'],
        experiment_arm=case_context['experiment_arm'],
        live_graph_trial_mode='auto',
        generator_version='lmd-generator-v1',
        policy_version='lmd-policy-v1',
        shadow_limit=5,
        trial_limit=2,
        db_url=cli_args.db_url,
        psql=cli_args.psql,
        phase11_policy_path='',
        phase11_disable_learned_policy=False,
        out='',
        dry_run=True,
        pretty=False,
    )


def normalize_rank_rows(rows: list[dict[str, Any]], *, key_field: str, score_field: str, breakdown_field: str = 'score_breakdown', why_field: str | None = None) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    for idx, row in enumerate(rows, start=1):
        key = coerce_string(row.get(key_field))
        if not key:
            continue
        item = {
            'key': key,
            'rank': idx,
            'score': round(safe_float(row.get(score_field)), 3),
            'score_breakdown': row.get(breakdown_field) if isinstance(row.get(breakdown_field), dict) else {},
        }
        if why_field:
            why = coerce_string(row.get(why_field))
            if why:
                item['why'] = why
        normalized.append(item)
    return normalized


def compare_rankings(*, baseline_rows: list[dict[str, Any]], learned_rows: list[dict[str, Any]], top_n: int = 3) -> dict[str, Any]:
    baseline_by_key = {row['key']: row for row in baseline_rows}
    learned_by_key = {row['key']: row for row in learned_rows}
    ordered_keys: list[str] = []
    seen: set[str] = set()
    for row in baseline_rows + learned_rows:
        key = row['key']
        if key in seen:
            continue
        seen.add(key)
        ordered_keys.append(key)

    shifts: list[dict[str, Any]] = []
    for key in ordered_keys:
        before = baseline_by_key.get(key)
        after = learned_by_key.get(key)
        before_rank = before.get('rank') if before else None
        after_rank = after.get('rank') if after else None
        rank_delta = None
        if before_rank is not None and after_rank is not None:
            rank_delta = before_rank - after_rank
        before_score = safe_float(before.get('score')) if before else None
        after_score = safe_float(after.get('score')) if after else None
        score_delta = None
        if before_score is not None and after_score is not None:
            score_delta = round(after_score - before_score, 3)
        shifts.append({
            'key': key,
            'baseline_rank': before_rank,
            'learned_rank': after_rank,
            'rank_delta': rank_delta,
            'baseline_score': before_score,
            'learned_score': after_score,
            'score_delta': score_delta,
            'entered': before is None and after is not None,
            'dropped': before is not None and after is None,
            'baseline_breakdown': before.get('score_breakdown') if before else {},
            'learned_breakdown': after.get('score_breakdown') if after else {},
            'baseline_why': before.get('why') if before else None,
            'learned_why': after.get('why') if after else None,
        })

    def shift_sort_key(item: dict[str, Any]) -> tuple[float, float, int]:
        rank_delta = abs(int(item['rank_delta'])) if item.get('rank_delta') is not None else 99 if item.get('entered') or item.get('dropped') else 0
        score_delta = abs(safe_float(item.get('score_delta')))
        novelty = 1 if item.get('entered') or item.get('dropped') else 0
        return (rank_delta, score_delta, novelty)

    top_baseline = [row['key'] for row in baseline_rows[:top_n]]
    top_learned = [row['key'] for row in learned_rows[:top_n]]
    overlap = sorted(set(top_baseline) & set(top_learned))
    return {
        'baseline_top1': top_baseline[0] if top_baseline else None,
        'learned_top1': top_learned[0] if top_learned else None,
        'top1_changed': bool(top_baseline[:1] != top_learned[:1]),
        'baseline_count': len(baseline_rows),
        'learned_count': len(learned_rows),
        'top_n': top_n,
        'top_n_overlap_count': len(overlap),
        'top_n_overlap_keys': overlap,
        'shifts': sorted(shifts, key=shift_sort_key, reverse=True),
    }


def summarize_bundle(bundle: dict[str, Any]) -> dict[str, Any]:
    debug_phase11 = ((bundle.get('debug') or {}).get('phase11') or {}) if isinstance(bundle.get('debug'), dict) else {}
    results = bundle.get('results') if isinstance(bundle.get('results'), dict) else {}
    trial_overlay = bundle.get('trial_overlay') if isinstance(bundle.get('trial_overlay'), dict) else {}
    return {
        'status': coerce_string(bundle.get('status')),
        'case_reviews': normalize_rank_rows(list(results.get('case_reviews') or []), key_field='case_key', score_field='retrieval_score', why_field='why_retrieved'),
        'active_interventions': normalize_rank_rows(list(results.get('active_interventions') or []), key_field='intervention_key', score_field='retrieval_score', why_field='why_retrieved'),
        'aggregate_notes': normalize_rank_rows(list(results.get('aggregate_notes') or []), key_field='path', score_field='retrieval_score', why_field='why_retrieved'),
        'trial_overlay': normalize_rank_rows(list(trial_overlay.get('selected_candidates') or []), key_field='proposal_key', score_field='overlay_score'),
        'live_nodes': normalize_rank_rows(list(debug_phase11.get('live_nodes_ranked') or []), key_field='node_key', score_field='score'),
        'live_edges': normalize_rank_rows(list(debug_phase11.get('live_edges_ranked') or []), key_field='edge_key', score_field='score'),
    }


def compare_case(case_context: dict[str, Any], cli_args: argparse.Namespace, generate_lmd_bundle) -> dict[str, Any]:
    lmd_args = build_lmd_args(case_context, cli_args)
    baseline_policy = copy.deepcopy(DEFAULT_POLICY)
    baseline_policy['loaded_from_file'] = False
    baseline_policy['source_path'] = 'DEFAULT_POLICY'
    learned_policy_path = Path(cli_args.policy_path)
    if not learned_policy_path.is_absolute():
        learned_policy_path = (WORKSPACE_ROOT / cli_args.policy_path).resolve()
    learned_policy = load_phase11_retrieval_policy(learned_policy_path)

    baseline_bundle = generate_lmd_bundle.build_bundle(lmd_args, phase11_policy=baseline_policy)
    learned_bundle = generate_lmd_bundle.build_bundle(lmd_args, phase11_policy=learned_policy)

    baseline_summary = summarize_bundle(baseline_bundle)
    learned_summary = summarize_bundle(learned_bundle)
    surfaces = {
        'case_reviews': compare_rankings(baseline_rows=baseline_summary['case_reviews'], learned_rows=learned_summary['case_reviews']),
        'active_interventions': compare_rankings(baseline_rows=baseline_summary['active_interventions'], learned_rows=learned_summary['active_interventions']),
        'aggregate_notes': compare_rankings(baseline_rows=baseline_summary['aggregate_notes'], learned_rows=learned_summary['aggregate_notes']),
        'trial_overlay': compare_rankings(baseline_rows=baseline_summary['trial_overlay'], learned_rows=learned_summary['trial_overlay']),
        'live_nodes': compare_rankings(baseline_rows=baseline_summary['live_nodes'], learned_rows=learned_summary['live_nodes']),
        'live_edges': compare_rankings(baseline_rows=baseline_summary['live_edges'], learned_rows=learned_summary['live_edges']),
    }
    return {
        'case_key': case_context['case_key'],
        'title': case_context['title'],
        'platform': case_context['platform'],
        'market_id': case_context['market_id'],
        'input_context': case_context,
        'comparison': surfaces,
        'baseline': baseline_summary,
        'learned': learned_summary,
    }


def surface_has_any_change(surface_report: dict[str, Any]) -> bool:
    if bool(surface_report.get('top1_changed')):
        return True
    for shift in surface_report.get('shifts') or []:
        if shift.get('entered') or shift.get('dropped'):
            return True
        if shift.get('rank_delta') not in (None, 0):
            return True
        if abs(safe_float(shift.get('score_delta'))) > 1e-9:
            return True
    return False



def build_summary(case_reports: list[dict[str, Any]], policy_path: str) -> dict[str, Any]:
    surfaces = ['case_reviews', 'active_interventions', 'aggregate_notes', 'trial_overlay', 'live_nodes', 'live_edges']
    top1_change_counts = {surface: 0 for surface in surfaces}
    any_change_counts = {surface: 0 for surface in surfaces}
    any_top1_change_cases = 0
    any_surface_change_cases = 0
    for report in case_reports:
        top1_changed = False
        any_changed = False
        comparison = report.get('comparison') if isinstance(report.get('comparison'), dict) else {}
        for surface in surfaces:
            surface_report = comparison.get(surface) or {}
            if bool(surface_report.get('top1_changed')):
                top1_change_counts[surface] += 1
                top1_changed = True
            if surface_has_any_change(surface_report):
                any_change_counts[surface] += 1
                any_changed = True
        if top1_changed:
            any_top1_change_cases += 1
        if any_changed:
            any_surface_change_cases += 1
    return {
        'generated_at': utc_now_iso(),
        'comparison_mode': 'default_normalized_priors_vs_normalized_plus_learned_overrides',
        'policy_path': policy_path,
        'case_count': len(case_reports),
        'cases_with_any_top1_change': any_top1_change_cases,
        'cases_with_any_surface_change': any_surface_change_cases,
        'top1_change_counts': top1_change_counts,
        'any_change_counts': any_change_counts,
    }


def render_markdown(report: dict[str, Any]) -> str:
    summary = report.get('summary') if isinstance(report.get('summary'), dict) else {}
    lines = [
        '# Phase 11 retrieval policy report',
        '',
        f"- generated_at: `{summary.get('generated_at')}`",
        f"- comparison_mode: `{summary.get('comparison_mode')}`",
        f"- policy_path: `{summary.get('policy_path')}`",
        f"- case_count: `{summary.get('case_count')}`",
        f"- cases_with_any_top1_change: `{summary.get('cases_with_any_top1_change')}`",
        f"- cases_with_any_surface_change: `{summary.get('cases_with_any_surface_change')}`",
        '',
        '## Top-1 change counts by surface',
    ]
    for surface, count in (summary.get('top1_change_counts') or {}).items():
        lines.append(f'- `{surface}`: `{count}`')
    lines.extend([
        '',
        '## Any-change counts by surface',
    ])
    for surface, count in (summary.get('any_change_counts') or {}).items():
        lines.append(f'- `{surface}`: `{count}`')

    for case_report in report.get('cases') or []:
        lines.extend([
            '',
            f"## {case_report.get('case_key')} — {case_report.get('title')}",
            '',
            f"- platform: `{case_report.get('platform')}`",
            f"- market_id: `{case_report.get('market_id')}`",
        ])
        comparison = case_report.get('comparison') if isinstance(case_report.get('comparison'), dict) else {}
        for surface, label in [
            ('case_reviews', 'Case reviews'),
            ('active_interventions', 'Active interventions'),
            ('aggregate_notes', 'Aggregate notes'),
            ('trial_overlay', 'Trial overlay'),
            ('live_nodes', 'Live nodes'),
            ('live_edges', 'Live edges'),
        ]:
            surface_report = comparison.get(surface) if isinstance(comparison.get(surface), dict) else {}
            lines.extend([
                '',
                f"### {label}",
                f"- baseline_top1: `{surface_report.get('baseline_top1')}`",
                f"- learned_top1: `{surface_report.get('learned_top1')}`",
                f"- top1_changed: `{surface_report.get('top1_changed')}`",
                f"- any_change: `{surface_has_any_change(surface_report)}`",
                f"- top_{surface_report.get('top_n')}_overlap: `{surface_report.get('top_n_overlap_count')}` / `{surface_report.get('top_n')}`",
            ])
            shifts = list(surface_report.get('shifts') or [])[:3]
            if shifts:
                lines.append('- biggest shifts:')
                for shift in shifts:
                    lines.append(
                        '  - '
                        + f"`{shift.get('key')}` baseline_rank={shift.get('baseline_rank')} learned_rank={shift.get('learned_rank')} "
                        + f"baseline_score={shift.get('baseline_score')} learned_score={shift.get('learned_score')}"
                    )
    return '\n'.join(lines).rstrip() + '\n'


def main() -> int:
    args = parse_args()
    generate_lmd_bundle = load_generate_lmd_bundle_module()
    case_keys = [coerce_string(item) for item in args.case_key if coerce_string(item)]
    if not case_keys:
        case_keys = recent_case_keys(args.max_cases)
    case_reports: list[dict[str, Any]] = []
    for case_key in case_keys:
        case_context = load_case_context(case_key)
        if not case_context['market_id'] or not case_context['title']:
            continue
        case_reports.append(compare_case(case_context, args, generate_lmd_bundle))

    policy_path = str((WORKSPACE_ROOT / args.policy_path).resolve()) if not Path(args.policy_path).is_absolute() else str(Path(args.policy_path))
    report = {
        'summary': build_summary(case_reports, policy_path),
        'cases': case_reports,
    }
    markdown = render_markdown(report)

    json_out = Path(args.json_out)
    if not json_out.is_absolute():
        json_out = (WORKSPACE_ROOT / args.json_out).resolve()
    md_out = Path(args.md_out)
    if not md_out.is_absolute():
        md_out = (WORKSPACE_ROOT / args.md_out).resolve()

    if not args.dry_run:
        json_out.parent.mkdir(parents=True, exist_ok=True)
        md_out.parent.mkdir(parents=True, exist_ok=True)
        write_json(json_out, report, pretty=True)
        md_out.write_text(markdown, encoding='utf-8')

    result = {
        'ok': True,
        'case_count': len(case_reports),
        'json_out': relative_to_workspace(json_out),
        'md_out': relative_to_workspace(md_out),
        'summary': report['summary'],
        'cases': [
            {
                'case_key': row.get('case_key'),
                'title': row.get('title'),
                'top1_change_flags': {
                    surface: bool(((row.get('comparison') or {}).get(surface) or {}).get('top1_changed'))
                    for surface in ['case_reviews', 'active_interventions', 'aggregate_notes', 'trial_overlay', 'live_nodes', 'live_edges']
                },
                'any_change_flags': {
                    surface: surface_has_any_change((row.get('comparison') or {}).get(surface) or {})
                    for surface in ['case_reviews', 'active_interventions', 'aggregate_notes', 'trial_overlay', 'live_nodes', 'live_edges']
                },
            }
            for row in case_reports
        ],
    }
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
