---
type: source_note
case_key: case-20260414-4d440738
dispatch_id: dispatch-case-20260414-4d440738-20260414T195302Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 68000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page and rules
source_type: market page / primary contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4d440738/researcher-analyses/2026-04-14/dispatch-case-20260414-4d440738-20260414T195302Z/personas/market-implied.md]
tags: [polymarket, contract-rules, binance, settlement]
---

# Summary

Polymarket shows the 68,000 strike trading around 94% Yes on 2026-04-14, and the rules specify a narrow resolution source: the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-20, using the final close price.

## Key facts extracted

- The market title is "Bitcoin above ___ on April 20?" and the 68,000 strike is the relevant contract.
- The displayed market price for the 68,000 strike is about 94% Yes, close to the assignment snapshot of 0.935.
- The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET (noon) on April 20 has a final close strictly higher than 68,000.
- The relevant source is Binance BTC/USDT specifically, not other exchanges or other BTC pairs.
- Precision is determined by the decimals shown in the Binance source.

## Evidence directly stated by source

- Contract wording and source of truth are explicit on the market page.
- Cross-strike prices on the ladder are internally coherent: higher probabilities for 62k/64k/66k, 94% at 68k, 85% at 70k, 73% at 72k, 51% at 74k.

## What is uncertain

- The fetched page is a public web rendering, not a formal API response.
- The page does not itself provide the eventual Binance candle print, only the resolution rule.

## Why this source may matter

This is the governing source for what counts. It makes the case rule-sensitive because spot BTC being above 68k on other venues or at nearby timestamps would not be sufficient if the Binance noon-ET 1-minute close prints below 68k.

## Possible impact on the question

This source strongly supports the market's high Yes probability only insofar as current spot is materially above 68k and the narrow noon-ET Binance condition does not add much extra failure risk. It also creates a nontrivial path to a No outcome via timing or exchange-specific variation even if BTC remains broadly strong.

## Reliability notes

Useful as the primary contract and price surface, but not fully independent evidence because the same venue both displays the consensus probability and defines the wording being analyzed.