---
type: source_note
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Polymarket April 17 BTC above ladder rules and market snapshot
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 17 close above 74000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page for Bitcoin above ___ on April 17
source_type: market rules / market snapshot
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/personas/variant-view.md
tags: [polymarket, rules, binance, threshold-market, noon-close]
---

# Summary

This source establishes both the governing market mechanics and the contemporaneous market-implied baseline for the 74,000 threshold outcome.

## Key facts extracted

- The market resolves **Yes** if the **Binance BTC/USDT 1-minute candle for 12:00 ET on April 17** has a final **Close** price **higher than 74,000**.
- It resolves **No** otherwise.
- The rules explicitly say the resolution source is **Binance**, not another venue or pair.
- The market page snapshot showed the **74,000 outcome at 66%** at fetch time.
- Adjacent ladder prices on the same page were approximately **72,000 at 91%** and **76,000 at 27%**, which gives useful contextual curvature around the threshold.

## Evidence directly stated by source

- Exact source-of-truth wording for the contract.
- Exact timing convention: **12:00 in ET timezone (noon)** on the specified date.
- Exact measurement field: the candle **Close**, not high/low/last trade on another venue.
- Market snapshot probabilities for the ladder.

## What is uncertain

- The fetched market page is a public web snapshot, so displayed prices can move after capture.
- The page itself does not provide tomorrow's settlement candle in advance; it only defines how to judge it when the time arrives.
- The webpage is sufficient for rule interpretation but not a substitute for the eventual Binance candle close.

## Why this source may matter

This is the governing contract source for the case. It determines what counts, what does not count, and prevents accidental drift into using other exchanges, spot indexes, highs/lows, or the wrong minute.

## Possible impact on the question

It sharpens the variant view because a close-above-at-a-specific-minute market is materially stricter than a touch/high market. That means intraday strength above 74k before noon ET is not enough if BTC fades by the exact 12:00 ET candle close.

## Reliability notes

- Strong for contract interpretation and baseline market pricing.
- Not sufficient alone for price forecasting.
- Evidence independence is limited if used alone, so a separate contextual/direct market-price source is still needed.