---
type: evidence_map
case_key: case-20260414-d1f59d32
dispatch_id: dispatch-case-20260414-d1f59d32-20260414T144613Z
research_run_id: d55ea712-2b8c-44c2-b67a-e67122805341
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-15
question: "Will the price of Bitcoin be above $74,000 on April 15?"
driver: operational-risk
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-d1f59d32/researcher-analyses/2026-04-14/dispatch-case-20260414-d1f59d32-20260414T144613Z/personas/risk-manager.md"]
tags: ["btc", "binance", "threshold", "timestamp-risk"]
---

# Summary

Evidence nets to a modest Yes lean, but with lower confidence than the 81.5% market price suggests because the contract is keyed to one specific Binance minute tomorrow rather than a general daily-close state.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 15, 2026 close above 74,000?

## Current lean

Lean Yes, but with meaningful timing/path fragility.

## Prior / starting view

Starting view was that current spot being above the threshold likely makes Yes the favorite, but a crypto one-minute timestamp contract should trade with more humility than a generic spot snapshot.

## Evidence supporting the claim

- Binance current spot above threshold by roughly 1.57k at one capture.
  - Source: 2026-04-14-risk-manager-binance-coinbase-spot-context.md
  - Why it matters causally: the market does not need upside continuation, only maintenance above the line.
  - Direct or indirect: direct for current state, indirect for settlement.
  - Weight: high.

- Recent Binance 1-minute closes in sampled window all remained above 75.2k.
  - Source: 2026-04-14-risk-manager-binance-coinbase-spot-context.md
  - Why it matters causally: shows near-term price stability above the strike at capture time.
  - Direct or indirect: direct for immediate microstructure context, indirect for next-day settlement.
  - Weight: medium.

- Coinbase cross-check near 75.3k.
  - Source: 2026-04-14-risk-manager-binance-coinbase-spot-context.md
  - Why it matters causally: reduces concern that Binance alone is transiently elevated.
  - Direct or indirect: contextual.
  - Weight: medium.

## Evidence against the claim

- The contract settles on one exact minute tomorrow on Binance, so a modest downswing at the wrong time is enough to lose even if BTC spends most of the next day above 74k.
  - Source: 2026-04-14-risk-manager-polymarket-rules-binance-resolution.md
  - Why it matters causally: path and timestamp dependence are the main failure mode.
  - Direct or indirect: direct for settlement mechanics.
  - Weight: high.

- The current cushion is only about 2% of spot, well within ordinary BTC daily movement.
  - Source: inferred from current exchange data and threshold.
  - Why it matters causally: ordinary volatility can erase the edge without requiring a regime change.
  - Direct or indirect: contextual.
  - Weight: high.

## Ambiguous or mixed evidence

- Cross-venue price agreement is reassuring for current state, but because Binance alone settles the market, it only partially reduces venue-specific risk.

## Conflict between inputs

No major factual conflict. The main issue is weighting: how much discount should be applied for one-minute timestamp fragility versus current spot cushion.

## Key assumptions

- The current above-threshold cushion is durable enough to survive until noon ET tomorrow.
- No exchange-specific anomaly materially distorts Binance BTC/USDT at the resolution minute.

## Key uncertainties

- Short-horizon BTC volatility over the next ~21 hours.
- Whether macro/news flow induces a risk-off move before the settlement minute.
- Exact Binance candle handling at the noon ET boundary as displayed on the venue UI.

## Disconfirming signals to watch

- BTC breaking below 74.5k and staying weak into the settlement window.
- A sharp venue-specific Binance dislocation versus Coinbase or other large venues.
- Elevated realized volatility in the hours immediately preceding noon ET.

## What would increase confidence

- BTC holding comfortably above 75k closer to the event.
- Additional cross-venue checks tomorrow morning showing no Binance divergence.
- Clean confirmation of the relevant ET-to-exchange candle mapping near settlement.

## Net update logic

Current spot context says Yes should be favored, but contract interpretation says confidence should be discounted because all favorable conditions must still hold at one exact minute on one venue. That combination produces a Yes lean below the market’s current confidence.

## Suggested downstream use

Use as orchestrator synthesis input and as a check against overconfident bullish weighting.