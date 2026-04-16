---
type: source_note
case_key: case-20260416-33b4e3b5
dispatch_id: dispatch-case-20260416-33b4e3b5-20260416T021538Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-price-resolution
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 1-minute candle closing at 12:00 ET on 2026-04-19 be above 80?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance SOLUSDT API + Polymarket market rules page
source_type: primary-plus-resolution-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT ; https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1m&limit=5 ; https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-33b4e3b5/researcher-analyses/2026-04-16/dispatch-case-20260416-33b4e3b5-20260416T021538Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution-rules, source-note]
---

# Summary

This source note captures the direct price check and contract-mechanics check most relevant to the April 19 SOL > 80 market.

## Key facts extracted

- Polymarket rules state the market resolves from the **Binance SOL/USDT 1-minute candle at 12:00 ET (noon) on Apr 19, 2026**, using the final **Close** price.
- The rules explicitly say the source is Binance SOL/USDT with **1m** candles and that price precision follows the source.
- A direct Binance API spot-price query on 2026-04-16 returned **SOLUSDT = 84.91**.
- A direct Binance 1-minute kline query around the research time showed recent closes clustered around **84.76 to 84.94**, confirming spot trading was materially above the 80 threshold at the time of review.
- The queried kline timestamps converted cleanly to **2026-04-16 02:13–02:17 UTC**, which is **2026-04-15 22:13–22:17 ET**, confirming the date/time translation behavior needed for the noon-ET settlement interpretation.

## Evidence directly stated by source

- Polymarket directly states the resolution mechanics and governing source.
- Binance API directly states the live spot price and recent 1-minute candle values for SOLUSDT.

## What is uncertain

- None of these sources directly settle the April 19 noon ET close yet, because settlement is still in the future.
- The Binance API check is a present-state observation, not a forecast.
- Web fetch could not render the interactive Binance chart page itself, so the direct Binance evidence here comes from the public API endpoints rather than the front-end chart UI.

## Why this source may matter

This is the most important combined source set because it identifies both the exact contract mechanics and the current cushion versus the threshold. For a date-specific crypto price market, the key risk question is not whether SOL is currently above 80, but whether it stays above 80 exactly at the noon-ET settlement minute on Binance.

## Possible impact on the question

The source set supports a bullish baseline because current Binance price is already several dollars above 80. It also highlights the central risk-manager point: resolution depends on **one exact Binance minute close**, so even a broadly bullish SOL tape can still fail on short-horizon volatility, weekend moves, or exchange-specific prints.

## Reliability notes

- Binance API is a high-credibility direct source for current SOLUSDT pricing.
- Polymarket market page is a high-credibility direct source for contract wording.
- Independence is limited because the rule source and price source serve different functions rather than corroborating the same factual claim from separate institutions.
- For this market, that is acceptable because one source defines settlement mechanics and the other is the governing price venue.