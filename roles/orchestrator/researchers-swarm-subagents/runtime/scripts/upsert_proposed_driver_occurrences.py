#!/usr/bin/env python3
from __future__ import annotations

"""Upsert structured proposed-driver occurrence records for completed research artifacts.

E1 behavior:
- read proposed drivers from the main finding and optionally linked assumption/evidence artifacts
- write one row per (artifact_path, proposed_driver_slug)
- mark removed proposals for an artifact path as inactive
- remain suitable for non-fatal use in the completion path
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from validate_research_artifact_linkages import (  # type: ignore
    DRIVER_ROOT,
    WORKSPACE_ROOT,
    listify,
    load_catalog,
    parse_frontmatter,
    resolve_value,
    sibling_artifact_paths,
    slugify,
)

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"

LOOKUP_SQL = r'''
SELECT json_build_object(
  'research_run_id', rr.id,
  'case_id', rr.case_id,
  'case_key', c.case_key,
  'market_id', c.market_id,
  'dispatch_id', COALESCE(rr.notes->>'dispatch_id', ''),
  'persona', rr.agent_label,
  'workspace_note_path', rr.workspace_note_path,
  'difficulty_class', COALESCE(c.orchestration_notes->'difficulty_profile'->>'difficulty_class', ''),
  'source_of_truth_class', COALESCE(c.orchestration_notes->'difficulty_profile'->>'source_of_truth_class', '')
)::text
FROM research_runs rr
JOIN cases c ON c.id = rr.case_id
WHERE rr.id = NULLIF(:'research_run_id', '')::uuid
LIMIT 1;
'''

UPSERT_SQL = r'''
INSERT INTO public.proposed_driver_occurrences (
  case_id,
  case_key,
  market_id,
  dispatch_id,
  research_run_id,
  persona,
  artifact_kind,
  artifact_path,
  proposed_driver_label,
  proposed_driver_slug,
  canonical_driver_suggestions,
  related_entities,
  related_canonical_drivers,
  difficulty_class,
  source_of_truth_class,
  status,
  occurred_at,
  updated_at
)
VALUES (
  NULLIF(:'case_id', '')::uuid,
  :'case_key',
  NULLIF(:'market_id', '')::uuid,
  NULLIF(:'dispatch_id', ''),
  NULLIF(:'research_run_id', '')::uuid,
  NULLIF(:'persona', ''),
  :'artifact_kind',
  :'artifact_path',
  :'proposed_driver_label',
  :'proposed_driver_slug',
  COALESCE(:'canonical_driver_suggestions', '[]')::jsonb,
  COALESCE(:'related_entities', '[]')::jsonb,
  COALESCE(:'related_canonical_drivers', '[]')::jsonb,
  NULLIF(:'difficulty_class', ''),
  NULLIF(:'source_of_truth_class', ''),
  'active',
  NOW(),
  NOW()
)
ON CONFLICT (artifact_path, proposed_driver_slug)
DO UPDATE SET
  case_id = EXCLUDED.case_id,
  case_key = EXCLUDED.case_key,
  market_id = EXCLUDED.market_id,
  dispatch_id = EXCLUDED.dispatch_id,
  research_run_id = EXCLUDED.research_run_id,
  persona = EXCLUDED.persona,
  artifact_kind = EXCLUDED.artifact_kind,
  proposed_driver_label = EXCLUDED.proposed_driver_label,
  canonical_driver_suggestions = EXCLUDED.canonical_driver_suggestions,
  related_entities = EXCLUDED.related_entities,
  related_canonical_drivers = EXCLUDED.related_canonical_drivers,
  difficulty_class = EXCLUDED.difficulty_class,
  source_of_truth_class = EXCLUDED.source_of_truth_class,
  status = 'active',
  updated_at = NOW();
'''

DEACTIVATE_SQL = r'''
WITH keep AS (
  SELECT value::text AS proposed_driver_slug
  FROM jsonb_array_elements_text(COALESCE(:'active_slugs', '[]')::jsonb)
)
UPDATE public.proposed_driver_occurrences pdo
SET status = 'inactive',
    updated_at = NOW()
WHERE pdo.artifact_path = :'artifact_path'
  AND pdo.status = 'active'
  AND NOT EXISTS (
    SELECT 1
    FROM keep k
    WHERE k.proposed_driver_slug = pdo.proposed_driver_slug
  );
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Upsert proposed-driver occurrence rows from research artifacts")
    parser.add_argument("--research-run-id", required=True, help="Research run id whose artifacts should be stored")
    parser.add_argument("--artifact-path", action="append", help="Artifact path relative to workspace or absolute; defaults to workspace_note_path")
    parser.add_argument("--include-linked-artifacts", action="store_true", help="Also include sibling assumption/evidence artifacts for the same persona")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""), help="Postgres connection URL")
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL), help="Path to psql binary")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser.parse_args()


def exec_sql(psql_bin: str, db_url: str, sql: str, variables: dict[str, str]) -> dict[str, Any] | None:
    if not db_url:
        raise ValueError("--db-url or PREDQUANT_ORCHESTRATOR_URL is required")
    cmd = [psql_bin, db_url, '-X', '-qAt', '-v', 'ON_ERROR_STOP=1']
    for key, value in variables.items():
        cmd.extend(['-v', f'{key}={value}'])
    cmd.extend(['-f', '-'])
    proc = subprocess.run(cmd, input=sql, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'psql failed')
    stdout = proc.stdout.strip()
    if not stdout:
        return None
    try:
        return json.loads(stdout.splitlines()[-1])
    except json.JSONDecodeError:
        return None


def resolve_artifact_paths(raw_paths: list[str] | None, default_path: str | None, include_linked: bool) -> list[Path]:
    seed_paths = list(raw_paths or [])
    if not seed_paths and default_path:
        seed_paths = [default_path]
    seen: set[Path] = set()
    out: list[Path] = []
    for raw in seed_paths:
        path = Path(raw)
        if not path.is_absolute():
            path = (WORKSPACE_ROOT / raw).resolve()
        candidates = [path]
        if include_linked:
            candidates.extend(sibling_artifact_paths(path))
        for candidate in candidates:
            resolved = candidate.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            out.append(resolved)
    return out


def classify_artifact(path: Path) -> tuple[str, str | None]:
    try:
        rel = path.relative_to(WORKSPACE_ROOT)
    except ValueError:
        rel = path
    parts = rel.parts
    if 'personas' in parts:
        return 'persona', path.stem
    if 'assumptions' in parts:
        return 'assumption', path.stem
    if 'evidence' in parts:
        return 'evidence', path.stem
    return 'unknown', path.stem


def json_compact(value: Any) -> str:
    return json.dumps(value, separators=(',', ':'), ensure_ascii=False)


def main() -> int:
    args = parse_args()
    try:
        lookup = exec_sql(args.psql, args.db_url, LOOKUP_SQL, {'research_run_id': args.research_run_id})
        if not lookup:
            raise ValueError('research run lookup returned no result')

        artifact_paths = resolve_artifact_paths(args.artifact_path, lookup.get('workspace_note_path'), args.include_linked_artifacts)
        driver_aliases, driver_slugs = load_catalog(DRIVER_ROOT, kind='driver')

        upserted = 0
        deactivated = 0
        active_summary: list[dict[str, Any]] = []

        for path in artifact_paths:
            if not path.exists():
                continue
            rel_path = str(path.relative_to(WORKSPACE_ROOT)) if path.is_relative_to(WORKSPACE_ROOT) else str(path)
            text = path.read_text()
            frontmatter, _ = parse_frontmatter(text)
            if frontmatter is None:
                continue
            proposed_drivers = listify(frontmatter.get('proposed_drivers'))
            related_entities = listify(frontmatter.get('related_entities'))
            related_drivers = listify(frontmatter.get('related_drivers'))
            artifact_kind, persona = classify_artifact(path)
            active_slugs: list[str] = []

            for label in proposed_drivers:
                slug = slugify(label)
                if not slug:
                    continue
                _, suggestions = resolve_value(label, driver_aliases, driver_slugs)
                exec_sql(
                    args.psql,
                    args.db_url,
                    UPSERT_SQL,
                    {
                        'case_id': lookup.get('case_id') or '',
                        'case_key': lookup.get('case_key') or '',
                        'market_id': lookup.get('market_id') or '',
                        'dispatch_id': lookup.get('dispatch_id') or '',
                        'research_run_id': lookup.get('research_run_id') or '',
                        'persona': persona or lookup.get('persona') or '',
                        'artifact_kind': artifact_kind,
                        'artifact_path': rel_path,
                        'proposed_driver_label': label,
                        'proposed_driver_slug': slug,
                        'canonical_driver_suggestions': json_compact(suggestions),
                        'related_entities': json_compact(related_entities),
                        'related_canonical_drivers': json_compact(related_drivers),
                        'difficulty_class': lookup.get('difficulty_class') or '',
                        'source_of_truth_class': lookup.get('source_of_truth_class') or '',
                    },
                )
                upserted += 1
                active_slugs.append(slug)
                active_summary.append({
                    'artifact_path': rel_path,
                    'proposed_driver_label': label,
                    'proposed_driver_slug': slug,
                    'persona': persona or lookup.get('persona'),
                    'artifact_kind': artifact_kind,
                    'canonical_driver_suggestions': suggestions,
                })

            exec_sql(
                args.psql,
                args.db_url,
                DEACTIVATE_SQL,
                {
                    'artifact_path': rel_path,
                    'active_slugs': json_compact(active_slugs),
                },
            )

        result = {
            'status': 'ok',
            'research_run_id': lookup.get('research_run_id'),
            'artifact_count': len(artifact_paths),
            'upserted_occurrence_count': upserted,
            'active_occurrences': active_summary,
        }
    except Exception as exc:  # noqa: BLE001
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1

    if args.pretty:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(json.dumps(result, separators=(',', ':'), default=str))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
