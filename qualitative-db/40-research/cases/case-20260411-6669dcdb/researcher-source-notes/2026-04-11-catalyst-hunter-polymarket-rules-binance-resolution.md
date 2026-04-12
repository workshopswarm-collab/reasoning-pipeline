---
type: source_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
analysis_date: 2026-04-11
persona: catalyst-hunter
domain: crypto
subdomain: markets
entity: btc
topic: bitcoin-above-72k-on-april-11
question: Will the price of Bitcoin be above $72,000 on April 11?
driver: operational-risk
date_created: 2026-04-11
source_name: Polymarket market rules page
source_type: market rules / contract page
source_url: https://polymarket.com/event/bitcoin-above-on-april-11
source_date: 2026-04-11
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/catalyst-hunter.md
tags: [polymarket, binance, resolution-rules, timing]
---

# Summary

This source provides the governing market wording and the stated source of truth for resolution.

## Key facts extracted

- The market resolves on the Binance BTC/USDT 1 minute candle for 12:00 ET on the specified date.
- The relevant value is the final candle "Close" price.
- The threshold is strictly higher than $72,000 for a Yes resolution.
- The rules explicitly say Binance BTC/USDT, not another exchange or pair.
- The page also showed the market-implied probability for the 72,000 line around 91% at capture time.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."

## What is uncertain

- The public Polymarket page is not itself the settlement feed; it points to Binance as the governing source.
- The phrase "12:00 in the ET timezone (noon)" requires explicit UTC translation because Binance candles are UTC-indexed in API usage.
- The page does not itself provide the resolved candle close for the target minute at the time this note was captured.

## Why this source may matter

It defines the exact pair, exact interval, exact timezone framing, and exact close-price logic. Those mechanics matter more than generic BTC spot prices from other venues.

## Possible impact on the question

This source makes the key catalyst less about broad overnight BTC narrative and more about whether Binance BTC/USDT remains above 72,000 exactly into the noon ET minute close. It also creates contract-interpretation and operational-verification risk if the ET-to-UTC mapping or candle-close interpretation is mishandled.

## Reliability notes

Useful as the contract page and governing wording source, but not sufficient alone for the terminal answer because the market settles to Binance data rather than to Polymarket display text.