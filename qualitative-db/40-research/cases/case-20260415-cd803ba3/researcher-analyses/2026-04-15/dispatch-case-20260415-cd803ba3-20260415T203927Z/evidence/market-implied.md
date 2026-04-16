---
type: evidence_map
case_key: case-20260415-cd803ba3
dispatch_id: dispatch-case-20260415-cd803ba3-20260415T203927Z
research_run_id: 64c78172-573e-457b-9f67-397835df0e76
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: reliability
date_created: 2026-04-15
agent: market-implied
status: draft
confidence: medium
conflict_status: low-direct-conflict
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-cd803ba3/researcher-analyses/2026-04-15/dispatch-case-20260415-cd803ba3-20260415T203927Z/personas/market-implied.md"]
tags: ["evidence-netting", "threshold-market", "market-implied"]
---

# Summary

The evidence nets to a moderate Yes lean and supports the view that the market is broadly efficient rather than obviously stale. The main support is that Binance settlement prices are already above the threshold and cross-venue spot checks align. The main pushback is timing: this contract settles on one exact future minute, so even a modest BTC pullback can flip the result.

## Question being evaluated

Whether Binance BTC/USDT will have a final 12:00 ET one-minute candle close above 74,000 on April 17, 2026.

## Current lean

Lean Yes, but not by a huge margin.

## Prior / starting view

Start from the market prior of about 70% Yes from assignment context and ask whether current evidence justifies that confidence.

## Evidence supporting the claim

- Binance 1m settlement-venue spot check showed BTCUSDT recent closes around 74.7k-74.9k.
  - source: source note `2026-04-15-market-implied-binance-and-cross-exchange-spot-check.md`
  - causal relevance: the asset is already trading above the target level on the actual settlement venue
  - directness: direct
  - weight: high
- CoinGecko and Coinbase spot checks were tightly aligned with Binance near 74.7k.
  - source: same source note
  - causal relevance: lowers concern that the threshold is being cleared only on one anomalous venue
  - directness: contextual cross-check
  - weight: medium
- Polymarket contract/rules define a simple threshold based on one Binance minute close, with no extra conditional complexity beyond strict greater-than.
  - source: source note `2026-04-15-market-implied-polymarket-rules-and-price.md`
  - causal relevance: reduces interpretive ambiguity; a clean threshold favors using current price cushion as the main input
  - directness: direct for contract interpretation
  - weight: medium

## Evidence against the claim

- The settlement minute is still about 19 hours away, and BTC can move more than 1% over that horizon.
  - source: inferred from market structure and current cushion size, grounded by live spot check
  - causal relevance: current above-threshold trading does not lock in the future noon ET close
  - directness: indirect/contextual
  - weight: high
- The exact contract uses the Binance 12:00 ET candle close, so a brief dip at the wrong minute is enough for No even if BTC trades above 74,000 for much of the day.
  - source: Polymarket rules note
  - causal relevance: one-minute timing precision increases fragility near the threshold
  - directness: direct for contract interpretation
  - weight: high

## Ambiguous or mixed evidence

- Polymarket displayed 63% on the fetched page while assignment metadata gave 70%; this does not change the directional view much but suggests the live price should be treated as a range rather than one exact static number.

## Conflict between inputs

There is no major factual conflict about the governing source or current broad price zone. The main disagreement is weighting-based: how much confidence should be placed on current spot being above the threshold versus the risk of a short-horizon reversal before the exact settlement minute.

## Key assumptions

- Current above-threshold spot levels have some persistence into April 17 noon ET.
- Binance will not materially diverge from broader spot references around settlement.

## Key uncertainties

- Overnight and morning BTC volatility before the exact settlement minute
- Whether any macro/crypto-specific catalyst hits before noon ET April 17

## Disconfirming signals to watch

- BTC loses 74,000 and fails to reclaim it during April 16 night / April 17 morning
- Binance trades persistently below other major spot references

## What would increase confidence

- BTC remains above 74,000 through multiple additional spot checks closer to settlement
- Morning-of-April-17 Binance pricing still shows a healthy cushion above 74,000

## Net update logic

Starting from the market's roughly 70% prior, the live Binance spot check largely validates the market's logic: the level is already cleared on the actual settlement venue. That supports respecting the market rather than leaning contrarian. But the cushion above 74,000 is not so large, and the contract's exact-minute resolution keeps fragility meaningful, so the market does not deserve extreme confidence.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why the market-implied researcher treated the market as roughly efficient rather than clearly overextended.