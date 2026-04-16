---
type: source_note
case_key: case-20260415-cd803ba3
dispatch_id: dispatch-case-20260415-cd803ba3-20260415T203927Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API spot and kline checks
source_type: exchange API / resolution-source-adjacent
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: very-high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, resolution-source, timing-sensitive]
---

# Summary

Binance spot and recent kline data indicate BTC/USDT was already above the $74,000 strike during this research run, but the contract resolves on the Binance 1-minute candle closing at 12:00 PM ET on April 17, so the critical question is not current spot alone but whether BTC remains above the threshold at that exact settlement minute.

## Key facts extracted

- Binance ticker price during the run: about 74,694.83 to 74,695.65 USDT.
- Recent 72 hourly closes from Binance show BTC recently traded in a roughly 70,506 to 76,038 range.
- Last 24h Binance range from the retrieved 1h candles was roughly 73,514 low to 75,281 high.
- Daily candles over the last 10 days show BTC climbed from the high-68k/low-69k area to the mid-74k area, but with intraday swings of several thousand dollars.

## Evidence directly stated by source

- The exchange API directly reports the current BTCUSDT price and recent 1m/1h/1d candle data.
- The contract's governing source of truth is Binance BTC/USDT with 1m candles, making Binance the most relevant direct evidence surface even though the API endpoint used here is not the exact visual web UI named in the rules.

## What is uncertain

- The contract refers specifically to the final close of the Binance 1-minute candle for 12:00 PM ET on April 17; this note does not yet observe that future candle.
- Binance API price data and the web chart UI should normally align, but the contract text cites the web chart as the formal resolution surface.
- Intraday volatility remains large enough that being above 74k now does not guarantee the noon ET April 17 close remains above 74k.

## Why this source may matter

This is the most direct available source for both current price context and the exact exchange named in the contract. It establishes that the market is asking about a threshold close that is already near or slightly below current trading levels, which makes path-dependent volatility the main remaining risk rather than a distant upside move.

## Possible impact on the question

This source supports a Yes-lean because BTC is already trading above the strike, but it also supports caution: the asset has recently moved through multi-thousand-dollar daily ranges, so the settlement-minute close can still flip if risk sentiment weakens before Friday noon ET.

## Reliability notes

- High relevance because Binance is the governing source of truth named by the contract.
- High recency because the data was fetched live during the run.
- Moderate residual risk because the API endpoint is resolution-source-adjacent rather than the exact chart UI, and because settlement depends on a future minute close rather than current spot.