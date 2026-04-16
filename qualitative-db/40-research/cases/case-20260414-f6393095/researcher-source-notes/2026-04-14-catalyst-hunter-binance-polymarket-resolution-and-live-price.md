---
type: source_note
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market rules page and Binance spot market/API docs plus live Binance ticker/klines
source_type: mixed_primary_and_contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-f6393095/researcher-analyses/2026-04-14/dispatch-case-20260414-f6393095-20260414T222237Z/personas/catalyst-hunter.md]
tags: [source-note, polymarket, binance, btc, resolution]
---

# Summary

This note captures the governing resolution mechanics and the most relevant live market context for the case. The Polymarket rules specify that settlement depends on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 17, using the final close price, not any other exchange or pair. Binance API documentation confirms that 1-minute klines and close prices are retrievable as structured market data, and live Binance prints on April 14 show BTC/USDT trading around 74k, materially above the 70k threshold.

## Key facts extracted

- Polymarket rules state the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final close price higher than 70000.
- The contract is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Binance market-data documentation for `GET /api/v3/klines` states 1-minute klines return open/high/low/close and support timezone interpretation for intervals.
- Live Binance spot ticker on April 14 printed BTCUSDT at roughly 74038.
- Recent 1-minute Binance klines fetched during this run showed closes clustered around 74038-74109.
- Binance 24hr ticker during this run showed a 24h high of 76038 and low of 73795, leaving a cushion of roughly 4k above the 70k line even at the 24h low.

## Evidence directly stated by source

- Polymarket directly states the governing source of truth and the exact candle/timeframe.
- Binance documentation directly states how 1-minute kline close data are exposed.
- Binance live endpoints directly state current BTCUSDT spot price and recent intraminute closes.

## What is uncertain

- The Polymarket page does not fully document edge-case handling if Binance UI and API presentation differ, though the governing source is still Binance BTC/USDT 1-minute candle close.
- Live spot price on April 14 does not guarantee April 17 noon ET price; macro or crypto-specific shocks could still push BTC below 70k before resolution.
- I did not identify a single scheduled deterministic catalyst between now and resolution that obviously dominates generic crypto risk sentiment.

## Why this source may matter

This is the key resolution bundle for the case. It narrows the question to a single exchange, pair, timezone, and 1-minute close while also showing the market currently sits meaningfully above the strike.

## Possible impact on the question

The direct implication is that the market should be judged mainly by whether BTC can avoid a >5% downside move into Friday noon ET on Binance spot, not by broader narratives about crypto direction in general. The main catalysts are therefore downside shocks or exchange-specific disruptions rather than the need for fresh upside.

## Reliability notes

- Polymarket rules page is the direct contract surface but still depends on Binance as the external resolution source.
- Binance API documentation is strong contextual support for how the candle data are represented.
- Live Binance ticker/klines are highly relevant and recent, but they are still a snapshot and not the settlement print itself.
- Evidence independence is moderate: the contract depends on Binance, and the main contextual price evidence is also from Binance, so the sources are aligned but not fully independent.