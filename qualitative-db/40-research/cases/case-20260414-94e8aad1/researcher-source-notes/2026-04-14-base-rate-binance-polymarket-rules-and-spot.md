---
type: source_note
case_key: case-20260414-94e8aad1
dispatch_id: dispatch-case-20260414-94e8aad1-20260414T175223Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-94e8aad1 | base-rate
question: Will the price of Bitcoin be above $70,000 on April 16?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance spot API docs + Binance BTCUSDT spot + Polymarket contract page
source_type: mixed_primary_context
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, contract-rules, btc]
---

# Summary

This note captures the governing contract language from Polymarket plus direct Binance price/context surfaces relevant to a short-horizon threshold market.

## Key facts extracted

- Polymarket states the market resolves **Yes** if the **Binance BTC/USDT 1-minute candle for 12:00 ET on April 16** has a final **Close** price **higher than 70,000**.
- Polymarket explicitly says the source is Binance BTC/USDT, not another exchange or pair.
- Binance spot API docs for `/api/v3/klines` confirm 1-minute klines exist and support a `timeZone` parameter, with kline close prices returned in the response.
- Direct Binance ticker endpoint for BTCUSDT on 2026-04-14 returned price **74,664.77** at fetch time.
- The market page showed the 70,000 line trading around **96.2% Yes**.

## Evidence directly stated by source

- Contract wording and source-of-truth come directly from the Polymarket event page.
- Binance documentation directly states that kline/candlestick data returns open/high/low/close values for a chosen interval.
- Binance ticker endpoint directly returned the current BTCUSDT price.

## What is uncertain

- The exact future April 16 12:00 ET 1-minute candle close is not knowable yet.
- The Polymarket page references Binance chart UI as the resolution surface, while Binance API docs provide a closely related machine-readable verification path; there is some low-level implementation ambiguity over UI candle vs API candle representation, though they should ordinarily match.
- No deeper historical distribution study was completed in this run, so the base-rate judgment is structural rather than statistically backtested.

## Why this source may matter

The market is narrow and rule-sensitive: it resolves on a specific exchange, pair, timeframe, timezone, and close field. Direct rule capture and a direct spot-price check matter more than broad narrative crypto news.

## Possible impact on the question

With BTC spot already near 74.7k, the relevant outside-view question becomes whether BTC is likely to remain above 70k at one specific minute roughly two days later, not whether BTC is in a long-run bull market. That supports a high Yes probability, but not necessarily as high as the market’s mid-90s pricing because crypto can move several percent quickly.

## Reliability notes

- Polymarket contract page is the practical governing contract surface for this market.
- Binance is the named source of truth, so Binance market data surfaces are authoritative for settlement mechanics.
- Independence between these sources is low-to-medium because Polymarket explicitly delegates to Binance rather than serving as an independent observational source.