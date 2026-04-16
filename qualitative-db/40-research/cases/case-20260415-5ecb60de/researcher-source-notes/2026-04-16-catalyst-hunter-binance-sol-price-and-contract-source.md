---
type: source_note
case_key: case-20260415-5ecb60de
dispatch_id: dispatch-case-20260415-5ecb60de-20260416T000100Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: market-structure
entity: sol
topic: binance sol-usdt spot price and market resolution mechanics
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above $80 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance SOLUSDT API and Polymarket market rules
source_type: primary-plus-resolution-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-5ecb60de/researcher-analyses/2026-04-16/dispatch-case-20260415-5ecb60de-20260416T000100Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, resolution-source, source-note]
---

# Summary

This source set establishes both the live reference price area for SOL/USDT and the exact market resolution mechanics. The market resolves from the Binance SOL/USDT 1-minute candle at 12:00 ET on April 19, 2026, with a Yes outcome only if the final candle close is strictly above 80.00.

## Key facts extracted

- Binance API returned a live SOLUSDT spot price of 84.73 at research time.
- Recent Binance 1-minute klines around research time showed SOL/USDT trading in the 84.63 to 84.97 area.
- Recent daily Binance klines showed SOL closing above 80 on every day from April 3 through April 16 available in the pull.
- Polymarket rules explicitly say the source of truth is Binance SOL/USDT with 1m candles selected, using the 12:00 ET candle close on the named date.
- The contract requires the close to be higher than 80; exactly 80.00 would resolve No.
- The market is about Binance SOL/USDT specifically, not other exchanges or pairs.

## Evidence directly stated by source

- Binance API spot endpoint returned `{"symbol":"SOLUSDT","price":"84.73000000"}`.
- Binance 1-minute kline endpoint returned recent closes of 84.93, 84.86, 84.80, 84.63, and 84.73.
- Binance daily kline endpoint showed closes of 80.40, 80.83, 81.89, 80.03, 85.56, 82.57, 83.33, 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, and 84.73 for the most recent 14 daily candles available.
- Polymarket rules state that the market resolves to Yes if the Binance 1 minute candle for SOL/USDT at 12:00 ET on April 19 has a final Close price higher than the strike.

## What is uncertain

- The live price and recent daily closes do not directly settle the April 19 noon ET candle, only the starting distance from the strike and recent realized volatility regime.
- Binance API access worked, but the browser-trade surface itself was harder to scrape directly; the API remains the cleaner direct surface for price verification.
- Near-term crypto headline catalysts before April 19 were not cleanly identified from the available web tools in this run, so the catalyst calendar is inferred mostly from generic weekend crypto flow risk rather than a specific scheduled event.

## Why this source may matter

This is the governing source set for both contract interpretation and the most decision-relevant current state variable: SOL/USDT on Binance. It makes the evidence floor legible because it verifies the exact venue, pair, price precision, timing surface, and strict-above threshold.

## Possible impact on the question

With SOL trading around 84.7, the market begins roughly 5.9% above the 80 strike. Absent a sharp downside move before noon ET April 19, this directly supports a high Yes probability. The main remaining path to No is a broad crypto risk-off move, exchange-specific dislocation, or a late drop that leaves the exact Binance noon candle at 80.00 or below.

## Reliability notes

- Binance is the authoritative price source for this contract and therefore the most important direct source.
- Polymarket rules are the authoritative contract-interpretation surface for what counts.
- This source set has high relevance and low source-of-truth ambiguity for the resolution mechanics, though it does not itself forecast the future path of SOL into April 19.
