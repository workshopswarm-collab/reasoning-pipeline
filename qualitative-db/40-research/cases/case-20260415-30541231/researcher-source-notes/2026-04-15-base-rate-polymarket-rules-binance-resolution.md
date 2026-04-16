---
type: source_note
case_key: case-20260415-30541231
dispatch_id: dispatch-case-20260415-30541231-20260415T133406Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page for Bitcoin above ___ on April 17
source_type: market-rule-page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-30541231/researcher-analyses/2026-04-15/dispatch-case-20260415-30541231-20260415T133406Z/personas/base-rate.md]
tags: [polymarket, binance, resolution-criteria, source-note]
---

# Summary

This source note captures the contract mechanics and governing resolution surface for the market.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for **12:00 ET (noon)** on April 17 has a final **Close** price strictly higher than 72,000.
- The market resolves No otherwise.
- The source of truth is Binance, specifically the BTC/USDT market with **1m** candles.
- The contract is explicitly about **Binance BTC/USDT**, not other exchanges or pairs.
- Price precision is determined by the source.

## Evidence directly stated by source

Directly stated on the market page rules section:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The Polymarket page itself is not the underlying price source; it only states the rule and resolution reference.
- It does not by itself provide the future April 17 noon ET candle close.

## Why this source may matter

This is the governing rule surface. Because the contract is narrow, date-specific, and source-specific, getting the exact resolution mechanics right is necessary before any probability estimate is useful.

## Possible impact on the question

This sharply narrows what matters: only the Binance BTC/USDT 12:00 ET one-minute close on April 17 counts. Broader narratives about Bitcoin price on other exchanges, earlier/later timestamps, or daily closes only matter contextually.

## Reliability notes

Reliable for contract interpretation, but not for underlying market data. Best used as the resolution-mechanics source paired with Binance price data as the direct contextual market source.
