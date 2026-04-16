---
type: source_note
case_key: case-20260415-9a9c8ea3
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and Binance BTCUSDT API surfaces
source_type: primary+verification
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, resolution-source, timing, btc]
---

# Summary

This source pair establishes both the governing contract mechanics and a live spot-level check against the threshold. Polymarket states the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-16, using the candle's final Close price. Binance API verification shows BTC/USDT trading around 74.6k on 2026-04-15, comfortably above the 72k threshold with less than one day to resolution.

## Key facts extracted

- Polymarket rule: market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on the specified date has a final Close higher than 72,000.
- The rule explicitly excludes other exchanges and other trading pairs.
- The relevant deadline is 2026-04-16 12:00 PM America/New_York, which is 2026-04-16 16:00:00 UTC.
- Binance ticker verification on 2026-04-15 showed BTCUSDT spot at 74,646.39.
- Recent 1-minute klines around the verification time also closed around 74,633 to 74,646, confirming the ticker was not a stale outlier.
- That leaves roughly a 2,646-point buffer above the strike, or about 3.7%.

## Evidence directly stated by source

- Polymarket directly states the resolution source and material conditions.
- Binance directly states live BTCUSDT price and minute-kline closes.

## What is uncertain

- The source note does not establish where BTC will trade at exactly 12:00 PM ET on 2026-04-16.
- A sharp downside move before the noon ET candle could still flip the result.
- Public web fetches do not independently verify Binance frontend display mechanics, only the exchange API and Polymarket rule text.

## Why this source may matter

This is the core settlement and timing evidence. For a narrow date-specific crypto threshold market, the most important catalyst is simply whether there is any credible near-term event or volatility regime shift large enough to erase a ~3.7% cushion before the exact settlement minute.

## Possible impact on the question

The source pair supports a high-probability Yes lean because the threshold is already in the money by a meaningful but not invulnerable margin, and the governing source of truth is clear enough to narrow the question to one thing: can BTC/USDT on Binance lose more than ~3.7% by noon ET tomorrow?

## Reliability notes

- Polymarket is authoritative for contract wording but not for final underlying price.
- Binance is authoritative for the underlying price because the contract explicitly names Binance BTC/USDT as the resolution source.
- Evidence independence is moderate rather than high because the two sources are contract-plus-underlying, not two separate market forecasts.
- Operational/source ambiguity is low to medium: the named source is clear, but there is always minor implementation risk around exact candle display/finality.