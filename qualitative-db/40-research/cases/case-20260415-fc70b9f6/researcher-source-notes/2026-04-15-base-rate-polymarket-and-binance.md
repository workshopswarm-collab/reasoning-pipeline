---
type: source_note
case_key: case-20260415-fc70b9f6
dispatch_id: dispatch-case-20260415-fc70b9f6-20260415T072610Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page plus Binance BTCUSDT kline API spot check
source_type: primary-plus-direct-context
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-fc70b9f6/researcher-analyses/2026-04-15/dispatch-case-20260415-fc70b9f6-20260415T072610Z/personas/base-rate.md
tags: [polymarket, binance, contract-mechanics, direct-evidence]
---

# Summary

This note captures the governing contract mechanics from the Polymarket market page and a direct Binance spot-market check showing BTC/USDT trading materially above 72,000 during the research run.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final Close price higher than 72,000.
- The listed resolution source is Binance BTC/USDT with 1m candles selected.
- Price precision is determined by the Binance source.
- The market page showed the 72,000 line around 85% during the fetch.
- A direct call to Binance spot klines during the run returned recent 1-minute candles with closes around 73,680 to 73,728 at 2026-04-15 07:23-07:27 UTC, roughly 27-31 hours before resolution.

## Evidence directly stated by source

From Polymarket rules text:
- market resolves on the Binance BTC/USDT 12:00 ET 1-minute candle close
- must be higher than 72,000, otherwise No
- source is Binance, not other exchanges or pairs

From direct Binance kline response observed in-run:
- recent BTCUSDT closes were above 73,600 at the time checked
- this means spot was already about 2.3% above the contract threshold during the research run

## What is uncertain

- The direct Binance check here is not the eventual settlement candle; it is only a current-state verification.
- BTC can move more than 2-3% in a day, so trading above the threshold now does not settle the question.
- Public fetched documentation for Binance kline endpoint was not cleanly retrievable via web_fetch, though the endpoint itself returned valid market data.

## Why this source may matter

The Polymarket page is the clearest accessible statement of the contract mechanics, while the direct Binance kline pull verifies the exact exchange/pair/candle surface is live and currently above the threshold. Together they make the relevant base-rate question straightforward: how often does BTC fall more than about 2.3% over roughly one day from this starting point?

## Possible impact on the question

These sources push toward Yes unless there is a meaningful downside move before noon ET on April 16. They also reduce contract-interpretation ambiguity because the exchange, pair, candle interval, timezone, and comparison operator are explicit.

## Reliability notes

- Polymarket is authoritative for the market's own wording but not for the final underlying price itself.
- Binance is the direct source-of-truth surface for the underlying settlement value.
- Evidence independence is medium: the two sources are not independent about contract structure, but they serve different functions (rules vs underlying price surface).