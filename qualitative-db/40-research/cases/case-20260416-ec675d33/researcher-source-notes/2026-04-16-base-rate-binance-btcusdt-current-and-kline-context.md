---
type: source_note
case_key: case-20260416-ec675d33
dispatch_id: dispatch-case-20260416-ec675d33-20260416T073538Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance BTCUSDT API and market contract page
source_type: exchange API + market rules page
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-ec675d33/researcher-analyses/2026-04-16/dispatch-case-20260416-ec675d33-20260416T073538Z/personas/base-rate.md]
tags: [binance, btcusdt, contract-rules, source-note]
---

# Summary

This note records the direct settlement-relevant source and nearby price context for the April 20 BTC > 72,000 market.

## Key facts extracted

- The contract resolves using the Binance BTC/USDT 1-minute candle for **12:00 PM America/New_York** on **2026-04-20**.
- 12:00 PM ET on 2026-04-20 equals **16:00 UTC**.
- A spot Binance API check on 2026-04-16 showed BTC/USDT at **74,864.10**.
- A Binance 90-day daily-close pull showed BTC daily closes above 72,000 on **29 of 90 days** (~32.2%).
- A Binance 365-day daily-close pull showed BTC daily closes above 72,000 on **304 of 365 days** (~83.3%).
- The current streak of daily closes above 72,000 in the 365-day pull was **4 days**.
- A 30-day daily-bar sample implied average absolute daily return around **1.69%**, which is large enough that a ~3.8% move over four days is very plausible in either direction.

## Evidence directly stated by source

- Binance ticker API returned `{"symbol":"BTCUSDT","price":"74864.10000000"}`.
- Binance 1-minute kline API returned recent BTCUSDT candles, confirming an accessible direct source for minute-candle close series.
- Polymarket rules page explicitly states the governing source is Binance BTC/USDT with 1m candles and the resolving candle is the **12:00 ET** candle on the date in the title.

## What is uncertain

- The live spot/ticker price on 2026-04-16 is not itself the resolving value; only the exact 12:00 ET candle close on 2026-04-20 matters.
- Daily closes are only a base-rate proxy for the threshold and do not directly measure the exact noon ET minute close.
- The market may move materially before resolution if BTC weakens over the remaining four days.

## Why this source may matter

This is the highest-quality direct evidence because it identifies both the exact settlement surface and current distance from the strike on that same exchange/pair.

## Possible impact on the question

The direct source supports a bullish default because BTC is already above 72,000 on the governing venue, but the historical/volatility context argues against treating an 84-85% implied probability as close to certain with four days left.

## Reliability notes

- Binance is the explicit source of truth for settlement, so source-of-truth ambiguity is low.
- There is still operational detail risk because settlement depends on one exact 1-minute candle at one exact timezone-converted timestamp.
- The daily-close base-rate context is structurally useful but not fully independent from the same exchange data family.