---
type: source_note
case_key: case-20260416-ec675d33
dispatch_id: dispatch-case-20260416-ec675d33-20260416T073538Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-20 close above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-ec675d33/researcher-analyses/2026-04-16/dispatch-case-20260416-ec675d33-20260416T073538Z/personas/market-implied.md]
tags: [polymarket, rules, pricing, resolution]
---

# Summary

The Polymarket event page gives both the live market-implied probability for the 72,000 threshold and the governing contract wording. As fetched on 2026-04-16, the 72,000 line traded around 85¢ Yes / 17¢ No, consistent with the assignment's current_price of 0.845. The rules specify a narrow resolution condition: Binance BTC/USDT, 1-minute candle, the candle labeled 12:00 in ET timezone on April 20, and the final Close price must be strictly higher than 72,000.

## Key facts extracted

- The 72,000 outcome displayed about 84% on-page, with Yes around 85¢ and No around 17¢.
- The market resolves on the Binance BTC/USDT pair only.
- The relevant observation is the 1-minute candle for 12:00 PM ET on April 20, 2026.
- The outcome is Yes only if the final Close price is higher than 72,000, not equal to it.
- Price precision is determined by the source's displayed decimal precision.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected on the top bar."
- The event page showed the 72,000 line at roughly 84%-85% when fetched.

## What is uncertain

- The fetched HTML is a public webpage representation rather than a signed exchange record.
- The page does not itself provide the future April 20 resolution print; it only specifies where that print will come from.
- Page percentages and prices can move continuously, so this is time-stamped evidence rather than a stable final state.

## Why this source may matter

This is the direct source for both the current market-implied probability and the contract mechanics. It establishes the exact conditions all of which must hold for Yes: correct exchange, correct pair, correct 1-minute candle, correct timestamp interpretation in ET, and a strictly greater-than threshold.

## Possible impact on the question

This source frames the case as mostly a near-term BTC price question with an important resolution-mechanics overlay. Because the wording is narrow and date-specific, the market price should be judged against the probability that Binance BTC/USDT remains above 72,000 specifically at noon ET on April 20, not just whether BTC trades above that level at some point or on another venue.

## Reliability notes

Strong for contract wording and contemporaneous market pricing because it is the venue's own event page. Weaker as an independent market-fundamentals source because it is the market itself, not an external check.