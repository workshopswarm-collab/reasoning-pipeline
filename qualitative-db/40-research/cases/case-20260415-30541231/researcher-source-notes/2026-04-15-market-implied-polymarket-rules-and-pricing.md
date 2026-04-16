---
type: source_note
case_key: case-20260415-30541231
dispatch_id: dispatch-case-20260415-30541231-20260415T133406Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-30541231 | market-implied
question: Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page rules and live pricing
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-implied, pricing]
---

# Summary

This source establishes both the live market-implied probability and the contract mechanics. It shows the 72,000 line trading around 84% Yes and states that the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on April 17, using the candle's final Close price.

## Key facts extracted

- The 72,000 outcome was displayed at roughly 84% Yes / 18% No when checked on 2026-04-15.
- The title date is April 17, 2026.
- Resolution depends on the Binance BTC/USDT 1-minute candle for 12:00 ET.
- The deciding value is the candle's final Close price.
- The threshold condition is strictly higher than 72,000.
- The rules explicitly exclude other exchanges and other trading pairs.
- Price precision is whatever Binance displays in the source.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The fetched webpage is a market surface, not the final settlement record itself.
- The page text does not itself show the eventual April 17 noon candle; it only defines how settlement will work.
- The event page presentation duplicates some text and is not a substitute for Binance verification.

## Why this source may matter

It is the clearest direct source for current market pricing and the operative contract language. For this case, contract mechanics matter because the question is date-specific, source-specific, and based on a single one-minute close rather than a daily average.

## Possible impact on the question

It supports using 84% as the market-implied baseline and forces attention to a narrow settlement mechanic: the April 17 12:00 ET Binance BTC/USDT 1-minute close must be above 72,000. This narrows the relevant forecasting task to whether BTC is likely to remain above that level at that exact timestamp.

## Reliability notes

Useful and necessary for contract interpretation, but not fully authoritative for the underlying price itself. The rules point to Binance as the governing source of truth, so Binance data must be checked separately.