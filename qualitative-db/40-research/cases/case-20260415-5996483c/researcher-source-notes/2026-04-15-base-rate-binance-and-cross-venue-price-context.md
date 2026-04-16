---
type: source_note
case_key: case-20260415-5996483c
dispatch_id: dispatch-case-20260415-5996483c-20260415T193222Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: BTC current level and recent daily range versus 70000 threshold
question: How far above 70000 is BTC currently trading, and how stable is that cushion?
driver: reliability
date_created: 2026-04-15
source_name: Binance API with CoinGecko and Coinbase spot cross-checks
source_type: exchange/API market data
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
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-5996483c/researcher-analyses/2026-04-15/dispatch-case-20260415-5996483c-20260415T193222Z/personas/base-rate.md
tags: [binance, coingecko, coinbase, btc, spot-price, cross-check]
---

# Summary

Recent market data shows BTC already trading well above 70,000 with a meaningful but not invulnerable cushion. Binance spot was about 74.9k, with CoinGecko and Coinbase closely aligned.

## Key facts extracted

- Binance BTCUSDT spot was approximately **74,887.18** at fetch time on 2026-04-15.
- CoinGecko reported Bitcoin around **74,857 USD**.
- Coinbase spot reported **74,896.295 USD**.
- Binance daily data for the prior roughly two weeks showed BTC below 70k in early April, then a breakout:
  - Apr 5 close around **68,853.66** after a high near **70,351.46**.
  - Apr 6 close around **71,924.22**.
  - Apr 8 close around **71,787.97**.
  - Apr 9 close around **72,962.70**.
  - Apr 10 close around **73,043.16**.
  - Apr 12 close around **74,417.99**.
  - Apr 13 close around **74,131.55**.
  - Apr 14 close around **74,887.18** with day high near **74,887.19** so far in the fetched series.

## Evidence directly stated by source

- BTC is currently trading roughly **6.9%** above the 70,000 threshold.
- Recent daily closes have generally held above 70,000 after the breakout, suggesting the threshold is not merely being grazed.

## What is uncertain

- These are spot and daily reference checks, not the resolving Apr 20 12:00 ET 1-minute close.
- BTC is volatile enough that a 6-7% cushion can still erode over several days.
- Cross-venue alignment today does not guarantee identical Binance close behavior at the resolution minute.

## Why this source may matter

This is the main contextual evidence for the outside view: when BTC is already several percent above a threshold and has recently held that regime for multiple daily closes, a close-above contract a few days out is usually favored.

## Possible impact on the question

The current cushion and recent regime support a high Yes probability, but the contract is still narrower than a simple "trade above at some point" framing because it requires one specific Binance minute close on Apr 20 noon ET.

## Reliability notes

High recency. Reasonably strong independence because Binance is primary for the contract while CoinGecko and Coinbase provide venue cross-checks. Still contextual rather than directly resolving.