---
type: source_note
case_key: case-20260415-9c95ce3a
dispatch_id: dispatch-case-20260415-9c95ce3a-20260415T173129Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-9c95ce3a | catalyst-hunter
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page plus Binance spot/API reference
source_type: market rules plus exchange data
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium-high
recency: current
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, binance, contract, settlement, btc]
---

# Summary

This note captures the governing resolution mechanics and the current Binance BTC/USDT spot context relevant to the April 17 noon ET contract.

## Key facts extracted

- Polymarket states the market resolves `Yes` if the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on April 17 has a final `Close` price above 72,000.
- The rules specify Binance BTC/USDT, not another venue or pair, as the governing source of truth.
- On review of the market page, the April 17 `72,000` contract was trading around 82% / 83c.
- A direct Binance API check during this run returned BTCUSDT spot around 74,148 and recent 1-minute candles in the low 74,100s.
- A 48-hour hourly Binance API pull shows BTC/USDT trading above 72,000 throughout the recent window sampled, with intraday movement roughly in the high-73k to mid-74k area on April 15 UTC.

## Evidence directly stated by source

- The Polymarket page directly states the exact settlement test and source.
- Binance API directly states current BTCUSDT spot price and recent kline closes.

## What is uncertain

- The contract settles on one specific minute close at 12:00 ET on April 17, so current spot above 72,000 does not itself settle the market.
- Web-search snippets for Binance public pages showed slightly different live prices from the API pull, likely due to timing differences across refresh moments.
- The key unresolved risk is not the contract wording but a sharp adverse BTC move before the reference minute.

## Why this source may matter

This is the highest-value direct evidence because it defines both the settlement mechanics and the current distance from the strike.

## Possible impact on the question

If BTC remains in the current low-to-mid 74k area, the market resolves `Yes`. The relevant catalyst question is therefore whether any event in the next ~45 hours can produce a drop of a bit more than 2k by the exact Binance reference minute.

## Reliability notes

- Polymarket market-page rules are the operative contract context but still depend on Binance as the ultimate price source.
- Binance API is highly relevant contextual evidence for current pricing, though not itself a guarantee of the final noon ET minute close.
- Source-of-truth ambiguity looks low because the venue, pair, interval, and close field are all explicitly specified.