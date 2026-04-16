---
type: source_note
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: BTC/USDT vs 74000 noon ET close threshold on April 17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 74000 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance API ticker and 1-minute klines plus Polymarket rules page
source_type: primary_market_and_governing_source_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10 ; https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15/2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/personas/base-rate.md
tags: [binance, polymarket, source-note, threshold-market, close-market]
---

# Summary

This note captures the governing market mechanics and current Binance context for the April 17 BTC above 74000 noon ET close market.

## Key facts extracted

- Polymarket rules state the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr 17 has a final close strictly higher than 74000.
- The source of truth is specifically Binance BTC/USDT, not another venue or pair.
- Binance spot ticker at fetch time showed BTCUSDT at 74912.01.
- Recent Binance 1-minute klines fetched at the same time ranged roughly from 74905.70 to 75267.85 over the prior 10 minutes, with closes between 74912.01 and 75197.93.
- Those prints were around 2026-04-16 02:43-02:52 UTC, i.e. evening Apr 15 ET.
- Polymarket page showed the 74000 line trading around 66% at fetch time, while nearby ladder outcomes implied the market saw 74000 as a live but not overwhelming threshold.

## Evidence directly stated by source

- Rules page explicitly defines the relevant candle, timezone, trading pair, and strict-greater-than threshold test.
- Binance API directly states current BTCUSDT price and recent 1-minute open/high/low/close values.

## What is uncertain

- The fetched Binance klines are not the resolving candle; they only show current proximity one day before resolution.
- The noon ET Apr 17 close can still move materially before settlement.
- The Polymarket public page is context for pricing and contract wording, but actual settlement will depend on the specified Binance candle, not current Polymarket pricing.

## Why this source may matter

These are the most direct sources for both market mechanics and current threshold proximity. They establish that this is a narrow, date-specific, source-sensitive close market rather than a touch market.

## Possible impact on the question

Because BTC is already modestly above 74000 more than a day before the relevant noon ET close, the base rate is better than a coin flip, but not near certainty: a 24/7 volatile asset can easily move a few percent over that remaining window, and only one exact 1-minute close on Binance matters.

## Reliability notes

- Binance API is the strongest available governing-source proxy before settlement and highly relevant because the contract explicitly references Binance BTC/USDT candles.
- Polymarket rules page is authoritative for the contract wording but not for the eventual resolved value.
- Independence is only moderate because both direct sources are tied to the same market mechanism, so a separate contextual source is still useful for cross-checking current spot level.
