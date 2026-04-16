---
type: source_note
case_key: case-20260415-9c95ce3a
dispatch_id: dispatch-case-20260415-9c95ce3a-20260415T173129Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-9c95ce3a | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page for "Bitcoin above 72,000 on April 17?"
source_type: market rules / market price page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, resolution-rules, market-price, binance]
---

# Summary

The Polymarket event page provides both the live market-implied probability for the 72,000 line and the contract-resolution language. It is the key source for what the market is pricing and how the contract is supposed to settle, but it is not itself the final governing source for the underlying BTC price print.

## Key facts extracted

- The 72,000 line was trading around 82-83% Yes at fetch time.
- The market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-17 has a final Close price strictly higher than 72,000.
- The source-of-truth exchange is Binance BTC/USDT specifically, not other exchanges or USD pairs.
- Price precision is whatever decimal precision the Binance source shows.
- Nearby ladder prices were internally coherent: 70k around 96%, 74k around 51%, 76k around 19%.

## Evidence directly stated by source

- The contract wording is explicit about date, time, timezone, venue, pair, and strict inequality.
- The live orderbook-derived price implies the crowd sees 72k as materially below the center of the expected Friday-noon distribution.
- The neighboring strike ladder suggests a distribution centered roughly in the 74k area rather than a random single-line mispricing.

## What is uncertain

- The page is a market interface, not an independently authoritative archive of Binance candle history.
- The visible probabilities can move quickly.
- The page does not itself prove where BTC will be on April 17; it only shows what traders are currently pricing.

## Why this source may matter

This source is necessary to interpret both the current market prior and the exact contract mechanics. For this case, rule precision matters because resolution depends on one specific Binance 1-minute close at noon ET rather than a daily close or composite spot price.

## Possible impact on the question

The ladder strongly supports the view that the market is already embedding a Friday-noon BTC expectation above 72k, with 72k treated as comfortably in-the-money but not locked. That makes any contrarian No case carry a burden to explain why the whole adjacent strike structure is wrong or stale.

## Reliability notes

Useful and necessary for market pricing plus contract language, but only medium credibility as a source for the underlying asset state because Polymarket is downstream of Binance for settlement.