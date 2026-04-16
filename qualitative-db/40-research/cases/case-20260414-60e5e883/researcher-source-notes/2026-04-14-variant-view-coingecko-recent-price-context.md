---
type: source_note
case_key: case-20260414-60e5e883
dispatch_id: dispatch-case-20260414-60e5e883-20260414T190542Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: markets
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: reliability
date_created: 2026-04-14
source_name: CoinGecko Bitcoin recent daily price history
source_type: market data aggregator / contextual source
source_url: https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=daily
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-60e5e883/researcher-analyses/2026-04-14/dispatch-case-20260414-60e5e883-20260414T190542Z/personas/variant-view.md]
tags: [coingecko, bitcoin, context, volatility]
---

# Summary

CoinGecko recent daily price history provides independent contextual evidence that BTC has traded on both sides of the $70,000 region during April, but has recently moved materially above it.

## Key facts extracted

- Recent daily prices from April 1 to April 14 were approximately:
  - Apr 1: 68.2k
  - Apr 2: 68.1k
  - Apr 3: 66.9k
  - Apr 4: 66.9k
  - Apr 5: 67.3k
  - Apr 6: 69.0k
  - Apr 7: 68.9k
  - Apr 8: 72.0k
  - Apr 9: 71.1k
  - Apr 10: 71.8k
  - Apr 11: 73.0k
  - Apr 12: 73.1k
  - Apr 13: 70.8k
  - Apr 14: about 74.5k intraday snapshot / 74.3k near fetch time
- The series shows BTC was below 70k in early April, moved above 70k on April 8, briefly pulled back near 70.8k on April 13, and rebounded above 74k on April 14.

## Evidence directly stated by source

- CoinGecko directly reports recent BTC/USD price observations over time.
- The sequence directly shows recent volatility around the relevant threshold region.

## What is uncertain

- CoinGecko is not the settlement source; the contract settles on Binance BTC/USDT specifically.
- Daily data smooths away intraday drawdowns and does not answer the exact noon ET minute-close question.
- Cross-venue prices can differ modestly from Binance BTCUSDT.

## Why this source may matter

This source helps test whether the market may be overconfident simply because spot is currently above strike. The recent path shows BTC can move several thousand dollars over days and was still near the threshold one day before research time.

## Possible impact on the question

The context supports a Yes-lean but also strengthens the variant caution: a market priced around 92.5% may be underweighting short-horizon volatility and exact-minute settlement risk, because BTC only recently cleared the strike by a comfortable margin and still experienced a near-threshold day on April 13.

## Reliability notes

Good independent contextual source for recent path and volatility regime. Not authoritative for settlement. Best used alongside Binance primary-source evidence, not instead of it.