---
type: source_note
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: ethereum
entity: ethereum
topic: case-20260416-989964fe | market-implied
question: Will the Binance ETH/USDT 12:00 ET one-minute candle close on 2026-04-17 be above 2200?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance ETHUSDT spot and recent 1m candles
source_type: primary market rules + primary exchange data
source_url: https://polymarket.com/event/ethereum-above-on-april-17 ; https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT ; https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=5
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/market-implied.md]
tags: [crypto, ethereum, polymarket, binance, resolution]
---

# Summary

The governing contract is mechanically simple but timing-sensitive: resolution depends only on the Binance ETH/USDT one-minute candle labeled 12:00 ET on 2026-04-17, and the current Binance spot price is already materially above the 2200 threshold.

## Key facts extracted

- Polymarket rules say the market resolves Yes if the Binance ETH/USDT 1-minute candle for 12:00 in the ET timezone on April 17 has a final Close price higher than 2200.
- The rules explicitly exclude other exchanges and other trading pairs.
- Binance spot API returned ETHUSDT price 2355.61 at fetch time.
- Recent Binance 1-minute klines around fetch time showed closes clustered around 2353.88 to 2355.60, indicating price was about 7 percent above the threshold with ordinary minute-to-minute noise.

## Evidence directly stated by source

- Direct resolution mechanics come from the Polymarket rules page.
- Direct current exchange price and recent minute candles come from Binance API endpoints.

## What is uncertain

- This source set does not settle tomorrow's noon candle; it only establishes current distance from the strike and the exact settlement mechanics.
- Short-horizon crypto volatility could still move ETH/USDT below 2200 by settlement.

## Why this source may matter

This is the core evidence for why the market can plausibly trade at an extreme Yes probability: the contract settles off one specific Binance minute close, and the current reference market is already comfortably above the threshold.

## Possible impact on the question

If Binance remains near current levels into tomorrow morning, the current 95.5 percent market-implied probability is easy to justify. The main residual question is not contract ambiguity but whether ETH can drop more than roughly 6.6 to 7 percent before the specific noon ET minute close.

## Reliability notes

- Polymarket is the governing contract source for settlement mechanics, so credibility is high for resolution interpretation.
- Binance is the stated source of truth for the actual closing price, so credibility is high for current spot and recent candle context.
- Independence is limited because both are directly tied to the same settlement mechanism, so an extra secondary market-context source is still useful for cross-checking price level and recent range.