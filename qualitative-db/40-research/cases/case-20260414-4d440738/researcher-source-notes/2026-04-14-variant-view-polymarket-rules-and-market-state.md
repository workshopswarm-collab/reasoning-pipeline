---
type: source_note
case_key: case-20260414-4d440738
dispatch_id: dispatch-case-20260414-4d440738-20260414T195302Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68000-on-april-20
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-20 close above 68000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page and rules
source_type: market/rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4d440738/researcher-analyses/2026-04-14/dispatch-case-20260414-4d440738-20260414T195302Z/personas/variant-view.md]
tags: [polymarket, rules, resolution-source, binance, btc]
---

# Summary

Polymarket's event page shows the current market-implied probability near 94% for "above 68,000" on April 20 and specifies that settlement depends on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET, using the candle's final Close price.

## Key facts extracted

- The visible market price for the 68,000 contract is about 94% Yes.
- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 noon ET on 2026-04-20 has a final Close strictly higher than 68,000.
- The settlement source is Binance, specifically BTC/USDT with 1m candles.
- The contract is exchange-specific and pair-specific; other exchanges or pairs do not govern settlement.
- Price precision is determined by the source display/series.

## Evidence directly stated by source

- The market uses Binance BTC/USDT, not a broader BTC index.
- The relevant observation is the final Close of one specific 1-minute candle, not a daily close, intraday high, or average.
- Noon ET timing is explicit in the rule text.

## What is uncertain

- The fetched page is not itself the authoritative settlement record; it is the contract description pointing to Binance as the source of truth.
- The page does not itself expose the future candle value, only the rule and current market odds.

## Why this source may matter

This is the governing contract/rules surface, so it determines the exact conditions that must all hold for a Yes resolution.

## Possible impact on the question

This source matters because a high spot BTC level alone is insufficient unless Binance BTC/USDT remains above 68,000 at the exact 12:00 ET one-minute candle close on April 20.

## Reliability notes

- Strong for contract wording and market-implied pricing.
- Not sufficient on its own for the actual future settlement value.
- Needs a direct Binance/source-of-truth check and at least one contextual price cross-check.