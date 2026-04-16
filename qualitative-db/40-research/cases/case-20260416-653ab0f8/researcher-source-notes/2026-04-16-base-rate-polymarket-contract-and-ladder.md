---
type: source_note
case_key: case-20260416-653ab0f8
dispatch_id: dispatch-case-20260416-653ab0f8-20260416T090226Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: polymarket btc above 72000 on april 18
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market rule page
source_url: https://polymarket.com/event/bitcoin-above-on-april-18
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [base-rate-finding]
tags: [polymarket, resolution-rules, market-implied-probability]
---

# Summary

The Polymarket event page provides the current market-implied probability and the contract wording. For the 12:00 PM ET Apr 18 ladder, the 72,000 line was trading around 88% at fetch time.

## Key facts extracted

- The relevant contract is the Apr 18 12:00 PM ET ladder outcome for BTC above 72,000.
- The market page showed the 72,000 line at roughly 88%.
- Nearby ladder prices were approximately 97% for 70,000, 62% for 74,000, 28% for 76,000, and 8% for 78,000.
- The rule says resolution depends on the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on Apr 18.
- The contract resolves Yes only if the final Close price for that specific minute is higher than 72,000.
- It is specifically Binance BTC/USDT, not other exchanges or pairs.

## Evidence directly stated by source

- Source-of-truth is Binance BTC/USDT candle data.
- Timing window is exact: the 12:00 ET one-minute candle on Apr 18, 2026.
- The outcome threshold is strictly above 72,000.

## What is uncertain

- The fetched page is a scraped representation, not the exchange settlement screen itself.
- The page does not by itself prove current Binance price; it only frames the contract and implied pricing.

## Why this source may matter

This is the governing contract source for what counts, the exact threshold, and the exact timing. It also anchors the market-implied baseline used for comparison.

## Possible impact on the question

The narrow one-minute, exchange-specific settlement means spot-exchange microstructure and short-horizon volatility matter more than a generic daily-close framing. That slightly lowers confidence versus an imprecise "sometime that day" interpretation.

## Reliability notes

Useful as the contract-definition source and for current crowd pricing, but not sufficient alone for the underlying BTC state. Best paired with an independent spot-price source and, ideally, direct Binance market data verification.