---
type: source_note
case_key: case-20260413-de71fc13
dispatch_id: dispatch-case-20260413-de71fc13-20260413T130158Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260413-de71fc13 | risk-manager
question: Will the price of Bitcoin be above $68,000 on April 13?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market rules page
source_type: market rules / resolution source description
source_url: https://polymarket.com/event/bitcoin-above-on-april-13
source_date: 2026-04-13
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
downstream_uses: [qualitative-db/40-research/cases/case-20260413-de71fc13/researcher-analyses/2026-04-13/dispatch-case-20260413-de71fc13-20260413T130158Z/personas/risk-manager.md]
tags: [polymarket, rules, resolution, timing]
---

# Summary

Polymarket states that this market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 13, using the final close price on Binance with 1m candles selected. The contract is exchange-specific and time-specific.

## Key facts extracted

- "Yes" resolves only if the Binance BTC/USDT 12:00 ET 1-minute candle close is higher than 68,000.
- The source of truth is Binance, not a composite index or another exchange.
- Time interpretation matters: the relevant candle is the one labeled 12:00 ET on Apr. 13.
- Price precision is whatever Binance displays for that source candle.

## Evidence directly stated by source

- The rules explicitly name Binance BTC/USDT as the resolution source.
- The rules explicitly say 1-minute candle, 12:00 ET, and final close price.
- The market page showed the 68,000 line trading around 99.7% Yes at fetch time.

## What is uncertain

- The public page is not itself the authoritative settlement print; it is the contract/rules surface pointing to Binance.
- The exact UI labeling on Binance can create timezone interpretation risk if not converted carefully.

## Why this source may matter

This source defines the contract mechanics and narrows the relevant evidence to one exact exchange, one exact pair, one timeframe, and one close value.

## Possible impact on the question

The market can still fail even if BTC is above 68k on other venues or at nearby times, so the main residual risk is contract-mechanics/timing risk plus a sharp selloff before the noon ET candle closes.

## Reliability notes

Useful for resolution mechanics, but not enough by itself for the actual price outcome because Polymarket points onward to Binance as the governing source of truth.