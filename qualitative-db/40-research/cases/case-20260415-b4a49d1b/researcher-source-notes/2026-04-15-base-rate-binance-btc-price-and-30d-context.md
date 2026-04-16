---
type: source_note
case_key: case-20260415-b4a49d1b
dispatch_id: dispatch-case-20260415-b4a49d1b-20260415T000939Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-14
source_name: Binance spot BTCUSDT API surfaces
source_type: exchange_market_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: base-rate
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-b4a49d1b/researcher-analyses/2026-04-15/dispatch-case-20260415-b4a49d1b-20260415T000939Z/personas/base-rate.md]
tags: [source-note, binance, btc, market-data, resolution-context]
---

# Summary

Binance spot data is the governing source family for this market because resolution depends on the Binance BTC/USDT 1-minute candle close at 12:00 ET on April 20. A current ticker pull showed BTCUSDT at 74,567.09 around 2026-04-15 00:10 UTC, and the recent 30 daily candles show BTC trading above 70,000 on a substantial share of recent days, including several closes in the low-to-mid 70k range.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT = 74,567.09.
- Recent Binance daily closes include multiple closes above 70,000, with latest visible daily close at 74,567.09 for the still-open April 15 UTC day.
- Over the visible 30-day series, BTC spent meaningful time both above and below 70,000, so 70k is not a trivial threshold but also not an extreme upside tail relative to current spot.
- Recent sequence shows BTC recovering from sub-70k closes in late March / early April into the current mid-70k area.

## Evidence directly stated by source

- Direct current price from Binance spot ticker.
- Direct recent daily OHLC data from Binance klines endpoint.

## What is uncertain

- The market resolves on the Binance 1-minute candle close at exactly 12:00 ET on April 20, not on current spot or daily closes.
- Daily candle data is UTC-based and therefore contextual rather than settlement-direct for the exact contract timestamp.
- Short-horizon crypto volatility can move several percentage points before resolution.

## Why this source may matter

This is the closest available direct source to the contract’s source of truth. It grounds whether the market’s 86% implied probability is broadly consistent with where BTC currently trades versus the 70k threshold.

## Possible impact on the question

Current spot roughly 6.5% above the threshold supports a high yes probability over a 5-day horizon, but not certainty. The key implication is that the market is pricing continuation from an already above-threshold starting point, not a major upside move from below 70k.

## Reliability notes

- High relevance because Binance is the named resolution source.
- API output is machine-readable and direct, but this note still does not directly verify the exact 12:00 ET candle that will matter at resolution.
- Daily candles are contextual only; exact settlement will depend on the 1-minute candle close on the specific date and time.