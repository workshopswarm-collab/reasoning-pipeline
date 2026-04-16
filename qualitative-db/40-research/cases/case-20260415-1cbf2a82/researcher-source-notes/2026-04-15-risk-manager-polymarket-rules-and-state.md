---
type: source_note
case_key: case-20260415-1cbf2a82
dispatch_id: dispatch-case-20260415-1cbf2a82-20260415T144104Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity: btc
topic: case-20260415-1cbf2a82 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 17?
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1cbf2a82/researcher-analyses/2026-04-15/dispatch-case-20260415-1cbf2a82-20260415T144104Z/personas/risk-manager.md]
tags: [source-note, polymarket, contract-interpretation, btc]
---

# Summary

The Polymarket contract states that the market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 17, using the candle's final Close price. The page also shows the current market state for the $72,000 threshold at roughly 84% Yes / 18% No on the fetched page, while assignment metadata gives current_price = 0.845.

## Key facts extracted

- Resolution is based on Binance, not a cross-exchange composite.
- The relevant instrument is BTC/USDT.
- The relevant bar is the 1-minute candle for 12:00 ET on April 17.
- The deciding field is the candle's final Close price.
- The condition is strictly higher than $72,000.
- Assignment metadata says current_price = 0.845, implying about 84.5% Yes.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... BTC/USDT... '1m' and 'Candles' selected..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The market page is not itself the final settlement authority; it describes the intended source-of-truth, but the actual resolving datum still must come from Binance at the specified minute.
- The exact mapping from "12:00 in ET" to the Binance candle timestamp should be checked at settlement time because Binance API timestamps are in UTC milliseconds.
- The fetched page displays slightly rounded pricing, while assignment metadata is more precise.

## Why this source may matter

This is the governing contract-language source for what counts, what exchange matters, and which candle field decides the outcome. It is the key source for timing and multi-condition interpretation risk.

## Possible impact on the question

This source narrows the forecast from a generic "BTC around then" question to a precise one-minute, one-exchange, one-field settlement event. That reduces ambiguity but increases path/timing risk: BTC can be above $72k broadly yet still fail if the specific Binance 12:00 ET one-minute close is $72,000 or lower.

## Reliability notes

Useful as the contract-definition source, but not sufficient by itself for price direction. It is authoritative about resolution mechanics, not about whether BTC will actually trade above the threshold at settlement.