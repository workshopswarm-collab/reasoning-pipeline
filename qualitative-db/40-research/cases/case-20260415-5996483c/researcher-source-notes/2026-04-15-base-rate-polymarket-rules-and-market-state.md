---
type: source_note
case_key: case-20260415-5996483c
dispatch_id: dispatch-case-20260415-5996483c-20260415T193222Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: BTC > 70000 on Apr 20 noon ET contract mechanics and market state
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page for bitcoin-above-on-april-20
source_type: market page / primary contract rules surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
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
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-5996483c/researcher-analyses/2026-04-15/dispatch-case-20260415-5996483c-20260415T193222Z/personas/base-rate.md
tags: [polymarket, contract-rules, binance, btc, noon-close]
---

# Summary

This source provides the governing contract wording and current market pricing for the April 20 BTC-above ladder. For the 70,000 line, the market was pricing roughly 92-93% Yes at fetch time.

## Key facts extracted

- The contract resolves Yes if the **Binance BTC/USDT 1-minute candle for 12:00 ET on April 20** has a final **Close** above 70,000.
- The contract resolves from the Binance trading page with **1m** and **Candles** selected.
- The rule is specifically about **Binance BTC/USDT**, not other venues or pairs.
- The event page showed the 70,000 line around **92-93% Yes** at fetch time.
- Other ladders on the same page were also skewed bullish, with 72,000 around 81% and 74,000 around 59%, which gives a rough cross-check on the market-implied distribution.

## Evidence directly stated by source

- Resolution depends on a single minute-candle **close**, not intraday high, touch, VWAP, or daily close.
- Timing is **12:00 in ET timezone (noon)** on the date in the title.
- Price precision is determined by the source display.

## What is uncertain

- The page does not itself provide the future resolving candle.
- The visible yes/no prices are snapshot-level and can move materially before resolution.

## Why this source may matter

This is the primary rules source and the best available current view of the market-implied baseline. Because the contract is narrow and date-specific, exact wording matters a lot.

## Possible impact on the question

The wording makes this less forgiving than a touch-style market. BTC can trade well above 70k during the window and still resolve No if the specific Binance 12:00 ET 1-minute close on April 20 prints below 70,000.

## Reliability notes

High reliability for contract wording and decent reliability for current market snapshot. It is the primary source for settlement mechanics, but not itself proof of the final outcome.