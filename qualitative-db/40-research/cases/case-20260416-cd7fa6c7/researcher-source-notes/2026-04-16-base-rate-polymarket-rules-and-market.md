---
type: source_note
case_key: case-20260416-cd7fa6c7
dispatch_id: dispatch-case-20260416-cd7fa6c7-20260416T010113Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-cd7fa6c7 | base-rate
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 17, 2026 close above 74000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market rules / primary contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: base-rate
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cd7fa6c7/researcher-analyses/2026-04-16/dispatch-case-20260416-cd7fa6c7-20260416T010113Z/personas/base-rate.md]
tags: [polymarket, contract-rules, resolution-source, binance]
---

# Summary

Primary rule source for the market. It establishes that the governing observation is not a daily close or broad cross-exchange BTC level, but the final close of the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 17, 2026.

## Key facts extracted

- Market title threshold is 74,000.
- Market page showed the 74,000 line trading around 65 cents at fetch time, implying roughly 65% market probability.
- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final Close price strictly higher than 74,000.
- The market resolves No otherwise.
- Resolution source is Binance BTC/USDT with 1m candles selected.
- Price precision is determined by the number of decimals in the Binance source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."

## What is uncertain

- The public market page is clear on the rule text, but practical settlement still depends on Binance displaying/finalizing that candle in a stable way at the relevant time.
- The fetched page duplicates some text blocks, so the rules should be treated as content extracted from the rendered page rather than a formal API schema.

## Why this source may matter

This source defines the exact event being priced. For a date-sensitive crypto threshold market, contract interpretation matters as much as directional BTC view because the relevant observation is one exchange, one pair, one timestamp, one minute, and one close value.

## Possible impact on the question

It narrows the problem to: what is the chance BTC/USDT on Binance is above 74,000 specifically at the noon ET 1-minute close on April 17. Any evidence about other exchanges, intraday highs, or end-of-day closes is only contextual.

## Reliability notes

High for contract wording because it is the primary market page, but medium on operational execution details because settlement still relies on Binance data presentation and the exact candle close being available/finalized without ambiguity.