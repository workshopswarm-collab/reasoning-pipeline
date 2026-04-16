---
type: source_note
case_key: case-20260416-bac9c8f2
dispatch_id: dispatch-case-20260416-bac9c8f2-20260416T033803Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-bac9c8f2 | risk-manager
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API and Polymarket market rules
source_type: primary_market_source_and_contract_surface
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-bac9c8f2/researcher-analyses/2026-04-16/dispatch-case-20260416-bac9c8f2-20260416T033803Z/personas/risk-manager.md]
tags: [source-note, binance, polymarket, resolution]
---

# Summary

This note captures the direct contract mechanics and a direct Binance spot check near the time of analysis. It matters because this market is narrow, date-specific, and resolves on one exact 1-minute Binance BTC/USDT candle close at 12:00 ET on Apr. 17.

## Key facts extracted

- Polymarket rules say the market resolves YES only if the Binance BTC/USDT 1-minute candle for **12:00 ET (noon)** on Apr. 17 has a final **Close** strictly higher than **74,000**.
- The relevant source-of-truth surface is Binance BTC/USDT, not other exchanges and not other BTC pairs.
- Price precision is determined by Binance source precision.
- At analysis time (2026-04-15 23:43 EDT / 2026-04-16 03:43 UTC), Binance API returned spot BTCUSDT price **74,983.50**.
- Recent Binance 1-minute klines around analysis time showed BTCUSDT trading in roughly the **74,976-75,032** band in the sampled minutes.
- CoinGecko spot check returned **$75,013**, broadly consistent with Binance and useful as a contextual cross-check rather than settlement authority.

## Evidence directly stated by source

From Polymarket rules:
- YES if Binance 1-minute candle for BTC/USDT at 12:00 ET on the specified date has final Close price higher than 74,000.
- Otherwise NO.
- Resolution source is Binance BTC/USDT with 1m candles.

From Binance API sample:
- `ticker/price`: BTCUSDT `74983.50000000`
- Recent 1-minute kline closes sampled near analysis time: `74982.01`, `74999.98`, `75001.18`, `74976.15`, `74983.50`

## What is uncertain

- This source note does not establish where BTCUSDT will be at **Apr. 17 12:00 ET**; it only anchors current spot and contract mechanics.
- It does not resolve whether any late volatility, macro catalyst, or exchange-specific dislocation could move BTC below 74,000 at the precise settlement minute.
- Binance UI wording in Polymarket rules references the exchange front-end, while this note verified using Binance public API endpoints; that is directionally appropriate but not identical to the exact UI surface named in the contract.

## Why this source may matter

For a narrow timing market, the biggest avoidable errors are contract-mechanics mistakes and overconfidence from using the wrong market or wrong timestamp. This source gives the governing resolution condition and shows current spot is only modestly above the threshold, leaving real path risk over the next ~12 hours.

## Possible impact on the question

This source supports a leaning to YES because current Binance spot is above 74,000 by roughly $984 and nearby 1-minute closes are also above 74,000. But it also supports a risk-manager caution: the edge is not huge for BTC over a sub-day window, so one adverse move by the exact noon ET candle could still flip the outcome.

## Reliability notes

- Polymarket rule text is the governing contract surface for interpreting resolution.
- Binance API is highly relevant and close to the source-of-truth, but final settlement should still follow the exact Binance 1-minute candle close available on the designated surface at the designated time.
- CoinGecko is only a contextual consistency check and not a settlement source.