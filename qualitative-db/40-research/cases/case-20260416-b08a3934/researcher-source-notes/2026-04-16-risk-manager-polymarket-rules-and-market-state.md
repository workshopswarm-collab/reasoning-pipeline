---
type: source_note
case_key: case-20260416-b08a3934
dispatch_id: dispatch-case-20260416-b08a3934-20260416T023832Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: markets
entity: btc
topic: case-20260416-b08a3934 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15T22:41:00-04:00
source_name: Polymarket market page and rules
source_type: market rules / market state
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, resolution-rules, market-state, btc]
---

# Summary

Polymarket provides the governing contract wording visible to traders and shows the current market state for the 72,000 threshold outcome. The page states resolution depends on the Binance BTC/USDT 1-minute candle at 12:00 ET on Apr 17, specifically the final Close price, and the 72,000 outcome was trading around 91% at the time checked.

## Key facts extracted

- The relevant threshold market is the Apr 17 noon ET BTC/USDT close-versus-72,000 contract.
- The visible market price for the 72,000 threshold was about 91%, matching the assignment baseline of 0.93 directionally.
- The contract resolves Yes only if the Binance 1-minute candle for BTC/USDT at 12:00 ET has a final Close strictly higher than 72,000.
- The source of truth is Binance BTC/USDT with 1m candles selected.
- Price precision is determined by Binance source precision.

## Evidence directly stated by source

- The page explicitly says the market resolves to Yes if the Binance 1 minute candle for BTC/USDT 12:00 ET on the specified date has a final Close price higher than the named threshold.
- The page explicitly says this is Binance BTC/USDT, not another exchange or pair.
- The page explicitly shows the 72,000 line trading around 91%.

## What is uncertain

- The market page alone does not independently verify Binance operational status or current BTC/USDT level.
- The page does not clarify edge handling beyond the visible rules text if Binance data were unavailable or amended later.
- The page is not itself the final settlement source; it points to Binance as the source of truth.

## Why this source may matter

This source governs the contract mechanics and defines the operational and timing risks that matter more than generic Bitcoin direction. It also provides the market-implied baseline that the analysis must compare against.

## Possible impact on the question

If the contract is read correctly, the central risk is not whether Bitcoin is generally strong but whether Binance BTC/USDT remains above 72,000 at the exact 12:00 ET one-minute close on Apr 17. That wording makes timing/path risk and exchange-specific operational risk relevant even if spot BTC is currently well above 72,000.

## Reliability notes

Useful and necessary for contract interpretation, but it is a platform surface rather than the underlying authoritative settlement source. Reliability for rules text is good; reliability for final resolution is incomplete without direct Binance verification.