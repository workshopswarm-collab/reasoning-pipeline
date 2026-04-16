---
type: source_note
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: binance-btcusdt-spot-and-klines
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance public market data API
source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7d14e3a4/researcher-analyses/2026-04-15/dispatch-case-20260415-7d14e3a4-20260415T231343Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, spot, klines, resolution-context]
---

# Summary

Direct Binance public API checks show BTC/USDT trading materially above the 72,000 threshold on 2026-04-15, with recent 1-minute candles around 74.7k and recent 4-hour / daily candles also above 72k. This does not settle the market, but it sharply narrows the path to a "No" outcome because the contract only needs the April 19 12:00 ET 1-minute close to stay above 72,000.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT last price `74721.13` on 2026-04-15.
- Recent 1-minute klines around retrieval time were clustered around 74.7k.
- Recent 4-hour context showed BTC/USDT holding in roughly the 74.5k-75.4k area in the latest bar sampled.
- Recent daily context showed BTC/USDT already above 72k on the latest daily bar sampled.

## Evidence directly stated by source

- `ticker/price` directly stated last trade price as `74721.13000000`.
- `klines?interval=1m` directly stated minute-level OHLCV values around the retrieval window.
- `klines?interval=4h` and `interval=1d` directly stated higher-timeframe OHLCV values useful for proximity-to-threshold context.

## What is uncertain

- The contract resolves on the Binance 1-minute candle for 12:00 ET on 2026-04-19, not on the current spot price.
- Public API data here is strong contextual evidence, but the formal governing source of truth is the Binance trading interface candle at the specified timestamp per market rules.
- BTC can move several thousand dollars over a few days; current cushion above 72k reduces but does not eliminate failure risk.

## Why this source may matter

This is the closest direct market-data source to the contract’s governing source of truth. It establishes both current distance from the threshold and whether a plausible path to failure would require a meaningful drawdown before the resolution timestamp.

## Possible impact on the question

Because BTC/USDT is already roughly 2.7k above the threshold with four days remaining, the main live catalyst question becomes whether any near-term shock can produce a sufficiently large drawdown by the noon ET resolution candle. Absent such a catalyst, this source supports a high probability of "Yes."

## Reliability notes

- High relevance because source is Binance itself, the exchange named in the contract.
- Slight source-of-truth gap remains because the market rules reference the Binance chart candle at a specific timestamp, not the API docs explicitly.
- Appropriate as primary direct evidence for current state and proximity to threshold.