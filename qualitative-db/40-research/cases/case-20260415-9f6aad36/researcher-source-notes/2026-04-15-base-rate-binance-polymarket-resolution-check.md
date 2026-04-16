---
type: source_note
case_key: case-20260415-9f6aad36
dispatch_id: dispatch-case-20260415-9f6aad36-20260415T082436Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-9f6aad36 | base-rate
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT 1m market data API and Polymarket market rules page
source_type: exchange API + market rules
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1000
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-9f6aad36/researcher-analyses/2026-04-15/dispatch-case-20260415-9f6aad36-20260415T082436Z/personas/base-rate.md]
tags: [source-note, bitcoin, btc, binance, polymarket, resolution]
---

# Summary

Direct source check of the governing market mechanics and the live Binance BTC/USDT 1-minute data surface suggests the market is fundamentally about whether BTC can avoid a drawdown below 72,000 by the specific settlement minute, not about a long-run directional call. As of the run time, BTC/USDT is trading around the high-73k area and the latest available 1-minute closes in the fetched sample are all above 72,000.

## Key facts extracted

- Polymarket rules say the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final Close strictly higher than 72,000.
- The rules explicitly use Binance BTC/USDT, not other exchanges or other BTC pairs.
- ET noon on 2026-04-16 converts to 16:00 UTC.
- A direct Binance API pull during this run returned recent BTCUSDT 1-minute candles with closes in the mid/high 73k range; a 1000-minute sample showed min close 73,566, max close 75,662.69, latest close 73,970.88, and 100% of sampled 1-minute closes above 72,000.
- Binance ticker endpoint during the run returned BTCUSDT spot price 73,977.13.

## Evidence directly stated by source

- Polymarket states the governing source of truth is Binance, specifically the BTC/USDT Close price for the 1-minute candle labeled 12:00 ET on the date in the title.
- Binance API returned raw klines and live spot ticker data directly from the named resolution venue.

## What is uncertain

- The fetched Binance sample covers the most recent 1000 minutes, not the actual settlement minute, which is still in the future.
- Binance website rendering itself was not fetched cleanly via the text extractor, so the API was used as the closest direct machine-readable Binance surface.
- Intraday BTC volatility could still push the settlement-minute close below 72,000 before resolution.

## Why this source may matter

This is the governing source pair for the contract: Polymarket defines the rule, and Binance provides the actual underlying price series used for settlement.

## Possible impact on the question

Because current BTCUSDT is already materially above the threshold, the base-rate question is mostly about the frequency of >~2.6% downside moves before the exact settlement minute rather than whether BTC can newly reach 72,000. That framing supports a high Yes baseline but not certainty.

## Reliability notes

- Polymarket rules page is direct for contract interpretation but not itself the future settlement print.
- Binance API is direct for venue data and likely more auditable than scraped page text for current-state verification.
- Evidence independence is only moderate because both points concern the same contract/venue stack rather than two unrelated market data providers.