---
type: source_note
case_key: case-20260414-3ce42d6c
dispatch_id: dispatch-case-20260414-3ce42d6c-20260414T130958Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-14 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and Binance BTCUSDT 1m klines API
source_type: primary-plus-direct-context
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-14
credibility: high
recency: high
stance: supports-yes
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3ce42d6c/researcher-analyses/2026-04-14/dispatch-case-20260414-3ce42d6c-20260414T130958Z/personas/market-implied.md]
tags: [source-note, polymarket, binance, btc]
---

# Summary

This note captures the governing contract mechanics from the Polymarket market page and a direct Binance spot-market context check. Together they show the market resolves from the Binance BTC/USDT one-minute candle labeled 12:00 ET on 2026-04-14, and that several hours before noon ET BTC/USDT was already trading around 74.5k, comfortably above the 70k threshold.

## Key facts extracted

- Polymarket says the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET has a final Close price higher than 70,000.
- The market explicitly uses Binance, not other exchanges or other pairs.
- Price precision is whatever decimal precision Binance displays for the source candle.
- The Polymarket page showed the 70,000 line trading around 99.9 cents / implied probability about 99.95% at fetch time.
- A direct Binance BTCUSDT 1m klines API check around 2026-04-14 13:07 UTC (09:07 ET) showed recent closes around 74,55x-74,58x, materially above 70,000.

## Evidence directly stated by source

From Polymarket market rules:
- Yes if the Binance 1 minute candle for BTC/USDT 12:00 ET on the specified date has a final Close higher than the strike.
- Resolution source is Binance BTC/USDT with 1m candles selected.
- The pair and venue are part of the contract definition.

From Binance direct API context check:
- Recent 1m closes fetched from `api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5` were approximately 74,551 to 74,584 shortly after 09:07 ET.

## What is uncertain

- This direct Binance check is not the exact resolution candle; it is a same-day pre-resolution context check.
- The market still depends on the final noon ET candle close, so an extreme intraday move of more than about 4.5k downward before noon ET would be needed for No.
- The public market page is a useful statement of rules but final operational settlement still depends on the underlying Binance candle data available at resolution time.

## Why this source may matter

This is the core direct-evidence package for the case: one source defines what counts, and the other shows where BTC/USDT actually was on the relevant venue shortly before the deadline.

## Possible impact on the question

The combined read strongly supports Yes. The threshold is far below observed same-day Binance spot levels, so the market's extreme confidence looks justified unless there is a very large same-morning selloff or a Binance-specific data/operational issue before noon ET.

## Reliability notes

- Polymarket rules are the appropriate contract-mechanics source but are still a platform surface rather than the final underlying settlement datum.
- Binance klines API is a direct exchange data surface and is more relevant than generic BTC/USD trackers because the contract specifies Binance BTC/USDT.
- Independence is moderate rather than high because both pieces ultimately hinge on Binance as the source of truth; however that is exactly what the contract requires.