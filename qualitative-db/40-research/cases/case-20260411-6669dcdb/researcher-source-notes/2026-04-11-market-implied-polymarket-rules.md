---
type: source_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
analysis_date: 2026-04-10
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260411-6669dcdb | market-implied
question: Will the price of Bitcoin be above $72,000 on April 11?
driver: reliability
date_created: 2026-04-10
source_name: Polymarket market page and rules
source_type: primary-contract
source_url: https://polymarket.com/event/bitcoin-above-on-april-11
source_date: 2026-04-10
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, contract, resolution, source-note]
---

# Summary

This note captures the market's stated baseline and the exact contractual resolution language.

## Key facts extracted

- The assignment states current market price is `0.7125`, implying a 71.25% Yes probability.
- The live market page at research time showed the 72,000 line trading around 90.8% Yes, suggesting material movement versus the assignment snapshot.
- The rules say the market resolves Yes if the Binance 1-minute candle for BTC/USDT `12:00` in ET on Apr. 11 has a final `Close` price higher than 72,000.
- The page explicitly says this is about Binance BTC/USDT, not other exchanges or pairs.
- The page says price precision is determined by the number of decimals in the source.

## Evidence directly stated by source

- Governing source is Binance, specifically the BTC/USDT close prices currently available at the Binance trade page with `1m` and `Candles` selected.
- Resolution hinges on the close price of a specific 1-minute candle, not on daily close, index price, or other exchanges.

## What is uncertain

- The assignment snapshot and live market page disagree materially on current price, so the market moved sharply during the run or the snapshot was stale.
- The page references a Binance UI workflow, not a machine-readable settlement endpoint, which leaves some operational ambiguity for later auditing.

## Why this source may matter

This source defines the contract, the source of truth, and the market-implied benchmark that the persona is supposed to evaluate.

## Possible impact on the question

Because the contract is a narrowly defined candle-close event on Binance BTC/USDT, pair mismatch and timezone mismatch are more important than broad BTC price commentary. The market's high Yes price is only sensible if traders are treating this as a near-spot threshold test with modest remaining time risk.

## Reliability notes

High reliability for contract wording. Lower reliability for live price extraction from the page because web fetch can capture a changed snapshot and the page is not optimized for clean machine parsing.