---
type: source_note
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: daily-close-threshold
entity: btc
topic: Polymarket contract rules and displayed market ladder for April 17 BTC threshold market
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 74000 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/personas/market-implied.md
tags: [polymarket, contract-rules, btc, binance, daily-close]
---

# Summary

This source establishes the governing contract mechanics and also provides the contemporaneous market-implied probability ladder visible on the event page.

## Key facts extracted

- The 74,000 outcome was displayed around 66% on the fetched page, while the assignment context listed current_price 0.71 for this run.
- The rules state the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 17 has a final Close price higher than 74,000.
- The rules explicitly say the governing source is Binance BTC/USDT with Candles set to 1m.
- The page also makes clear this is Binance BTC/USDT specifically, not other exchanges or pairs.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The fetched event page is not itself the final settlement print; it is only a statement of rules and a snapshot of market pricing.
- The page view showed 66% rather than the assignment-context 71%, so intraday movement is likely present.

## Why this source may matter

This is the primary governing-source and contract-interpretation source. It determines what counts, what does not count, and why other exchange prices are only contextual.

## Possible impact on the question

It sharply narrows the problem: this is not a broad "BTC above 74k sometime" market and not a generic spot-price market. All material conditions must hold together: Binance, BTC/USDT, the 12:00 ET candle on Apr. 17, and the final 1-minute Close higher than 74,000.

## Reliability notes

High value for rules/mechanics because it is the contract page itself. Moderate value for displayed price because the fetched snapshot may lag or differ from assignment-time market price.