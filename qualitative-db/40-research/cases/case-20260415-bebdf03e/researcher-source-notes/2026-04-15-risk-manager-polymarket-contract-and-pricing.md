---
type: source_note
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-21 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page
source_type: primary-contract
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-bebdf03e/researcher-analyses/2026-04-15/dispatch-case-20260415-bebdf03e-20260415T221944Z/personas/risk-manager.md]
tags: [source-note, polymarket, contract, market-price]
---

# Summary

This source note captures the market-implied baseline and the exact contract wording. The relevant contract is not a generic April 21 daily close or cross-exchange BTC price question; it is specifically the Binance BTC/USDT 1-minute candle at 12:00 ET on April 21. The displayed Yes price for 72,000 was about 81 cents during the run, implying roughly 81.5% market probability from the provided current price 0.815.

## Key facts extracted

- The market title is "Will the price of Bitcoin be above $72,000 on April 21?"
- Contract wording says Yes resolves if the Binance BTC/USDT 1-minute candle for 12:00 ET has a final close price higher than 72,000.
- The source of truth is Binance, not other exchanges or pairs.
- Market page showed the 72,000 line around 80-81% Yes during the run, consistent with assignment metadata current_price 0.815.
- Neighboring ladder prices were materially different (e.g. 70,000 around 90%, 74,000 around 58%), which helps contextualize how tightly the market centers BTC around the low-to-mid 70s by settlement.

## Evidence directly stated by source

- Exact resolution conditions, timing, and source of truth.
- Current contract pricing ladder and market-implied baseline.

## What is uncertain

- The web page may lag slightly or round displayed prices.
- The market price embeds crowd expectations but is not direct evidence of final settlement.

## Why this source may matter

This source defines what counts for resolution and provides the baseline probability against which the risk-manager view must compare. It also shows the crowd is fairly confident but not near-certainty, leaving room to stress-test downside paths.

## Possible impact on the question

The source frames the key risk correctly: the contract depends on one specific exchange, one specific pair, one specific minute, and an above/not-above cutoff. That makes path and timing risk more important than in a broad weekly average price question.

## Reliability notes

High reliability for contract terms and the market-implied baseline because Polymarket defines the market. Low independence on pricing because this is the market itself, not an external evidence source.