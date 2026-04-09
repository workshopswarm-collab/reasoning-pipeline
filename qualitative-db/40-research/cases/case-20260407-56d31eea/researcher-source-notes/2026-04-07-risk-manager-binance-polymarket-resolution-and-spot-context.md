---
type: source_note
case_key: case-20260407-56d31eea
dispatch_id: dispatch-case-20260407-56d31eea-20260407T023203Z
analysis_date: 2026-04-07
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: binance
topic: case-20260407-56d31eea | risk-manager
question: Will the price of Bitcoin be above $66,000 on April 7?
driver: operational-risk
date_created: 2026-04-06
source_name: Binance BTCUSDT API + Polymarket market page / gamma API
source_type: primary-plus-contextual
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [bitcoin, binance]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-56d31eea/researcher-analyses/2026-04-07/dispatch-case-20260407-56d31eea-20260407T023203Z/personas/risk-manager.md]
tags: [binance, polymarket, btcusdt, resolution-source, one-minute-candle]
---

# Summary

This source note captures the governing resolution mechanics and the live Binance context most relevant to downside risk. Polymarket’s market record explicitly says the market resolves from the Binance BTC/USDT 1-minute candle for **12:00 ET** on April 7, using the final **Close** price. Binance’s public API confirms a direct 1-minute kline surface for BTCUSDT and live spot around the mid-68k area during this run, materially above the 66k threshold.

## Key facts extracted

- Polymarket gamma market record for slug `bitcoin-above-66k-on-april-7` states:
  - question: `Will the price of Bitcoin be above $66,000 on April 7?`
  - endDate: `2026-04-07T16:00:00Z`
  - resolution description: resolves to Yes if the Binance BTC/USDT **1 minute candle** for **12:00 in ET timezone (noon)** has a final **Close** price above 66,000.
- Binance API endpoint `api/v3/klines` returns direct BTCUSDT 1-minute candles with explicit open time, close time, OHLC, and volume.
- During this research run, Binance `ticker/24hr` showed:
  - last price: `68524.94`
  - 24h low: `68273.34`
  - 24h high: `70351.46`
- Binance order book snapshot showed the market trading tightly around `68524.93` / `68524.94` at the time checked.

## Evidence directly stated by source

- The settlement source is Binance, not any average, oracle bundle, or cross-exchange consensus.
- The relevant datapoint is the **close** of a single one-minute candle, not intraminute high/low and not another exchange’s BTC price.
- Price precision is determined by Binance’s displayed/source precision.

## What is uncertain

- The future 12:00 ET candle for April 7 obviously does not yet exist at research time, so the source-of-truth does not settle the answer yet.
- The exact Binance web UI rendering path could differ from API formatting, though the market description points to the same BTC/USDT 1m candle concept.
- Short-horizon crypto volatility remains large enough that a same-day move below 66k is plausible even from a 68.5k starting point.

## Why this source may matter

This is the central source note because the market is unusually cleanly specified: one exchange, one pair, one timeframe, one candle close field, one threshold. That sharply lowers interpretation ambiguity but concentrates risk on short-horizon path dependence and exchange-specific print risk.

## Possible impact on the question

Because BTC was trading roughly 2.5k above the threshold during the run, the base rate favors Yes. But the exact mechanics matter: the market can still lose on a brief downside move that leaves the **final noon ET close** at or below 66,000, even if broader crypto sentiment remains constructive.

## Reliability notes

- Binance API is a highly credible direct source for BTCUSDT spot/kline data.
- Polymarket gamma API is a strong direct contextual source for contract mechanics and timing.
- Evidence independence is only medium because the contextual source references the same governing Binance surface.
- Source-of-truth ambiguity appears low: the market explicitly identifies exchange, pair, interval, field, timezone, and precision rule.