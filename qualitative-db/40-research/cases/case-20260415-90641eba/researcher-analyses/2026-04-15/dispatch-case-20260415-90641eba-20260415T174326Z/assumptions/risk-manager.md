---
type: assumption_note
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
research_run_id: 5a9faab7-79fb-4b21-b3ce-4db9167a2052
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: daily-close-threshold
entity: bitcoin
topic: "Persistence of BTC above 70000 into the settlement minute"
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: liquidity
date_created: 2026-04-15
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-20 12:00 ET"
related_entities: ["binance", "bitcoin"]
related_drivers: ["liquidity", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-90641eba/researcher-source-notes/2026-04-15-risk-manager-polymarket-rules.md", "qualitative-db/40-research/cases/case-20260415-90641eba/researcher-source-notes/2026-04-15-risk-manager-price-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/risk-manager.md"]
tags: ["assumption-note", "btc", "binance", "settlement-risk"]
---

# Assumption

BTC will remain above 70000 on Binance BTC/USDT through the specific 12:00 ET one-minute settlement close on April 20 rather than merely trading above that level beforehand.

## Why this assumption matters

The contract is not asking whether BTC is generally above 70k this week; it asks whether one specific Binance minute closes above 70k. Most of the bullish case depends on translating current price cushion into persistence at the exact deadline.

## What this assumption supports

- A Yes-leaning probability estimate.
- Agreement or rough agreement with the market's high implied probability.
- The view that current spot distance above threshold is more important than unresolved tail risks.

## Evidence or logic behind the assumption

- Binance spot is already around 74000, leaving roughly a 4000-point cushion above the threshold.
- Cross-venue spot checks are consistent, suggesting the move is not a one-venue anomaly.
- For BTC, a 5-6% move over five days is common enough to matter, but not so common that it overwhelms the current lead by default.

## What would falsify it

- BTC falls back below 70000 on Binance as April 20 approaches.
- Market structure changes make noon ET especially weak relative to surrounding times.
- A sharp macro or crypto-specific selloff compresses the current cushion.

## Early warning signs

- Repeated rejection near or below 71k as the date approaches.
- Elevated intraday downside volatility on Binance.
- Cross-venue spot sliding back toward 70k rather than stabilizing comfortably above it.

## What changes if this assumption fails

The market should be treated as materially less than a high-80s probability. If BTC is trading near or below 70k shortly before settlement, the close-specific contract mechanics become the dominant driver and No risk rises quickly.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/risk-manager.md