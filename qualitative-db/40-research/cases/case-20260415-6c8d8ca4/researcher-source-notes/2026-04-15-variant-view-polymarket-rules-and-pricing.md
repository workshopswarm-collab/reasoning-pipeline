---
type: source_note
case_key: case-20260415-6c8d8ca4
dispatch_id: dispatch-case-20260415-6c8d8ca4-20260415T084705Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market-contract-page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-6c8d8ca4/researcher-analyses/2026-04-15/dispatch-case-20260415-6c8d8ca4-20260415T084705Z/personas/variant-view.md]
tags: [polymarket, rules, contract, resolution]
---

# Summary

This source defines the market-implied baseline and the governing contract mechanics. It says the market resolves from the Binance BTC/USDT 1-minute candle at 12:00 ET on April 17, using the final Close price, with price precision determined by Binance.

## Key facts extracted

- The 72,000 line was trading around 81% on the market page at fetch time.
- Resolution is not based on daily close, CME, Coinbase, or consolidated BTC spot; it is specifically Binance BTC/USDT.
- The decisive print is the 1-minute candle for 12:00 ET on the named date.
- The condition is strictly higher than 72,000.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The market page is not itself the final settlement record; it describes the rule but does not provide the future decisive candle.
- The web fetch view can duplicate page text and is not ideal for exact live pricing precision, so it is better for rule capture than microstructure analysis.

## Why this source may matter

The contract is narrow and timing-sensitive. Misreading the source of truth or the required candle would create a false edge.

## Possible impact on the question

This source establishes that all bullish reasoning must survive a very specific timestamp and exchange filter. It slightly supports a cautious variant view because a contract based on a single minute on one venue is more fragile than a generic "BTC above 72k that day" framing.

## Reliability notes

Good for contract wording and approximate market pricing; weaker than direct Binance data for the actual underlying spot state.