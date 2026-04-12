---
type: evidence_map
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
status: draft
confidence: medium
conflict_status: low-direct-conflict-high-threshold-risk
action_relevance: high
related_entities: ["bureau-of-labor-statistics"]
related_drivers: ["macro", "sentiment"]
proposed_entities: []
proposed_drivers: ["bls-rounding-threshold-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-analyses/2026-04-09/dispatch-case-20260409-d9a24086-20260409T165631Z/personas/market-implied.md"]
tags: ["evidence-map", "cpi", "market-implied"]
---

# Summary

The market has a strong pro-Yes case because a reputable and current public nowcast sits above the threshold, but the price still appears somewhat overextended because the threshold is binary, the official source has not yet printed, and the contract resolves on the BLS one-decimal seasonally adjusted CPI-U value.

## Question being evaluated

Will the official BLS one-month percent change in the seasonally adjusted CPI-U for March 2026 be 0.8% or more?

## Current lean

Lean Yes, but with less confidence than the market price implies.

## Prior / starting view

Starting from the market prior, the default view was that traders may already be keying off a late-stage nowcast or preview that points clearly above the threshold.

## Evidence supporting the claim

- Cleveland Fed inflation nowcast (directly relevant contextual source): March 2026 CPI nowcast is 0.84 month-over-month, updated 04/09.
  - Why it matters causally: this is the clearest public metric that could justify a near-resolution Yes bid.
  - Direct vs indirect: contextual, not settlement-direct.
  - Weight: high.
- Cleveland Fed methodology states the CPI nowcast is seasonally adjusted month-over-month.
  - Why it matters causally: aligns the model output with the contract’s target metric better than many casual inflation references would.
  - Direct vs indirect: contextual/technical.
  - Weight: medium-high.
- BLS release timing is one day away / next morning, making late-stage public nowcasts highly salient to price formation.
  - Why it matters causally: when resolution is close, good public signals can compress uncertainty fast.
  - Direct vs indirect: indirect market-structure support.
  - Weight: medium.

## Evidence against the claim

- The governing BLS print is not out yet.
  - Why it matters causally: the contract resolves on the official BLS number, not on a nowcast.
  - Direct vs indirect: direct resolution risk.
  - Weight: high.
- The threshold is very close to the contextual estimate: 0.84 versus a 0.8 cutoff with one-decimal official reporting.
  - Why it matters causally: small model or realization error can flip a near-certain-looking trade into a loss.
  - Direct vs indirect: direct contract-interpretation / threshold risk.
  - Weight: high.
- Evidence independence is limited because the strongest public support is one prominent nowcast plus the official BLS settlement surface rather than several independent pre-release indicators all saying the same thing.
  - Why it matters causally: a single favored public forecast can be over-weighted.
  - Direct vs indirect: contextual.
  - Weight: medium.

## Ambiguous or mixed evidence

- Market price itself may reflect efficient aggregation of private trader synthesis, but that same price could also reflect overconfidence around a single threshold-adjacent forecast.
- February BLS CPI was only 0.3% m/m SA, which is not directly predictive here but reminds us that recent prints can differ meaningfully from late nowcasts.

## Conflict between inputs

There is no major factual conflict between sources reviewed. The disagreement is interpretive and weighting-based: how much confidence should be assigned to a 0.84 public nowcast when settlement requires a one-decimal BLS official print at or above 0.8.

## Key assumptions

- The Cleveland Fed nowcast is the main public information anchor behind the current market price.
- The nowcast is close enough to the settlement metric that it deserves substantial weight.
- No late-breaking information materially undercuts the nowcast before the BLS release.

## Key uncertainties

- Final BLS realized seasonally adjusted monthly CPI-U for March 2026.
- Whether market participants are embedding additional private or harder-to-observe information beyond the public nowcast.
- Exact threshold sensitivity due to one-decimal official reporting.

## Disconfirming signals to watch

- Any credible late preview pointing to 0.7% or lower.
- Official BLS release below 0.8%.
- Evidence that widely cited nowcasts are misaligned with the contract metric.

## What would increase confidence

- Another independent and credible pre-release forecast also clearly above 0.8.
- Direct pre-release evidence on the BLS seasonally adjusted monthly CPI-U headline pointing above the threshold.
- A wider buffer than 0.84 versus 0.8.

## Net update logic

Starting from the market prior, the Cleveland Fed nowcast is strong enough to justify a clear Yes lean. But the final estimate stays below the market because the best public support sits only marginally above the threshold and does not eliminate official-print or rounding-adjacent risk.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- retrospective evaluation of how much weight to place on public nowcasts when the contract threshold is near the forecast