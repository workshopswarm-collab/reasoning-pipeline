---
type: source_note
case_key: case-20260415-1a345042
dispatch_id: dispatch-case-20260415-1a345042-20260415T223206Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: BTC/USDT Binance price context for Apr 21 noon ET threshold market
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-21 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Binance API ticker and daily klines
source_type: exchange market data / primary contextual
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=30
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1a345042/researcher-analyses/2026-04-15/dispatch-case-20260415-1a345042-20260415T223206Z/personas/base-rate.md]
tags: [binance, btcusdt, price-history, source-note]
---

# Summary

Binance direct market data shows BTC/USDT trading around 75,002 on 2026-04-15, already materially above the 72,000 threshold for the Apr 21 noon ET contract. Recent daily closes have mostly been near or above the threshold, with several closes above 72,000 in the last week.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price `75002.22000000` on fetch.
- Daily klines for the most recent stretch show:
  - 2026-04-10 close 72,962.70
  - 2026-04-11 close 73,043.16
  - 2026-04-12 close 70,740.98
  - 2026-04-13 close 74,417.99
  - 2026-04-14 close 74,131.55
  - 2026-04-15 current/day close snapshot 75,002.22 at fetch time
- In the last 9 daily closes through Apr 15, 6 were above 72,000.
- Recent realized range is wide enough that a 4-5% drawdown over six days is plausible, so being above the level today does not settle the contract.

## Evidence directly stated by source

- Current BTC/USDT price on Binance.
- Recent Binance daily open/high/low/close series.

## What is uncertain

- The contract resolves on the 1-minute candle closing price at exactly 12:00 ET on Apr 21, not on any daily close.
- Daily klines are only a contextual proxy for path/level persistence; they do not directly answer the exact settlement minute.
- Intraday volatility between now and Apr 21 could still push price below 72,000 at the relevant minute.

## Why this source may matter

This is the most relevant contextual source because the market explicitly settles to Binance BTC/USDT, so Binance price behavior is the best outside-view anchor for whether a 72,000 threshold six days out is structurally likely.

## Possible impact on the question

The source supports a high but not near-certain probability of Yes: BTC is currently several thousand dollars above the threshold and recent closes have mostly remained above it, but the margin is not so large that a normal crypto downswing can be ignored.

## Reliability notes

- Strong source for price context because it is Binance directly, the same venue named in the contract.
- Not the exact resolution surface because settlement depends on the Binance web candle close at 12:00 ET on Apr 21 rather than the API endpoints captured here.
- Suitable as primary contextual evidence, not by itself as settlement proof.