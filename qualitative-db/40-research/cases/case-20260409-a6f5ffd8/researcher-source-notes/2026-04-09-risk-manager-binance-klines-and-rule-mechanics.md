---
type: source_note
case_key: case-20260409-a6f5ffd8
dispatch_id: dispatch-case-20260409-a6f5ffd8-20260409T071326Z
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: btc
topic: case-20260409-a6f5ffd8 | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 9?
driver: operational-risk
date_created: 2026-04-09
source_name: Binance spot API klines docs and live BTCUSDT endpoints
source_type: primary + contextual
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/risk-manager.md]
tags: [binance, klines, resolution-mechanics, timezone, btcusdt]
---

# Summary

This source note captures the authoritative Binance mechanics relevant to a Polymarket contract that resolves on the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-09.

## Key facts extracted

- Binance Spot API docs state that `GET /api/v3/klines` returns kline/candlestick bars and that klines are uniquely identified by their **open time**.
- The response schema explicitly includes both **open time** and **close time**, with close time equal to the end of the minute minus 1 ms.
- Binance docs state the optional `timeZone` parameter changes how **kline intervals are interpreted**, but `startTime` and `endTime` are still interpreted in **UTC regardless of timeZone**.
- A local ET-to-UTC conversion for 2026-04-09 12:00:00 America/New_York yields **2026-04-09 16:00:00 UTC**, Unix ms **1775750400000**.
- Live Binance spot ticker at research time showed BTC/USDT around **71045.86**, modestly above 70,000.
- Recent live 1-minute BTCUSDT klines fetched from Binance were available and formatted consistently with the docs; this confirms the endpoint shape and close-price field behavior, though the target future candle was not yet available.

## Evidence directly stated by source

- Binance docs: klines are uniquely identified by their open time.
- Binance docs: response field 5 is the candle close price, and response field 6/7 include volume/close time.
- Binance docs: if `timeZone` is provided, interval boundaries are interpreted in that timezone, but `startTime`/`endTime` remain UTC.

## What is uncertain

- Polymarket wording says the market resolves to the Binance 1-minute candle for BTC/USDT “12:00 in the ET timezone (noon),” but does not itself clarify whether the relevant bar is identified by the minute’s **open label** or by the minute whose **close occurs at noon**. Binance docs strongly imply the standard interpretation should be the candle with open time 12:00 ET / 16:00 UTC.
- The public Binance web chart wording on the UI can sometimes be less explicit than the API docs, leaving a mild user-interface interpretation risk even though the API mechanics are clear.

## Why this source may matter

This is the governing source class for the contract. The market is effectively a narrow-resolution timing/mechanics question rather than a broad Bitcoin thesis question.

## Possible impact on the question

The key practical implication is that the settlement should hinge on the BTCUSDT 1-minute candle opening at **12:00:00 ET / 16:00:00 UTC** and closing at **12:00:59.999 ET / 16:00:59.999 UTC**, with the decisive value being that candle’s **final close price**. Since BTC was already trading above 70k during the research window, the main remaining risks are timing/path risk and any residual interpretation ambiguity around which exact minute Polymarket chooses.

## Reliability notes

- Primary source quality: high. Binance is the named settlement source and its API docs are authoritative for kline mechanics.
- Independence: limited, because the settlement source and the mechanics source are both Binance-related; this is acceptable here because the contract itself is single-source by design.
- Operational caveat: because the market is timestamp-sensitive and settles on one minute close, even a small intraminute move matters disproportionately.