---
type: source_note
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 15, 2026 close above 72000?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market page and rules
source_type: market rules / venue page
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [risk-manager.md, risk-manager.md#resolution-or-source-of-truth-interpretation]
tags: [polymarket, market-rules, resolution-source, binance]
---

# Summary

This source defines the market structure, current market-implied price, and the governing settlement rule: the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 15, 2026 must have a final Close price above 72,000 for the answer to resolve Yes.

## Key facts extracted

- The relevant threshold market was trading around 73% Yes at review time.
- Resolution depends on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 15, 2026.
- The deciding field is the candle's final Close price, not intraminute high or another exchange's quote.
- Price precision is whatever Binance displays / returns for the source candle.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The market page itself does not explain implementation details for ET-to-candle mapping beyond the plain-language rule.
- It does not clarify edge-case handling if Binance UI and API presentation differ, so separate Binance documentation is useful contextual verification.

## Why this source may matter

This is the primary contract and source-of-truth description. For a date-specific, multi-condition market, rule interpretation is at least as important as directional BTC price analysis.

## Possible impact on the question

This source sharply limits what counts: BTC must be above 72,000 specifically on Binance BTC/USDT, specifically using the 12:00 ET 1-minute candle close on April 15. That creates timing risk and exchange-specific risk even if broader BTC sentiment is bullish.

## Reliability notes

Strong for contract wording and current market baseline, but only medium overall as a settlement guide because it points to Binance without fully documenting candle API semantics. A second source is needed for implementation confidence.