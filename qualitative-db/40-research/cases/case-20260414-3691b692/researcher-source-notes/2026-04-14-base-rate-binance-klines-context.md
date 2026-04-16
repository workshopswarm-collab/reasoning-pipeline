---
type: source_note
case_key: case-20260414-3691b692
dispatch_id: dispatch-case-20260414-3691b692-20260414T170231Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on 2026-04-16 above 72000?
driver: reliability
date_created: 2026-04-14
source_name: Binance BTCUSDT kline API spot data
source_type: exchange_market_data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m
source_date: 2026-04-14
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3691b692/researcher-analyses/2026-04-14/dispatch-case-20260414-3691b692-20260414T170231Z/personas/base-rate.md]
tags: [binance, klines, source-of-truth, price-context, base-rate]
---

# Summary

Direct Binance kline data shows BTC/USDT was already well above 72,000 at the relevant intraday comparison point when reviewed on April 14, with the exact 12:00 PM ET equivalent minute on April 14 closing at 75,356.48. Recent daily and intraday behavior shows 72,000 has become an active but not perfectly secure support zone over the last week.

## Key facts extracted

- Direct query to Binance 1-minute klines returned the April 14 16:00 UTC candle (12:00 PM ET during DST) with close 75,356.48.
- Direct query to Binance 1-minute klines for the future April 16 16:00 UTC candle returned no data yet, confirming the event is unresolved and the timestamp conversion used is sensible.
- April 9 through April 14 noon-ET-equivalent 1-minute closes were: 72,342.21; 72,476.00; 72,865.57; 70,860.00; 71,902.91; 75,356.48.
- In minute-level data from April 1 through April 14 review time, BTC/USDT was above 72,000 for about 22.3% of observed minutes overall, but the share rose materially in the most recent regime: roughly 65.4% on April 10, 100% on April 11, 7.0% on April 12, 33.7% on April 13, and 100% so far on April 14 before review cutoff.
- Daily closes from April 10 to April 14 were 72,962.70; 73,043.16; 70,740.98; 74,417.99; and partial April 14 price action reaching above 76,000 intraday before settling near 74.7k around review time.
- Looking at recent ET-noon reference points, the asset crossed above 72,000 on April 9 and has held that level at the same reference time on 3 of the last 6 days, with only April 12 and April 13 noon ET below the threshold.

## Evidence directly stated by source

- Binance 1-minute and daily kline endpoints provide direct observed open, high, low, close values for BTC/USDT on the exchange named in the contract.
- The returned April 14 16:00 UTC candle close was 75356.48.

## What is uncertain

- The API is not the exact UI surface named in the rule, though it is Binance direct data and should be a strong verification surface rather than a perfect legal settlement substitute.
- Short-horizon BTC volatility remains high enough that two-day drawdowns of several percent are plausible.
- Sample windows used for recent-regime frequency checks are small.

## Why this source may matter

This is the closest available direct source to the contract's source of truth and it anchors both the current level relative to 72,000 and the relevant time-zone conversion.

## Possible impact on the question

A market pricing 90%-91% Yes is implicitly saying that a roughly 4.5% buffer above the strike, with two calendar days to go, is very likely to survive until the exact noon ET minute on April 16. Binance data supports a bullish lean but also shows recent failures of that same threshold, so the remaining path risk is not negligible.

## Reliability notes

High reliability as direct exchange market data from Binance. Some residual source-of-truth ambiguity remains because the rule cites the Binance trading interface rather than the API endpoint, but the data source family is the same and adequate for verification.