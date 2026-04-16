---
type: source_note
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-20 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rule text for Bitcoin above 70000 on April 20
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-implied, bitcoin]
---

# Summary

This source established the live market-implied baseline and the exact resolution mechanics. It is the governing source for what counts, because this is a rule-sensitive, date-specific contract.

## Key facts extracted

- The specific 70000 threshold contract was trading around 86% Yes at fetch time, close to the assignment's `current_price` of 0.875.
- The event page shows the ladder around this strike: 68000 at ~94%, 70000 at ~86%, 72000 at ~73%, 74000 at ~52%, 76000 at ~31%.
- The market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-20.
- The relevant field is the candle's final `Close` price, not intraminute high, daily close, or another exchange's print.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- Rule text says Yes resolves if the Binance 1-minute candle for BTC/USDT at 12:00 ET on the specified date has a final Close price higher than 70000.
- Rule text says Binance BTC/USDT is the resolution source, specifically the chart/candles interface with 1m selected.
- The live market ladder implies the crowd centers expected April 20 noon ET BTC/USDT around the low-to-mid 70s rather than just barely above 70k.

## What is uncertain

- The fetched market page is not itself the settlement record; it states the rules but not the final future Binance print.
- The public market page does not explain trader positioning, hedging, or whether the 86% price overstates true probability because of demand imbalance.
- The page does not independently verify Binance chart accessibility or any possible operational edge cases at resolution time.

## Why this source may matter

It is the direct source for market-implied probability and the contract mechanics. Because the contract is narrow and date-sensitive, getting the timing, venue, and measurement field right matters as much as getting the directional BTC view right.

## Possible impact on the question

This source strongly supports using the market as a serious prior. The strike ladder suggests traders are not merely saying BTC might be above 70k; they are implicitly placing the likely April 20 noon ET level several thousand dollars above the threshold. That makes an 87.5% prior plausible if spot remains in the mid-70k area and no major downside shock occurs.

## Reliability notes

- Strong for contract wording and live market-implied baseline.
- Not independent from market sentiment; this is the crowd prior itself, not external verification.
- Needs at least one additional contextual source for price level / market context verification.
