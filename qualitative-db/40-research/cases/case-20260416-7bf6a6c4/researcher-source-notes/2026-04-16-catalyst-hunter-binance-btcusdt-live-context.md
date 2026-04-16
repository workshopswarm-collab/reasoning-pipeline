---
type: source_note
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Binance BTC/USDT live spot and recent intraday range before Apr 17 noon ET close market
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on Apr 17 close above 74000?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance Spot API
authoritative source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15T22:56:23-04:00
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, binance, btc, threshold-market, live-price]
---

# Summary

Binance live BTC/USDT data shows BTC already trading above the 74000 threshold during the evening before the Apr 17 noon ET settlement minute, but the market resolves on the specific Binance 1-minute **close** at 12:00 ET on Apr 17 rather than on any earlier trade or high.

## Key facts extracted

- Binance spot ticker returned BTCUSDT at roughly 74912-74946 during collection.
- Binance 24h ticker returned:
  - lastPrice: 74946.49
  - openPrice: 74327.42
  - highPrice: 75425.00
  - lowPrice: 73514.00
  - priceChangePercent: 0.833
- Recent 1-minute kline pulls showed BTC/USDT staying mostly in the high-74k / low-75k area during the observed window.
- A larger kline pull showed an observed recent range in the fetched sample of about 73580.85 to 75425.00, roughly a 2.5% swing range.

## Evidence directly stated by source

- Binance API directly provides the live BTC/USDT ticker and recent 1-minute candles.
- The direct governing venue named by the contract is Binance BTC/USDT.

## What is uncertain

- These observations do not prove what the Apr 17 12:00 ET 1-minute candle close will be.
- I did not capture the future governing candle because it has not occurred yet.
- The exact ET-to-Binance chart alignment still needs to be applied at resolution time; this note is pre-resolution context, not settlement proof.

## Why this source may matter

This is the most relevant direct venue/source because the contract explicitly resolves on Binance BTC/USDT, not on a broader BTC index or another exchange.

## Possible impact on the question

Being already above 74000 with only modest distance from spot to threshold supports a Yes-leaning pre-resolution view. But because the contract uses a specific future 1-minute close, this source mainly shows that the threshold is currently in-range rather than settled.

## Reliability notes

- High reliability for direct venue pricing context because Binance is the governing source.
- Medium reliability for forecasting the Apr 17 noon close because spot can move materially in a 24/7 market before the specific settlement minute.