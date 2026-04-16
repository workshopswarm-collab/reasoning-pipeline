---
type: source_note
case_key: case-20260415-2ce6159e
dispatch_id: dispatch-case-20260415-2ce6159e-20260415T142913Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: spot-market-structure
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API BTCUSDT ticker, 24hr stats, klines, and exchangeInfo
source_type: exchange-api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2ce6159e/researcher-analyses/2026-04-15/dispatch-case-20260415-2ce6159e-20260415T142913Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, pricing, resolution-source, direct-evidence]
---

# Summary

Direct Binance market data is the governing source family for this contract and currently shows BTC/USDT well above 72,000 with a large cushion into the final 24 hours.

## Key facts extracted

- Binance spot ticker returned BTCUSDT at 74,326.67 around the research time.
- Binance 24hr ticker returned lastPrice 74,291.57, high 75,746.04, low 73,514.00, and open 75,609.14.
- Recent one-minute klines show intraday trading around 74.3k-74.4k, not near the 72k threshold.
- Binance exchangeInfo for BTCUSDT shows symbol status `TRADING` and price tick size `0.01`, relevant for contract precision and market functioning.
- Daily klines for the last week show closes mostly in the 70.7k-74.4k range, with April 12 high touching 74,900 and April 13 high 76,038.

## Evidence directly stated by source

- The contract-relevant market exists on Binance as BTCUSDT spot and is actively trading.
- The spot price and 24h low are both above 72,000 at the time checked.
- Price precision appears to be cents on the exchange API (`tickSize` 0.01), consistent with the market rule that precision follows the source.

## What is uncertain

- This source does not itself say where the 12:00 ET candle tomorrow will close.
- The contract text references the Binance web chart UI, while this note relies on Binance API endpoints as a close proxy for the same underlying market data.
- A sharp macro or crypto-specific selloff in the next ~21.5 hours could still push price below 72,000 by the resolution minute.

## Why this source may matter

This is the closest thing to a primary source short of observing the exact resolution candle itself. It directly informs both the current cushion above the strike and the operational reliability of the settlement venue.

## Possible impact on the question

Because BTC/USDT is already ~2.3k above the strike and even the checked 24h low stayed above 72k, the default lean is Yes unless a meaningful negative catalyst arrives before the noon ET settlement window.

## Reliability notes

Very high relevance and recency. Evidence is direct for current price state and settlement mechanics, but indirect for tomorrow's exact noon close.