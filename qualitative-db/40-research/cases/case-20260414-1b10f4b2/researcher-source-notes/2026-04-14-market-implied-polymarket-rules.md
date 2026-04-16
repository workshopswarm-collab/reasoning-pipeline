---
type: source_note
case_key: case-20260414-1b10f4b2
dispatch_id: dispatch-case-20260414-1b10f4b2-20260414T201759Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-1b10f4b2 | market-implied
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-20 above 68000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page and rules
source_type: market rules / primary market source
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-1b10f4b2/researcher-analyses/2026-04-14/dispatch-case-20260414-1b10f4b2-20260414T201759Z/personas/market-implied.md]
tags: [polymarket, rules, resolution, market-implied]
---

# Summary

Polymarket lists the April 20 ladder market with the 68,000 line priced around 94%, and the rules specify that resolution depends on the Binance BTC/USDT 1-minute candle at exactly 12:00 ET on April 20, 2026, using the final close price.

## Key facts extracted

- The 68,000 outcome was displayed at roughly 94% on 2026-04-14.
- The market resolves "Yes" if the Binance BTC/USDT 12:00 ET one-minute candle on the specified date has a final close higher than 68,000.
- Resolution is exchange-specific: Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the decimals shown by the source.

## Evidence directly stated by source

- The rules directly identify Binance BTC/USDT 1m candles as the governing source of truth.
- The page directly displayed the current contract pricing ladder, including the 68,000 level.

## What is uncertain

- The fetched page is a web rendering of the event page rather than a signed API export.
- The page does not itself prove the future noon close; it only defines the contract and current market view.

## Why this source may matter

This is the primary source for both the market-implied probability and the contract interpretation. For this case, misunderstanding the exact noon ET one-minute close condition would be a material research error.

## Possible impact on the question

It anchors the market prior at about 94% and sharply narrows the operative question to whether BTC/USDT on Binance stays above 68,000 at one precise minute, not merely whether spot BTC trades above that level generally around April 20.

## Reliability notes

Reliable for contract wording and displayed market pricing, but not sufficient alone for the directional forecast because it is not independent evidence about where BTC will trade on April 20.