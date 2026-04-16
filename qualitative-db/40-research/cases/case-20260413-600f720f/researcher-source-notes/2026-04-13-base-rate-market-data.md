---
type: source_note
case_key: case-20260413-600f720f
dispatch_id: dispatch-case-20260413-600f720f-20260413T233138Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: market-data
entity: btc
topic: will-bitcoin-reach-76k-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-13
source_name: CoinGecko BTC range data and Binance daily candle
source_type: market data APIs
source_url: https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from=1776038400&to=1776643200
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-600f720f/researcher-analyses/2026-04-13/dispatch-case-20260413-600f720f-20260413T233138Z/personas/base-rate.md]
tags: [coingecko, binance, btc, source-note]
---

# Summary

Independent market-data pulls show BTC traded well below $76,000 during the relevant observed period so far. A CoinGecko range query over Apr 13-20 UTC showed a maximum observed price of about $74,724.44, and Binance's daily candle for 2026-04-13 showed a high of $74,900.00.

## Key facts extracted

- CoinGecko range query covering Apr 13-20 2026 UTC returned 282 BTC/USD datapoints.
- Maximum observed CoinGecko price in that pull: about $74,724.44 at 2026-04-13T23:24:57Z.
- Minimum observed CoinGecko price in that pull: about $70,627.41.
- Binance daily candle for 2026-04-13 UTC: open 70,741.56; high 74,900.00; low 70,566.99; close 74,638.01.
- Those two independent contextual sources both show BTC materially below the $76,000 threshold as of the assignment-time verification pass.

## Evidence directly stated by source

- CoinGecko directly reports time-stamped BTC/USD prices within the requested date range.
- Binance directly reports the day's BTCUSDT candle high of 74,900.

## What is uncertain

- These are contextual pricing sources, not necessarily the exact settlement source Polymarket will use.
- Binance BTCUSDT is not identical to all possible BTC/USD settlement references.
- Weekly markets can still resolve YES later if the threshold is reached after this snapshot.

## Why this source may matter

This provides the key outside-view anchor: threshold-touch contracts only resolve YES if spot actually reaches the level, and the available observed data show BTC still about $1.1k to $1.3k below the target at verification time.

## Possible impact on the question

Given BTC had not yet reached $76,000 in the checked data, a 75% implied probability looks aggressive unless there is strong reason to expect a further near-term upward extension within the same week.

## Reliability notes

Strong for contextual price-state verification and evidence independence because CoinGecko aggregation and Binance exchange data are separate operational sources. Still not the final settlement source, so they are best treated as high-value contextual evidence rather than conclusive direct settlement evidence.