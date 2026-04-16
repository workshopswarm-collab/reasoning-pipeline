---
type: source_note
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: daily-close-threshold
entity: btc
topic: Polymarket contract mechanics for BTC above 70000 on April 20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / contract page
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/risk-manager.md
tags: [source-note, polymarket, rules, binance, btc]
---

# Summary

This source establishes the governing contract mechanics. The market resolves Yes only if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 20 has a final Close strictly higher than 70000. This is a narrow close-above contract, not a touch market and not a multi-exchange reference.

## Key facts extracted

- Governing source is Binance BTC/USDT.
- Relevant metric is the final Close of the 1-minute candle for 12:00 ET on April 20.
- The threshold comparison is strictly higher than 70000.
- Other exchanges or trading pairs do not count.
- Price precision is whatever Binance displays on the source surface.
- On the market page snapshot retrieved during this run, the 70000 line traded around 88% / 89¢ Yes.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The fetched page gives rules text and market pricing, but not a durable API-level guarantee about how Binance labels ET on the chart UI.
- The market is unresolved today, so this source does not yet provide the decisive April 20 noon close.

## Why this source may matter

It is the primary source for what counts. Because this is a date-specific close-above contract with extreme pricing, the biggest operational risk is misreading the mechanics as a touch market or relying on the wrong venue.

## Possible impact on the question

This source sharply narrows the event: BTC can trade above 70000 many times before April 20 and still resolve No if the Binance 12:00 ET 1-minute candle closes at or below 70000. That increases path and timing risk versus simpler "hit level by date" framing.

## Reliability notes

High reliability for contract interpretation because it is the market's own rules page. Lower usefulness for forecasting the actual April 20 close because it is not itself a price forecast source.