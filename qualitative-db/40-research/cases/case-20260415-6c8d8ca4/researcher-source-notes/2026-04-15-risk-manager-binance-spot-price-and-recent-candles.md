---
type: source_note
case_key: case-20260415-6c8d8ca4
dispatch_id: dispatch-case-20260415-6c8d8ca4-20260415T084705Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close on April 17 above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Binance API ticker and 1-minute klines
source_type: exchange primary data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-6c8d8ca4/researcher-analyses/2026-04-15/dispatch-case-20260415-6c8d8ca4-20260415T084705Z/personas/risk-manager.md]
tags: [binance, primary-data, btcusdt, spot-price, candles]
---

# Summary

This source provides direct Binance BTC/USDT spot pricing context and recent 1-minute candle data from the same venue family named in the contract.

## Key facts extracted

- Binance ticker endpoint showed BTCUSDT at 74,037.08 at fetch time.
- Recent 1-minute klines fetched from Binance were clustered around 74,033 to 74,095.
- This places spot roughly 2,037 points above the 72,000 strike about two days before resolution.
- The recent candles show minute-level noise of tens of dollars, not thousands, over the sampled window.

## Evidence directly stated by source

- Ticker payload: `{ "symbol": "BTCUSDT", "price": "74037.08000000" }`
- Recent 1-minute close values in fetched kline sample included approximately 74,059.79, 74,033.29, 74,046.19, 74,037.09.

## What is uncertain

- This is only a spot snapshot plus a very short candle sample, not a full realized-volatility study.
- The exact settlement print is for April 17 at 12:00 ET, so current price only informs distance-to-strike and path risk.
- The API endpoint is not literally the same UI surface named in the rules, though it is direct Binance market data.

## Why this source may matter

As a direct Binance source, it grounds the case in the actual venue and pair that will settle the contract. It also frames the key downside question as whether BTC can fall more than ~2.7% from the observed level before the relevant noon ET minute close.

## Possible impact on the question

The current buffer above 72,000 supports the market's bullish lean, but the key risk remains path/timing sensitivity: a relatively modest crypto drawdown into the specific settlement minute would be enough to flip the market to No.

## Reliability notes

Strong primary venue data for current conditions, but still only contextual for the future settlement minute; it should be paired with explicit contract wording and broader market-risk interpretation.