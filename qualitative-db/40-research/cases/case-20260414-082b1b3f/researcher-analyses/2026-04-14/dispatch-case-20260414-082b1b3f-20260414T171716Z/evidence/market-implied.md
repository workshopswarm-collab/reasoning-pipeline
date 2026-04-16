---
type: evidence_map
case_key: case-20260414-082b1b3f
dispatch_id: dispatch-case-20260414-082b1b3f-20260414T171716Z
research_run_id: 610ec326-1972-404d-8e1d-a774adfab64a
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: spot-market
entity: sol
topic: will-the-binance-sol-usdt-1-minute-candle-at-12-00-pm-et-on-2026-04-17-close-above-80
question: "Will the Binance SOL/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 80?"
driver: reliability
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["market-implied", "evidence-netting", "binance"]
---

# Summary

The market's extreme Yes pricing is mostly explained by current Binance spot being comfortably above the 80 threshold, but the contract remains vulnerable to short-horizon crypto volatility because settlement depends on one exact minute close.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle corresponding to 12:00 PM ET on 2026-04-17 close above 80?

## Current lean

Lean Yes, but slightly less confident than the market.

## Prior / starting view

Start from the market's 88.5% implied probability as an information-rich prior.

## Evidence supporting the claim

- **Live Binance spot above threshold by ~5.25 points**  
  - Source: Binance API source note.
  - Why it matters: the market only needs SOL to remain above a level it has already cleared.
  - Direct or indirect: direct.
  - Weight: high.

- **5-minute average consistent with sampled 1-minute closes**  
  - Source: Binance API source note.
  - Why it matters: reduces the odds that the observed spot level is a transient print artifact.
  - Direct or indirect: direct.
  - Weight: medium.

- **Contract wording is simple and venue-specific**  
  - Source: Polymarket rules.
  - Why it matters: limits ambiguity; if Binance is near 85 now, the market's high Yes price has a straightforward rationale.
  - Direct or indirect: direct.
  - Weight: medium.

## Evidence against the claim

- **Single-minute-close exposure**  
  - Source: Polymarket rules.
  - Why it matters: this is not a daily average or end-of-day settle; a brief selloff at the exact noon ET minute can defeat Yes.
  - Direct or indirect: direct.
  - Weight: high.

- **Only modest cushion relative to crypto volatility**  
  - Source: Binance spot sample plus general market context.
  - Why it matters: a ~6% move over roughly three days is not an extraordinary downside move for SOL.
  - Direct or indirect: mixed.
  - Weight: medium-high.

- **Exchange-specific operational dependence**  
  - Source: contract rules and driver context.
  - Why it matters: Binance-specific pricing or operational anomalies could matter even if broader SOL pricing elsewhere looks fine.
  - Direct or indirect: indirect.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- Secondary web snippets suggest SOL price context in the mid-80s, but they are less authoritative than direct Binance API pulls.
- No strong independent evidence was found suggesting imminent downside, but absence of such evidence is not strong proof in a short-horizon crypto market.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: whether the current cushion above 80 deserves something close to 90% or something a bit lower once one-minute timing risk is respected.

## Key assumptions

- Current spot level is a meaningful anchor for the next ~3 days.
- No major risk-off shock or Binance-specific disruption occurs before settlement.
- Noon ET mapping in the contract reflects the minute that Binance data can unambiguously support at settlement.

## Key uncertainties

- Magnitude of short-horizon SOL volatility into April 17.
- Whether the market has better tacit information about near-term crypto flows than is visible from a quick public-source check.

## Disconfirming signals to watch

- SOL trending down toward 80 by April 16-17.
- Broad crypto drawdown led by BTC/ETH.
- Any Binance operational event affecting spot data confidence.

## What would increase confidence

- Continued Binance trading above mid-80s into April 16-17.
- Independent context showing low realized volatility or strong market support into the event window.
- Another verification pull closer to settlement still showing comfortable distance from 80.

## Net update logic

The evidence keeps the lean on Yes because spot is already above the threshold on the named venue, which is the market's strongest point. The discount versus market comes from the contract's one-minute timing sensitivity and the fact that a ~6% downside move in SOL over several days is possible enough that 88.5% feels slightly rich.

## Suggested downstream use

Use as orchestrator synthesis input and as an auditable record of why a mildly below-market Yes view was taken despite respecting the market prior.
