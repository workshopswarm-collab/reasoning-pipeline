---
type: source_note
case_key: case-20260415-7253c25f
dispatch_id: dispatch-case-20260415-7253c25f-20260415T220737Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-7253c25f | base-rate
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for "Bitcoin above ___ on April 21?"
source_type: market rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7253c25f/researcher-analyses/2026-04-15/dispatch-case-20260415-7253c25f-20260415T220737Z/personas/base-rate.md]
tags: [polymarket, market-rules, resolution-source, btc]
---

# Summary

This source establishes the contract mechanics and provides the current market-implied probability. It says the market resolves "Yes" if the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 21 has a final close strictly higher than $72,000.

## Key facts extracted

- The market title is "Bitcoin above ___ on April 21?"
- The relevant threshold for this line is $72,000.
- Resolution is based on the Binance BTC/USDT 1-minute candle at 12:00 ET on April 21.
- The deciding value is the final "Close" price of that 1-minute candle.
- The comparison is strictly higher than $72,000, not greater-than-or-equal.
- The market page snapshot showed the 72,000 line at about 80% / 81% Yes.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- "Price precision is determined by the number of decimal places in the source."

## What is uncertain

- The web-fetched page is a scraped representation, not the live interactive market UI.
- Polymarket’s scraped page does not independently verify Binance data availability or how Binance labels the noon ET candle in UI terms.

## Why this source may matter

This is the governing market-rules source. It determines the exact settlement conditions and the current market-implied baseline.

## Possible impact on the question

The contract is narrower than a generic "BTC above 72k on April 21" question. A bullish weekly path can still lose if Binance BTC/USDT prints below 72,000 exactly at the noon ET 1-minute close.

## Reliability notes

Useful as the contract-defining source, but not sufficient alone for the probability estimate because it does not provide the underlying BTC path or volatility context. The rules are relatively clear, so source-of-truth ambiguity looks low to medium rather than high.