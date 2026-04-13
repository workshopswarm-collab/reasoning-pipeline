---
type: source_note
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-13
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-13 close above 70000?
driver: reliability
date_created: 2026-04-13
source_name: Binance public API verification pass
source_type: exchange-api
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&endTime=1776088260000&limit=5
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
downstream_uses: [qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/risk-manager.md]
tags: [binance, api, verification, btcusdt]
---

# Summary

This verification pass confirmed Binance API availability and demonstrated how 1-minute BTC/USDT klines are timestamped, but it did not directly return the future 12:00 ET candle needed for settlement at the time of research.

## Key facts extracted

- Binance server time at fetch was 1776088209663 ms, roughly 2026-04-13 13:50:09 UTC, which is about 09:50 ET.
- Recent Binance 1-minute klines were available and showed BTC/USDT trading above 70,000 during the sampled pre-noon window.
- The requested future noon ET candle was unavailable because the market had not yet reached the resolving minute.

## Evidence directly stated by source

- Binance API exposes 1-minute kline data with open time, close time, and Close fields.
- The sampled minutes around 09:46-09:50 ET had closes between about 70,964 and 71,609.

## What is uncertain

- This is not direct evidence of the noon ET settling candle; it is only contextual evidence that spot price was comfortably above 70,000 about 2 hours and 10 minutes before resolution.
- Intraday volatility could still take BTC below 70,000 by the resolving minute.

## Why this source may matter

It is the closest accessible authoritative source class to the final settlement source and reduces ambiguity about contract mechanics, timestamping, and whether BTC was meaningfully above the strike before noon.

## Possible impact on the question

This supports a high Yes probability but leaves meaningful path risk: the contract is about one exact minute close, not average price or earlier trading range.

## Reliability notes

High credibility as direct Binance data, but only medium sufficiency for this pre-resolution question because it cannot yet settle the noon ET outcome. The key remaining risk is timing, not data-source quality.