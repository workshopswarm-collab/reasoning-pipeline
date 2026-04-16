---
type: system_plan
domain: methodology
status: active
last_updated: 2026-04-15
owner: evaluator
tags: [methodology/roadmap, causal-map, lmd, recursive-improvement, implementation-plan]
---

# Causal Map + LMD Implementation Roadmap

This document is the implementation roadmap for the bounded self-improving LMD + causal-map system.

It sits between:
- `causal-map-lmd-integration-spec.md` (target architecture)
- `causal-lifecycle-policy.md` (promotion / decay / anti-sprawl guardrails)
- current live repo code (source of truth for what is already implemented)

## Core operating model

The system should improve through three coupled loops:

1. **retrieval loop**
   - improve which learnings / checks / mechanisms LMD retrieves
2. **topology loop**
   - advance candidate nodes / edges through shadow, trial, and promotion
3. **repair loop**
   - detect drift, duplicates, stale topology, and low-utility graph items and demote / repair them

Design principle:
- prefer more measurement and policy-controlled transitions over freer automation
- prefer batch deterministic advancement over opaque one-off judgment
- keep sophistication layered and reversible

## Lifecycle split

### Proposal-layer stages

Proposal-layer candidates may move through:
- `observed`
- `aggregated`
- `shadow_candidate`
- `trial_candidate`
- `promotion_ready`
- `rejected`
- `duplicate_of_live_graph`

Proposal-layer items are **not** live graph canon.

### Live-graph stages

Live graph nodes / edges may move through:
- `draft`
- `trial`
- `active`
- `hold`
- `retired`
- `archived`

LMD recall policy:
- `active` = recallable by default
- `trial` = recallable only in explicit trial / treatment modes
- `draft` = review-visible, not default recall
- `hold`, `retired`, `archived` = not injected

## Current implemented baseline

### Phase 0 — significance / mining baseline cleanup

**Status:** implemented

Implemented surfaces:
- stricter projection significance now governs proposal mining
- required-check-heavy but structurally weak projections no longer qualify as significant
- mining recomputes significance instead of trusting stale embedded metadata
- invariant checker:
  - `roles/evaluator/runtime/scripts/check_causal_projection_mining_invariants.py`

Done when:
- proposal occurrence case keys match the significance-qualified projection set

### Phase 1 — shadow outcome labeling

**Status:** implemented

Implemented surfaces:
- migration:
  - `roles/evaluator/sql/034_proposed_causal_shadow_outcome_labels.sql`
- shadow outcome library:
  - `roles/evaluator/runtime/lib/proposed_causal_shadow_outcomes.py`
- scorer:
  - `roles/evaluator/runtime/scripts/score_proposed_causal_shadow_outcomes.py`

Current deterministic labels:
- `helpful`
- `neutral`
- `harmful`
- `unclear`

Current rule:
- use only deterministic downstream evidence from:
  - same-case proposal occurrences
  - same-case canonical reviewed suggestions
  - same-case final projection overlap
- absent downstream reviewed artifacts should remain `unclear`

### Phase 2A — family policy control surface

**Status:** implemented

Implemented surfaces:
- canonical config:
  - `qualitative-db/60-causal-map/family-policies.json`
- DB table:
  - `roles/evaluator/sql/035_causal_family_policies.sql`
- loader:
  - `roles/evaluator/runtime/lib/causal_family_policy.py`
- DB sync helper:
  - `roles/evaluator/runtime/scripts/upsert_causal_family_policies.py`

Current purpose:
- turn `mechanism_family` into a real policy surface for:
  - shadow budgets
  - trial budgets
  - active capacity
  - family-local ranking
  - advancement blockers

### Phase 2B — deterministic proposal advancement

**Status:** implemented

Implemented surfaces:
- authoritative aggregation / stage writing:
  - `roles/evaluator/runtime/scripts/aggregate_causal_candidate_proposals.py`
- explicit advancement entrypoint:
  - `roles/evaluator/runtime/scripts/advance_proposed_causal_candidates.py`

Current advancement rule:
- proposal must first clear base support thresholds (`promotion_status in {proposed, draft_recommendation}`)
- then it must clear family-policy thresholds for:
  - shadow judged count
  - helpful shadow count
  - shrunken `shadow_trial_score`
  - non-intervention support case count
  - genericity ceiling
  - duplicate-similarity ceiling
- then it must rank inside the family trial budget (`max_trial_candidates`)
- only then does lifecycle stage advance to `trial_candidate`

Current conservative trial utility:
- `shadow_trial_score = shadow_score_sum / (shadow_judged_count + 4.0)`

Current live reality on 2026-04-15:
- advancement path works
- synthetic smoke can produce `trial_candidate`
- current real data still yields `0 trial_candidate`, which is correct under present evidence

## Forward implementation phases

### Phase 3 — trial exposure substrate

#### Goal
Create the first-class logging substrate for proposal-layer trial exposures before trial candidates are injected into runtime prompts.

#### Build
Add:
- `roles/evaluator/sql/036_proposed_causal_trial_exposures.sql`
- `roles/evaluator/runtime/lib/proposed_causal_trial_selection.py`
- `roles/evaluator/runtime/scripts/log_proposed_causal_trial_exposure.py`
- optional `trial_overlay` block in `lmd-bundle.json`
- dispatch/runtime summary fields for trial overlays

#### Recommended schema
`public.proposed_causal_trial_exposures`
- `proposal_id`
- `proposal_key`
- `candidate_type`
- `mechanism_family`
- `case_key`
- `dispatch_id`
- `research_run_id`
- `experiment_id`
- `experiment_arm`
- `trial_rank`
- `shadow_trial_score`
- `family_trial_rank`
- `injected`
- `preview_only`
- `overlay_mode`
- `matched_active_nodes`
- `matched_candidate_edges`
- `matched_required_checks`
- `notes`
- timestamps

#### Selection policy
Trial exposure selection should require:
- `lifecycle_stage == trial_candidate`
- family policy enabled
- positive or non-negative trial utility
- no duplicate-of-live-graph
- no merge blocker
- strict per-dispatch overlay caps

#### Done when
- trial overlay previews can be selected deterministically
- exposures are logged per dispatch / proposal
- no runtime prompt injection is required yet

### Phase 4 — trial-mode injection

#### Goal
Actually test proposal-layer trial candidates in runtime, safely.

#### Status
Partially implemented on 2026-04-15.

Implemented surfaces:
- bundle-native overlay injection decision in `generate_lmd_bundle.py`
- separate experimental prompt section in `build_researcher_prompt.py`
- treatment-only gating via bundle `trial_overlay.used`
- dispatch/runtime/frontmatter propagation of `trial_overlay_used` and injected counts
- trial exposure logging records whether the overlay was previewed or treatment-injected

#### Build
Add / extend:
- trial-only injection path in bundle generation / prompt rendering
- treatment/trial cohort gating
- separate logging from canonical LMD exposure

#### Injection rule
Trial candidates must be:
- treatment / trial cohort only
- clearly marked experimental
- not treated as canonical live-graph memory
- token-bounded and count-bounded

#### Suggested prompt section
- `## Trial mechanism checks (experimental)`
- explicitly described as experimental / not canon

#### Remaining work
- live runs still have `0 trial_candidate`, so no real trial overlays are injected yet
- when real trial candidates appear, validate prompt size, section behavior, and runtime logging on live dispatches
- optionally add tighter per-prompt token/candidate caps if early live runs show prompt bloat

#### Done when
- treatment dispatches can receive bounded trial overlays
- control dispatches cannot
- all trial injections are logged separately

### Phase 5 — trial outcome evaluation

#### Goal
Measure whether actual trial injection helped.

#### Status
Implemented on 2026-04-15.

Implemented surfaces:
- migration:
  - `roles/evaluator/sql/037_proposed_causal_trial_outcome_labels.sql`
- deterministic scorer:
  - `roles/evaluator/runtime/lib/proposed_causal_trial_outcomes.py`
  - `roles/evaluator/runtime/scripts/score_proposed_causal_trial_outcomes.py`
- aggregation / summary integration:
  - `roles/evaluator/runtime/scripts/aggregate_causal_candidate_proposals.py`

#### Metrics
Track:
- `trial_exposure_count`
- `trial_helpful_count`
- `trial_neutral_count`
- `trial_harmful_count`
- `trial_unclear_count`
- `trial_score_sum`
- `trial_shrunken_utility`

#### Current utility rule
Use conservative shrinkage:
- `trial_shrunken_utility = trial_score_sum / (trial_exposure_count + 6.0)`

Scoring scope:
- actual injected trial exposures only by default
- preview-only overlays are excluded from trial utility and remain non-evidentiary for this phase

#### Done when
- every injected trial exposure can later be labeled deterministically
- proposal summaries expose trial utility, not just shadow utility
- trial utility is available for the later `trial_candidate -> promotion_ready` controller

### Phase 6 — promotion-ready controller

#### Goal
Advance only the strongest `trial_candidate` proposals to `promotion_ready`.

#### Status
Implemented on 2026-04-15.

#### Build
Implemented in:
- `roles/evaluator/runtime/scripts/advance_proposed_causal_candidates.py`
- `roles/evaluator/runtime/scripts/aggregate_causal_candidate_proposals.py`
- family policy surfaces:
  - `qualitative-db/60-causal-map/family-policies.json`
  - `roles/evaluator/sql/038_extend_causal_family_policies_for_promotion.sql`

#### Required transition checks
`trial_candidate -> promotion_ready` now requires:
- positive trial utility after shrinkage
- bounded contestation
- bounded genericity
- no open health violations
- no duplicate / merge blocker
- family rank high enough to deserve a slot

#### Current blockers
- `below_family_min_trial_judged_count`
- `below_family_min_trial_helpful_count`
- `below_family_min_trial_shrunken_utility`
- `harmful_trial_rate_too_high`
- `contest_case_count_above_family_limit`
- `open_health_violations`
- `family_slot_taken_by_stronger_sibling`
- `not_trial_candidate`

#### Notes
Current deterministic implementation adds:
- `trial_shrunken_utility`
- `trial_harmful_rate`
- `promotion_readiness`
- `family_promotion_ready_rank`
- `within_family_promotion_ready_budget`

#### Done when
- `promotion_ready` is batch-generated with explicit reasons
- proposal summaries expose promotion-readiness blockers and ranks

### Phase 7 — materialize promotion-ready candidates into live graph drafts

#### Goal
Turn `promotion_ready` proposals into real live-graph `draft` nodes / edges.

#### Status
Implemented on 2026-04-15.

#### Build
Implemented in:
- `roles/evaluator/runtime/scripts/materialize_promoted_causal_candidates.py`

#### Output surfaces
Writes to:
- `qualitative-db/60-causal-map/nodes/`
- `qualitative-db/60-causal-map/edges/`

Records:
- originating `proposal_id`
- support case keys
- shadow summary
- trial summary
- promotion reasons
- lifecycle event (best-effort against `causal_graph_lifecycle_events` via schema introspection)

#### Notes
Current materialization behavior is intentionally non-destructive:
- skip if the target draft note already exists
- never overwrite an existing live graph note
- refresh proposal advancement after materialization so materialized proposals can naturally fall out of the pending-candidate path on the next aggregate pass

#### Done when
- `promotion_ready` can materialize into live `draft` topology with preserved provenance
- repeated runs are idempotent for already-materialized proposal keys

### Phase 8 — live-graph trial recall

#### Goal
Allow live-graph `trial` items to participate in LMD recall, but only in explicit trial / treatment modes.

#### Status
Implemented on 2026-04-15.

#### Build
Implemented in:
- `roles/orchestrator/researchers-swarm-subagents/planner/scripts/generate_lmd_bundle.py`
- `roles/orchestrator/researchers-swarm-subagents/planner/scripts/build_researcher_prompt.py`
- `roles/evaluator/runtime/lib/lmd.py`
- `roles/evaluator/runtime/scripts/elevate_live_causal_graph_drafts_to_trial.py`

#### Rule
- `draft` = review-only
- `trial` = explicit trial recall only
- `active` = default recall

#### Notes
Current Phase 8 behavior is intentionally bounded:
- LMD bundle generation now enforces lifecycle-aware live-graph recall (`active` by default; `trial` only when the run is in explicit treatment / trial / shadow mode)
- prompt rendering labels non-active live-graph causal focus items so treatment-only trial structure is visible as experimental rather than silently presented as settled canon
- edge exposure logging now preserves lifecycle metadata for live-graph causal-focus candidates
- explicit draft -> trial advancement is manual and review-driven via `elevate_live_causal_graph_drafts_to_trial.py`; the automated controller remains a later Phase 9 concern

#### Done when
- promoted draft items can be elevated to live `trial`
- only trial/treatment cohorts see them

### Phase 9 — active promotion / demotion controller

#### Goal
Move live graph items through:
- `draft -> trial -> active`
- `active -> hold -> retired -> archived`

#### Status
First bounded slice implemented on 2026-04-15.

#### Build
Current slice implemented in:
- `roles/evaluator/runtime/scripts/update_causal_node_stats.py`
- `roles/evaluator/runtime/scripts/update_causal_edge_stats.py` (extended metadata for helpful/harmful trial outcomes)
- `roles/evaluator/runtime/scripts/advance_live_causal_graph_items.py`

Use:
- `causal_graph_lifecycle_events`
- `causal_graph_health_violations`
- live utility stats
- family budgets
- decay signals

#### Promotion requirements
- repeated positive trial utility
- low harmful rate
- non-trivial context breadth
- family active slot availability
- acceptable contestation profile

#### Demotion requirements
- repeated negative utility
- long non-use despite matching opportunities
- family crowding
- supersession by stronger sibling
- stale evidence

#### Notes
Current Phase 9 behavior is intentionally conservative and preview-first:
- `advance_live_causal_graph_items.py` defaults to dry-run / recommendation mode; `--apply` is required for real lifecycle writes
- the controller now supports bounded draft -> trial and trial -> active promotion recommendations, plus hold/retire demotion recommendations for health-violation, negative-utility, crowding, supersession, and stale-hold cases
- family caps reuse the existing causal-family policy surface (`max_trial_candidates`, `max_active_nodes`, `max_active_edges`) rather than inventing a second live-graph policy file
- node-level stats now have a dedicated updater so node-only trial exposures can contribute to lifecycle decisions instead of leaving the controller edge-only
- `run_live_causal_graph_cycle.py` now provides a single periodic wrapper that refreshes node/edge stats, runs health scanning, and then invokes the controller from one entry point
- current live dry-runs are expected to be quiet until real trial exposure data accumulates; seed/draft graph items should remain mostly blocked rather than auto-promoting

#### Done when
- live graph topology can self-tighten over time

### Phase 10 — repair / health automation

#### Goal
Make the causal-map system self-repairing without unconstrained self-rewriting.

#### Status
Health scan, low-risk repair, and automatic cycle-integration slices implemented on 2026-04-15.

#### Build
Current slices implemented in:
- `roles/evaluator/runtime/scripts/scan_causal_graph_health.py`
- `roles/evaluator/runtime/scripts/repair_causal_graph.py`
- `roles/evaluator/runtime/scripts/run_live_causal_graph_cycle.py`

Later phase work still planned:
- broader low-risk repair coverage beyond hold / retire / align-status / regenerate-sidecar-first policy
- higher-risk repair actions should remain explicit and auditable

#### Violation classes
At minimum:
- structural
- evidence
- utility
- freshness

#### Notes
Current Phase 10 behavior is intentionally conservative but now materially more automatic:
- `scan_causal_graph_health.py` scans the live graph for structural, evidence, utility, and freshness issues and can refresh `causal_graph_health_violations`
- the scan slice resolves health state by reopening current findings and marking stale in-scope live-graph findings as resolved, rather than only appending duplicates forever
- the scanner is filterable by node / edge / mechanism family, which makes it usable both from the periodic wrapper and for targeted audits during development
- `repair_causal_graph.py` computes repairs from the same current health-scan logic and now auto-applies broader low-risk deterministic actions: `active|trial -> hold` for clearly unhealthy live items, `hold -> retired` for stale hold items, status alignment for `lifecycle_stage` / `status` mismatches, and sidecar regeneration for missing-sidecar findings
- live edges with missing review paths now route into the automatic hold policy when they are still in `active` or `trial`, rather than remaining purely advisory
- `run_live_causal_graph_cycle.py` now includes repair as a first-class automatic step after health scan and before the controller; repair writes still require explicit apply mode in live runs, but the operational surface is no longer manual handoff only
- unsupported or more speculative repairs (for example proposal reopening, merge suggestions, evidence reconstruction, or auto-generated new topology) remain deferred suggestions in the repair output rather than automatic writes
- current repair previews may still be quiet when the persisted stats tables have not been refreshed recently; the periodic wrapper is intended to refresh node/edge stats before health scan, and repair/controller should generally be interpreted from the same persisted cycle state

#### Repair actions
Start low-risk only:
- recompute summaries
- align status to lifecycle stage
- regenerate missing sidecars
- mark hold
- reopen as proposal only
- suggest merge
- retire stale items

#### Done when
- periodic repair scans can run safely
- low-risk repairs are automatic
- higher-risk repairs remain auditable

### Phase 11 — learned retrieval policy tuning

#### Goal
Improve LMD impact without requiring topology changes every time.

#### Status
First learned-ranking slice implemented on 2026-04-15.

#### Build
Extend retrieval scoring in bundle generation to consider:
- active utility
- trial utility
- shadow utility
- family crowding
- decay penalties
- contestation penalties
- active vs trial trust tier
- dispatch-local overlay caps

#### Notes
Current Phase 11 behavior is a first scoring slice, not the full tuning end-state:
- `generate_lmd_bundle.py` now loads richer candidate/node/edge stats, computes live-family crowding from the current graph plus family-policy caps, and attaches Phase 11 score metadata to recalled live nodes/edges
- live-graph causal context is now ordered by learned usefulness instead of plain key ordering, so prompt/exposure ordering reflects active/trial trust tier, learned utility, contestation, decay, and family crowding
- case-review retrieval now gets Phase 11 live-graph bonuses from matched nodes/edges plus richer candidate-stat bonuses instead of only a thin edge-weight bump
- active-intervention selection now uses explicit score breakdowns with selector-match score, required-check overlap bonuses, and Phase 11 live-context bonuses instead of only selector score plus a thin candidate bonus
- aggregate-note selection is now candidate-scored rather than fixed-heuristic-only, with explicit breakdowns tied to live workflow/source-family signals and learned candidate stats
- the Phase 11 formula layer is now distribution-aware: candidate/node/edge bonuses are normalized against the actual live stats-table distributions rather than assuming a fixed raw numeric range, and overlay scoring is normalized against the current proposal-summary distribution as well
- bundle debug output now surfaces ranked live node/edge metadata plus selected case-review / intervention / aggregate-note score breakdowns directly, including the normalized Phase 11 distribution profiles, so retrieval changes are inspectable rather than hidden inside final ordering
- `proposed_causal_trial_selection.py` now uses trial utility and live-family crowding in overlay scoring, and dispatch-local overlay caps now tighten automatically when the current bundle already contains live trial structure
- remaining future work can still refine formulas and weighting once more real live-graph trial exposure data accumulates; this slice establishes the first measured, normalized ranking path

#### Done when
- retrieval ranking changes based on measured usefulness, not just static heuristics

### Phase 12 — cross-family / higher-order discovery

#### Goal
Allow the system to discover better higher-order reusable structures over time.

#### Build later, offline only
- sibling clustering
- merge / supersession ranking
- motif detection
- cross-family interaction suggestions
- multi-hop mechanism suggestions

#### Hard rule
Nothing in this phase may directly create live recallable canon.
Everything must still flow through:
- proposal
- shadow
- trial
- promotion_ready
- live draft / trial / active

## Required metrics going forward

### Proposal-layer metrics
Keep / extend:
- `shadow_trial_score`
- `shadow_label_balance`
- `trial_exposure_count`
- `trial_helpful_count`
- `trial_harmful_count`
- `trial_shrunken_utility`
- `family_trial_rank`
- `family_active_rank`
- `promotion_ready_blockers`

### Live-graph metrics
Add / extend:
- `last_matched_at`
- `last_injected_at`
- `last_helpful_at`
- `live_shrunken_utility`
- `decay_score`
- `sibling_competition_score`

## Practical sequencing rule

Prefer the following order:
1. add logging / evaluation surfaces
2. add deterministic stage transitions
3. add bounded runtime injection
4. add promotion / demotion automation
5. add repair / decay automation
6. tune retrieval formulas after enough evidence accumulates

## Current next recommended step

The next best implementation step after the current baseline is:
- **Phase 11 — learned retrieval policy tuning**

Reason:
- Phases 3 through 10 now have working bounded implementations across exposure logging, trial injection, lifecycle control, health scanning, and automatic low-risk repairs.
- The next numbered step should shift from topology/control-plane construction toward retrieval ranking that uses measured usefulness, trust tier, decay, contestation, and family crowding.
- Remaining Phase 10 work can continue incrementally, but it is no longer the stale blocker implied by the old Phase 3 note.
