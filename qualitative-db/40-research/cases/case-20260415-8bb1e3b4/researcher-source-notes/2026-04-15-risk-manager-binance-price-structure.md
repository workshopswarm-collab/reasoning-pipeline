---
type: source_note
case_key: case-20260415-8bb1e3b4
dispatch_id: dispatch-case-20260415-8bb1e3b4-20260415T150551Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-8bb1e3b4 | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT spot and recent klines
source_type: exchange-market-data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: current
stance: mildly-supportive
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8bb1e3b4/researcher-analyses/2026-04-15/dispatch-case-20260415-8bb1e3b4-20260415T150551Z/personas/risk-manager.md]
tags: [binance, btcusdt, price, volatility, recent-context]
---

# Summary

Current Binance BTC/USDT spot is materially above $70,000, but the relevant risk is not level alone; it is whether BTC remains above that threshold specifically for the April 20 12:00 ET one-minute close. Recent Binance daily data show BTC has traded both substantially below and substantially above $70,000 over the last two weeks, with enough realized volatility to keep a real but limited path-risk to the downside.

## Key facts extracted

- Current Binance BTC/USDT spot at check was about $73,985.70.
- 14-day Binance daily close range was about $66,901.99 to $74,417.99.
- 14-day high reached about $76,038.00.
- 14-day low reached about $65,712.12.
- Last five daily closes were approximately 73,043.16, 70,740.98, 74,417.99, 74,131.55, and 73,985.70.
- Recent one-minute candles around the check time were clustered near $74.0k-$74.2k, implying a cushion of roughly $4k above the contract strike.

## Evidence directly stated by source

- Binance ticker endpoint returned BTCUSDT near 73,985.7 during the research pass.
- Binance 1d kline data show BTC has already spent time both under and above $70k in the recent window.
- Binance 1m kline samples show short-horizon price movement can be tens of dollars per minute, but not evidence of current severe instability.

## What is uncertain

- Spot level four-plus days before resolution does not directly settle the noon April 20 candle.
- Daily bars hide intraday swings and event risk.
- Exchange-specific dislocations or weekend volatility could still matter before resolution.

## Why this source may matter

This is the closest direct factual basis for the current state of the underlying source of truth. It supports the bullish baseline because BTC is above the strike with visible cushion, but it also demonstrates that sub-$70k prints were not remote in the recent past.

## Possible impact on the question

The evidence supports a Yes lean, but less than near-certainty. A roughly $4k cushion with several days remaining argues for high probability, while recent realized volatility argues against treating 87%-88% as trivial or fully locked.

## Reliability notes

High credibility for current and historical Binance market data because Binance is also the contract's governing source. Independence is limited because the same source informs both prediction target and current-state evidence.