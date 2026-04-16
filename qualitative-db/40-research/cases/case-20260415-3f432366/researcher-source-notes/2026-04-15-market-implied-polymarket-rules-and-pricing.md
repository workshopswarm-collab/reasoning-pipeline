---
type: source_note
case_key: case-20260415-3f432366
dispatch_id: dispatch-case-20260415-3f432366-20260415T074424Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3f432366/researcher-analyses/2026-04-15/dispatch-case-20260415-3f432366-20260415T074424Z/personas/market-implied.md]
tags: [polymarket, contract-rules, pricing, source-note]
---

# Summary

This source establishes both the current market-implied baseline and the governing contract mechanics for resolution.

## Key facts extracted

- The assigned current price for the 72,000 strike is 0.745 in the run prompt; the fetched market page showed the displayed 72,000 contract around 75-76% at retrieval time.
- The market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final Close strictly higher than 72,000.
- The specified source of truth is Binance BTC/USDT with 1m candles selected.
- The contract is exchange-specific and pair-specific; other exchanges or BTC/USD references do not govern resolution.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- Resolution source: Binance BTC/USDT.
- Resolution window: the 12:00 ET candle on the date in the title.
- Winning condition: final Close price higher than 72,000, not merely touching or averaging above.

## What is uncertain

- The web-fetched market page is a scraped snapshot and can lag live price slightly.
- The exact Binance UI display path can change, though the rule text clearly names the underlying source series.

## Why this source may matter

This is the governing settlement source and the direct source for market-implied consensus. It determines what counts and what does not count.

## Possible impact on the question

Because the contract is tied to one specific 1-minute Binance close at noon ET, intra-minute spikes, other exchange prints, and daily closes are not enough by themselves. This narrows the event and slightly increases path/timing risk versus a looser “BTC above 72k on the day” framing.

## Reliability notes

Useful as the primary contract source, but the market-page odds are a tradable snapshot rather than a stable historical record. For resolution interpretation it is authoritative; for live price it is good but should be cross-checked when precision matters.
