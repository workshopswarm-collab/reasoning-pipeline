---
type: system_plan
domain: methodology
status: active
last_updated: 2026-04-16
owner: evaluator
tags: [methodology/plan, causal-map, lmd, drivers-candidates, compiler, provisional-families]
---

# Driver-Candidate → Causal Compiler Implementation Plan

This document is the repo-ready implementation plan for compiling occurrence-backed mechanism discovery into the bounded LMD + causal-map lifecycle.

**Architectural clarification:** despite the historical filename, the canonical upstream substrate is `public.proposed_driver_occurrences`. The `qualitative-db/40-research/review-queue/drivers-candidates/` tree is a generated review surface over that ledger, not the source of truth.

It is meant to be the concrete bridge between:
- `public.proposed_driver_occurrences`
- `qualitative-db/40-research/review-queue/drivers-candidates/`
- `qualitative-db/00-system/methodology/causal-lifecycle-policy.md`
- `qualitative-db/00-system/methodology/causal-map-lmd-implementation-roadmap.md`
- the existing proposal-layer and live-graph runtime tables/scripts

## Why this exists

The current system already has:
- review-queue driver candidate notes
- surfaced family review and provisional family synthesis artifacts
- proposal-layer occurrence/stats tables
- shadow / trial / promotion infrastructure for causal proposals
- live-graph lifecycle, health scans, repair, and runtime recall

What it does **not** yet have is a deterministic compiler path that turns review-queue driver discoveries into:
- provisional families
- structured node/edge proposal seeds
- proposal occurrences that can enter the existing shadow / trial / promotion controller

Without that path, the system has a family-birth cold start and relies too much on manual concept translation.

## Core rule

`public.proposed_driver_occurrences` is the canonical upstream evidence ledger.

`drivers-candidates/` artifacts remain review/discovery artifacts derived from that ledger.

They must **not** directly create LMD-recallable canon.

The allowed compiler path is:

```text
reviewed case artifacts
-> proposed_driver_occurrence upsert
-> generated drivers-candidates review surfaces
-> compiled causal packet
-> provisional causal family
-> compiled proposal occurrence registry
-> shadow / trial / promotion
-> live graph draft / trial / active
```

## Design goals

1. Preserve provenance from source case / note to runtime proposal.
2. Reuse existing proposal-layer DB tables rather than inventing a parallel candidate system.
3. Add a small provisional-family incubation layer between discovery notes and proposal promotion.
4. Make the compiler deterministic enough for batch reruns and idempotent upserts.
5. Keep new families conservative by default: shadow-first, bounded exploratory trial only after replay evidence.
6. Make the compiler outputs inspectable on disk so a fresh session can audit failures and edge cases.

---

# 1) Canonical storage split

## Existing discovery layer

Canonical upstream substrate:
- `public.proposed_driver_occurrences`

Generated review surfaces:
- `qualitative-db/40-research/review-queue/drivers-candidates/generated-index.{md,json}`
- `qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/`
- `qualitative-db/40-research/review-queue/drivers-candidates/surfaced-family-review/`
- `qualitative-db/40-research/review-queue/drivers-candidates/provisional-family-synthesis/`

These remain human-readable, review-friendly, and non-canonical.

## New compiler-intermediate layer

Add:
- `qualitative-db/40-research/review-queue/drivers-candidates/compiled-causal-packets/`
  - one packet per source driver candidate note
  - JSON + markdown debug artifacts
  - deterministic compiler outputs and route decisions

## New provisional-family layer

Add DB incubation tables:
- `public.provisional_causal_families`
- `public.provisional_causal_family_members`
- `public.driver_candidate_compiler_runs`

## Existing runtime proposal layer

Continue using:
- `public.proposed_causal_candidate_occurrences`
- `public.proposed_causal_candidate_stats`

## Existing live graph layer

Continue using:
- `public.causal_nodes`
- `public.causal_edges`
- stats / lifecycle / health / repair tables and scripts

---

# 2) Exact data model

## 2A. New table: `public.provisional_causal_families`

Purpose:
- track family candidates born from driver-candidate discovery before they become canonical family policy entries or stable live-graph families

Recommended schema:

- `family_key text primary key`
- `family_label text not null`
- `family_description text`
- `source_lane text not null default 'drivers_candidates'`
- `status text not null`
  - allowed values:
    - `draft`
    - `review`
    - `shadow_enabled`
    - `trial_enabled`
    - `promoted`
    - `rejected`
    - `archived`
- `family_review_path text`
- `synthesis_path text`
- `seed_candidate_count integer not null default 0`
- `distinct_case_count integer not null default 0`
- `distinct_domain_count integer not null default 0`
- `distinct_platform_count integer not null default 0`
- `distinct_category_count integer not null default 0`
- `existing_family_overlap jsonb not null default '{}'::jsonb`
- `live_graph_overlap jsonb not null default '{}'::jsonb`
- `family_metadata jsonb not null default '{}'::jsonb`
- `compiler_metadata jsonb not null default '{}'::jsonb`
- `created_at timestamptz not null default now()`
- `updated_at timestamptz not null default now()`

Recommended indexes:
- `status`
- `source_lane`
- `updated_at`

## 2B. New table: `public.provisional_causal_family_members`

Purpose:
- map source driver-candidate notes into provisional families with explicit membership scores and compiled node/edge seeds

Recommended schema:

- `family_key text not null references public.provisional_causal_families(family_key) on delete cascade`
- `source_candidate_note_path text not null`
- `source_candidate_key text not null`
- `case_key text`
- `membership_score numeric not null default 0`
- `membership_role text not null`
  - allowed values:
    - `seed`
    - `supporting`
    - `borderline`
- `compiled_claim text`
- `compiled_node_seeds jsonb not null default '[]'::jsonb`
- `compiled_edge_seeds jsonb not null default '[]'::jsonb`
- `member_metadata jsonb not null default '{}'::jsonb`
- `created_at timestamptz not null default now()`
- `updated_at timestamptz not null default now()`

Primary key:
- `(family_key, source_candidate_note_path)`

Recommended secondary indexes:
- `case_key`
- `membership_role`
- `updated_at`

## 2C. New table: `public.driver_candidate_compiler_runs`

Purpose:
- audit compiler batch runs and make reruns / freshness / failure recovery explicit

Recommended schema:

- `run_id text primary key`
- `compiler_version text not null`
- `source_root text not null`
- `packet_root text not null`
- `status text not null`
  - `started`
  - `completed`
  - `failed`
  - `partial`
- `source_note_count integer not null default 0`
- `compiled_packet_count integer not null default 0`
- `rejected_count integer not null default 0`
- `proposal_seed_count integer not null default 0`
- `family_only_count integer not null default 0`
- `error_count integer not null default 0`
- `summary jsonb not null default '{}'::jsonb`
- `started_at timestamptz not null default now()`
- `completed_at timestamptz`

## 2D. Reuse existing proposal-layer tables as-is

### `public.proposed_causal_candidate_occurrences`

This remains the authoritative intake table for compiler-produced proposal seeds.

Important existing fields already fit the compiler path:
- `proposal_id`
- `proposal_key`
- `candidate_type`
- `candidate_label`
- `case_key`
- `review_path`
- `projection_path`
- `occurrence_reason`
- `evidence_excerpt`
- `genericity_penalty`
- `trigger_snapshot`
- `proposal_metadata`
- `mechanism_family`
- `proposal_source`
- `evidence_channels`
- `normalized_cluster_key`
- `context_snapshot`

### `public.proposed_causal_candidate_stats`

This remains the authoritative aggregation and lifecycle table. The compiler should feed it; it should not replace it.

---

# 3) On-disk compiler artifacts

## 3A. Packet directory

Add:

```text
qualitative-db/40-research/review-queue/drivers-candidates/compiled-causal-packets/
  generated-index.md
  packets/
    <candidate-slug>.json
    <candidate-slug>.md
  inputs/
    <candidate-slug>.json
```

## 3B. Packet contract

Each compiled packet should contain:

- source note metadata
- extracted mechanism phrase / claim
- compiler route decision
- provisional family assignment
- compiled node seeds
- compiled edge seeds
- genericity / duplication / confidence signals
- rationale bullets
- pointers to source case/review paths

Recommended top-level shape:

```json
{
  "schema_version": "v1",
  "source_candidate_note_path": "...",
  "source_candidate_key": "...",
  "source_case_key": "...",
  "compiler_action": "reject | route_to_learning | family_only | proposal_seed | merge_into_existing_family",
  "provisional_family_key": "...",
  "compiled_claim": "...",
  "compiled_nodes": [],
  "compiled_edges": [],
  "genericity_penalty": 0.0,
  "duplicate_risk": 0.0,
  "confidence": 0.0,
  "rationale": [],
  "compiler_metadata": {}
}
```

## 3C. Generated compiler status report

Add:
- `qualitative-db/60-causal-map/generated/driver-candidate-compiler-status.json`
- `qualitative-db/60-causal-map/generated/driver-candidate-compiler-status.md`

This report should summarize:
- packet counts by action
- provisional-family counts by status
- duplicate / merge routing counts
- notes rejected as non-causal
- notes routed to learning instead of causal proposal seed
- families ready for shadow
- families ready for exploratory trial

---

# 4) Proposed file + migration names

## SQL migrations

Add in this order:
- `roles/evaluator/sql/040_provisional_causal_families.sql`
- `roles/evaluator/sql/041_provisional_causal_family_members.sql`
- `roles/evaluator/sql/042_driver_candidate_compiler_runs.sql`

## Runtime scripts

Add:
- `roles/evaluator/runtime/scripts/compile_driver_candidates_to_causal_packets.py`
- `roles/evaluator/runtime/scripts/materialize_provisional_causal_families.py`
- `roles/evaluator/runtime/scripts/upsert_driver_candidate_proposal_occurrences.py`
- `roles/evaluator/runtime/scripts/generate_provisional_family_policies.py`
- `roles/evaluator/runtime/scripts/replay_provisional_family_shadow.py`
- `roles/evaluator/runtime/scripts/report_driver_candidate_compiler_status.py`
- `roles/evaluator/runtime/scripts/run_driver_candidate_compiler_cycle.py`

## Runtime library helpers

Add:
- `roles/evaluator/runtime/lib/driver_candidate_compiler.py`
- `roles/evaluator/runtime/lib/provisional_family_policy.py`

## File outputs

Add / generate:
- `qualitative-db/40-research/review-queue/drivers-candidates/compiled-causal-packets/`
- `qualitative-db/60-causal-map/provisional-family-policies.generated.json`
- `qualitative-db/60-causal-map/generated/driver-candidate-compiler-status.{json,md}`
- optionally:
  - `qualitative-db/60-causal-map/generated/provisional-family-shadow-replay.{json,md}`

---

# 5) Exact compiler workflow

## Step 0 — upstream discovery remains unchanged

Source artifacts:
- reviewed case notes
- case causal projections
- driver candidate notes
- family review suggestions
- provisional family synthesis notes

The compiler never bypasses review. It only consumes review-queue artifacts.

## Step 1 — compile driver candidate notes into structured packets

Script:
- `compile_driver_candidates_to_causal_packets.py`

Inputs:
- `drivers-candidates/candidate-notes/*.md`
- optional review/synthesis hints from:
  - `surfaced-family-review/`
  - `provisional-family-synthesis/`

For each note, parse/extract:
- candidate slug
- source case key / review path
- recurring mechanism phrasing
- explicit or implied directionality
- broadness / genericity signals
- possible existing family matches
- possible live-graph duplicate / merge targets
- whether the note describes:
  - a reusable node
  - a reusable edge
  - only a broad family theme
  - a non-causal lesson

### Step 1 route decisions

Each note must end in exactly one compiler action:
- `reject`
  - noise / too broad / too weak / malformed
- `route_to_learning`
  - durable lesson, but not a reusable causal mechanism
- `family_only`
  - signals a recurring family/theme but does not yet support a clean node/edge seed
- `proposal_seed`
  - specific enough to create node/edge proposal occurrences
- `merge_into_existing_family`
  - clearly belongs to an existing canonical or provisional family without adding a new family key

## Step 2 — cluster packets into provisional families

Script:
- `materialize_provisional_causal_families.py`

Inputs:
- compiled packets
- surfaced family-review hints
- provisional family-synthesis artifacts
- current canonical family policy keys

Behavior:
- assign stable `family_key`
- upsert `public.provisional_causal_families`
- upsert `public.provisional_causal_family_members`
- write synthesized family metadata:
  - seed note count
  - distinct case count
  - domain spread
  - overlap with canonical family set
  - overlap with live graph
  - duplicate / merge risk

### Step 2 statuses

Initial family status rules:
- `draft`
  - brand-new family with weak evidence
- `review`
  - enough evidence to track, but not yet shadow-enabled
- `shadow_enabled`
  - enough evidence to support replay/shadow matching
- `trial_enabled`
  - enough replay evidence for bounded exploratory trial eligibility
- `rejected`
  - bad cluster / duplicate / too broad / non-causal
- `promoted`
  - family accepted into canonical family policy set
- `archived`
  - obsolete / merged / dormant

## Step 3 — generate provisional family policies

Script:
- `generate_provisional_family_policies.py`

Output:
- `qualitative-db/60-causal-map/provisional-family-policies.generated.json`

Default policy for a new provisional family:
- enabled for shadow only
- trial disabled by default
- active capacity = 0
- conservative genericity ceiling
- no live-graph promotion budget

This file should be merged read-only with canonical `family-policies.json` by the policy loader.

## Step 4 — upsert compiler-produced proposal occurrences

Script:
- `upsert_driver_candidate_proposal_occurrences.py`

For each compiled packet with `compiler_action=proposal_seed`:
- create node and/or edge occurrence rows in `public.proposed_causal_candidate_occurrences`

### Field mapping

#### Common mapping
- `proposal_id`
  - `node:<node_key>` or `edge:<edge_key>`
- `proposal_key`
  - compiled node/edge key
- `candidate_type`
  - `node` or `edge`
- `candidate_label`
  - compiled label
- `case_key`
  - source case key
- `review_path`
  - source review path
- `projection_path`
  - source projection when available
- `occurrence_reason`
  - `driver_candidate_compiler`
- `evidence_excerpt`
  - compact claim / quote from the source note
- `genericity_penalty`
  - compiler-generated value
- `mechanism_family`
  - provisional or canonical family key
- `proposal_source`
  - `driver_candidate_compiler`
- `evidence_channels`
  - should include `driver_candidate_note`
- `normalized_cluster_key`
  - provisional family key or family cluster key
- `context_snapshot`
  - case mechanics / category / source-of-truth class / domain spread
- `proposal_metadata`
  - source note path
  - compiler action
  - compiler version
  - confidence
  - duplicate / merge hints
  - provisional family key

#### Node-specific mapping
- `node_type`
- `source_node_key = null`
- `target_node_key = null`
- `effect_sign = null`

#### Edge-specific mapping
- `source_node_key`
- `target_node_key`
- `effect_sign`
- `support_direction`

## Step 5 — existing aggregation/advancement pipeline takes over

Run existing scripts unchanged or with minor source-awareness extensions:
- `aggregate_causal_candidate_proposals.py`
- `advance_proposed_causal_candidates.py`

Compiler-originated proposal occurrences should aggregate into:
- `aggregated`
- `shadow_candidate`
- `trial_candidate`
- `promotion_ready`

under the same bounded lifecycle rules as other proposal sources.

## Step 6 — replay / backfill for provisional families

Script:
- `replay_provisional_family_shadow.py`

Purpose:
- reduce cold start by using existing reviewed cases to estimate whether a provisional family repeatedly matches and whether its proposal seeds would have had shadow utility

Outputs:
- family-level replay stats in `family_metadata`
- optional generated report:
  - `qualitative-db/60-causal-map/generated/provisional-family-shadow-replay.{json,md}`

Recommended replay metrics:
- matched_case_count
- distinct_case_count
- shadow_match_count
- shadow_positive_count
- shadow_score_sum
- genericity failures
- duplicate-of-live-graph rate
- family-local case-mix distribution

## Step 7 — bounded exploratory trial enablement

A provisional family becomes `trial_enabled` only after:
- replay/shadow evidence clears minimum gates
- duplicate/live-graph overlap risk is acceptable
- genericity remains bounded
- no family-level quarantine / freeze flag is active

At that point, compiler-born proposal seeds inside the family may become `trial_candidate` through the existing proposal controller and use the current treatment-only overlay path.

---

# 6) Deterministic compiler heuristics

## Route-to-learning instead of causal proposal when:
- the note is clearly a broad lesson, not a reusable mechanism
- the note is too descriptive / too case-specific
- no stable node or edge claim can be extracted

## Family-only instead of proposal-seed when:
- the pattern looks recurrent
- there is enough evidence to name a family
- but the note does not yet support a clean node or edge formulation

## Proposal-seed when:
- the note expresses a reusable mechanism claim
- at least one stable node or edge key can be extracted
- genericity is not excessive
- it does not obviously duplicate the live graph

## Merge-into-existing-family when:
- the idea is genuinely new as a note/example
- but clearly belongs inside an already known family
- and should not create a new family key

## Reject when:
- malformed / low-confidence note
- pure topical tag without mechanism content
- duplicate noise with no incremental evidence value

---

# 7) Exact modifications to existing code

## `roles/evaluator/runtime/lib/causal_family_policy.py`

Extend loader to merge:
1. canonical `qualitative-db/60-causal-map/family-policies.json`
2. generated `qualitative-db/60-causal-map/provisional-family-policies.generated.json`

Rule:
- canonical policy wins on collisions
- provisional families cannot overwrite canonical family keys

## `roles/evaluator/runtime/scripts/aggregate_causal_candidate_proposals.py`

Extend reporting so compiler-originated proposal occurrences are visible in:
- source mix
- family birth / provisional-family summaries
- family-level blocker reporting

## `roles/evaluator/runtime/scripts/report_causal_governance.py`

Extend to include:
- provisional family quarantine recommendations
- provisional families with repeated weak replay or repeated hold-causing descendants

## `roles/evaluator/runtime/scripts/run_lmd_causal_maintenance_cycle.py`

Later phase: optionally include the compiler cycle and reports in the broader maintenance loop after initial validation.

---

# 8) New reports needed

## `report_driver_candidate_compiler_status.py`

Should answer:
- how many driver candidate notes were compiled?
- how many were rejected / routed to learning / family-only / proposal-seed?
- which provisional families are growing?
- which provisional families are ready for shadow or exploratory trial?
- which notes/families repeatedly fail because of genericity or live-graph duplication?

## `report_provisional_family_cold_start_status.py`

Optional but recommended.

Should answer:
- which provisional families are blocked by too few cases?
- too little shadow judged evidence?
- too much genericity?
- too much overlap with canonical families?
- too much contestation / weak replay?

---

# 9) Rollout order

## Slice 1 — compiler IR + family tables

Implement:
- migrations `040-042`
- packet compiler
- provisional family materializer
- compiler status report

Done when:
- driver candidate notes compile into stable packets
- provisional families exist in DB
- no proposal upserts yet

## Slice 2 — proposal bridge

Implement:
- proposal occurrence upsert bridge
- source-aware aggregation visibility

Done when:
- compiler-originated proposal seeds appear in `proposed_causal_candidate_occurrences`
- aggregation runs cleanly

## Slice 3 — replay/backfill

Implement:
- family replay / shadow pass
- cold-start status report
- provisional-family policy generation

Done when:
- provisional families can accumulate replay evidence without live prompt injection

## Slice 4 — bounded exploratory family trials

Implement:
- `trial_enabled` gating from replay evidence
- bounded exploratory family slot rules
- governance visibility for family freezes/quarantines

Done when:
- new families can enter trial without manual case injection
- family birth remains bounded and auditable

---

# 10) Acceptance criteria

The compiler path is good enough when all of the following are true:

1. A new driver candidate note can be deterministically compiled into one of the allowed actions.
2. Source note → provisional family → proposal occurrence provenance is fully preserved.
3. Compiler-originated proposal seeds enter the existing proposal lifecycle without custom ad hoc handling.
4. New family birth does not require hand-editing canonical family policy files.
5. New families remain shadow-first and bounded by default.
6. Families/proposals can be rejected, merged, frozen, or archived without destructive rewrites.
7. A fresh session can inspect compiler packets, provisional family DB state, and status reports and explain why a note did or did not enter trial.

---

# 11) Open questions to resolve during implementation

1. Should provisional families remain DB-only, or should each family also get a markdown note under `qualitative-db/60-causal-map/provisional-families/` for human review?
   - recommended answer: DB first, optional generated markdown later

2. Should compiler-originated proposal occurrences use `proposal_source='driver_candidate_compiler'` only, or preserve more granular sub-sources?
   - recommended answer: use `driver_candidate_compiler` plus richer `proposal_metadata`

3. Should family replay statistics live in `family_metadata` or a separate stats table?
   - recommended answer: start in `family_metadata`, split later only if querying becomes heavy

4. Should the maintenance cycle run compiler/replay every time by default?
   - recommended answer: no; start with explicit batch runs, then add scheduled backstop only after stability is proven

---

# 12) Fresh-session read order

For a new session that needs to continue this work, read in this order:

1. `qualitative-db/00-system/methodology/causal-lifecycle-policy.md`
2. `qualitative-db/00-system/methodology/causal-map-lmd-implementation-roadmap.md`
3. `qualitative-db/00-system/methodology/driver-candidate-causal-compiler-implementation-plan.md`
4. `qualitative-db/40-research/review-queue/README.md`
5. current generated status artifacts under `qualitative-db/60-causal-map/generated/`

That sequence should be enough to reconstruct:
- what layer each artifact belongs to
- what remains discovery-only vs runtime-governed
- what exact implementation slice should be built next
