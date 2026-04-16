---
type: source_note
case_key: case-20260415-c8d6e83e
dispatch_id: dispatch-case-20260415-c8d6e83e-20260415T151858Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: markets
entity:
topic: polymarket-contract-and-pricing
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 68000 on April 20, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: prediction_market_rule_page
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-c8d6e83e/researcher-analyses/2026-04-15/dispatch-case-20260415-c8d6e83e-20260415T151858Z/personas/risk-manager.md]
tags: [source-note, polymarket, contract, pricing]
---

# Summary

This source note captures the market-implied baseline and the exact contract mechanics from the Polymarket page.

## Key facts extracted

- The 68,000 line was trading around 95% / 96¢ Yes at the time of fetch, consistent with the assignment's `current_price: 0.955`.
- The market resolves Yes if the Binance BTC/USDT one-minute candle for `12:00` in ET on April 20 has a final close above 68,000.
- The contract is explicitly about Binance BTC/USDT, not other exchanges or other pairs.
- Price precision is determined by the source.

## Evidence directly stated by source

- Resolution text names Binance as the governing source of truth.
- The event page shows a very high implied probability for the 68k threshold.
- The rule is multi-condition: the correct date, ET noon minute, Binance venue, BTC/USDT pair, and final close field all matter.

## What is uncertain

- The fetched page is a rendered public market page, not a formal downloadable rulebook artifact.
- The page does not itself discuss operational contingencies like exchange outages or UI/API discrepancies.

## Why this source may matter

This is the market's own rule surface and pricing surface. It is necessary both for interpreting the contract and for assessing whether current market confidence looks too high versus the actual narrow resolution mechanics.

## Possible impact on the question

The page supports a strong baseline that Yes is favored, but it also highlights the main risk-manager concern: a 95.5% market can still underprice narrow resolution failure modes when the rule depends on one exact minute, one venue, and one field.

## Reliability notes

- High credibility for current market pricing and displayed rules.
- Independence from Binance is medium at best: it is authoritative for the contract wording, but not for the underlying price source itself.