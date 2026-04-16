---
type: source_note
case_key: case-20260414-9c18e804
dispatch_id: dispatch-case-20260414-9c18e804-20260414T135145Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: weekly bitcoin hit-price market
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Polymarket event page and embedded event JSON
source_type: primary market/rules source
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: base-rate
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-9c18e804/researcher-analyses/2026-04-14/dispatch-case-20260414-9c18e804-20260414T135145Z/personas/base-rate.md]
tags: [polymarket, rules, pricing, source-note]
---

# Summary

Primary source for both market-implied probability and resolution mechanics.

## Key facts extracted

- The specific market `will-bitcoin-reach-76k-april-13-19` showed outcomePrices `["0.825","0.175"]` in the embedded page JSON when checked on 2026-04-14, implying roughly 82.5% for Yes.
- Best bid / ask shown in embedded JSON were approximately 0.81 / 0.84.
- Rule text: market resolves Yes if any Binance BTC/USDT 1-minute candle during the title date range has a `High` price equal to or greater than the threshold in the title.
- The rules explicitly exclude other exchanges, other trading pairs, and other spot markets.
- The weekly parent market page also showed neighboring ladder prices: 78k about 44.85-46.6%, 80k about 18.35-19.1%, 82k about 5.85-6.5%, 84k about 2.6-3.5%.

## Evidence directly stated by source

- Governing source of truth is Binance BTC/USDT 1-minute candle highs.
- The market window runs from Apr 13, 2026 to Apr 20, 2026 (title says Apr 13-19; page end date Apr 20 reflects post-window resolution timing / ET boundary handling).
- The contract is threshold-touch based, not end-of-week closing-price based.

## What is uncertain

- The live webpage FAQ text looked internally inconsistent in places, so the embedded structured JSON/rules text is more reliable than the generic FAQ copy.
- The page itself is not an independent source for whether BTC will actually hit the threshold; it is mainly authoritative for contract mechanics and market pricing.

## Why this source may matter

This source settles what counts for resolution and gives the current market-implied baseline that the finding must compare against.

## Possible impact on the question

Because the contract is based on any Binance 1-minute high touching 76k rather than the weekly close, the probability should be materially higher than a naive “BTC ends the week above 76k” framing.

## Reliability notes

High reliability for contract wording and current displayed market pricing. Not independent evidence on future BTC path.