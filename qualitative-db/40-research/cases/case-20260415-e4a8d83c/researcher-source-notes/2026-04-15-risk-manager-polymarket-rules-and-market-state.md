---
type: source_note
case_key: case-20260415-e4a8d83c
dispatch_id: dispatch-case-20260415-e4a8d83c-20260415T230345Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: btc
topic: case-20260415-e4a8d83c | risk-manager
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market rules / platform page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-e4a8d83c/researcher-analyses/2026-04-15/dispatch-case-20260415-e4a8d83c-20260415T230345Z/personas/risk-manager.md]
tags: [polymarket, market-rules, resolution, btc]
---

# Summary

Polymarket states that this market resolves from the Binance BTC/USDT 1-minute candle at 12:00 PM ET on April 17, using the candle's final Close price. The same page also showed the current market pricing for the $74,000 threshold at roughly 72% Yes on capture.

## Key facts extracted

- Resolution condition is not spot price at an arbitrary moment; it is the **final Close** of the Binance BTC/USDT **1-minute candle labeled 12:00 in ET timezone**.
- Market resolves Yes only if that final Close is **higher than 74,000**.
- Resolution source is specifically Binance BTC/USDT with 1m candles selected.
- Price precision is whatever decimal precision the source shows.
- Captured market state on page load showed the April 17 $74,000 line trading around **72% Yes**.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The web capture gives current market pricing but not full order-book depth or time series evolution.
- The page language does not independently verify how Binance labels candle time on the front-end, so a direct Binance/API verification remains important.

## Why this source may matter

This is the governing contract surface. The key risk here is contract interpretation, not macro thesis alone. The market depends on a narrow time slice, a specific exchange, and one exact field (Close), so any analysis that uses broader BTC spot narratives without checking the actual settlement mechanics can be wrong.

## Possible impact on the question

This source makes timing risk and exchange-specific basis risk material. BTC can trade above 74k broadly yet still resolve No if the Binance BTC/USDT 12:00 ET 1-minute close prints 74,000 or lower.

## Reliability notes

High reliability for contract mechanics because this is the market's own stated rules. Lower reliability for fair-value inference because the page is a market venue, not an independent external data source.