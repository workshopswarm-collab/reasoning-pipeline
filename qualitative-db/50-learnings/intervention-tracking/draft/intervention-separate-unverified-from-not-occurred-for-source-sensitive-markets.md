---
type: learning_note
learning_type: intervention
learning_scope: cross_case_candidate
case_key:
market_category: mixed-resolution-sensitive
domain: cross-domain
subdomain: source-sensitive_markets
entity:
topic: Separate unverified state from not-occurred state in source-sensitive markets
question:
date_created: 2026-04-15
resolution_date:
evaluation_scope: future_case_runtime
evaluation_target: researcher_prompt
outcome_observed:
decision_taken: candidate_intervention
error_pattern: verification_state_conflation
intervention_status: draft
application_surface: researcher_prompt
change_kind: prompt_guardrail
intervention_key: separate-unverified-from-not-occurred-for-source-sensitive-markets
hypothesis: For source-sensitive markets, explicitly separating event-state from verification-state should reduce cases where incomplete proof is priced as if the event itself is unlikely.
related_entities: ["polymarket"]
related_drivers: ["source-of-truth handling", "settlement mechanics", "verification caution"]
upstream_inputs:
  - qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md
downstream_uses: []
promotion_candidates: []
tags: ["learning/intervention", "surface/researcher_prompt", "change_kind/prompt_guardrail", "source-truth", "verification-state"]
---

# Separate unverified from not occurred for source-sensitive markets

## What was being evaluated

- Candidate prompt-guardrail intervention for markets where resolution depends on a specific authoritative source or governing proof surface.

## What the pipeline believed or did

- In the reviewed touch-market case, incomplete direct proof capture appears to have been treated too similarly to evidence that the event had probably not happened.

## What happened in reality

- The market resolved Yes, and the evaluator review suggested the workflow needed a sharper distinction between:
  - the event not having occurred
  - the event potentially having occurred but not yet being directly verified on the governing source

## Outcome and scoring evidence

- Primary seed evidence: `case-20260414-4e668883`.
- The reviewed lesson was not that verification discipline is unnecessary; it was that verification uncertainty should be represented separately from event-probability uncertainty.

## Which inputs were high signal

- The reviewed case’s source-sensitive settlement framing.
- The explicit underconfidence / workflow lesson in the evaluator review.

## Which inputs were misleading

- Letting unresolved verification state act as a broad negative weight on the underlying event probability without forcing the distinction to be spelled out.

## What was missing

- A prompt-level guardrail requiring the analyst to label event-state and verification-state separately whenever source-sensitive settlement is material.

## Error-pattern classification

- Candidate cross-case intervention for verification-state conflation.

## Driver and mechanism takeaways

- This is primarily a representation/control intervention: it does not tell the model to be more bullish; it tells it not to compress two different uncertainties into one number without explanation.

## Source / input / workflow takeaways

- The likely leverage point is a prompt structure requirement that asks explicitly whether the evidence gap is about the world or about proof capture.

## Proposed intervention or hold decision

- Keep as `draft` pending more than one reviewed case or an explicit controlled rollout.

## Promotion candidates for stable layers

- None yet.

## How this should be reused later

- Reconsider when future source-sensitive cases show similar underconfidence or proof-state confusion.
