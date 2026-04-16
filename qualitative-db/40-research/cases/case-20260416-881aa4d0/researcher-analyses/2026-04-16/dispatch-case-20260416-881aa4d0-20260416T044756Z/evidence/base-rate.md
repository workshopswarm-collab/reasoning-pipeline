---
type: evidence_map
case_key: case-20260416-881aa4d0
dispatch_id: dispatch-case-20260416-881aa4d0-20260416T044756Z
research_run_id: 96e5bef4-5a68-4025-b05a-4322e6fb205e
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-17
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 70000?"
driver: reliability
date_created: 2026-04-16
agent: orchestrator
status: complete
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-881aa4d0/researcher-analyses/2026-04-16/dispatch-case-20260416-881aa4d0-20260416T044756Z/personas/base-rate.md"]
tags: ["evidence-map", "btc", "binance", "threshold"]
---

# Summary

The evidence nets to a strong Yes lean because the contract threshold sits materially below the current Binance BTC/USDT level and the contract mechanics are straightforward once the exact source, pair, timezone, and candle definition are checked.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on Apr. 17, 2026 have a final Close above 70,000?

## Current lean

Yes, with high probability but not quite as high as the market's 99% implied probability.

## Prior / starting view

Starting outside-view prior: if BTC is already well above a threshold less than 24 hours before a Binance-noon settlement, Yes should usually be favored strongly, but 99% is an extreme price that deserves a volatility and contract-mechanics check.

## Evidence supporting the claim

- Direct Binance ticker and kline data show BTC/USDT around 74.7k-74.9k during the research window. Direct, high weight.
- Recent one-minute candles sampled from Binance all closed well above 70k. Direct, medium weight.
- Binance 24h stats show the low during the sampled period remained above 73.5k, still comfortably above the threshold. Direct, medium weight.
- Polymarket rules clearly point to Binance BTC/USDT 12:00 ET 1-minute close, reducing source-of-truth ambiguity. Direct for mechanics, high weight.

## Evidence against the claim

- BTC can move several percent in less than a day; a roughly 6-7% decline from the current level would be enough to flip the market to No. Indirect/contextual, high weight.
- Single-minute settlement markets retain residual operational/timestamp risk, especially when UI time labeling and ET conversion matter. Contextual, low-to-medium weight.
- The market is already at an extreme probability, which leaves little room for error and raises the bar for confidence. Contextual, medium weight.

## Ambiguous or mixed evidence

- Market pricing itself is informative but partly endogenous; it should not be treated as independent evidence from the same underlying exchange state.
- The recent 24h range is supportive but not decisive because crypto volatility can regime-shift quickly.

## Conflict between inputs

No material factual conflict found. The main tension is weighting-based: whether the current price cushion and simple mechanics justify something as high as 99%.

## Key assumptions

- Binance remains the operative and stable settlement source.
- BTC does not suffer an unusually large downside move before the settlement minute.
- No exchange-specific anomaly creates a misleading or disputed settlement print.

## Key uncertainties

- Remaining one-day BTC volatility.
- Whether any exogenous catalyst emerges before Apr. 17 noon ET.
- Residual operational edge cases around the exact final settlement minute.

## Disconfirming signals to watch

- BTC/USDT losing the current cushion and trading toward 71k-72k.
- A sudden volatility spike or macro shock.
- Binance data/feed irregularities close to settlement.

## What would increase confidence

- Another direct Binance check closer to Apr. 17 morning ET still showing price well above 70k.
- Continued 24h low remaining materially above the threshold.

## Net update logic

The starting outside-view already favored Yes because the threshold sat well below current spot. Direct Binance verification plus a contract-mechanics check preserved that lean. The main downweight versus market is simply that BTC one-day downside tails are real, so 99% feels a bit too close to certainty for a single-minute crypto settlement market.

## Suggested downstream use

Use as synthesis input and forecast update support; low need for follow-up investigation unless BTC volatility rises materially before settlement.