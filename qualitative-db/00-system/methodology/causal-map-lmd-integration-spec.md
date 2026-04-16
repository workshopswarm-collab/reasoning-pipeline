---
type: system_spec
domain: methodology
status: proposed
last_updated: 2026-04-15
owner: evaluator
tags: [methodology/spec, causal-map, lmd, retrieval, interventions]
---

# Causal Map + LMD Integration Design Spec

This document defines the target architecture for adding a causal-map layer on top of the qualitative database and using that layer to improve LMD (Learning Memory Distillate) retrieval, intervention application, and recursive-learning evaluation.

This is a **target implementation spec**.
It describes how the next mechanism-aware LMD layer should work; it does not claim that all described surfaces already exist today.

Related specs:
- `qualitative-db/00-system/methodology/recursive-learning-system-spec.md`

## Why this exists

The current recursive-learning system can already do the following:
- compile per-case learning packets
- write reviewed case reviews
- extract structured learning signals
- aggregate cross-case patterns
- persist evaluator indexes and signal occurrences
- propose importance-gated evaluator memory upgrades

What it still lacks is a strong mechanism layer between:
- qualitative case reviews and signals
- runtime learning retrieval
- intervention applicability
- impact-driven policy updates

Without that mechanism layer, LMD retrieval risks relying too much on:
- category matching
- tags
- text semantics
- broad recurring signal keys

A causal map addresses that gap by letting LMD retrieve based on **shared causal pathways**, not just topic similarity.

## Core thesis

The causal map should be used primarily as a **retrieval and policy layer**, not as a large prompt payload.

In practical terms:
- the qualitative DB remains the canonical human-readable evidence and lesson store
- the causal map becomes the canonical machine-readable mechanism store
- LMD uses the causal map to select the right reviewed cases, active interventions, and required checks for a new case

## Design principles

1. **Mechanism beats topic**
   - shared causal pathways should rank above raw topical similarity

2. **Structured similarity beats pure semantic similarity**
   - LMD may use semantics, but only after structured gating / shortlisting

3. **Observed facts and inferred causes must stay distinct**
   - the graph should distinguish active observed nodes from inferred edge claims and contested edges

4. **Causal retrieval should stay compact**
   - do not inject the whole graph into prompts
   - inject only a compact causal context, matched learnings, and required checks

5. **The graph must improve through outcomes, not free self-rewriting**
   - edge confidence, retrieval weight, and intervention status should be updated through logged exposure + resolved outcomes + shrinkage

## Non-goals

This layer should **not**:
- dump the whole causal graph into prompts
- let LMD freely rewrite graph structure from one case without review
- replace canonical case reviews with graph-only storage
- use semantics as the only retrieval criterion
- pretend causal certainty when the evidence is weak or contested

## Conceptual architecture

```text
40-research/ case provenance
        +
quant truth / resolutions / Brier
        +
50-learnings/ case reviews / signals / interventions
        +
60-causal-map/ nodes / edges / projections / graph stats
        ->
LMD bundle generation
        ->
runtime injection + exposure logging
        ->
outcome evaluation
        ->
weight / intervention updates
```

## Proposed canonical storage surfaces

## Proposed qualitative graph layer

Recommended new canonical folder:

```text
qualitative-db/60-causal-map/
  README.md
  nodes/
    <node-key>.md
  edges/
    <edge-key>.md
  templates/
    causal-node-template.md
    causal-edge-template.md
  generated/
    graph-index.json
    edge-stats.json
    node-stats.json
```

Rationale:
- `50-learnings/` remains the reviewed learning layer
- `60-causal-map/` becomes the normalized mechanism layer on top of those learnings

## Case-linked projections

Each reviewed case should eventually gain an optional causal projection artifact:

```text
qualitative-db/50-learnings/case-reviews/<case-key>/
  causal-projection.json
```

This is the case-level bridge from the reviewed note and signal packet into the mechanism graph.

## Proposed graph contracts

## Causal node contract

A node should represent a reusable state, event, mechanism, workflow condition, or intervention condition.

Suggested fields:

```json
{
  "artifact_type": "causal_node",
  "schema_version": "v1",
  "node_key": "price-near-threshold",
  "label": "Price near threshold",
  "node_type": "market_state",
  "status": "active",
  "description": "Market state where reference price is close enough to a threshold/touch boundary that path dynamics matter materially.",
  "tags": ["threshold", "touch", "path-risk"],
  "contexts": {
    "platforms": ["polymarket"],
    "categories": ["crypto"],
    "question_mechanics": ["threshold-touch"]
  },
  "linked_paths": {
    "drivers": ["qualitative-db/30-drivers/reliability.md"],
    "domains": [],
    "entities": []
  }
}
```

### Suggested node types
- `market_state`
- `external_event`
- `resolution_condition`
- `workflow_condition`
- `source_condition`
- `intervention_condition`
- `risk_state`

## Causal edge contract

An edge should represent a directional causal or quasi-causal claim.

Suggested fields:

```json
{
  "artifact_type": "causal_edge",
  "schema_version": "v1",
  "edge_key": "price-near-threshold__increases__touch-probability",
  "source_node_key": "price-near-threshold",
  "target_node_key": "touch-probability",
  "effect_sign": "increases",
  "status": "active",
  "confidence_mode": "reviewed",
  "confidence_prior": 0.65,
  "description": "When price is sufficiently close to the touch threshold and time remains, touch probability usually increases materially.",
  "contexts": {
    "question_mechanics": ["threshold-touch"],
    "time_horizon_labels": ["short", "medium"],
    "source_of_truth_class": ["authoritative_direct", "authoritative_with_fallback"]
  },
  "linked_intervention_keys": ["verify-primary-source-for-authoritative-with-fallback"],
  "evidence_paths": []
}
```

### Edge confidence should be separated into:
- prior / reviewed confidence
- empirical exposure count
- empirical uplift estimate
- contested / stale status

## Case causal projection contract

Each reviewed case may have a projection artifact like:

```json
{
  "artifact_type": "case_causal_projection",
  "schema_version": "v1",
  "case_key": "case-20260414-4e668883",
  "review_path": "qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md",
  "signal_packet_path": "qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/signal-packet.json",
  "active_nodes": [
    "price-near-threshold",
    "time-remaining-nontrivial",
    "settlement-source-specificity",
    "verification-caution"
  ],
  "candidate_edges": [
    "price-near-threshold__increases__touch-probability",
    "settlement-source-specificity__increases__resolution-risk",
    "verification-caution__decreases__fair-value"
  ],
  "contested_edges": [
    "verification-caution__decreases__fair-value"
  ],
  "required_checks": [
    "verify_primary_resolution_source",
    "separate_resolution_risk_from_path_probability"
  ],
  "projection_metadata": {
    "projected_by": "roles/evaluator/.../project_case_to_causal_map.py",
    "projection_version": "v1"
  }
}
```

## Proposed database surfaces

The graph should be queryable in Postgres even if markdown remains canonical for prose.

## Core graph tables

### `causal_nodes`
Suggested fields:
- `node_key TEXT PRIMARY KEY`
- `label TEXT NOT NULL`
- `node_type TEXT NOT NULL`
- `status TEXT NOT NULL`
- `contexts JSONB NOT NULL DEFAULT '{}'::jsonb`
- `tags JSONB NOT NULL DEFAULT '[]'::jsonb`
- `path TEXT UNIQUE`
- `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`
- `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`

### `causal_edges`
Suggested fields:
- `edge_key TEXT PRIMARY KEY`
- `source_node_key TEXT NOT NULL REFERENCES causal_nodes(node_key)`
- `target_node_key TEXT NOT NULL REFERENCES causal_nodes(node_key)`
- `effect_sign TEXT NOT NULL`
- `status TEXT NOT NULL`
- `confidence_mode TEXT NOT NULL`
- `confidence_prior NUMERIC`
- `contexts JSONB NOT NULL DEFAULT '{}'::jsonb`
- `path TEXT UNIQUE`
- `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`
- `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`

### `causal_edge_evidence`
Links edges to cases / reviews / signals / interventions.

Suggested fields:
- `id BIGSERIAL PRIMARY KEY`
- `edge_key TEXT NOT NULL REFERENCES causal_edges(edge_key)`
- `case_key TEXT`
- `review_path TEXT`
- `signal_kind TEXT`
- `signal_key TEXT`
- `evidence_path TEXT`
- `support_direction TEXT`
  - `supports|weakens|contests`
- `confidence NUMERIC`
- `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`

### `case_causal_projections`
Stores per-case projected active nodes / edges.

Suggested fields:
- `case_key TEXT PRIMARY KEY`
- `review_path TEXT NOT NULL`
- `projection_path TEXT NOT NULL`
- `active_nodes JSONB NOT NULL DEFAULT '[]'::jsonb`
- `candidate_edges JSONB NOT NULL DEFAULT '[]'::jsonb`
- `contested_edges JSONB NOT NULL DEFAULT '[]'::jsonb`
- `required_checks JSONB NOT NULL DEFAULT '[]'::jsonb`
- `projection_version TEXT NOT NULL`
- `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`

## LMD experiment and exposure tables

### `lmd_experiment_assignments`
Suggested fields:
- `case_key TEXT PRIMARY KEY`
- `experiment_id TEXT NOT NULL`
- `arm TEXT NOT NULL`
  - `control|treatment`
- `generator_version TEXT NOT NULL`
- `policy_version TEXT NOT NULL`
- `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`

### `lmd_bundle_exposures`
Suggested fields:
- `id BIGSERIAL PRIMARY KEY`
- `case_key TEXT NOT NULL`
- `candidate_id TEXT NOT NULL`
- `candidate_type TEXT NOT NULL`
  - `case_review|intervention|aggregate_note|edge`
- `rank_position INT`
- `retrieval_score NUMERIC`
- `was_injected BOOLEAN NOT NULL DEFAULT TRUE`
- `required_check_keys JSONB NOT NULL DEFAULT '[]'::jsonb`
- `token_cost_estimate NUMERIC`
- `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`

### `lmd_candidate_stats`
Suggested fields:
- `candidate_id TEXT PRIMARY KEY`
- `candidate_type TEXT NOT NULL`
- `n_exposed INT NOT NULL DEFAULT 0`
- `distinct_case_count INT NOT NULL DEFAULT 0`
- `raw_uplift NUMERIC`
- `shrunken_uplift NUMERIC`
- `cost_adjusted_uplift NUMERIC`
- `genericity_penalty NUMERIC NOT NULL DEFAULT 0`
- `learned_weight NUMERIC NOT NULL DEFAULT 0`
- `status TEXT NOT NULL`
  - `draft|active|hold|retired`
- `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`

## Retrieval design for causal-aware LMD

## Key principle

LMD retrieval should be **hybrid**, not semantic-only.

### Retrieval order

1. structured shortlist
2. semantic rerank within shortlist
3. final cap + policy filtering

## Stage 1: structured shortlist

Shortlist inputs should include:
- platform
- category
- question mechanics
- source-of-truth class
- probability bucket
- time horizon
- active causal nodes
- candidate causal edges
- error family overlap
- intervention applicability

### Suggested shortlist rules

Case reviews / interventions should enter the shortlist only if they share at least one of:
- same active node family
- same causal edge family
- same question mechanics class
- same source-of-truth class
- same active intervention applicability condition

## Stage 2: semantic rerank

Once shortlisting is done, use semantic similarity on:
- case title
- question text
- review summary
- learning-packet summary fields
- aggregate note summaries

Semantic similarity should help rank cases that are already structurally plausible matches.
It should **not** be the sole selector.

## Stage 3: final scoring

Suggested scoring shape:

```text
retrieval_score =
  mechanism_overlap_score
+ source_truth_overlap_score
+ intervention_applicability_score
+ edge_confidence_score
+ candidate_uplift_score
+ category_overlap_score
+ semantic_similarity_score
- genericity_penalty
- stale_penalty
- token_cost_penalty
```

### Weighting principle

Highest weights should go to:
- shared causal edges
- shared source-of-truth mechanics
- active intervention match
- learned uplift / edge stats

Lower weights should go to:
- category overlap
- semantics

## LMD bundle extensions

A causal-aware `lmd-bundle.json` should include:

```json
{
  "causal_context": {
    "active_nodes": ["price-near-threshold", "verification-caution"],
    "matched_edges": ["price-near-threshold__increases__touch-probability"],
    "contested_edges": ["verification-caution__decreases__fair-value"],
    "required_checks": ["separate_resolution_risk_from_path_probability"]
  },
  "results": {
    "case_reviews": [],
    "active_interventions": [],
    "aggregate_notes": []
  }
}
```

### Prompt rendering rule

Do not inject raw graph structure into the prompt.
Instead inject a compact causal section such as:

```text
## LMD
case_review_paths:
- ...
active_intervention_paths:
- ...
causal_focus:
- price-near-threshold -> touch-probability
- verification-caution -> fair-value (contested)
required_checks:
- separate_resolution_risk_from_path_probability
```

## How the causal map improves over time

The causal map should improve through **logged outcome data**, not unbounded self-editing.

## Edge-level learning

For each edge, update:
- exposure count
- distinct case count
- observed uplift when edge-linked interventions or retrievals were used
- shrunken uplift estimate
- genericity / noise penalties
- active / hold / retired status

## Candidate-level learning

For each candidate (case review, intervention, aggregate note, or edge-derived rule), update:
- treatment exposure count
- matched control comparison
- raw uplift
- shrunken uplift
- cost-adjusted uplift
- learned retrieval weight

## Update cadence

Recommended cadence:
- per-case logging immediately
- policy / weight update in batch (nightly or periodic)

Do **not** update retrieval policy on every single case in real time.
Use batch updates with shrinkage.

## Intervention integration

Interventions should be first-class in the causal map.

Each intervention may be linked to:
- nodes it applies to
- edges it guards against or exploits
- source-of-truth classes where it is valid
- case cohorts where it showed uplift

This matters because interventions are often easier to evaluate than freeform notes.

## Guardrails

- keep graph injection small and derived, not raw and huge
- store contested edges explicitly; do not collapse disagreement into false certainty
- require deterministic exposure logging before using learned weights for promotion/demotion
- never let one case auto-promote a durable edge or intervention without review or batch evidence
- penalize generic recurring patterns that are too vague to guide behavior
- separate observed active nodes from inferred causal edges

## Proposed implementation surfaces

```text
roles/evaluator/runtime/scripts/
  upsert_causal_nodes.py
  upsert_causal_edges.py
  project_case_to_causal_map.py
  generate_lmd_bundle.py
  assign_lmd_experiment_arm.py
  log_lmd_bundle_exposure.py
  update_lmd_candidate_stats.py
  update_causal_edge_stats.py
```

```text
roles/evaluator/sql/
  020_causal_nodes.sql
  021_causal_edges.sql
  022_causal_edge_evidence.sql
  023_case_causal_projections.sql
  024_lmd_experiment_assignments.sql
  025_lmd_bundle_exposures.sql
  026_lmd_candidate_stats.sql
```

## Suggested phase plan

### Phase 1: graph substrate
- define node / edge contracts
- create DB tables
- create proposed canonical `60-causal-map/` structure

### Phase 2: case projections
- generate `causal-projection.json` from reviewed case reviews + signal packets
- persist case projections

### Phase 3: causal-aware LMD retrieval
- add structured shortlist based on active nodes / edges / mechanics
- semantic rerank within shortlist
- emit `causal_context` in `lmd-bundle.json`

### Phase 4: exposure logging + A/B assignment
- assign control/treatment deterministically
- log bundle exposures and candidate exposures

### Phase 5: learned policy updates
- compute shrunken uplift by candidate / edge / intervention
- update learned retrieval weights and candidate statuses

## Acceptance criteria

This spec should be considered materially implemented only when:

1. there is a canonical causal node / edge representation
2. reviewed cases can be projected into `causal-projection.json`
3. LMD retrieval uses structured node/edge overlap before semantics
4. `lmd-bundle.json` contains compact causal context
5. LMD exposures are logged per case and per candidate
6. candidate / edge stats are updated from resolved outcomes
7. retrieval policy can improve through learned weights rather than only static tags or semantics

## One-line operating model

Use the causal map as a normalized mechanism layer between reviewed evaluator knowledge and LMD, so the pipeline retrieves by shared causal pathway, logs exposure and impact, and improves retrieval/intervention policy over time based on resolved outcomes rather than topic similarity or uncontrolled self-rewriting.
