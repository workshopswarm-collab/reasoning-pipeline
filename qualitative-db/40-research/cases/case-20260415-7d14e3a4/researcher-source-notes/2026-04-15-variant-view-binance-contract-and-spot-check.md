---
type: source_note
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-19
question: Will the Binance BTC/USDT 1-minute candle closing at 12:00 PM ET on 2026-04-19 have a close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API + Polymarket market rules
source_type: primary
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7d14e3a4/researcher-analyses/2026-04-15/dispatch-case-20260415-7d14e3a4-20260415T231343Z/personas/variant-view.md]
tags: [binance, resolution-source, btc, contract-check]
---

# Summary

This source note captures the governing settlement mechanics from Polymarket and a direct spot-price verification from Binance.

## Key facts extracted

- Polymarket says the market resolves from the Binance BTC/USDT 1-minute candle for `12:00` in ET on the named date, using the final candle `Close` value.
- The relevant timestamp for April 19, 2026 noon ET converts to `2026-04-19T16:00:00Z` because New York is on EDT (`UTC-4`).
- Binance API spot check on 2026-04-15 returned BTCUSDT around `74,688.88`, already above the 72,000 threshold.
- Binance `exchangeInfo` for BTCUSDT shows tick size `0.01`, so cent-level precision appears to govern practical threshold comparison.
- Recent Binance 1-minute kline output confirms standard candle structure with open time and close time boundaries, supporting the interpretation that the noon ET candle is the one opening at `16:00:00Z` and closing at `16:00:59.999Z`.

## Evidence directly stated by source

- Binance ticker endpoint returned `{"symbol":"BTCUSDT","price":"74688.88000000"}` on 2026-04-15.
- Binance kline endpoint returned standard 1-minute candles with explicit open and close timestamps and a final close field.
- Polymarket rules explicitly state the settlement source is Binance BTC/USDT with `1m` candles and the market resolves `Yes` only if the final `Close` is higher than 72,000.

## What is uncertain

- This does not directly observe the April 19 noon ET candle; it only verifies current level, timestamp mapping, and source mechanics.
- Short-horizon BTC volatility could still move price below 72,000 by the settlement minute.
- Public web rendering of Binance charts can differ from API access details, though the API structure is consistent with the market wording.

## Why this source may matter

This is the core source-of-truth check. It establishes the exact instrument, venue, time conversion, and current reference level versus the threshold.

## Possible impact on the question

Because the governing source is Binance BTC/USDT and current spot is materially above 72,000 by roughly 2.7k, the default view is `Yes`. The main remaining risk is adverse short-term price movement before the exact settlement minute, not ambiguity about the contract source.

## Reliability notes

High reliability for venue mechanics and current quoted spot because Binance is the direct source referenced by the contract. Lower reliability for forecasting the April 19 noon ET level, since the source is a contemporaneous market data point rather than a predictive source.