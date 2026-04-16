---
type: source_note
case_key: case-20260416-2ab48f50
dispatch_id: dispatch-case-20260416T002737Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-2ab48f50 | market-implied
question: Will the price of Bitcoin be above $74,000 on April 17?
driver:
date_created: 2026-04-15
source_name: Polymarket market page and rules for Bitcoin above 74000 on April 17
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-2ab48f50/researcher-analyses/2026-04-16/dispatch-case-20260416-2ab48f50-20260416T002737Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-implied, btc]
---

# Summary

This source establishes the market-implied baseline and the governing resolution mechanics. It also shows the cross-strike ladder for the same noon-April-17 event, which is useful for inferring what the market as a whole is pricing.

## Key facts extracted

- The assigned market's current price was 61% on the Polymarket page for the 74,000 threshold, matching the runtime `current_price: 0.62` closely enough for analysis.
- The market resolves based on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET timezone on April 17, using the final close price.
- The contract is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Related strike prices on the same page showed a monotone ladder: 72k around 91%, 74k around 61%, 76k around 23%, 78k around 6%.

## Evidence directly stated by source

- Resolution rule: Yes if the Binance 1-minute candle for BTC/USDT at 12:00 ET on April 17 has a final close above 74,000.
- Source of truth: Binance BTC/USDT candles.
- The market page itself displayed roughly 61% for the 74,000 strike at capture time.

## What is uncertain

- The market page snapshot is not a formal historical time series and may move after capture.
- The public page does not by itself prove that Binance will present the candle in exactly the same UI layout at resolution time, though it names Binance as the source.

## Why this source may matter

This is the governing contract source and the cleanest view of the market's own implied probability structure across nearby strikes.

## Possible impact on the question

The ladder implies the crowd sees BTC slightly above the 74k threshold as more likely than not, but not by a large margin; that is consistent with spot trading already above 74k yet with enough time-to-resolution and crypto volatility to leave substantial downside risk.

## Reliability notes

High reliability for contract interpretation and current market pricing. Lower reliability for anything beyond the displayed snapshot, since it is still just one moment of the live market.