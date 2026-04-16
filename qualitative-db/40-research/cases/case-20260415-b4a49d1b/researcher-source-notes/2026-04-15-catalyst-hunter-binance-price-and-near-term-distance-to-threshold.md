---
type: source_note
case_key: case-20260415-b4a49d1b
dispatch_id: dispatch-case-20260415-b4a49d1b-20260415T000939Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API spot price and recent candles
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: very-high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-b4a49d1b/researcher-analyses/2026-04-15/dispatch-case-20260415-b4a49d1b-20260415T000939Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, spot, threshold-distance, recent-range]
---

# Summary

This source provides direct exchange data from the same venue named in the contract and shows BTC already materially above the 70,000 threshold with only five days remaining.

## Key facts extracted

- Binance ticker price returned `74500.00000000` for BTCUSDT during the verification pass.
- Binance avgPrice returned about `74575.08327737`.
- Recent daily candles from Binance showed closes of 72,962.70 on Apr 10, 73,043.16 on Apr 11, 70,740.98 on Apr 12, 74,417.99 on Apr 13, and 74,131.55 on Apr 14.
- The lowest low in those ten daily candles was 67,732.01 on Apr 7, but BTC has closed above 70k for the last five completed daily candles in the sample.
- At the observed spot level, BTC had roughly a 6% buffer over the 70,000 contract threshold.

## Evidence directly stated by source

Direct API outputs captured during the run:
- ticker endpoint: `{"symbol":"BTCUSDT","price":"74500.00000000"}`
- avgPrice endpoint: `{"mins":5,"price":"74575.08327737","closeTime":1776212029165}`
- daily kline outputs showed recent open/high/low/close data including Apr 10-14 closes all above 70k.

## What is uncertain

- The contract resolves on a specific 12:00 ET one-minute close on Apr 20, not on today's spot or daily close.
- Intraday volatility between now and resolution can still produce a sub-70k noon print even if daily closes stay above 70k.
- Public API access confirms venue data but does not itself show the future settlement candle.

## Why this source may matter

This is the closest direct source to the eventual settlement venue and is the strongest direct evidence that the threshold is currently in-the-money with meaningful cushion.

## Possible impact on the question

Because the market is already trading around 74.5k on the named exchange, the main way the market resolves No is a fairly sharp downside move or a localized noon ET dip below 70k over the next five days. That narrows the catalyst search to downside repricing triggers rather than upside attainment.

## Reliability notes

High-value direct source because Binance is the named source of truth for settlement. The main limitation is temporal: it confirms current state, not the final Apr 20 noon candle.
