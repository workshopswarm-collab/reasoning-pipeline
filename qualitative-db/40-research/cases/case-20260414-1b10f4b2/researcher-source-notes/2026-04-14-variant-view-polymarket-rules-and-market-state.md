---
type: source_note
case_key: case-20260414-1b10f4b2
dispatch_id: dispatch-case-20260414-1b10f4b2-20260414T201759Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the price of Bitcoin be above $68,000 on April 20?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [variant-view.md, variant-view.md#Resolution or source-of-truth interpretation]
tags: [polymarket, contract-rules, binance, resolution]
---

# Summary

This source establishes the governing contract mechanics and the current market-implied probability. It shows that the relevant outcome is not a daily close or spot average, but the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 20, with the final close required to be strictly above 68000.

## Key facts extracted

- The current market-implied probability for the 68000 threshold is about 94%.
- Resolution is based on Binance BTC/USDT, not other exchanges or pairs.
- The relevant data point is the 1-minute candle for 12:00 ET (noon) on April 20.
- The contract requires the final close to be higher than 68000; if not higher, resolution is No.
- Price precision is whatever Binance displays in the source.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."
- The market page displayed the 68000 line around 94% at fetch time.

## What is uncertain

- The market page itself is not the settlement source; Binance is.
- The exact interpretation of the 12:00 ET candle label on Binance UI should still be treated carefully because UI labeling/timezone presentation can differ by interface locale.

## Why this source may matter

This is the governing market contract surface. The main variant risk in an otherwise high-probability setup is not broad BTC direction but narrow resolution mechanics: exact exchange, exact pair, exact minute, exact timezone, and strict greater-than test.

## Possible impact on the question

This source materially raises confidence that the market is mostly a question about avoiding a sharp BTC drawdown below 68000 by one specific minute on one specific exchange. It also identifies the key tail risk: exchange-specific or minute-specific deviation rather than broad market weakness alone.

## Reliability notes

Useful and necessary for contract interpretation, but only medium credibility as an evidence source for outcome probability because it is not the underlying settlement feed itself.