---
type: source_note
case_key: case-20260415-d9ca8ddf
dispatch_id: dispatch-case-20260415-d9ca8ddf-20260415T195847Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-d9ca8ddf | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for "Bitcoin above ___ on April 17?"
source_type: market-rules-page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [risk-manager.md, risk-manager.sidecar.json, assumptions/risk-manager.md, evidence/risk-manager.md]
tags: [polymarket, market-rules, resolution-source, binance, time-sensitive]
---

# Summary

This source provides the governing contract mechanics for the market and the market-implied baseline as observed during the run.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for **12:00 ET (noon) on April 17, 2026** has a final **Close** price **higher than 72,000**.
- The market resolves No otherwise.
- The stated resolution source is Binance, specifically the BTC/USDT chart with **1m** and **Candles** selected.
- The rule explicitly says the market is about **Binance BTC/USDT**, not other exchanges or pairs.
- The visible market price for the 72,000 line during the run was approximately **93% Yes**.

## Evidence directly stated by source

- The market is a **date-sensitive, exact-time, single-exchange, single-pair** contract.
- The relevant value is the candle **Close**, not the last traded price at some other moment.
- Precision is governed by Binance source decimals.

## What is uncertain

- The public Polymarket page is a secondary presentation of the rules; settlement still depends on the actual Binance data state visible/available at resolution.
- The page does not independently prove what the April 17 noon ET candle close will be.

## Why this source may matter

This is the governing source for contract interpretation. The main market risk is not confusion about the threshold but timing and venue specificity: a materially different price on another exchange or even adjacent minutes on Binance would not control resolution.

## Possible impact on the question

This source anchors the correct resolution mechanics and shows the market was pricing the event as very likely. It also highlights the main fragility: traders must be right about the exact Binance BTC/USDT 12:00 ET one-minute close, not just about BTC broadly staying above 72k.

## Reliability notes

Primary for contract wording, but not primary for the eventual price outcome itself. High value for settlement interpretation; limited value for directional price forecasting beyond showing the crowd baseline.