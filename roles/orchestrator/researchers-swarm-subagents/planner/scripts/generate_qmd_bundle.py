#!/usr/bin/env python3
from __future__ import annotations

"""Generate a lightweight QMD retrieval bundle for a research dispatch.

Q2 retrieval policy:
- planner-side gate decides whether to use QMD
- same-case retrieval always suppressed
- same-market retrieval suppressed on reruns/history
- canonical entity/driver notes are preferred first
- prior-case analogs are higher-bar, artifact-gated, and small
- output is a compact JSON bundle suitable for prompt injection and provenance
"""

import argparse
import json
import os
import re
import subprocess
from functools import lru_cache
from pathlib import Path
from typing import Any

DEFAULT_PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
SCRIPT_PATH = Path(__file__).resolve()
WORKSPACE_ROOT = SCRIPT_PATH.parents[5]
ENTITY_ROOT = WORKSPACE_ROOT / "qualitative-db" / "20-entities"
DRIVER_ROOT = WORKSPACE_ROOT / "qualitative-db" / "30-drivers"

STOPWORDS = {
    'the', 'a', 'an', 'and', 'or', 'of', 'to', 'in', 'on', 'for', 'by', 'at', 'with', 'will', 'be', 'is', 'are',
    'was', 'were', 'has', 'have', 'if', 'not', 'yes', 'no', 'from', 'into', 'only', 'however', 'also', 'again',
    'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'day',
    'week', 'month', 'year', 'end', 'reach', 'hit', 'between', 'above', 'below', 'this', 'that', 'according',
    'market', 'resolve', 'resolves', 'resolved', 'resolution', 'source', 'sources', 'specified', 'title', 'price',
    'prices', 'higher', 'lower', 'otherwise', 'currently', 'available', 'selected', 'please', 'note', 'about',
    'other', 'exchanges', 'trading', 'pairs', 'precision', 'determined', 'number', 'decimal', 'places', 'timezone',
    'date', 'minute', 'candle', 'candles', 'close', 'final', 'value', 'official', 'general', 'reported', 'primary',
    'information', 'effect', 'used', 'using', 'case', 'cases',
}

SOURCE_SURFACE_TOKENS = {
    'binance', 'coinbase', 'cme', 'polymarket', 'kalshi', 'metaculus', 'fivethirtyeight', 'draftkings', 'fanduel',
}

COMPARATOR_TOKENS = {'above', 'below', 'over', 'under'}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a lightweight QMD retrieval bundle")
    parser.add_argument("--case-key", required=True)
    parser.add_argument("--market-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", default="")
    parser.add_argument("--category", default="")
    parser.add_argument("--platform", default="")
    parser.add_argument("--run-kind", default="novel")
    parser.add_argument("--rerun-scope", default="")
    parser.add_argument("--prior-dispatch-count", type=int, default=0)
    parser.add_argument("--prior-case-count", type=int, default=0)
    parser.add_argument("--difficulty-class", default="")
    parser.add_argument("--source-of-truth-class", default="")
    parser.add_argument("--focus-hints-json", default="[]")
    parser.add_argument("--db-url", default=os.getenv("PREDQUANT_ORCHESTRATOR_URL", ""))
    parser.add_argument("--psql", default=os.getenv("PSQL_BIN", DEFAULT_PSQL))
    parser.add_argument("--out", help="Optional output path for bundle json")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def slugify(value: str) -> str:
    text = (value or "").strip().lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[\s_/]+", "-", text)
    text = re.sub(r"[^a-z0-9.-]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-.")
    return text


def parse_frontmatter(text: str) -> tuple[dict[str, Any], int] | tuple[None, None]:
    if not text.startswith("---\n"):
        return None, None
    lines = text.splitlines(keepends=True)
    if not lines or lines[0] != "---\n":
        return None, None
    data: dict[str, Any] = {}
    i = 1
    while i < len(lines):
        raw = lines[i].rstrip("\n")
        if raw == "---":
            return data, sum(len(line) for line in lines[: i + 1])
        if not raw.strip():
            i += 1
            continue
        match = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", raw)
        if not match:
            i += 1
            continue
        key, remainder = match.group(1), match.group(2)
        if remainder.startswith("[") and remainder.endswith("]"):
            inner = remainder[1:-1].strip()
            data[key] = [part.strip().strip('"').strip("'") for part in inner.split(",") if part.strip()]
        else:
            data[key] = remainder.strip().strip('"').strip("'")
        i += 1
    return None, None


@lru_cache(maxsize=8)
def load_catalog(root: Path, kind: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    if not root.exists():
        return items
    for path in sorted(root.rglob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text()
        fm, body_start = parse_frontmatter(text)
        body = text[body_start:] if body_start else text
        slug = slugify(path.stem)
        aliases = [slug]
        if fm:
            for alias in fm.get("aliases", []) if isinstance(fm.get("aliases"), list) else []:
                aliases.append(slugify(str(alias)))
            main = fm.get(kind)
            if isinstance(main, str) and main.strip():
                aliases.append(slugify(main))
        title_line = next((ln.strip('# ').strip() for ln in body.splitlines() if ln.startswith('# ')), path.stem)
        summary = ""
        for ln in body.splitlines():
            stripped = ln.strip()
            if stripped and not stripped.startswith('#') and not stripped.startswith('- ') and not stripped.startswith('---'):
                summary = stripped
                break
        items.append({
            'slug': slug,
            'path': str(path.relative_to(WORKSPACE_ROOT)),
            'aliases': sorted(set(a for a in aliases if a)),
            'title': title_line,
            'summary': summary[:240],
        })
    return items


def clean_search_text(text: str) -> str:
    cleaned = re.sub(r"https?://\S+", " ", text or "")
    cleaned = re.sub(r"\bwww\.\S+", " ", cleaned)
    cleaned = cleaned.replace("BTC/USDT", "BTC USDT")
    cleaned = re.sub(r"[_/]+", " ", cleaned)
    return cleaned


def normalize_tokens(text: str) -> set[str]:
    raw = re.findall(r"[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*", clean_search_text(text).lower())
    return {tok for tok in raw if tok not in STOPWORDS and len(tok) >= 3}


def extract_numeric_tokens(text: str) -> set[str]:
    return set(re.findall(r"\b\d+(?:\.\d+)?\b", clean_search_text(text or "")))


def extract_comparator_tokens(text: str) -> set[str]:
    return {tok for tok in re.findall(r"\b[a-z]+\b", clean_search_text(text).lower()) if tok in COMPARATOR_TOKENS}


def extract_surface_tokens(text: str) -> set[str]:
    return normalize_tokens(text) & SOURCE_SURFACE_TOKENS


def alias_matches(alias: str, normalized_text: str, tokens: set[str]) -> bool:
    alias_slug = slugify(alias)
    if not alias_slug:
        return False
    alias_tokens = [part for part in alias_slug.split('-') if part]
    if len(alias_tokens) <= 1:
        return alias_slug in tokens
    return alias_slug in normalized_text


def best_alias_match(*, aliases: list[str], title: str, description: str, focus_text: str = "") -> tuple[str | None, float, str | None]:
    title_clean = clean_search_text(title)
    desc_clean = clean_search_text(description)
    focus_clean = clean_search_text(focus_text)
    title_norm = slugify(title_clean)
    desc_norm = slugify(desc_clean)
    focus_norm = slugify(focus_clean)
    title_tokens = normalize_tokens(title_clean)
    desc_tokens = normalize_tokens(desc_clean)
    focus_tokens = normalize_tokens(focus_clean)

    best_alias = None
    best_score = 0.0
    best_reason = None
    for alias in aliases:
        alias_slug = slugify(alias)
        alias_token_count = max(1, len([part for part in alias_slug.split('-') if part]))
        if focus_text and alias_matches(alias, focus_norm, focus_tokens):
            score = 7.0 + alias_token_count
            reason = "matched retrieval focus hint"
        elif alias_matches(alias, title_norm, title_tokens):
            score = 5.0 + alias_token_count
            reason = "matched market title"
        elif alias_matches(alias, desc_norm, desc_tokens):
            score = 2.5 + alias_token_count
            reason = "matched market description"
        else:
            continue
        if score > best_score:
            best_alias = alias_slug
            best_score = score
            best_reason = reason
    return best_alias, best_score, best_reason


def qmd_tier(run_kind: str, difficulty_class: str, source_of_truth_class: str) -> tuple[str, bool]:
    difficulty = (difficulty_class or '').lower()
    source_truth = (source_of_truth_class or '').lower()
    if run_kind == 'rerun':
        return 'tier1', True
    if difficulty in {'hard', 'high'}:
        return 'tier2', True
    if difficulty in {'easy', 'low'} and 'authoritative' in source_truth:
        return 'tier0', False
    return 'tier1', True


def match_entities(title: str, description: str, max_results: int = 2) -> list[dict[str, Any]]:
    ranked: list[tuple[float, dict[str, Any]]] = []
    for item in load_catalog(ENTITY_ROOT, 'entity'):
        matched_alias, score, reason = best_alias_match(
            aliases=item['aliases'],
            title=title,
            description=description,
        )
        if not matched_alias:
            continue
        ranked.append((score, {
            'type': 'entity',
            'slug': item['slug'],
            'path': item['path'],
            'artifact_exists': True,
            'retrieval_score': round(score, 2),
            'retrieval_role': 'canonical_context',
            'why_retrieved': f"{reason} via entity alias `{matched_alias}`",
            'summary': item['summary'] or item['title'],
        }))

    dedup: list[dict[str, Any]] = []
    seen = set()
    for _, item in sorted(ranked, key=lambda pair: (-pair[0], pair[1]['slug'])):
        if item['slug'] in seen:
            continue
        seen.add(item['slug'])
        dedup.append(item)
    return dedup[:max_results]


def select_driver_notes(title: str, description: str, focus_hints: list[str], source_of_truth_class: str, max_results: int = 2) -> list[dict[str, Any]]:
    notes: list[tuple[float, dict[str, Any]]] = []
    focus_text = ' '.join(x for x in focus_hints if isinstance(x, str))
    catalog = load_catalog(DRIVER_ROOT, 'driver')
    for item in catalog:
        matched_alias, score, reason = best_alias_match(
            aliases=item['aliases'],
            title=title,
            description=description,
            focus_text=f"{focus_text} {source_of_truth_class}",
        )
        if not matched_alias:
            continue
        notes.append((score, {
            'type': 'driver',
            'slug': item['slug'],
            'path': item['path'],
            'artifact_exists': True,
            'retrieval_score': round(score, 2),
            'retrieval_role': 'mechanism',
            'why_retrieved': f"{reason} via driver alias `{matched_alias}`",
            'summary': item['summary'] or item['title'],
        }))

    if not notes:
        source_text = slugify(f"{title} {description} {focus_text} {source_of_truth_class}")
        if any(token in source_text for token in ['resolution', 'settlement', 'rules', 'source-of-truth', 'authoritative', 'fallback', 'exchange-source']):
            for preferred in ['reliability', 'operational-risk']:
                item = next((x for x in catalog if x['slug'] == preferred), None)
                if item:
                    score = 4.0 if preferred == 'reliability' else 3.5
                    notes.append((score, {
                        'type': 'driver',
                        'slug': item['slug'],
                        'path': item['path'],
                        'artifact_exists': True,
                        'retrieval_score': round(score, 2),
                        'retrieval_role': 'mechanism',
                        'why_retrieved': 'source-of-truth / resolution mechanics suggest this canonical driver may be relevant',
                        'summary': item['summary'] or item['title'],
                    }))

    dedup: list[dict[str, Any]] = []
    seen = set()
    for _, item in sorted(notes, key=lambda pair: (-pair[0], pair[1]['slug'])):
        if item['slug'] in seen:
            continue
        seen.add(item['slug'])
        dedup.append(item)
    return dedup[:max_results]


def sql_literal(value: str) -> str:
    return "'" + (value or "").replace("'", "''") + "'"


def exec_sql(psql_bin: str, db_url: str, sql: str) -> Any:
    if not db_url:
        return []
    proc = subprocess.run([psql_bin, db_url, '-X', '-qAt', '-v', 'ON_ERROR_STOP=1', '-f', '-'], input=sql, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'psql failed')
    stdout = proc.stdout.strip()
    return json.loads(stdout.splitlines()[-1]) if stdout else []


def allow_similar_case_analogs(*, tier: str, run_kind: str) -> bool:
    return run_kind == 'rerun' or tier == 'tier2'


def retrieve_similar_cases(args: argparse.Namespace, max_results: int, *, min_score: float = 6.0) -> list[dict[str, Any]]:
    case_key_sql = sql_literal(args.case_key)
    market_id_sql = sql_literal(args.market_id)
    market_filter = 'TRUE' if args.run_kind != 'rerun' else f'm.id::text <> {market_id_sql}'
    sql = f"""
SELECT COALESCE(json_agg(row_to_json(x)), '[]'::json)::text
FROM (
  SELECT c.case_key, c.market_id, m.title, m.description, m.category, m.platform, m.status AS market_status
  FROM cases c
  JOIN markets m ON m.id = c.market_id
  WHERE c.case_key <> {case_key_sql}
    AND ({market_filter})
  ORDER BY c.opened_at DESC NULLS LAST
  LIMIT 80
) x;
"""
    rows = exec_sql(args.psql, args.db_url, sql) or []
    current_text = f"{args.title} {args.description}"
    current_tokens = normalize_tokens(current_text)
    current_numbers = extract_numeric_tokens(current_text)
    current_comparators = extract_comparator_tokens(current_text)
    current_surfaces = extract_surface_tokens(current_text)
    current_entities = {item['slug'] for item in match_entities(args.title, args.description, max_results=4)}
    ranked: list[tuple[float, dict[str, Any]]] = []

    for row in rows:
        case_dir = WORKSPACE_ROOT / 'qualitative-db' / '40-research' / 'cases' / row['case_key']
        current_md = case_dir / 'researcher-swarm-current.md'
        if not current_md.exists():
            continue

        candidate_text = f"{row.get('title') or ''} {row.get('description') or ''}"
        title_tokens = normalize_tokens(candidate_text)
        overlap = current_tokens & title_tokens
        candidate_surfaces = extract_surface_tokens(candidate_text)
        shared_surfaces = current_surfaces & candidate_surfaces if current_surfaces and candidate_surfaces else set()
        meaningful_overlap = {tok for tok in overlap if not tok.isdigit()}
        candidate_entities = {item['slug'] for item in match_entities(row.get('title') or '', row.get('description') or '', max_results=4)}
        shared_entities = current_entities & candidate_entities if current_entities and candidate_entities else set()
        if not shared_entities and not shared_surfaces:
            continue

        score = min(len(meaningful_overlap or overlap), 4) * 1.5
        reasons = [f"meaningful token overlap={len(meaningful_overlap)}"]
        if shared_entities:
            score += min(len(shared_entities), 2) * 3.0
            reasons.append("shared canonical entity context")

        candidate_numbers = extract_numeric_tokens(candidate_text)
        number_overlap = current_numbers & candidate_numbers
        if number_overlap:
            score += min(len(number_overlap), 2) * 1.25
            reasons.append("shared numeric threshold/date cues")

        if shared_surfaces:
            score += 3.0
            reasons.append("same source/resolution surface")

        candidate_comparators = extract_comparator_tokens(candidate_text)
        if current_comparators and candidate_comparators and current_comparators & candidate_comparators:
            score += 0.75
            reasons.append("same threshold direction")

        if (row.get('category') or '').lower() == (args.category or '').lower() and args.category:
            score += 2.0
            reasons.append("same category")
        if (row.get('platform') or '').lower() == (args.platform or '').lower() and args.platform:
            score += 1.5
            reasons.append("same platform")

        if score < min_score:
            continue

        summary = row.get('title') or row['case_key']

        ranked.append((score, {
            'type': 'case',
            'case_key': row['case_key'],
            'path': str(current_md.relative_to(WORKSPACE_ROOT)),
            'artifact_exists': True,
            'retrieval_score': round(score, 2),
            'retrieval_role': 'analog',
            'why_retrieved': f"high-bar analog ({'; '.join(reasons)}; score={score:.1f})",
            'summary': summary[:260],
        }))

    ranked.sort(key=lambda item: (-item[0], item[1]['case_key']))
    return [item for _, item in ranked[:max_results]]


def main() -> int:
    args = parse_args()
    focus_hints = json.loads(args.focus_hints_json or '[]')
    tier, use_qmd = qmd_tier(args.run_kind, args.difficulty_class, args.source_of_truth_class)
    suppress_same_case = True
    suppress_same_market = args.run_kind == 'rerun' or args.prior_dispatch_count > 0 or args.prior_case_count > 0

    bundle = {
        'status': 'ok',
        'qmd_used': use_qmd,
        'qmd_tier': tier,
        'query_profile': {
            'run_kind': args.run_kind,
            'rerun_scope': args.rerun_scope or None,
            'prior_dispatch_count': args.prior_dispatch_count,
            'prior_case_count': args.prior_case_count,
            'difficulty_class': args.difficulty_class or None,
            'source_of_truth_class': args.source_of_truth_class or None,
            'suppress_same_case': suppress_same_case,
            'suppress_same_market': suppress_same_market,
        },
        'retrieval_policy': {
            'artifact_existence_gating': True,
            'canon_first': True,
            'analog_second': True,
            'similar_case_strategy': 'rerun_or_tier2_only',
        },
        'results': {
            'similar_cases': [],
            'entity_notes': [],
            'driver_notes': [],
        },
        'result_paths': [],
    }

    if use_qmd:
        entity_limit = 2
        driver_limit = 2
        case_limit = 0
        if allow_similar_case_analogs(tier=tier, run_kind=args.run_kind):
            case_limit = 2 if tier == 'tier1' else 3

        bundle['results']['entity_notes'] = match_entities(args.title, args.description, entity_limit)
        bundle['results']['driver_notes'] = select_driver_notes(args.title, args.description, focus_hints, args.source_of_truth_class, driver_limit)
        if case_limit > 0:
            bundle['results']['similar_cases'] = retrieve_similar_cases(args, case_limit)
        ordered_groups = [
            bundle['results']['entity_notes'],
            bundle['results']['driver_notes'],
            bundle['results']['similar_cases'],
        ]
        bundle['result_paths'] = [item['path'] for group in ordered_groups for item in group if item.get('artifact_exists')]

    if args.out:
        out = Path(args.out)
        if not out.is_absolute():
            out = (WORKSPACE_ROOT / args.out).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(bundle, indent=2, sort_keys=True))

    if args.pretty:
        print(json.dumps(bundle, indent=2, sort_keys=True))
    else:
        print(json.dumps(bundle, separators=(',', ':')))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
