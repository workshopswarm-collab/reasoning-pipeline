from __future__ import annotations

import hashlib
import json
import re
from collections import OrderedDict
from pathlib import Path
from typing import Any

SUBAGENT_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = SUBAGENT_DIR.parents[2]
TEMPLATES_DIR = WORKSPACE_ROOT / "qualitative-db" / "00-system" / "templates"
SYNDICATED_TEMPLATE_PATH = TEMPLATES_DIR / "syndicated-finding-template.md"
SYNDICATED_RUNTIME_METADATA_TEMPLATE_PATH = TEMPLATES_DIR / "syndicated-finding-runtime-metadata-template.json"
RESEARCH_CASES_ROOT = WORKSPACE_ROOT / "qualitative-db" / "40-research" / "cases"
RESEARCHERS_SWARM_ROOT = WORKSPACE_ROOT / "roles" / "orchestrator" / "researchers-swarm-subagents"
DISPATCH_MANIFEST_ROOT = RESEARCHERS_SWARM_ROOT / "runtime" / "dispatch-manifests"
CASE_SYNTHESIS_DIRNAME = "synthesizer-agent"
CASE_DECISION_HANDOFF_FILENAME = "decision-handoff.md"
SYNTHESIS_SUBAGENT_LABEL_PREFIX = "synthesis-final"

DECISION_HEADER_ORDER = [
    "type",
    "case_key",
    "dispatch_id",
    "question",
    "coverage_status",
    "market_implied_probability",
    "syndicated_probability_low",
    "syndicated_probability_high",
    "syndicated_probability_midpoint",
    "edge_vs_market_pct_points",
    "relation_to_market",
    "edge_quality",
    "edge_independent_verification_quality",
    "compressed_toward_market_due_to_verification",
    "contract_ambiguity_level",
    "contract_ambiguity_reason",
    "independently_verified_points",
    "verification_gap_summary",
    "best_countercase_summary",
    "main_reason_for_disagreement",
    "resolution_mechanics_summary",
    "freshness_sensitive",
    "freshness_driver",
    "decision_blockers",
    "blockers_require_new_research",
    "disagreement_type",
    "disagreement_intensity",
    "synthesis_confidence_quality",
    "staleness_risk",
    "next_checkpoint",
    "follow_up_needed",
]

SECTION_ORDER = [
    "Alpha summary",
    "Input coverage",
    "Market-implied baseline",
    "Syndicated probability estimate",
    "Difference from swarm-implied center",
    "Agreement or disagreement with market",
    "Independent verification of edge",
    "Compression toward market due to verification",
    "Timing and catalyst posture",
    "Decision blockers",
    "Implication for the question",
    "Consensus across personas",
    "Key disagreements across personas",
    "Best countercase",
    "Encapsulated assumptions",
    "Encapsulated evidence map",
    "Evidence weighting",
    "Counterpoints / strongest disconfirming evidence",
    "Resolution or source-of-truth interpretation",
    "Why this could create or destroy alpha",
    "What would falsify this interpretation / change the view",
    "Highest-value next research",
    "Source-quality assessment",
    "Verification impact",
    "Persona contribution map",
    "Reusable lesson signals",
    "Orchestrator review suggestions",
    "Recommended follow-up",
]

SYNTHESIZER_ENUMS = {
    "coverage_status": {"complete", "partial"},
    "edge_independent_verification_quality": {"low", "medium", "high"},
    "compressed_toward_market_due_to_verification": {"yes", "no"},
    "contract_ambiguity_level": {"none", "minor", "moderate", "major"},
    "freshness_sensitive": {"yes", "no"},
    "blockers_require_new_research": {"yes", "no"},
    "disagreement_type": {"facts", "contract", "timing", "interpretation", "market_pricing", "mixed"},
    "disagreement_intensity": {"low", "medium", "high"},
    "synthesis_confidence_quality": {"low", "medium", "high"},
    "staleness_risk": {"low", "medium", "high"},
    "follow_up_needed": {"yes", "no"},
}

RUNTIME_METADATA_FIELDS = [
    "artifact_type",
    "artifact_path",
    "case_key",
    "dispatch_id",
    "question",
    "generated_by",
    "synthesis_method",
    "synthesis_status",
    "market_snapshot_time",
    "source_personas",
    "missing_personas",
    "source_finding_paths",
    "source_supporting_artifacts",
    "source_persona_count",
    "missing_persona_count",
    "supporting_artifact_count",
    "upstream_inputs",
    "downstream_uses",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def write_json(path: Path, data: Any, *, pretty: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if pretty:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    else:
        path.write_text(json.dumps(data, ensure_ascii=False) + "\n")


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
    if text.startswith("{") and text.endswith("}"):
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return text.strip().strip('"').strip("'")
    if re.fullmatch(r"-?\d+", text):
        return int(text)
    if re.fullmatch(r"-?\d+\.\d+", text):
        return float(text)
    return text.strip().strip('"').strip("'")


def parse_frontmatter(text: str) -> tuple[OrderedDict[str, Any], int] | tuple[None, None]:
    if not text.startswith("---\n"):
        return None, None
    lines = text.splitlines(keepends=True)
    if not lines or lines[0] != "---\n":
        return None, None
    data: OrderedDict[str, Any] = OrderedDict()
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
        if remainder == "":
            block_items: list[str] = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j].rstrip("\n")
                if nxt == "---":
                    break
                if re.match(r"^\s{2,}-\s+", nxt):
                    block_items.append(re.sub(r"^\s{2,}-\s+", "", nxt))
                    j += 1
                    continue
                if nxt.strip() == "":
                    j += 1
                    continue
                if re.match(r"^[A-Za-z0-9_]+:\s*.*$", nxt):
                    break
                j += 1
            if block_items:
                data[key] = [load_jsonish_scalar(item) for item in block_items]
                i = j
                continue
            data[key] = ""
            i += 1
            continue
        data[key] = load_jsonish_scalar(remainder)
        i += 1
    return None, None


def dump_scalar(value: Any) -> str:
    if value is None or value == "":
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
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


def normalize_probability(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
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


def derive_syndicated_fields(*, market_implied_probability: Any, low: Any, high: Any) -> dict[str, Any]:
    market = normalize_probability(market_implied_probability)
    low_p = normalize_probability(low)
    high_p = normalize_probability(high)
    out: dict[str, Any] = {
        "market_implied_probability": round_probability(market),
        "syndicated_probability_low": round_probability(low_p),
        "syndicated_probability_high": round_probability(high_p),
        "syndicated_probability_midpoint": None,
        "edge_vs_market_pct_points": None,
        "relation_to_market": "unclear",
        "edge_quality": "unclear",
        "valid": False,
    }
    if market is None or low_p is None or high_p is None or low_p > high_p:
        return out
    midpoint = round((low_p + high_p) / 2.0, 4)
    edge = round((midpoint - market) * 100.0, 1)
    if low_p <= market <= high_p:
        relation = "crosses_market"
    elif abs(edge) < 3.0:
        relation = "roughly_agree"
    elif midpoint > market:
        relation = "above_market"
    elif midpoint < market:
        relation = "below_market"
    else:
        relation = "roughly_agree"
    if relation in {"crosses_market", "unclear"}:
        edge_quality = "unclear"
    elif abs(edge) < 3.0:
        edge_quality = "weak"
    elif abs(edge) < 7.0:
        edge_quality = "moderate"
    else:
        edge_quality = "strong"
    out.update(
        {
            "syndicated_probability_midpoint": midpoint,
            "edge_vs_market_pct_points": edge,
            "relation_to_market": relation,
            "edge_quality": edge_quality,
            "valid": True,
        }
    )
    return out


def runtime_json_path_for(markdown_path: Path) -> Path:
    return markdown_path.with_suffix(".runtime.json")


def relative_to_workspace(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(WORKSPACE_ROOT))
    except ValueError:
        return str(resolved)


def coerce_string(value: Any) -> str:
    return "" if value is None else str(value).strip()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_json(value: Any) -> str:
    return sha256_text(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")))


def extract_explicit_probability_from_persona(frontmatter: dict[str, Any], body: str) -> float | None:
    frontmatter_prob = normalize_probability(frontmatter.get("own_probability"))
    if frontmatter_prob is not None:
        return frontmatter_prob

    section_match = re.search(
        r"(?is)^##\s+Own probability estimate\s*(.+?)(?=^##\s+|\Z)",
        body,
        re.MULTILINE,
    )
    if section_match:
        search_text = section_match.group(1)
    else:
        phrase_match = re.search(
            r"(?is)(?:my estimate is|i estimate|my probability is|probability estimate:?|i put the probability at)\s+(.{0,120})",
            body,
        )
        if not phrase_match:
            return None
        search_text = phrase_match.group(1)

    percent_match = re.search(r"(?i)(\d+(?:\.\d+)?)\s*%\s*(?:yes|no)?", search_text)
    if percent_match:
        try:
            value = float(percent_match.group(1)) / 100.0
        except ValueError:
            value = None
        return normalize_probability(value)

    decimal_match = re.search(r"\b(0(?:\.\d+)?|1(?:\.0+)?)\b", search_text)
    if decimal_match:
        return normalize_probability(decimal_match.group(1))
    return None


def extract_first_nonempty_paragraph(body: str) -> str:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", body) if part.strip()]
    return paragraphs[0] if paragraphs else ""


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


def case_synthesis_dir_for(case_key: str) -> Path:
    return RESEARCH_CASES_ROOT / case_key / CASE_SYNTHESIS_DIRNAME


def case_synthesis_markdown_path_for(case_key: str) -> Path:
    return case_synthesis_dir_for(case_key) / "syndicated-finding.md"


def case_decision_handoff_path_for(case_key: str) -> Path:
    return case_synthesis_dir_for(case_key) / CASE_DECISION_HANDOFF_FILENAME


def synthesis_subagent_label(dispatch_id: str) -> str:
    return f"{SYNTHESIS_SUBAGENT_LABEL_PREFIX}:{dispatch_id}"


def telegram_topic_session_key(chat_id: Any, topic_id: Any) -> str:
    chat = coerce_string(chat_id)
    topic = coerce_string(topic_id)
    if not chat or not topic:
        return ""
    if chat.startswith("-"):
        return f"agent:main:telegram:group:{chat}:topic:{topic}"
    return f"agent:main:telegram:chat:{chat}:topic:{topic}"


