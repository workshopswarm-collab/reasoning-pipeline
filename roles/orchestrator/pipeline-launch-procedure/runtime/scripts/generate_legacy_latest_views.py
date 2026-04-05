#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
ROOT = Path(__file__).resolve().parents[5]

SQL = r'''
SELECT json_build_object(
  'research_run_id', rr.id,
  'agent_label', rr.agent_label,
  'workspace_note_path', rr.workspace_note_path,
  'case_key', c.case_key,
  'slug', m.slug,
  'dispatch_id', rr.notes->>'dispatch_id'
)::text
FROM research_runs rr
JOIN cases c ON c.id = rr.case_id
JOIN markets m ON m.id = c.market_id
WHERE rr.id = NULLIF(:'research_run_id', '')::uuid
LIMIT 1;
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate legacy latest-view compatibility notes when canonical files exist")
    parser.add_argument("--research-run-id", required=True)
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""))
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL))
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def run_sql(psql_bin: str, db_url: str, sql_text: str, variables: dict[str, str]) -> dict:
    proc = subprocess.run(
        [psql_bin, db_url, '-X', '-qAt', '-v', 'ON_ERROR_STOP=1', *sum((["-v", f"{k}={v}"] for k, v in variables.items()), []), '-f', '-'],
        input=sql_text,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'psql failed')
    stdout = proc.stdout.strip()
    return json.loads(stdout.splitlines()[-1]) if stdout else {}


def legacy_persona_note_path(case_key: str, slug: str | None, persona: str) -> Path:
    safe_slug = slug or 'market'
    return ROOT / f"qualitative-db/40-research/agent-findings/{persona}/{case_key}-{safe_slug}.md"


def legacy_assumption_note_path(case_key: str, persona: str) -> Path:
    return ROOT / f"qualitative-db/40-research/assumption-notes/{case_key}-{persona}-assumptions.md"


def legacy_evidence_map_path(case_key: str, persona: str) -> Path:
    return ROOT / f"qualitative-db/40-research/evidence-maps/{case_key}-{persona}-evidence-map.md"


def compatibility_note_body(*, case_key: str, dispatch_id: str, canonical_path: str, note_kind: str, persona: str) -> str:
    vault_target = canonical_path.replace('qualitative-db/', '').removesuffix('.md')
    return (
        "---\n"
        "type: compatibility_latest_view\n"
        f"case_key: {case_key}\n"
        f"dispatch_id: {dispatch_id}\n"
        f"note_kind: {note_kind}\n"
        f"persona: {persona}\n"
        f"canonical_path: {canonical_path}\n"
        "generated_by: orchestrator\n"
        "---\n\n"
        f"# Latest view — {persona}\n\n"
        "This is a generated compatibility/latest-view note.\n"
        "Do not treat it as canonical history.\n\n"
        f"- latest dispatch: `{dispatch_id}`\n"
        f"- canonical note: `{canonical_path}`\n\n"
        f"![[{vault_target}]]\n"
    )


def maybe_write(path: Path, body: str) -> str:
    if path.exists():
        try:
            existing = path.read_text()
        except Exception:
            existing = ''
        if 'type: compatibility_latest_view' not in existing:
            return 'preserved_existing'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body)
    return 'written'


def main() -> int:
    args = parse_args()
    try:
        row = run_sql(args.psql, args.db_url, SQL, {'research_run_id': args.research_run_id})
        if not row:
            raise ValueError('research run not found')
        case_key = row['case_key']
        dispatch_id = row.get('dispatch_id') or ''
        persona = row['agent_label']
        slug = row.get('slug')
        canonical_persona = ROOT / row['workspace_note_path']
        analysis_root = canonical_persona.parent.parent
        canonical_assumption = analysis_root / 'assumptions' / f'{persona}.md'
        canonical_evidence = analysis_root / 'evidence' / f'{persona}.md'

        results = {'persona': None, 'assumption': 'missing_canonical', 'evidence': 'missing_canonical'}
        if canonical_persona.exists():
            results['persona'] = maybe_write(
                legacy_persona_note_path(case_key, slug, persona),
                compatibility_note_body(case_key=case_key, dispatch_id=dispatch_id, canonical_path=row['workspace_note_path'], note_kind='persona_finding', persona=persona),
            )
        else:
            results['persona'] = 'missing_canonical'
        if canonical_assumption.exists():
            results['assumption'] = maybe_write(
                legacy_assumption_note_path(case_key, persona),
                compatibility_note_body(case_key=case_key, dispatch_id=dispatch_id, canonical_path=str(canonical_assumption.relative_to(ROOT)), note_kind='assumption_note', persona=persona),
            )
        if canonical_evidence.exists():
            results['evidence'] = maybe_write(
                legacy_evidence_map_path(case_key, persona),
                compatibility_note_body(case_key=case_key, dispatch_id=dispatch_id, canonical_path=str(canonical_evidence.relative_to(ROOT)), note_kind='evidence_map', persona=persona),
            )
        payload = {'status': 'ok', 'research_run_id': args.research_run_id, 'results': results}
    except Exception as exc:  # noqa: BLE001
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    print(json.dumps(payload, indent=2 if args.pretty else None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
