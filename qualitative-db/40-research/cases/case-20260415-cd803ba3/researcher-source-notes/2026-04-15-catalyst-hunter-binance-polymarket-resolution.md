---
type: source_note
case_key: case-20260415-cd803ba3
dispatch_id: dispatch-case-20260415-cd803ba3-20260415T203927Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 74000 on April 17, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API and Polymarket rules page
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
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-cd803ba3/researcher-analyses/2026-04-15/dispatch-case-20260415-cd803ba3-20260415T203927Z/personas/catalyst-hunter.md]
tags: [source-note, primary-source, binance, polymarket, resolution]
---

# Summary

This note captures the governing source-of-truth mechanics and current spot context for the April 17 BTC > 74k contract.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT **1-minute candle at 12:00 ET** on April 17, using the candle's final **Close** price.
- The contract is specifically about **Binance BTC/USDT**, not other exchanges or pairs.
- Binance API spot fetch at research time showed BTCUSDT at **74748.18**.
- Recent Binance 1-minute klines around research time showed closes clustered roughly in the **74638-74768** range.

## Evidence directly stated by source

- Polymarket rule text directly specifies the source, instrument, interval, timezone reference, and winning condition.
- Binance API directly provides current BTCUSDT price and recent 1-minute candles.

## What is uncertain

- Current spot is not the settlement print; the market resolves nearly two days later at a very specific minute.
- The public API sample verifies current trading level, but not the eventual noon-ET close on Apr 17.
- I did not independently verify how Binance UI labels ET versus local timezone settings; I rely on Polymarket's stated ET interpretation for contract mechanics.

## Why this source may matter

This is the core evidence set for both contract interpretation and the starting state of the underlying. Because the contract is narrow and time-specific, source-of-truth mechanics matter almost as much as directional BTC outlook.

## Possible impact on the question

If BTC can simply hold near current levels into the specified minute, Yes is favored. But because the resolution depends on a single one-minute close on Binance at noon ET, near-term volatility and timing risk remain material even when spot is already above 74k.

## Reliability notes

- High reliability for contract wording and current underlying level.
- Independence is limited because both pieces are tightly tied to the same market/resolution stack rather than broader contextual drivers.
- Best used with at least one independent contextual source on likely near-term catalysts and volatility regime.