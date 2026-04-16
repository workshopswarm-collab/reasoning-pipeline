---
type: source_note
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-18
question: Will the price of Bitcoin be above $70,000 on April 18?
driver: reliability
date_created: 2026-04-14
source_name: Binance spot API and Coinbase spot API near assignment time
source_type: exchange_price_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8a0619b6/researcher-analyses/2026-04-14/dispatch-case-20260414-8a0619b6-20260414T194140Z/personas/risk-manager.md]
tags: [source-note, binance, coinbase, spot-price, verification]
---

# Summary

This note records a direct verification pass on live exchange pricing close to assignment time. It is not a forecast source, but it materially constrains the required move by showing BTC already trading well above the 70,000 threshold on the governing exchange.

## Key facts extracted

- Binance API at capture time returned BTCUSDT spot price 74,110.63.
- Binance 1-minute klines for the latest five minutes showed BTC/USDT trading in a narrow band around 74.1k-74.25k.
- Coinbase spot API at nearly the same time returned BTC-USD spot around 74,166.545.
- Cross-exchange proximity suggests the observed level was not a single obvious Binance outlier at capture time.

## Evidence directly stated by source

- Binance ticker endpoint: current BTCUSDT price = 74,110.63.
- Binance kline endpoint: recent minute closes all above 74,000 in the sampled window.
- Coinbase spot endpoint: BTC-USD around 74,166.545.

## What is uncertain

- This is a current-state snapshot, not a direct read of the eventual April 18 noon ET settlement minute.
- Coinbase is contextual rather than governing for resolution.
- No realized-volatility or options-implied distribution was retrieved in this run, so tail risk must be judged from the contract structure and spot cushion rather than a full volatility model.

## Why this source may matter

The market only needs BTC on Binance to remain above 70,000 at one specific minute on April 18. Starting from roughly 74.1k on April 14 means the No case needs about a 5.5% downside move by the relevant settlement minute, or a localized exchange-specific print below the threshold at that time.

## Possible impact on the question

This source supports a high Yes probability, but not certainty. It mainly narrows the practical failure modes to: meaningful BTC drawdown over four days, sharp intraday downside into the exact noon ET window, or Binance-specific pricing dislocation.

## Reliability notes

High-quality for current spot context because Binance is the governing exchange and Coinbase offers an independent cross-check. Limited as a forecast input because spot snapshots alone do not encode path risk or weekend volatility.