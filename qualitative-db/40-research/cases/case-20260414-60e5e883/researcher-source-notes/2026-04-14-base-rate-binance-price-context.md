---
type: source_note
case_key: case-20260414-60e5e883
dispatch_id: dispatch-case-20260414-60e5e883-20260414T190542Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: reliability
date_created: 2026-04-14
source_name: Binance BTCUSDT spot klines (daily, hourly, and noon-ET 1m checks)
source_type: exchange market data / primary contextual source
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m
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
downstream_uses: [qualitative-db/40-research/cases/case-20260414-60e5e883/researcher-analyses/2026-04-14/dispatch-case-20260414-60e5e883-20260414T190542Z/personas/base-rate.md]
tags: [binance, btcusdt, spot-price, base-rate, noon-et-check]
---

# Summary

Direct Binance price data show BTC/USDT is already materially above 70,000 with only a few days left until resolution. The relevant outside-view question is therefore not whether Bitcoin can rally to 70k, but whether it can suffer a sufficiently sharp drawdown by noon ET on April 17.

## Key facts extracted

- Daily closes from April 7 through April 14 were all above 70,000, with closes ranging roughly from 70,741 to 74,418.
- The last 96 hourly closes before collection had zero hourly closes below 70,000.
- The minimum hourly low in that 96-hour sample was 70,505.88, still above the contract threshold.
- Direct checks of the 16:00 UTC candle (12:00 ET during EDT) show recent noon-ET 1-minute closes of about 70,860 on April 12, 71,902.91 on April 13, and 75,356.48 on April 14.
- At collection time on April 14, the spot region was around 74k to 75k, leaving a buffer of roughly 6% to 8% above the 70k threshold.

## Evidence directly stated by source

- Binance API kline outputs provide timestamped open/high/low/close data for BTC/USDT at 1-minute, 1-hour, and 1-day intervals.
- The noon-ET mapping corresponds to 16:00 UTC on these dates because April 17 falls during U.S. daylight saving time.

## What is uncertain

- Exchange API observations are a current snapshot and do not directly answer future price path risk.
- A sharp macro or crypto-specific shock could still move BTC/USDT below 70,000 before resolution.
- This note does not independently model volatility distributions; it establishes the empirical starting point and recent path stability.

## Why this source may matter

It is the direct contextual evidence for current distance from threshold, recent realized stability above 70,000, and correct noon-ET-to-UTC time mapping. Those are central for a short-horizon base-rate estimate.

## Possible impact on the question

Because BTC/USDT has remained above 70,000 across recent daily closes, hourly closes, and recent noon-ET one-minute checks, the base rate favors Yes unless a rare but plausible multi-day drawdown breaks that cushion before Friday noon ET.

## Reliability notes

High authority for exchange-specific price context because the contract settles on Binance BTC/USDT itself. Evidence independence is still only moderate because both the contextual source and settlement source ultimately hinge on Binance data, but this is appropriate for an exchange-specific contract.
