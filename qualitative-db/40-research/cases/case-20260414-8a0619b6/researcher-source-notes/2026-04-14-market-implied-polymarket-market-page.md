---
type: source_note
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-18
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 70000 on 2026-04-18?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page for Bitcoin above ___ on April 18
source_type: prediction_market_listing_and_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-18
source_date: 2026-04-14
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
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8a0619b6/researcher-analyses/2026-04-14/dispatch-case-20260414-8a0619b6-20260414T194140Z/personas/market-implied.md]
tags: [source-note, polymarket, resolution-rules, btc]
---

# Summary

This source establishes both the market-implied baseline and the contract mechanics. The relevant outcome shows the 70,000 line trading around 90%, and the page states the market resolves from the Binance BTC/USDT 1-minute candle at 12:00 ET on April 18, using the final candle close.

## Key facts extracted

- The 70,000 threshold outcome was displayed at roughly 90% on the page at capture time.
- The title/date context is April 18, 2026.
- Resolution is based on the Binance BTC/USDT pair, not other exchanges or pairs.
- The relevant timestamp is the 12:00 ET 1-minute candle.
- The settlement condition is the final candle close being higher than 70,000.
- Price precision is governed by the precision shown in the source.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- The visible ladder showed 70,000 at about 90%.

## What is uncertain

- The web-fetched market page is a rendered consumer page, so it is useful for visible pricing and rules language but not an official exchange API record.
- Intraday probabilities can move materially before the contract resolves.

## Why this source may matter

It is the governing public market interface for both the implied probability and the resolution wording. For a date-specific, source-specific crypto contract, this source defines what counts.

## Possible impact on the question

This source anchors the market-implied view near 90% and narrows the question to a precise operational test: Binance BTC/USDT, 12:00 ET, April 18, final 1-minute close > 70,000.

## Reliability notes

Useful and necessary for contract interpretation, but not fully independent from market sentiment because it is the market itself. It should be paired with direct Binance price data and at least one contextual market price source.