---
type: source_note
case_key: case-20260415-35855579
dispatch_id: dispatch-case-20260415-35855579-20260415T225312Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page and Binance BTCUSDT spot API check
source_type: market rules page + exchange API
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-35855579/researcher-analyses/2026-04-15/dispatch-case-20260415-35855579-20260415T225312Z/personas/variant-view.md]
tags: [polymarket, binance, resolution-source, intraday, timing]
---

# Summary

This source note captures the direct contract mechanics from the Polymarket market page and a verification pass against Binance's public BTCUSDT API. The main importance is not directional macro news but the narrow settlement mechanics: the market resolves off a single Binance BTC/USDT 1-minute candle at 12:00 PM America/New_York time on April 16, 2026.

## Key facts extracted

- Polymarket states the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 PM ET on April 16 has a final Close price higher than 72,000.
- The stated resolution source is Binance BTC/USDT with 1m candles selected.
- The contract is explicitly about Binance BTC/USDT, not other exchanges or pairs.
- A timezone conversion check shows 2026-04-16 12:00 PM ET equals 2026-04-16 16:00:00 UTC.
- A Binance public API spot check on 2026-04-15 showed BTCUSDT trading around 75,088, materially above the 72,000 threshold.
- Attempting to query the exact future 2026-04-16 16:00 UTC candle now correctly returns no candle yet, which is consistent with the event still being unresolved at research time.

## Evidence directly stated by source

- Direct from Polymarket rules: Yes resolves if the Binance 1-minute candle for BTC/USDT at 12:00 ET on the specified date has a final Close above the strike.
- Direct from Polymarket rules: price precision is determined by the source.
- Direct from Polymarket page snapshot: the 72,000 line was trading about 97.7%-98% Yes during this check.

## What is uncertain

- The exact final 12:00 ET candle close is unknown until the resolution minute occurs.
- BTC can move materially overnight; the current spot price does not settle the contract.
- The market page references the Binance trading UI as resolution surface; the API is a practical verification surface, but settlement still depends on Binance's BTC/USDT candle data as represented by the stated source.

## Why this source may matter

This is the governing source-of-truth note for the case. It narrows the analysis away from general "Bitcoin tomorrow" framing and toward whether one specific Binance minute close remains above 72,000 at noon ET.

## Possible impact on the question

The contract mechanics make the market mostly a short-horizon spot-price persistence question, not a broad narrative question. Because spot was already roughly 4% above the threshold during the check, the obvious baseline is that Yes should remain favored. The variant angle comes from the fact that a single-minute close can still fail on sharp intraday volatility, exchange-specific wick behavior, or overnight risk-off moves.

## Reliability notes

- Polymarket rules page is the best direct contract source available in this run and is authoritative for how traders are expected to interpret settlement.
- Binance public API is a strong contextual verification surface for current BTCUSDT pricing and candle mechanics, though the exact settlement surface is the Binance BTC/USDT candle data itself at the specified time.
- Evidence independence is moderate rather than high because the exchange verification is not independent of the named settlement source; it is mainly a consistency check.