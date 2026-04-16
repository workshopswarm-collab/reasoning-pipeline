from __future__ import annotations

from pathlib import Path

LIB_PATH = Path(__file__).resolve()
RUNTIME_ROOT = LIB_PATH.parents[1]
ROLE_ROOT = LIB_PATH.parents[2]
ROLES_ROOT = LIB_PATH.parents[3]
ORCHESTRATOR_ROOT = LIB_PATH.parents[4]

QUALITATIVE_DB_ROOT = ORCHESTRATOR_ROOT / "qualitative-db"
QUANT_DB_ROOT = ORCHESTRATOR_ROOT / "quant-db"
CASES_ROOT = QUALITATIVE_DB_ROOT / "40-research" / "cases"
LEARNINGS_ROOT = QUALITATIVE_DB_ROOT / "50-learnings"
CASE_REVIEWS_ROOT = LEARNINGS_ROOT / "case-reviews"
INTERVENTIONS_ROOT = LEARNINGS_ROOT / "intervention-tracking"
CAUSAL_MAP_ROOT = QUALITATIVE_DB_ROOT / "60-causal-map"
CAUSAL_NODES_ROOT = CAUSAL_MAP_ROOT / "nodes"
CAUSAL_EDGES_ROOT = CAUSAL_MAP_ROOT / "edges"
LEARNING_TEMPLATE_PATH = QUALITATIVE_DB_ROOT / "00-system" / "templates" / "learning-note-template.md"


def case_dir(case_key: str) -> Path:
    return CASES_ROOT / case_key


def case_review_dir(case_key: str) -> Path:
    return CASE_REVIEWS_ROOT / case_key


def learning_packet_path(case_key: str) -> Path:
    return case_review_dir(case_key) / "learning-packet.json"


def signal_packet_path(case_key: str) -> Path:
    return case_review_dir(case_key) / "signal-packet.json"


def provenance_path(case_key: str) -> Path:
    return case_review_dir(case_key) / "provenance.json"


def case_review_markdown_path(case_key: str) -> Path:
    return case_review_dir(case_key) / "review.md"


def intervention_dir(status: str) -> Path:
    return INTERVENTIONS_ROOT / status


def intervention_sidecar_path(note_path: Path) -> Path:
    return note_path.with_suffix('.json')


def causal_node_sidecar_path(note_path: Path) -> Path:
    return note_path.with_suffix('.json')


def causal_edge_sidecar_path(note_path: Path) -> Path:
    return note_path.with_suffix('.json')


def case_causal_projection_path(case_key: str) -> Path:
    return case_review_dir(case_key) / "causal-projection.json"


def case_causal_suggestions_path(case_key: str) -> Path:
    return case_review_dir(case_key) / "causal-suggestions.json"


def case_canonical_causal_suggestions_path(case_key: str) -> Path:
    return case_review_dir(case_key) / "causal-suggestions-canonical.json"


def ensure_parent(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def to_repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ORCHESTRATOR_ROOT.resolve()))
    except Exception:
        return str(path)
