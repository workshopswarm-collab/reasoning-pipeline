---
type: source_note
case_key: case-20260413-9e664afd
dispatch_id: dispatch-case-20260413-9e664afd-20260413T164930Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260413-9e664afd | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 70000 on April 14, 2026?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket event page and rules for bitcoin-above-on-april-14
source_type: market rules / market state
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9e664afd/researcher-analyses/2026-04-13/dispatch-case-20260413-9e664afd-20260413T164930Z/personas/market-implied.md]
tags: [polymarket, rules, market-state, binance, source-of-truth]
---

# Summary

This source established both the current market-implied baseline for the 70,000 threshold and the exact contract mechanics.

## Key facts extracted

- The displayed price for the 70,000 threshold was 93% on the fetched event page.
- The market resolves Yes if the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 14 has a final Close price above 70,000.
- The source of truth is Binance BTC/USDT with 1m candles selected.
- The contract is exchange-specific and pair-specific: Binance BTC/USDT, not another venue or pair.
- Price precision is determined by the number of decimals shown in the Binance source.

## Evidence directly stated by source

- Resolution depends on the Binance 1-minute candle close at 12:00 ET on the specified date.
- The 70,000 line was trading around 93% at fetch time.

## What is uncertain

- The fetched page is a web snapshot, not an authenticated API pull.
- The page text does not independently prove whether the displayed percentage is the final best market price at the exact assignment timestamp.
- Polymarket’s page does not itself provide the Binance close; it only specifies the rule.

## Why this source may matter

It is the governing contract source for what counts, what timestamp matters, and which venue determines settlement. Without this rules check, the market could be misread as a generic BTC/USD level question rather than a very specific Binance BTC/USDT noon-ET candle-close question.

## Possible impact on the question

This source makes the case mostly about whether BTC/USDT can stay above 70,000 until the specific noon-ET 1-minute close, not whether bitcoin is broadly bullish in a loose daily sense.

## Reliability notes

Primary for contract wording and source-of-truth designation. Medium-high credibility for resolution mechanics; weaker for exact live price than a dedicated market API would be.