---
type: source_note
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-f29db686 | variant-view
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules for bitcoin-above-on-april-17
source_type: market contract / rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/personas/variant-view.md]
tags: [polymarket, contract, resolution-source, binance, btc]
---

# Summary

Polymarket's rules make this a narrowly specified contract on a single Binance BTC/USDT 1-minute candle close at 12:00 ET on April 17, not a broad question about where BTC trades generally during the day.

## Key facts extracted

- The visible market price for the 74,000 line was about 66-67%, while assignment context gave `current_price: 0.605`.
- The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for `12:00` in ET timezone has a final `Close` strictly higher than 74,000.
- The governing source is Binance with `1m` candles selected.
- The rules explicitly say this is about Binance BTC/USDT, not other exchanges or other trading pairs.
- Precision is determined by Binance source decimals.

## Evidence directly stated by source

Directly from the market page/rules:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The page is a market UI rather than a technical specification of how Binance labels the noon ET candle internally.
- Visible price on the page can move quickly; assignment context is likely the better pinned run-time baseline.
- The page itself does not provide historical volatility or distribution around noon ET next day.

## Why this source may matter

It is the contract-governing source for what counts. For a date-sensitive, multi-condition market, most variant edge comes from interpreting the precise resolution mechanics rather than from generic BTC sentiment.

## Possible impact on the question

This source lowers confidence in any naive "BTC is above 74k now so Yes is favored" framing. All of the following must hold for Yes:
1. Binance BTC/USDT remains above 74,000 through the relevant observation window.
2. The specific 12:00 ET 1-minute candle is the one used.
3. The final close of that exact candle is above 74,000, not merely the spot price shortly before or after.

## Reliability notes

High reliability on contract interpretation because this is the market's own rules page. Moderate limitations for probability estimation because it does not itself provide independent price-distribution evidence.