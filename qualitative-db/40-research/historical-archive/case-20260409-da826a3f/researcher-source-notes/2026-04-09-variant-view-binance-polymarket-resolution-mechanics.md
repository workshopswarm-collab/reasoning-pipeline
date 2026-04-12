---
type: source_note
case_key: case-20260409-da826a3f
dispatch_id: dispatch-case-20260409-da826a3f-20260409T211410Z
analysis_date: 2026-04-09
persona: variant-view
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-68k-on-april-10
question: Will the price of Bitcoin be above $68,000 on April 10?
driver: operational-risk
date_created: 2026-04-09
source_name: Polymarket market rules plus Binance UIKlines timing check
source_type: primary-rule-plus-direct-exchange-api-check
source_url: https://polymarket.com/event/bitcoin-above-on-april-10
source_date: 2026-04-09
credibility: medium-high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-da826a3f/researcher-analyses/2026-04-09/dispatch-case-20260409-da826a3f-20260409T211410Z/personas/variant-view.md]
tags: [source-note, polymarket, binance, resolution-mechanics, timezone]
---

# Summary

This note captures the core resolution mechanics for the April 10 BTC>$68k market and the timing checks that matter most for avoiding a false read. The main point is that the governing source of truth is the Binance BTC/USDT 1-minute candle labeled 12:00 in ET, which maps to 16:00 UTC on 2026-04-10 because New York is on EDT (UTC-4).

## Key facts extracted

- Polymarket rules say the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on April 10 has a final Close strictly higher than 68,000.
- The cited resolution source is Binance BTC/USDT with 1m candles selected.
- ET on 2026-04-10 is EDT, so 12:00 ET = 16:00 UTC.
- A direct time conversion check gives the 12:00 ET candle open timestamp as 1775836800000 ms, with close timestamp 1775836859999 ms.
- A direct Binance `uiKlines` API query using `timeZone=-4` and the relevant window returned an empty array when asked for future candles on 2026-04-10 from the current date of 2026-04-09. That is expected because the target candle has not occurred yet, but it does confirm the endpoint accepts the timing format without surfacing an alternate timezone interpretation.

## Evidence directly stated by source

- Polymarket directly states the resolution mechanics, source, pair, interval, comparison operator, and precision convention.
- Binance API behavior directly supports that candle retrieval is time-window based and that future candles are not yet available.

## What is uncertain

- The exact final close value is not yet observable as of this research run because the target candle is in the future.
- Polymarket references the Binance web UI as the resolution source, while this check used the Binance API for timing validation rather than the final settlement print itself.
- The precise web-UI candle label convention cannot be fully confirmed until the relevant candle exists and can be inspected directly.

## Why this source may matter

This is the core source note because the case is rule-sensitive and time-sensitive rather than thesis-sensitive. The main risk is not misunderstanding Bitcoin trend direction; it is misunderstanding which candle, timezone, or close field actually governs settlement.

## Possible impact on the question

Correctly mapping 12:00 ET to 16:00 UTC reduces one of the main ways this market could be misread. It supports a high-confidence procedural interpretation that the market is really asking whether the Binance BTC/USDT close for the 16:00 UTC one-minute candle on 2026-04-10 exceeds 68,000.

## Reliability notes

- Polymarket is authoritative for contract wording.
- Binance is authoritative for the underlying price print.
- Evidence independence is limited because both sources are part of the same settlement chain rather than independent market evidence.
- For directional forecasting, this note is high value for mechanics and only moderate value for price direction.