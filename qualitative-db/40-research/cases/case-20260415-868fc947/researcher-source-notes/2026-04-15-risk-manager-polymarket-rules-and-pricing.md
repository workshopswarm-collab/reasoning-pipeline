---
type: source_note
case_key: case-20260415-868fc947
dispatch_id: dispatch-case-20260415-868fc947-20260415T090047Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-868fc947/researcher-analyses/2026-04-15/dispatch-case-20260415-868fc947-20260415T090047Z/personas/risk-manager.md]
tags: [polymarket, rules, resolution, pricing]
---

# Summary

Polymarket provides the governing contract language and the current market-implied probability baseline. For the 72,000 strike, the market page showed roughly 88% Yes at time of review.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-16 has a final Close above 72,000.
- The source of truth is Binance BTC/USDT, not other exchanges or other BTC pairs.
- Price precision is determined by Binance source precision.
- On the market page at review time, the 72,000 strike was priced around 88% Yes / 13% No.

## Evidence directly stated by source

- Exact resolution language tied to Binance, 1m candle, 12:00 ET, and Close price.
- Outcome threshold is strictly higher than 72,000, not equal to 72,000.
- The 72,000 line currently trades at an extreme probability relative to nearby strikes.

## What is uncertain

- The page is a market interface, not the settlement source itself.
- Front-end prices can move quickly and are only a snapshot.
- The page does not itself provide tomorrow's resolving candle.

## Why this source may matter

This is the authoritative source for contract interpretation and for the market-implied probability comparison required in the finding.

## Possible impact on the question

It anchors both the baseline probability and the key risk-manager concern: the contract is narrow and time-specific, so even a bullish spot backdrop can still fail if the exact noon ET Binance close prints below 72,000.

## Reliability notes

Useful and necessary for rules, but only medium credibility for price snapshots because it is a trading interface rather than the final data source. The resolution mechanics are clear, so source-of-truth ambiguity is low once Binance is checked directly.