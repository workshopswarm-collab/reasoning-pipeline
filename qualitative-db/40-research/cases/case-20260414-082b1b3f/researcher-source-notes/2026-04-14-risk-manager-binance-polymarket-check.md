---
type: source_note
case_key: case-20260414-082b1b3f
dispatch_id: dispatch-case-20260414-082b1b3f-20260414T171716Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: trading-markets
entity: sol
topic: solana-above-80-on-april-17
question: Will the Binance SOL/USDT 1-minute candle labeled 12:00 ET on 2026-04-17 close above 80?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance API and Polymarket market page
source_type: primary+resolution-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: risk-manager
related_entities: [sol, solana]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-082b1b3f/researcher-analyses/2026-04-14/dispatch-case-20260414-082b1b3f-20260414T171716Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution-source, price-check, timing]
---

# Summary

Primary verification focused on the contract mechanics and the current Binance SOL/USDT level relevant to an April 17 noon ET threshold of 80. Polymarket's rules make Binance SOL/USDT the governing source of truth and specify the exact candle/time condition. Binance spot API outputs on 2026-04-14 show SOL trading materially above 80, around 85.25, with recent 1-minute candles clustered near 85.2 and daily closes over recent sessions mostly above 80.

## Key facts extracted

- Polymarket states the market resolves from the Binance SOL/USDT 1-minute candle for 12:00 ET on 2026-04-17, using the final close of that candle.
- The market is not about other exchanges or pairs; it is specifically Binance SOL/USDT.
- Binance ticker endpoint returned SOLUSDT price 85.25000000 at fetch time on 2026-04-14.
- Binance avgPrice endpoint returned 5-minute average 85.26572922.
- Recent Binance 1-minute klines around 2026-04-14 17:20 UTC (13:20 ET) showed closes between 85.23 and 85.30.
- Recent Binance daily klines show SOL closing above 80 on most recent sessions; the latest two daily closes before the run were 86.51 and 85.25.

## Evidence directly stated by source

- Direct contract mechanics from Polymarket rules: resolution depends on the Binance SOL/USDT 12:00 ET 1-minute candle close on April 17, compared against 80.
- Direct market context from Binance: current spot price and recent candles are above the strike.

## What is uncertain

- The relevant resolution observation is still about three days away, so current spot levels can drift materially before settlement.
- Web access did not produce the interactive Binance trade page directly, so contract-mechanics verification relied on Polymarket's quoted rules plus Binance public API outputs rather than manual inspection of the website candle UI.
- No independent macro/news source was needed to explain the current price level, but that means this note is stronger on direct price/state verification than on broader catalyst mapping.

## Why this source may matter

This source pair is enough to establish the governing settlement mechanism and the current distance from the threshold. For a date-specific crypto threshold market, that directly frames both the base case and the main risk: path dependence over the next ~72 hours rather than ambiguity about what settles the market.

## Possible impact on the question

Current direct evidence supports a Yes lean because spot is already more than 6% above the threshold. The same evidence also highlights the core risk-manager objection: a short-horizon crypto asset can easily move more than 6% by the settlement minute, so the contract is far from settled despite the current cushion.

## Reliability notes

- Binance public API is highly relevant because Binance is the governing source for the contract.
- Polymarket page is the most direct accessible statement of the contract mechanics in this run.
- Evidence independence is only medium because the market rule and the price source are linked through the same Binance-centered resolution framework, though this is appropriate for a source-of-truth market.
- Reliability for current-state verification is high; reliability for forecasting April 17 noon conditions is inherently limited by time gap and crypto volatility.
