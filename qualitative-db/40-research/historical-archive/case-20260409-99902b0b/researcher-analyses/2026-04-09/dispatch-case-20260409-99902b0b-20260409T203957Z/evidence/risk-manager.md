---
type: evidence_map
case_key: case-20260409-99902b0b
dispatch_id: dispatch-case-20260409-99902b0b-20260409T203957Z
research_run_id: 20c642ba-b4cf-44ef-9473-852b273b7995
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: exchange-data
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-10
question: "Will the price of Bitcoin be above $70,000 on April 10?"
driver: operational-risk
date_created: 2026-04-09
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low-direct-conflict
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["binance-btcusdt-settlement-candle"]
proposed_drivers: ["deadline-specific path-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-99902b0b/researcher-analyses/2026-04-09/dispatch-case-20260409-99902b0b-20260409T203957Z/personas/risk-manager.md"]
tags: ["evidence-map", "timing-risk", "crypto", "resolution"]
---

# Summary

The net evidence still leans Yes because Binance BTC/USDT is currently more than 2.3k above the strike, but the key risk-manager takeaway is that the market appears more confident than the evidence warrants for a single-minute, next-day settlement.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for April 10, 2026 at 12:00 ET have a final Close above 70,000?

## Current lean

Lean Yes, but with materially less confidence than the market.

## Prior / starting view

Starting view was that a market priced near 88.5% likely reflected BTC already being above 70k with moderate cushion, but extreme pricing raised concern about deadline-specific overconfidence.

## Evidence supporting the claim

- Binance primary spot data showed BTCUSDT around 72.3k-72.4k on April 9 afternoon ET.
  - direct evidence
  - high weight
  - matters because the named settlement venue currently has a sizable cushion over 70k.
- Polymarket rules clearly define the settlement source and the market price was extreme in the Yes direction.
  - direct for contract mechanics, indirect for state of world
  - medium weight
  - matters because it confirms the exact condition and shows broad market confidence.

## Evidence against the claim

- Settlement depends on one exact 1-minute close at noon ET rather than general daily trading above 70k.
  - direct contract-interpretation risk
  - high weight
  - matters because a brief drawdown at the wrong time is enough to lose.
- The current cushion is only roughly 3.3% to 3.5%, which is not large for BTC over an overnight plus morning window.
  - direct from Binance data plus contextual volatility logic
  - medium-high weight
  - matters because a routine crypto move could erase the buffer.
- Binance-specific venue/pair dependence creates exchange-specific basis or data-path risk, even if the broader BTC market stays strong.
  - contract-specific operational risk
  - medium weight
  - matters because the contract does not average across venues.

## Ambiguous or mixed evidence

- The market price itself is informative but could reflect true edge or herd overconfidence around a simple threshold.
- Current spot strength is supportive, but crypto’s short-horizon volatility means spot observations have limited forward certainty.

## Conflict between inputs

No major factual conflict between sources. The tension is mostly weighting-based: how much to trust the current 2.3k+ cushion versus the fragility of a one-minute settlement window.

## Key assumptions

- BTC is unlikely to fall more than about 3.3% before noon ET April 10.
- Binance BTC/USDT will track the broader BTC spot market without meaningful venue-specific dislocation.

## Key uncertainties

- Overnight macro or crypto-specific news flow.
- Short-horizon realized volatility into the settlement window.
- Whether noon ET produces idiosyncratic volatility on Binance.

## Disconfirming signals to watch

- BTC trading below 71k overnight or in the morning.
- Evidence of a sharp risk-off move in crypto broadly.
- Binance-specific pricing anomalies or operational instability.

## What would increase confidence

- Another Binance verification pass on the morning of April 10 still showing BTC well above 71k.
- Evidence that realized overnight volatility remains subdued.

## Net update logic

The evidence moved the starting view from generic cautious-Yes to specific "Yes but below market" because the primary-source buffer is real and meaningful, yet the contract mechanics concentrate risk into a narrow timestamp where a fairly ordinary crypto move could still flip the result.

## Suggested downstream use

Use as an Orchestrator synthesis input and as a caution against treating extreme market pricing as near-certainty on deadline-specific crypto candle contracts.