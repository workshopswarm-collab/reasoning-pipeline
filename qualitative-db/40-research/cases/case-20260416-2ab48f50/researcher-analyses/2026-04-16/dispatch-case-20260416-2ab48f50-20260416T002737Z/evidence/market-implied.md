---
type: evidence_map
case_key: case-20260416-2ab48f50
dispatch_id: dispatch-case-20260416-2ab48f50-20260416T002737Z
research_run_id: 0de08f8c-11d2-43fb-9216-f99ed04303e0
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
date_created: 2026-04-15
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["intraday-crypto-volatility-around-thresholds"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-2ab48f50/researcher-analyses/2026-04-16/dispatch-case-20260416-2ab48f50-20260416T002737Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "market-implied"]
driver:
---

# Summary

This evidence map nets a simple threshold case where contract mechanics matter, current spot is modestly favorable to Yes, and the main remaining uncertainty is ordinary crypto volatility into the specified Binance candle.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 17 close above 74,000?

## Current lean

Lean Yes, but only moderately.

## Prior / starting view

Starting from the market price, the baseline view was that Yes was more likely than not but far from locked, because the threshold sat close to live BTC spot.

## Evidence supporting the claim

- Polymarket strike ladder and assigned current price: around 61-62% for 74k, with 72k much higher and 76k much lower.
  - Directness: direct for market-implied baseline.
  - Why it matters: suggests the crowd is pricing a plausible but not dominant buffer above 74k.
  - Weight: high.
- Binance ticker spot check above threshold at 74,589.27.
  - Directness: direct to source-of-truth venue, though not at resolution timestamp.
  - Why it matters: the contract is currently in-the-money on the named settlement venue.
  - Weight: high.
- CoinGecko spot check at 74,530.
  - Directness: contextual/independent cross-check.
  - Why it matters: supports that Binance is not obviously showing a weird isolated print.
  - Weight: medium.

## Evidence against the claim

- The edge over the threshold is small, under 1% at capture.
  - Directness: direct from spot-vs-threshold comparison.
  - Why it matters: BTC can easily move more than that before noon ET next day.
  - Weight: high.
- Settlement uses one specific 1-minute Binance candle close.
  - Directness: direct from contract rules.
  - Why it matters: path dependence is high; even if BTC spends most of the period above 74k, a brief move below at the precise candle close resolves No.
  - Weight: high.

## Ambiguous or mixed evidence

- The smooth ladder suggests efficiency, but it can also mean everyone is extrapolating the same short-term spot level rather than possessing differentiated edge.

## Conflict between inputs

No major factual conflict. The main issue is weighting: how much confidence to put on current spot being above threshold versus the fragility of a single-minute timestamped settlement.

## Key assumptions

- No large exchange-specific distortion on Binance BTCUSDT.
- No major catalyst before settlement that overwhelms ordinary overnight volatility.
- The displayed market ladder is a decent aggregation of current information rather than stale flow.

## Key uncertainties

- Overnight BTC volatility magnitude and direction.
- Whether Binance candle behavior around noon ET differs from broad spot path in a way that matters for a one-minute close.

## Disconfirming signals to watch

- BTCUSDT decisively slipping below 74k on Binance.
- Divergence between Binance and broader BTC spot.
- New operational issues affecting Binance data or trading.

## What would increase confidence

- Repeated spot checks showing BTC maintaining a wider cushion above 74k.
- Evidence that no major macro or crypto catalyst is scheduled before resolution.

## Net update logic

Current spot being above the threshold makes the market's >50% Yes pricing look sensible. But the small margin over 74k and single-minute settlement mechanics cap confidence. Net result: slight lean above the market, not a strong disagreement.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input; the main lesson is that this looks like a market-efficiency / threshold-volatility case, not an obvious anti-market opportunity.