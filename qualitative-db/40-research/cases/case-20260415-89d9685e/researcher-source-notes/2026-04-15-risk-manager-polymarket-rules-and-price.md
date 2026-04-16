---
type: source_note
case_key: case-20260415-89d9685e
dispatch_id: dispatch-case-20260415-89d9685e-20260415T181939Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: markets
entity: btc
topic: case-20260415-89d9685e | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page for Bitcoin above 72,000 on April 16
source_type: market page / resolution rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
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
downstream_uses: []
tags: [polymarket, resolution-rules, market-price, bitcoin]
---

# Summary

The Polymarket event page gives both the market-implied price for the 72,000 threshold outcome and the operative contract wording. It is the best direct source for what the market currently believes and for the resolution mechanics as presented to traders, but it is not itself the final source of truth for settlement because the rules delegate that to Binance BTC/USDT 1-minute candles.

## Key facts extracted

- The 72,000 threshold contract was priced around 94¢ on 2026-04-15, implying roughly 94% market probability for "Yes".
- The rules say the market resolves to "Yes" if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final close above 72,000.
- The rules explicitly say the settlement source is Binance, specifically the BTC/USDT close price shown with 1m candles selected.
- The contract is exchange-specific and pair-specific: Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the number of decimals in the source.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."
- The event page displayed "Buy Yes 94¢" for the 72,000 line during collection.

## What is uncertain

- The event page is not the official Binance candle record; it only describes which source should govern.
- The page does not itself explain how Binance labels its 1-minute candles relative to ET; that mapping needs separate verification.
- Market price can move after collection.

## Why this source may matter

It defines the contract mechanics traders are using and anchors the market-implied baseline that the researcher must compare against.

## Possible impact on the question

This source shows the market is already treating a close above 72,000 as very likely. It also identifies the key operational and interpretation risks: exact exchange, exact pair, exact 1-minute interval, ET/noon timing, and strict use of the candle close rather than spot or intraminute highs.

## Reliability notes

Useful and necessary for contract interpretation, but not sufficient by itself for the full risk view because it is a market venue page that delegates source-of-truth authority to Binance.