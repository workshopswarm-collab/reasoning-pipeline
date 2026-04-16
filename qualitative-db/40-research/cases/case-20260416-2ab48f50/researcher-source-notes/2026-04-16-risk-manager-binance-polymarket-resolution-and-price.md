---
type: source_note
case_key: case-20260416-2ab48f50
dispatch_id: dispatch-case-20260416-2ab48f50-20260416T002737Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-2ab48f50 | risk-manager
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API and Polymarket market rules page
source_type: primary_market_and_resolution_source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
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
downstream_uses: [qualitative-db/40-research/cases/case-20260416-2ab48f50/researcher-analyses/2026-04-16/dispatch-case-20260416-2ab48f50-20260416T002737Z/personas/risk-manager.md]
tags: [source-note, binance, polymarket, resolution, btc]
---

# Summary

This note captures the governing resolution mechanics and the current Binance reference price context that matter most for a narrow date-specific BTC threshold market.

## Key facts extracted

- Polymarket states the market resolves to Yes if the Binance BTC/USDT 1 minute candle for 12:00 ET on April 17 has a final Close strictly higher than 74,000.
- The governing source of truth is Binance BTC/USDT with 1m candles, not other exchanges or other BTC pairs.
- Price precision is determined by the decimals shown by the source.
- At capture time, Binance API returned BTCUSDT last price 74769.89.
- Recent Binance 1m candles around capture time showed BTC trading mostly in the mid-74,000s and briefly near 74,770.
- Polymarket market page showed the 74,000 strike trading around 61%, implying the market saw BTC as modestly more likely than not to finish above the strike at the specified noon ET close.

## Evidence directly stated by source

- Resolution requires all of the following to hold for Yes: correct date, 12:00 ET timestamp, Binance venue, BTC/USDT pair, 1 minute candle, and final Close greater than 74,000.
- Binance ticker and recent 1m candles directly show spot-level context near the threshold, but do not settle the market until the specified future candle closes.

## What is uncertain

- The current price can move materially over the roughly 39.5 hours remaining until resolution.
- Binance front-end and API can differ from other venues or aggregators in small ways; only Binance BTC/USDT matters.
- The exact candle mapping between ET noon and Binance timestamps still requires careful handling at settlement time, though ET noon corresponds to 16:00 UTC on April 17.

## Why this source may matter

This is the key primary evidence because the contract is rule-sensitive and venue-specific. The main risk is not conceptual confusion about Bitcoin generally, but timing and source-of-truth mismatch.

## Possible impact on the question

The direct evidence says the market is slightly in-the-money at capture time, but only by a small margin relative to normal BTC intraday volatility. That supports a cautious Yes lean rather than a high-confidence Yes.

## Reliability notes

Binance is the explicit resolution source, so source-of-truth credibility is high for settlement mechanics. However, current spot/ticker data are only weakly predictive for a next-day noon close in a volatile asset, so predictive reliability is moderate rather than high.