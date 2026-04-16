---
type: source_note
case_key: case-20260415-8b112bd4
dispatch_id: dispatch-case-20260415-8b112bd4-20260415T153012Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-8b112bd4 | risk-manager
question: Will the Binance BTC/USDT 1-minute candle for 2026-04-16 12:00 ET close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance spot API market-data docs
source_type: primary_and_resolution_method
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: risk-manager
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8b112bd4/researcher-analyses/2026-04-15/dispatch-case-20260415-8b112bd4-20260415T153012Z/personas/risk-manager.md]
tags: [source-note, polymarket, binance, contract-interpretation, kline]
---

# Summary

This source pair establishes the governing resolution mechanics and the exact data object that matters: the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16, using the final Close value, with price precision determined by Binance's displayed precision.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance 1-minute candle for BTC/USDT at 12:00 ET on April 16 has a final Close price higher than 70,000.
- Polymarket explicitly says the source is Binance BTC/USDT, not other exchanges or other trading pairs.
- Binance API documentation states `/api/v3/klines` returns kline/candlestick bars and that the close price is one of the returned fields.
- Binance documentation notes klines are uniquely identified by open time.
- Binance documentation supports a `timeZone` parameter for interpreting kline intervals, but start/end times remain UTC.

## Evidence directly stated by source

- Direct contract language from Polymarket: the settlement object is the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone and the condition is whether its final Close is higher than 70,000.
- Direct Binance docs: kline response includes open time, close time, open/high/low/close, and can be queried at 1-minute interval.

## What is uncertain

- Polymarket references the Binance web UI with 1m candles selected; API and UI should align, but the contract literally points users to the UI.
- The docs do not by themselves give the future April 16 noon ET candle, only the data structure and timing semantics.
- There remains ordinary path risk between now and settlement despite the contract mechanics being clear.

## Why this source may matter

This is the governing source-of-truth pair for the case. It removes most contract ambiguity and sharply narrows the real question to one operationally simple but time-sensitive event: whether Binance BTC/USDT stays above 70,000 at the exact noon ET minute close tomorrow.

## Possible impact on the question

This source materially lowers interpretation risk. Because the live Binance spot price on April 15 is already several thousand dollars above 70,000, the main remaining risk is not contract wording but price-path risk into the exact minute of settlement.

## Reliability notes

- Polymarket is authoritative for contract wording.
- Binance is authoritative for the referenced market data object.
- Evidence independence is medium rather than high because both sources describe the same settlement pipeline rather than offering independent directional price forecasts.