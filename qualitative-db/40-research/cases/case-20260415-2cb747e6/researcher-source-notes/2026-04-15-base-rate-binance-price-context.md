---
type: source_note
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: markets
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API BTCUSDT price and recent candles
source_type: exchange primary / market data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=15
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [base-rate finding]
tags: [binance, btcusdt, candles, price-level, base-rate]
---

# Summary

Binance public API data shows BTC/USDT has been trading above 72,000 for most of the past several days and was around 74.2k at the time checked on April 15. Recent daily and hourly candles indicate the market is already above the threshold with roughly one day remaining, but there is still plausible downside room because daily ranges of 1k-2k+ have been common.

## Key facts extracted

- Spot price check via Binance ticker endpoint returned about 74,196.60.
- Binance 5-minute average price endpoint returned about 74,191.73.
- April 7 daily close: 71,924.22, just below 72,000.
- April 8 daily close: 71,069.93, below 72,000.
- April 9 daily close: 71,787.97, below 72,000.
- April 10 daily close: 72,962.70, above 72,000.
- April 11 daily close: 73,043.16, above 72,000.
- April 12 daily close: 70,740.98, below 72,000.
- April 13 daily close: 74,417.99, above 72,000.
- April 14 daily close: 74,131.55, above 72,000.
- Intraday hourly data on April 15 remained around the high-73k to low-74k area during the checked window.
- Recent daily ranges have often exceeded 1,000 dollars and occasionally 2,000 dollars, meaning a move back below 72,000 by the specific noon ET minute is not impossible.

## Evidence directly stated by source

- Binance APIs directly provide recent BTC/USDT prices and OHLC candle history.
- The recent observed level is materially above 72,000.
- The threshold is within typical short-term volatility distance rather than safely out of range.

## What is uncertain

- These endpoints are not the same UI workflow named in Polymarket’s rules, though they are still direct Binance data and likely highly aligned.
- The exact resolution minute is still in the future, so present price only provides contextual support.
- Price behavior around macro or crypto-specific catalysts over the next ~24 hours could change the level materially.

## Why this source may matter

This is the key direct evidence about whether the threshold is currently in reach. For a short-dated above/below market, the best outside-view input is the current distance from the strike relative to typical realized intraday volatility over the remaining horizon.

## Possible impact on the question

Because BTC/USDT is already about 2.2k above the threshold, the prior should favor Yes, but not with certainty. The relevant base-rate question becomes whether a roughly 3% downside move by the noon ET minute is common enough over one day to justify a materially lower probability than the market’s near-90% reading.

## Reliability notes

This is high-quality direct market data from Binance public endpoints. Independence versus the resolution source is limited because it is the same venue, but for this contract that is a feature more than a bug.