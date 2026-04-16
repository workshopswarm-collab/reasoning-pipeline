---
type: source_note
case_key: case-20260415-572502e1
dispatch_id: dispatch-case-20260415-572502e1-20260415T124520Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on April 16, 2026?
driver: reliability
date_created: 2026-04-15
source_name: Binance public market data API spot check
source_type: primary-market-data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-572502e1/researcher-analyses/2026-04-15/dispatch-case-20260415-572502e1-20260415T124520Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, market-data, verification]
---

# Summary

This source is the closest available primary source to the contract's governing settlement feed. A spot check of Binance public API showed BTC/USDT trading well above 72,000 on April 15, giving the market roughly a 2.3k cushion one day before the noon ET settlement window.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price 74,344.93 at check time.
- Recent 1-minute Binance klines were clustering in the low-to-mid 74.3k area.
- The nearest live price margin versus the 72,000 threshold was about +2,344.93, or roughly +3.3%.
- The recent microstructure around the check showed active minute-by-minute trading but no sign of the threshold being near immediate danger.

## Evidence directly stated by source

- `{"symbol":"BTCUSDT","price":"74344.93000000"}` from Binance ticker endpoint.
- Recent 1-minute klines included closes around 74,364.79, 74,344.00, 74,309.71, 74,337.67, and 74,350.55.

## What is uncertain

- This is a spot check from April 15, not the actual April 16 12:00 ET settlement candle.
- One-day crypto volatility can erase a 3% cushion, so this is supportive but not dispositive.
- Public API output is close to but not exactly the same user-interface path named in the contract, though both are Binance BTC/USDT market data.

## Why this source may matter

For a short-horizon binary on a specific threshold, current distance from the strike is one of the most material facts. It also serves as the additional verification pass required by the extreme market pricing.

## Possible impact on the question

The current spot level supports a Yes lean and suggests the most likely repricing catalyst before resolution is not a scheduled economic release but an adverse risk-off move large enough to push BTC back below 72k by noon ET.

## Reliability notes

High credibility for current Binance market state. Independence versus Polymarket is high because the data comes from the exchange named in the contract, but it is still only a snapshot and not the eventual settlement print.