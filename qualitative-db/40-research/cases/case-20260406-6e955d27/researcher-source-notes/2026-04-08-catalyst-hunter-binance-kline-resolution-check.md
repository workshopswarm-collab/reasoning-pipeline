---
type: source_note
case_key: case-20260406-6e955d27
dispatch_id: dispatch-case-20260406-6e955d27-20260408T153555Z
analysis_date: 2026-04-08
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260406-6e955d27 | catalyst-hunter
question: Will the price of Bitcoin be above $66,000 on April 6?
driver: operational-risk
date_created: 2026-04-08
source_name: Binance Spot API kline data and market page rules
source_type: primary
source_url: https://api.binance.com/api/v3/klines
source_date: 2026-04-08
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260406-6e955d27/researcher-analyses/2026-04-08/dispatch-case-20260406-6e955d27-20260408T153555Z/personas/catalyst-hunter.md
tags: [binance, kline, resolution-check, source-of-truth]
---

# Summary

This note verifies the market's governing source of truth directly: Binance BTCUSDT 1-minute klines, with timezone handling aligned to ET as specified by the Polymarket rules.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT 1-minute candle for **12:00 ET** on April 6, using the candle's final **Close** price.
- Binance spot API documentation for `/api/v3/klines` states:
  - klines are uniquely identified by **open time**
  - `interval=1m` is supported
  - `timeZone` can be specified, and interval interpretation follows that timezone
  - `startTime` and `endTime` are interpreted in UTC regardless of `timeZone`
- A direct API query for BTCUSDT with `interval=1m`, `timeZone=-4`, and `startTime=1775491200000` returns the 12:00-12:00:59 ET candle for 2026-04-06.
- Returned kline:
  - open time: `1775491200000`
  - open: `69968.87000000`
  - high: `69974.28000000`
  - low: `69938.58000000`
  - close: `69938.59000000`
  - close time: `1775491259999`
- The close price is well above the threshold of **66,000**.

## Evidence directly stated by source

- Binance docs directly state how klines work, that 1-minute intervals exist, and that a timezone parameter can be used for interval interpretation.
- The API response directly reports the candle close value for the relevant minute.

## What is uncertain

- The Polymarket rules reference the Binance website chart UI rather than the API endpoint. The API is not explicitly named in the rule text.
- However, Binance documentation indicates `uiKlines` and `klines` share parameters/response structure, and the API output is a strong direct verification surface for the underlying candle data.
- I did not independently capture a historical chart screenshot from the Binance web UI due extraction limits on the dynamic page.

## Why this source may matter

This is the clearest authoritative surface for both case-specific checks:
- **verify Binance data feed**
- **check close candle logic**

It reduces ambiguity around which minute counts and what "Close" means operationally.

## Possible impact on the question

This source materially supports a very high Yes probability because it confirms both the resolution mechanism and that the relevant historical candle actually closed at **69,938.59**, far above the strike.

## Reliability notes

- Primary source quality is high because Binance is the governing resolution source.
- Operational ambiguity is low once the 12:00 ET candle is interpreted as the minute opened at 12:00:00 ET and closed at 12:00:59 ET.
- Remaining risk is mostly interface/API parity rather than price-level uncertainty, and the margin above 66,000 is large enough that small display differences would not matter.