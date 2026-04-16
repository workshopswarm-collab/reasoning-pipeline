---
type: source_note
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 72000 on April 21, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page for Bitcoin above ___ on April 21
source_type: market page / contract specification
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
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
tags: [source-note, polymarket, contract, binance, btc]
---

# Summary

This source provides the market-implied probability snapshot and the governing contract wording for what counts as a Yes resolution.

## Key facts extracted

- The specific 72,000 strike was trading around 81-82% Yes at fetch time.
- The market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on April 21, 2026.
- The operative value is the final candle "Close" price, not intraminute highs, lows, or prices from other exchanges.
- Price precision is determined by the Binance source.

## Evidence directly stated by source

- The page explicitly states: "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- The page explicitly identifies Binance BTC/USDT as the resolution source.

## What is uncertain

- The market page is not itself the exchange data source; it describes the resolution source but does not provide the final authoritative candle values for the future resolution time.
- The page fetch is a scraped web rendering, so the displayed quote should be treated as a current snapshot rather than a canonical historical archive.

## Why this source may matter

It defines the contract mechanics and shows that this is a narrow, date-specific, source-specific, and multi-condition market. Those mechanics matter because even a broadly bullish BTC view could fail if the exact Binance noon ET candle closes at or below 72,000.

## Possible impact on the question

This source anchors both the market baseline and the need to analyze exact timing/source conditions rather than generic "BTC sometime that day" price narratives.

## Reliability notes

Useful as the governing contract description and market-implied baseline, but not sufficient on its own for price-level analysis because it is not the final settlement source and the displayed quote is just a snapshot.