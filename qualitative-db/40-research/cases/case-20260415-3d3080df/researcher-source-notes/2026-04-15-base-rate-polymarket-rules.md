---
type: source_note
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-14
source_name: Polymarket event page and market rules
source_type: primary
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3d3080df/researcher-analyses/2026-04-15/dispatch-case-20260415-3d3080df-20260415T002239Z/personas/base-rate.md]
tags: [polymarket, contract-rules, settlement, bitcoin]
---

# Summary

Polymarket's rules define a narrow, rule-sensitive contract: Yes resolves only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20 has a final close strictly higher than 70,000. The event page also showed current market pricing around 85-86% for the 70,000 line during this run.

## Key facts extracted

- Current market-implied probability for "above 70,000" is about 85-86%.
- Resolution is based on Binance BTC/USDT only, not other exchanges or other BTC pairs.
- The specific observation window is the 1-minute candle labeled 12:00 in ET timezone on April 20.
- The threshold condition is strictly higher than 70,000, not equal to or above.
- Price precision is determined by the source's displayed decimal precision.

## Evidence directly stated by source

- The market is not asking whether BTC touches 70k, trades above 70k intraday elsewhere, or closes the day above 70k.
- All material conditions that must hold for Yes are specified on the event page.
- The market itself is already pricing a high-probability Yes outcome.

## What is uncertain

- The event page does not discuss fallback procedures if Binance chart UI and API are temporarily inconsistent.
- The page does not supply a historical distribution or contextual evidence for how often BTC stays above a threshold over a five-day horizon.
- The event page snapshot of odds can move quickly.

## Why this source may matter

This is the contract source. For an extreme-probability, date-sensitive market, resolution mechanics and exact timing matter enough that they can dominate a loosely framed directional thesis.

## Possible impact on the question

This source does not itself justify Yes or No, but it sharply constrains what evidence is relevant. It supports a disciplined base-rate approach: start from current spot versus strike and then ask how often BTC loses more than about 6% over five days and ends below the threshold at the exact resolution minute.

## Reliability notes

High credibility for contract interpretation because Polymarket authored the rules. Independence versus Binance price data is medium because Polymarket rules point directly back to Binance as source of truth, so a separate contextual source is still useful for outside-view calibration.