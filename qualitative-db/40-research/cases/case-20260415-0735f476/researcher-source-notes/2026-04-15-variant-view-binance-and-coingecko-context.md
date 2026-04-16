---
type: source_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: threshold-daily-close
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20 close above 70000?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API plus CoinGecko market snapshot
source_type: exchange data + secondary market-data aggregator
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, binance, coingecko, btc, price-context]
---

# Summary

Direct Binance API pulls show BTC/USDT around **74.6k** on April 15, with the last 7 daily candles all closing above 70k and recent daily highs reaching roughly **76.0k**. CoinGecko independently showed Bitcoin around **74.7k**, with a 24h range roughly **73.6k-75.2k**, broadly confirming the level.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT around **74,626.57**.
- Binance 7 daily candles showed closes of roughly **71,788; 72,963; 73,043; 70,741; 74,418; 74,132; 74,627**.
- None of the last 7 daily closes in the pulled window were below 70,000.
- Daily highs in that sample reached about **76,038**.
- A 72-hour Binance 1h sample showed price action mostly in the **73.5k-75.3k** region, still well above 70k.
- CoinGecko independently showed Bitcoin around **74,732**, with 24h high about **75,206** and low about **73,617**.

## Evidence directly stated by source

- Direct evidence from Binance is current level and recent realized trading range on the governing exchange/pair.
- CoinGecko provides a secondary confirmation that the general BTC/USD level is in the mid-74k area rather than close to 70k.

## What is uncertain

- These endpoints do not provide the exact April 20 12:00 ET close yet.
- CoinGecko is not the governing source and can diverge slightly from Binance because of aggregation and market structure.
- A 5-day horizon remains long enough for macro or crypto-specific volatility to matter.

## Why this source may matter

The main market question is not abstract direction but whether BTC can remain above a threshold that is currently several thousand dollars below spot on the governing venue.

## Possible impact on the question

The current buffer above 70k materially supports a Yes lean. The variant view is that the market may still be **overconfident** because this is a single-minute close market with several days left; a sharp weekend drawdown or exchange-specific deviation could still knock the noon ET close below 70k even if BTC broadly stays bullish.

## Reliability notes

Binance public API is high relevance because it matches the named venue and pair, though it is still not the exact final noon-ET 1m candle. CoinGecko is useful as an independent contextual cross-check but should not be treated as the source of truth for settlement.