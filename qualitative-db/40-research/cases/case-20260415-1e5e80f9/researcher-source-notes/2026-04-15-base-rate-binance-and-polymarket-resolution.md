---
type: source_note
case_key: case-20260415-1e5e80f9
dispatch_id: dispatch-case-20260415-1e5e80f9-20260415T080017Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-1e5e80f9 | base-rate
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on April 16, 2026 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket contract page and Binance BTCUSDT 1m klines API
source_type: primary_and_authoritative_resolution_context
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: base-rate
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1e5e80f9/researcher-analyses/2026-04-15/dispatch-case-20260415-1e5e80f9-20260415T080017Z/personas/base-rate.md]
tags: [source-note, polymarket, binance, resolution, btc]
---

# Summary

This source set establishes both the contract mechanics and the direct price context most relevant to a short-horizon base-rate estimate.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT one-minute candle labeled 12:00 in ET on April 16, 2026 has a final close strictly above 72,000.
- The contract explicitly says the governing source is Binance BTC/USDT with 1m candles, not other exchanges or pairs.
- Polymarket showed the 72,000 line trading around 83% at the time of review.
- Binance recent 1m klines fetched on April 15 showed BTC/USDT trading around the mid-74k to low-75k range, several percent above 72,000.

## Evidence directly stated by source

- Polymarket rules directly specify the source of truth, timing condition, and strict comparison operator.
- Binance klines directly state observed minute-by-minute BTC/USDT prices on the exchange named in the contract.

## What is uncertain

- The fetched Binance sample was recent market context, not the resolving April 16 noon ET candle itself.
- Short-horizon crypto moves can still be large enough to invalidate a simple spot-anchor view.
- The public Binance trade page was not machine-readable via fetch, so the direct API kline endpoint was used for contextual verification.

## Why this source may matter

This is the most decision-relevant source pair because the market is narrow, date-sensitive, and source-sensitive. Contract interpretation matters almost as much as directional BTC view.

## Possible impact on the question

The contract mechanics are straightforward and narrow. Given BTC was already materially above 72k on Binance the day before resolution, the outside-view default becomes that a next-day noon print remains above 72k unless a meaningful downside move occurs.

## Reliability notes

- Polymarket contract text is high-value for rules and source-of-truth interpretation, though it is not itself the settlement print.
- Binance API market data is a direct exchange source and is more reliable for actual price context than third-party summaries.
- Independence is limited because both sources are tied to the same market structure, but they answer different parts of the problem: rules vs observed price level.
