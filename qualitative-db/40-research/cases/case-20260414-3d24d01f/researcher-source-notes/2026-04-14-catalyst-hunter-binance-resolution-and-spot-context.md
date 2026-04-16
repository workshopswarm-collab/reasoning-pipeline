---
type: source_note
case_key: case-20260414-3d24d01f
dispatch_id: dispatch-case-20260414-3d24d01f-20260414T184328Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-3d24d01f | catalyst-hunter
question: Will the price of Bitcoin be above $70,000 on April 19?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance spot API + Polymarket rules page
source_type: exchange API and market rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260414-3d24d01f/researcher-analyses/2026-04-14/dispatch-case-20260414-3d24d01f-20260414T184328Z/personas/catalyst-hunter.md
tags: [binance, resolution-source, price-context, btc]
---

# Summary

This source note captures the governing settlement source and the immediate spot-price context for the April 19 BTC > 70k market.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 19, using the final Close price.
- Binance API documentation confirms `GET /api/v3/klines` returns 1-minute candlesticks with a close field and supports timezone interpretation for kline intervals, while start/end times remain UTC.
- On 2026-04-14 during this run, Binance spot BTCUSDT traded around 74.0k-74.3k.
- Binance 24h stats showed a session high of 76,038 and low of 72,298.93, implying BTC had recently traded materially above the 70k threshold.
- Recent daily candles for the last 7 sessions all closed above 70k, with closes ranging roughly 70.7k to 74.4k.

## Evidence directly stated by source

- Binance ticker price endpoint returned BTCUSDT at 74,022.72 during the final verification pass.
- Binance 24h ticker returned lastPrice 74,022.72, high 76,038.00, low 72,298.93.
- Binance daily klines for the prior 7 daily candles all closed above 70,000.
- Polymarket rules explicitly define Binance BTC/USDT, 1m candle, 12:00 ET, and final Close as the governing source of truth.

## What is uncertain

- The exact April 19 noon ET close cannot be known yet.
- Weekend macro or crypto-specific catalysts in the next ~4.9 days could still move BTC below 70k by the resolution minute.
- Binance chart UI presentation could differ cosmetically from API output, though both should reflect the same underlying market data.

## Why this source may matter

This is the highest-value direct evidence because the contract is narrow and date-specific. It establishes both the precise settlement mechanics and whether BTC currently has meaningful cushion versus the 70k threshold.

## Possible impact on the question

The combination of exact settlement mechanics and current spot context supports a high Yes probability, but not certainty: all material conditions still require Binance BTC/USDT to print a final 12:00 ET 1-minute close above 70,000 on April 19.

## Reliability notes

- Binance is the named resolution source, so source-of-truth authority is high for settlement.
- The Polymarket page is authoritative for contract wording.
- These are not independent in the sense of causal market forecasting; they are independent enough for mechanics verification but not for broader catalyst analysis.
