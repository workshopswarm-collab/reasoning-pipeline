---
type: source_note
case_key: case-20260414-76e5614f
dispatch_id: dispatch-case-20260414-76e5614f-20260414T182607Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [catalyst-hunter.md]
tags: [polymarket, resolution-rules, market-implied-probability, binance]
---

# Summary

This source establishes the governing contract language and the current market-implied baseline for the $72,000 threshold.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-17 has a final Close above 72,000.
- Resolution source is Binance BTC/USDT with 1m candles selected; other exchanges or pairs do not count.
- The April 17 market showed the $72,000 line trading around 84 cents Yes / 19 cents No on fetch, consistent with the assignment current_price of 0.83.
- Nearby ladder prices on the same page imply the market also sees $74,000 as much less certain (~60 cents Yes) and $70,000 as much more likely (~93.5 cents Yes).

## Evidence directly stated by source

- Exact resolution mechanics, source-of-truth exchange, pair, timeframe, and comparison operator (strictly higher than 72,000).
- Current market-implied probability near 83-84% for the 72,000 threshold.

## What is uncertain

- The page is not itself the final authoritative Binance chart print; it is the contract wrapper describing what will later decide resolution.
- Extracted web content may lag the live market by minutes.

## Why this source may matter

This is the governing contract source and baseline probability input. Because the case is date-sensitive and resolution depends on a specific one-minute candle on one venue, these mechanics matter as much as the directional BTC thesis.

## Possible impact on the question

The market is not asking whether BTC broadly trades strong this week; it asks whether Binance BTC/USDT remains above 72,000 at a precise noon ET timestamp on April 17. That makes timing, venue-specific microstructure, and event sequencing material.

## Reliability notes

Reliable for contract wording and current market pricing, but not sufficient alone for the terminal answer because final settlement depends on the future Binance candle.