---
type: source_note
case_key: case-20260415-c8d6e83e
dispatch_id: dispatch-case-20260415-c8d6e83e-20260415T151858Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the price of Bitcoin be above $68,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules snapshot
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, contract-interpretation, market-implied-probability]
---

# Summary

This source establishes both the live market-implied baseline and the exact contract mechanics. It shows the $68,000 line trading around 95-96% Yes and defines settlement as the Binance BTC/USDT 1-minute candle labeled 12:00 in ET timezone on April 20, using the final Close price.

## Key facts extracted

- The specific threshold market is "$68,000" for April 20.
- The market snapshot showed Yes around 96¢, consistent with the assignment's `current_price: 0.955`.
- The page states the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 20 has a final Close above 68,000.
- Resolution is tied to Binance BTC/USDT specifically, not other exchanges or pairs.
- Price precision is determined by Binance source formatting.

## Evidence directly stated by source

- Contract wording explicitly names Binance as source of truth.
- Contract wording explicitly names the 1-minute candle Close, not intraminute high/low or another aggregation.
- Market prices on the page imply very high confidence that BTC will still be above 68k by the relevant noon ET window.

## What is uncertain

- The public market page is not itself the final Binance data source; it only describes the source-of-truth mechanics.
- The page does not independently verify the exact timestamp mapping from ET noon to Binance candle labeling conventions, so that needs separate checking.

## Why this source may matter

This is the governing contract/rules source for interpreting what must happen for Yes to resolve. Because the case is date-sensitive and rule-sensitive, this source is mandatory.

## Possible impact on the question

The high market price sets a strong consensus baseline near 95.5%. But because the contract depends on a single one-minute Binance close at a specific time, a variant view can focus on path risk and timestamp-specific failure modes rather than only broad directional BTC sentiment.

## Reliability notes

Good for contract interpretation and market baseline, but not sufficient alone for the actual probability judgment because it is partly self-referential and not independent evidence about BTC price behavior.