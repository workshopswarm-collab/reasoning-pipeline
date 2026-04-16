---
type: source_note
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 70000 on 2026-04-20?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market_contract
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3ae5a275/researcher-analyses/2026-04-14/dispatch-case-20260414-3ae5a275-20260414T202946Z/personas/variant-view.md]
tags: [source-note, polymarket, contract, binance, resolution]
---

# Summary

The Polymarket market page provides both the market-implied probability snapshot and the governing resolution mechanics. For the 70,000 line, the page showed roughly 85% at fetch time, consistent with assignment `current_price: 0.855`. The critical contract detail is that settlement is based on the Binance BTC/USDT 1-minute candle for **12:00 ET** on April 20, using the final **Close** value, not any intraday high, daily close, or cross-exchange composite.

## Key facts extracted

- Market title: Bitcoin above 70,000 on April 20.
- 70,000 line displayed at about 85% / 86c Yes.
- Resolution requires the Binance BTC/USDT **1-minute candle** at **12:00 ET (noon)** on the specified date.
- The relevant price field is the candle's final **Close** price.
- Resolution is exchange-specific: Binance BTC/USDT only, not another venue or pair.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... BTC/USDT ... with '1m' and 'Candles' selected."
- The 70,000 bucket was shown around 85% at time of capture.

## What is uncertain

- The webpage fetch is a scrape, not an authenticated exchange feed.
- The market page itself does not explain how ET maps during DST beyond saying ET/noon; operationally this should mean America/New_York local time, which is EDT on Apr. 20, 2026.
- The market page does not itself provide live Binance candle history for verification.

## Why this source may matter

This is the governing source for contract interpretation, which is crucial because a narrow time-window contract can diverge materially from a looser "BTC stays above 70k generally" intuition.

## Possible impact on the question

This source makes timing/path dependence central. A bullish BTC backdrop is not enough by itself; all material conditions must hold simultaneously: correct date, correct venue/pair, correct 12:00 ET minute, and final close > 70,000.

## Reliability notes

High reliability for contract terms and snapshot market state because this is the listed market page itself. It is not the settlement value source; Binance remains the actual source of truth for resolution.