---
type: source_note
case_key: case-20260415-7b143efd
dispatch_id: dispatch-case-20260415-7b143efd-20260415T132144Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-7b143efd | market-implied
question: Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 20, 2026 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / venue page
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7b143efd/researcher-analyses/2026-04-15/dispatch-case-20260415-7b143efd-20260415T132144Z/personas/market-implied.md]
tags: [polymarket, rules, market-implied, settlement]
---

# Summary

Polymarket’s own market page states that this contract resolves based on the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 20, 2026, using the final Close price, with Yes requiring a Close higher than 70,000. The same page showed the 70,000 line trading around 86% at capture time.

## Key facts extracted

- The relevant contract is specifically about the Binance BTC/USDT pair, not other exchanges or pairs.
- The contract uses the 1-minute candle for 12:00 in ET timezone on the specified date.
- The settlement variable is the candle’s final Close price.
- The rule uses a strict threshold: higher than 70,000, not equal to 70,000.
- The market page displayed the 70,000 outcome near 86% at the time captured.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."
- Price shown on the page for the 70,000 line was approximately 86% / 86¢.

## What is uncertain

- The market page is a venue surface, not the ultimate source-of-truth itself; Binance is still the governing settlement source.
- Web capture of the market page is sufficient to read displayed rules and approximate price but not ideal for tick-level audit history.

## Why this source may matter

It defines the resolution mechanics and shows what the live market was pricing. For this case, understanding the exact source-of-truth and threshold wording is necessary because the contract is date-specific, uses a single 1-minute candle, and has strict exchange/pair constraints.

## Possible impact on the question

This source establishes that the question is not "Will spot BTC generally stay above 70k?" but "Will Binance BTC/USDT’s noon ET 1-minute candle on April 20 close above 70,000?" That framing makes exchange-specific operational issues and exact time-window interpretation relevant, even if underlying BTC direction remains the dominant mechanism.

## Reliability notes

Reliable for reading the venue’s displayed contract wording and current market-implied probability. Less authoritative than Binance itself for final settlement data. Independence is low because this is the contract venue describing its own settlement source, not an external verifier.