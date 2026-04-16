from __future__ import annotations

from typing import Any

DEFAULT_SIGNIFICANCE_PROFILE = {
    'min_active_nodes': 4,
    'min_candidate_edges': 2,
    'min_contested_edges': 1,
    'min_non_intervention_active_nodes': 2,
    'min_non_intervention_candidate_edges': 1,
    'min_non_intervention_required_checks': 2,
}

STRONG_NON_INTERVENTION_CHANNELS = {
    'review_text',
    'signal_packet',
    'frontmatter',
    'existing_edge_evidence',
}


def significance_profile(overrides: dict[str, Any] | None = None) -> dict[str, int]:
    profile = {key: int(value) for key, value in DEFAULT_SIGNIFICANCE_PROFILE.items()}
    for key, value in (overrides or {}).items():
        if key not in profile:
            continue
        try:
            profile[key] = max(0, int(value))
        except Exception:
            continue
    return profile



def _detail_rows(projection: dict[str, Any], key: str) -> list[dict[str, Any]]:
    rows = ((projection.get('projection_metadata') or {}).get(key) or [])
    if isinstance(rows, list):
        return [row for row in rows if isinstance(row, dict)]
    return []



def _required_checks(projection: dict[str, Any]) -> list[dict[str, Any]]:
    rows = projection.get('required_checks') or []
    if isinstance(rows, list):
        return [row for row in rows if isinstance(row, dict)]
    return []



def projection_metrics(projection: dict[str, Any]) -> dict[str, int]:
    active_node_details = _detail_rows(projection, 'active_node_details')
    candidate_edge_details = _detail_rows(projection, 'candidate_edge_details')
    contested_edge_details = _detail_rows(projection, 'contested_edge_details')
    required_checks = _required_checks(projection)

    non_intervention_active_node_count = sum(
        1 for row in active_node_details if set(row.get('evidence_channels') or []) & STRONG_NON_INTERVENTION_CHANNELS
    )
    non_intervention_candidate_edge_count = sum(
        1 for row in candidate_edge_details if set(row.get('evidence_channels') or []) & STRONG_NON_INTERVENTION_CHANNELS
    )
    non_intervention_required_check_count = sum(
        1 for row in required_checks if set(row.get('evidence_channels') or []) & STRONG_NON_INTERVENTION_CHANNELS
    )
    active_intervention_required_check_count = sum(
        1 for row in required_checks if 'linked_intervention_active' in set(row.get('evidence_channels') or [])
    )
    draft_intervention_required_check_count = sum(
        1 for row in required_checks if 'linked_intervention_draft' in set(row.get('evidence_channels') or [])
    )
    heuristic_required_check_count = sum(
        1 for row in required_checks if 'heuristic' in set(row.get('evidence_channels') or [])
    )

    return {
        'active_node_count': len(projection.get('active_nodes') or []),
        'candidate_edge_count': len(projection.get('candidate_edges') or []),
        'contested_edge_count': len(projection.get('contested_edges') or []),
        'required_check_count': len(required_checks),
        'non_intervention_active_node_count': non_intervention_active_node_count,
        'non_intervention_candidate_edge_count': non_intervention_candidate_edge_count,
        'non_intervention_required_check_count': non_intervention_required_check_count,
        'active_intervention_required_check_count': active_intervention_required_check_count,
        'draft_intervention_required_check_count': draft_intervention_required_check_count,
        'heuristic_required_check_count': heuristic_required_check_count,
    }



def projection_significance(projection: dict[str, Any], *, profile: dict[str, Any] | None = None) -> dict[str, Any]:
    cfg = significance_profile(profile)
    metrics = projection_metrics(projection)

    hits: list[str] = []
    if (
        metrics['active_node_count'] >= cfg['min_active_nodes']
        and metrics['candidate_edge_count'] >= cfg['min_candidate_edges']
        and metrics['non_intervention_active_node_count'] >= cfg['min_non_intervention_active_nodes']
    ):
        hits.append('active_nodes_and_candidate_edges')
    if (
        metrics['contested_edge_count'] >= cfg['min_contested_edges']
        and metrics['non_intervention_active_node_count'] >= 1
    ):
        hits.append('contested_edges')
    if (
        metrics['non_intervention_active_node_count'] >= cfg['min_non_intervention_active_nodes']
        and metrics['non_intervention_candidate_edge_count'] >= cfg['min_non_intervention_candidate_edges']
    ):
        hits.append('non_intervention_structural_evidence')

    return {
        'significant': bool(hits),
        'profile': cfg,
        'metrics': metrics,
        'reasons': hits,
        'weak_support_reasons': [
            reason
            for reason, present in [
                (
                    'non_intervention_required_checks',
                    metrics['non_intervention_required_check_count'] >= cfg['min_non_intervention_required_checks']
                    and metrics['non_intervention_active_node_count'] >= 1,
                ),
            ]
            if present and reason not in hits
        ],
    }



def assign_projection_significance(projection: dict[str, Any], *, profile: dict[str, Any] | None = None) -> dict[str, Any]:
    significance = projection_significance(projection, profile=profile)
    metadata = projection.get('projection_metadata')
    if not isinstance(metadata, dict):
        metadata = {}
        projection['projection_metadata'] = metadata
    metadata['projection_significance'] = significance
    return significance
