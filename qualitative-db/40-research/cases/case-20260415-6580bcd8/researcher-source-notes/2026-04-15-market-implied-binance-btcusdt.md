---
type: source_note
case_key: case-20260415-6580bcd8
dispatch_id: dispatch-case-20260415-6580bcd8-20260415T081158Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on April 17, 2026?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTC/USDT API snapshot and recent hourly candles
source_type: exchange data / market data API
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: real-time
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-6580bcd8/researcher-analyses/2026-04-15/dispatch-case-20260415-6580bcd8-20260415T081158Z/personas/market-implied.md]
tags: [binance, btcusdt, market-data, resolution-source]
---

# Summary

Binance spot data shows BTC/USDT trading at 73846.60000000 around the time of research, comfortably above the 72,000 threshold, while the last ~3 days of hourly candles show BTC spending nearly all hours above 72,000 after a breakout on April 13.

## Key facts extracted

- Spot ticker snapshot returned BTCUSDT at 73846.60000000 on 2026-04-15.
- Recent hourly candles show a move from roughly 70.7k-71.2k on April 13 UTC into repeated 74k-76k prints on April 14 UTC.
- The lowest hourly low in the displayed April 14-15 segment stayed above 73.5k after the breakout matured, leaving a multi-thousand-dollar cushion versus the 72k strike.
- The relevant contract source is Binance BTC/USDT specifically, matching the market rules.

## Evidence directly stated by source

- Binance ticker endpoint directly states the current BTC/USDT spot price.
- Binance kline endpoint directly states historical open/high/low/close values for each 1-hour bar.

## What is uncertain

- The contract resolves on the 12:00 ET one-minute candle close on April 17, not the current spot price or hourly bars.
- A fast selloff of more than roughly 1.8k by the resolution minute would still flip the outcome.
- API snapshots do not by themselves prove the web trading UI will show identical formatting at resolution time, though both are Binance source surfaces.

## Why this source may matter

This is the closest available authoritative source to the stated settlement source because it comes directly from Binance and references the exact BTC/USDT market the contract uses.

## Possible impact on the question

The source strongly supports the market's high Yes probability because BTC is already trading materially above 72k with recent realized price action mostly above the strike. It mainly informs baseline distance-to-strike and source-of-truth compatibility, not guaranteed resolution.

## Reliability notes

Direct exchange data is high-value for this case because the rules explicitly name Binance BTC/USDT. Remaining risk comes from timing: the contract keys off one future minute close, so current pricing has high but not perfect probative value.
