---
type: source_note
case_key: case-20260416-63fb3082
dispatch_id: dispatch-case-20260416-63fb3082-20260416T145628Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 68000 on April 21, 2026?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market page and Coinbase BTC-USD spot cross-check
source_type: market_rules_plus_context
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: medium_high
recency: high
stance: neutral
certainty: medium_high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-63fb3082/researcher-analyses/2026-04-16/dispatch-case-20260416-63fb3082-20260416T145628Z/personas/variant-view.md]
tags: [polymarket, resolution-rules, coinbase, source-note]
---

# Summary

This note captures the explicit contract language and an extra verification pass using an independent market-price context source. The rules make clear that only the Binance BTC/USDT 12:00 ET 1-minute candle close matters. Coinbase spot provides independent contextual confirmation that BTC is also trading well above 68,000 across venues, reducing concern that Binance is uniquely elevated at the moment.

## Key facts extracted

- Polymarket shows the 68,000 line trading around 95% (Buy Yes about 95.4 cents on the fetched page).
- Contract resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21 has a final close strictly higher than 68,000.
- Price precision is determined by Binance source decimals.
- Polymarket lists related ladders for the same date (66k at 98%, 70k at 88%, 72k at 71%, 74k at 48%), which implies the market currently centers BTC in the low-to-mid 70k zone by resolution date.
- Coinbase BTC-USD spot cross-check returned about 72,961.27, also comfortably above 68,000.

## Evidence directly stated by source

- The governing source of truth is Binance, not other exchanges.
- The relevant timestamp is 12:00 ET on April 21.
- The threshold test is strictly greater than 68,000, not greater-than-or-equal.
- The market itself is already pricing a very high probability of Yes.

## What is uncertain

- The fetched Polymarket page is a secondary display surface, not the exchange settlement engine.
- Coinbase is a useful independent context source but cannot settle the contract.
- The page does not explain operational edge cases beyond the stated rules.

## Why this source may matter

The rules define what all material conditions are. The Coinbase cross-check matters because it reduces the chance that a current Binance-only price dislocation is creating a false sense of safety.

## Possible impact on the question

Supports a high-Yes view while also highlighting the narrow set of ways the market could still be wrong: a fast drawdown before noon ET, or a Binance-specific settlement/candle issue near the decision window.

## Reliability notes

Polymarket rules are authoritative for contract interpretation but secondary for actual BTC pricing. Coinbase is an independent contextual source with good market relevance, but not the settlement source.