from __future__ import annotations

import json
import re
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DECISION_MAKER_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = DECISION_MAKER_DIR.parents[1]
TEMPLATES_DIR = WORKSPACE_ROOT / "qualitative-db" / "00-system" / "templates"
DECISION_PACKET_TEMPLATE_PATH = TEMPLATES_DIR / "decision-packet-template.md"
DECISION_PACKET_SCHEMA_PATH = TEMPLATES_DIR / "decision-packet.schema.json"
RESEARCH_CASES_ROOT = WORKSPACE_ROOT / "qualitative-db" / "40-research" / "cases"
CASE_SYNTHESIS_DIRNAME = "synthesizer-agent"
CASE_DECISION_DIRNAME = "decision-maker"
CASE_DECISION_PACKET_FILENAME = "decision-maker-packet.md"
CASE_DECISION_PACKET_JSON_RELATIVE = "artifacts/decision-maker-packet.json"
CASE_DECISION_STAGE_STATUS_JSON_RELATIVE = "artifacts/decision-stage-status.json"
CASE_LIGHT_REFRESH_BRIEF_JSON_RELATIVE = "artifacts/light-refresh-brief.json"
CASE_LIGHT_REFRESH_BRIEF_MARKDOWN_RELATIVE = "artifacts/light-refresh-brief.md"
DISPATCH_MANIFESTS_DIR = WORKSPACE_ROOT / "roles" / "orchestrator" / "researchers-swarm-subagents" / "runtime" / "dispatch-manifests"

DECISION_PACKET_FRONTMATTER_ORDER = [
    "type",
    "case_key",
    "dispatch_id",
    "question",
    "market_id",
    "external_market_id",
    "market_slug",
    "platform",
    "market_title",
    "source_decision_handoff_path",
    "source_syndicated_finding_path",
    "source_light_refresh_brief_path",
    "refresh_mode",
    "recommended_side",
    "trade_authorization",
    "position_policy",
    "decision_readiness",
    "fair_value_low",
    "fair_value_high",
    "fair_value_mid",
    "market_reference_price",
    "edge_mid_vs_market_pct_points",
    "independent_verification_quality",
    "compressed_toward_market_applied",
    "decision_confidence",
    "valid_until",
    "tags",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def write_json(path: Path, data: Any, *, pretty: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if pretty:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    else:
        path.write_text(json.dumps(data, ensure_ascii=False) + "\n")


def relative_to_workspace(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(WORKSPACE_ROOT))
    except ValueError:
        return str(resolved)


def coerce_string(value: Any) -> str:
    return "" if value is None else str(value).strip()


def normalize_probability(value: Any) -> float | None:
    if value is None or value == "" or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        numeric = float(value)
    else:
        text = str(value).strip()
        if not text:
            return None
        if text.endswith("%"):
            try:
                numeric = float(text[:-1]) / 100.0
            except ValueError:
                return None
        else:
            try:
                numeric = float(text)
            except ValueError:
                return None
    if numeric < 0 or numeric > 1:
        return None
    return numeric


def round_probability(value: float | None) -> float | None:
    return None if value is None else round(value, 4)


def percent_points_from_prob_delta(delta: float | None) -> float | None:
    return None if delta is None else round(delta * 100.0, 1)


def decision_case_dir(case_key: str) -> Path:
    return RESEARCH_CASES_ROOT / case_key / CASE_DECISION_DIRNAME


def case_synthesis_dir(case_key: str) -> Path:
    return RESEARCH_CASES_ROOT / case_key / CASE_SYNTHESIS_DIRNAME


def case_decision_handoff_path(case_key: str) -> Path:
    return case_synthesis_dir(case_key) / "decision-handoff.md"


def case_syndicated_finding_path(case_key: str) -> Path:
    return case_synthesis_dir(case_key) / "syndicated-finding.md"


def case_syndicated_runtime_path(case_key: str) -> Path:
    return case_synthesis_dir(case_key) / "syndicated-finding.runtime.json"


def case_decision_packet_markdown_path(case_key: str) -> Path:
    return decision_case_dir(case_key) / CASE_DECISION_PACKET_FILENAME


def case_decision_packet_json_path(case_key: str) -> Path:
    return decision_case_dir(case_key) / CASE_DECISION_PACKET_JSON_RELATIVE


def case_decision_stage_status_path(case_key: str) -> Path:
    return decision_case_dir(case_key) / CASE_DECISION_STAGE_STATUS_JSON_RELATIVE


def case_light_refresh_brief_json_path(case_key: str) -> Path:
    return decision_case_dir(case_key) / CASE_LIGHT_REFRESH_BRIEF_JSON_RELATIVE


def case_light_refresh_brief_markdown_path(case_key: str) -> Path:
    return decision_case_dir(case_key) / CASE_LIGHT_REFRESH_BRIEF_MARKDOWN_RELATIVE


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json_if_exists(path: Path) -> Any:
    if not path.exists():
        return None
    return load_json(path)


def load_jsonish_scalar(value: str) -> Any:
    text = value.strip()
    if text == "":
        return ""
    if text.lower() == "true":
        return True
    if text.lower() == "false":
        return False
    if text.startswith("[") and text.endswith("]"):
        try:
            parsed = json.loads(text)
            if isinstance(parsed, list):
                return parsed
        except json.JSONDecodeError:
            pass
        inner = text[1:-1].strip()
        if not inner:
            return []
        return [part.strip().strip('"').strip("'") for part in inner.split(",") if part.strip()]
    if re.fullmatch(r"-?\d+", text):
        return int(text)
    if re.fullmatch(r"-?\d+\.\d+", text):
        return float(text)
    return text.strip().strip('"').strip("'")


def parse_frontmatter(text: str) -> tuple[OrderedDict[str, Any], str]:
    if not text.startswith("---\n"):
        return OrderedDict(), text
    lines = text.splitlines(keepends=True)
    if not lines or lines[0] != "---\n":
        return OrderedDict(), text
    data: OrderedDict[str, Any] = OrderedDict()
    i = 1
    while i < len(lines):
        raw = lines[i].rstrip("\n")
        if raw == "---":
            body = "".join(lines[i + 1 :])
            return data, body
        if not raw.strip():
            i += 1
            continue
        match = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", raw)
        if not match:
            i += 1
            continue
        key, remainder = match.group(1), match.group(2)
        data[key] = load_jsonish_scalar(remainder)
        i += 1
    return OrderedDict(), text


def dump_scalar(value: Any) -> str:
    if value is None or value == "":
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return json.dumps(value, ensure_ascii=False)
    text = str(value)
    if re.fullmatch(r"[A-Za-z0-9_./:+-]+", text):
        return text
    return json.dumps(text, ensure_ascii=False)


def dump_frontmatter(data: OrderedDict[str, Any], body: str) -> str:
    lines = ["---\n"]
    for key, value in data.items():
        rendered = dump_scalar(value)
        if rendered == "":
            lines.append(f"{key}:\n")
        else:
            lines.append(f"{key}: {rendered}\n")
    lines.append("---\n")
    if body and not body.startswith("\n"):
        lines.append("\n")
    lines.append(body)
    return "".join(lines)


def load_markdown_frontmatter(path: Path) -> tuple[OrderedDict[str, Any], str]:
    return parse_frontmatter(path.read_text())


def dispatch_manifest_path(dispatch_id: str) -> Path:
    return DISPATCH_MANIFESTS_DIR / f"{dispatch_id}.json"


def load_dispatch_manifest_market(dispatch_id: str) -> dict[str, Any]:
    if not dispatch_id:
        return {}
    path = dispatch_manifest_path(dispatch_id)
    if not path.exists():
        return {}
    try:
        payload = load_json(path)
    except Exception:
        return {}
    market = payload.get("market") if isinstance(payload, dict) else {}
    return dict(market) if isinstance(market, dict) else {}


def find_case_dir_for_dispatch(dispatch_id: str) -> Path | None:
    if not RESEARCH_CASES_ROOT.exists():
        return None
    for case_dir in RESEARCH_CASES_ROOT.iterdir():
        if not case_dir.is_dir():
            continue
        handoff = case_dir / CASE_SYNTHESIS_DIRNAME / "decision-handoff.md"
        if not handoff.exists():
            continue
        frontmatter, _ = load_markdown_frontmatter(handoff)
        if coerce_string(frontmatter.get("dispatch_id")) == dispatch_id:
            return case_dir
    return None


def find_synthesis_stage_status_path(case_key: str, dispatch_id: str) -> Path | None:
    case_dir = RESEARCH_CASES_ROOT / case_key
    if not case_dir.exists() or not dispatch_id:
        return None
    matches = sorted(case_dir.rglob(f"{dispatch_id}/synthesis-stage-status.json"))
    if matches:
        return matches[-1]
    fallback = sorted(case_dir.rglob("synthesis-stage-status.json"))
    for path in fallback:
        try:
            payload = load_json(path)
        except Exception:
            continue
        if coerce_string((payload or {}).get("dispatch_id")) == dispatch_id:
            return path
    return None


def telegram_topic_session_key(chat_id: Any, topic_id: Any) -> str:
    chat = coerce_string(chat_id)
    topic = coerce_string(topic_id)
    if not chat or not topic:
        return ""
    if chat.startswith("-"):
        return f"agent:main:telegram:group:{chat}:topic:{topic}"
    return f"agent:main:telegram:chat:{chat}:topic:{topic}"


def case_timeline_path_for(case_key: str) -> Path:
    return RESEARCH_CASES_ROOT / case_key / "timeline.md"


def ensure_case_timeline(path: Path, *, case_key: str) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        f"type: research_case_timeline\n"
        f"case_key: {case_key}\n"
        "generated_by: orchestrator\n"
        "---\n\n"
        "# Timeline\n\n"
    )


def append_case_timeline_entry(case_key: str, entry: str, *, unique_token: str | None = None) -> bool:
    path = case_timeline_path_for(case_key)
    ensure_case_timeline(path, case_key=case_key)
    text = path.read_text()
    token = unique_token or entry.strip()
    if token and token in text:
        return False
    path.write_text(text.rstrip() + "\n" + entry.rstrip() + "\n")
    return True
