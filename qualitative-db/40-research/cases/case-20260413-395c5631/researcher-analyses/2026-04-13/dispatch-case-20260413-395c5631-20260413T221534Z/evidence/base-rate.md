---
type: evidence_map
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
research_run_id: c136fc5f-2724-4182-ac8d-dfb825aa79f2
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-15
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-15 be above 72000?"
driver: reliability
date_created: 2026-04-13
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-395c5631/researcher-analyses/2026-04-13/dispatch-case-20260413-395c5631-20260413T221534Z/personas/base-rate.md"]
tags: ["evidence-map", "bitcoin", "base-rate"]
---

# Summary

The outside-view started below the market because 72k noon-ET closes have been uncommon across the recent month, but the current price regime and direct Binance state data justify moving to a modest Yes lean rather than staying anchored to the longer short-term base rate.

## Question being evaluated

Whether Binance BTC/USDT will print a final one-minute candle close above 72,000 at 12:00 ET on April 15, 2026.

## Current lean

Moderate Yes lean, but less confident than the market.

## Prior / starting view

Starting from recent 35-day noon-ET closes alone, the outside-view prior would be low: only about 17% of those observations were above 72k.

## Evidence supporting the claim

- **Current Binance spot around 73.8k**
  - source: 2026-04-13-base-rate-binance-and-cross-exchange-price-check.md
  - causal relevance: price is already above threshold by roughly 1.8k, so the event requires persistence rather than a fresh upside break
  - directness: direct
  - weight: high

- **Recent immediate regime improved sharply**
  - source: same note
  - causal relevance: noon-ET closes were above 72k on Apr 9, Apr 10, Apr 11, and Apr 13
  - directness: direct
  - weight: medium-high

- **Cross-exchange alignment**
  - source: same note
  - causal relevance: reduces concern that Binance alone is showing an anomalously high reading versus broader BTC pricing
  - directness: indirect for resolution, direct for price-state validation
  - weight: medium

## Evidence against the claim

- **Longer recent base rate is much lower than market**
  - source: same note
  - causal relevance: only 6 of the last 35 noon-ET observations were above 72k, which argues against treating this threshold as normal
  - directness: direct analog / base-rate evidence
  - weight: high

- **Threshold can fail even after intraday strength**
  - source: same note
  - causal relevance: Apr 12 traded above 72k intraday but noon-ET close was below 72k, showing that being near or even above the threshold earlier does not lock in the resolution minute
  - directness: direct analog
  - weight: medium-high

- **Contract is narrow**
  - source: 2026-04-13-base-rate-polymarket-contract-and-market.md
  - causal relevance: the market depends on a single one-minute close on a single exchange, creating timing and microstructure risk
  - directness: direct contract evidence
  - weight: medium

## Ambiguous or mixed evidence

- The market price near 73% may reflect informed trading, but it may also embed momentum-chasing after BTC recovered above the threshold.
- Cross-exchange parity helps, but the contract still resolves on Binance only.

## Conflict between inputs

No major factual conflict. The tension is weighting-based: a colder short-term base rate points low, while current regime evidence points materially higher.

## Key assumptions

- The current above-72k regime persists into April 15 noon ET.
- No fresh macro or crypto-specific shock breaks BTC back below the threshold.
- Binance remains a fair reflection of broader BTC pricing at the resolution minute.

## Key uncertainties

- BTC volatility over the next ~38 hours.
- Whether noon ET specifically is vulnerable to intraday reversals.
- Whether the market is over-extrapolating the latest two-day rebound.

## Disconfirming signals to watch

- Repeated hourly closes below 72k before April 15.
- Sharp cross-market risk-off move.
- Widening divergence between Binance BTC/USDT and other BTC/USD references.

## What would increase confidence

- Another day of sustained trading above 72k.
- Continued noon-ET style closes above the threshold.
- Evidence of low realized volatility into the settlement window.

## Net update logic

The base-rate anchor alone would be far below the market, but direct state evidence matters more here because the horizon is short and BTC is already above the strike. That justifies a move from a low prior to a modest Yes lean, though not all the way to the market's ~73%.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit trail for why the persona remained below market despite leaning Yes.