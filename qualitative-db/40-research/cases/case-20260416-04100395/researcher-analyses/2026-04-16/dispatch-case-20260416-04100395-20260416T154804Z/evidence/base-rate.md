---
type: evidence_map
case_key: case-20260416-04100395
dispatch_id: dispatch-case-20260416-04100395-20260416T154804Z
research_run_id: b2985bb1-f13a-4cea-b14f-3b4f8d56b47b
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-data
entity: ethereum
topic: will-the-binance-eth-usdt-12-00-et-one-minute-candle-on-2026-04-17-close-above-2300
question: "Will the Binance ETH/USDT 12:00 ET one-minute candle on 2026-04-17 close above 2300?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/personas/base-rate.md"]
tags: ["evidence-map", "eth", "base-rate"]
---

# Summary

The net evidence supports a slight Yes lean, but the outside view is less bullish than the market because the threshold sits only modestly below current spot and recent realized ETH prices crossed it repeatedly.

## Question being evaluated

Will the Binance ETH/USDT 12:00 ET one-minute candle on 2026-04-17 close above 2300?

## Current lean

Slight Yes lean, but close to a coin flip.

## Prior / starting view

For a one-day crypto threshold market with settlement at one exact minute, the starting prior should be moderate unless spot is already comfortably beyond the line or a strong catalyst clearly dominates.

## Evidence supporting the claim

- Current Binance spot was around 2333.42 during retrieval.
  - direct source: Binance API
  - causal relevance: spot currently above the threshold
  - directness: direct
  - weight: high
- CoinGecko cross-check placed ETH around 2338.82.
  - direct source: CoinGecko
  - causal relevance: confirms broad market context is similar, reducing fear of a Binance-only data glitch
  - directness: contextual
  - weight: medium
- Several recent daily closes were above 2300, including about 2369.46, 2322.44, 2359.95, and 2333.43.
  - direct source: Binance daily klines
  - causal relevance: shows the line is live and reachable in the current regime
  - directness: contextual
  - weight: medium

## Evidence against the claim

- The latest spot and daily close are only about 1-2% above 2300, not safely above it.
  - source: Binance API
  - causal relevance: normal one-day ETH volatility can erase that cushion
  - directness: direct/contextual hybrid
  - weight: high
- Recent daily closes also printed below 2300 multiple times, including around 2285.00 and 2191.65.
  - source: Binance daily klines
  - causal relevance: threshold crossing frequency cuts both ways and argues against an extreme Yes probability
  - directness: contextual
  - weight: high
- Contract resolution depends on one specific noon ET minute close, not the day high, low, or broader average price.
  - source: Polymarket rules
  - causal relevance: narrow settlement window increases path dependence and lowers confidence in any near-threshold bullish view
  - directness: direct
  - weight: high

## Ambiguous or mixed evidence

- Current risk sentiment may be mildly bullish because ETH is above threshold now, but that same fact is already reflected in the market and does not by itself justify a strong premium over a near-threshold base rate.

## Conflict between inputs

There is no major factual conflict. The disagreement is weighting-based: the market appears to put more weight on current above-threshold spot than the outside-view threshold-crossing distribution warrants.

## Key assumptions

- Recent realized price distribution is informative for the next day's noon ET minute.
- No major catalyst or exchange-specific distortion emerges before settlement.

## Key uncertainties

- Intraday volatility between now and noon ET tomorrow.
- Any macro or crypto-specific catalyst not captured in this quick base-rate pass.
- Potential microstructure difference between Binance noon ET print and all-day price context.

## Disconfirming signals to watch

- ETH falling back under 2300 and failing to reclaim it before settlement.
- Broad crypto risk-off move.
- Binance-specific dislocation or resolution ambiguity.

## What would increase confidence

- Evidence of sustained trading materially above 2300 into settlement.
- More granular intraday distribution data around noon ET.
- Stronger catalyst evidence for directional continuation.

## Net update logic

Starting from a moderate prior for a one-day exact-minute threshold, current spot above the line pulls the estimate upward. But because the cushion is thin and recent realized prices crossed the threshold both ways, the update stops well short of the market's mid-60s Yes pricing.

## Suggested downstream use

Use as synthesis input and as an audit trail for why this base-rate lane stayed only mildly bullish rather than endorsing the market's stronger Yes lean.