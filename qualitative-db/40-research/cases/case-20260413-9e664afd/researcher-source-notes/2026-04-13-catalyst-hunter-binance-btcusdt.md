---
type: source_note
case_key: case-20260413-9e664afd
dispatch_id: dispatch-case-20260413-9e664afd-20260413T164930Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: binance-btcusdt-spot-and-contract-source
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-14 close above 70000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance spot API plus market rules as surfaced by Polymarket
source_type: primary_market_data_and_resolution_rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9e664afd/researcher-analyses/2026-04-13/dispatch-case-20260413-9e664afd-20260413T164930Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, resolution-source, btc, intraday]
---

# Summary

This source note captures the governing resolution mechanics and a direct spot-price check from Binance, which is the named source of truth for the market.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance BTC/USDT **1 minute candle for 12:00 ET on 2026-04-14**, specifically the final **Close** price.
- The market resolves Yes only if that close is **higher than 70000**.
- The market is about **Binance BTC/USDT**, not other exchanges or pairs.
- On 2026-04-13 around 12:50 ET, Binance public API returned BTCUSDT spot price around **72200-72275**.
- Binance recent 1-minute klines at the same check showed closes clustered around **72235-72405**, materially above 70000.

## Evidence directly stated by source

- Binance API ticker endpoint returned live BTCUSDT prices above 72000 during the verification window.
- Binance API 1-minute kline endpoint returned recent minute closes above 72000.
- Polymarket market page explicitly names Binance BTC/USDT 1m candle close at 12:00 ET as the governing source of truth.

## What is uncertain

- The exact 12:00 ET close on 2026-04-14 is still future and could differ materially from current spot.
- Public API output is a practical verification surface but the market text points users to the Binance trading interface candlestick display as the resolution surface.
- A sharp BTC drawdown over the next ~23 hours remains possible even if not currently indicated by this snapshot.

## Why this source may matter

This is the most important direct source because it both defines what counts for settlement and shows the current state relative to the threshold.

## Possible impact on the question

If Binance BTC/USDT is already trading roughly 3%+ above 70000 with less than one day left, the market should stay heavily Yes unless a material negative catalyst or exchange-specific pricing issue emerges before noon ET on 2026-04-14.

## Reliability notes

- Binance is the named resolution source, so source-of-truth relevance is high.
- API and web-interface surfaces may differ in presentation, but both reflect Binance market data.
- Reliability risk is not zero because the contract depends on a single venue and a single one-minute closing print.