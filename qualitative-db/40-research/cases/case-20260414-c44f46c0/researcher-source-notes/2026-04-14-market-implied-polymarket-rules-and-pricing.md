---
type: source_note
case_key: case-20260414-c44f46c0
dispatch_id: dispatch-case-20260414-c44f46c0-20260414T185449Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-19
question: Will the price of Bitcoin be above $68,000 on April 19?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-c44f46c0/researcher-analyses/2026-04-14/dispatch-case-20260414-c44f46c0-20260414T185449Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-pricing, resolution]
---

# Summary

This source established both the market-implied baseline and the governing contract mechanics.

## Key facts extracted

- The specific 68,000 threshold contract was trading around 95.5%, consistent with the assignment's `current_price` of 0.9575.
- The market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 19, 2026.
- The exact condition is whether the final candle close is higher than 68,000, not equal to 68,000.
- Resolution is tied to Binance BTC/USDT, not other exchanges or USD indices.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- Polymarket page lists the 68,000 outcome at roughly 95%.
- Rules state: resolution uses Binance, BTC/USDT, 1m candle, 12:00 ET, final close price.

## What is uncertain

- The fetched public page is not itself the final settlement record; it is the visible rules surface.
- Page pricing can move intraday; it is a snapshot, not a stable historical series.

## Why this source may matter

It defines the market-implied probability and the formal contract interpretation needed for any valid analysis. For this case, timing and source-of-truth details materially matter.

## Possible impact on the question

This source makes clear that the relevant event is not "Bitcoin generally above 68k that day" but specifically whether Binance BTC/USDT closes above 68,000 on the 12:00 ET one-minute candle on April 19.

## Reliability notes

Useful as the primary contract/rules source, but not fully independent from the market itself. It is strong for contract wording, weaker for objective external reality beyond the displayed price snapshot.
