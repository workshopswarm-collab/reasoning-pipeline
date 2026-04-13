---
type: source_note
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-13
question: Will the price of Bitcoin be above $70,000 on April 13?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-13
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/market-implied.md]
tags: [polymarket, rules, resolution-source, market-implied]
---

# Summary

The Polymarket market page provides both the live implied probability for the 70,000 strike and the resolution mechanics. For the 70,000 line, the visible price was 94% on the fetched page, which is materially above the assignment snapshot `current_price: 0.71`; this suggests either market movement after assignment or a stale assignment snapshot. The rules state the contract resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 13, using the final Close price, and that price must be strictly higher than 70,000.

## Key facts extracted

- The market page listed the 70,000 strike at 94% at fetch time.
- The contract resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET has a final Close above 70,000.
- The governing source is Binance BTC/USDT with `1m` and `Candles` selected.
- The contract is specific to Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance..."
- The visible outcome ladder showed 70,000 at 94%.

## What is uncertain

- The page fetch is a rendered web surface rather than an authenticated API response, so the visible market price may lag or differ from the assignment snapshot.
- The market page does not itself provide the final Binance 12:00 ET candle close within the fetched content.

## Why this source may matter

This is the governing contract surface and the best source for what counts, what does not count, and which exchange/pair/time window controls resolution.

## Possible impact on the question

It sharply narrows the question to a single Binance BTC/USDT 1-minute close at exactly 12:00 ET. That reduces ambiguity, but creates operational sensitivity around the exact timestamp and source surface.

## Reliability notes

Reliable for contract wording and visible market pricing. Less authoritative than Binance itself for the underlying BTC/USDT price path.