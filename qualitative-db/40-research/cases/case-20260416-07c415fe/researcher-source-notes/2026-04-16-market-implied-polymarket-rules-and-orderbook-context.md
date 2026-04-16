---
type: source_note
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: prediction-markets
entity:
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page and rules
source_type: market page / contract rules / market-implied context
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: supports yes
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-implied, resolution]
---

# Summary

The Polymarket event page shows the contract mechanics and current crowd pricing. The visible page for April 19 indicates the 80 strike was trading around 89% Yes / 13% No at fetch time, with explicit rules that resolution uses the Binance SOL/USDT one-minute candle for 12:00 ET on the specified date.

## Key facts extracted

- The April 19 event page lists multiple strike outcomes for SOL.
- The 80 strike was displayed around `89%` with Yes around `90¢` and No around `13¢` at fetch time.
- Rules state the market resolves `Yes` if the Binance 1 minute candle for `SOL/USDT` at `12:00` in `ET timezone (noon)` on the specified date has a final close above the stated price.
- Rules further specify the source is Binance, the pair is SOL/USDT, and price precision is determined by the source.

## Evidence directly stated by source

- Market-implied probability was about 0.89 to 0.90 for the 80 strike.
- The contract is narrow and mechanical: one exchange, one pair, one one-minute candle, one timestamp, close price must be strictly higher than 80.

## What is uncertain

- The fetched page is a consumer-facing market page and may not perfectly reflect deep book liquidity or final execution prices at every moment.
- The displayed 89%/90¢ values imply some spread or snapshot mismatch, so this should be treated as approximate market-implied context rather than a precise microstructure audit.

## Why this source may matter

It is both the market's own statement of current consensus and the main contract wording needed to avoid misresolving on the wrong exchange, pair, timestamp, or inequality condition.

## Possible impact on the question

Supports treating the live market as a serious prior: if the crowd is around 89-90% Yes while the underlying Binance spot is already mid-85s, the market appears to be pricing that a roughly 5+ dollar drawdown in three days is possible but still unlikely.

## Reliability notes

- High relevance for contract interpretation.
- Medium-high credibility for current displayed odds, but this is still a website snapshot rather than a formal historical market data export.
- Important to combine with Binance price evidence because rules alone do not establish the underlying probability.