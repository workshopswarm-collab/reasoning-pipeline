---
type: source_note
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 15, 2026 close above 72000?
driver: reliability
date_created: 2026-04-13
source_name: Binance spot API docs plus live BTCUSDT data
source_type: exchange documentation and live market data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-13
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
downstream_uses: [risk-manager.md, risk-manager.md#source-quality-assessment]
tags: [binance, api, klines, btcusdt, timing]
---

# Summary

Binance documentation confirms that 1-minute klines are uniquely identified by open time and that the close price is an explicit returned field. Live Binance spot data at review time showed BTC/USDT around 73.8k, modestly above the 72k threshold with roughly 42 hours left until the deciding noon ET candle.

## Key facts extracted

- Binance `GET /api/v3/klines` returns a 1-minute candle series with explicit open time and close price fields.
- Klines are uniquely identified by open time.
- The docs allow a `timeZone` parameter for interpreting candle intervals in non-UTC timezones, while `startTime` and `endTime` remain UTC.
- Live Binance BTC/USDT spot data at review time printed about 73,825.51.
- Recent 1-minute candles around review time were trading in the 73.4k-73.9k area, showing current cushion above 72k but also normal intraday movement in the hundreds of dollars.

## Evidence directly stated by source

- Binance docs: "Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time."
- Binance docs response schema includes close price as the fifth field in each kline.
- Binance ticker endpoint returned BTCUSDT around 73825.51 at review time.

## What is uncertain

- The live ticker is only a spot snapshot, not evidence about the settlement candle 42 hours later.
- API docs explain mechanics but do not directly settle which exact API call Polymarket will use if there is any UI/API discrepancy.
- No independent macro/news catalyst source was added in this pass, so the directional probability is anchored mainly on current price cushion and ordinary BTC volatility/path risk.

## Why this source may matter

It helps verify the rule can be operationalized cleanly and gives direct, exchange-native context for whether the threshold is currently in or out of the money.

## Possible impact on the question

Because BTC was already above 72k on Binance by about 1.8k at review time, the base directional lean is toward Yes. But the market still hinges on one exact minute nearly two days away, so path dependence and volatility remain the central downside risks.

## Reliability notes

High for exchange mechanics and live exchange-native pricing. Weak as a standalone forecasting source because it does not independently estimate future BTC distribution by the settlement minute.