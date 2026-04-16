---
type: source_note
case_key: case-20260415-7253c25f
dispatch_id: dispatch-case-20260415-7253c25f-20260415T220737Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-21 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT live/API plus Polymarket rules page
source_type: primary+market-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
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
downstream_uses: []
tags: [binance, polymarket, resolution-source, market-context]
---

# Summary
Binance is the governing settlement surface for the contract, and live Binance API data on 2026-04-15 shows BTC/USDT trading above the 72,000 threshold with recent daily closes mostly around or above that line. Polymarket currently prices the April 21 >72k outcome around 80-81%.

## Key facts extracted
- Binance spot API returned BTCUSDT last price of 75,074.83 on 2026-04-15.
- Recent daily Binance closes/highs/lows from the last 10 daily candles show BTC has spent substantial recent time above 72,000.
- The Polymarket rules page explicitly says settlement uses the Binance BTC/USDT 1-minute candle at 12:00 ET on Apr 21, using the final Close price.
- The Polymarket market page currently shows the 72,000 outcome around 80-81%.

## Evidence directly stated by source
- Polymarket directly states the market resolves Yes if the Binance BTC/USDT 12:00 ET one-minute candle on the specified date has a final close above 72,000.
- Binance directly states the current spot price and provides historical candles for BTCUSDT.

## What is uncertain
- The authoritative settlement value is the exact 12:00 ET one-minute candle close on Apr 21, not today's spot price or daily close.
- The Polymarket page does not itself prove what BTC will be on Apr 21; it only provides current market pricing and rules.
- Direct browsing access to the Binance chart UI was limited, so the API was used as the direct Binance surface for current and recent prices.

## Why this source may matter
This source pair is enough to anchor both the contract mechanics and the near-term price baseline. For a date-specific crypto threshold market, those are the two highest-value direct inputs.

## Possible impact on the question
Because BTC is already trading materially above 72,000 with several recent daily closes above that level, the base state supports Yes. The remaining question is not whether 72,000 is currently reachable, but whether BTC can stay above that level through a specific intraday minute six days out.

## Reliability notes
- Binance is the governing source of truth for settlement, so source-of-truth quality is high.
- Binance API data is direct and machine-readable, which reduces transcription risk.
- Polymarket market text is useful for current implied probability and explicit rule wording, but it is not itself an independent truth source on future BTC price.
- Evidence independence is moderate: rules and price baseline come from different surfaces, but both are still tied to the same market ecosystem.
- Recent Binance context: 2026-04-11 close 73,043.16 high 73,790.00 low 72,513.09; 2026-04-12 close 70,740.98 high 73,137.24 low 70,505.88; 2026-04-13 close 74,417.99 high 74,900.00 low 70,566.99; 2026-04-14 close 74,131.55 high 76,038.00 low 73,795.47; 2026-04-15 close 75,074.83 high 75,281.00 low 73,514.00
