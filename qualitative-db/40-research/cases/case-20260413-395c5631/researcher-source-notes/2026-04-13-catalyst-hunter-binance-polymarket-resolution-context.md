---
type: source_note
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-15 be above 72000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance API and Polymarket market page
source_type: primary_market_and_resolution_context
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, binance, resolution]
---

# Summary

This source pair establishes the contract mechanics and the current spot context that matters most for a date-specific BTC threshold market.

## Key facts extracted

- Polymarket states the market resolves using the Binance BTC/USDT 1-minute candle for 12:00 ET on April 15, 2026.
- The condition is specifically that the final candle close must be higher than 72,000; equal to 72,000 would resolve No.
- The source of truth is Binance BTC/USDT, not other exchanges or other BTC pairs.
- Binance spot API on 2026-04-13 showed BTCUSDT around 74,164 shortly after assignment time.
- Recent Binance daily closes from the API showed a sequence roughly 71,788 -> 72,963 -> 73,043 -> 70,741 -> 74,164, implying high short-horizon volatility but current price still above the target threshold.
- Recent 3-hour 1-minute range sampled during the run was about 72,555 to 74,420, so the market has recently traded above 72,000 with room to spare, but intraday swings are large enough that a sub-72k print by resolution remains plausible.

## Evidence directly stated by source

From Polymarket market page:
- resolution uses Binance BTC/USDT 1m candle at 12:00 ET on the specified date
- resolve Yes only if final close is higher than the specified price

From Binance API:
- current spot price is above 72,000 as of 2026-04-13
- recent realized trading range around the threshold remains material

## What is uncertain

- Binance spot price at the exact noon ET resolution minute on April 15 remains highly path dependent.
- The market page does not by itself explain what macro or flow catalysts could move BTC over the next ~36 hours.
- Short-term volatility could erase the current cushion quickly.

## Why this source may matter

This is the governing source pair for a narrow, date-specific contract. It tells us both what counts mechanically and whether BTC currently has a meaningful buffer over the strike.

## Possible impact on the question

Because BTC is currently above the threshold and recently traded with a cushion above it, the base case leans Yes. But the contract is narrow enough that timing and volatility matter more than a generic bullish Bitcoin thesis.

## Reliability notes

- Polymarket is authoritative for contract wording but not for final underlying price.
- Binance BTC/USDT is the operative resolution source for the underlying value.
- API data is strong for spot context and recent realized volatility, though not itself a guarantee of the exact final settlement minute outcome.
