---
type: source_note
case_key: case-20260416-653ab0f8
dispatch_id: dispatch-case-20260416-653ab0f8-20260416T090226Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-18
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on April 18, 2026?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market page and contract rules
source_type: market_contract
source_url: https://polymarket.com/event/bitcoin-above-on-april-18
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-653ab0f8/researcher-analyses/2026-04-16/dispatch-case-20260416-653ab0f8-20260416T090226Z/personas/variant-view.md]
tags: [polymarket, contract, source-note, threshold-market]
---

# Summary

The Polymarket contract explicitly resolves on whether the Binance BTC/USDT 1-minute candle for 12:00 ET on April 18 has a final close above 72,000. The same market page showed the 72,000 line trading around 88% Yes at retrieval time.

## Key facts extracted

- Current market-implied probability for the 72,000 line was approximately 88% Yes.
- Contract condition is binary: Yes if the Binance BTC/USDT 12:00 ET 1-minute candle close is higher than 72,000; otherwise No.
- Source of truth is specifically Binance BTC/USDT, not other exchanges and not other pairs.
- Precision is determined by the number of decimal places in the Binance source.
- The market closes/resolves at 12:00 ET on April 18, 2026.

## Evidence directly stated by source

- Exact threshold: 72,000.
- Exact timing window: 12:00 in ET timezone.
- Exact instrument: Binance BTC/USDT.
- Exact comparison rule: final close price must be higher than 72,000.

## What is uncertain

- The page does not itself quantify expected volatility into settlement.
- The page does not clarify edge handling beyond the stated source/precision language if Binance UI behavior changes, though the rule text is clear enough for ordinary use.

## Why this source may matter

This source defines what must be true for the market to resolve Yes or No and therefore governs all other interpretation.

## Possible impact on the question

It narrows the research problem to a short-horizon BTC downside-risk question under a specific exchange, pair, timeframe, and timestamp. It also makes cross-exchange or BTC/USD commentary secondary unless it changes expectations for Binance BTC/USDT at the exact resolution minute.

## Reliability notes

High reliability for contract wording and current market state. This is the governing source for resolution logic, but not the future outcome itself.
