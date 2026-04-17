from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from .causal_candidates import default_threshold_profile, proposal_id
from .io import read_json
from .paths import to_repo_relative
from .proposed_causal_metadata import classify_intervention_dependency, normalize_cluster_key
from .proposed_driver_occurrence_compiler import PACKETS_ROOT, load_packet_rows, packet_json_path
from .provisional_family_autopolicy import PROVISIONAL_FAMILY_POLICIES_PATH
from .provisional_family_registry import PROVISIONAL_FAMILY_REGISTRY_JSON_PATH, label_for_slug, normalize_family_key, normalize_slug

BRIDGE_SOURCE = 'occurrence_packet_shadow_bridge'
PROPOSAL_SOURCE = 'driver_occurrence_compiler'
EVIDENCE_CHANNELS = ['signal_packet']



def load_provisional_family_registry_payload() -> dict[str, Any]:
    payload = read_json(PROVISIONAL_FAMILY_REGISTRY_JSON_PATH, default={}) or {}
    if not isinstance(payload, dict):
        return {}
    return payload



def load_generated_provisional_family_policies_payload() -> dict[str, Any]:
    payload = read_json(PROVISIONAL_FAMILY_POLICIES_PATH, default={}) or {}
    if not isinstance(payload, dict):
        return {}
    return payload



def load_enabled_generated_family_policies() -> dict[str, dict[str, Any]]:
    payload = load_generated_provisional_family_policies_payload()
    rows: dict[str, dict[str, Any]] = {}
    for row in payload.get('policies') or []:
        if not isinstance(row, dict):
            continue
        if not bool(row.get('enabled')):
            continue
        family_key = str(row.get('mechanism_family') or '').strip()
        if family_key:
            rows[family_key] = row
    return rows



def registry_family_index(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for row in payload.get('families') or []:
        if not isinstance(row, dict):
            continue
        family_key = str(row.get('family_key') or '').strip()
        if family_key:
            out[family_key] = row
    return out



def registry_member_index(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for row in payload.get('members') or []:
        if not isinstance(row, dict):
            continue
        candidate_slug = str(row.get('candidate_slug') or '').strip()
        if candidate_slug:
            out[candidate_slug] = row
    return out



def preferred_candidate_label(packet: dict[str, Any]) -> str:
    slug = normalize_slug(packet.get('candidate_slug'))
    label = str(packet.get('candidate_label') or '').strip()
    if not label:
        return label_for_slug(slug)
    normalized_label = normalize_slug(label)
    if normalized_label == slug:
        return label_for_slug(slug)
    return label



def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))



def derived_genericity_penalty(*, family_row: dict[str, Any], policy_row: dict[str, Any], case_occurrences: list[dict[str, Any]]) -> float:
    base = 0.22
    canonical_family = str(family_row.get('canonical_family') or 'unassigned')
    if canonical_family != 'unassigned':
        base -= 0.04
    if str(family_row.get('family_key') or '').startswith('prov:novel:'):
        base += 0.04
    evidence_mass = float(policy_row.get('evidence_mass') or family_row.get('source_occurrence_count') or 0)
    health_score = float(policy_row.get('health_score') or 0.0)
    distinct_cases = int(family_row.get('distinct_case_count') or 0)
    if evidence_mass >= 30:
        base -= 0.03
    if evidence_mass >= 80:
        base -= 0.03
    if distinct_cases >= 5:
        base -= 0.02
    if distinct_cases >= 10:
        base -= 0.02
    if health_score >= 0.65:
        base -= 0.03
    if len(case_occurrences) > 1:
        base -= 0.01
    return round(clamp(base, 0.08, 0.35), 4)



def case_occurrence_groups(packet: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in packet.get('source_occurrences') or []:
        if not isinstance(row, dict):
            continue
        case_key = str(row.get('case_key') or '').strip()
        if not case_key:
            continue
        grouped[case_key].append(row)
    return dict(grouped)



def build_context_snapshot(*, family_row: dict[str, Any], case_rows: list[dict[str, Any]]) -> dict[str, Any]:
    canonical_family = str(family_row.get('canonical_family') or 'unassigned')
    source_family_slug = normalize_slug(family_row.get('source_family_slug'))
    question_mechanics: list[str] = []
    if canonical_family and canonical_family != 'unassigned':
        question_mechanics.append(canonical_family)
    elif source_family_slug and source_family_slug != 'unassigned':
        question_mechanics.append(source_family_slug.replace('-', '_'))
    source_of_truth_class = sorted({str(row.get('source_of_truth_class') or '').strip() for row in case_rows if str(row.get('source_of_truth_class') or '').strip()})
    domains = sorted({str(item).strip() for item in [canonical_family if canonical_family != 'unassigned' else '', source_family_slug.replace('-', '_') if source_family_slug and source_family_slug != 'unassigned' else ''] if str(item).strip()})
    return {
        'platforms': [],
        'categories': [],
        'question_mechanics': question_mechanics,
        'source_of_truth_class': source_of_truth_class,
        'domains': domains,
    }



def build_trigger_snapshot(*, family_key: str, policy_row: dict[str, Any], case_key: str, case_rows: list[dict[str, Any]], packet: dict[str, Any]) -> dict[str, Any]:
    return {
        'active_nodes': [],
        'candidate_edges': [],
        'contested_edges': [],
        'required_checks': [],
        'source_sections': sorted({str(row.get('artifact_kind') or '').strip() for row in case_rows if str(row.get('artifact_kind') or '').strip()}) or ['occurrence_packet_shadow_bridge'],
        'source_occurrence_artifact_paths': sorted({str(row.get('artifact_path') or '').strip() for row in case_rows if str(row.get('artifact_path') or '').strip()}),
        'source_personas': sorted({str(row.get('persona') or '').strip() for row in case_rows if str(row.get('persona') or '').strip()}),
        'source_case_key': case_key,
        'packet_hash': str(packet.get('packet_hash') or ''),
        'packet_key': str(packet.get('packet_key') or ''),
        'provisional_family_key': family_key,
        'canonical_family': str((policy_row.get('policy_notes') or {}).get('canonical_family') or ''),
    }



def build_proposal_metadata(*, family_key: str, family_row: dict[str, Any], policy_row: dict[str, Any], packet: dict[str, Any], case_key: str, case_rows: list[dict[str, Any]], context_snapshot: dict[str, Any], packet_path: Path) -> dict[str, Any]:
    policy_notes = policy_row.get('policy_notes') or {}
    return {
        'bridge_source': BRIDGE_SOURCE,
        'source_list': [PROPOSAL_SOURCE],
        'description': f"Occurrence-backed shadow bridge for {preferred_candidate_label(packet)} under {family_key}",
        'canonical_status': str(family_row.get('family_state') or 'provisional'),
        'canonical_reason': str(family_row.get('bridge_status') or ''),
        'packet_key': str(packet.get('packet_key') or ''),
        'packet_hash': str(packet.get('packet_hash') or ''),
        'packet_path': to_repo_relative(packet_path),
        'candidate_note_path': str(packet.get('candidate_note_path') or ''),
        'compiler_version': str(packet.get('compiler_version') or ''),
        'provisional_family_key': family_key,
        'canonical_family': str(policy_notes.get('canonical_family') or family_row.get('canonical_family') or 'unassigned'),
        'lineage_parent_family_key': str(policy_notes.get('lineage_parent_family_key') or family_row.get('lineage_parent_family_key') or ''),
        'source_family_slug': str(family_row.get('source_family_slug') or ''),
        'family_policy_source': str(policy_row.get('policy_source') or ''),
        'family_shadow_enabled': bool(policy_row.get('enabled', False)),
        'family_shadow_budget': int(policy_row.get('max_shadow_candidates') or 0),
        'policy_health_score': float(policy_row.get('health_score') or 0.0),
        'policy_evidence_mass': float(policy_row.get('evidence_mass') or 0.0),
        'case_occurrence_count': len(case_rows),
        'source_occurrence_count': int((packet.get('source_summary') or {}).get('source_occurrence_count') or 0),
        'distinct_case_count': int((packet.get('source_summary') or {}).get('distinct_case_count') or 0),
        'distinct_persona_count': int((packet.get('source_summary') or {}).get('distinct_persona_count') or 0),
        'case_personas': sorted({str(row.get('persona') or '').strip() for row in case_rows if str(row.get('persona') or '').strip()}),
        'case_artifact_paths': sorted({str(row.get('artifact_path') or '').strip() for row in case_rows if str(row.get('artifact_path') or '').strip()}),
        'context_snapshot': context_snapshot,
    }



def build_occurrence_row(*, packet: dict[str, Any], family_row: dict[str, Any], policy_row: dict[str, Any], case_key: str, case_rows: list[dict[str, Any]]) -> dict[str, Any]:
    proposal_key = normalize_slug(packet.get('candidate_slug'))
    candidate_label = preferred_candidate_label(packet)
    packet_path = packet_json_path(proposal_key)
    context_snapshot = build_context_snapshot(family_row=family_row, case_rows=case_rows)
    trigger_snapshot = build_trigger_snapshot(
        family_key=str(family_row.get('family_key') or ''),
        policy_row=policy_row,
        case_key=case_key,
        case_rows=case_rows,
        packet=packet,
    )
    proposal_metadata = build_proposal_metadata(
        family_key=str(family_row.get('family_key') or ''),
        family_row=family_row,
        policy_row=policy_row,
        packet=packet,
        case_key=case_key,
        case_rows=case_rows,
        context_snapshot=context_snapshot,
        packet_path=packet_path,
    )
    source_labels = sorted({str(row.get('proposed_driver_label') or '').strip() for row in case_rows if str(row.get('proposed_driver_label') or '').strip()})
    evidence_excerpt = f"{candidate_label} observed in {case_key}; source labels: {', '.join(source_labels[:4])}"[:2000]
    family_key = str(family_row.get('family_key') or '')
    genericity_penalty = derived_genericity_penalty(family_row=family_row, policy_row=policy_row, case_occurrences=case_rows)
    return {
        'proposal_id': proposal_id('node', proposal_key),
        'proposal_key': proposal_key,
        'candidate_type': 'node',
        'candidate_label': candidate_label,
        'mechanism_family': family_key,
        'proposal_source': PROPOSAL_SOURCE,
        'case_key': case_key,
        'review_path': str((proposal_metadata.get('candidate_note_path') or '') or ((case_rows[0].get('artifact_path') if case_rows else '') or to_repo_relative(packet_path))),
        'projection_path': to_repo_relative(packet_path),
        'source_node_key': proposal_key,
        'target_node_key': '',
        'node_type': 'mechanism',
        'effect_sign': '',
        'support_direction': 'supports',
        'occurrence_reason': f'{BRIDGE_SOURCE}; family_key={family_key}; packet_hash={packet.get("packet_hash")}; case_occurrence_count={len(case_rows)}',
        'evidence_excerpt': evidence_excerpt,
        'genericity_penalty': genericity_penalty,
        'evidence_channels': list(EVIDENCE_CHANNELS),
        'intervention_dependency': classify_intervention_dependency(EVIDENCE_CHANNELS),
        'normalized_cluster_key': normalize_cluster_key(
            candidate_type='node',
            proposal_key=proposal_key,
            mechanism_family=family_key,
            candidate_label=candidate_label,
            source_node_key=proposal_key,
        ),
        'context_snapshot': context_snapshot,
        'trigger_snapshot': trigger_snapshot,
        'threshold_profile': default_threshold_profile('node'),
        'proposal_metadata': proposal_metadata,
    }



def build_shadow_bridge_rows(
    *,
    packets: list[dict[str, Any]] | None = None,
    registry_payload: dict[str, Any] | None = None,
    generated_policies_payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    packets = packets if packets is not None else load_packet_rows()
    registry_payload = registry_payload if registry_payload is not None else load_provisional_family_registry_payload()
    generated_policies_payload = generated_policies_payload if generated_policies_payload is not None else load_generated_provisional_family_policies_payload()
    enabled_policy_rows = {
        str(row.get('mechanism_family') or '').strip(): row
        for row in (generated_policies_payload.get('policies') or [])
        if isinstance(row, dict) and bool(row.get('enabled')) and str(row.get('mechanism_family') or '').strip()
    }
    family_rows = registry_family_index(registry_payload)
    member_rows = registry_member_index(registry_payload)
    packet_by_candidate_slug = {
        normalize_slug(packet.get('candidate_slug')): packet
        for packet in packets
        if normalize_slug(packet.get('candidate_slug'))
    }

    allowed_candidate_slugs_by_family: dict[str, set[str]] = {}
    for family_key, policy_row in enabled_policy_rows.items():
        candidate_rows: list[tuple[int, int, int, str]] = []
        for candidate_slug, member_row in member_rows.items():
            if str(member_row.get('family_key') or '').strip() != family_key:
                continue
            packet = packet_by_candidate_slug.get(candidate_slug)
            if not packet:
                continue
            source_summary = packet.get('source_summary') or {}
            candidate_rows.append(
                (
                    int(source_summary.get('source_occurrence_count') or 0),
                    int(source_summary.get('distinct_case_count') or 0),
                    int(source_summary.get('distinct_persona_count') or 0),
                    candidate_slug,
                )
            )
        candidate_rows.sort(key=lambda row: (-row[0], -row[1], -row[2], row[3]))
        max_shadow_candidates = max(0, int(policy_row.get('max_shadow_candidates') or 0))
        allowed_candidate_slugs_by_family[family_key] = {row[3] for row in candidate_rows[:max_shadow_candidates]}

    bridged_rows: list[dict[str, Any]] = []
    skipped_rows: list[dict[str, Any]] = []
    family_counts: dict[str, int] = defaultdict(int)

    for packet in packets:
        candidate_slug = normalize_slug(packet.get('candidate_slug'))
        member_row = member_rows.get(candidate_slug)
        if not member_row:
            skipped_rows.append({'candidate_slug': candidate_slug, 'reason': 'registry_member_missing'})
            continue
        family_key = str(member_row.get('family_key') or '').strip()
        if not family_key:
            skipped_rows.append({'candidate_slug': candidate_slug, 'reason': 'registry_family_key_missing'})
            continue
        policy_row = enabled_policy_rows.get(family_key)
        if not policy_row:
            skipped_rows.append({'candidate_slug': candidate_slug, 'family_key': family_key, 'reason': 'family_policy_not_enabled'})
            continue
        allowed_candidate_slugs = allowed_candidate_slugs_by_family.get(family_key, set())
        if candidate_slug not in allowed_candidate_slugs:
            skipped_rows.append({'candidate_slug': candidate_slug, 'family_key': family_key, 'reason': 'family_shadow_budget_exhausted'})
            continue
        family_row = family_rows.get(family_key) or {}
        case_groups = case_occurrence_groups(packet)
        if not case_groups:
            skipped_rows.append({'candidate_slug': candidate_slug, 'family_key': family_key, 'reason': 'source_case_occurrences_missing'})
            continue
        for case_key, case_rows in sorted(case_groups.items()):
            bridged_rows.append(build_occurrence_row(packet=packet, family_row=family_row, policy_row=policy_row, case_key=case_key, case_rows=case_rows))
            family_counts[family_key] += 1

    bridged_rows.sort(key=lambda row: (row['mechanism_family'], row['proposal_key'], row['case_key']))
    return {
        'type': 'occurrence_shadow_bridge_rows',
        'proposal_source': PROPOSAL_SOURCE,
        'bridge_source': BRIDGE_SOURCE,
        'row_count': len(bridged_rows),
        'enabled_family_count': len(enabled_policy_rows),
        'bridged_family_counts': dict(sorted(family_counts.items(), key=lambda item: (-item[1], item[0]))),
        'allowed_candidate_counts': {family_key: len(candidate_slugs) for family_key, candidate_slugs in sorted(allowed_candidate_slugs_by_family.items())},
        'rows': bridged_rows,
        'skipped': skipped_rows,
    }
