---
type: source_note
case_key: case-20260413-de71fc13
dispatch_id: dispatch-case-20260413-de71fc13-20260413T130158Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-13
question: Will the Binance BTC/USDT 1m candle for 2026-04-13 12:00 ET close above 68000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance spot klines API and Polymarket market rules page
source_type: primary-plus-context
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m ; https://polymarket.com/event/bitcoin-above-on-april-13
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-de71fc13/researcher-analyses/2026-04-13/dispatch-case-20260413-de71fc13-20260413T130158Z/personas/variant-view.md]
tags: [binance, polymarket, settlement, timing, source-note]
---

# Summary

This source check paired the contract wording on Polymarket with direct Binance spot 1-minute kline queries to verify what the governing source of truth is and whether the relevant noon ET candle is already observable.

## Key facts extracted

- Polymarket says the market resolves from the Binance BTC/USDT 1 minute candle for `12:00` in ET timezone, using the final `Close` price.
- At research time around 09:02-09:03 ET on 2026-04-13, Binance API responses showed BTC/USDT already trading around 70.9k-71.2k.
- Direct kline queries returned valid candles for 08:00 ET and 09:00 ET.
- Direct kline queries for 10:00 ET, 11:00 ET, and 12:00 ET returned no rows yet, which is expected because those candles had not occurred yet.

## Evidence directly stated by source

- Polymarket rules page: yes if the Binance BTC/USDT 12:00 ET 1-minute candle has a final close above 68,000; otherwise no.
- Binance API returned:
  - 08:00 ET candle close `70888.27`
  - 09:00 ET candle close `71110.83`
- Latest live-adjacent 1-minute Binance API prints during the check were in the low 71k area.

## What is uncertain

- The noon ET candle itself was not yet observable at research time.
- Binance web UI wording on the rules page refers to manual chart inspection, while the API provides the same underlying kline structure but I did not verify the exact noon candle in the UI because it was not yet formed.
- A sharp intraday move, exchange disruption, or source-handling edge case before noon could still change resolution.

## Why this source may matter

It directly establishes both the contract mechanics and the current price buffer versus the 68k threshold. It also shows why this market is not literally settled yet even if spot is already comfortably above threshold.

## Possible impact on the question

The source supports a strong `Yes` lean because BTC was already more than 3k above the threshold hours before settlement. The main variant caveat is operational/contractual: traders may treat the market as effectively done before the actual governing candle exists, so the residual risk is concentrated in the remaining time window and in source-of-truth mechanics rather than in normal small price noise.

## Reliability notes

- Binance is the named governing source of truth, so source-of-truth relevance is high.
- Polymarket is authoritative for the contract wording but not the underlying price feed itself.
- Evidence independence is only medium because the market rules and Binance source are contractually linked rather than independent observational systems.