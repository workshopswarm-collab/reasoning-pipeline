---
type: source_note
case_key: case-20260415-1a345042
dispatch_id: dispatch-case-20260415-1a345042-20260415T223206Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: Contract mechanics for Apr 21 BTC > 72000 market
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-21 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event rules page
source_type: market rules / primary contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1a345042/researcher-analyses/2026-04-15/dispatch-case-20260415-1a345042-20260415T223206Z/personas/base-rate.md]
tags: [polymarket, rules, settlement, source-note]
---

# Summary

The contract resolves Yes only if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on Apr 21 has a final Close strictly higher than 72,000. This makes the exact venue, pair, time zone, minute, and strict-greater-than condition all material.

## Key facts extracted

- Resolution source is Binance.
- Relevant pair is BTC/USDT.
- Relevant chart setting is 1-minute candles.
- Relevant timestamp is 12:00 in ET timezone on Apr 21, 2026.
- Relevant field is the candle's final Close price.
- The threshold test is strictly higher than 72,000, not greater-than-or-equal.
- Other exchanges or other pairs do not count.
- Price precision is determined by the decimals shown in the source.

## Evidence directly stated by source

All contract mechanics above are directly stated in the rules text on the event page.

## What is uncertain

- The rules page does not itself display the future settlement candle.
- There remains minor operational ambiguity around how Binance web UI timezone labeling maps internally, but the market text explicitly says ET and points users to the Binance chart surface.

## Why this source may matter

This is the governing contract source. For a date-specific and multi-condition market, correctly interpreting the minute, pair, venue, and strict comparison operator is mandatory.

## Possible impact on the question

The source narrows the claim: the trade is not about Bitcoin broadly, nor a daily close, nor another exchange. It is about one exact Binance BTC/USDT minute close at noon ET on Apr 21 being strictly above 72,000.

## Reliability notes

- High reliability for contract interpretation because it is the market's own rules page.
- It is not evidence about future price direction, only about what must happen for resolution.