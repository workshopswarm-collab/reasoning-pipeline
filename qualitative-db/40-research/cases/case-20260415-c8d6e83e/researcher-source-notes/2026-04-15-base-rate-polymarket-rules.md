---
type: source_note
case_key: case-20260415-c8d6e83e
dispatch_id: dispatch-case-20260415-c8d6e83e-20260415T151858Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the price of Bitcoin be above $68,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / primary source
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-c8d6e83e/researcher-analyses/2026-04-15/dispatch-case-20260415-c8d6e83e-20260415T151858Z/personas/base-rate.md]
tags: [source-note, polymarket, rules, contract, base-rate]
---

# Summary

The Polymarket market page states that this market resolves Yes if the Binance BTC/USDT one-minute candle for 12:00 in ET timezone on 2026-04-20 has a final close strictly higher than 68,000. This establishes the governing source of truth, timing, and strict comparison condition.

## Key facts extracted

- Resolution is based on Binance BTC/USDT, not other exchanges or pairs.
- The relevant candle is the 12:00 ET one-minute candle on April 20, 2026.
- The condition is that the final close must be strictly higher than 68,000.
- Price precision is determined by the decimals reported by the source.
- The current market price shown for the 68,000 threshold was about 96 cents Yes / roughly 95.5% implied probability in assignment metadata.

## Evidence directly stated by source

- The market page directly states the resolution criteria and settlement source.
- The page directly states the threshold and timing convention in ET.

## What is uncertain

- The web page does not itself provide the future settlement candle, only the contract specification.
- The market page text does not explain whether Binance UI availability versus API availability could create any operational edge case, though the wording strongly points to Binance as authoritative.

## Why this source may matter

This is the primary contract source. For a date-sensitive, rule-sensitive market, the exact settlement mechanics matter almost as much as the directional price view.

## Possible impact on the question

The rules narrow the question to one exact exchange, pair, timezone, minute, and strict threshold comparison. That reduces ambiguity but means a high-probability yes case can still fail if BTC falls below 68,000 at the specific noon ET minute.

## Reliability notes

As the primary market source, Polymarket is authoritative for contract wording. The remaining risk is not source credibility but operational interpretation at the exact settlement minute.