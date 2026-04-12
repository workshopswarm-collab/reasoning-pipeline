---
type: source_note
case_key: case-20260409-99902b0b
dispatch_id: dispatch-case-20260409-99902b0b-20260409T203957Z
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-10
question: Will the price of Bitcoin be above $70,000 on April 10?
driver: operational-risk
date_created: 2026-04-09
source_name: Polymarket market page and rules
source_type: market listing / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-10
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, resolution, source-note]
---

# Summary

The Polymarket market page provides both the current market-implied probability for the $70,000 threshold and the governing resolution mechanics. The key contract detail is that settlement depends on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 10, specifically the final Close price, not an intraday high, daily close, or cross-exchange average.

## Key facts extracted

- The $70,000 threshold contract was trading around 95% Yes at fetch time.
- The market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 10 has a final Close above $70,000.
- The resolution source is Binance BTC/USDT with 1m Candles selected.
- The contract is exchange-specific and pair-specific: Binance BTC/USDT, not another exchange or pair.
- Price precision is determined by the number of decimals in the source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The fetched page is a live market surface and can move quickly; the market-implied probability is time-sensitive.
- The page itself does not provide a direct historical time-series of the probability path around the threshold.
- The page does not independently verify whether Binance UI and Binance API will present identical formatting at settlement time, though both point to Binance as source of truth.

## Why this source may matter

This is the governing source for both market-implied probability and contract interpretation. Because the contract is narrow and time-specific, precise wording matters as much as broader BTC directional analysis.

## Possible impact on the question

This source makes the decision problem much narrower than "Will BTC trade above 70k tomorrow?" It instead asks whether BTC stays above $70,000 specifically into the noon ET 1-minute close on Binance. That raises the importance of near-term timing, exchange-specific prints, and any last-hour volatility or operational anomalies.

## Reliability notes

High reliability for contract wording because this is the market's own rules page. Lower reliability for broader price inference because it is not the underlying exchange data source itself.