---
type: source_note
case_key: case-20260409-99902b0b
dispatch_id: dispatch-case-20260409-99902b0b-20260409T203957Z
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: markets
entity: btc
topic: case-20260409-99902b0b | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 10?
driver: operational-risk
date_created: 2026-04-09
source_name: Polymarket market page and rules for bitcoin-above-on-april-10
source_type: market rules / venue page
source_url: https://polymarket.com/event/bitcoin-above-on-april-10
source_date: 2026-04-09
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-99902b0b/researcher-analyses/2026-04-09/dispatch-case-20260409-99902b0b-20260409T203957Z/personas/risk-manager.md]
tags: [polymarket, market-rules, resolution-source, timing-risk]
---

# Summary

This source establishes the contract mechanics and current market pricing context. It says the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 10 has a final Close above 70,000, and otherwise resolves No. The same page showed the 70,000 strike trading around 95% at fetch time.

## Key facts extracted

- Governing source of truth is Binance BTC/USDT with 1m candles.
- Relevant datapoint is the final Close of the 12:00 ET candle on April 10, 2026.
- This is not a generic BTC spot-price question across exchanges; Binance BTC/USDT is the only named resolution venue/pair.
- The page showed the 70,000 line around 95% implied probability when fetched.
- Precision is determined by Binance source decimals.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."

## What is uncertain

- The public market page is a secondary presentation layer rather than Binance itself.
- The page does not itself provide the future April 10 noon candle value.
- The visible 95% price may move materially before resolution.

## Why this source may matter

It defines the multi-condition resolution mechanics, which are the main risk-management issue here: correct date, correct timezone, correct venue, correct pair, correct candle granularity, and specifically the final Close rather than intraminute highs.

## Possible impact on the question

This source makes clear that a broad thesis like "BTC is trading above 70k now" is supportive but not sufficient on its own. The actual question is whether Binance BTC/USDT remains above 70,000 at the exact April 10 noon ET 1-minute close.

## Reliability notes

Good for contract interpretation and market-implied pricing, but not the authoritative future settlement datapoint itself. Reliability for rules is reasonably high because it is the listing venue; reliability for actual final settlement value depends on Binance.