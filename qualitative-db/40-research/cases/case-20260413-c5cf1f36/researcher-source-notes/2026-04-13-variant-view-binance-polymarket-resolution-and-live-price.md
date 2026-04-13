---
type: source_note
case_key: case-20260413-c5cf1f36
dispatch_id: dispatch-case-20260413-c5cf1f36-20260413T181345Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-66k-on-april-15
question: Will the Binance BTC/USDT 12:00 PM ET one-minute candle close on 2026-04-15 above 66000?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket rules page and Binance public market data
source_type: primary_plus_primary_market_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, binance, resolution, btc]
---

# Summary

This source note captures the governing contract mechanics and a contemporaneous live-price anchor relevant to the April 15 noon ET resolution window.

## Key facts extracted

- The market resolves from the Binance BTC/USDT **1 minute candle for 12:00 in ET timezone (noon)** on April 15, 2026.
- The relevant value is the candle's **final Close** price, not an intraminute high, low, or another exchange print.
- Price precision is determined by Binance source decimals.
- On 2026-04-13 during this research pass, Binance public API returned BTCUSDT spot around **72,191.22**.
- Recent Binance daily candles show BTC closing materially above 66,000 for the last several days leading into the event window.

## Evidence directly stated by source

From the Polymarket market page rules:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."

From Binance public API during this pass:
- ticker price: 72191.22000000
- last five 1m closes observed during the pass were all ~72146 to ~72191
- recent daily closes from Apr 4 to Apr 13 all printed above 66,000, with Apr 13 daily data at the time of query showing close 72191.22000000

## What is uncertain

- The actual resolving print is still about two days away; BTC can move several thousand dollars in that time.
- Binance API/public site availability and final candle display behavior remain small but nonzero operational considerations.
- Daily candles are contextual only; they do not settle the contract.

## Why this source may matter

This is the direct resolution framework plus a current exchange anchor. It establishes that the market is not asking about generalized "Bitcoin above 66k" on average, but a very specific Binance one-minute ET-noon closing print.

## Possible impact on the question

The direct evidence supports a strong Yes baseline because spot is currently more than 6,000 above the strike. The main credible variant case is not broad bearishness alone, but that the market may still be mildly overconfident because a narrow one-minute, exchange-specific, time-specific contract can fail even when the broader BTC narrative remains bullish.

## Reliability notes

- Polymarket rules page is the governing market source-of-truth for contract interpretation.
- Binance public API is a strong direct source for current exchange pricing context, though only the actual April 15 12:00 ET one-minute candle will settle the market.
- This note combines one governing source and one direct market-data source; independence is medium rather than high because both center on the same exchange-resolution setup.