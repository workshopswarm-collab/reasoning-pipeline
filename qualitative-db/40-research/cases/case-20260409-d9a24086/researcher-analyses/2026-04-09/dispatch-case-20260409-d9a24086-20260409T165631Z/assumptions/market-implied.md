---
type: assumption_note
case_key: case-20260409-d9a24086
dispatch_id: dispatch-case-20260409-d9a24086-20260409T165631Z
research_run_id: bd395927-510f-48c2-96b9-38cc2cf15695
analysis_date: 2026-04-09
persona: market-implied
domain: economics
subdomain: macro-data-and-indicators
entity: bureau-of-labor-statistics
topic: will-monthly-inflation-increase-by-0.8-or-more-in-march
question: "Will monthly inflation increase by 0.8% or more in March?"
driver: macro
date_created: 2026-04-09
agent: market-implied
status: active
certainty: medium
importance: high
time_horizon: immediate
related_entities: ["bureau-of-labor-statistics"]
related_drivers: ["macro", "sentiment"]
proposed_entities: []
proposed_drivers: ["bls-rounding-threshold-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-analyses/2026-04-09/dispatch-case-20260409-d9a24086-20260409T165631Z/personas/market-implied.md"]
tags: ["assumption-note", "cpi", "threshold", "rounding"]
---

# Assumption

The market’s near-95% Yes price assumes that the March 2026 official BLS seasonally adjusted CPI-U month-over-month reading will land clearly enough above the 0.8% threshold that rounding to one decimal does not turn an apparent edge into a miss.

## Why this assumption matters

The contract is binary and resolves on a one-decimal official BLS figure, so threshold/rounding risk matters more than in a continuous inflation forecast.

## What this assumption supports

- A high Yes probability despite the event not yet being officially released.
- The interpretation that public nowcasts above 0.8% justify a strongly positive market stance.
- The view that the market may be efficiently aggregating threshold-sensitive information.

## Evidence or logic behind the assumption

- The Cleveland Fed nowcast for March 2026 CPI is 0.84 month-over-month, updated 2026-04-09.
- The nowcast is explicitly seasonally adjusted and month-over-month, matching the contract’s target metric directionally.
- BLS is scheduled to publish the official March 2026 CPI release on April 10, 2026 at 8:30 AM ET, so the market is close to resolution and likely concentrated on last-mile forecast quality.

## What would falsify it

- A later credible preview or leak indicating the official BLS CPI-U print is below 0.75 before rounding.
- Official BLS release at 0.7% or lower.
- Evidence that market participants are misreading non-seasonally adjusted data or another inflation series as the settlement metric.

## Early warning signs

- Late contextual sources emphasizing downside surprises in shelter, gasoline, or core services.
- Clarifications showing that the public nowcast most traders watch is not aligned to the settlement metric.
- Signs the market price is being driven by narrative momentum rather than metric-specific evidence.

## What changes if this assumption fails

The Yes probability should fall materially, because the main pro-market case is not that inflation is merely high, but that the exact official BLS seasonally adjusted monthly CPI-U print clears the binary threshold used for settlement.

## Notes that depend on this assumption

- Main market-implied finding for this run.
- Cleveland Fed source note.
- Any later synthesis that interprets the current price as efficient rather than overextended.