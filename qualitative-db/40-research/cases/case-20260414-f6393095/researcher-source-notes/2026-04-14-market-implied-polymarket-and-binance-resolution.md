---
type: source_note
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-f6393095 | market-implied
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page and gamma API for bitcoin-above-on-april-17
source_type: market page / market API
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260414-f6393095/researcher-analyses/2026-04-14/dispatch-case-20260414-f6393095-20260414T222237Z/personas/market-implied.md
  - qualitative-db/40-research/cases/case-20260414-f6393095/researcher-analyses/2026-04-14/dispatch-case-20260414-f6393095-20260414T222237Z/evidence/market-implied.md
tags: [polymarket, market-structure, resolution-rules, binance]
---

# Summary

Polymarket's event page and its gamma API show that the April 17 ladder market is structured around Binance BTC/USDT 1-minute candle close prices at 12:00 ET, and the specific $70,000 leg is trading around 93.5%-93.9% Yes on 2026-04-14. This source is the clearest direct statement of both the market-implied probability and the contract mechanics the market is pricing.

## Key facts extracted

- Event title: "Bitcoin above ___ on April 17?"
- Market description states resolution is based on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17.
- Outcome resolves Yes only if the final Close is higher than the stated threshold.
- The $70,000 contract was available as the slug `bitcoin-above-70k-on-april-17`.
- Polymarket page showed roughly 93% / Buy Yes 93.9¢ for the $70,000 strike at fetch time.
- Gamma API listing showed outcomePrices for the $70,000 market at `["0.935", "0.065"]` in the assignment context and around 0.939 on the public page snapshot.
- Event endDate / next update time corresponds to 2026-04-17 16:00:00Z, which is 12:00 ET.

## Evidence directly stated by source

- Contract wording: Yes iff Binance BTC/USDT 12:00 ET 1-minute candle final Close is above $70,000.
- Source-of-truth venue: Binance, not other exchanges or other BTC pairs.
- Price precision is determined by Binance source decimals.
- Current market-implied probability is in the low-to-mid 90s.

## What is uncertain

- Public page and API snapshots can move slightly minute to minute.
- Polymarket itself is not the final settlement source for the underlying BTC price; it is the contract venue describing how settlement will happen.
- The page does not by itself prove Binance continuity or absence of exchange-specific anomalies at the resolution minute.

## Why this source may matter

This is the core direct evidence for what the market currently implies and what exact conditions the market is pricing. It also narrows resolution ambiguity by making the noon ET candle, exchange venue, pair, and field (Close) explicit.

## Possible impact on the question

If the market is around 93.5%-93.9% Yes while spot BTC/USDT is already above $74k, then traders are effectively pricing only a modest chance of a >$4k drop over roughly 2.5 days or a Binance-specific settlement anomaly.

## Reliability notes

- Strong for market state and rule wording because it is the venue hosting the contract.
- Not sufficient alone for the underlying price path; must be paired with an independent price source or direct Binance market data.
- Evidence independence versus Binance is medium, because Polymarket contract wording itself points back to Binance as source of truth.