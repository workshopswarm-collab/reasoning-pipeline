---
type: source_note
case_key: case-20260415-58166133
dispatch_id: dispatch-case-20260415-58166133-20260415T083617Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity: btc
topic: case-20260415-58166133 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for bitcoin-above-on-april-16
source_type: market rules / market pricing surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-58166133/researcher-analyses/2026-04-15/dispatch-case-20260415-58166133-20260415T083617Z/personas/risk-manager.md]
tags: [polymarket, market-rules, market-pricing, resolution-criteria]
---

# Summary

Polymarket’s own market page establishes both the current market-implied probability for the $72,000 threshold and the contract mechanics. It shows the $72,000 outcome around 84% and states that resolution depends specifically on the Binance BTC/USDT 1-minute candle at 12:00 ET on Apr 16, 2026, using the final Close price.

## Key facts extracted

- The market title is "Bitcoin above ___ on April 16?"
- The listed threshold relevant to this run is $72,000.
- The page shows the $72,000 outcome at roughly 84% at fetch time.
- The rule is binary for this threshold: Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr 16 closes higher than 72,000; otherwise No.
- The source of truth is Binance BTC/USDT, not other exchanges or other pairs.
- Price precision is determined by the decimal precision shown by the source.

## Evidence directly stated by source

- Resolution source is Binance.
- Relevant candle is the 1-minute candle for 12:00 in ET timezone.
- The deciding field is the final candle "Close" price.
- The market-implied probability for the 72,000 level was approximately 84% when checked.

## What is uncertain

- The webpage snapshot is not itself the authoritative settlement print; Binance is.
- The page does not independently prove that Binance historical candle display will remain accessible in the same interface state at settlement.
- The page alone does not give path-risk context for BTC between now and settlement.

## Why this source may matter

This is the governing contract surface for the market. It defines the exact timing, symbol, exchange, and price field that matter, which is essential because this is a narrow-resolution crypto market with exchange-specific settlement mechanics.

## Possible impact on the question

This source makes clear that the thesis is not "Bitcoin broadly stays above 72k" but rather "the Binance BTC/USDT 12:00 ET 1-minute candle on Apr 16 closes above 72,000." That narrows the relevant risk to exchange-specific and minute-specific resolution mechanics.

## Reliability notes

High for contract wording and current displayed market pricing, but not sufficient alone for settlement because the authoritative source-of-truth print is Binance.