---
type: source_note
case_key: case-20260415-10579f0a
dispatch_id: dispatch-case-20260415-10579f0a-20260415T184424Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-10579f0a | market-implied
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 70000 on April 17, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API + Polymarket event rules + spot cross-checks
source_type: mixed_primary_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-17 ; https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd ; https://api.coinbase.com/v2/prices/BTC-USD/spot
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-10579f0a/researcher-analyses/2026-04-15/dispatch-case-20260415-10579f0a-20260415T184424Z/personas/market-implied.md]
tags: [binance, polymarket, btc, market-implied, resolution-source]
---

# Summary

The core direct evidence is that Binance spot BTC/USDT was already trading materially above $70,000 on April 15, 2026, while the Polymarket contract resolves from the Binance BTC/USDT 12:00 ET one-minute candle close on April 17. Independent context checks from CoinGecko and Coinbase showed BTC/USD around the same mid-$74k area, supporting the market's very high implied probability that BTC remains above $70k by the resolution timestamp.

## Key facts extracted

- Polymarket rules say the market resolves to Yes if the Binance BTC/USDT 12:00 ET one-minute candle on April 17 has a final close price strictly higher than 70,000.
- Polymarket displayed the April 17 "70,000" line around 97% Yes on fetch.
- Binance ticker endpoint returned BTCUSDT price `74294.01000000` on April 15.
- Binance recent one-minute klines also showed closes in the `74262` to `74311` range.
- CoinGecko simple price returned Bitcoin at `74303` USD.
- Coinbase spot returned BTC-USD at `74369.435`.

## Evidence directly stated by source

- Direct authoritative-style contract text from the market page identifies Binance BTC/USDT, the 12:00 ET one-minute candle, and the need for a final close above the threshold.
- Direct exchange data from Binance indicates the relevant underlying was roughly 6% above the threshold with about two days remaining.
- Contextual spot checks from CoinGecko and Coinbase indicate no obvious exchange-specific dislocation large enough to undermine the general price regime.

## What is uncertain

- This does not directly settle the April 17 noon print because BTC can move materially in ~44 hours.
- Binance API spot price and recent klines are direct for the underlying exchange, but not yet the exact future resolution candle.
- Cross-exchange context does not eliminate the possibility of a sharp drawdown or Binance-specific anomaly at the exact resolution minute.

## Why this source may matter

This source bundle covers the two most important questions for a market-implied researcher: what exactly resolves the contract, and whether current public price evidence justifies the market's extreme confidence. Here it largely does.

## Possible impact on the question

The source bundle supports a high Yes probability because the market only needs BTC/USDT on Binance to remain above 70,000 by noon ET on April 17, and the current spot regime is already several thousand dollars above that threshold. The main residual risk is a short-horizon drawdown or exchange-specific print issue, not ordinary ambiguity about the contract.

## Reliability notes

- Binance is the governing source of truth for resolution, so its API and exchange surface carry the most weight.
- Polymarket rules are authoritative for contract interpretation but not for the underlying price level.
- CoinGecko and Coinbase are useful independent contextual checks, though neither governs settlement.
- Evidence independence is medium: all price sources reflect the same global BTC market, but Binance versus Coinbase/CoinGecko still gives a useful sanity check against a single-surface read error.
