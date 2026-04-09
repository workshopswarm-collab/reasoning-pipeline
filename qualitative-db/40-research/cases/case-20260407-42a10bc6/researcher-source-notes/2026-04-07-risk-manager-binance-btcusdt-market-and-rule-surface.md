---
type: source_note
case_key: case-20260407-42a10bc6
dispatch_id: dispatch-case-20260407-42a10bc6-20260407T014927Z
analysis_date: 2026-04-07
persona: risk-manager
domain: crypto
subdomain: exchanges
entity: binance
topic: case-20260407-42a10bc6 | risk-manager
question: Will the price of Bitcoin be above $68,000 on April 7?
driver: operational-risk
date_created: 2026-04-07
source_name: Binance BTCUSDT API + Polymarket market rules
source_type: exchange API and market rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [bitcoin, binance]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-42a10bc6/researcher-analyses/2026-04-07/dispatch-case-20260407-42a10bc6-20260407T014927Z/personas/risk-manager.md]
tags: [btc, btcusdt, binance, market-rules, source-of-truth]
---

# Summary

This note captures the governing source-of-truth surface and current Binance spot context for the case.

## Key facts extracted

- Polymarket rules state resolution is based on the Binance BTC/USDT **1 minute candle for 12:00 ET (noon) on 2026-04-07**, specifically the candle's final **Close** price.
- The rule text explicitly says the source is the Binance BTC/USDT chart with **1m** and **Candles** selected.
- The market is about **Binance BTC/USDT**, not other exchanges or other BTC pairs.
- Current Binance spot context at research time:
  - `ticker/price`: BTCUSDT price = **68369.12**
  - `ticker/24hr`: lastPrice = **68370.00**, openPrice = **68840.56**, highPrice = **70351.46**, lowPrice = **68300.00**
  - `depth`: top-of-book around **68379.99 / 68380.00**
- The assigned market current_price of **0.845** implies an 84.5% market probability for Yes, but the public Polymarket event surface fetched during research showed the 68,000 line around **70%**, indicating either stale assignment metadata or a moved market.
- Time conversion check: **2026-04-07 12:00 ET = 2026-04-07 16:00 UTC**.

## Evidence directly stated by source

- Binance API directly states the current BTCUSDT spot price and 24h range.
- Polymarket rule text directly states the resolution mechanics and governing source.

## What is uncertain

- The final answer depends specifically on the **12:00 ET / 16:00 UTC** one-minute candle close, which had not yet occurred at research time.
- The exact public market probability may have moved from the assignment metadata after the run was generated.
- Binance chart UI and Binance API should generally align, but the contract names the chart/UI surface rather than the API endpoint.

## Why this source may matter

This is the most direct available evidence for both current price context and the market's settlement mechanics.

## Possible impact on the question

If BTC remains near current levels, Yes is plausible but not safe; the market requires a **single specific minute close** above 68,000, so intraday path risk and minute-level volatility still matter.

## Reliability notes

- Binance is the contract's explicit governing source of truth, so source-of-truth ambiguity is low.
- The main residual risk is operational/implementation risk: chart candle labeling, ET-to-UTC alignment, and reliance on a single minute close rather than a broader average.