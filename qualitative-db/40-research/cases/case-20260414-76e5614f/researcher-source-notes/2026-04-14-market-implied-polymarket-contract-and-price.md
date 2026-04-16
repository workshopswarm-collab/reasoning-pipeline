---
type: source_note
case_key: case-20260414-76e5614f
dispatch_id: dispatch-case-20260414-76e5614f-20260414T182607Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page for Bitcoin above $72,000 on April 17
source_type: market page / contract page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
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
downstream_uses: []
tags: [polymarket, contract, resolution-source, btc]
---

# Summary

This source defines the market-implied baseline and the governing contract mechanics. It shows the current implied probability for the $72,000 threshold and states that settlement depends specifically on the Binance BTC/USDT 1-minute candle at 12:00 PM ET on April 17, 2026.

## Key facts extracted

- The $72,000 line is trading around 84¢ yes / 19¢ no on the fetched page, consistent with the assignment baseline of 0.83.
- The market resolves "Yes" only if the Binance BTC/USDT 1-minute candle for 12:00 PM ET on April 17 has a final close strictly higher than 72,000.
- The relevant source is Binance BTC/USDT, not other exchanges or BTC/USD pairs.
- Price precision is determined by the source display.
- Adjacent strikes imply a monotonic surface: about 60% for above 74k and about 34% for above 76k, which gives context for how the crowd is shaping the BTC distribution around noon ET on April 17.

## Evidence directly stated by source

- Current market pricing for the threshold ladder.
- Exact wording of resolution conditions.
- Exact source-of-truth venue and pair.

## What is uncertain

- The fetched page does not expose order-book depth or time series, so it does not by itself show how stable the 83-84% price is.
- The event page is a secondary interface for the contract; actual settlement still depends on Binance market data at resolution time.

## Why this source may matter

This is the primary source for the market-implied probability and for the contract wording. Because the contract is narrow and date-specific, understanding the exact noon ET Binance close condition is mandatory.

## Possible impact on the question

This source establishes that the research question is not “will BTC generally trade above 72k around April 17,” but whether Binance BTC/USDT prints a 12:00 PM ET 1-minute candle close above 72,000 on that date. That narrows the analysis to both price level and timing/path dependence.

## Reliability notes

Reliable for contract wording and displayed market price. Not authoritative for the final answer itself, because the source of truth at settlement is Binance rather than Polymarket’s display layer.