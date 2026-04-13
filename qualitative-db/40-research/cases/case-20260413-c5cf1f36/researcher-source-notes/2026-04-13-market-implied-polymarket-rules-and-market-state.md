---
type: source_note
case_key: case-20260413-c5cf1f36
dispatch_id: dispatch-case-20260413-c5cf1f36-20260413T181345Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260413-c5cf1f36 | market-implied
question: Will the price of Bitcoin be above $66,000 on April 15?
date_created: 2026-04-13
source_name: Polymarket event page and market rules for Bitcoin above ___ on April 15
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-c5cf1f36/researcher-analyses/2026-04-13/dispatch-case-20260413-c5cf1f36-20260413T181345Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-implied, resolution]
---

# Summary

The Polymarket event page provides both the live market-implied probability for the 66,000 strike and the governing contract mechanics. For the Apr 15 12:00 PM ET market, the 66,000 line was showing roughly 99% Yes at capture time, implying the market strongly expects Binance BTC/USDT to remain above that threshold at the specified noon ET 1-minute close.

## Key facts extracted

- The event page listed the Apr 15 66,000 outcome at about 99% Yes.
- The contract resolves from the Binance BTC/USDT 1-minute candle for 12:00 in ET on the specified date.
- The decisive field is the final candle "Close" price, not high/low, not another exchange, and not another pair.
- Price precision is whatever Binance displays in the source.

## Evidence directly stated by source

- Resolution source: Binance.
- Instrument: BTC/USDT.
- Time condition: 12:00 PM ET on Apr 15, 2026.
- Resolution condition: the final 1-minute candle close must be higher than 66,000 for Yes.

## What is uncertain

- The event page itself is not the final settlement source; it points to Binance as the source of truth.
- The page does not itself explain any hidden edge-case handling beyond the quoted rule text.

## Why this source may matter

This is the key contract-definition source for what exactly must happen. The market-implied price is only meaningful if the resolution mechanics are correctly interpreted, especially because this is a date-specific, narrow-resolution market.

## Possible impact on the question

The source makes the market's extreme pricing easier to understand: with BTC spot already materially above 66,000, only a large downward move by the exact Binance BTC/USDT noon ET 1-minute close would flip the market to No.

## Reliability notes

Polymarket is authoritative for contract wording and live market price, but not for the final observed BTC price itself. For settlement-level interpretation, Binance remains the governing source of truth.