---
type: source_note
case_key: case-20260415-47643da0
dispatch_id: dispatch-case-20260415-47643da0-20260415T010752Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket event rules page
source_type: market_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-47643da0/researcher-analyses/2026-04-15/dispatch-case-20260415-47643da0-20260415T010752Z/personas/risk-manager.md]
tags: [polymarket, market-rules, resolution, timezone, direct-evidence]
---

# Summary

The Polymarket event page states the exact resolution mechanics for this market. The key risk-management value is clarifying that the contract is not about any exchange-average BTC price, daily close, or general April 17 trading level; it is about one exact Binance BTC/USDT 1-minute candle close at 12:00 ET on April 17.

## Key facts extracted

- The market resolves `Yes` if the Binance BTC/USDT 1-minute candle for `12:00` in ET timezone on April 17 has a final close strictly higher than `72,000`.
- Otherwise it resolves `No`.
- The source of truth is Binance, specifically the BTC/USDT trade page with `1m` and `Candles` selected.
- The market is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the number of decimal places in the source.
- On the event page at research time, the 72,000 contract was trading around 84-85% yes, matching the assignment's current_price ~0.84.

## Evidence directly stated by source

- `This market will resolve to "Yes" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title. Otherwise, this market will resolve to "No".`
- `The resolution source for this market is Binance...`
- `Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs.`

## What is uncertain

- The fetched page did not independently verify any broader Polymarket help-center guidance because the attempted help article fetch 404ed.
- There is mild operational ambiguity around how ET is displayed versus Binance timestamps, but the market text is explicit that the relevant minute is `12:00` ET.

## Why this source may matter

This is the governing contract source. It determines what conditions all must hold for a Yes resolution and sharply narrows the relevant evidence set.

## Possible impact on the question

This source reduces thesis drift. A bullish BTC view is insufficient unless BTC remains above 72,000 at the exact named minute on Binance BTC/USDT. That exact-timing dependency is the main residual risk to an otherwise high-yes stance.

## Reliability notes

- High credibility because it is the market's own published rules page.
- High relevance and recency.
- Not independent from the market being analyzed; it is the governing contract surface rather than outside confirmation.
- Essential for resolution interpretation but not for estimating underlying BTC path risk.