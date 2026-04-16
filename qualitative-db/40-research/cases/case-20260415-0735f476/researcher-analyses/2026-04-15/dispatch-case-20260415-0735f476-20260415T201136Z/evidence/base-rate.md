---
type: evidence_map
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
research_run_id: f0a4e7fb-4b0c-4950-b281-fe2a4d6335ef
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-market
entity: bitcoin
topic: "evidence net for Bitcoin above 70,000 on April 20"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 20 close above 70,000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-base-rate-polymarket-rules-and-market-state.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-base-rate-binance-and-cross-venue-spot-check.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/base-rate.md"]
tags: ["evidence-map", "btc", "threshold-market"]
---

# Summary

Evidence nets to a Yes lean, but with less confidence than the market because the contract is a single-minute close on Binance and there are still five days for a drawdown.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 20 close above 70,000?

## Current lean

Yes is more likely than no.

## Prior / starting view

Starting outside-view prior: if BTC were already several percent above threshold with less than a week remaining, the default expectation would be favorable for Yes but not near certainty because single-minute close contracts remain path-sensitive.

## Evidence supporting the claim

- **Current level is comfortably above threshold**.
  - Source: Binance/API spot note.
  - Why it matters: distance-to-threshold is the dominant short-horizon structural input.
  - Direct/indirect: direct for present state.
  - Weight: high.
- **Cross-venue agreement around mid-74k reduces bad-read risk**.
  - Source: Binance/API spot note using CoinGecko and Coinbase.
  - Why it matters: independent confirmation that BTC is not merely barely above 70k.
  - Direct/indirect: direct for present state, indirect for final outcome.
  - Weight: medium.
- **Market mechanics are simple once wording is interpreted correctly**.
  - Source: Polymarket rules note.
  - Why it matters: narrow rule means no extra hidden conditions beyond one specified Binance close.
  - Direct/indirect: direct for contract interpretation.
  - Weight: medium-high.

## Evidence against the claim

- **Single-minute close markets remain fragile even when spot is above threshold**.
  - Source: Polymarket rules note and contract mechanics.
  - Why it matters: an otherwise bullish BTC path can still fail if the noon ET minute lands below 70k.
  - Direct/indirect: direct for mechanism.
  - Weight: high.
- **There are still about five days remaining**.
  - Source: case context and event timing.
  - Why it matters: BTC can move several percent over that horizon, so current cushion is meaningful but not decisive.
  - Direct/indirect: indirect.
  - Weight: medium-high.
- **Binance is the governing surface, not generic BTC/USD**.
  - Source: Polymarket rules note.
  - Why it matters: exchange-specific basis or wick differences can matter near threshold.
  - Direct/indirect: direct for settlement risk.
  - Weight: medium.

## Ambiguous or mixed evidence

- The market’s own 93-94% price is informative but endogenous. It may reflect good crowd aggregation, or it may slightly overstate persistence because traders anchor on current spot rather than exact-minute settlement risk.

## Conflict between inputs

No major factual conflict. The main disagreement is weighting-based: how much discount a base-rate model should apply for five-day path risk and single-minute-close mechanics.

## Key assumptions

- BTC remains in the same rough price regime into April 20.
- Binance BTC/USDT tracks broader BTC spot closely enough that cross-venue checks remain informative.

## Key uncertainties

- Near-term macro or crypto-specific shock.
- Whether BTC can give back >6% before the governing minute.
- Whether Binance-specific pricing diverges materially at settlement.

## Disconfirming signals to watch

- BTC revisiting 71k-72k before April 20.
- Binance underperforming other venues.
- Evidence of rising volatility regime or sharp risk-off sentiment.

## What would increase confidence

- Continued BTC closes materially above 72k into April 19-20.
- Additional direct verification on Binance UI/chart as the event approaches.
- Stable cross-venue basis with no Binance-specific weakness.

## Net update logic

The outside-view prior already favored Yes because BTC is well above the line with limited time left. Current Binance and cross-venue spot checks support that prior. I still discount below the market because this is not a broad “above sometime this week” contract; it is a single precise minute close on one exchange.

## Suggested downstream use

Use as synthesis input and as an auditable record of why the base-rate lane is Yes-leaning but less aggressive than the market.