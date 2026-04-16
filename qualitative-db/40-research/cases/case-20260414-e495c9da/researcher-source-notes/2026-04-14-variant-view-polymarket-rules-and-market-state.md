---
type: source_note
case_key: case-20260414-e495c9da
dispatch_id: dispatch-case-20260414-e495c9da-20260414T191806Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-19
question: Will the price of Bitcoin be above $70,000 on April 19?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules for Bitcoin above ___ on April 19
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-e495c9da/researcher-analyses/2026-04-14/dispatch-case-20260414-e495c9da-20260414T191806Z/personas/variant-view.md]
tags: [polymarket, rules, contract-interpretation, market-implied-probability]
---

# Summary

This source establishes the market-implied baseline and the contract mechanics. For the $70,000 strike, the market page showed roughly 92% probability on April 14, while the rules specify settlement from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 19.

## Key facts extracted

- The relevant strike is $70,000 for April 19.
- The market page displayed the $70,000 outcome around 92% with Yes trading around 93 cents and No around 9 cents at fetch time.
- Resolution is based on the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on the specified date.
- The relevant metric is the final Close price of that candle.
- The market is explicitly about Binance BTC/USDT, not other exchanges or other Bitcoin reference prices.
- Price precision follows Binance source precision.

## Evidence directly stated by source

- The contract is a narrow, date-sensitive, source-specific market.
- Multiple material conditions must all hold for a Yes interpretation: use Binance, use BTC/USDT, use the 1-minute candle corresponding to 12:00 ET, and use that candle's final Close being strictly above 70,000.

## What is uncertain

- The fetched public page is not itself the governing source of truth for the settlement value; it only points to Binance as the settlement source.
- The public market page does not itself explain how ET labeling maps onto Binance API timestamps, so that mapping required separate verification.

## Why this source may matter

This is the direct source for contract wording and market-implied probability, so it anchors both the baseline and the interpretation burden.

## Possible impact on the question

It raises the bar for a casual bullish answer. BTC can stay above 70k broadly and still fail if Binance BTC/USDT prints a sub-70k final close on the exact noon-ET minute candle.

## Reliability notes

Useful and necessary for rules, but not sufficient alone for settlement interpretation because Polymarket delegates the actual source of truth to Binance. The market-implied price is also a consensus object, not evidence of the underlying event itself.
