---
type: source_note
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity:
topic: case-20260415-7d14e3a4 | risk-manager
question: Will the Binance BTC/USDT 1-minute candle for 2026-04-19 12:00 ET close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page
source_type: market contract / primary rules source
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [risk-manager.md, risk-manager.sidecar.json, evidence/risk-manager.md]
tags: [polymarket, contract-rules, resolution-source, noon-et]
---

# Summary

The Polymarket rules page defines a narrow, timing-sensitive contract: the market resolves Yes only if Binance BTC/USDT's 1-minute candle for 12:00 ET on 2026-04-19 has a final close strictly higher than 72,000.

## Key facts extracted

- Resolution is based on the Binance BTC/USDT pair only.
- Resolution uses the 1-minute candle for `12:00` in the ET timezone on the specified date.
- The relevant value is the candle's final `Close` price.
- The comparison is strict: price must be `higher than` the threshold, not equal to it.
- Price precision is determined by Binance source decimal places.
- The Polymarket surface displayed the 72,000 line at roughly `87%` at fetch time, consistent with assignment `current_price: 0.865`.

## Evidence directly stated by source

- Contract wording and settlement mechanics are directly stated by the rules page.
- The market surface directly provides the current market-implied probability context for the 72,000 threshold.

## What is uncertain

- The fetched page is a public web rendering, not a signed rules export.
- The page does not explain fallback procedures if Binance UI access is degraded at resolution time.

## Why this source may matter

This is the governing contract source for the market. It defines the exact timing, exchange, pair, candle interval, threshold condition, and strict inequality required for resolution.

## Possible impact on the question

It raises path and operational risk versus a generic “BTC above 72k by date” interpretation. A trader can be directionally right on Bitcoin strength and still lose if BTC falls below 72,000 specifically at the noon ET 1-minute candle, or if there is confusion around exact candle interpretation.

## Reliability notes

- High relevance because this is the market's own rules page.
- High authority for contract interpretation, though there remains modest operational ambiguity around exact data-display/fallback handling.
