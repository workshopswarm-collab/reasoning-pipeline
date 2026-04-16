---
type: source_note
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: threshold-close-markets
entity: sol
topic: SOL above 80 on Apr 19 via Binance noon ET 1m close
question: Will the price of Solana be above $80 on April 19?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page rules plus direct Binance SOLUSDT spot/1m endpoint checks
source_type: primary-plus-direct-market-data
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/market-implied.md
tags: [polymarket, binance, rules, source-note, sol]
---

# Summary

The Polymarket market page gives the governing contract mechanics directly: resolution is based on the Binance SOL/USDT 1-minute candle for 12:00 ET on Apr 19, using the final Close, and the outcome is Yes only if that close is higher than 80. Direct Binance API checks on Apr 15 evening ET showed SOL/USDT around 84.70 with recent 1-minute closes in the 84.67-84.75 range, meaning the market is currently several dollars above the threshold but still has multiple days of path risk before the governing timestamp.

## Key facts extracted

- Governing source named by the contract: Binance SOL/USDT.
- Governing condition: the 12:00 ET one-minute candle on Apr 19 must have a final Close strictly higher than 80.
- This is a close-at-a-specific-minute market, not a touch/high market.
- Direct Binance endpoint checks returned current SOLUSDT around 84.70 and recent one-minute closes clustered near 84.7 on Apr 15 evening ET.
- The contract is exchange-specific and pair-specific; other exchanges or SOL/USD references are only contextual.

## Evidence directly stated by source

- Polymarket rules state the exact resolution condition and source of truth.
- Binance endpoint output directly states the observed current SOL/USDT price and recent one-minute klines at the time checked.

## What is uncertain

- Current price does not guarantee the Apr 19 12:00 ET final close.
- Public web extraction of the Binance page itself was unreliable in this environment, so the direct market-data verification here came from Binance public API endpoints rather than the rendered trade page.
- Contract wording references the trade page UI, but the economic substance appears to be the same Binance one-minute close series.

## Why this source may matter

This is the core mechanism note for the case. It identifies the governing source, the exact timestamp logic, and the key distinction that the market is about a single future close rather than a touch event. That distinction materially raises path dependence versus the more permissive touch-style markets.

## Possible impact on the question

Because SOL is currently above 80 on Binance, the market's high Yes probability has an obvious basis. But because the contract resolves on one specific noon ET minute several days later, the remaining question is whether SOL can stay above 80 through that exact checkpoint rather than merely trade above it at any time before then.

## Reliability notes

- Primary rules source quality: high.
- Direct market-data check quality: high for spot context, but not itself the settlement print because the event has not happened yet.
- Independence: low-to-medium because both pieces are tied to the same market structure, though one is rules text and one is direct exchange data.
- Main residual ambiguity is operational rather than conceptual: whether the eventual UI-rendered candle and public API candle remain perfectly aligned at settlement time.