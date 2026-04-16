---
type: source_note
case_key: case-20260415-31d67ba1
dispatch_id: dispatch-case-20260415-31d67ba1-20260415T185542Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and Binance BTCUSDT API snapshots
source_type: primary_market_and_resolution_source
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, contract-interpretation, btc]
---

# Summary

This note captures the market's explicit resolution mechanics and a direct price snapshot from Binance, the governing source of truth.

## Key facts extracted

- The Polymarket contract resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-17 has a final Close price strictly above 70,000.
- The market is specifically tied to Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the source.
- As of 2026-04-15 around 14:57 ET, Binance spot BTCUSDT was about 74,374 and Binance 5-minute average price was about 74,360.
- Recent 1-minute klines fetched from Binance were all around 74.33k-74.36k.

## Evidence directly stated by source

- Polymarket rules explicitly say the relevant source is Binance with 1m candles selected and that the relevant datapoint is the 12:00 ET candle close on the date in the title.
- Binance ticker API returned BTCUSDT price 74374.14.
- Binance avgPrice API returned 74359.72902815 over the previous 5 minutes.

## What is uncertain

- The fetched Binance API snapshots are from April 15, not the resolution minute itself.
- The market page accessible by web fetch is not the actual Binance chart UI used by many traders, so final settlement still depends on the live Binance source at resolution time.
- Intraday volatility between now and noon ET on April 17 could still move BTC below 70,000 for the relevant minute close.

## Why this source may matter

This is the closest thing to a governing primary source set: it defines exactly what counts and provides the actual exchange/pair reference level the contract cares about.

## Possible impact on the question

Because current Binance BTCUSDT is roughly 6% above the 70,000 threshold with less than two days remaining, the contract currently leans toward Yes unless there is a material downside move before the exact noon ET resolution minute.

## Reliability notes

High for contract mechanics and current reference price because this combines the market's own written rules with Binance API data from the named exchange and pair. The main remaining risk is not source credibility but time-window sensitivity and exact resolution-minute behavior.
