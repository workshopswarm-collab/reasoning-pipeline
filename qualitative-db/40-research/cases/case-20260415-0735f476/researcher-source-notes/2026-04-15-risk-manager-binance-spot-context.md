---
type: source_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-market
entity: btc
topic: Current BTC level versus 70000 threshold
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT API ticker and recent 1m klines with cross-checks
source_type: exchange_market_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: supportive
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/risk-manager.md
tags: [binance, coinbase, coingecko, spot-price, context]
---

# Summary

Current spot and recent minute-level data place BTC comfortably above the 70,000 threshold several days before the April 20 noon ET resolution point, but this remains contextual rather than dispositive because the contract is about one future minute close on Binance.

## Key facts extracted

- Binance spot ticker returned BTCUSDT price 74,670.53.
- Recent Binance 1-minute klines sampled around the check also showed closes in the 74,650-74,717 range.
- CoinGecko cross-check returned BTC at 74,712 USD.
- Coinbase cross-check returned BTC-USD spot at 74,653.785.
- All checked venues were materially above 70,000 at the time of review.

## Evidence directly stated by source

Observed directly from API responses on 2026-04-15:
- Binance ticker: {"symbol":"BTCUSDT","price":"74670.53000000"}
- Binance recent klines included closes such as 74716.52, 74671.57, 74650.01, 74676.96, 74667.05.
- CoinGecko: {"bitcoin":{"usd":74712}}
- Coinbase: {"data":{"amount":"74653.785","base":"BTC","currency":"USD"}}

## What is uncertain

- These checks do not prove what the Binance 12:00 ET 1-minute candle close will be on April 20.
- Short-dated crypto moves can be large enough that a several-thousand-dollar drawdown before the deadline remains plausible.
- Coinbase BTC-USD and CoinGecko BTC/USD are contextual only; they are not governing sources for settlement.

## Why this source may matter

This is the core direct-context evidence for why the market is priced as a strong Yes favorite. BTC is not marginally above the threshold; it currently sits roughly 6.6% above it.

## Possible impact on the question

This evidence supports a high Yes probability, but it also clarifies the main risk-manager caution: current price level is useful only if it persists through the exact future Binance minute close. A sizeable downside move before noon ET on April 20 would still flip the outcome to No.

## Reliability notes

High-quality near-real-time exchange data. Binance is directly relevant because it is the governing exchange, though the sampled data are not yet the resolution candle. Coinbase and CoinGecko provide independent contextual confirmation of broad market level but not settlement authority.