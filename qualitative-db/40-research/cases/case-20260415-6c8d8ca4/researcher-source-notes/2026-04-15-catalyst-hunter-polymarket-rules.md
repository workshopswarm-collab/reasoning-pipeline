---
type: source_note
case_key: case-20260415-6c8d8ca4
dispatch_id: dispatch-case-20260415-6c8d8ca4-20260415T084705Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: prediction-markets
entity:
topic: bitcoin-above-72k-on-april-17
question: What exactly has to happen for the market to resolve Yes?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market rules / primary
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: []
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-6c8d8ca4/researcher-analyses/2026-04-15/dispatch-case-20260415-6c8d8ca4-20260415T084705Z/personas/catalyst-hunter.md]
tags: [polymarket, market-rules, resolution, source-note]
---

# Summary

The Polymarket market page clarifies the exact contract mechanics: the relevant print is the Binance BTC/USDT one-minute candle close for 12:00 ET on April 17, and the outcome is Yes only if that close is strictly higher than 72,000.

## Key facts extracted

- Market title: “Will the price of Bitcoin be above $72,000 on April 17?”
- Current market price shown during fetch: about `81-82%` for Yes on the 72,000 line.
- Resolution rule: resolve Yes if the Binance BTC/USDT `12:00` ET one-minute candle on the specified date has a final `Close` price higher than `72,000`.
- Otherwise resolve No.
- The source is explicitly Binance BTC/USDT, not another exchange or pair.
- Price precision is determined by the source.

## Evidence directly stated by source

- The exact resolution mechanics.
- The governing source-of-truth family.
- The current market-implied probability shown on the market page.

## What is uncertain

- The fetched page is not an official Polymarket API response and can lag or reflect UI rounding.
- The market page does not itself provide the future Binance noon ET close.

## Why this source may matter

This source defines the legal/operational contract boundary. It determines which timestamp matters, which venue matters, and that the threshold comparison is strict (`higher than 72,000`).

## Possible impact on the question

The noon ET timing matters because BTC can swing materially intraday. A view that BTC is likely above 72k “sometime that day” is not enough; it specifically has to be above 72k on the final one-minute close at noon ET.

## Reliability notes

High reliability for contract wording and displayed market odds. Slight ambiguity remains only around UI rounding versus exact tradable probability, but not around the key contract rule itself.
