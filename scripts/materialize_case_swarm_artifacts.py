#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
CASES_ROOT = REPO_ROOT / 'qualitative-db' / '40-research' / 'cases'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Materialize case-root swarm artifacts from researcher-analyses outputs')
    parser.add_argument('--case-key', required=True)
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def case_dir(case_key: str) -> Path:
    return CASES_ROOT / case_key


def read_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def latest_dispatch_dir(root: Path) -> Path | None:
    analyses_root = root / 'researcher-analyses'
    if not analyses_root.exists():
        return None
    candidates = [p for p in analyses_root.rglob('dispatch-*') if p.is_dir()]
    if not candidates:
        return None
    candidates.sort(key=lambda p: (p.stat().st_mtime, str(p)))
    return candidates[-1]


def build_summary_markdown(case_key: str, dispatch_dir: Path, qmd_bundle: dict[str, Any], summary_text: str) -> str:
    rel_dispatch = dispatch_dir.relative_to(REPO_ROOT)
    metadata = qmd_bundle.get('metadata') if isinstance(qmd_bundle.get('metadata'), dict) else {}
    lines = [
        '# Researcher swarm summary',
        '',
        f'- case_key: `{case_key}`',
        f'- dispatch_dir: `{rel_dispatch}`',
    ]
    for key in ['dispatch_id', 'generated_at', 'market_id', 'market_title']:
        value = metadata.get(key)
        if value:
            lines.append(f'- {key}: `{value}`')
    lines.extend(['', summary_text.strip(), ''])
    return '\n'.join(lines)


def build_current_markdown(case_key: str, dispatch_dir: Path, qmd_bundle: dict[str, Any], pipeline_status: dict[str, Any], summary_text: str) -> str:
    rel_dispatch = dispatch_dir.relative_to(REPO_ROOT)
    metadata = qmd_bundle.get('metadata') if isinstance(qmd_bundle.get('metadata'), dict) else {}
    personas = qmd_bundle.get('personas') if isinstance(qmd_bundle.get('personas'), dict) else {}
    lines = [
        '# Researcher swarm current',
        '',
        f'- case_key: `{case_key}`',
        f'- dispatch_dir: `{rel_dispatch}`',
        f'- pipeline_status: `{pipeline_status.get("status", "")}`',
        f'- current_stage: `{pipeline_status.get("current_stage", "")}`',
    ]
    if metadata.get('generated_at'):
        lines.append(f'- generated_at: `{metadata.get("generated_at")}`')
    lines.extend(['', '## Persona outputs', ''])
    if personas:
        for persona, payload in personas.items():
            note_path = ''
            if isinstance(payload, dict):
                note_path = str(payload.get('workspace_note_path') or payload.get('note_path') or '').strip()
            line = f'- `{persona}`'
            if note_path:
                line += f' -> `{note_path}`'
            lines.append(line)
    else:
        lines.append('- No persona outputs found in qmd-bundle metadata')
    lines.extend(['', '## Summary excerpt', '', summary_text.strip(), ''])
    return '\n'.join(lines)


def write_artifact_index(root: Path, *, dispatch_dir: Path, summary_path: Path, qmd_bundle_path: Path, case_summary_path: Path, case_current_path: Path, pipeline_status_path: Path, synthesized_paths: dict[str, str]) -> Path:
    artifact_dir = root / 'artifacts'
    artifact_dir.mkdir(parents=True, exist_ok=True)
    index_path = artifact_dir / 'index.json'
    payload = {
        'artifact_type': 'case_artifact_index',
        'schema_version': 'case-artifact-index/v1',
        'dispatch_dir': str(dispatch_dir.relative_to(REPO_ROOT)),
        'swarm': {
            'dispatch_summary_path': str(summary_path.relative_to(REPO_ROOT)),
            'dispatch_qmd_bundle_path': str(qmd_bundle_path.relative_to(REPO_ROOT)),
            'case_swarm_summary_path': str(case_summary_path.relative_to(REPO_ROOT)),
            'case_swarm_current_path': str(case_current_path.relative_to(REPO_ROOT)),
        },
        'pipeline_status_path': str(pipeline_status_path.relative_to(REPO_ROOT)) if pipeline_status_path.exists() else '',
        'synthesis': synthesized_paths,
    }
    index_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')
    return index_path


def main() -> int:
    args = parse_args()
    root = case_dir(args.case_key)
    if not root.exists():
        raise SystemExit(f'missing case dir: {root}')
    dispatch_dir = latest_dispatch_dir(root)
    if dispatch_dir is None:
        print(json.dumps({'ok': True, 'noop': True, 'reason': 'no_dispatch_dir', 'case_key': args.case_key}, indent=2 if args.pretty else None))
        return 0

    summary_path = dispatch_dir / 'summary.md'
    qmd_bundle_path = dispatch_dir / 'qmd-bundle.json'
    if not summary_path.exists() or not qmd_bundle_path.exists():
        print(json.dumps({'ok': True, 'noop': True, 'reason': 'missing_dispatch_summary_or_qmd_bundle', 'case_key': args.case_key, 'dispatch_dir': str(dispatch_dir.relative_to(REPO_ROOT))}, indent=2 if args.pretty else None))
        return 0

    summary_text = summary_path.read_text(errors='ignore')
    qmd_bundle = read_json(qmd_bundle_path)
    pipeline_status_path = root / 'pipeline-status.json'
    pipeline_status = read_json(pipeline_status_path) if pipeline_status_path.exists() else {}

    case_summary_path = root / 'researcher-swarm-summary.md'
    case_current_path = root / 'researcher-swarm-current.md'
    case_summary_path.write_text(build_summary_markdown(args.case_key, dispatch_dir, qmd_bundle, summary_text))
    case_current_path.write_text(build_current_markdown(args.case_key, dispatch_dir, qmd_bundle, pipeline_status, summary_text))

    synth_paths = {}
    for rel in [
        'synthesizer-agent/syndicated-finding.md',
        'synthesizer-agent/syndicated-finding.runtime.json',
        'synthesizer-agent/decision-handoff.md',
        'decision-maker/artifacts/decision-maker-packet.json',
    ]:
        p = root / rel
        if p.exists():
            synth_paths[rel] = str(p.relative_to(REPO_ROOT))

    artifact_index_path = write_artifact_index(
        root,
        dispatch_dir=dispatch_dir,
        summary_path=summary_path,
        qmd_bundle_path=qmd_bundle_path,
        case_summary_path=case_summary_path,
        case_current_path=case_current_path,
        pipeline_status_path=pipeline_status_path,
        synthesized_paths=synth_paths,
    )

    result = {
        'ok': True,
        'case_key': args.case_key,
        'dispatch_dir': str(dispatch_dir.relative_to(REPO_ROOT)),
        'researcher_swarm_summary': str(case_summary_path.relative_to(REPO_ROOT)),
        'researcher_swarm_current': str(case_current_path.relative_to(REPO_ROOT)),
        'artifact_index': str(artifact_index_path.relative_to(REPO_ROOT)),
    }
    print(json.dumps(result, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
