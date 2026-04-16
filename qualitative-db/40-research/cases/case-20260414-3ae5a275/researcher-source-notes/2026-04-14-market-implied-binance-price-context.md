---
type: source_note
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-14
source_name: Binance public API BTCUSDT ticker and daily klines
source_type: exchange market data / primary contextual source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3ae5a275/researcher-analyses/2026-04-14/dispatch-case-20260414-3ae5a275-20260414T202946Z/personas/market-implied.md]
tags: [binance, btcusdt, spot, price-context]
---

# Summary

Binance spot data showed BTC/USDT at 74,258.65 on April 14, materially above the 70,000 threshold. The recent 14-day daily series shows BTC closing above 70,000 on 8 of the last 9 completed daily candles before the run, with only one recent close slightly above 70k risk-tested down to roughly 70.5k intraday on April 11 and a stronger rebound afterward.

## Key facts extracted

- Spot ticker at check time: BTCUSDT 74,258.65.
- Recent daily closes from Binance klines:
  - Apr 6 close: 71,924.22
  - Apr 7 close: 71,069.93
  - Apr 8 close: 71,787.97
  - Apr 9 close: 72,962.70
  - Apr 10 close: 73,043.16
  - Apr 11 close: 70,740.98
  - Apr 12 close: 74,417.99
- Recent intraday low on Apr 11: 70,505.88, still above 70k by only a modest margin.
- Latest daily candle in the pulled set (ongoing day context) had traded as high as 76,038.00 and low as 73,795.47 so far.

## Evidence directly stated by source

- The exchange and pair that matter for settlement are currently trading comfortably above the threshold.
- Recent realized trading has already spent multiple days above the strike.
- There is still nontrivial volatility: a roughly 4.7k daily range appeared on Apr 12 (70,566.99 to 74,900.00).

## What is uncertain

- Daily candles do not directly settle the contract; only the exact 12:00 ET 1-minute candle on Apr 20 does.
- This source does not independently explain why BTC is in this regime; it only confirms the current and recent price context on the settlement venue.

## Why this source may matter

This is the cleanest direct evidence that the market’s 85.5% Yes price is not arbitrary: the relevant exchange is already trading more than 6% above the threshold with several recent daily closes above it.

## Possible impact on the question

Supports a high Yes probability, but not near-certainty. The contract still fails if BTC mean-reverts below 70k by the specific minute on Apr 20.

## Reliability notes

High reliability for current and recent Binance price context because this is first-party exchange API data. Independence versus the settlement source is low by design, since the settlement source is also Binance.