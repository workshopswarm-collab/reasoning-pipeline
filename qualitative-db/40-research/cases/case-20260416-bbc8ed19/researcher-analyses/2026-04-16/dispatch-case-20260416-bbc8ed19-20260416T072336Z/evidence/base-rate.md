---
type: evidence_map
case_key: case-20260416-bbc8ed19
dispatch_id: dispatch-case-20260416-bbc8ed19-20260416T072336Z
research_run_id: fe68063c-5ebd-4e0c-8741-db8f1a15ca20
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-20
question: "Will the price of Bitcoin be above $72,000 on April 20?"
driver: reliability
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-bbc8ed19/researcher-analyses/2026-04-16/dispatch-case-20260416-bbc8ed19-20260416T072336Z/personas/base-rate.md"]
tags: ["evidence-map", "btc", "base-rate"]
---

# Summary

This evidence map nets a short-horizon threshold market where the main question is not whether BTC rises, but whether it avoids a roughly 4% drop by the resolving Binance minute.

## Question being evaluated

Will Binance BTCUSDT's 12:00 ET one-minute candle on 2026-04-20 have a final close above 72000?

## Current lean

Lean Yes at high but not extreme confidence.

## Prior / starting view

Starting prior: if BTC is already several percent above the threshold with only four calendar days left, the base rate should favor staying above unless there is strong case-specific negative evidence.

## Evidence supporting the claim

- Current Binance BTCUSDT spot is 74909.72, already above the threshold by about 4.0%.
  - direct
  - high weight
  - matters because the contract only needs threshold retention, not a further breakout
- In a 365-day Binance daily sample, about 83.7% of 4-day forward windows exceeded the decline tolerance needed to stay above 72k from today's level.
  - contextual
  - medium weight
  - matters because it provides an outside-view retention rate for the relevant horizon
- 83.3% of sampled daily closes were themselves above 72k.
  - contextual
  - medium weight
  - matters because 72k is not an unusually high tail threshold relative to the recent regime

## Evidence against the claim

- The exact contract resolves on a one-minute Binance candle at a specific noon ET timestamp, not on a daily close.
  - direct contract mechanic
  - medium weight
  - matters because intraday volatility can produce a transient resolving print below threshold even if the broader daily regime looks strong
- BTC can move more than 4% over a few days, especially in crypto.
  - contextual
  - medium weight
  - matters because the current cushion is meaningful but not huge
- Same-source dependence is high because both settlement mechanics and historical context come from Binance surfaces.
  - provenance concern
  - low to medium weight

## Ambiguous or mixed evidence

- The market itself prices Yes around 84.5%, which is close to the simple historical retention estimate. That means there is little obvious base-rate mispricing to exploit.

## Conflict between inputs

No material factual conflict found in this run. The main issue is weighting: how much to discount daily-base-rate evidence because settlement is one exact one-minute candle.

## Key assumptions

- Current trading regime remains broadly stable through the resolution window.
- No large exogenous shock dominates the short-horizon base rate.
- Binance remains an operationally usable settlement surface.

## Key uncertainties

- Whether a weekend or macro headline creates a fast downdraft before noon ET on April 20.
- Whether intraday noise around the exact resolving minute is larger than the daily-close framing suggests.

## Disconfirming signals to watch

- BTC breaking and holding below 72k before resolution.
- Accelerating downside momentum into April 20.
- Evidence of Binance-specific pricing or operational anomalies.

## What would increase confidence

- Continued trading above 73-74k into April 19-20.
- Additional check of intraday realized volatility near comparable windows.

## Net update logic

The starting outside-view already favored Yes because spot was above threshold. The historical 3-5 day retention rates supported that prior rather than overturning it. The main downweight came from contract narrowness: a one-minute resolving print is noisier than a daily close, so the final estimate stays slightly below the simple raw retention number.

## Suggested downstream use

- orchestrator synthesis input
- forecast update
