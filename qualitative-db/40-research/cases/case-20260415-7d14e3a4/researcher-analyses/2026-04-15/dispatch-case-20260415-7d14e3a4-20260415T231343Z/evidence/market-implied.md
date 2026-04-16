---
type: evidence_map
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
research_run_id: 8e3762bf-5ed8-45f0-a13c-e1f786758034
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-19
question: "Will the price of Bitcoin be above $72,000 on April 19?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-7d14e3a4/researcher-analyses/2026-04-15/dispatch-case-20260415-7d14e3a4-20260415T231343Z/personas/market-implied.md"]
tags: ["market-implied", "threshold-market", "audit"]
---

# Summary

The netted evidence favors respecting the market's bullish lean, but with some discount for short-horizon crypto volatility and the narrow settlement minute.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-19 have a final close above $72,000?

## Current lean

Yes is more likely than not by a wide margin, but slightly less certain than the market's 86.5% price implies.

## Prior / starting view

Starting view anchored to market price: 86.5% yes.

## Evidence supporting the claim

- Binance spot around $74,695 with recent 1m closes in the same region.
  - Source: `2026-04-15-market-implied-binance-btcusdt-live-and-kline.md`
  - Why it matters: direct venue/pair alignment; current level is already ~$2.7k above strike.
  - Direct or indirect: direct for current state, indirect for final resolution.
  - Weight: high.
- Polymarket ladder and contract text place the 72k outcome around 87% yes and define the exact settlement mechanism.
  - Source: `2026-04-15-market-implied-polymarket-contract-and-ladder.md`
  - Why it matters: tells us what the market is pricing and how narrowly it settles.
  - Direct or indirect: direct for market-implied baseline and resolution mechanics.
  - Weight: high.
- Independent BTC quote context from CNBC also shows price band comfortably above 72k.
  - Source: `2026-04-15-market-implied-cnbc-btc-context.md`
  - Why it matters: suggests the cushion is not unique to a single reading from Binance.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim

- The contract is about one exact minute at noon ET on Apr 19, not average price over the period.
  - Why it matters causally: narrow timing increases path risk.
  - Direct or indirect: direct contract interpretation.
  - Weight: high.
- BTC can move several percent over a few days; a $2k-$3k cushion is meaningful but not invulnerable.
  - Why it matters causally: ordinary crypto volatility is the main route to no.
  - Direct or indirect: contextual.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- Independent contextual pricing helps sanity-check the level, but it does not reduce venue-specific settlement dependence to zero because Binance BTC/USDT is still the governing pair.

## Conflict between inputs

No major factual conflict. The main tension is weighting-based: how much confidence should be assigned to a current multi-thousand-dollar cushion over a three-plus-day horizon in BTC.

## Key assumptions

- Current cushion above strike survives ordinary volatility.
- No meaningful Binance-specific settlement anomaly appears.

## Key uncertainties

- How much BTC can move before Apr 19 noon ET.
- Whether any late macro or crypto-specific shock changes regime.

## Disconfirming signals to watch

- BTC trading back near or below $73k before Apr 19.
- Elevated volatility or exchange-specific dislocation on Binance.

## What would increase confidence

- BTC remaining above roughly $74k into Apr 18-19.
- Cross-venue prices staying tightly aligned with Binance BTC/USDT.

## Net update logic

The evidence keeps the directional yes lean intact because the market is not asking for a bullish breakout; it is asking for maintenance of an already-achieved price level. The main reason not to simply accept 86.5% at face value is that BTC's short-horizon volatility and the exact-minute settlement condition still leave a meaningful failure path.

## Suggested downstream use

- orchestrator synthesis input
- forecast update
- decision-maker review
