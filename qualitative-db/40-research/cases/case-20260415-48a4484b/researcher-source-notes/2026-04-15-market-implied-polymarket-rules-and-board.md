---
type: source_note
case_key: case-20260415-48a4484b
dispatch_id: dispatch-case-20260415-48a4484b-20260415T180644Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for bitcoin-above-72k-on-april-16
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-48a4484b/researcher-analyses/2026-04-15/dispatch-case-20260415-48a4484b-20260415T180644Z/personas/market-implied.md]
tags: [polymarket, contract-rules, resolution-source, price-threshold]
---

# Summary

The Polymarket market page provides the live market-implied probability and the governing contract language. For the $72,000 line, the page showed roughly 94% Yes at the time of review. The rules explicitly resolve on the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 16, using that candle's final Close price, with Yes only if the close is strictly higher than 72,000.

## Key facts extracted

- Current market-implied probability for "above 72,000" was about 94% Yes at review time.
- Resolution source is Binance BTC/USDT, not another exchange or pair.
- Resolution window is the 1-minute candle for 12:00 ET (noon) on April 16, 2026.
- The relevant field is the candle's final Close price.
- The threshold condition is strictly greater than 72,000, not greater-than-or-equal.

## Evidence directly stated by source

- Contract resolves Yes if the Binance 1-minute candle for BTC/USDT 12:00 in ET on the specified date has a final Close price higher than the strike.
- Price precision is determined by the source decimals.
- Board context across strikes was internally coherent: 70k near 99%, 72k near 94%, 74k near 56%, 76k near 10%.

## What is uncertain

- The fetched market page is not itself the final settlement record; it is a live webpage snapshot.
- The page does not prove Binance API/data availability at the exact settlement minute tomorrow.
- The page alone cannot confirm whether a UI candle label exactly corresponds to the API kline open-time convention, so a second verification source is needed.

## Why this source may matter

This is the governing contract surface and the only source that directly states what must happen for this market to resolve Yes or No.

## Possible impact on the question

It anchors both the market prior and the legal/mechanical answer condition. Because the contract is narrowly date- and source-specific, this source is necessary to avoid answering the wrong question (e.g., using another exchange, a spot snapshot instead of the 1-minute close, or a >= interpretation).

## Reliability notes

Useful as the primary contract source, but not fully sufficient on its own because live web pages can be stale, rounded, or UI-dependent. It should be paired with a direct Binance source or API check for source-of-truth mechanics and current price context.