---
type: source_note
case_key: case-20260415-10579f0a
dispatch_id: dispatch-case-20260415-10579f0a-20260415T184424Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page + Binance BTCUSDT public API verification
source_type: market-rules-and-exchange-api
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-10579f0a/researcher-analyses/2026-04-15/dispatch-case-20260415-10579f0a-20260415T184424Z/personas/risk-manager.md]
tags: [source-note, polymarket, binance, resolution]
---

# Summary

This source note captures the governing contract mechanics and an additional verification pass against Binance public market data for the specific Polymarket contract.

## Key facts extracted

- Polymarket states the market resolves "Yes" if the Binance BTC/USDT 1-minute candle for **12:00 ET (noon)** on April 17 has a final **Close** price **higher than 70,000**.
- Resolution source is explicitly Binance BTC/USDT with **1m** candles.
- The contract is about **Binance BTC/USDT specifically**, not other exchanges or other BTC pairs.
- The relevant timestamp maps to **2026-04-17 16:00:00 UTC** because April 17 falls in Eastern Daylight Time (UTC-4).
- Binance public API was reachable during the research run and returned live BTCUSDT prices/candles.
- A verification pass on April 15 showed spot BTCUSDT around **74,290.44**, roughly **5.8% above** the 70,000 threshold.
- Recent intraday 1-minute data sampled during the run showed a day high around **74,618.87** and day low around **73,514.00**, still above 70,000.

## Evidence directly stated by source

- The market uses the Binance 1-minute candle close at 12:00 ET on the named date.
- The outcome requires the close to be strictly higher than 70,000.
- Price precision is determined by the source.

## What is uncertain

- The final April 17 noon ET candle is not yet available, so this note cannot settle the market directly.
- The public Binance web trading page was not cleanly extractable via text fetch, so the direct verification used Binance public API rather than the webpage UI.
- There remains some operational dependence on Binance producing a normal 1-minute candle and Polymarket using that source as described.

## Why this source may matter

This is the governing source-of-truth surface for the contract and the most important mechanical input. The extra API pass reduces risk of misunderstanding the time mapping or exchange-specific nature of the contract.

## Possible impact on the question

The rule text and API pass together support a high-probability leaning Yes because current Binance BTCUSDT is materially above 70,000 and the contract threshold is comfortably below spot. The remaining risk is mostly path/timing risk into the exact noon ET close rather than source ambiguity.

## Reliability notes

- Polymarket rule text is the authoritative contract interpretation source for what counts.
- Binance public API is a strong contextual verification source for exchange-specific price level and timestamp mechanics, but it does not itself guarantee future resolution.
- Evidence independence is moderate: both sources relate to the same market mechanism, but one is contract text and the other is the exchange data surface named in the contract.