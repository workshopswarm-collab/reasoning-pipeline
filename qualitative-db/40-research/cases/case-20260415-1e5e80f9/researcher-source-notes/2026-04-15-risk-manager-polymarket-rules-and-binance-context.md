---
type: source_note
case_key: case-20260415-1e5e80f9
dispatch_id: dispatch-case-20260415-1e5e80f9-20260415T080017Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 16 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance public market data API check
source_type: primary+contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1e5e80f9/researcher-analyses/2026-04-15/dispatch-case-20260415-1e5e80f9-20260415T080017Z/personas/risk-manager.md]
tags: [polymarket, binance, resolution-rules, btc]
---

# Summary

This source note records the governing contract mechanics from Polymarket and a direct Binance market-data context check relevant to tail-risk assessment.

## Key facts extracted

- Polymarket states the market resolves "Yes" if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final close above 72,000.
- Resolution is specifically tied to Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by Binance source precision.
- Polymarket displayed the 72,000 line at roughly 83% at fetch time, consistent with assignment current_price 0.825.
- Binance public API check on 2026-04-15 around 08:02 UTC showed BTCUSDT spot around 73,722.51, already above the strike by roughly $1.7k the day before resolution.
- Recent 1-minute Binance klines fetched successfully, confirming Binance market-data surfaces were live and queryable at check time.

## Evidence directly stated by source

From Polymarket rules text:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

From Binance API outputs checked directly:
- ticker price: 73722.51000000
- recent klines endpoint returned normal 1-minute BTCUSDT candles, indicating accessible direct exchange reference data.

## What is uncertain

- The API spot price checked was not the resolution candle itself; it is contextual evidence only.
- The exact noon ET candle close can still differ materially from the current spot price over the remaining time window.
- Binance website chart rendering and API data can differ slightly in presentation, though both point to the same exchange reference surface.
- There is always some residual operational or timestamp interpretation risk around the exact noon ET candle mapping.

## Why this source may matter

It establishes the governing source of truth and the exact multi-condition mechanics: correct date, exact time window, exact venue, exact pair, exact field (close), and threshold comparison (> 72,000).

## Possible impact on the question

The note supports a high base probability for Yes because BTC/USDT was already comfortably above 72,000 during the pre-resolution period, but it also highlights the key residual failure mode: a sub-72,000 Binance 12:00 ET closing print on April 16 despite being above the level beforehand.

## Reliability notes

- Polymarket rule text is the primary contract-mechanics source and should govern interpretation.
- Binance public API is a strong direct contextual source for live exchange pricing, but not itself the full settlement statement unless it corresponds to the exact resolution candle.
- Evidence independence is moderate: both sources reference the same underlying market mechanism, but they serve different roles (rules vs live price context).
- Main remaining risk is not source credibility but path/timing risk between now and the resolution candle.