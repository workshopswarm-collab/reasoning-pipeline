---
type: source_note
case_key: case-20260416-b08a3934
dispatch_id: dispatch-case-20260416-b08a3934-20260416T023832Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 72000?
driver: reliability
date_created: 2026-04-15T22:41:00-04:00
source_name: CoinGecko 30-day Bitcoin market chart
source_type: secondary
source_url: https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-b08a3934/researcher-analyses/2026-04-16/dispatch-case-20260416-b08a3934-20260416T023832Z/personas/base-rate.md]
tags: [coingecko, context, base-rate, volatility]
---

# Summary

A 30-day CoinGecko market-chart pull shows Bitcoin has recently spent substantial time in the low-to-mid 70,000s with dips into the low 71,000s and high 72,000s, but is currently back near 75,000. This contextual source supports the view that 72,000 is no longer a far-out upside target; it is now a near-below-spot threshold.

## Key facts extracted

- Recent 30-day BTC/USD prints include periods around 75,000 early in the window.
- The same series also shows pullbacks to roughly the low 71,000s, indicating the threshold is not trivially risk-free.
- Research-time spot context from this secondary source is directionally consistent with Binance: BTC is trading materially above 72,000.

## Evidence directly stated by source

- Historical price points over the last 30 days show BTC has oscillated above and below 72,000 but is currently above it.

## What is uncertain

- CoinGecko uses aggregated market data and BTC/USD rather than Binance BTC/USDT specifically.
- This source is contextual only and cannot settle the contract.
- The exact probability of a >4% downside move by tomorrow noon ET cannot be inferred from this data alone.

## Why this source may matter

It provides an outside-view volatility context: when the threshold is below current spot but within recent trading range, the market should be high probability but not treated as certainty.

## Possible impact on the question

This source modestly supports a bullish resolution by showing the threshold is currently below spot and within recent normal trading territory, while also preserving a nonzero chance of a sharp drop below 72,000 before the settlement minute.

## Reliability notes

Useful as an independent contextual check, but meaningfully weaker than Binance for settlement purposes because it is aggregated and not pair-specific to BTC/USDT on Binance.
