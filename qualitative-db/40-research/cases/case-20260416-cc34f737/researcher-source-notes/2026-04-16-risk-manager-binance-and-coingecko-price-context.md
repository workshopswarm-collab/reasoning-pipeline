---
type: source_note
case_key: case-20260416-cc34f737
dispatch_id: dispatch-case-20260416-cc34f737-20260416T162722Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-market-context
entity: ethereum
topic: case-20260416-cc34f737 | risk-manager
question: Will the Binance ETH/USDT 1 minute candle for 12:00 ET on 2026-04-17 close above 2300?
driver: reliability
date_created: 2026-04-16
source_name: Binance public market data plus CoinGecko ETH market snapshot
source_type: exchange/API plus market-data aggregator
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cc34f737/researcher-analyses/2026-04-16/dispatch-case-20260416-cc34f737-20260416T162722Z/personas/risk-manager.md]
tags: [binance, coingecko, ethusdt, spot-price, context]
---

# Summary

This source note records the live market context close to analysis time. It does not settle the contract, but it materially informs path risk and the distance from the 2300 threshold.

## Key facts extracted

- Binance ETHUSDT last price during fetch: 2332.09, with bid/ask around 2332.08/2332.09.
- Binance 24h high/low during fetch: 2385.61 / 2285.10.
- Binance weighted average price over 24h: about 2340.75.
- Recent 1m candles from Binance show ETH/USDT trading in the mid-2330s into the end of the sampled window.
- CoinGecko ETH USD current_price during fetch: 2335.54, 24h high/low 2379.62 / 2291.35, last_updated 2026-04-16T16:29:27Z.

## Evidence directly stated by source

- Binance public API directly stated current ETHUSDT spot price and recent 1m kline closes.
- CoinGecko directly stated a near-contemporaneous ETH/USD reference level and 24h range.

## What is uncertain

- These snapshots do not prove where ETH/USDT will be at noon ET on 2026-04-17.
- CoinGecko is contextual rather than governing because the contract resolves from Binance ETH/USDT only.
- Short-horizon crypto volatility can erase a current cushion quickly.

## Why this source may matter

The key risk question is whether the current buffer above 2300 is large enough relative to overnight/intraday volatility and a single-minute settlement window. This note gives the current cushion and recent range.

## Possible impact on the question

Current pricing modestly supports Yes because ETH/USDT is trading about 32 dollars above 2300, but the 24h low near 2285 shows that the threshold is still within plausible short-horizon downside reach. That makes the main risk not directional impossibility but timing/path fragility.

## Reliability notes

High reliability for Binance current market context because it is direct exchange data. Medium-high reliability for CoinGecko as an independent contextual cross-check rather than settlement source. Independence is moderate because both ultimately reflect the same broader ETH market, but only Binance governs resolution.