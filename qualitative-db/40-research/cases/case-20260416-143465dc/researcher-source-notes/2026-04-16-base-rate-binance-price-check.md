---
type: source_note
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: tokens
entity: sol
topic: will-solana-reach-90-april-13-19
question: Will Solana reach $90 April 13-19?
date_created: 2026-04-16
source_name: Binance market data API checks for SOLUSDT
source_type: exchange_market_data
source_url: https://api.binance.com/api/v3/klines
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: []
upstream_inputs: [qualitative-db/40-research/cases/case-20260416-143465dc/researcher-source-notes/2026-04-16-base-rate-binance-resolution-source.md]
downstream_uses: [qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/personas/base-rate.md]
tags: [binance, price-history, touch-probability, verification]
---

# Summary

A direct Binance API check of SOLUSDT 1-minute candles over the relevant April 13-19 window so far found no qualifying $90 touch yet. The highest observed 1-minute High in the checked window was $89.15 on 2026-04-16 19:00 UTC (3:00 PM ET). Recent daily highs show SOL moving up from low 80s into upper 80s, but still below the contract threshold.

## Key facts extracted

- Checked Binance SOLUSDT 1-minute klines for the contract window beginning 2026-04-13 00:00 ET.
- Across the checked interval through 2026-04-16 afternoon ET, the maximum 1-minute High observed was 89.15.
- The max qualifying near-miss candle opened at 2026-04-16T19:00:00Z and closed at 2026-04-16T19:00:59.999Z.
- Recent daily highs were 86.81 on Apr 13, 87.67 on Apr 14, 85.83 on Apr 15, and 89.15 on Apr 16.
- A Binance 24h ticker pull at the time of research showed last price 88.96 and 24h high 89.15.
- In the last 30 daily candles, SOL posted highs >= 90 on 8 of 30 days; over the last 14 days, 0 of 14 days reached 90.

## Evidence directly stated by source

- Binance kline API returned a maximum 1-minute High of 89.15 in the relevant checked window.
- Binance recent daily klines showed an upswing from about 81.5 close on Apr 12 to upper-80s by Apr 16.
- Binance 24h ticker showed SOL trading only about 1.2% below the threshold at research time.

## What is uncertain

- The April 17-19 portion of the resolution window had not occurred yet at the time of this check.
- A touch market can resolve from a brief spike that is hard to infer from end-of-day closes alone.
- Short-horizon crypto moves are highly path dependent and can overshoot during risk-on bursts.

## Why this source may matter

This is the key direct empirical check for both whether the event has already happened and how far away the market currently is from the threshold.

## Possible impact on the question

The evidence supports a view that the event remains live but unresolved: no touch yet, though the threshold is close enough that one strong continuation move could settle the market quickly.

## Reliability notes

High-quality direct data from the governing exchange source, but the analysis depends on correct time-window handling and only covers the period observed so far. It is strong for present-state verification, not a guarantee about the remaining days.