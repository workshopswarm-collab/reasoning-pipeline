---
type: source_note
case_key: case-20260416-3e035ad7
dispatch_id: dispatch-case-20260416-3e035ad7-20260416T043505Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-3e035ad7 | base-rate
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 70000?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance API and Polymarket market rules
source_type: primary+contextual
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-3e035ad7/researcher-analyses/2026-04-16/dispatch-case-20260416-3e035ad7-20260416T043505Z/personas/base-rate.md]
tags: [binance, polymarket, resolution, btc, source-note]
---

# Summary

This note checks the governing contract mechanics and a direct Binance price surface for the April 17 BTC-above-70000 market.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT **1-minute candle labeled 12:00 ET** on the date in the title.
- The decisive field is the candle's final **Close** price, not intraminute high/low and not another exchange.
- The threshold is strict: the close must be **higher than 70000**.
- A direct Binance API spot price check at approximately 2026-04-16T04:36:33Z showed BTCUSDT at **74975.57**.
- Recent 1-minute Binance klines around the check time all closed around **74.9k**, materially above 70k.

## Evidence directly stated by source

- Polymarket market page states: resolve Yes if the Binance 1 minute candle for BTC/USDT 12:00 in ET timezone on Apr 17 has a final Close price higher than 70000.
- Binance ticker endpoint returned `{ "symbol": "BTCUSDT", "price": "74975.57000000" }`.
- Binance klines endpoint returned the last five 1-minute candles with closes between 74901.62 and 74992.00 during the sampled window.

## What is uncertain

- The market settles on **tomorrow's** noon ET candle, not today's current spot price.
- Crypto can move materially in less than 24 hours, so current price is not dispositive.
- Binance UI and API naming around candle timestamps can create edge-case confusion if the displayed 12:00 ET candle corresponds to the minute ending at 12:00 rather than starting at 12:00, though the contract clearly anchors to Binance's displayed 12:00 candle.

## Why this source may matter

It provides both the governing resolution language and a direct read on the current Binance level relative to the threshold. That is the minimum primary evidence needed for a narrow, date-specific market.

## Possible impact on the question

Because BTC is currently about 7.1% above the threshold on the governing exchange, the base rate for remaining above 70000 by the relevant noon ET snapshot in less than 36 hours is very high absent a sharp selloff. The main remaining uncertainty is short-horizon crypto volatility, not contract wording.

## Reliability notes

- Binance is the explicit source of truth, so source-of-truth relevance is very high.
- Polymarket is authoritative for the contract wording but not for the final price itself.
- Evidence independence is only medium because the rules page references Binance directly; still, the price check and the rules check answer different parts of the problem.
- Operational-risk remains relevant because the contract depends on Binance's displayed candle data rather than a multi-exchange benchmark.
