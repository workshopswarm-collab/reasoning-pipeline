---
type: source_note
case_key: case-20260415-1a345042
dispatch_id: dispatch-case-20260415-1a345042-20260415T223206Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-1a345042 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page + Binance BTCUSDT API live verification
source_type: primary_market_rules_and_exchange_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1a345042/researcher-analyses/2026-04-15/dispatch-case-20260415-1a345042-20260415T223206Z/personas/risk-manager.md]
tags: [polymarket, binance, resolution, btc]
---

# Summary

This note captures the direct rule surface for the market and a live verification pass on Binance BTCUSDT pricing mechanics.

## Key facts extracted

- Polymarket rules say the market resolves Yes if the Binance BTC/USDT 1 minute candle for 12:00 ET on April 21 has a final Close price strictly higher than 72,000.
- The rules explicitly name Binance BTC/USDT with 1m candles as the resolution source and specify that other exchanges or trading pairs do not count.
- Price precision is determined by the number of decimals on the Binance source.
- A timezone check maps 2026-04-21 12:00 ET to 2026-04-21 16:00 UTC.
- Live Binance public API verification on 2026-04-15 showed BTCUSDT spot around 74,989 and recent 1m candles near 75,000.
- A 1,000-minute Binance kline pull on 2026-04-15 showed all sampled closes above 72,000, with min 73,566 and max 75,267.69.

## Evidence directly stated by source

- Polymarket directly states the resolution condition, source, timeframe, and comparison operator (higher than the threshold).
- Binance public market data directly shows current BTCUSDT spot and 1-minute kline fields including Close values.

## What is uncertain

- The Polymarket page does not itself clarify every Binance UI/API edge case around the label "12:00 in the ET timezone" beyond pointing to the Binance trading surface.
- Current spot being above 72,000 does not settle the April 21 noon ET candle; several days of price path remain.
- Binance operational or data-surface issues near the observation time could matter if UI and API behavior diverge.

## Why this source may matter

This is the governing contract surface plus the direct exchange source class named in the contract, so it determines both what counts and the main operational failure modes.

## Possible impact on the question

The direct rule check removes most ambiguity about exchange, pair, and candle granularity. The live Binance data also shows a current buffer of roughly 4 percent above the threshold, which supports a Yes lean but still leaves nontrivial path risk over the remaining days.

## Reliability notes

- Polymarket is authoritative for the contract wording but not for the future outcome.
- Binance is authoritative for the referenced market data but still leaves some operational interpretation risk around the exact noon-ET candle selection and any exchange-side anomalies.
- Independence is limited because the contract is explicitly pinned to Binance; contextual sources are useful mainly for robustness, not settlement authority.
