---
type: assumption_note
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
research_run_id: 6b7a203d-2b34-4f67-89c3-97e85086fe5b
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 70000?"
driver: reliability
date_created: 2026-04-15
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "5 days"
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["base-rate-finding"]
tags: ["assumption", "short-horizon", "price-regime"]
---

# Assumption

The recent above-70k trading regime on Binance will persist through the April 20 noon ET resolution window without a drawdown larger than roughly 5-6%.

## Why this assumption matters

The bullish case depends less on long-run Bitcoin appreciation and more on short-horizon regime persistence over the next five days.

## What this assumption supports

- A probability estimate above 50%
- A view that current spot cushion meaningfully supports yes
- A conclusion that the market is directionally right but slightly overconfident

## Evidence or logic behind the assumption

BTC was around 74.3k on Binance at assignment time, giving a cushion of about 4.3k over the threshold. Recent daily closes have mostly held above 70k, indicating the market is currently in an above-threshold regime rather than needing a fresh breakout.

## What would falsify it

- A rapid macro or crypto-specific selloff that takes Binance BTC/USDT below 70k before or at the April 20 noon ET candle
- Evidence of renewed high volatility with repeated failed attempts to hold above 70k

## Early warning signs

- Consecutive daily closes back below 72k
- Sharp intraday liquidation cascades or exchange-specific stress
- A material drop in BTC across major venues that removes the current cushion

## What changes if this assumption fails

If the regime breaks, the yes case weakens quickly because this contract is decided by one exact minute rather than a broad average or end-of-day range.

## Notes that depend on this assumption

- Main finding for base-rate persona
- Binance and CoinGecko context source note