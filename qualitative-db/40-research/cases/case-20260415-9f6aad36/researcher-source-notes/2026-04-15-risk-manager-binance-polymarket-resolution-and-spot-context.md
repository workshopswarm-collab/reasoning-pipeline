---
type: source_note
case_key: case-20260415-9f6aad36
dispatch_id: dispatch-case-20260415-9f6aad36-20260415T082436Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-9f6aad36 | risk-manager
question: Will the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance public API
source_type: primary_market_rule plus primary_exchange_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-9f6aad36/researcher-analyses/2026-04-15/dispatch-case-20260415-9f6aad36-20260415T082436Z/personas/risk-manager.md]
tags: [polymarket, binance, resolution, btc, source-note]
---

# Summary

This source note captures the contract mechanics from the Polymarket market page and direct Binance price context from Binance public API surfaces.

## Key facts extracted

- Polymarket states the market resolves to "Yes" if the Binance BTC/USDT 1-minute candle for **12:00 in ET timezone (noon)** on the date in the title has a final **Close** price higher than 72,000.
- Polymarket states the resolution source is Binance BTC/USDT with **"1m" and "Candles" selected**, not another exchange or pair.
- Price precision is determined by the number of decimals on the Binance source.
- Binance public ticker API showed BTCUSDT spot at **73970.88** at fetch time on 2026-04-15.
- Binance 1-minute klines fetched near the research time showed recent closes clustered around **73915-73974**, well above 72,000.
- Binance server time endpoint returned **1776240791525**, confirming current exchange time was accessible from a direct exchange-controlled endpoint during the run.

## Evidence directly stated by source

From Polymarket rules:
- Resolution depends on the **Binance 1-minute candle close** at **12:00 PM ET on April 16**.
- All material conditions must hold for Yes:
  1. source is Binance,
  2. pair is BTC/USDT,
  3. interval is 1 minute,
  4. relevant candle is the 12:00 PM ET candle on April 16,
  5. final close price is strictly **higher than 72,000**.

From Binance API:
- BTCUSDT spot was materially above 72,000 during this run.
- Recent 1-minute candles were also materially above 72,000 during this run.

## What is uncertain

- This source set does not itself determine where BTC will be at the exact resolution candle tomorrow.
- Public API access confirms current exchange data surfaces, but the final settlement surface referenced by Polymarket is the Binance trading chart/candle view, not this note's API snapshot.
- Exchange operational issues, sharp intraday volatility, or a fast risk-off move before noon ET on April 16 could still flip the outcome.

## Why this source may matter

This is the governing source-of-truth pair for the case: Polymarket defines the contract and Binance defines the settlement observation. Direct verification of both sharply reduces contract-interpretation risk.

## Possible impact on the question

The source set supports a bullish baseline because current exchange price is around 2.7% above the threshold. It also highlights the main residual risk: the market can still fail if BTC falls below 72,000 by the precise settlement minute or if operational/source interpretation issues arise around the relevant candle.

## Reliability notes

- Polymarket is authoritative for market rules but not for the future underlying price.
- Binance is authoritative for the underlying settlement observation specified by the market.
- Evidence independence is moderate rather than high because the contextual market view and the ultimate settlement source are tightly linked to the same crypto venue ecosystem.
- Main remaining uncertainty is timing/path risk rather than source credibility.