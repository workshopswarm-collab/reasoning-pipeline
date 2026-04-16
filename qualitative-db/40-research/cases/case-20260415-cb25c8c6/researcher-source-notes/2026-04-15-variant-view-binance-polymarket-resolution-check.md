---
type: source_note
case_key: case-20260415-cb25c8c6
dispatch_id: dispatch-case-20260415-cb25c8c6-20260415T194743Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-19
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on 2026-04-19 be above 68000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance public market data endpoints
source_type: mixed-primary-context
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [variant-view-finding]
tags: [polymarket, binance, resolution, timing-risk, source-note]
---

# Summary

This note checks the governing contract mechanics directly from the Polymarket market page and supplements them with Binance public API data to understand the current distance from the threshold and the main variant risk.

## Key facts extracted

- The market resolves from the Binance BTC/USDT **1 minute candle** for **12:00 in the ET timezone (noon)** on **April 19, 2026**.
- The deciding field is the candle's final **Close** price, not intraminute high, low, or another exchange's print.
- The threshold is strictly **higher than 68,000**; equal to 68,000 would not satisfy "above 68,000."
- Binance BTC/USDT public API spot checks on 2026-04-15 showed BTCUSDT around **75,037.79**, with 24h low around **73,514** and high around **75,281**.
- With spot materially above 68k several days before resolution, the obvious base case is Yes, but the contract remains exposed to a single-exchange, single-minute, timestamp-specific close.

## Evidence directly stated by source

From the Polymarket rules page:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."
- "Price precision is determined by the number of decimal places in the source."

From Binance public API checks:
- `/api/v3/ticker/price?symbol=BTCUSDT` returned last price 75037.79 on 2026-04-15.
- `/api/v3/ticker/24hr?symbol=BTCUSDT` returned 24h low 73514 and high 75281 on 2026-04-15.

## What is uncertain

- The exact final 12:00 PM ET candle close on April 19 cannot be known yet.
- The Polymarket page is clear on rules, but web extraction does not itself prove the future Binance UI display format at settlement time.
- Market risk is not mainly ambiguity about source-of-truth; it is the path-dependent chance that BTC drops below 68k by that precise minute.

## Why this source may matter

This is the governing source-of-truth surface for the contract plus a direct exchange-market-data check. It establishes both the narrow mechanics and why a variant view, if any, should focus on single-minute/timestamp fragility rather than broad directional BTC sentiment.

## Possible impact on the question

This source supports a high Yes probability but not a near-certainty. The key variant argument is that a market priced near 98-99% may be underweighting the fact that all of the following must hold simultaneously: Binance remains the operative source, BTC/USDT on Binance stays above 68k into April 19 noon ET, and the exact 12:00 PM ET 1-minute candle closes above 68k.

## Reliability notes

- Polymarket rules page is the authoritative contract-mechanics source for this market.
- Binance public API endpoints are highly relevant direct contextual evidence for current price state, though they do not settle the future outcome.
- Evidence independence is moderate: both sources ultimately key off the same market/exchange complex, but they answer different questions (contract mechanics vs current price context).