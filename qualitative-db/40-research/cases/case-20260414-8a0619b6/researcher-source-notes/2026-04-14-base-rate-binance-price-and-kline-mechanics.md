---
type: source_note
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-8a0619b6 | base-rate
question: Will the price of Bitcoin be above $70,000 on April 18?
driver: reliability
date_created: 2026-04-14
source_name: Binance spot API docs and BTCUSDT market data
source_type: exchange docs + exchange market data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8a0619b6/researcher-analyses/2026-04-14/dispatch-case-20260414-8a0619b6-20260414T194140Z/personas/base-rate.md]
tags: [binance, api, btcusdt, klines, price-history]
---

# Summary

Binance documentation confirms that kline/candlestick data is available at 1-minute resolution and identified by open time, with a timezone parameter available for interval interpretation. Live Binance spot data showed BTC/USDT around 74,159 on April 14. Recent daily data from Binance indicates BTC has been above 70k often, but not at anything close to a 90% frequency on a strict close basis in 2026 so far.

## Key facts extracted

- Binance documents `/api/v3/klines` for candlestick data, including `interval=1m`.
- Binance states klines are uniquely identified by their open time.
- Binance docs allow a `timeZone` parameter for interval interpretation, while noting `startTime` and `endTime` are interpreted in UTC.
- Live Binance ticker data on 2026-04-14 showed BTCUSDT at 74,159.48.
- Using Binance daily kline history, BTC daily closes above 70k occurred 60 of 104 days in 2026 through April 14 (~57.7%).
- In the most recent 30 daily closes through April 14, BTC closed above 70k on 15 of 30 days.
- Recent closes were mixed: Apr 12 close 70,740.98; Apr 13 close 74,417.99; Apr 14 latest close in retrieved series 74,114.39.

## Evidence directly stated by source

- Binance docs: klines are available for `1m` interval and identified by open time.
- Binance API ticker: BTCUSDT spot price was 74,159.48 at fetch time.
- Binance daily historical market data directly provides recent close/high/low values used for base-rate framing.

## What is uncertain

- Daily close frequency is only an approximation for the actual contract, which is a single noon-ET minute close.
- The exact April 18 noon ET candle cannot be observed yet, so current evidence is indirect for resolution and direct only for current level and mechanics.
- API docs help verify mechanics but do not by themselves prove how the website chart UI labels the noon-ET candle.

## Why this source may matter

This source is the most relevant independent check on both the governing exchange and the structural prior. It shows that the threshold is currently in-the-money, but also that remaining above 70k on a specific future timestamp is materially less certain than the market's 90% implies.

## Possible impact on the question

Because BTC is currently around 74k, the event is favored. But historical frequency from recent Binance data suggests a disciplined outside-view estimate should still leave meaningful room for a drop below 70k by the relevant minute, especially given BTC's several-thousand-dollar short-horizon swings.

## Reliability notes

Binance is the governing exchange and therefore high-quality for mechanics and price data. Independence versus Polymarket is high because this is the underlying source of truth rather than a derivative market page. The main limitation is that daily kline history is contextual rather than a direct read of the eventual resolving 1-minute candle.