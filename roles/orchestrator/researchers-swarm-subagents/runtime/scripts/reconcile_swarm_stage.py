#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[4]
if str(REPO_ROOT / 'scripts') not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / 'scripts'))

from case_pipeline_status import summarize_case_pipeline_status, update_case_pipeline_status_with_followups as update_case_pipeline_status  # noqa: E402

WORKSPACE_ROOT = REPO_ROOT
EXPECTED_PERSONAS = [
    'base-rate',
    'catalyst-hunter',
    'market-implied',
    'risk-manager',
    'variant-view',
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Reconcile swarm-stage status for a dispatch/case')
    parser.add_argument('--case-key')
    parser.add_argument('--dispatch-dir')
    parser.add_argument('--stale-seconds', type=float, default=900.0)
    parser.add_argument('--out')
    parser.add_argument('--check-only', action='store_true', help='Do not write swarm-stage-status.json or update pipeline-status.json')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text())
    return payload if isinstance(payload, dict) else {}


def write_json(path: Path, payload: dict[str, Any], *, pretty: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2 if pretty else None, sort_keys=pretty) + '\n')


def relative_to_workspace(path: Path | None) -> str:
    if path is None:
        return ''
    candidate = Path(path)
    if not candidate.is_absolute():
        return str(candidate)
    try:
        return str(candidate.relative_to(WORKSPACE_ROOT))
    except ValueError:
        return str(candidate)


def canonical_dispatch_dir_from_case_status(case_key: str) -> Path | None:
    summary = summarize_case_pipeline_status(case_key)
    dispatch_id = str(summary.get('dispatch_id') or '').strip()
    if not dispatch_id:
        return None
    analyses_root = WORKSPACE_ROOT / 'qualitative-db' / '40-research' / 'cases' / case_key / 'researcher-analyses'
    for candidate in analyses_root.glob(f'*/{dispatch_id}'):
        if candidate.is_dir():
            return candidate.resolve()
    return None


def resolve_dispatch_dir(case_key: str) -> Path:
    canonical = canonical_dispatch_dir_from_case_status(case_key)
    if canonical is not None:
        return canonical
    analyses_root = WORKSPACE_ROOT / 'qualitative-db' / '40-research' / 'cases' / case_key / 'researcher-analyses'
    candidates = sorted(analyses_root.glob('*/dispatch-case-*'), key=lambda p: p.stat().st_mtime, reverse=True)
    if not candidates:
        raise FileNotFoundError(f'no dispatch directory found for case {case_key}')
    full_named = [p for p in candidates if p.name.startswith(f'dispatch-{case_key}-')]
    if full_named:
        return full_named[0]
    return candidates[0]


def dispatch_id_from_dir(dispatch_dir: Path) -> str:
    return dispatch_dir.name if dispatch_dir.name.startswith('dispatch-case-') else ''


def is_short_fallback_dispatch_dir(dispatch_dir: Path, *, case_key: str) -> bool:
    name = dispatch_dir.name
    return name.startswith('dispatch-case-') and not name.startswith(f'dispatch-{case_key}-')


def find_manifest(dispatch_id: str) -> Path | None:
    manifest = REPO_ROOT / 'roles' / 'orchestrator' / 'researchers-swarm-subagents' / 'runtime' / 'dispatch-manifests' / f'{dispatch_id}.json'
    return manifest if manifest.exists() else None


def latest_mtime(paths: list[Path]) -> float:
    values = [p.stat().st_mtime for p in paths if p.exists()]
    return max(values) if values else 0.0


def classify_swarm(*, completed_personas: list[str], synthesis_status: str, latest_update_seconds_ago: float, stale_seconds: float) -> tuple[str, str, list[str], str]:
    missing = [p for p in EXPECTED_PERSONAS if p not in completed_personas]
    if synthesis_status == 'synthesis_completed':
        return 'completed', 'completed', missing, 'swarm and synthesis already completed'
    if not missing:
        return 'ready_for_synthesis', 'ready_for_synthesis', missing, 'all expected personas are present; synthesis may be launched/resumed'
    if latest_update_seconds_ago > stale_seconds:
        return 'stale', 'stale', missing, 'swarm appears incomplete and stale; resume the same dispatch'
    return 'in_progress', 'in_progress', missing, 'swarm is still progressing or recently updated'


def main() -> None:
    args = parse_args()
    if not args.case_key and not args.dispatch_dir:
        raise SystemExit('one of --case-key or --dispatch-dir is required')

    dispatch_dir = Path(args.dispatch_dir).resolve() if args.dispatch_dir else resolve_dispatch_dir(args.case_key)
    case_key = args.case_key or next((part for part in dispatch_dir.parts if part.startswith('case-')), '')
    if case_key and is_short_fallback_dispatch_dir(dispatch_dir, case_key=case_key):
        canonical = canonical_dispatch_dir_from_case_status(case_key)
        if canonical is not None and canonical != dispatch_dir:
            dispatch_dir = canonical
    dispatch_id = dispatch_id_from_dir(dispatch_dir)
    manifest_path = find_manifest(dispatch_id)
    personas_dir = dispatch_dir / 'personas'
    assumptions_dir = dispatch_dir / 'assumptions'
    evidence_dir = dispatch_dir / 'evidence'
    summary_path = dispatch_dir / 'summary.md'
    synthesis_status_path = dispatch_dir / 'synthesis-stage-status.json'

    completed_personas = sorted(p.stem for p in personas_dir.glob('*.md')) if personas_dir.exists() else []
    completed_assumptions = sorted(p.stem for p in assumptions_dir.glob('*.md')) if assumptions_dir.exists() else []
    completed_evidence = sorted(p.stem for p in evidence_dir.glob('*.md')) if evidence_dir.exists() else []
    synthesis_status_payload = load_json(synthesis_status_path) if synthesis_status_path.exists() else {}
    synthesis_status = str(synthesis_status_payload.get('status') or '').strip()

    scan_paths: list[Path] = []
    for path in [summary_path, synthesis_status_path]:
        if path.exists():
            scan_paths.append(path)
    for directory in [personas_dir, assumptions_dir, evidence_dir]:
        if directory.exists():
            scan_paths.extend(sorted(directory.glob('*.md')))
    latest_update_ts = latest_mtime(scan_paths)
    now_ts = datetime.now(timezone.utc).timestamp()
    latest_update_seconds_ago = max(0.0, now_ts - latest_update_ts) if latest_update_ts else float('inf')

    status, health, missing_personas, recommendation = classify_swarm(
        completed_personas=completed_personas,
        synthesis_status=synthesis_status,
        latest_update_seconds_ago=latest_update_seconds_ago,
        stale_seconds=args.stale_seconds,
    )

    out_path = Path(args.out).resolve() if args.out else dispatch_dir / 'swarm-stage-status.json'
    payload = {
        'artifact_type': 'swarm_stage_status',
        'schema_version': 'swarm-stage-status/v1',
        'generated_at': utc_now_iso(),
        'case_key': case_key,
        'dispatch_id': dispatch_id,
        'dispatch_dir': relative_to_workspace(dispatch_dir),
        'manifest_path': relative_to_workspace(manifest_path),
        'status': status,
        'health': health,
        'expected_personas': EXPECTED_PERSONAS,
        'completed_personas': completed_personas,
        'missing_personas': missing_personas,
        'completed_assumptions': completed_assumptions,
        'completed_evidence': completed_evidence,
        'summary_exists': summary_path.exists(),
        'synthesis_status': synthesis_status,
        'synthesis_status_path': relative_to_workspace(synthesis_status_path) if synthesis_status_path.exists() else '',
        'latest_update_seconds_ago': latest_update_seconds_ago,
        'stale_seconds_threshold': args.stale_seconds,
        'recommendation': recommendation,
        'recommended_resume_command': (
            f"python3 roles/orchestrator/researchers-swarm-subagents/runtime/scripts/resume_swarm_stage.py --case-key {case_key} --pretty"
            if case_key else ''
        ),
        'status_file_path': relative_to_workspace(out_path),
        'check_only': bool(args.check_only),
    }

    if not args.check_only:
        if case_key:
            current_summary = summarize_case_pipeline_status(case_key)
            current_status = str(current_summary.get('status') or '').strip()
            if current_status not in {'pipeline_completed', 'pipeline_failed', 'pipeline_skipped'}:
                stage_state = 'completed' if status in {'completed', 'ready_for_synthesis'} else 'in_progress' if status == 'in_progress' else 'failed' if status == 'stale' else 'pending'
                update_case_pipeline_status(
                    case_key=case_key,
                    dispatch_id=dispatch_id,
                    status='pipeline_in_progress',
                    current_stage='swarm' if status in {'in_progress', 'stale'} else 'synthesis' if status == 'ready_for_synthesis' else 'decision' if status == 'completed' else 'swarm',
                    stage_status_patch={'swarm': stage_state},
                    runner_id='reconcile_swarm_stage',
                    message='Swarm stage reconciled',
                    terminal_summary_patch={'swarm_stage_status_path': relative_to_workspace(out_path)},
                )
            else:
                payload['canonical_update_skipped'] = True
                payload['canonical_status_preserved'] = current_status
        write_json(out_path, payload, pretty=True)

    print(json.dumps(payload, indent=2 if args.pretty else None))


if __name__ == '__main__':
    main()
