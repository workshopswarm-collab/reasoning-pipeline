---
type: system_guide
domain: learnings
status: active
last_updated: 2026-04-15
owner: orchestrator
tags: [learnings/guide, qualitative-db/50-learnings, workflow, recursive-improvement]
---

# 50-learnings

This README is subordinate to `qualitative-db/00-system/README.md` and related 00-system policy files. If there is any conflict, follow `qualitative-db/00-system/`.

Fresh-instance shortcut:
1. read `qualitative-db/00-system/START-HERE.md`
2. read `qualitative-db/00-system/README.md`
3. read this file only if you are reviewing resolved cases, aggregating cross-case lessons, or evaluating whether the pipeline itself should change

This folder is the vault's **recursive-improvement layer**.

Concrete implementation target:
- `qualitative-db/00-system/methodology/recursive-learning-system-spec.md`
- `qualitative-db/00-system/methodology/causal-map-lmd-integration-spec.md`

## Concrete build order from current state

This section is the near-term implementation order for turning the current evaluator + learning layer into a real recursive-learning runtime.

### Current foundation already in place

Already built:
- canonical evaluator case-review bundles under `case-reviews/<case-key>/`
- quant-aware `learning-packet.json`
- canonical `review.md`
- `signal-packet.json`
- DB-backed `learning_case_reviews` + `learning_signal_occurrences`
- aggregate generated indexes under `error-patterns/`, `source-performance/`, `workflow-performance/`, and `driver-learning/`
- evaluator-agent review authoring
- importance-gated evaluator memory upgrades

Current implementation snapshot:
- Step 1 is live: intervention registry + intervention application logging are implemented repo-side and backed by live Postgres tables
- Step 2 foundation is now live: `lmd_experiment_assignments` and `lmd_bundle_exposures` exist in Postgres; deterministic assignment is wired into dispatch preparation; runtime handoff code is prepared to log LMD bundle exposures when a real `lmd-bundle.json` is present
- Step 3 substrate is now live: canonical mechanism notes exist under `qualitative-db/60-causal-map/`; live Postgres tables now exist for `causal_nodes`, `causal_edges`, `causal_edge_evidence`, and `case_causal_projections`; and the first small seed ontology has been registered (9 nodes, 6 edges, 5 evidence rows)
- Step 4 first slice is now live: `roles/evaluator/runtime/scripts/project_case_to_causal_map.py` writes `case-reviews/<case-key>/causal-projection.json`, persists into `public.case_causal_projections`, and is now optionally wired into `materialize_case_review_bundle.py` / `backfill_case_review_bundles.py` via `--causal-projection`; proof-of-life projection exists for `case-20260414-4e668883` (1 live projection row so far)
- Step 5 first slice is now live: planner-side `roles/orchestrator/researchers-swarm-subagents/planner/scripts/generate_lmd_bundle.py` performs mechanism-first shortlisting with semantic reranking inside the shortlist, writes `lmd-bundle.json` during dispatch preparation, and carries compact causal context / required checks / result paths through dispatch notes
- Step 6 is now live: `build_researcher_prompt.py` injects LMD after QMD for treatment-arm bundles, promotes LMD required checks into the case completion checklist, sets `lmd_used=true` only when a treatment bundle has real payload, and thereby activates downstream LMD exposure logging in runtime handoff flow
- Step 7 first slice is now live: evaluator scripts `update_lmd_candidate_stats.py` and `update_causal_edge_stats.py` compute batch outcome/weight stats into live Postgres tables `lmd_candidate_stats` and `causal_edge_stats`; planner-side `generate_lmd_bundle.py` can now consult those learned stats when a DB URL is available, so learned edge/candidate weights can influence future retrieval scoring
- Next later step: broader cohort accumulation and calibration of the learned-weight formulas/status thresholds as real treatment exposures arrive

### Next implementation order

#### 1. Intervention registry + application tracking
Build first because this is the cleanest measurable unit for runtime learning.

Add:
- intervention markdown canon under `intervention-tracking/`
- DB tables for interventions and intervention applications
- scripts to upsert interventions and log when they are applied to a case

Goal:
- make runtime learning use explicit, bounded interventions instead of only freeform notes
- create the measurement substrate needed for LMD evaluation

#### 2. LMD experiment assignment + exposure logging
Build before broad runtime rollout so LMD can be evaluated cleanly.

Add:
- deterministic control/treatment assignment for LMD-eligible cases
- bundle exposure logging
- candidate exposure logging
- experiment / generator / policy version tracking

Goal:
- know exactly which cases got LMD, which learned items were shown, and what later happened

#### 3. Minimal causal-graph substrate
This is where **building the causal graph** should begin.

Build a narrow reviewed v1 first, not a giant auto-generated graph.

Add:
- `qualitative-db/60-causal-map/`
- SQL tables for causal nodes, edges, edge evidence, and case projections
- a small initial node/edge ontology for the highest-density mechanism families already visible in the repo

Recommended v1 scope:
- threshold / touch mechanics
- publication / timing mechanics
- source-of-truth / settlement mechanics
- workflow caution vs path-probability conflicts

Goal:
- create a typed mechanism layer that can later guide LMD retrieval

#### 4. Case-level causal projection
Project reviewed cases into the graph.

Add:
- `case-reviews/<case-key>/causal-projection.json`
- projection scripts that map reviewed notes + signal packets + learning packets into:
  - active nodes
  - candidate edges
  - contested edges
  - required checks

Goal:
- make each reviewed case queryable by mechanism, not only by category/tags/semantics

#### 5. `generate_lmd_bundle.py` with hybrid retrieval
Build LMD retrieval only after interventions and causal projections exist.

Retrieval order should be:
1. structured shortlist by mechanics / source-of-truth / node-edge overlap / intervention applicability
2. semantic rerank inside the shortlist
3. small capped bundle for runtime injection

Goal:
- retrieve by mechanism first, semantics second
- keep runtime bundles small and attributable

#### 6. Runtime injection into researcher pipeline
Once `lmd-bundle.json` exists, inject it into the live researcher runtime.

First target:
- researcher prompt path

Bundle should inject only:
- a few matching reviewed case reviews
- active intervention paths
- required checks
- optional compact causal focus section

Goal:
- turn evaluator learning into real changed behavior in future cases

#### 7. Outcome evaluation + learned weight updates
After enough logged exposures exist, update candidate and graph policy in batch.

Add:
- candidate-level stats
- edge-level stats
- shrunken uplift / cost-adjusted uplift
- learned retrieval weights
- intervention promotion / hold / retire logic

Goal:
- make LMD and the causal map improve through logged outcomes rather than free self-rewriting

### Operating rule for the causal graph

The causal graph should be used primarily as:
- a **mechanism-aware retrieval layer** for LMD
- a **policy/evaluation layer** for interventions and edge usefulness

It should **not** be used as:
- a giant prompt payload
- an unconstrained self-editing knowledge system

### Practical rule of thumb

- evaluator reviews and signals create the reviewed learning substrate
- the causal graph organizes that substrate by mechanism
- LMD turns the organized substrate into a small runtime bundle
- logged outcomes then update both intervention policy and graph-linked retrieval weights

It exists to answer:
- what did a resolved case actually teach us?
- which signals were helpful, misleading, or missing?
- which recurring driver patterns are emerging across cases?
- which pipeline stages, sources, or workflows are helping or hurting?
- what concrete intervention should we test, keep, or reject?

`50-learnings/` is not just a passive postmortem bin.
It is the place where resolved-case evidence is turned into reusable improvements.

## Core architecture

Treat this layer as a bounded learning loop:

1. **Case work happens in `40-research/`**
   - source notes, role-specific findings, assumptions, evidence maps, synthesis, decision handoff

2. **Forecasts and outcomes are tracked in quant systems**
   - forecast decisions, supersession chains, resolutions, scoring, calibration

3. **Resolved cases produce learning artifacts here**
   - especially one case-level review that says what happened, what helped, what misled, and what should change

4. **Cross-case patterns are aggregated here**
   - recurring false signals
   - recurring missed signals
   - recurring driver patterns
   - recurring source or workflow failures

5. **Interventions are tracked explicitly here**
   - prompt changes
   - weighting/routing changes
   - retrieval changes
   - workflow or verification changes

6. **Only durable lessons get promoted outward**
   - `30-drivers/` for reusable causal mechanisms
   - `10-domains/` or `20-entities/` for durable canon updates
   - `00-system/` for workflow or governance changes

This keeps the system recursive without making it uncontrolled.
The loop is: **observe -> review -> aggregate -> intervene -> evaluate -> promote or reject**.

Hard boundary:
- reviewed learnings here may feed proposal generation and intervention evaluation
- they do **not** directly create LMD-recallable graph canon without passing through the causal-map lifecycle policy in `qualitative-db/00-system/methodology/causal-lifecycle-policy.md`

## Folder guide

### `case-reviews/`

The atomic learning unit.

Use for one resolved case at a time.
A good case review should capture:
- what the original question was
- what the pipeline believed or did
- what happened in reality
- what signals were high-signal
- what signals were misleading
- what was missing
- how the miss or success should be classified
- what concrete change, if any, is suggested

Default rule:
- if you only write one learning artifact for a resolved case, write it here first

### `error-patterns/`

Cross-case failure-pattern layer.

Use this when the lesson is no longer about only one case, but about a repeated mistake class.

Current subfolders:
- `false-signals/` = signals that looked important but repeatedly misled the pipeline
- `missed-signals/` = signals that should have been weighted earlier or more heavily

Use these folders to answer:
- which patterns produce recurring overconfidence?
- which patterns are repeatedly underweighted?
- which failure modes show up across market categories?

### `driver-learning/`

Bridge between resolved-case learning and `30-drivers/`.

Use for:
- evaluating whether a proposed driver is real, durable, and reusable
- recording repeated evidence about how an existing driver helped or hurt
- linking case-level observations to possible driver promotion or refinement

Default rule:
- if the lesson is about a causal mechanism that may deserve durable driver treatment later, it belongs here before or alongside promotion work in `30-drivers/`

### `input-quality/`

Use for evidence-quality and artifact-quality lessons that are broader than a single source.

Examples:
- weak provenance patterns
- thin evidence-floor failures
- overuse of low-independence inputs
- poor assumption capture
- missing structured evidence maps when they were needed

### `source-performance/`

Use for source-class and source-specific evaluation.

Examples:
- an official source that is highly reliable but operationally brittle
- a recurring media source that is fast but noisy
- a source family that repeatedly helps in one market class and hurts in another

### `workflow-performance/`

Use for pipeline-stage, handoff, and role-performance lessons.

Examples:
- researcher-role failures or strengths
- synthesis-stage compression problems
- handoff-loss issues
- evaluation-stage blind spots
- routing or escalation behavior that repeatedly helps or hurts

This folder is intentionally workflow-oriented rather than anthropomorphic.
If a lesson is really about one role, state that explicitly inside the note.

### `intervention-tracking/`

Use for explicit improvement actions and their later evaluation.

Examples:
- prompt or contract changes
- retrieval-policy changes
- verification-policy changes
- routing or threshold changes
- category-specific heuristics

A strong intervention note should say:
- what changed
- why it changed
- what problem it was trying to fix
- what evidence supported the change
- how success or failure should later be judged

This is the control surface that turns learning into bounded self-improvement rather than ad hoc drift.

## What belongs here

Use `50-learnings/` for:
- resolved-case reviews
- cross-case error-pattern notes
- driver-learning notes
- source and input-quality evaluation
- workflow and handoff evaluation
- intervention tracking and follow-up evaluation
- conflict lessons after disagreements are resolved enough to judge

## What does not belong here

Do **not** use this folder for:
- active case research that still belongs in `40-research/`
- raw source extraction
- unresolved live disagreements that have not yet been reviewed
- direct canonical driver/entity/domain rewrites
- raw forecast rows or scoring outputs that belong in quant systems

If the material is still provisional or unresolved, keep it in `40-research/` first.
If the material is already durable canon, promote it into the appropriate stable layer instead.

## Role rule

Researchers may read this folder, but ordinary researchers should not treat it as their default working layer.

Normal writers here:
- Orchestrator
- Decision-maker
- other explicitly authorized evaluation / maintenance roles

## Relationship to other layers

- `30-drivers/` = reusable causal mechanisms
- `40-research/` = case-specific evidence and reasoning
- `50-learnings/` = resolved-case review and recursive improvement

Use this distinction:
- if it is about **what is happening in this case right now** -> `40-research/`
- if it is about **what the resolved case taught us afterward** -> `50-learnings/`
- if it is about **how a mechanism usually works across many cases** -> `30-drivers/`

## Promotion rule

`50-learnings/` is where a candidate improvement becomes explicit enough to evaluate.

But it is **not** automatically canon.

Promote outward only when the lesson is:
- durable
- materially useful
- supported by more than one case or by one especially strong case review
- clear enough to survive outside the original case context

## Fast mental model

- `40-research/` = what did we think?
- quant systems = what did we predict and how did it score?
- `50-learnings/` = what did we learn and what should change?
- stable layers = what is now durable enough to reuse by default?
