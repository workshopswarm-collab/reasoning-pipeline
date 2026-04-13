---
type: source_note
case_key: case-20260413-f68a8c5c
dispatch_id: dispatch-case-20260413-f68a8c5c-20260413T165914Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260413-f68a8c5c | market-implied
question: Will the price of Bitcoin be above $68,000 on April 14?
driver: reliability
date_created: 2026-04-13
source_name: Polymarket event page rules
source_type: market rules / contract surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, resolution, contract]
---

# Summary

This note captures the contract mechanics and source-of-truth wording from the Polymarket market page.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for `12:00` in ET on April 14 has a final close price higher than 68,000.
- Otherwise it resolves No.
- The specified resolution source is Binance, with `1m` and `Candles` selected.
- The contract is specifically about Binance BTC/USDT, not other exchanges or other trading pairs.
- Price precision is determined by the number of decimal places in the source.
- The visible current market price for the 68,000 line was about 99%, consistent with the assignment’s structured `current_price` value of 0.9595 showing a very high implied probability.

## Evidence directly stated by source

The rules section explicitly names the instrument, timeframe, timezone framing, settlement condition, and source surface.

## What is uncertain

- The page text says `12:00 in the ET timezone (noon)` but does not separately define whether the operative candle is the minute beginning at 12:00:00 ET or ending at 12:00:59 ET; standard Binance 1-minute candle conventions imply the candle labeled 12:00 is the relevant bar.
- The scraped page’s visible odds can lag the assignment’s structured price; the assignment value is cleaner for exact market-implied probability.

## Why this source may matter

This is the governing contract surface. Any forecast must respect these mechanics rather than using generic BTC price intuition.

## Possible impact on the question

The contract wording narrows the relevant event to a single exchange-specific 1-minute closing print at a specific ET timestamp, which keeps a small but real residual chance of failure even if BTC is comfortably above 68k beforehand.

## Reliability notes

- High credibility as the contract/rules page itself.
- Essential for date/timing and multi-condition verification.
- Main caveat is minor implementation ambiguity around candle labeling, not around the exchange/pair/source-of-truth itself.
