---
type: evidence_map
case_key: case-20260416-653ab0f8
dispatch_id: dispatch-case-20260416-653ab0f8-20260416T090226Z
research_run_id: 328768aa-288b-4c05-a3d1-89c31bf5092f
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: "btc above 72000 on apr 18"
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on Apr 18 close above 72000?"
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
downstream_uses: ["base-rate-finding"]
tags: ["evidence-map", "short-horizon", "contract-interpretation"]
---

# Summary

Base-rate lean is Yes, but slightly below market confidence. The key outside-view claim is that staying above 72k for another two days is more likely than not given current spot context near 75k, yet an exact one-minute exchange-specific settlement should trade below certainty.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on Apr 18, 2026 have a final close above 72,000?

## Current lean

Yes, with probability below the market's 88% but still clearly above 50%.

## Prior / starting view

Starting outside-view prior for a two-day crypto threshold market with exact minute settlement was closer to the 70-80% range, not high-80s, unless current spot sat materially above the threshold.

## Evidence supporting the claim

- CNBC spot context showed BTC around 75k with day low around 74.5k.
  - direct/contextual: contextual, not settlement-direct
  - why it matters: threshold is several percent below current spot
  - weight: high
- Polymarket ladder shape was coherent across nearby strikes: 70k ~97%, 72k ~88%, 74k ~62%, 76k ~28%.
  - direct/contextual: direct for market pricing, indirect for truth
  - why it matters: suggests 72k is inside the expected near-term distribution rather than a heroic target
  - weight: medium-high
- Contract horizon is short (~48 hours).
  - direct/contextual: structural/base-rate reasoning
  - why it matters: absent a new shock, large downside regime shifts are less common than continued range trading over two days
  - weight: medium

## Evidence against the claim

- Settlement is a single exact Binance one-minute close at noon ET, not a daily close or average.
  - direct/contextual: direct contract interpretation
  - why it matters: microstructure and intraday volatility can flip outcomes even if broader trend remains positive
  - weight: high
- BTC is volatile enough that a ~4% move lower in two days is entirely plausible.
  - direct/contextual: structural/base-rate reasoning
  - why it matters: the cushion above 72k is meaningful but not huge in crypto terms
  - weight: high
- Direct Binance API verification was not available through the tooling used here.
  - direct/contextual: verification limitation
  - why it matters: leaves some source mismatch risk between contextual spot references and the actual settlement venue
  - weight: medium

## Ambiguous or mixed evidence

- CoinDesk fetch was not numerically useful; it neither supported nor contradicted the main view.
- Market pricing itself may embed stronger exchange-specific knowledge, but it can also overstate certainty in near-threshold ladder contracts.

## Conflict between inputs

There was no strong factual conflict across sources. The main disagreement is weighting-based: how much discount should be applied for exact-minute settlement risk relative to current spot cushion.

## Key assumptions

- Current mid-70k regime broadly persists into Apr 18.
- Binance BTC/USDT remains reasonably aligned with broader BTC spot references.
- No new macro or crypto-specific shock produces a rapid drawdown.

## Key uncertainties

- Exact Binance BTC/USDT price path between now and settlement
- Whether noon ET on Apr 18 coincides with a volatile macro/news window
- Whether exchange-specific prints diverge enough to matter around the final minute

## Disconfirming signals to watch

- BTC trades down through 74k and approaches 72k before settlement
- Apr 18 72k and 74k ladder contracts both reprice sharply lower
- Any Binance-specific operational or pricing anomaly

## What would increase confidence

- Direct Binance API/page confirmation that BTC/USDT remains comfortably above 72k through Apr 17 and Apr 18 morning
- Evidence of subdued realized volatility into the settlement window

## Net update logic

The starting view was that exact-minute crypto threshold contracts deserve caution. Current price context several percent above the threshold shifted the lean to Yes, but not enough to fully endorse an 88% probability because the contract is still one venue, one pair, one minute.

## Suggested downstream use

Use this as synthesis input showing a base-rate case for Yes with moderate discount versus market confidence, mainly due to narrow resolution mechanics rather than a bearish directional thesis.