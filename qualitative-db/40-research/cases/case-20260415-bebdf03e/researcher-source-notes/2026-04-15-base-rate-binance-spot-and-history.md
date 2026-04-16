---
type: source_note
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 72000 on April 21, 2026?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT API spot and daily history
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=365
source_date: 2026-04-15
credibility: high
recency: high
stance: mildly supportive
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, binance, exchange-data, btc, base-rate]
---

# Summary

This is the primary price-data source family most relevant to the contract because the market resolves from Binance BTC/USDT. Spot and recent history indicate BTC is currently above 72,000, but the outside-view base rate is materially lower than the market price implies once one accounts for several more days of volatility and the exact noon-ET close condition.

## Key facts extracted

- Binance spot at research time was about 75,000 BTC/USDT.
- Over the last 30 daily closes, only 20% of closes were above 72,000.
- Over the last 90 daily closes, about 32.2% of closes were above 72,000.
- Over the last 7 daily closes, about 71.4% were above 72,000, showing strong short-run momentum.
- A simple recent-volatility projection from 90-day realized returns with current spot near 75,000 produced a rough 6-day probability near 62% of finishing above 72,000.
- Binance exchange metadata confirms BTCUSDT is an active trading symbol and the exchange timezone is UTC, reinforcing the need to map the contract’s noon ET requirement to the correct minute candle rather than assume local exchange-display conventions.

## Evidence directly stated by source

- The Binance API returned live BTCUSDT spot near 75,000 during the run.
- The Binance API returned recent historical daily close series showing mixed but improving time-above-threshold behavior.

## What is uncertain

- Daily closes are only a proxy for the exact 12:00 ET 1-minute closing price used for settlement.
- The simple volatility projection is model-based and not an official exchange statistic.
- Short-term crypto volatility can move materially over a 5-6 day window, so base rates from different lookbacks vary widely.

## Why this source may matter

Because the contract settles on Binance, Binance data is the cleanest primary source for both current level and reference-class price behavior. It directly informs whether the current level provides enough cushion over 72,000 to justify an 81.5% probability.

## Possible impact on the question

This source supports a Yes-leaning view because spot is already above the strike, but it also argues against taking the market’s 81.5% at face value because the cushion is only around 4% and recent realized volatility is high enough that several days of drift could easily erase it.

## Reliability notes

High relevance and high source quality for the price path because Binance is the governing market source. The main limitation is mismatch between daily bars and the exact noon-ET 1-minute settlement candle.