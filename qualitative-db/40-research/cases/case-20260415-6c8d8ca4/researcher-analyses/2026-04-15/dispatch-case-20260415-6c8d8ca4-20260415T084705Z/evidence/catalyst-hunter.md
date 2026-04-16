---
type: evidence_map
case_key: case-20260415-6c8d8ca4
dispatch_id: dispatch-case-20260415-6c8d8ca4-20260415T084705Z
research_run_id: f79d565f-cc9b-4a94-b85a-7a0ee0f7745b
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will Binance BTC/USDT close above 72,000 on the 12:00 ET one-minute candle on April 17?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["macro", "operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-6c8d8ca4/researcher-analyses/2026-04-15/dispatch-case-20260415T084705Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "bitcoin", "catalyst-hunter"]
---

# Summary

The current lean is Yes because the governing source (Binance BTC/USDT) shows BTC trading materially above the strike with only about two days left, but the contract remains fragile to a single fast downside move because it resolves on a specific one-minute noon ET close.

## Question being evaluated

Will the Binance BTC/USDT one-minute candle for 12:00 ET on April 17, 2026 close above 72,000?

## Current lean

Moderate Yes lean.

## Prior / starting view

Starting view from market price: roughly 81% Yes, implying the market thinks BTC is likely to stay above the strike but still assigns meaningful crash/slip risk.

## Evidence supporting the claim

- Binance spot/ticker source note: direct, high-weight.
  - BTC was about 74,040.86 during the run, around 2.83% above the strike.
  - Causally important because current cushion reduces the number of paths to No.
- Binance recent daily/hourly klines: direct, medium-high weight.
  - Recent closes recovered to and held around the mid-74k area after a prior dip.
  - Suggests BTC is not hovering at the threshold.
- Short time-to-resolution: indirect but important, medium weight.
  - Only about 51 hours remain, so absent a catalyst there is less time for a deep repricing.
- Polymarket contract page: direct for odds/rules, medium weight.
  - Market itself prices Yes around 81-82%, confirming broad expectation that current cushion matters.

## Evidence against the claim

- Narrow timed-print resolution: direct, high weight.
  - This is not daily close or average price; one minute at noon ET determines outcome.
  - Even temporary volatility at the wrong moment can flip the contract.
- Recent BTC volatility shown in Binance daily range: direct, medium-high weight.
  - BTC traded from ~70.5k low to ~74.9k high in recent sessions, proving 2-4% moves are realistic on this horizon.
- Lack of strong independent catalyst confirmation in accessible web sources: indirect, medium weight.
  - Available contextual fetches were thin or blocked, so confidence in the “no major catalyst imminent” judgment is moderate rather than high.

## Ambiguous or mixed evidence

- CME FedWatch page confirms the next FOMC meeting exists as an ongoing macro background variable, but the extracted page did not provide a directly useful near-term probability table for this case.
- CoinDesk markets page extraction was too thin to add decisive contextual support.

## Conflict between inputs

There is little factual conflict. The main tension is weighting-based:
- current price cushion argues Yes
- Bitcoin’s intrinsic short-term volatility and one-minute settlement design argue caution

Evidence that would resolve the tension best: additional high-quality near-term macro/calendar or ETF-flow data that clearly increases or decreases downside shock risk before noon ET April 17.

## Key assumptions

- No new material macro or crypto-specific shock hits before resolution.
- Binance remains a stable, usable resolution venue.
- Current cushion above 72k is not quickly erased by ordinary volatility.

## Key uncertainties

- Whether any unscheduled risk-off headline appears before noon ET April 17.
- Whether BTC drifts back toward the strike despite currently trading well above it.
- How much noon ET microstructure noise matters if spot is only marginally above 72k at resolution time.

## Disconfirming signals to watch

- BTC re-entering the 72k-73k zone and failing to bounce.
- Exchange-specific operational issues affecting Binance price formation or accessibility.
- A broad cross-asset drawdown in the next two sessions.

## What would increase confidence

- Another full trading session with BTC holding above 73k.
- Independent confirmation of benign ETF-flow / macro conditions into April 17.
- Price action that pushes farther from the strike, e.g. sustained trade above 75k.

## Net update logic

The evidence keeps the view Yes-leaning because the direct settlement source shows BTC comfortably above the strike and not pinned near it. I downweight a stronger Yes because the contract is unusually path-sensitive: one-minute noon ET settlement plus Bitcoin volatility means a single downside shock can still invalidate the thesis.

## Suggested downstream use

Use as an orchestrator synthesis input and forecast update input, with attention to whether later researchers surface a specific scheduled downside catalyst before noon ET April 17.
