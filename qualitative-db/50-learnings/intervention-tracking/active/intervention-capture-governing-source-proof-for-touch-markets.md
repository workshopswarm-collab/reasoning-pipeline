---
type: learning_note
learning_type: intervention
learning_scope: cross_case_candidate
case_key:
market_category: polymarket-discovery
domain: crypto
subdomain: threshold_touch_markets
entity:
topic: Capture governing-source proof for source-sensitive touch markets
question:
date_created: 2026-04-15
resolution_date:
evaluation_scope: future_case_runtime
evaluation_target: researcher_prompt
outcome_observed:
decision_taken: candidate_intervention
error_pattern: verification_caution_overweighting_risk
intervention_status: active
application_surface: researcher_prompt
change_kind: verification_rule
intervention_key: capture-governing-source-proof-for-touch-markets
activated_at: 2026-04-15T02:40:00-04:00
hypothesis: In touch/high-style markets with source-sensitive settlement, explicitly requiring governing-source proof capture and distinguishing "not yet verified" from "not yet occurred" should reduce unnecessary probability discounting without weakening settlement discipline.
related_entities: ["polymarket", "binance"]
related_drivers: ["touch-style settlement mechanics", "verification-surface caution"]
upstream_inputs:
  - qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md
downstream_uses: []
promotion_candidates: []
tags: ["learning/intervention", "surface/researcher_prompt", "change_kind/verification_rule", "threshold-touch", "source-truth"]
---

# Capture governing-source proof for touch markets

## What was being evaluated

- Candidate intervention for future source-sensitive threshold-touch / intraperiod-high markets.
- Initial evidence comes from reviewed case `case-20260414-4e668883` and similar mechanism expectations in the recursive-learning plan.

## What the pipeline believed or did

- In the reviewed ETH touch case, the pipeline was directionally correct but appeared mildly underconfident while also lacking structured capture of the exact governing-source event proof.
- The review suggested that verification caution may have been priced too expensively relative to the remaining distance, remaining time, and touch-friendly settlement rules.

## What happened in reality

- The market resolved Yes.
- The evaluator review judged the main missing piece not as generic research weakness but as insufficient structured proof capture for the governing resolution surface.

## Outcome and scoring evidence

- Supporting reviewed case: `case-20260414-4e668883`.
- Focal case forecast: `0.87` vs resolved value `1.0`.
- Reviewed takeaway: separate “not yet verified” from “not yet occurred,” especially in touch-style settlement markets.

## Which inputs were high signal

- Reviewed case evidence that touch-style settlement mechanics and tiny remaining distance mattered more than generic resistance narratives.
- Workflow takeaway that the missing artifact was governing-source proof capture, not generic lack of directional evidence.

## Which inputs were misleading

- Treating incomplete direct proof as if it justified the same discount as low event probability.
- Letting source-of-truth caution remain unstructured rather than forcing a specific proof-capture step.

## What was missing

- A deterministic requirement to identify the governing source and explicitly capture qualifying event proof when the event is plausible or near-complete.
- A runtime distinction between:
  - event not yet occurred
  - event may already have occurred but remains unverified on the governing surface

## Error-pattern classification

- Candidate workflow / verification intervention for recurring settlement-mechanics and verification-caution cases.

## Driver and mechanism takeaways

- This intervention targets cases where touch-friendly mechanics, small threshold distance, and authoritative source sensitivity interact.
- It is meant to improve proof capture and probability calibration, not to weaken settlement rigor.

## Source / input / workflow takeaways

- The likely leverage point is workflow structure, not broader source expansion.
- If this intervention later proves useful, it should manifest as a reusable verification rule rather than ad hoc prompt prose.

## Proposed intervention or hold decision

- Promote to `active` for a narrow controlled rollout on source-sensitive threshold-touch / intraperiod-high-low cases.
- Deterministic code should add required checks for governing-source identification, proof capture, and explicit unverified-vs-not-occurred labeling.
- Revisit status once real treatment exposures accumulate and Step 7 candidate stats become nontrivial.

## Promotion candidates for stable layers

- None yet.

## How this should be reused later

- Revisit when similar touch/source-sensitive cases accumulate.
- If activated, log each application so later cohort-level evaluation can test whether the rule reduces underconfidence or verification-driven delay.
