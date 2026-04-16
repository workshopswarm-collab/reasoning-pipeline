---
type: source_note
case_key: case-20260415-2cba3460
dispatch_id: dispatch-case-20260415-2cba3460-20260415T115730Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: prediction-markets
entity: btc
topic: bitcoin-above-72k-on-april-16
question: What exact conditions must hold for the Apr 16 BTC > 72k market to resolve Yes?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page rules
source_type: market rules / resolution specification
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2cba3460/researcher-analyses/2026-04-15/dispatch-case-20260415-2cba3460-20260415T115730Z/personas/variant-view.md]
tags: [polymarket, rules, resolution, source-of-truth]
---

# Summary

The Polymarket rules state that this market resolves Yes only if the Binance BTC/USDT one-minute candle for 12:00 in ET timezone on Apr 16 has a final close price higher than 72,000. The contract is narrow and depends on a single exchange, a single pair, a single one-minute candle, and a strict greater-than comparison.

## Key facts extracted

- Governing source of truth is Binance.
- Relevant instrument is BTC/USDT, not BTC/USD and not other exchanges.
- Relevant observation is the 12:00 ET one-minute candle on Apr 16.
- Relevant field is the final close price of that candle.
- The threshold condition is strictly higher than 72,000.
- Price precision is determined by the number of decimals shown by the source.

## Evidence directly stated by source

Direct rule text says the market resolves Yes if the Binance 1 minute candle for BTC/USDT 12:00 in ET timezone on the date specified in the title has a final Close price higher than the specified threshold.

## What is uncertain

- The rules text does not specify fallback handling for Binance display outages or temporary data revisions beyond naming the source.
- The web page extract does not independently validate how Binance labels the candle in UI timezones; it only states the ET interpretation in the market rule.

## Why this source may matter

This is the contract-specification source. Because the market is narrow and rule-sensitive, the exact wording materially changes what should be forecast. A daily BTC level on another venue is not sufficient.

## Possible impact on the question

The narrow mechanics slightly strengthen the bearish variant case relative to a generic "BTC above 72k tomorrow" interpretation, because a single volatile minute on one venue can miss the threshold even if BTC spends most of the day above it.

## Reliability notes

- High relevance because it is the market’s own resolution language.
- Not independent from Polymarket, but it is the authoritative contract text for what counts.
- Must be paired with a direct Binance source to evaluate the live state and operational dependency.
