#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from case_pipeline_status import list_case_pipeline_statuses

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES_ROOT = REPO_ROOT / 'qualitative-db' / '40-research' / 'cases'
DEFAULT_REPORT_FILE = REPO_ROOT / 'scripts' / '.runtime-state' / 'pipeline-artifact-contract-report.json'
CANONICAL_CASE_KEY_RE = re.compile(r'^case-\d{8}-[a-f0-9]{8}$')
DISPATCH_CASE_KEY_RE = re.compile(r'(case-\d{8}-[a-f0-9]{8})')


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def load_json_if_exists(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')


def is_canonical_case_key(value: str) -> bool:
    return bool(CANONICAL_CASE_KEY_RE.match(str(value or '').strip()))


def case_key_from_dispatch_id(dispatch_id: str) -> str:
    match = DISPATCH_CASE_KEY_RE.search(str(dispatch_id or '').strip())
    return match.group(1) if match else ''


def add_issue(issues: list[dict[str, Any]], *, level: str, code: str, message: str, **extra: Any) -> None:
    issue = {'level': level, 'code': code, 'message': message}
    issue.update(extra)
    issues.append(issue)


def is_repaired_legacy_status_path(root: Path, source_path: Path, *, payload_case_key: str, dispatch_id: str) -> bool:
    target_case_key = payload_case_key if is_canonical_case_key(payload_case_key) else case_key_from_dispatch_id(dispatch_id)
    if not target_case_key:
        return False
    target_payload = load_json_if_exists(root / target_case_key / 'pipeline-status.json')
    repair_metadata = target_payload.get('repair_metadata') if isinstance(target_payload.get('repair_metadata'), dict) else {}
    repaired_from = repair_metadata.get('repaired_from_legacy_paths') if isinstance(repair_metadata.get('repaired_from_legacy_paths'), list) else []
    rel_source = str(source_path.relative_to(REPO_ROOT))
    return rel_source in {str(item) for item in repaired_from}


def evaluate_case_artifact_contract(cases_root: Path | None = None, *, report_file: Path | None = None) -> dict[str, Any]:
    root = (cases_root or DEFAULT_CASES_ROOT).expanduser().resolve()
    issues: list[dict[str, Any]] = []
    canonical_case_dirs = 0
    legacy_status_dirs = 0
    repaired_legacy_status_dirs = 0

    if not root.exists():
        add_issue(issues, level='error', code='missing_cases_root', message='Cases root does not exist', path=str(root))
    else:
        for case_dir in sorted(path for path in root.iterdir() if path.is_dir()):
            case_name = case_dir.name
            canonical = is_canonical_case_key(case_name)
            if canonical:
                canonical_case_dirs += 1

            pipeline_status_path = case_dir / 'pipeline-status.json'
            payload = load_json_if_exists(pipeline_status_path) if pipeline_status_path.exists() else {}
            payload_case_key = str(payload.get('case_key') or '').strip()
            dispatch_id = str(payload.get('dispatch_id') or '').strip()
            dispatch_case_key = case_key_from_dispatch_id(dispatch_id)

            if pipeline_status_path.exists() and not canonical:
                legacy_status_dirs += 1
                if is_repaired_legacy_status_path(root, pipeline_status_path, payload_case_key=payload_case_key, dispatch_id=dispatch_id):
                    repaired_legacy_status_dirs += 1
                else:
                    add_issue(
                        issues,
                        level='error',
                        code='legacy_pipeline_status_dir',
                        message='Found non-canonical case directory containing pipeline-status.json',
                        case_dir=case_name,
                        path=str(pipeline_status_path.relative_to(REPO_ROOT)),
                        payload_case_key=payload_case_key,
                        dispatch_id=dispatch_id,
                    )

            if pipeline_status_path.exists() and canonical:
                if not payload_case_key:
                    add_issue(
                        issues,
                        level='error',
                        code='missing_pipeline_status_case_key',
                        message='Canonical case pipeline-status.json is missing case_key',
                        case_key=case_name,
                        path=str(pipeline_status_path.relative_to(REPO_ROOT)),
                    )
                elif not is_canonical_case_key(payload_case_key):
                    add_issue(
                        issues,
                        level='error',
                        code='noncanonical_pipeline_status_case_key',
                        message='pipeline-status.json case_key is not canonical',
                        case_key=case_name,
                        payload_case_key=payload_case_key,
                        path=str(pipeline_status_path.relative_to(REPO_ROOT)),
                    )
                elif payload_case_key != case_name:
                    add_issue(
                        issues,
                        level='error',
                        code='pipeline_status_case_key_mismatch',
                        message='pipeline-status.json case_key does not match containing case directory',
                        case_key=case_name,
                        payload_case_key=payload_case_key,
                        path=str(pipeline_status_path.relative_to(REPO_ROOT)),
                    )

                if dispatch_case_key and dispatch_case_key != case_name:
                    add_issue(
                        issues,
                        level='error',
                        code='dispatch_case_key_mismatch',
                        message='pipeline-status.json dispatch_id resolves to a different canonical case key than its containing directory',
                        case_key=case_name,
                        dispatch_case_key=dispatch_case_key,
                        dispatch_id=dispatch_id,
                        path=str(pipeline_status_path.relative_to(REPO_ROOT)),
                    )

            analyses_root = case_dir / 'researcher-analyses'
            has_dispatch_workspace = any(analyses_root.glob('*/dispatch-case-*')) if analyses_root.exists() else False
            if canonical and has_dispatch_workspace:
                if not pipeline_status_path.exists():
                    add_issue(
                        issues,
                        level='warn',
                        code='missing_pipeline_status_for_dispatch_workspace',
                        message='Canonical case has dispatch workspace artifacts but no case-root pipeline-status.json',
                        case_key=case_name,
                    )
                if not (case_dir / 'researcher-swarm-summary.md').exists():
                    add_issue(
                        issues,
                        level='warn',
                        code='missing_researcher_swarm_summary',
                        message='Canonical case has dispatch workspace artifacts but is missing case-root researcher-swarm-summary.md',
                        case_key=case_name,
                    )
                if not (case_dir / 'researcher-swarm-current.md').exists():
                    add_issue(
                        issues,
                        level='warn',
                        code='missing_researcher_swarm_current',
                        message='Canonical case has dispatch workspace artifacts but is missing case-root researcher-swarm-current.md',
                        case_key=case_name,
                    )
                if not (case_dir / 'artifacts' / 'index.json').exists():
                    add_issue(
                        issues,
                        level='warn',
                        code='missing_case_artifacts_index',
                        message='Canonical case has dispatch workspace artifacts but is missing case-root artifacts/index.json',
                        case_key=case_name,
                    )

    active_nonterminal_cases = list_case_pipeline_statuses(include_terminal=False)
    if len(active_nonterminal_cases) > 1:
        add_issue(
            issues,
            level='error',
            code='multiple_active_canonical_cases',
            message='More than one canonical non-terminal case exists at the same time',
            active_case_keys=[str(item.get('case_key') or '') for item in active_nonterminal_cases],
            active_statuses=[
                {
                    'case_key': str(item.get('case_key') or ''),
                    'status': str(item.get('status') or ''),
                    'current_stage': str(item.get('current_stage') or ''),
                }
                for item in active_nonterminal_cases
            ],
        )

    if any(issue.get('level') == 'error' for issue in issues):
        status = 'error'
        exit_code = 2
    elif issues:
        status = 'warn'
        exit_code = 1
    else:
        status = 'ok'
        exit_code = 0

    report = {
        'status': status,
        'exit_code': exit_code,
        'checked_at': utc_now_iso(),
        'cases_root': str(root),
        'summary': {
            'canonical_case_dirs': canonical_case_dirs,
            'legacy_status_dirs': legacy_status_dirs,
            'repaired_legacy_status_dirs': repaired_legacy_status_dirs,
            'active_nonterminal_case_count': len(active_nonterminal_cases),
            'active_nonterminal_case_keys': [str(item.get('case_key') or '') for item in active_nonterminal_cases],
            'issue_count': len(issues),
            'error_count': sum(1 for item in issues if item.get('level') == 'error'),
            'warn_count': sum(1 for item in issues if item.get('level') == 'warn'),
        },
        'issues': issues,
    }
    if report_file is not None:
        write_json(report_file.expanduser().resolve(), report)
    return report
