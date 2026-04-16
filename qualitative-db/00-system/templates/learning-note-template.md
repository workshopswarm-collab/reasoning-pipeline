---
type: learning_note
learning_type:
learning_scope:
case_key:
market_category:
domain:
subdomain:
entity:
topic:
question:
date_created:
resolution_date:
evaluation_scope:
evaluation_target:
outcome_observed:
decision_taken:
error_pattern:
intervention_status:
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
promotion_candidates: []
tags: []
---

# Learning Note

Use this template for artifacts in `qualitative-db/50-learnings/`.

It works best for:
- resolved-case reviews in `case-reviews/`
- cross-case pattern notes in `error-patterns/`
- driver-evaluation notes in `driver-learning/`
- source/input/workflow evaluations
- intervention notes in `intervention-tracking/`

## What was being evaluated

State the original case, question, workflow, source family, driver, or intervention.

## What the pipeline believed or did

Describe what the pipeline actually concluded, weighted, routed, or changed.

## What happened in reality

State the observed outcome, resolved truth, or later evidence that matters for evaluation.

## Outcome and scoring evidence

Record the most relevant quantitative or operational evidence:
- forecast probability or recommendation
- resolved outcome
- score or calibration signal when available
- timing or settlement details that mattered

## Which inputs were high signal

List the sources, findings, assumptions, drivers, or workflow steps that helped.

## Which inputs were misleading

List the sources, findings, assumptions, drivers, or workflow steps that pushed the pipeline the wrong way.

## What was missing

State the evidence, framing, verification step, or workflow behavior that would have improved the outcome.

## Error-pattern classification

Classify the main learning pattern as precisely as you can.

Examples:
- wrong-direction call
- underconfidence
- overconfidence
- false signal overweighted
- missed signal underweighted
- settlement-mechanics miss
- timing miss
- source-quality failure
- workflow / handoff failure
- driver misattribution

## Driver and mechanism takeaways

State what this note teaches about recurring causal mechanisms.
If the lesson might justify a new or revised durable driver, say so explicitly.

## Source / input / workflow takeaways

Explain whether source quality, evidence selection, provenance handling, handoffs, or workflow structure helped or hurt.

## Proposed intervention or hold decision

State what should happen next.

Examples:
- no change needed
- monitor for recurrence
- add a verification requirement
- change a prompt / contract
- adjust retrieval or routing
- create a driver-learning follow-up
- promote a durable lesson into a stable layer

## Promotion candidates for stable layers

List lessons that may deserve promotion into `30-drivers/`, `10-domains/`, `20-entities/`, or `00-system/` after review.

## How this should be reused later

State how a future evaluator, decision-maker, or maintenance pass should use this note.
