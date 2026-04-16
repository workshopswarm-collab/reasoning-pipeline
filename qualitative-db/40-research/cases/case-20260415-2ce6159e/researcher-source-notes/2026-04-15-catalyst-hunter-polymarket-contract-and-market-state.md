---
type: source_note
case_key: case-20260415-2ce6159e
dispatch_id: dispatch-case-20260415-2ce6159e-20260415T142913Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: prediction-market-structure
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market-rules-page
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2ce6159e/researcher-analyses/2026-04-15/dispatch-case-20260415-2ce6159e-20260415T142913Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, market-implied-probability, settlement]
---

# Summary

The Polymarket market rules clearly define a narrow, time-specific Binance BTC/USDT settlement condition and currently price the 72,000 threshold at about 93%.

## Key facts extracted

- The market title is "Bitcoin above ___ on April 16?" with an Apr 16, 2026 resolution window.
- The 72,000 line is quoted at about 93% on the event page.
- Rules specify Yes only if the Binance BTC/USDT one-minute candle for 12:00 ET on the specified date has a final close above 72,000.
- Rules explicitly say this is Binance BTC/USDT, not other exchanges or pairs.
- Rules state price precision is determined by the source.

## Evidence directly stated by source

- Governing source of truth is Binance BTC/USDT one-minute candle close at 12:00 ET on Apr 16.
- Market-implied probability for above 72,000 is approximately 0.93 at observation time.
- All material conditions must hold simultaneously: correct venue, correct pair, correct one-minute candle, correct ET timestamp, close price strictly above 72,000.

## What is uncertain

- The event page is a snapshot and can move quickly.
- The page does not independently verify Binance UI/API alignment at the exact settlement minute.
- The page does not identify what catalyst, if any, traders are pricing over the next day.

## Why this source may matter

This is the controlling contract language and the direct source for market-implied odds, so it anchors both resolution interpretation and the baseline the research view must compare against.

## Possible impact on the question

The contract is narrower than a generic "BTC above 72k tomorrow" claim. Any thesis must be about Binance BTC/USDT specifically at the noon ET one-minute close, not broad crypto sentiment alone.

## Reliability notes

High reliability for contract interpretation and current market pricing. It is authoritative for the market's rules but not for the underlying BTC spot price itself.