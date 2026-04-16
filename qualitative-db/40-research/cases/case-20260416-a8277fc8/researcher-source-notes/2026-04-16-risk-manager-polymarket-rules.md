---
type: source_note
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 1-minute candle at 12:00 ET on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market rules page
source_type: market rules / resolution source summary
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/risk-manager.md
tags: [polymarket, rules, resolution-source, binance, noon-close]
---

# Summary

Polymarket states that this market resolves based on the Binance SOL/USDT 1-minute candle for 12:00 ET on Apr. 19, 2026, specifically the final **Close** price, not the intraminute high or another exchange.

## Key facts extracted

- The contract resolves **Yes** if the Binance SOL/USDT 1-minute candle for **12:00 ET** on the specified date has a final **Close** price **higher than 80**.
- Otherwise it resolves **No**.
- The stated resolution source is Binance, specifically the SOL/USDT market with **1m** candles selected.
- The rules explicitly say the market is about Binance SOL/USDT, **not other exchanges or trading pairs**.
- Price precision is determined by the number of decimals on the source.

## Evidence directly stated by source

Direct quote anchor from the fetched rules page:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for SOL/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the SOL/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/SOL_USDT with \"1m\" and \"Candles\" selected on the top bar."

## What is uncertain

- The fetched public market page is a Polymarket presentation layer, not the final settlement record itself.
- Binance web UI fetch did not render cleanly through the lightweight web fetch tool, so this note captures the rule text and governing source reference rather than a screenshot of the UI.
- Because the event date has not occurred yet, the qualifying 12:00 ET candle cannot yet be directly verified.

## Why this source may matter

This is the clearest available direct statement of the contract mechanics and governing source, which is crucial because the risk here is primarily contract interpretation and timing, not fundamental ambiguity about what Solana is.

## Possible impact on the question

This source sharply narrows the relevant question: the market is not asking whether SOL trades above 80 at any point before Apr. 19, nor whether other exchanges print above 80, but whether Binance SOL/USDT closes above 80 on the specific 12:00 ET one-minute candle.

## Reliability notes

- Strong for contract wording and intended resolution mechanics.
- Still secondary to the eventual governing Binance candle itself for final settlement.
- Good enough to establish the mechanism that all later evidence must map onto.