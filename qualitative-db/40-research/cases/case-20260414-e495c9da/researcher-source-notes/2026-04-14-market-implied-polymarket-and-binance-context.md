---
type: source_note
case_key: case-20260414-e495c9da
dispatch_id: dispatch-case-20260414-e495c9da-20260414T191806Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-e495c9da | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-19 be above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and Binance/CoinGecko spot checks
source_type: primary-market-page plus exchange/API spot verification
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-e495c9da/researcher-analyses/2026-04-14/dispatch-case-20260414-e495c9da-20260414T191806Z/personas/market-implied.md]
tags: [polymarket, binance, bitcoin, spot-price, resolution-rules]
---

# Summary

This source note captures the market-implied baseline from the Polymarket event page and a same-day verification pass of relevant spot price context from Binance API and CoinGecko.

## Key facts extracted

- The assigned market current_price is 0.895, implying roughly 89.5% for Yes.
- The Polymarket event page displayed the Apr 19 70,000 strike at about 92% Yes / 9% No at fetch time, directionally consistent with the assignment baseline though slightly higher.
- The market rules state that resolution is based on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on Apr 19, and specifically the final Close price for that candle.
- A read-only Binance API spot check returned BTCUSDT around 74,326.5 on 2026-04-14.
- A CoinGecko spot check returned BTC around 74,366 USD on 2026-04-14, broadly corroborating the Binance level.
- With BTC trading roughly 6% above the 70,000 threshold five days before resolution, the market does not require a new rally; it requires avoiding a drawdown of more than about 4.3k by noon ET on Apr 19.

## Evidence directly stated by source

From Polymarket page:
- The event title and strike ladder for Apr 19 were present.
- Rules: Yes resolves if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr 19 has a final Close above 70,000.
- Resolution source: Binance BTC/USDT, not another exchange or pair.

From Binance API check:
- `ticker/price?symbol=BTCUSDT` returned price 74326.50000000.
- Recent 1-minute klines showed BTCUSDT trading in the 74.26k-74.34k area during the check.

From CoinGecko API check:
- `simple/price?ids=bitcoin&vs_currencies=usd` returned 74366 USD.

## What is uncertain

- The Polymarket event page may lag slightly from the assigned `current_price` field, so the precise market-implied percentage at the minute of assignment could differ by a couple points.
- Spot checks do not directly answer the resolution question because several days remain and BTC is volatile.
- CoinGecko is contextual because the contract resolves only on Binance BTC/USDT.

## Why this source may matter

It establishes both the governing settlement mechanics and the live distance between current BTC spot and the 70,000 threshold. That is central to interpreting whether the market's high probability is justified.

## Possible impact on the question

The market’s high Yes probability looks understandable if traders are mostly pricing current spot distance to strike plus the absence of any obvious immediate negative catalyst. But because the contract is narrow and time-specific, the main residual risk is a several-day drawdown, exchange-specific print difference, or intraday timing mismatch at exactly noon ET.

## Reliability notes

- Polymarket is the direct primary source for contract wording and one live view of market pricing, but not the formal settlement source.
- Binance is the governing source of truth for resolution, making it the most important source for mechanics and relevant market level.
- CoinGecko is independent contextual verification of the broader BTC price region, useful but not settlement-authoritative.
- Evidence independence is moderate: Polymarket price and Binance spot are related through the same underlying market, but they serve different roles (crowd probability vs governing price source).