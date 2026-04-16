---
type: evidence_map
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
research_run_id: 3134cc8d-5ce6-426f-bc39-ac8045afe8c0
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-18
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 70000 on 2026-04-18?"
driver: reliability
date_created: 2026-04-14
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-8a0619b6/researcher-analyses/2026-04-14/dispatch-case-20260414-8a0619b6-20260414T194140Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "market-implied"]
---

# Summary

The evidence mostly supports the market's high-probability Yes lean, but the contract's narrow timing and BTC's inherent volatility argue against treating 90% as lock-tight.

## Question being evaluated

Will Binance BTC/USDT close above 70,000 on the final 12:00 ET one-minute candle on April 18, 2026?

## Current lean

Lean Yes, with probability in the mid-to-high 80s rather than an unquestioned 90%+ certainty.

## Prior / starting view

Starting baseline was the market-implied 89-90% from Polymarket.

## Evidence supporting the claim

- Binance spot was around 74.1k at research time, giving a cushion of roughly 4.1k above the strike.
  - source: Binance source note
  - causal relevance: the exact settlement venue/pair is already materially above the threshold
  - direct vs indirect: direct
  - weight: high
- Binance 24-hour low was still above 72.9k.
  - source: Binance source note
  - causal relevance: recent realized downside did not approach the strike
  - direct vs indirect: direct
  - weight: medium-high
- CoinGecko cross-check was broadly aligned around 74.2k.
  - source: CoinGecko source note
  - causal relevance: reduces concern that Binance was showing a one-off anomalous level
  - direct vs indirect: contextual
  - weight: medium
- Polymarket priced the 70k line around 90% while adjacent ladder outcomes also showed a smooth distribution.
  - source: Polymarket source note
  - causal relevance: suggests the crowd view is internally coherent rather than obviously broken
  - direct vs indirect: contextual
  - weight: medium

## Evidence against the claim

- BTC can move more than 5% in four days, so the cushion is meaningful but not overwhelming.
  - source: inferential from current price distance and crypto volatility context
  - causal relevance: a single sharp risk-off episode can flip the contract
  - direct vs indirect: indirect
  - weight: high
- The contract is resolved on one exact minute on Binance, creating venue- and timing-specific fragility.
  - source: Polymarket rules
  - causal relevance: even if broader market context is healthy, a narrow timestamp can still fail
  - direct vs indirect: direct on mechanics
  - weight: medium-high

## Ambiguous or mixed evidence

- The market page itself is both evidence of consensus and part of the thing being evaluated; it should not be treated as independent proof.
- CoinGecko confirms broad level but not the exact Binance noon ET close.

## Conflict between inputs

There is no strong factual conflict across sources. The main disagreement is weighting-based: whether a ~5.5% buffer four days out deserves about 90% or a somewhat lower probability.

## Key assumptions

- Current BTC price level remains broadly stable enough into April 18.
- No major downside catalyst hits before the noon ET settlement window.
- Binance-specific operational or print anomalies do not become resolution-relevant.

## Key uncertainties

- Near-term BTC volatility over a four-day horizon.
- Whether a weekend-style or event-driven drop could erase the current cushion.
- Whether the exact noon ET one-minute candle creates more path fragility than the market is crediting.

## Disconfirming signals to watch

- BTC falls toward 71k-72k before April 18.
- Binance-specific dislocations or unusual wicks emerge.
- Adjacent Polymarket ladder lines cheapen sharply, implying deteriorating near-term confidence.

## What would increase confidence

- BTC holding above 73k into April 17-18.
- Continued agreement between Binance and broad aggregators.
- No evidence of unusual event risk around the settlement window.

## Net update logic

The market starts from a strong prior and current direct evidence mostly supports it. The reason not to simply match or exceed 90% is that the contract is date-specific, exchange-specific, and one-minute specific, so a 4-day crypto path still contains nontrivial failure risk.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit trail for why the final estimate is close to, but slightly below, the market-implied baseline.