---
type: source_note
case_key: case-20260415-f07c9e26
dispatch_id: dispatch-case-20260415-f07c9e26-20260415T013036Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-14T21:33:00-04:00
source_name: Polymarket event page and rules
source_type: market rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
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
downstream_uses: []
tags: [polymarket, rules, contract, market-price]
---

# Summary

This source note captures the contract wording and the current market-implied baseline from the Polymarket event page.

## Key facts extracted

- The market asks whether the Binance BTC/USDT 1-minute candle for `12:00` in ET on April 16 will have a final close above $72,000.
- The rules specify Binance BTC/USDT with `1m` candles as the resolution source and note that price precision is determined by the number of decimals in the source.
- The visible price for the `$72,000` line was about `91%` / `91¢` Yes at fetch time.
- Nearby ladder prices imply a distribution centered above $72,000, with $74,000 still around the mid-60s.

## Evidence directly stated by source

- Contract mechanics, timing convention, and named source-of-truth surface.
- Live market price for the exact threshold being researched.

## What is uncertain

- The page does not explain whether Binance API and Binance UI can ever diverge in display/rounding at the exact settlement moment.
- The event page gives the market price but not the trader reasoning behind it.

## Why this source may matter

This source defines the contract. It is the governing rules surface for what counts as Yes or No and is also the only direct source for the current market-implied probability.

## Possible impact on the question

The rules page makes clear that the key condition is not a daily close or another venue's price, but a very specific Binance 1-minute noon-ET close. The live 91% price indicates traders see a relatively low probability of BTC falling below $72,000 by that exact timestamp.

## Reliability notes

- High credibility for market mechanics and current price because it is the native market page.
- Not independent of the market itself; it is authoritative for rules and price but not for validating the future path of BTC.
