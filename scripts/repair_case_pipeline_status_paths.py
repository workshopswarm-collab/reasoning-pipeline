#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
CASES_ROOT = REPO_ROOT / 'qualitative-db' / '40-research' / 'cases'
MATERIALIZE = REPO_ROOT / 'scripts' / 'materialize_case_swarm_artifacts.py'
CASE_KEY_RE = re.compile(r'(case-\d{8}-[a-f0-9]{8})')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Repair UUID-rooted pipeline-status artifacts back into canonical case-key folders')
    parser.add_argument('--apply', action='store_true', help='Write merged pipeline-status files into canonical case roots')
    parser.add_argument('--materialize', action='store_true', help='Re-materialize case-root swarm artifacts after a successful repair write')
    parser.add_argument('--pretty', action='store_true')
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text())
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def dump_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')


def parse_iso(value: str) -> datetime:
    text = str(value or '').strip()
    if not text:
        return datetime.fromtimestamp(0, tz=timezone.utc)
    if text.endswith('Z'):
        text = text[:-1] + '+00:00'
    try:
        dt = datetime.fromisoformat(text)
    except Exception:
        return datetime.fromtimestamp(0, tz=timezone.utc)
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def timeline_entries(payload: dict[str, Any]) -> list[dict[str, Any]]:
    raw = payload.get('timeline')
    return [item for item in raw if isinstance(item, dict)] if isinstance(raw, list) else []


def dedupe_timeline(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    unique: list[dict[str, Any]] = []
    for entry in entries:
        key = json.dumps(entry, sort_keys=True)
        if key in seen:
            continue
        seen.add(key)
        unique.append(entry)
    unique.sort(key=lambda item: (str(item.get('at') or ''), json.dumps(item, sort_keys=True)))
    return unique


def canonical_case_key_from_dispatch(dispatch_id: str) -> str:
    match = CASE_KEY_RE.search(str(dispatch_id or ''))
    return match.group(1) if match else ''


def canonical_case_key_from_workspace(dispatch_id: str) -> str:
    dispatch_id = str(dispatch_id or '').strip()
    if not dispatch_id:
        return ''
    for path in CASES_ROOT.glob(f'case-*/researcher-analyses/*/{dispatch_id}'):
        if path.is_dir():
            return path.parents[2].name
    return ''


def resolve_target_case_key(source_dir: Path, payload: dict[str, Any]) -> tuple[str, str]:
    payload_case_key = str(payload.get('case_key') or '').strip()
    if payload_case_key.startswith('case-'):
        return payload_case_key, 'payload.case_key'

    dispatch_id = str(payload.get('dispatch_id') or '').strip()
    from_dispatch = canonical_case_key_from_dispatch(dispatch_id)
    if from_dispatch:
        return from_dispatch, 'dispatch_id'

    from_workspace = canonical_case_key_from_workspace(dispatch_id)
    if from_workspace:
        return from_workspace, 'workspace_lookup'

    for entry in timeline_entries(payload):
        for key in ('manifest_path', 'dispatch_id'):
            candidate = canonical_case_key_from_dispatch(str(entry.get(key) or ''))
            if candidate:
                return candidate, f'timeline.{key}'

    return '', 'unresolved'


def merge_status_payloads(target_case_key: str, source_path: Path, source_payload: dict[str, Any], target_payload: dict[str, Any]) -> dict[str, Any]:
    source_updated = parse_iso(str(source_payload.get('updated_at') or ''))
    target_updated = parse_iso(str(target_payload.get('updated_at') or ''))
    base = dict(source_payload if source_updated >= target_updated else target_payload)
    other = target_payload if base is source_payload else source_payload

    for key, value in other.items():
        if key not in base or base.get(key) in ('', None, [], {}):
            base[key] = value

    merged_timeline = dedupe_timeline(timeline_entries(target_payload) + timeline_entries(source_payload))
    if merged_timeline:
        base['timeline'] = merged_timeline
        base['last_event'] = merged_timeline[-1]

    merged_stage_statuses = {}
    if isinstance(target_payload.get('stage_statuses'), dict):
        merged_stage_statuses.update(target_payload.get('stage_statuses') or {})
    if isinstance(source_payload.get('stage_statuses'), dict):
        merged_stage_statuses.update(source_payload.get('stage_statuses') or {})
    if merged_stage_statuses:
        base['stage_statuses'] = merged_stage_statuses

    merged_terminal_summary = {}
    if isinstance(target_payload.get('terminal_summary'), dict):
        merged_terminal_summary.update(target_payload.get('terminal_summary') or {})
    if isinstance(source_payload.get('terminal_summary'), dict):
        merged_terminal_summary.update(source_payload.get('terminal_summary') or {})
    if merged_terminal_summary:
        base['terminal_summary'] = merged_terminal_summary

    base['artifact_type'] = 'case_pipeline_status'
    base['schema_version'] = 'case-pipeline-status/v1'
    base['case_key'] = target_case_key

    repair_meta = base.get('repair_metadata') if isinstance(base.get('repair_metadata'), dict) else {}
    moved = repair_meta.get('repaired_from_legacy_paths') if isinstance(repair_meta.get('repaired_from_legacy_paths'), list) else []
    rel_source = str(source_path.relative_to(REPO_ROOT))
    if rel_source not in moved:
        moved.append(rel_source)
    repair_meta['repaired_from_legacy_paths'] = sorted(set(moved))
    repair_meta['last_repaired_at'] = datetime.now(timezone.utc).isoformat()
    base['repair_metadata'] = repair_meta
    return base


def maybe_materialize(case_key: str) -> dict[str, Any]:
    if not MATERIALIZE.exists():
        return {'ok': False, 'reason': 'materialize_script_missing'}
    proc = subprocess.run(
        ['python3', str(MATERIALIZE), '--case-key', case_key],
        cwd=str(REPO_ROOT),
        text=True,
        capture_output=True,
        check=False,
    )
    payload = {}
    text = (proc.stdout or '').strip()
    if text:
        try:
            parsed = json.loads(text)
            if isinstance(parsed, dict):
                payload = parsed
        except Exception:
            payload = {}
    return {
        'ok': proc.returncode == 0,
        'returncode': proc.returncode,
        'stdout': proc.stdout,
        'stderr': proc.stderr,
        'payload': payload,
    }


def main() -> int:
    args = parse_args()
    repairs: list[dict[str, Any]] = []

    for source_path in sorted(CASES_ROOT.glob('*/pipeline-status.json')):
        source_dir = source_path.parent
        if source_dir.name.startswith('case-'):
            continue

        source_payload = load_json(source_path)
        target_case_key, resolution = resolve_target_case_key(source_dir, source_payload)
        record: dict[str, Any] = {
            'source_path': str(source_path.relative_to(REPO_ROOT)),
            'source_dir': source_dir.name,
            'source_case_key_field': str(source_payload.get('case_key') or ''),
            'dispatch_id': str(source_payload.get('dispatch_id') or ''),
            'resolution': resolution,
            'target_case_key': target_case_key,
            'applied': False,
        }

        if not target_case_key:
            record['status'] = 'unresolved'
            repairs.append(record)
            continue

        target_path = CASES_ROOT / target_case_key / 'pipeline-status.json'
        record['target_path'] = str(target_path.relative_to(REPO_ROOT))
        target_payload = load_json(target_path)
        repaired_from = []
        if isinstance(target_payload.get('repair_metadata'), dict) and isinstance(target_payload['repair_metadata'].get('repaired_from_legacy_paths'), list):
            repaired_from = [str(item) for item in target_payload['repair_metadata'].get('repaired_from_legacy_paths') or []]
        rel_source = str(source_path.relative_to(REPO_ROOT))
        if rel_source in repaired_from:
            record['status'] = 'already_repaired'
            repairs.append(record)
            continue

        if args.apply:
            merged = merge_status_payloads(target_case_key, source_path, source_payload, target_payload)
            dump_json(target_path, merged)
            record['applied'] = True
            record['status'] = 'repaired'
            record['merged_timeline_count'] = len(timeline_entries(merged))
            if args.materialize:
                record['materialize'] = maybe_materialize(target_case_key)
        else:
            record['status'] = 'would_repair'

        repairs.append(record)

    summary = {
        'ok': True,
        'apply': bool(args.apply),
        'materialize': bool(args.materialize),
        'repair_count': sum(1 for item in repairs if item.get('status') in {'repaired', 'would_repair'}),
        'already_repaired_count': sum(1 for item in repairs if item.get('status') == 'already_repaired'),
        'unresolved_count': sum(1 for item in repairs if item.get('status') == 'unresolved'),
        'repairs': repairs,
    }
    print(json.dumps(summary, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
