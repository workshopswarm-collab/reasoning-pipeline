---
type: source_note
case_key: case-20260416-b80742d2
dispatch_id: dispatch-case-20260416-b80742d2-20260416T014833Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: spot-market-structure
entity: xrp
topic: XRP > $1.30 on Apr 19 Polymarket resolution mechanics and live Binance spot context
question: Will the Binance XRP/USDT 12:00 ET 1-minute candle close on 2026-04-19 be above 1.30?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance spot API docs and live Binance endpoints
source_type: primary-plus-contextual
source_url: https://polymarket.com/event/xrp-above-on-april-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [xrp]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-b80742d2/researcher-analyses/2026-04-16/dispatch-case-20260416-b80742d2-20260416T014833Z/personas/market-implied.md]
tags: [polymarket, binance, xrp, settlement-mechanics, timezone, spot-price]
---

# Summary

This source bundle establishes both the contract mechanics and the current spot context most relevant to the market-implied view. Polymarket states that resolution depends on the Binance XRP/USDT 1-minute candle labeled 12:00 in ET on April 19, using the final Close price, with precision determined by Binance. Binance's own spot API docs confirm that `/api/v3/klines` and `/api/v3/uiKlines` provide 1-minute candlestick close prices and allow timezone interpretation for interval labeling, while live Binance spot endpoints currently show XRP/USDT around 1.4018 and a 24-hour high of 1.4086.

## Key facts extracted

- Polymarket rules explicitly say the market resolves Yes if the Binance XRP/USDT 12:00 ET 1-minute candle has a final Close above 1.30 on April 19, 2026.
- The relevant source of truth is Binance, not another exchange or another XRP pair.
- Binance market-data docs say klines are available at `/api/v3/klines` and are identified by open time, with `interval=1m` and optional `timeZone` parameter support.
- Binance docs note that if `timeZone` is provided, kline intervals are interpreted in that timezone, while `startTime` and `endTime` remain UTC.
- Live Binance ticker endpoint returned XRPUSDT last price `1.40180000` at retrieval time.
- Live Binance 24-hour ticker returned weighted average price `1.37782565`, high `1.40860000`, low `1.35030000`, and last price `1.40180000`.
- Live Binance 1-minute klines and uiKlines around retrieval time were also closing around `1.40180000`.

## Evidence directly stated by source

- Polymarket directly states the resolution rule and named resolution source.
- Binance directly states the API mechanics for klines, including timeZone handling and the meaning of the returned close field.
- Binance live endpoints directly state the observed live market prices at retrieval time.

## What is uncertain

- The market resolves on April 19 at noon ET, so the current April 15/16 spot level does not settle the contract.
- It remains possible for XRP/USDT to trade below 1.30 by the relevant noon ET minute despite currently trading well above that threshold.
- The public-facing Binance web UI may display the relevant candle through charting infrastructure that is not perfectly identical to raw REST retrieval formatting, though the close field definition is aligned.

## Why this source may matter

This bundle provides the direct rules-and-mechanics foundation needed to avoid a sloppy “XRP is above 1.30 now, so Yes is certain” inference. It also gives the most direct current evidence for why the market is pricing Yes at an extreme level: spot is already materially above the strike with meaningful 24-hour cushion.

## Possible impact on the question

The source bundle strongly supports the market’s current Yes-heavy pricing as directionally sensible. If XRP/USDT is already around 1.40 and the contract only needs the noon ET 1-minute close on April 19 to remain above 1.30, then the embedded market assumption is that a roughly 7%+ drawdown over the next few days is possible but not the base case.

## Reliability notes

- Polymarket is the direct contract-specification source, so reliability for settlement wording is high.
- Binance is the named source of truth and also the direct source for live spot data, so reliability for mechanics and current price context is high.
- Independence is only medium because both the resolution mechanics and live price evidence ultimately route through Binance, but that is appropriate here because Binance is the governing source of truth.