---
type: source_note
case_key: case-20260414-d1f59d32
dispatch_id: dispatch-case-20260414-d1f59d32-20260414T144613Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-d1f59d32 | market-implied
question: Will the price of Bitcoin be above $74,000 on April 15?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market rules page + Binance spot/API checks + CoinGecko contextual spot check
source_type: mixed_primary_contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-14
credibility: medium-high
recency: same-day
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-d1f59d32/researcher-analyses/2026-04-14/dispatch-case-20260414-d1f59d32-20260414T144613Z/personas/market-implied.md]
tags: [polymarket, binance, btc, resolution, spot-price]
---

# Summary

This note captures the governing contract mechanics from the Polymarket market page and a same-day price-context verification from Binance API plus CoinGecko.

## Key facts extracted

- Polymarket rules say the market resolves to Yes if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET timezone on April 15 has a final Close strictly higher than 74,000.
- The governing source of truth is explicitly Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the source.
- The Polymarket page displayed the 74,000 rung at roughly 83% at fetch time, broadly consistent with the assignment’s current_price input of 0.815.
- Binance API check on 2026-04-14 around 14:48Z showed BTCUSDT around 75,366.61, i.e. about 1.85% above 74,000.
- Binance recent 1-minute klines in the same verification pass showed closes clustered around 75.27k-75.38k, reinforcing that spot was already comfortably above the contract strike one day before resolution.
- CoinGecko contextual price check was consistent at about 75,387 USD.

## Evidence directly stated by source

Direct from Polymarket rules page:
- Yes resolves if the Binance 1 minute candle for BTC/USDT 12:00 in ET timezone on the specified date has a final Close price higher than the threshold.
- Resolution source is Binance BTC/USDT with 1m Candles selected.
- The market is about Binance BTC/USDT specifically, not other exchanges or trading pairs.

Direct from Binance API:
- BTCUSDT ticker price fetched at approximately 75,366.61.
- Recent 1m closes were approximately 75,376.44; 75,270.15; 75,300.41; 75,364.94; and an in-progress line around 75,365.66.

Direct from CoinGecko:
- BTC/USD simple price was approximately 75,387.

## What is uncertain

- The contract resolves on the specific Binance 12:00 ET 1-minute candle close on April 15, not on the current April 14 spot price.
- Short-horizon BTC volatility can still move the market below 74,000 by the relevant minute.
- Web extraction from Binance’s browser page was weak, so the strongest direct Binance evidence here came from public API endpoints rather than the rendered trading UI.

## Why this source may matter

This source set establishes both the exact settlement mechanic and the current distance from the strike. For a narrow date/time crypto contract, those are the two highest-materiality inputs.

## Possible impact on the question

The evidence supports a market-respecting prior that Yes should be favored because spot is already above the strike by roughly 1.8% with less than a day to go. It does not settle the contract early, but it makes the market’s low-80s probability understandable rather than obviously stale or overextended.

## Reliability notes

- Polymarket rules page is the primary contract-definition source, but it is still a market-hosted page and not the ultimate outcome itself.
- Binance public API is highly relevant for current context because the contract keys off Binance BTC/USDT; however, current ticker/klines are contextual for today, not the actual resolving candle tomorrow.
- CoinGecko adds a lightweight independent context check that BTC is in the same price neighborhood, but it is not the governing source of truth for settlement.
