---
type: source_note
case_key: case-20260415-f07c9e26
dispatch_id: dispatch-case-20260415-f07c9e26-20260415T013036Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-f07c9e26 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API (BTCUSDT ticker, 1m klines, exchangeInfo, 24hr stats)
source_type: exchange api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-f07c9e26/researcher-analyses/2026-04-15/dispatch-case-20260415-f07c9e26-20260415T013036Z/personas/risk-manager.md]
tags: [binance, btcusdt, source-note, direct-source]
---

# Summary

This source note captures direct exchange data from Binance, the named source of truth in the contract.

## Key facts extracted

- Binance ticker price for BTCUSDT at collection time was `74668.60000000`.
- Recent 1-minute klines around collection time show BTC/USDT trading in the mid-74.6k range, well above the 72,000 threshold.
- Binance exchangeInfo for BTCUSDT shows symbol status `TRADING` and price tick size `0.01000000`, confirming two-decimal precision on the spot market.
- Binance 24hr stats showed last price `74668.60000000`, 24h high `76038.00000000`, 24h low `73795.47000000`, and weighted average price `74759.85572781`.
- A timezone check maps the relevant contract timestamp `2026-04-16 12:00:00 ET` to `2026-04-16 16:00:00 UTC`, with target candle open time `1776355200000` ms.
- Recent daily klines show BTCUSDT closes of approximately 71.8k, 73.0k, 73.0k, 70.7k, 74.4k, 74.1k, and current partial day around 74.7k, indicating the market has been trading above 72k on most recent days but with at least one recent sharp downside move to the low 70k range intraday.

## Evidence directly stated by source

- Binance directly reports the current BTCUSDT last price and recent 1-minute and daily kline values.
- Binance directly defines market precision through `PRICE_FILTER.tickSize`.
- Binance directly provides the recent 24-hour trading range relevant to path-risk assessment.

## What is uncertain

- The contract resolves on the final close of the Binance 1-minute candle at 12:00 ET on April 16, not on the current price or on any average price.
- Binance direct API data collected now cannot by itself rule out a >$2.6k downside move before the resolution minute.
- The Polymarket wording references the Binance trading UI candle display rather than the public API, so there remains modest implementation ambiguity about whether the UI and API could ever diverge due to display/latency issues, though that appears low risk.

## Why this source may matter

This is the governing direct source class for settlement and the clearest available evidence on current distance from the threshold, precision, and immediate volatility envelope.

## Possible impact on the question

The direct Binance data strongly supports a high probability that BTC remains above 72,000 by the relevant noon ET minute, but it also shows that the margin over the threshold is only about 3.7% and therefore still vulnerable to a meaningful but not extraordinary crypto move over roughly 14.5 hours.

## Reliability notes

High reliability for direct market state because Binance is the named settlement source. Residual risk comes from contract implementation details around the exact UI candle close and from normal crypto volatility rather than source credibility.