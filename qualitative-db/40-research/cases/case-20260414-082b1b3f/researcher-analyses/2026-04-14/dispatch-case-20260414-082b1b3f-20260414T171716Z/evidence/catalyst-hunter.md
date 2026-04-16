---
type: evidence_map
case_key: case-20260414-082b1b3f
dispatch_id: dispatch-case-20260414-082b1b3f-20260414T171716Z
research_run_id: 0d8c8713-f67b-4fe7-a3e1-9d1e0689468d
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: spot-market
entity: sol
topic: will-the-binance-sol-usdt-12-00-et-1-minute-candle-close-above-80-on-april-17-2026
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 17, 2026?"
driver: operational-risk
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-082b1b3f/researcher-analyses/2026-04-14/dispatch-case-20260414-082b1b3f-20260414T171716Z/personas/catalyst-hunter.md"]
tags: ["catalyst-comparison", "timing-risk", "settlement-risk"]
---

# Summary

This evidence map shows that the main catalyst conclusion is the lack of a dominant scheduled catalyst before settlement, leaving ordinary crypto volatility and exchange-specific settlement mechanics as the key drivers.

## Question being evaluated

Will Binance SOL/USDT close above 80 on the 1-minute candle for 2026-04-17 12:00 ET?

## Current lean

Lean Yes, but less confidently than the market.

## Prior / starting view

Starting view was that a current price around 85 with only a few days to settlement should make Yes the base case unless contract mechanics or recent volatility showed meaningful fragility.

## Evidence supporting the claim

- Current Binance spot is about 85.31.
  - source: case source notes using Binance API
  - why it matters: the market is already in the money by roughly 6%
  - direct or indirect: direct
  - weight: high

- Recent 1-minute prices are stable around 85.2 to 85.3.
  - source: Binance 1m klines
  - why it matters: no immediate sign of threshold stress
  - direct or indirect: direct
  - weight: medium

- Recent daily closes recovered above 80 after early-April weakness.
  - source: Binance 1d klines
  - why it matters: current regime is above the strike, so No needs a renewed drawdown rather than status quo continuation
  - direct or indirect: direct
  - weight: medium

- No high-information scheduled Solana-specific catalyst was verified before settlement.
  - source: research pass outcome and absence of identified event in this run
  - why it matters: without a known catalyst, repricing path is more likely to be ordinary volatility than a specific event shock
  - direct or indirect: indirect
  - weight: medium

## Evidence against the claim

- Recent Binance history includes sub-80 prints within the same month.
  - source: Binance 1d klines and prior case source notes
  - why it matters: a move below the threshold is recent and plausible, not tail-only
  - direct or indirect: direct
  - weight: high

- The contract resolves on one exact minute, not a daily average or end-of-day close.
  - source: Polymarket rules
  - why it matters: path and timestamp risk matter more than medium-term thesis confidence
  - direct or indirect: direct
  - weight: high

- Exchange-specific or market-wide shock could matter more than Solana fundamentals over this short window.
  - source: contract structure plus crypto market behavior
  - why it matters: a modest downside move is enough to flip resolution
  - direct or indirect: indirect
  - weight: medium

## Ambiguous or mixed evidence

- Recent rebound into mid-80s can be read as regained support or as a setup where a routine pullback is still enough to break 80.
- Lack of a known catalyst reduces event risk but does not eliminate macro or weekend-style volatility risk.

## Conflict between inputs

There is no major factual conflict. The main disagreement is weighting-based: whether a 6% cushion over a few days deserves something near 90%+ confidence or something a bit lower because of single-minute settlement risk.

## Key assumptions

- No major downside catalyst emerges before settlement.
- Binance API prices remain representative of the eventual settlement surface.
- Crypto market conditions remain roughly rangebound rather than sharply risk-off.

## Key uncertainties

- Whether a macro or exchange-specific headline appears in the final 48-72 hours.
- Whether SOL beta to broader crypto rises into settlement.
- Whether the exact 12:00 ET minute proves more fragile than current spot suggests.

## Disconfirming signals to watch

- SOL trading back near 82-83 before April 17.
- Sharp BTC-led selloff dragging altcoins lower.
- Binance-specific operational disruption.

## What would increase confidence

- Continued SOL trading above 84 into April 16-17.
- No adverse market-wide or exchange-specific headlines.
- Additional direct confirmation that Binance UI candle and API outputs align cleanly for the relevant minute.

## Net update logic

The evidence keeps the lean on Yes because current price is comfortably above the strike and no strong negative scheduled catalyst was found. But the combination of recent sub-80 history and exact one-minute settlement timing argues for trimming confidence below the market’s extreme pricing.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- follow-up investigation only if new catalyst headlines emerge before settlement