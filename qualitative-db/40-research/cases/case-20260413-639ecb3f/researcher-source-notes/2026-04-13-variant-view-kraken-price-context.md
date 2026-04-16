---
type: source_note
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: protocols
entity: ethereum
topic: ethereum spot price context
question: Will Ethereum reach $2,400 April 13-19?
date_created: 2026-04-13
source_name: Kraken public ticker and daily OHLC API
source_type: exchange API / contextual market data
source_url: https://api.kraken.com/0/public/Ticker?pair=ETHUSD
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [variant-view.md]
tags: [kraken, spot-price, volatility, context]
---

# Summary

Kraken public market data showed ETH already trading around $2,358 on Apr 13, with same-day high around $2,364.7 and recent daily highs rising from the low-$2200s into the mid-$2300s. Contextually, the remaining move needed to touch $2,400 was small, but not trivial.

## Key facts extracted

- Kraken ticker at review time showed ETH/USD last trade around 2358.39.
- Kraken daily OHLC for Apr 13 showed open about 2191.74, high about 2364.74, low about 2175.00, close/latest around 2362.99 at retrieval time.
- Recent daily highs from the API showed:
  - Apr 8 high about 2246.17
  - Apr 9 high about 2258.47
  - Apr 10 high about 2329.85
  - Apr 11 high about 2288.99
  - Apr 12/13 session high about 2364.74
- From ~2358 spot, the contract only needed roughly another $42 of upside, about 1.8%.

## Evidence directly stated by source

- Current ETH/USD spot price on Kraken.
- Current and recent daily high/low/open/close values from Kraken OHLC.

## What is uncertain

- Kraken is not the governing settlement venue; Binance ETH/USDT is.
- Daily OHLC does not show intraday microstructure or whether momentum persists through the week.
- Crypto trades continuously, so these values can age quickly.

## Why this source may matter

It gives an independent contextual check against the market-implied thesis. If ETH is already within ~2% of the threshold on day one of a seven-day touched-high contract, the market’s high probability has a mechanical basis. It also helps frame the strongest variant view: the contract may still be somewhat overconfident because near-threshold starts can reverse sharply in crypto.

## Possible impact on the question

This source supports a Yes-leaning baseline because the threshold is nearby and the contract counts any brief touch. At the same time, it leaves room for a cautious under-market variant because one failed breakout/reversal can strand price below $2,400 all week.

## Reliability notes

Kraken API is credible and recent as contextual price evidence, but it is not the official resolution source. Best used as an independent market-condition cross-check rather than as settlement evidence.