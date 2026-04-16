---
type: source_note
case_key: case-20260414-3d24d01f
dispatch_id: dispatch-case-20260414-3d24d01f-20260414T184328Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-19
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 70000 on 2026-04-19?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market rules page for bitcoin-above-on-april-19
source_type: primary-contract
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3d24d01f/researcher-analyses/2026-04-14/dispatch-case-20260414-3d24d01f-20260414T184328Z/personas/variant-view.md]
tags: [polymarket, rules, resolution, source-note]
---

# Summary

This source note captures the exact market wording and the main rule-sensitive details that matter for resolution.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT one-minute candle for 12:00 in ET on April 19 has a final `Close` price above 70000.
- The market does not resolve on other exchanges or other pairs.
- Price precision is defined by the source.
- The market page showed the 70000 line trading around 89-90% at the time of review.

## Evidence directly stated by source

- Governing source of truth is Binance BTC/USDT with 1m candles selected.
- Relevant condition is the final `Close` for the 12:00 ET candle, not intraminute high, spot quote from another venue, or broader daily close.

## What is uncertain

- The page does not provide a more formal settlement data extraction method than the Binance chart instruction.
- The market page itself is not independent evidence on BTC fundamentals; it is mostly a contract and crowd-pricing source.

## Why this source may matter

This is the governing contract source. For a date-sensitive one-minute-candle market, exact wording materially controls the outcome.

## Possible impact on the question

It narrows the actual risk to a single timestamp and single venue/pair. That makes the market look safer than a broad directional BTC view, but it also creates a variant-risk angle: a short-lived but sharp selloff, exchange-specific dislocation, or settlement-minute operational issue can defeat an otherwise bullish broad-market thesis.

## Reliability notes

- High importance because it is the contract surface.
- Not independent from the trading market itself.
- Good for resolution wording, weak for external market-state inference.