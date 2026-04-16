---
type: source_note
case_key: case-20260415-cb25c8c6
dispatch_id: dispatch-case-20260415-cb25c8c6-20260415T194743Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-19
question: Will the Binance BTC/USDT 12:00 ET 1m candle close on 2026-04-19 be above 68000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page for Bitcoin above ___ on April 19
source_type: market rules / resolution surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-cb25c8c6/researcher-analyses/2026-04-15/dispatch-case-20260415-cb25c8c6-20260415T194743Z/personas/catalyst-hunter.md]
tags: [polymarket, resolution-rules, binance, btcusdt, deadline]
---

# Summary

This source establishes the contract mechanics and governing source of truth. It says the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 19, 2026, using the final Close price, and that the threshold is strictly higher than 68,000.

## Key facts extracted

- Resolution depends on the Binance BTC/USDT pair specifically, not other exchanges or pairs.
- The relevant observation is the 1-minute candle labeled 12:00 in ET on April 19, 2026.
- The winning condition is that the final Close price is higher than 68,000.
- If the close is 68,000 exactly or below, the market resolves No.
- Precision is determined by the source display / source decimals.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."

## What is uncertain

- The page does not independently prove how Binance labels the candle relative to ET versus UTC; that requires a separate operational interpretation pass.
- The page does not provide a current BTC price itself.

## Why this source may matter

This is the governing settlement source. For a narrow date-specific market, the exact exchange, pair, minute bucket, timezone, and strict inequality matter more than general BTC direction.

## Possible impact on the question

It makes the thesis primarily a short-horizon path question: BTC/USDT only needs to remain above 68,000 at the specific noon ET minute on April 19. With spot already far above 68,000 on April 15, the main remaining risks are a sharp drawdown before the window or a contract-interpretation / exchange-data issue.

## Reliability notes

High reliability for contract mechanics because this is the market's own rules page. It is not independent evidence about future BTC price path, so it must be paired with direct market data or exchange data for the actual probability view.
