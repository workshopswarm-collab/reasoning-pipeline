---
type: source_note
case_key: case-20260415-9a9c8ea3
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-9a9c8ea3 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page
source_type: market rules / resolution source description
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [risk-manager finding, risk-manager evidence map]
tags: [polymarket, rules, resolution, bitcoin, btc]
---

# Summary

This source establishes the exact contract mechanics and governing source-of-truth surface. The contract resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16, using the final close price for that minute and comparing it against the threshold in the title.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final close above 72,000.
- The governing source named by the contract is Binance, specifically the BTC/USDT candles view with 1m selected.
- The contract is exchange-specific and pair-specific: Binance BTC/USDT, not other exchanges or pairs.
- Price precision follows the source precision on Binance.
- The event page showed the 72,000 line trading around 96% at capture time, implying an extreme-confidence baseline.

## Evidence directly stated by source

Directly stated by the rules page:
- resolution depends on the Binance 1-minute candle for BTC/USDT at 12:00 in ET timezone
- final close must be higher than the stated threshold
- Binance is the resolution source
- precision is determined by the source decimals

## What is uncertain

- The page text does not independently verify how Binance internally labels its candle timestamps versus ET display; that requires separate verification.
- The page does not itself provide the final settlement print yet because the resolution time has not occurred.

## Why this source may matter

This is the contract-defining source. Most forecast error risk here is not directional macro risk but timing and source-mechanics risk: wrong minute, wrong timezone, wrong exchange, or wrong instrument would settle the contract incorrectly.

## Possible impact on the question

This source sharply narrows the relevant question from broad BTC price direction to a specific operational condition: whether Binance BTC/USDT closes above 72,000 on the exact 12:00 ET one-minute candle on April 16.

## Reliability notes

High reliability for contract mechanics because this is the market operator's own rules page. It is not sufficient by itself for the outcome because the final observed Binance close must still be checked at resolution time.