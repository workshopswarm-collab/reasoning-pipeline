---
type: evidence_map
case_key: case-20260415-c0464347
dispatch_id: dispatch-case-20260415-c0464347-20260415T011958Z
research_run_id: 7d5d69d4-0793-4adc-8ee3-4a8c0cd51f9d
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-c0464347/researcher-analyses/2026-04-15/dispatch-case-20260415-c0464347-20260415T011958Z/personas/market-implied.md"]
tags: ["evidence-map", "threshold-market", "market-implied"]
---

# Summary

This evidence map nets out why the market's high Yes pricing looks mostly reasonable but not obviously cheap.

## Question being evaluated

Whether Binance BTC/USDT will print a final 1-minute candle close above 70,000 for the 12:00 ET candle on 2026-04-20.

## Current lean

Lean Yes at a high but not extreme probability.

## Prior / starting view

Starting point was the market-implied 88% from Polymarket, treated as an information-rich prior.

## Evidence supporting the claim

- Live Binance BTCUSDT price around 74.6k on 2026-04-14 21:21 ET.
  - Direct source: Binance ticker endpoint.
  - Why it matters: spot is already materially above the strike.
  - Direct evidence.
  - Weight: high.

- Recent Binance 1-minute klines around the verification window closed around 74.6k-74.7k.
  - Direct source: Binance kline / uiKline endpoints.
  - Why it matters: same data family as the settlement convention.
  - Direct evidence for current buffer, though not for final settlement.
  - Weight: high.

- Binance 24h low remained around 73.8k during the verification window.
  - Direct source: Binance 24hr ticker.
  - Why it matters: threshold remained well below even recent downside within the last day.
  - Direct contextual evidence.
  - Weight: medium-high.

- Polymarket ladder context shows lower thresholds priced near certainty and 72k still priced 77%.
  - Source: Polymarket market page.
  - Why it matters: the whole strike surface appears internally coherent rather than isolated at 70k.
  - Contextual market evidence.
  - Weight: medium.

## Evidence against the claim

- The contract resolves on one exact minute, not a daily close or average.
  - Source: Polymarket rules.
  - Why it matters: single-minute settlement increases tail-risk sensitivity.
  - Direct contract evidence.
  - Weight: high.

- BTC can move more than 6% over five days, especially in leveraged crypto conditions.
  - Source: inference from crypto market structure and current 24h range size.
  - Why it matters: existing cushion is meaningful but not invulnerable.
  - Indirect/contextual evidence.
  - Weight: medium-high.

- Binance-specific operational or price-dislocation issues near settlement could matter because the source is exchange-specific.
  - Source: contract design and exchange-specific settlement dependency.
  - Why it matters: non-fundamental venue noise can affect settlement.
  - Indirect but structurally relevant.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- Current strong BTC level could reflect durable demand or just a transient high-beta rally; for this contract only the settlement minute matters.

## Conflict between inputs

There is no major factual conflict. The main disagreement is weighting-based: how much protection does a ~4.6k buffer really provide over five days in BTC?

## Key assumptions

- The present price cushion remains mostly intact through April 20 noon ET.
- Binance settlement mechanics behave normally and map cleanly to the API/UI candle convention.

## Key uncertainties

- Magnitude of short-term BTC volatility over the next five days.
- Whether any macro or crypto-specific catalyst triggers a sharp selloff before the exact resolution minute.

## Disconfirming signals to watch

- BTC rapidly losing the 72k-73k zone.
- A volatility shock that expands downside tails.
- Binance-specific pricing irregularity near settlement.

## What would increase confidence

- BTC holding above 74k into the weekend.
- Continued Polymarket strike-surface coherence without meaningful repricing lower.
- Another Binance verification closer to resolution showing the threshold still distant.

## Net update logic

The evidence did not justify a major move away from the market prior. Direct Binance checks support the market's high Yes view, but the exact-minute settlement design keeps the answer below near-certainty.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit artifact showing why this run broadly respects the market while retaining residual tail-risk skepticism.