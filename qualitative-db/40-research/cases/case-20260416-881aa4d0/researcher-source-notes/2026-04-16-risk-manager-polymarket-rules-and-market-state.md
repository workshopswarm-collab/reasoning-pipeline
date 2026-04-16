---
type: source_note
case_key: case-20260416-881aa4d0
dispatch_id: dispatch-case-20260416-881aa4d0-20260416T044756Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-881aa4d0 | risk-manager
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close on April 17, 2026 be above 70000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market contract / resolution rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-881aa4d0/researcher-analyses/2026-04-16/dispatch-case-20260416-881aa4d0-20260416T044756Z/personas/risk-manager.md]
tags: [polymarket, contract-rules, market-implied-probability, resolution-source]
---

# Summary

This source establishes the contract mechanics, the named source of truth, and the market-implied baseline relevant to the case.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 17, 2026 has a final close above 70,000.
- The market specifically names Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the number of decimals shown in the source.
- The visible Polymarket market state showed the 70,000 line trading around 99.0% Yes at capture time.

## Evidence directly stated by source

- Resolution source is Binance, specifically the BTC/USDT candles view with 1m selected.
- The relevant observation is the final close of the 12:00 ET minute candle on the date specified.
- Outcome depends on a strict greater-than condition, not greater-than-or-equal.

## What is uncertain

- The Polymarket web page is not itself the authoritative settlement source; it only points to Binance as that source.
- The page snapshot does not independently verify the actual Binance candle that will exist at settlement time.
- Polymarket display formatting can be noisy in scraped output, so market state should be treated as indicative for baseline probability, not as an auditable trade ledger.

## Why this source may matter

It defines the exact resolution mechanics and shows that this is a rule-sensitive, time-specific market where exchange-specific operational details matter.

## Possible impact on the question

The source materially narrows the question: broad BTC bullishness is insufficient by itself. For Yes to resolve, all of the following must hold: Binance must remain the operative source, the relevant candle must be the 12:00 ET one-minute candle on April 17, the BTC/USDT close used by Binance must be final, and that final close must exceed 70,000.

## Reliability notes

Useful for contract interpretation and market baseline, but not sufficient alone for final truth. It is best paired with a direct Binance surface or API check for contextual verification.