---
type: evidence_map
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
research_run_id: 90773935-2f5e-4e91-9d22-c5aa8eee5106
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: threshold-daily-close
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20 close above 70000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["threshold-daily-close"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-variant-view-polymarket-rules-and-market-state.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-variant-view-binance-and-coingecko-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/variant-view.md"]
tags: ["evidence-map", "btc", "binance", "threshold-close"]
---

# Summary

Evidence favors Yes because BTC is trading well above 70k on the governing venue, but the strongest credible variant view is that a **single-minute close contract with five days remaining** should not be priced as near-certain merely because spot is currently comfortable.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20 close above 70,000?

## Current lean

Lean Yes, but less strongly than the market.

## Prior / starting view

Starting from the 0.93 market price, the initial expectation was that the market was probably right directionally but maybe too confident given the fixed-time close mechanic.

## Evidence supporting the claim

- **Current Binance level near 74.6k**
  - source: Binance ticker / source note
  - causal relevance: leaves a ~6.6% buffer above threshold
  - directness: direct for current governing-venue price, indirect for April 20 noon close
  - weight: high

- **Recent Binance daily closes all above 70k in pulled 7-day sample**
  - source: Binance daily klines / source note
  - causal relevance: suggests sustained regime above the threshold rather than a one-off spike
  - directness: direct historical venue evidence
  - weight: medium-high

- **Independent CoinGecko check around 74.7k**
  - source: CoinGecko market endpoint / source note
  - causal relevance: reduces chance the observed level is a bad single-source print
  - directness: contextual, not governing
  - weight: medium

## Evidence against the claim

- **Contract settles on one exact minute close, not broad trading range**
  - source: Polymarket rules / source note
  - causal relevance: even a temporary selloff at settlement minute can defeat a generally bullish thesis
  - directness: direct contract evidence
  - weight: high

- **Five days remain in a volatile 24/7 asset**
  - source: contract timing plus Binance volatility context
  - causal relevance: enough time for a macro or crypto-specific drawdown of several thousand dollars
  - directness: interpretive
  - weight: medium-high

- **Extreme market pricing above 90% can reflect stale spot anchoring**
  - source: market page plus mechanism comparison
  - causal relevance: traders may overweight current level and underweight path/time risk
  - directness: interpretive
  - weight: medium

## Ambiguous or mixed evidence

- Recent daily highs above 75k are supportive, but they also show BTC can move $1k+ intraday, which cuts both ways.
- Cross-source agreement on current price helps, but it does not directly forecast the specific noon ET close on April 20.

## Conflict between inputs

There is little factual conflict. The main disagreement is **weighting-based**: how much discount to apply for fixed-time settlement risk despite strong current spot levels.

## Key assumptions

- The current 4k-5k cushion above 70k is meaningful enough to dominate ordinary downside volatility.
- Binance-specific pricing will remain broadly aligned with global BTC spot into the resolution window.

## Key uncertainties

- Weekend volatility between now and April 20.
- Macro or crypto-specific catalysts that could induce a sharp selloff.
- Whether the noon ET minute lands during a transient weak patch even if BTC broadly stays elevated.

## Disconfirming signals to watch

- Binance BTC/USDT daily closes slipping back toward 72k or 71k.
- Sudden downside volatility expansion.
- Evidence of exchange-specific dislocation on Binance.

## What would increase confidence

- Additional daily closes above 73k-74k before April 20.
- Stable trading through the weekend without material downside breaks.
- Direct pre-resolution confirmation from Binance 1m candles near the event.

## Net update logic

The evidence keeps the contract in Yes territory because spot is materially above the threshold and recent realized trading supports that regime. The variant update is not a bearish thesis on BTC itself; it is a contract-interpretation and timing-risk discount against treating this as almost settled several days early.

## Suggested downstream use

Use as synthesis input for whether market-extreme pricing on fixed-time close contracts should be slightly discounted when the crowd may be anchoring too heavily to current spot.