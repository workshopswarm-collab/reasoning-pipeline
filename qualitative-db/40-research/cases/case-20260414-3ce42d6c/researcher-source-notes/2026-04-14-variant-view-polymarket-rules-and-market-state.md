---
type: source_note
case_key: case-20260414-3ce42d6c
dispatch_id: dispatch-case-20260414-3ce42d6c-20260414T130958Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the Binance BTC/USDT 1-minute candle for 2026-04-14 12:00 ET close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-14
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [variant-view.md]
tags: [polymarket, contract-rules, market-implied-probability, binance]
---

# Summary

This source established the operative contract mechanics and the market-implied baseline for the 70k threshold.

## Key facts extracted

- The market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on 2026-04-14 has a final close strictly higher than 70000.
- The governing source of truth is Binance, specifically the BTC/USDT chart with 1m candles selected.
- The relevant timestamp is noon America/New_York on 2026-04-14, which is 16:00 UTC because New York is on EDT.
- The market-implied probability for the 70,000 threshold was approximately 99.95% from the provided current_price 0.9995; the page scrape also showed the 70,000 line trading effectively at 99.9-100%.

## Evidence directly stated by source

- Resolution source: Binance BTC/USDT close price on the 12:00 ET one-minute candle.
- Precision: whatever decimal precision Binance displays for the source candle.
- Condition is strict inequality: higher than 70000, not equal to 70000.

## What is uncertain

- The public Polymarket page does not itself display the actual resolving candle close; it only defines the source-of-truth and market pricing.
- The page does not eliminate operational edge cases such as Binance display/API inconsistency at settlement time.

## Why this source may matter

This is the direct contract/rules source. It defines the exact exchange, pair, time window, and inequality condition that matter for settlement.

## Possible impact on the question

It sharply narrows the only material variant pathway: not broad BTC direction, but whether an exact Binance noon-ET minute close or exchange-specific operational issue could upset what otherwise looks nearly certain.

## Reliability notes

High relevance because this is the contract-definition surface, but not sufficient alone for factual settlement because it is not the actual Binance candle output.