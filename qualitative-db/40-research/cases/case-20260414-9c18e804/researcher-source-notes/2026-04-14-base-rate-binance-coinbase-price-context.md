---
type: source_note
case_key: case-20260414-9c18e804
dispatch_id: dispatch-case-20260414-9c18e804-20260414T135145Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: recent bitcoin price path
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Binance BTCUSDT daily klines and Coinbase BTC-USD daily candles
source_type: exchange market-data context
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10 ; https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=86400
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: base-rate
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-9c18e804/researcher-analyses/2026-04-14/dispatch-case-20260414-9c18e804-20260414T135145Z/personas/base-rate.md]
tags: [binance, coinbase, btc, price-context, source-note]
---

# Summary

Recent exchange data shows BTC has already traded close to the threshold but has not yet clearly broken above 76k in the checked data.

## Key facts extracted

- Binance daily data for 2026-04-13 showed high about 75,397 and close about 75,340.
- Binance daily data for 2026-04-12 showed high about 74,900.
- Coinbase daily candles showed 2026-04-13 high about 75,489 and 2026-04-12 high about 74,936.9.
- Earlier in mid-March 2026, Coinbase daily candles in the returned history included a day with high about 76,022.6, showing 76k is not a historically exotic print for BTC in this regime.
- Over the recent 10-day window BTC moved from high-60ks to mid-75ks, indicating strong upside momentum but also that 76k had not yet obviously been exceeded in the current Apr 13-19 window at time checked.

## Evidence directly stated by source

- BTC is trading within roughly 1% of the 76k threshold.
- Independent exchange data (Binance and Coinbase) agree closely on the recent price range.

## What is uncertain

- The fetched data here are daily candles, not the exact Binance 1-minute highs that govern resolution.
- Daily highs can slightly understate or smooth the precise intraday touch path relative to the governing source.

## Why this source may matter

This is the main contextual evidence for how demanding the threshold actually is from current levels. Being within about 1% of target with nearly six days left is structurally favorable for a touch-style contract.

## Possible impact on the question

Supports a high Yes probability, but not certainty: near-threshold status plus remaining time makes 76k likely, yet failure is still plausible if momentum stalls and BTC mean-reverts.

## Reliability notes

High reliability for broad price context. Medium relevance to exact settlement because final resolution is based only on Binance BTC/USDT 1-minute highs.