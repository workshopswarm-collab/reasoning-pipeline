---
type: system_guide
domain: causal_map
status: active
last_updated: 2026-04-15
owner: evaluator
tags: [causal-map/guide, qualitative-db/60-causal-map, recursive-improvement]
---

# 60-causal-map

This folder is the canonical **mechanism layer** above reviewed learnings.

Use it to store:
- causal nodes
- causal edges
- curated machine-readable mechanism structure
- compact graph metadata that later supports LMD retrieval and intervention policy

Do **not** use it as a giant prompt payload.
The graph exists to help the system select the right learnings and checks, not to dump raw ontology into runtime prompts.

Lifecycle policy:
- `qualitative-db/00-system/methodology/causal-lifecycle-policy.md`

## Current v1 scope

The initial seed ontology is intentionally narrow.
It currently centers on:
- threshold / touch mechanics
- source-of-truth / settlement mechanics
- workflow caution vs fair-value discount pressure
- publication / timing mechanics (seeded, still draft-light)

## Canonical layout

```text
qualitative-db/60-causal-map/
  README.md
  nodes/
    <node-key>.md
    <node-key>.json
  edges/
    <edge-key>.md
    <edge-key>.json
  candidates/
    README.md
  templates/
    causal-node-template.md
    causal-edge-template.md
  generated/
```

Markdown is the human-readable canonical layer.
JSON sidecars are optional but preferred when the node/edge needs structured contexts, lifecycle fields, linked interventions, or evidence rows for deterministic parsing.

## Canonical metadata expectations

Every live node or edge should eventually carry:
- `mechanism_family`
- `source_kind`
- `lifecycle_stage`
- optional supersession / merge metadata

Recommended family examples:
- `threshold_touch`
- `source_resolution`
- `workflow_pricing`
- `publication_timing`

Recommended source kinds:
- `seed`
- `manual`
- `proposal_auto`
- `merged`

Recommended live lifecycle stages:
- `draft`
- `trial`
- `active`
- `hold`
- `retired`
- `archived`

## Runtime / DB helpers

Evaluator-owned helpers live under `roles/evaluator/`:
- node registry: `roles/evaluator/runtime/scripts/upsert_causal_nodes.py`
- edge registry + edge evidence sync: `roles/evaluator/runtime/scripts/upsert_causal_edges.py`
- case projection: `roles/evaluator/runtime/scripts/project_case_to_causal_map.py`
- significance-gated projection backfill: `roles/evaluator/runtime/scripts/backfill_significant_causal_projections.py`
  - Phase 2 tightened significance so repeated required-check count alone is no longer enough; significant projections now need real structural evidence with non-intervention support channels
- candidate mining: `roles/evaluator/runtime/scripts/mine_causal_candidates.py`
- candidate aggregation: `roles/evaluator/runtime/scripts/aggregate_causal_candidate_proposals.py`
- case suggestion extraction: `roles/evaluator/runtime/scripts/extract_case_causal_suggestions.py`
- case suggestion canonicalization: `roles/evaluator/runtime/scripts/canonicalize_causal_suggestions.py`
- shadow match logging: `roles/evaluator/runtime/scripts/log_proposed_causal_shadow_matches.py`
- lifecycle baseline backfill: `roles/evaluator/runtime/scripts/backfill_causal_lifecycle_baseline.py`
- node utility/stat refresh: `roles/evaluator/runtime/scripts/update_causal_node_stats.py`
- edge utility/stat refresh: `roles/evaluator/runtime/scripts/update_causal_edge_stats.py`
- bounded live-graph lifecycle controller: `roles/evaluator/runtime/scripts/advance_live_causal_graph_items.py`
- periodic stat/health/repair/controller wrapper: `roles/evaluator/runtime/scripts/run_live_causal_graph_cycle.py`
- health scan slice: `roles/evaluator/runtime/scripts/scan_causal_graph_health.py`
- low-risk repair slice: `roles/evaluator/runtime/scripts/repair_causal_graph.py`
- SQL:
  - `roles/evaluator/sql/020_causal_nodes.sql`
  - `roles/evaluator/sql/021_causal_edges.sql`
  - `roles/evaluator/sql/022_causal_edge_evidence.sql`
  - `roles/evaluator/sql/023_case_causal_projections.sql`
  - `roles/evaluator/sql/024_proposed_causal_candidate_occurrences.sql`
  - `roles/evaluator/sql/025_proposed_causal_candidate_stats.sql`
  - `roles/evaluator/sql/028_causal_graph_lifecycle_columns.sql`
  - `roles/evaluator/sql/029_causal_node_stats.sql`
  - `roles/evaluator/sql/030_causal_graph_lifecycle_events.sql`
  - `roles/evaluator/sql/031_proposed_causal_shadow_matches.sql`
  - `roles/evaluator/sql/032_causal_graph_health_violations.sql`

## Hard rules

- Prefer a small reviewed ontology over a huge speculative one.
- Active edges should usually have at least one reviewed evidence path or an explicit rationale for why they are active.
- Draft edges are allowed when they are plausible but not yet sufficiently supported.
- Keep observed facts, projected case state, and reusable mechanism claims distinct.
- Later LMD retrieval should use the graph to shortlist; it should not inline the whole graph into prompts.
- Proposal-layer candidates are not live graph canon and should not be injected directly.
- Evaluator memory or freeform notes must not directly create LMD-recallable graph topology.
- Family assignment and lifecycle stage are mandatory anti-sprawl controls.
- Retirement, hold, and supersession should remove items from runtime recall without destroying their provenance.
