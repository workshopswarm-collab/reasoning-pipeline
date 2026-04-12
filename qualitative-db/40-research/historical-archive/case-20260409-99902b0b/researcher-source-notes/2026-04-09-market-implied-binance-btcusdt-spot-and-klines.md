---
type: source_note
case_key: case-20260409-99902b0b
dispatch_id: dispatch-case-20260409-99902b0b-20260409T203957Z
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: exchanges
entity: binance
topic: case-20260409-99902b0b | market-implied
question: Will the price of Bitcoin be above $70,000 on April 10?
driver: liquidity
date_created: 2026-04-09
source_name: Binance API BTCUSDT ticker and 1m klines
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-09
credibility: high
recency: live
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [binance, btc, bitcoin]
related_drivers: [liquidity, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-99902b0b/researcher-analyses/2026-04-09/dispatch-case-20260409-99902b0b-20260409T203957Z/personas/market-implied.md]
tags: [binance, btcusdt, resolution-source, live-price]
---

# Summary

Binance is the governing resolution venue for this contract, and its own API shows BTC/USDT trading well above $70,000 shortly before the assignment time. The last-10-minute 1m kline sequence also shows spot trading in a narrow band around $72.3k-$72.4k, well above the threshold.

## Key facts extracted

- Binance ticker endpoint returned `BTCUSDT` price `72363.48`.
- Binance 1m klines for the last 10 minutes covered 20:31-20:40 UTC on 2026-04-09.
- The listed 1m closes were all above $72,300 in that interval.
- The contract resolves on the Binance 1-minute candle for `12:00` ET on 2026-04-10, so venue-specific Binance pricing matters more than generic BTC/USD references.

## Evidence directly stated by source

- Ticker response: `{"symbol":"BTCUSDT","price":"72363.48000000"}`.
- Example close values from the recent 1m kline data: `72325.54`, `72354.19`, `72407.87`, `72436.32`, `72411.31`, `72392.38`, `72387.18`, `72374.99`, `72383.78`, `72362.65`.

## What is uncertain

- This is only a spot snapshot about 15 hours before the resolution minute; it does not directly settle the noon ET April 10 close.
- Intraday crypto volatility could still move BTC/USDT below $70,000 by the resolution minute.
- API spot/ticker and visible chart close should usually align, but the contract text points specifically to the Binance chart candle close at 12:00 ET.

## Why this source may matter

This is the primary source family because the contract explicitly resolves to Binance BTC/USDT 1-minute candle close data. It directly informs both the current distance from the threshold and the correct venue/mechanics for settlement.

## Possible impact on the question

This source strongly supports the market's high yes probability because current Binance spot is roughly $2.36k above the threshold, implying a meaningful buffer. It does not eliminate overnight or morning downside risk, but it shows the market is not pricing yes off an already-marginal spot level.

## Reliability notes

- High reliability for venue-specific current price context because Binance is the stated resolution source.
- For final settlement, the chart-visible 12:00 ET 1m candle close remains the ultimate governing datapoint, so this API note is highly relevant but still pre-resolution.