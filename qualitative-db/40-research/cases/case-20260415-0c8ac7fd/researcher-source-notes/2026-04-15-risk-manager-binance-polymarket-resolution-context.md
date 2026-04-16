---
type: source_note
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: btc-threshold-close
entity: btc
topic: Binance BTC/USDT noon ET close-above-72000 market mechanics and current context
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT 1m klines API and Polymarket event/market metadata
source_type: mixed_primary_and_contextual
source_url: https://www.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=120
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/risk-manager.md
tags: [source-note, binance, polymarket, btc, threshold-market]
---

# Summary

This source note captures the governing source-of-truth mechanics from Polymarket plus a direct Binance 1-minute market context check relevant to the April 17 noon ET resolution.

## Key facts extracted

- Polymarket rules state the market resolves **Yes** if the **Binance BTC/USDT 1 minute candle for 12:00 ET on April 17** has a final **Close** above 72,000.
- The rules explicitly say this is about **Binance BTC/USDT**, not other exchanges or pairs.
- The market is therefore a **single-minute close-above** contract, not a touch / intraperiod-high contract.
- As of 2026-04-15 around 19:09Z-19:13Z, Binance 1-minute BTCUSDT closes were approximately **74,679.83**, **74,646.65**, **74,650.32**, **74,697.66**, and **74,703.99**.
- Over the sampled recent 120 one-minute candles, close prices ranged from about **73,931.47** to **74,703.99**.
- On the live Polymarket event surface, the April 17 **72,000** row was trading around the high-80s cents (assignment current_price 0.87; web surface displayed about 88¢).

## Evidence directly stated by source

- Polymarket directly states the governing resolution mechanics and source: Binance BTC/USDT 1-minute candle at 12:00 ET, final close price, above the stated threshold.
- Binance 1-minute kline output directly provides recent BTCUSDT open/high/low/close data in machine-readable form.

## What is uncertain

- The decisive candle has **not yet occurred**; the market does not resolve from current price alone.
- Exchange-specific volatility between now and April 17 noon ET remains material even though the spot context is comfortably above 72,000.
- I did not obtain a clean machine-readable Gamma market-row extraction for the single 72k row due endpoint friction, so the exact live market quote is taken from assignment metadata plus the public web surface rather than a standalone API extract.

## Why this source may matter

- It determines the actual settlement mechanics and avoids the common error of reasoning from the wrong exchange, wrong pair, wrong time zone, or wrong intraperiod statistic.
- It also shows that current BTC context is not marginally above 72k but several percent above it, which matters for path-risk framing.

## Possible impact on the question

- The governing source sharply narrows the real question to whether **Binance BTC/USDT 12:00 ET close on Apr 17** stays above 72,000.
- The current price cushion supports a high Yes probability, but the single-minute close mechanic leaves nontrivial downside if BTC sells off by noon ET on the 17th.

## Reliability notes

- Polymarket market rules are the authoritative contract-description source for mechanics.
- Binance is the stated governing source for the final resolving datapoint.
- Evidence independence is limited because both sources point back to the same settlement surface rather than independent causal evidence.
- This note is strong on mechanism clarity and current market context, but not on independent macro-causal explanation.