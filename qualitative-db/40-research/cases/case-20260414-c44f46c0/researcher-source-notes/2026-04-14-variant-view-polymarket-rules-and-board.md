---
type: source_note
case_key: case-20260414-c44f46c0
dispatch_id: dispatch-case-20260414-c44f46c0-20260414T185449Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-19
question: Will the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-19 close above 68000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market/rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
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
downstream_uses: [variant-view.md, variant-view.sidecar.json, evidence/variant-view.md]
tags: [polymarket, rules, resolution-source, market-baseline]
---

# Summary

This source established both the market-implied baseline and the exact contract mechanics. It is not the underlying settlement source, but it is the authoritative statement of what Polymarket says will count.

## Key facts extracted

- The relevant outcome is the 68,000 threshold leg, trading around 95.5% on the fetched page; assignment context gave current_price 0.9575.
- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 19 has a final Close strictly higher than 68,000.
- The market is specifically tied to Binance BTC/USDT, not other exchanges or other BTC pairs.
- Price precision is determined by the source.

## Evidence directly stated by source

- Rules text explicitly names Binance BTC/USDT candles as the resolution source.
- Rules text explicitly names the 12:00 ET 1-minute candle close as the decisive observation.
- Market board prices show the crowd heavily favors Yes at the 68,000 strike.

## What is uncertain

- The market page does not itself resolve ambiguities about Binance chart display versus API extraction details.
- The page does not independently verify current Binance spot conditions; it only states the contract and shows trader pricing.

## Why this source may matter

The main edge in this case is less about broad bitcoin direction and more about whether an apparently obvious outcome is still being priced with sufficient respect for contract mechanics, timing, and Binance-specific source risk.

## Possible impact on the question

This source makes clear that all of the following must hold for Yes: Binance BTC/USDT remains the operative source, the relevant candle is the one corresponding to 12:00 PM ET on April 19, and that candle’s final close is above 68,000. That narrows the question from a generic “will BTC stay high” view to a specific exchange/time/close-price condition.

## Reliability notes

Useful and necessary for contract interpretation, but not sufficient alone because it is not the underlying Binance data source. Best paired with Binance documentation and live Binance pricing context.