---
type: source_note
case_key: case-20260415-30541231
dispatch_id: dispatch-case-20260415-30541231-20260415T133406Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API and Polymarket event rules
source_type: primary + governing market rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, binance, polymarket, resolution-rules, btc]
---

# Summary

This note captures the governing resolution mechanics from the Polymarket market page and a direct Binance API spot snapshot used to anchor current distance from the strike.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on April 17 has a final Close price higher than 72,000.
- Polymarket specifies Binance BTC/USDT as the source of truth, not other exchanges or pairs.
- Binance public API returned BTCUSDT spot price 74,042.63 on 2026-04-15 during this run.
- Recent 1-minute Binance klines retrieved in this run clustered around roughly 74.0k-74.3k, indicating BTC was already materially above the 72k threshold with about two days remaining.
- Binance exchangeInfo for BTCUSDT indicates the pair is active and the price tick size is 0.01, which is relevant to price precision.

## Evidence directly stated by source

- Direct from Polymarket rules: settlement is based on the Binance BTC/USDT 12:00 ET 1-minute candle close on the specified date.
- Direct from Binance API: BTCUSDT latest traded spot and recent 1-minute candles.

## What is uncertain

- The public API snapshot does not itself guarantee the final noon ET candle on April 17.
- The web-fetched Polymarket page is a readable mirror extraction, not the official API payload, though it reproduced the rule text clearly.
- No single external macro or event-calendar source in this run identified a scheduled binary catalyst likely to force BTC below 72k before the deadline.

## Why this source may matter

This is the core direct evidence set: one source defines settlement mechanics and one source anchors current price distance from the strike on the governing venue.

## Possible impact on the question

Because BTC is already about 2.0k above the strike on the governing venue, the market mainly turns on whether any catalyst or broad risk-off move can push Binance BTC/USDT below 72k precisely into the noon ET minute on April 17.

## Reliability notes

- Binance API is highly relevant because Binance BTC/USDT is the explicit source of truth.
- Polymarket market-page rules are highly relevant because they define what counts.
- These two sources are not independent, but they are the most decision-relevant direct sources for this contract.