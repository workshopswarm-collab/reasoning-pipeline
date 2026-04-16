---
type: source_note
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-15 be above 72000?
driver: reliability
date_created: 2026-04-13
source_name: Binance API with cross-exchange spot checks (CoinGecko, Coinbase)
source_type: exchange/API data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-395c5631/researcher-analyses/2026-04-13/dispatch-case-20260413-395c5631-20260413T221534Z/personas/base-rate.md]
tags: [binance, coinbase, coingecko, btc, source-note]
---

# Summary

This note captures the direct price-state evidence near the time of analysis and a simple independent cross-check that Binance was not showing an obvious outlier price.

## Key facts extracted

- Binance BTCUSDT spot was about **73,823.14** at check time.
- CoinGecko showed bitcoin around **73,767 USD**.
- Coinbase BTC-USD ticker showed about **73,849.57 USD**.
- The three sources were closely aligned, suggesting no large exchange-specific dislocation at the time of the check.
- Recent Binance daily candles showed closes of roughly 71,070 (Apr 8), 71,788 (Apr 9), 72,963 (Apr 10), 73,043 (Apr 11), 70,741 (Apr 12), and 73,809 partial/current for Apr 13.
- Recent 12:00 ET / 16:00 UTC hourly closes were above 72k on Apr 9, Apr 10, Apr 11, and Apr 13, but below on Apr 12.
- Across the last 35 daily 12:00 ET observations available from recent hourly data, only **6/35 (~17%)** were above 72k, showing the threshold has been unusual over a longer short-term reference window even though the last few days improved materially.

## Evidence directly stated by source

- Binance API directly reported the live BTCUSDT price and recent candles.
- Coinbase and CoinGecko directly reported contemporaneous BTC/USD prices.

## What is uncertain

- These checks do not directly settle the April 15 noon ET candle.
- The 35-day lookback is a narrow recent reference class, not a full historical cycle.
- Cross-exchange alignment now does not eliminate basis divergence at resolution minute.

## Why this source may matter

It provides direct, current evidence that BTC is already above the threshold and that Binance is not obviously detached from other major price references.

## Possible impact on the question

Being ~2.5% above the threshold with roughly 38 hours left substantially raises the chance of finishing above 72k versus a cold prior. But the recent path also shows BTC can dip back below 72k within a day, so the setup is favorable rather than locked.

## Reliability notes

High-value direct evidence for present market state because Binance is the governing source of truth. Cross-checking with Coinbase and CoinGecko modestly improves confidence that the observed level is not a Binance-only artifact.