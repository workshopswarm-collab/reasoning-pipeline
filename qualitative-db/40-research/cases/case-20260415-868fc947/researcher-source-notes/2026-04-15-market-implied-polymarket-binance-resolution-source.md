---
type: source_note
case_key: case-20260415-868fc947
dispatch_id: dispatch-case-20260415-868fc947-20260415T090047Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-868fc947 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page / Gamma event metadata for Bitcoin above on April 16
source_type: market page and API metadata
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-868fc947/researcher-analyses/2026-04-15/dispatch-case-20260415-868fc947-20260415T090047Z/personas/market-implied.md]
tags: [polymarket, resolution-criteria, binance, btc]
---

# Summary

This source establishes the exact contract mechanics and current market-implied pricing for the $72k threshold outcome.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16, 2026 has a final close strictly above $72,000.
- The governing source of truth is Binance BTC/USDT with 1m candles, not other exchanges or pairs.
- The event end date is 2026-04-16T16:00:00Z, which matches 12:00 ET on April 16.
- The specific market slug `bitcoin-above-72k-on-april-16` showed outcome prices `["0.875", "0.125"]` at collection time, implying an 87.5% Yes probability.
- Best bid / ask were 0.87 / 0.88, so the live book was consistent with the assignment snapshot.

## Evidence directly stated by source

- Contract wording explicitly requires all of these for Yes: correct asset (BTC), correct pair (BTC/USDT), correct venue (Binance), correct candle interval (1 minute), correct timestamp (12:00 ET on April 16), and final close greater than $72,000.
- Price precision is determined by the source.

## What is uncertain

- The source does not itself provide the future settlement candle.
- It does not explain why traders are pricing 87.5%; it only shows that they are.

## Why this source may matter

This is the primary source for both market-implied probability and resolution mechanics. Because the contract is narrow and date-sensitive, correct interpretation of the source-of-truth is mandatory.

## Possible impact on the question

It makes the key analytical task clear: estimate the probability that Binance BTC/USDT remains above $72,000 at the exact noon ET 1-minute close on April 16, rather than relying on generic Bitcoin spot commentary.

## Reliability notes

High reliability for contract terms and live market price because it is the platform operating the market and exposes the event/market metadata directly. It is not independent evidence about where BTC will trade tomorrow; it is the definition of what counts and the market prior.