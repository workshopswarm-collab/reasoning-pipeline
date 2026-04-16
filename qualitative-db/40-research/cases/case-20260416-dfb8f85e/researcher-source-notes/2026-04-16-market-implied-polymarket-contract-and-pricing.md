---
type: source_note
case_key: case-20260416-dfb8f85e
dispatch_id: dispatch-case-20260416-dfb8f85e-20260416T140232Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the price of Bitcoin be above $72,000 on April 21?
driver:
date_created: 2026-04-16
source_name: Polymarket market page and contract rules
source_type: prediction_market_primary
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-dfb8f85e/researcher-analyses/2026-04-16/dispatch-case-20260416-dfb8f85e-20260416T140232Z/personas/market-implied.md]
tags: [polymarket, contract, resolution, market-price]
---

# Summary

Polymarket shows the contract wording, source-of-truth rules, and the current market-implied price for the 72,000 threshold outcome.

## Key facts extracted

- The specific outcome relevant here is the Apr 21, 2026 threshold market for BTC above 72,000.
- The market page showed the 72,000 line at roughly 79% at fetch time; assignment context listed current_price 0.71.
- Contract resolves Yes if the Binance BTC/USDT 1 minute candle for 12:00 ET on Apr 21 has a final close above 72,000.
- Contract is explicitly about Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the source's decimals.

## Evidence directly stated by source

- The governing settlement source is Binance BTC/USDT 1m candle close at 12:00 ET on the specified date.
- The market is multi-condition: exchange/pair must match, timestamp must match, and close price must be above 72,000.
- The market price itself implies a high but not near-certain probability of Yes.

## What is uncertain

- Web fetch may lag or represent a slightly different moment than assignment metadata, so the exact live probability may have moved between 71% and ~80%.
- The market page alone does not prove spot/reference price on Binance at the time of research; it only shows what the market is pricing.

## Why this source may matter

This is the governing contract source and the only direct way to verify what resolution mechanics count.

## Possible impact on the question

The contract wording materially matters because this is not a generic "BTC above 72k sometime that day" market. It is a narrow question about the final close of one specific Binance 1m candle at noon ET on Apr 21.

## Reliability notes

Good for contract interpretation and market-implied baseline. Less authoritative for underlying BTC price than Binance itself.