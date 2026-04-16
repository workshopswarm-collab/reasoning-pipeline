---
type: source_note
case_key: case-20260415-2cba3460
dispatch_id: dispatch-case-20260415-2cba3460-20260415T115730Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-2cba3460 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance spot market data/docs
source_type: primary_and_contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2cba3460/researcher-analyses/2026-04-15/dispatch-case-20260415-2cba3460-20260415T115730Z/personas/market-implied.md]
tags: [source-note, polymarket, binance, btc]
---

# Summary

This note captures the direct contract mechanics and a same-morning check of Binance BTC/USDT spot pricing versus the $72,000 strike. The market is explicitly keyed to the Binance BTC/USDT 1-minute candle labeled 12:00 ET on Apr 16, not to any other exchange or broader daily close.

## Key facts extracted

- Polymarket rules state the market resolves "Yes" if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr 16 has a final close strictly higher than 72,000.
- Polymarket rules also specify that price precision is determined by the source and that the relevant source is Binance BTC/USDT with 1m candles.
- Binance spot ticker at approximately 07:58 ET on Apr 15 showed BTCUSDT around 74,187.70.
- Recent Binance 1m klines around 11:54-11:58 UTC on Apr 15 showed closes between roughly 74,173 and 74,223, comfortably above 72,000.
- Binance 24hr ticker check showed last price around 74,163.79, daily high 76,038, low 73,514, so even the 24h low remained above 72,000.
- Binance documentation for `/api/v3/klines` confirms the close price field and notes that `timeZone` can be specified for candle interval interpretation, while `startTime`/`endTime` remain UTC.

## Evidence directly stated by source

- Direct from Polymarket page: resolution is based on Binance BTC/USDT 1-minute candle close at 12:00 ET on the specified date.
- Direct from Binance docs: kline response contains a close price field and supports timezone-aware interval interpretation.
- Direct from Binance API checks: current spot and recent minute closes are materially above the 72,000 threshold.

## What is uncertain

- This source set does not settle the Apr 16 noon ET outcome yet; it only establishes current distance from strike and confirms mechanics.
- There is some operational ambiguity between the chart UI language in Polymarket rules and programmatic Binance endpoints; however, both appear to reference the same 1-minute candle structure.
- A large intraday move before tomorrow noon ET could still take BTC below 72,000.

## Why this source may matter

This is the core provenance for both the market's high implied probability and the main residual risk. The contract is narrow and date-sensitive, so verifying the exact resolution mechanics and current distance from the strike matters more than broad macro commentary.

## Possible impact on the question

The direct source check supports why the market is priced near 88.5%: BTC is already about 3% above the strike with the entire last 24h trading range still above 72,000 on Binance. That does not make "Yes" certain, but it makes the current market confidence look broadly defensible absent a sharp downside move before noon ET tomorrow.

## Reliability notes

- Polymarket is authoritative for contract wording but not for the future result.
- Binance is the governing source of truth for settlement data.
- Binance API documentation is a strong contextual source for interpreting candle fields and timing.
- CoinGecko and similar aggregators are useful only as secondary context because the contract is Binance-specific.
