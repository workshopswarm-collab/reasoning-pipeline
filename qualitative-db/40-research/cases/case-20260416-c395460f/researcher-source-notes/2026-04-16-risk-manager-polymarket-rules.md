---
type: source_note
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: market-resolution
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 1-minute candle at 12:00 PM ET on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-15T22:28:00-04:00
source_name: Polymarket market page and rules
source_type: market rules / resolution source description
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: medium-high
recency: current
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: [sol]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-c395460f/researcher-analyses/2026-04-16/dispatch-case-20260416-c395460f-20260416T022702Z/personas/risk-manager.md]
tags: [polymarket, rules, binance, resolution]
---

# Summary

This source defines the contract mechanics for the market and is the governing rules surface for what must happen for a Yes resolution.

## Key facts extracted

- The market resolves Yes if the Binance SOL/USDT 1-minute candle for **12:00 in ET timezone (noon)** on the specified date has a final **Close** price higher than 80.
- The resolution source is Binance, specifically the SOL/USDT chart with **1m** and **Candles** selected.
- The market is about **Binance SOL/USDT**, not other exchanges or other pairs.
- Price precision is determined by the number of decimal places shown by the source.
- On fetch, the 80-strike contract was trading around **89-90% Yes**.

## Evidence directly stated by source

- Contract wording ties resolution to a single exchange, a single pair, a single time bucket, and the candle close rather than spot price at an arbitrary instant.
- The page explicitly distinguishes Binance SOL/USDT from other exchanges/pairs.

## What is uncertain

- The public market page reproduces the rules text but does not itself show the final settling candle in advance.
- Binance web UI presentation details could differ from API field naming, though the economic object appears to be the same 1-minute candle close.

## Why this source may matter

This is the primary source for the contract mechanics. For a date-sensitive and multi-condition market, the exact exchange, pair, timezone, and candle-close rule matter more than generic SOL price commentary.

## Possible impact on the question

The question is not simply whether SOL is generally above 80 near April 19. All of the following must hold for Yes: Binance must be the reference venue, the pair must be SOL/USDT, the relevant interval must be the 12:00 PM ET 1-minute candle on 2026-04-19, and that candle's final close must be strictly greater than 80.

## Reliability notes

Good primary source for contract interpretation, but not sufficient alone for probability estimation. It needs at least one contextual market-price source and, for this case, an additional verification pass because the market probability is extreme.