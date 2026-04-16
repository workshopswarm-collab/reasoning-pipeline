---
type: source_note
case_key: case-20260415-6580bcd8
dispatch_id: dispatch-case-20260415-6580bcd8-20260415T081158Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-6580bcd8 | risk-manager
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 17, 2026 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API and Binance-linked market rules
source_type: primary_and_resolution_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-6580bcd8/researcher-analyses/2026-04-15/dispatch-case-20260415-6580bcd8-20260415T081158Z/personas/risk-manager.md]
tags: [binance, btcusdt, contract-mechanics, date-sensitive]
---

# Summary

Binance is the governing source of truth for settlement. On 2026-04-15 around 08:14 UTC, Binance spot endpoints showed BTCUSDT around 73.83k, already above the 72k threshold by roughly 1.8k. Binance kline data for the same period also confirmed live 1-minute candle closes in the 73.7k-73.8k range. Polymarket's rules page matches that settlement logic: the relevant condition is the final close of the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 17, not any other exchange or a daily close.

## Key facts extracted

- Binance ticker/price endpoint returned BTCUSDT price `73830.09000000` on 2026-04-15.
- Binance 24hr ticker endpoint returned open price `74533.71000000`, high `76038.00000000`, low `73514.00000000`, and last price `73830.09000000`.
- Binance kline endpoint for 2026-04-15 08:00-08:15 UTC returned 1-minute candle closes consistently above 73.6k in the sample checked.
- Polymarket rule text states the market resolves Yes only if the Binance BTC/USDT 1-minute candle for `12:00` in ET on April 17 has final close price higher than 72,000.
- The contract is source-specific and time-specific: Binance BTC/USDT only; 1-minute candle close only; noon ET only.

## Evidence directly stated by source

- Binance direct API surfaces report current BTCUSDT spot prices and 1-minute klines.
- Polymarket directly states Binance is the resolution source and specifies the relevant candle and threshold.

## What is uncertain

- This source set does not itself forecast where BTC will trade at noon ET on April 17; it only establishes current price level and precise resolution mechanics.
- The rule text visible on Polymarket does not independently verify whether Binance's website candle label uses local browser timezone or ET-normalized display, though the contract explicitly says `12:00 in the ET timezone`.
- A current spot price above 72k leaves room for a >2% downside move before resolution.

## Why this source may matter

This is the highest-quality source set for the case because it covers both the direct settlement mechanism and the current reference price relative to the threshold.

## Possible impact on the question

The fact that BTCUSDT is already materially above 72k supports a Yes lean, but the contract remains exposed to short-horizon volatility and exact-timestamp risk. The contract mechanics reduce ambiguity about what counts, but they also make path risk concentrated into one minute and one venue.

## Reliability notes

- Binance API is authoritative for Binance-reported market data and is meaningfully stronger than secondary price aggregators for this contract.
- Polymarket page is authoritative for the market's written rules but not for the eventual price observation itself.
- Independence is only medium because both items relate to the same exchange-centric mechanism, so additional contextual verification is still useful even if the direct source-of-truth is clear.
