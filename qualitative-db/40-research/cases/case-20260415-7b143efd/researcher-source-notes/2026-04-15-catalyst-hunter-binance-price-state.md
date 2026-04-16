---
type: source_note
case_key: case-20260415-7b143efd
dispatch_id: dispatch-case-20260415-7b143efd-20260415T132144Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT API spot price and recent candles
source_type: exchange API / direct market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7b143efd/researcher-analyses/2026-04-15/dispatch-case-20260415-7b143efd-20260415T132144Z/personas/catalyst-hunter.md]
tags: [binance, spot-price, candles, direct-evidence, market-state]
---

# Summary

This source provides direct exchange data from Binance, the contract’s stated source of truth, showing BTC/USDT already materially above 70,000 on 2026-04-15 and offering a recent-volatility frame for the catalyst window.

## Key facts extracted

- Binance BTC/USDT last price on fetch was about 74,422.
- Binance 5-minute average price endpoint returned about 74,355.
- 24-hour range was roughly 73,514 to 76,038.
- Daily candles from April 5 to April 14 show BTC closing above 70,000 on most recent days in the run-up to the target date.
- Recent daily closes included roughly 72,962 on Apr 9, 73,043 on Apr 10, 70,741 on Apr 11, 74,418 on Apr 12, 74,132 on Apr 13, and 74,416 partial on Apr 14/15 API window.

## Evidence directly stated by source

- Direct Binance API responses for ticker price, average price, 24-hour stats, and recent klines.

## What is uncertain

- The contract resolves on a specific future 12:00 ET one-minute close, so current price only gives distance-to-threshold and volatility context, not a settled answer.
- API timestamps are in Unix milliseconds and need interpretation relative to ET for exact candle mapping on resolution day.

## Why this source may matter

Because Binance is the named resolution source, current and recent Binance price behavior is the most decision-relevant direct evidence. It shows the market currently has a roughly 4.4k cushion above the 70k threshold, meaning only a material downside move over the next five days would flip the contract to No.

## Possible impact on the question

Directly supports a high Yes probability while also framing the key remaining catalyst question: whether any macro or crypto-specific event before April 20 noon ET can plausibly drive a more than ~6% downside move from current Binance levels.

## Reliability notes

High reliability for present market state because it is direct exchange data from the named source of truth. Lower relevance for terminal settlement than the eventual April 20 noon ET candle itself.