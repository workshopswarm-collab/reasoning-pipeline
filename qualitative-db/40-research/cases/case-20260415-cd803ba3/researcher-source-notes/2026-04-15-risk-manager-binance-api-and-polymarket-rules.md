---
type: source_note
case_key: case-20260415-cd803ba3
dispatch_id: dispatch-case-20260415-cd803ba3-20260415T203927Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-price
entity: btc
topic: case-20260415-cd803ba3 | risk-manager
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API plus Polymarket market rules page
source_type: primary-plus-market-rules
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-cd803ba3/researcher-analyses/2026-04-15/dispatch-case-20260415-cd803ba3-20260415T203927Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution-source, timing-risk]
---

# Summary

This source note captures the two most important direct inputs for this case: Polymarket's contract wording and recent Binance BTC/USDT 1-minute data from the public API, used as a proxy for the Binance candle data the contract explicitly names.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for **12:00 ET on April 17, 2026** has a final **Close** strictly above 74,000.
- The market is specifically about **Binance BTC/USDT**, not other exchanges or pairs.
- Recent Binance API reads on 2026-04-15 showed BTC/USDT around **74.75k**, with recent 1-minute closes including **74637.82, 74694.82, 74730.09, 74768.01, 74751.69**.
- The threshold is therefore only modestly below the spot area observed roughly 44 hours before resolution.

## Evidence directly stated by source

- Polymarket rules directly state the governing market condition and source of truth.
- Binance API directly states recent BTC/USDT prices and minute closes.

## What is uncertain

- The official resolution source is the Binance trading interface candle display; the API is highly likely but not perfectly guaranteed to mirror any UI-specific finalization quirks.
- There is still substantial time until the relevant 12:00 ET candle on April 17, so current prices are only contextual, not settling evidence.
- BTC can move more than 1-2% over a short window, so being above threshold now does not guarantee being above threshold at the exact resolving minute.

## Why this source may matter

This is the core source pair for the case because it defines both the exact contract mechanic and the current distance from the strike. For a narrow time-specific BTC level market, the main risk is not interpreting macro thesis incorrectly; it is underestimating exact-timestamp and exchange-specific path risk.

## Possible impact on the question

The direct evidence modestly supports Yes because current Binance BTC/USDT is above 74,000. But the same source pair also highlights the main downside risk: the market resolves on one exact minute close, so short-term volatility and exchange-specific prints can still flip the outcome.

## Reliability notes

- Polymarket market page is authoritative for the contract wording but not the final BTC print itself.
- Binance is the stated resolution source; its public API is a strong direct proxy for the named source, though the contract names the Binance trading interface candle display specifically.
- Independence between the two sources is medium rather than high because both concern the same market mechanism rather than separate information channels.