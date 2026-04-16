from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
BULLET_KV_RE = re.compile(r"^-\s+([A-Za-z0-9_\-]+):\s+`?(.*?)`?\s*$")
TIMELINE_EVENT_RE = re.compile(r"^-\s+([0-9T:+\-\.Z]+)\s+—\s+(.*)$")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def write_json(path: Path, data: Any, pretty: bool = True) -> None:
    text = json.dumps(data, indent=2 if pretty else None, sort_keys=False)
    path.write_text(text + ("\n" if not text.endswith("\n") else ""), encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, Any]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    raw = match.group(1)
    data: dict[str, Any] = {}
    current_list_key: str | None = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and current_list_key:
            data.setdefault(current_list_key, []).append(line[4:].strip().strip('"').strip("'"))
            continue
        if re.match(r"^[A-Za-z0-9_\-]+:\s*$", line):
            key = line.split(":", 1)[0].strip()
            data[key] = []
            current_list_key = key
            continue
        current_list_key = None
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [item.strip().strip('"').strip("'") for item in inner.split(",") if item.strip()]
        else:
            data[key] = value.strip().strip('"').strip("'")
    return data


def strip_frontmatter(text: str) -> str:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return text
    return text[match.end():]


def extract_bullet_kv(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in text.splitlines():
        match = BULLET_KV_RE.match(line.strip())
        if not match:
            continue
        data[match.group(1)] = match.group(2)
    return data


def extract_timeline_events(text: str) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for line in text.splitlines():
        match = TIMELINE_EVENT_RE.match(line.strip())
        if not match:
            continue
        events.append({
            "ts": match.group(1),
            "summary": match.group(2),
        })
    return events


def split_markdown_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in strip_frontmatter(text).splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)
    return {key: "\n".join(lines).strip() for key, lines in sections.items()}


def extract_bullets(text: str) -> list[str]:
    items: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            items.append(stripped[2:].strip())
    return items


def iso_sort_key(value: str | None) -> str:
    return value or ""
