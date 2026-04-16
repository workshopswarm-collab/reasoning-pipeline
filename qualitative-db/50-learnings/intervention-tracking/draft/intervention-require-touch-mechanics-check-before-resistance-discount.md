---
type: learning_note
learning_type: intervention
learning_scope: cross_case_candidate
case_key:
market_category: threshold-touch
domain: crypto
subdomain: threshold_touch_markets
entity:
topic: Require touch-mechanics check before resistance discount
question:
date_created: 2026-04-15
resolution_date:
evaluation_scope: future_case_runtime
evaluation_target: researcher_prompt
outcome_observed:
decision_taken: candidate_intervention
error_pattern: touch_mechanics_underweighting
intervention_status: draft
application_surface: researcher_prompt
change_kind: weighting_rule
intervention_key: require-touch-mechanics-check-before-resistance-discount
hypothesis: In threshold-touch / intraperiod high-low markets, forcing an explicit touch-mechanics check before leaning on narrative resistance should reduce underweighting of markets where any qualifying touch resolves Yes.
related_entities: ["polymarket", "binance"]
related_drivers: ["touch-style settlement mechanics", "time-to-threshold", "path probability vs verification caution"]
upstream_inputs:
  - qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md
downstream_uses: []
promotion_candidates: []
tags: ["learning/intervention", "surface/researcher_prompt", "change_kind/weighting_rule", "threshold-touch", "settlement-mechanics"]
---

# Require touch-mechanics check before resistance discount

## What was being evaluated

- Candidate weighting/analysis intervention for threshold-touch and similar intraperiod high-low markets.

## What the pipeline believed or did

- The reviewed ETH touch case appears to have leaned too much on generic resistance/caution framing without first forcing a clear settlement-mechanics analysis of what counts as a Yes.

## What happened in reality

- The market resolved Yes.
- The evaluator review suggested that distance-to-threshold, remaining time, and any-touch settlement mechanics deserved more explicit foregrounding before discounting probability based on generic reversal narratives.

## Outcome and scoring evidence

- Primary seed evidence: `case-20260414-4e668883`.
- The reviewed forecast was directionally correct but likely too conservative relative to the market mechanics.

## Which inputs were high signal

- The reviewed case’s emphasis on small remaining distance and touch-friendly mechanics.
- The distinction between path probability and source-verification caution.

## Which inputs were misleading

- Generic technical resistance language when it is not clearly tied to the contract’s actual settlement rule.

## What was missing

- A mandatory check that asks: does any qualifying touch resolve the contract, and if so, have we explicitly evaluated distance, time remaining, and likely path volatility before applying a resistance discount?

## Error-pattern classification

- Candidate cross-case intervention for touch-mechanics underweighting.

## Driver and mechanism takeaways

- This intervention is meant to ensure the contract mechanic is evaluated before adding discretionary conservative discounts.

## Source / input / workflow takeaways

- The leverage point is prompt/checklist structure, not broader source retrieval.

## Proposed intervention or hold decision

- Keep as `draft` until it has either recurrent reviewed support or a controlled experiment path.

## Promotion candidates for stable layers

- None yet.

## How this should be reused later

- Revisit for future threshold-touch / intraperiod-high-low markets, especially where the remaining distance is small and time remains nontrivial.
