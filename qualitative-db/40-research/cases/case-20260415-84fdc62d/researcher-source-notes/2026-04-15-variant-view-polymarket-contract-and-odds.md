---
type: source_note
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 PM ET 1-minute candle close on 2026-04-20 above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-84fdc62d/researcher-analyses/2026-04-15/dispatch-case-20260415-84fdc62d-20260415T125809Z/personas/variant-view.md]
tags: [polymarket, contract, resolution, binance, timing]
---

# Summary

The market is explicitly about the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 20, 2026, with a Yes outcome only if the final close is strictly higher than 70,000. Market pricing on April 15 showed the 70,000 line trading around 86% Yes.

## Key facts extracted

- Resolution is tied to Binance BTC/USDT, not other exchanges or BTC/USD indices.
- The relevant datapoint is the 1-minute candle for 12:00 PM ET on the specified date.
- The close must be strictly greater than 70,000, not equal.
- Price precision is determined by the decimals shown by Binance.
- On fetch, the 70,000 contract was trading at roughly 86% Yes.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- Resolution source is Binance with BTC/USDT, 1m candles.

## What is uncertain

- The public market page does not itself show the future April 20 candle, only the contract wording and current odds.
- The page does not independently clarify edge cases beyond the wording shown.

## Why this source may matter

This is the governing source for what counts. The contract is date-sensitive, exchange-specific, pair-specific, timezone-specific, and based on a single minute close, so resolution mechanics matter almost as much as directional BTC outlook.

## Possible impact on the question

This source forces the analysis to focus on whether Binance BTC/USDT stays above 70,000 specifically at noon ET on April 20, not whether BTC broadly trades above 70,000 on average across venues or at some other time that day.

## Reliability notes

High reliability for contract interpretation because it is the market operator’s own rules page. It is not evidence about future price direction by itself.