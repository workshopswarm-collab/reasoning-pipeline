---
type: source_note
case_key: case-20260415-3f432366
dispatch_id: dispatch-case-20260415-3f432366-20260415T074424Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules for Bitcoin above on April 17
source_type: market rules / resolution source description
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3f432366/researcher-analyses/2026-04-15/dispatch-case-20260415-3f432366-20260415T074424Z/personas/risk-manager.md]
tags: [polymarket, resolution-rules, binance, btc]
---

# Summary

This source establishes the contract mechanics. The market resolves Yes only if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 17 has a final close strictly higher than 72,000. This makes the case mainly about a precise timestamp, exchange-specific print, and strict threshold test rather than a looser daily-price question.

## Key facts extracted

- Resolution is tied to Binance BTC/USDT, not a cross-exchange BTC/USD composite.
- The relevant datapoint is the final close of the 1-minute candle for 12:00 ET on April 17, 2026.
- The threshold condition is strictly higher than 72,000.
- Price precision follows the decimals shown by the source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The rules do not restate whether daylight saving handling could create UI confusion, but they explicitly anchor to ET.
- The rules do not provide historical volatility context, so they cannot by themselves support a directional price probability.

## Why this source may matter

This is the governing source-of-truth description. It sharply narrows the claim: BTC can trade above 72k on other venues or at other times and still resolve No if the specified Binance minute close is 72,000 or below.

## Possible impact on the question

The exact minute-close requirement adds timing risk and exchange-specific operational/resolution risk. That pushes a risk-manager lens toward discounting overconfident takes that treat the market as equivalent to "BTC roughly above 72k that day."

## Reliability notes

Primary for contract interpretation, but not primary for the actual future price outcome. High credibility on what counts for resolution; no directional predictive power by itself.