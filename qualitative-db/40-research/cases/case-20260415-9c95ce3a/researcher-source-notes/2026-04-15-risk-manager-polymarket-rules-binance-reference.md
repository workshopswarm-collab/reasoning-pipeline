---
type: source_note
case_key: case-20260415-9c95ce3a
dispatch_id: dispatch-case-20260415-9c95ce3a-20260415T173129Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page for Bitcoin above ___ on April 17
source_type: market rules / resolution source reference
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-9c95ce3a/researcher-analyses/2026-04-15/dispatch-case-20260415-9c95ce3a-20260415T173129Z/personas/risk-manager.md]
tags: [polymarket, resolution-rules, binance, date-sensitive]
---

# Summary

This source establishes the governing contract mechanics. The market does not resolve on a daily close, intraday high, or cross-exchange composite price. It resolves on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 17, using the final Close value.

## Key facts extracted

- Resolution is Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final Close strictly higher than 72,000.
- Resolution source is Binance, not another exchange and not a consolidated BTC index.
- The relevant pair is BTC/USDT specifically.
- The relevant data field is the candle Close, not open/high/low or any trade during the minute.
- Precision is determined by the decimals shown by the source.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The page does not itself provide the future resolution value, only the method.
- The phrase "12:00 in the ET timezone" should map to 16:00 UTC on April 17 given current DST, but that conversion still needs to be applied carefully by the analyst.
- The page does not clarify edge handling beyond the quoted rules, so operational access to Binance data at resolution time still matters.

## Why this source may matter

This is the governing source for contract interpretation. It defines the exact win condition and creates the main risk-manager point: apparent comfort from BTC trading above 72k now can still fail if the precise Binance 1-minute close at the specified time prints 72,000 or lower.

## Possible impact on the question

This source raises the importance of timing risk, exchange-specific print risk, and strict multi-condition logic. A bullish broad-Bitcoin view is not sufficient by itself; the thesis must also survive the precise timestamp and exchange/pair constraints.

## Reliability notes

Polymarket is the authoritative source for this contract's resolution language, so it is primary for market mechanics. Reliability for underlying price truth is indirect because the ultimate numeric observation will come from Binance at resolution time.