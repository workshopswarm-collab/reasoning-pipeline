---
type: source_note
case_key: case-20260415-5996483c
dispatch_id: dispatch-case-20260415-5996483c-20260415T193222Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin-threshold-daily-close
entity: btc
topic: Binance BTC/USDT current level and relevant noon-ET candle structure
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 20 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API BTCUSDT ticker and 1m klines
source_type: exchange-primary
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1000
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, 1m-candle, noon-et, primary-source]
---

# Summary

Direct Binance market data shows BTC/USDT trading materially above 70,000 on April 15, with the latest observed close at 74,896.22 around 15:34 ET. The April 15 12:00 ET 1-minute candle closed at 73,792.01, also well above 70,000. This does not settle the April 20 market, but it confirms the current state is comfortably above the threshold and that the governing exchange/source can be queried directly.

## Key facts extracted

- Latest observed Binance BTC/USDT 1-minute close in the pull: 74,896.22 at 2026-04-15 15:34 ET.
- Distance above 70,000 at that observation: 4,896.22 points, about 6.99%.
- Observed April 15 12:00 ET 1-minute candle on Binance BTC/USDT:
  - open: 73,844.07
  - high: 73,844.07
  - low: 73,762.89
  - close: 73,792.01
- The source surface is the same exchange family referenced by contract rules, though the contract specifically cites the Binance trading UI candle close for settlement.

## Evidence directly stated by source

- Binance API returned current ticker price and recent 1-minute klines for BTCUSDT.
- The returned 1-minute candles can be timestamp-mapped into America/New_York to identify the noon ET candle.

## What is uncertain

- The API pull does not prove what the April 20 12:00 ET candle will be.
- The market’s governing source is the Binance trading UI candle close, so API/UI parity is highly likely but still a small operational verification consideration.
- This source alone does not address potential major BTC drawdowns before April 20.

## Why this source may matter

It is the best available direct source for current exchange-traded BTC/USDT levels and for understanding the exact candle mechanism used by the contract.

## Possible impact on the question

Because BTC is already roughly 7% above the threshold five days before settlement, the burden for a No outcome is not merely “BTC weakens somewhat” but “BTC falls below 70,000 exactly into the April 20 noon ET 1-minute close on Binance.” That makes the market’s bullish pricing directionally sensible, though exact contract timing still matters.

## Reliability notes

Primary exchange data, highly recent, and directly tied to the contract’s governing venue. Residual ambiguity is low-to-moderate because the contract names the Binance UI candle close specifically rather than the public API endpoint.