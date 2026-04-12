---
type: source_note
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: crypto
subdomain: market-structure-and-resolution
entity: ethereum
topic: ethereum-above-2100-on-april-10
question: Will the price of Ethereum be above $2,100 on April 10?
driver: operational-risk
date_created: 2026-04-09
source_name: Binance spot API docs + live public API
source_type: primary-plus-verification
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [catalyst-hunter.md, catalyst-hunter.sidecar.json]
tags: [binance, resolution-source, kline, source-note]
---

# Summary

This note captures the governing resolution mechanics from Polymarket's stated rules and the matching Binance public API behavior used for verification.

## Key facts extracted

- Polymarket says the market resolves from the Binance ETH/USDT 1 minute candle for 12:00 in ET timezone (noon) on the target date, using the final Close price.
- Binance spot API docs say `/api/v3/klines` returns kline/candlestick bars and that klines are uniquely identified by their open time.
- Binance docs also say the `timeZone` parameter changes how intervals are interpreted, while `startTime` and `endTime` remain interpreted in UTC regardless of `timeZone`.
- Live Binance public API returned current `serverTime`, confirming Binance exposes a direct server-time surface for UTC alignment checks.
- Live Binance public API returned 1-minute ETHUSDT klines with 60,000 ms candle spacing and close times ending in `...9999`, consistent with standard one-minute candle construction.

## Evidence directly stated by source

- Binance docs: klines are uniquely identified by their open time.
- Binance docs: supported `timeZone` includes offsets like `-4` and `-1:00`.
- Binance docs: `startTime` and `endTime` are always interpreted in UTC, regardless of `timeZone`.
- Binance live API sample on 2026-04-09 returned recent ETHUSDT 1m candles around 2211-2213 with open times and close times exactly one minute apart.

## What is uncertain

- Binance docs do not separately explain the exact web-chart UI selection mechanics for "12:00 in ET timezone" on the retail trading page beyond the general kline API behavior.
- Because the target resolution time is in the future relative to this run, the actual deciding candle close cannot yet be observed.

## Why this source may matter

This is the clearest source-of-truth surface for contract mechanics. It anchors the interpretation that the decisive candle is the one whose open time is 12:00:00 ET on Apr 10, 2026, with final close price taken at the end of that one-minute interval.

## Possible impact on the question

This sharply limits relevant catalysts to events capable of moving ETH/USDT before or during the minute ending 12:00:59 ET on Apr 10. It also reduces ambiguity about timezone handling: ET noon on Apr 10, 2026 corresponds to 16:00 UTC if Eastern Daylight Time remains in effect, which it does on that date.

## Reliability notes

- High reliability for mechanics: Binance is the named resolution source and its public docs plus live endpoint behavior align.
- Independence is limited because both the docs and live endpoint are Binance surfaces, but that is acceptable here because the contract itself names Binance as the governing source.
- This source does not answer where ETH will trade tomorrow; it only clarifies how the market will be judged.
