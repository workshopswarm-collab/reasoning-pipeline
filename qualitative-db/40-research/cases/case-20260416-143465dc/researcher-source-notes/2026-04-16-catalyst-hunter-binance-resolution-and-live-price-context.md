---
type: source_note
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-90-touch-resolution-and-live-binance-context
question: Will Solana reach $90 April 13-19?
driver:
date_created: 2026-04-16
source_name: Polymarket market rules plus Binance SOLUSDT API
source_type: primary_market_rules_plus_authoritative_resolution_feed
source_url: https://polymarket.com/event/what-price-will-solana-hit-april-13-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/personas/catalyst-hunter.md
  - qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/evidence/catalyst-hunter.md
tags: [polymarket, binance, resolution-source, sol]
---

# Summary

This source note captures the governing contract mechanics and the current Binance SOL/USDT path context for the April 13-19 "$90 touch" market.

## Key facts extracted

- Polymarket states the market resolves "Yes" if **any Binance 1-minute candle** for SOL/USDT during the title date range has a final **High** price **equal to or greater than $90**.
- The governing source of truth is explicitly Binance SOL/USDT with the chart on **1m candles**.
- Other exchanges, other pairs, and other market data do **not** count.
- Binance API sampling across the eligible window from **2026-04-13 00:00 ET** through **2026-04-16 15:19 ET** shows a realized period high of **89.15**, not yet 90.
- Daily highs from the Binance 1m data pulled for the active window were:
  - 2026-04-13: 86.81
  - 2026-04-14: 87.67
  - 2026-04-15: 85.83
  - 2026-04-16 through 15:19 ET: 89.15
- Binance 24h ticker at capture time showed SOL/USDT last price about **88.97**, 24h high **89.15**, and 24h move **+4.5%**.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will immediately resolve to \"Yes\" if any Binance 1-minute candle for SOL/USDT during the date range specified in the title ... has a final \"High\" price equal to or greater than the price specified in the title."
- "The resolution source for this market is Binance, specifically the SOL/USDT \"High\" prices ... with the chart settings on \"1m\" candles selected on the top bar."
- "Prices from other exchanges, different trading pairs, or spot markets will not be considered for the resolution of this market."

From Binance API:
- The 1m kline feed is machine-readable and directly exposes the candle high field used by the contract.
- The queried eligible-window data did not include a candle high at or above 90 as of collection time.

## What is uncertain

- This note does not establish whether SOL will print 90 later in the eligible window; it only confirms that it had not yet done so at collection time.
- The exact catalyst that could push SOL above 90 is not contained in the rules/API source and must be inferred from contextual market reporting.

## Why this source may matter

This is the core settlement and verification source. For a narrow touch market, contract mechanics matter almost as much as directional price view, because a brief one-minute wick is sufficient.

## Possible impact on the question

The evidence supports a live setup where the market is near-but-not-over the trigger. That raises the importance of near-term catalysts and intraday volatility rather than end-of-week closing price logic.

## Reliability notes

- Very high reliability for resolution mechanics: Polymarket explicitly names Binance 1m highs as the source of truth.
- Very high reliability for live price verification: Binance API directly exposes the relevant kline and ticker fields.
- Independence versus contextual reporting is low because both pieces are tied to the same exchange ecosystem, but that is appropriate here because the contract itself is exchange-specific.