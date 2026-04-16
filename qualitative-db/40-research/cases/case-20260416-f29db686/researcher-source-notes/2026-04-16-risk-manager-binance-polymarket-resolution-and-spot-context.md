---
type: source_note
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-f29db686 | risk-manager
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and Binance BTCUSDT public market data
source_type: primary-plus-contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/personas/risk-manager.md]
tags: [source-note, polymarket, binance, btc, resolution]
---

# Summary

This note captures the contract mechanics and the most relevant current spot context for the Apr 17 noon ET BTC > 74,000 market.

## Key facts extracted

- Polymarket rules say the market resolves Yes only if the Binance BTC/USDT **1-minute candle for 12:00 ET on Apr 17** has a final **Close** price **higher than 74,000**.
- The source of truth is Binance BTC/USDT with **1m Candles** selected; not another exchange or pair.
- Current displayed market price for the 74,000 line on Polymarket was about **61%** on fetch.
- Binance public API spot context at approximately **2026-04-16 00:43 UTC** showed BTCUSDT around **74,771.12**.
- Recent Binance 1-minute closes in the fetch window were all above 74,000, roughly **74,771 to 74,834**.

## Evidence directly stated by source

From Polymarket page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected on the top bar."
- The 74,000 contract displayed around 61% on the fetched page.

From Binance public API output gathered during this run:
- ticker price: 74,771.12
- recent 1m closes included 74,774.37, 74,828.33, 74,834.00, 74,792.20, 74,771.12

## What is uncertain

- Current spot level does not settle the contract; only the **single 12:00 ET one-minute close on Apr 17** matters.
- Binance page UI itself did not extract cleanly via web fetch, so the direct Binance evidence here comes from Binance public API rather than the exact front-end candle widget named in the market wording.
- Overnight volatility could move BTC several percent before the settlement minute.

## Why this source may matter

This is the core source set for ruling out common contract mistakes. The market is not asking whether BTC trades above 74,000 at any time, nor whether another exchange prints above 74,000, nor whether BTC closes the day above 74,000. It is asking about one specific Binance minute close.

## Possible impact on the question

The current spot being above 74,000 supports a positive lean, but the narrow settlement design creates meaningful timing and microstructure risk. That means a risk-manager should resist over-reading a modest current cushion as if it were a broad daily-close advantage.

## Reliability notes

- Polymarket contract page is the authoritative statement of market rules and thus the governing source for resolution mechanics.
- Binance public API is highly relevant contextual evidence for current spot and recent minute closes, but not itself the written settlement instruction.
- Evidence independence is only moderate because both sources concern the same underlying venue and instrument.
- Main residual ambiguity is practical rather than conceptual: exact front-end candle display versus public API should usually align, but the contract wording points to the Binance chart interface as the final surface.