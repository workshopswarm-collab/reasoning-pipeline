---
type: source_note
case_key: case-20260415-47643da0
dispatch_id: dispatch-case-20260415-47643da0-20260415T010752Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API + Polymarket market rules page
source_type: primary-plus-contextual
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1440
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, resolution-check, timing]
---

# Summary

This source check verified the governing source of truth, the exact contract mechanics, and the current BTC/USDT trading range relevant to the April 17 noon ET resolution window.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance BTC/USDT **1 minute candle for 12:00 in the ET timezone (noon)** on April 17, using the candle's final **Close** price.
- The contract is specifically about **Binance BTC/USDT**, not other exchanges or pairs.
- Current market-implied probability from Polymarket for the 72,000 threshold is about **84%-85%**.
- Direct Binance API checks on 2026-04-14 21:12 ET showed BTCUSDT spot around **74,691.57**.
- A 60-minute Binance 1m-kline pass showed closes between about **74,400.24 and 74,731.22**.
- A 24-hour Binance 1m-kline pass showed closes between about **73,857.55 and 75,986.03**.
- Binance exchange metadata confirms BTCUSDT is an active trading symbol and the price tick size is **0.01**, which matters for close-price precision.

## Evidence directly stated by source

- Polymarket page directly states the resolution rule and source: Binance BTC/USDT, 1m candle, 12:00 ET, final close price.
- Binance API directly states recent klines, current price, 24h range, server time, and market metadata for BTCUSDT.

## What is uncertain

- This does not directly settle the April 17 noon ET candle because resolution is still ahead.
- The key remaining uncertainty is whether BTC experiences a downside move of more than roughly 3.6% from the checked spot level by the settlement minute.
- Binance website UI wording could differ from API formatting, but the API data aligns with the same market and price precision conventions.

## Why this source may matter

This is the core source pair for the case: Polymarket defines the contract mechanics, and Binance provides the governing price surface the contract points to.

## Possible impact on the question

Because BTCUSDT was trading materially above 72,000 at the time of verification and had stayed above that threshold throughout the prior 24h sample, the main near-term catalyst for a No outcome is not a specific scheduled event but a sharp risk-off move or exchange-specific dislocation before April 17 noon ET.

## Reliability notes

- Binance API is a strong direct source for the referenced market and avoids scraping ambiguity from the interactive chart UI.
- Polymarket page is the contextual source for contract wording.
- Independence between the two sources is medium rather than high because one defines the rules and the other supplies the referenced data surface; they are complementary, not competing.