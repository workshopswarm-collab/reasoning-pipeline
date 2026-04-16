---
type: source_note
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket rules page plus Binance API verification
source_type: primary_contract_plus_primary_market_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: risk-manager
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3d3080df/researcher-analyses/2026-04-15/dispatch-case-20260415-3d3080df-20260415T002239Z/personas/risk-manager.md]
tags: [polymarket, binance, resolution, btc, price-threshold]
---

# Summary

This source note captures the governing contract language and a same-day verification pass on Binance BTC/USDT price context. The market resolves from a very specific source and timestamp: the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 20, using the final Close price.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance 1-minute candle for BTC/USDT at 12:00 ET on April 20 has a final Close price higher than 70,000.
- Polymarket explicitly says this is Binance BTC/USDT, not other exchanges or pairs.
- Binance API verification on 2026-04-14/15 showed BTCUSDT trading around 74.56k.
- Binance exchange info shows BTCUSDT status as TRADING and price tick size at 0.01, relevant because the contract says precision follows the source.
- Binance 1-minute kline endpoint returned recent candles successfully, confirming the contract’s operational source appears available and machine-readable.
- Independent contextual cross-check via CoinGecko also showed bitcoin near 74.6k USD at roughly the same time.

## Evidence directly stated by source

From the Polymarket rules page:
- Yes resolves if the Binance BTC/USDT 12:00 ET 1-minute candle final Close is higher than 70,000.
- Otherwise No.
- Resolution source is Binance, specifically BTC/USDT with 1m candles selected.
- Price precision is determined by the source.

From Binance API checks:
- `ticker/price?symbol=BTCUSDT` returned 74559.33.
- `klines?symbol=BTCUSDT&interval=1m&limit=2` returned recent 1-minute candles, including a close of 74559.34.
- `exchangeInfo?symbol=BTCUSDT` returned symbol metadata showing BTCUSDT actively trading and price tick size of 0.01.

## What is uncertain

- This source note does not establish what BTC/USDT will be on April 20 at exactly 12:00 ET; it only verifies current context and resolution mechanics.
- Binance web UI labeling of candle timestamps versus API UTC timestamps can still create reviewer confusion if not normalized carefully.
- Macro/news shocks over the next several days could move BTC materially even though spot is currently well above the threshold.

## Why this source may matter

This is the highest-value source cluster for the case because it pins down both the source of truth and the operational conditions required for resolution. It removes ambiguity about exchange, pair, interval, and threshold comparison.

## Possible impact on the question

The current price context supports a Yes lean because BTC/USDT is already several thousand dollars above 70,000. But the more important contribution is risk framing: the market requires all of the following to hold for Yes—Binance BTC/USDT remains the governing reference, the relevant noon-ET candle is the one used, and its final Close remains above 70,000 at the exact minute that counts.

## Reliability notes

- Polymarket rules page is authoritative for market contract interpretation.
- Binance is authoritative for the settlement data point itself.
- CoinGecko is only contextual and not a settlement source.
- Evidence independence is moderate: Binance and CoinGecko are separate sources for spot context, but only Binance matters for final settlement.