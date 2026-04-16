---
type: source_note
case_key: case-20260415-868fc947
dispatch_id: dispatch-case-20260415-868fc947-20260415T090047Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT API spot, 24h stats, and 1m klines
source_type: exchange primary market data
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-868fc947/researcher-analyses/2026-04-15/dispatch-case-20260415-868fc947-20260415T090047Z/personas/risk-manager.md]
tags: [binance, btcusdt, price, klines, settlement-source]
---

# Summary

Direct Binance data shows BTC/USDT trading materially above 72,000 on 2026-04-15 morning ET, with last price around 74.0k, 24h low around 73.5k, and recent 1-minute candles around 74.1k. This supports a bullish base case but also shows that the relevant settlement is a single exact minute tomorrow rather than a broad daily level.

## Key facts extracted

- Binance ticker price was approximately 74,034.23 at time of check.
- Binance 24h stats showed high about 76,038 and low about 73,514 over the prior 24 hours.
- Binance recent 1m klines were printing closes around 74.1k to 74.2k before a drop back toward 74.0k.
- Binance avgPrice endpoint showed a 5-minute average near 74,124.31.
- The target resolution minute for this market is 2026-04-16 12:00 ET, which converts to 2026-04-16 16:00:00 UTC.

## Evidence directly stated by source

- Current spot and microstructure are above the 72,000 threshold by roughly 2,000 points.
- Recent intraday variation is meaningful but still left price above the threshold during the checked window.
- Binance can be queried directly for the exact candle type the contract references.

## What is uncertain

- This source does not tell us tomorrow's noon ET close.
- A single-minute close can fail even if most surrounding trading remains above 72,000.
- Short-horizon crypto volatility means current cushion can compress materially within 24 hours.

## Why this source may matter

This is the primary settlement-related source and the strongest direct evidence on where BTC/USDT currently sits relative to the strike.

## Possible impact on the question

It materially supports Yes because price is currently above strike by about 2.8%, but from a risk-manager lens it also highlights path risk: a sharp intraday selloff or noon-minute wick tomorrow is enough to break an otherwise broadly bullish narrative.

## Reliability notes

High credibility for direct exchange data and highly relevant because the contract explicitly uses Binance BTC/USDT. Independence versus Polymarket is limited on rules because Polymarket itself points to Binance, but this is still the primary evidence class for settlement-related analysis.