---
type: source_note
case_key: case-20260415-cd803ba3
dispatch_id: dispatch-case-20260415-cd803ba3-20260415T203927Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-cd803ba3 | base-rate
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API plus Polymarket market page rules
source_type: primary_and_market_source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=30 ; https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-cd803ba3/researcher-analyses/2026-04-15/dispatch-case-20260415-cd803ba3-20260415T203927Z/personas/base-rate.md]
tags: [binance, polymarket, source-note, resolution-rules, price-context]
---

# Summary

This source note combines the governing market rules from the Polymarket event page with direct Binance BTC/USDT price data relevant to the contract. Together they establish both what resolves the market and the current outside-view price context.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT 1 minute candle for 12:00 ET on April 17, using the candle's final Close price.
- The contract is specifically about Binance BTC/USDT, not other exchanges or pairs.
- The market page showed the 74,000 line at roughly 63% at fetch time, close to but slightly below the assignment snapshot current_price of 0.70.
- Binance spot ticker at fetch time was 74,853.01, about $853 above the strike.
- Recent Binance daily candles show BTC closed below 74,000 on many recent days but moved back above that level in the last several sessions; the latest daily closes in the fetched window include 74,417.99, 74,131.55, and 74,650.01.
- The same 30-day Binance daily window also shows meaningful downside excursions into the mid-60ks and upper-60ks, so a two-day move back below 74,000 is plainly within recent realized range.

## Evidence directly stated by source

- Polymarket rules directly specify the resolution mechanism, timing reference, and venue.
- Binance API directly states current BTCUSDT spot price and recent historical OHLCV candles.

## What is uncertain

- Binance API queries here did not directly pull the exact April 17 12:00 ET future candle, because that candle does not yet exist.
- Polymarket page display can differ slightly from the assignment snapshot due to live movement or page rendering lag.
- Daily candles are contextual rather than resolution-direct because resolution depends on a single 1-minute close, not daily close.

## Why this source may matter

This is the core contract-interpretation and market-context evidence. It determines the correct source of truth and gives the most relevant direct price baseline ahead of resolution.

## Possible impact on the question

The current price being modestly above 74,000 supports a Yes-lean, but recent realized volatility around the threshold limits confidence. Because the market resolves from one precise Binance minute close at noon ET on April 17, even a broadly bullish backdrop can still fail if BTC dips below the line at that exact minute.

## Reliability notes

- Binance is the explicit governing source of truth for settlement, so source-of-truth reliability is high for the contract itself.
- For forecasting, Binance current price and recent candles are highly relevant but not sufficient alone; they need contextualization because the target is a future point-in-time minute close.