---
type: source_note
case_key: case-20260416-8bef05aa
dispatch_id: dispatch-case-20260416-8bef05aa-20260416T144205Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-market
entity: polymarket
topic: Bitcoin above 72000 on April 21 contract mechanics and cross-line board
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: liquidity
date_created: 2026-04-16
source_name: Polymarket market page
source_type: primary market / contract page
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: market-implied
related_entities: [polymarket, btc]
related_drivers: [liquidity]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-analyses/2026-04-16/dispatch-case-20260416-8bef05aa-20260416T144205Z/personas/market-implied.md
tags: [source-note, polymarket, contract-mechanics, market-board]
---

# Summary

Polymarket’s own contract page provides both the live market-implied probability for the 72,000 line and the governing resolution mechanics. It also shows the surrounding strike ladder, which is useful for inferring whether the board is internally coherent or stale.

## Key facts extracted

- The assigned line `72,000` was trading around `71%` / `0.705` at capture.
- Neighboring outcomes on the same board were roughly:
  - `70,000` at `88%`
  - `72,000` at `71%`
  - `74,000` at `48%`
- Resolution rule: the market resolves Yes if the **Binance BTC/USDT 1 minute candle for 12:00 ET on Apr 21** has a final **Close** price above the threshold.
- The source of truth is explicitly Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the source.

## Evidence directly stated by source

- This is a **close-above** market tied to a single minute close, not a touch/high market.
- The governing source is Binance BTC/USDT candle data.
- The cross-line board suggests an orderly distribution: 72k sits between 70k very likely and 74k near coin-flip.

## What is uncertain

- The public page does not give full market-depth, order-book concentration, or trader-composition detail.
- The page does not prove whether the 71% price is highly efficient versus merely directionally reasonable.

## Why this source may matter

This is the direct market and contract source. It establishes both the market-implied prior and the exact mechanism that must be satisfied for settlement.

## Possible impact on the question

The page supports treating 71% as a serious prior rather than an arbitrary quote. It also prevents a category error: the market is not asking whether BTC touches 72k any time before Apr 21, but whether the noon ET Binance 1m close on Apr 21 is above 72k.

## Reliability notes

Primary for contract wording and live displayed board levels, but only medium-high for efficiency because market microstructure and trader concentration are not visible from the page alone.
