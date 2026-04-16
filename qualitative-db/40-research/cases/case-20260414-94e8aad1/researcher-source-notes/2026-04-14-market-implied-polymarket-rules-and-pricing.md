---
type: source_note
case_key: case-20260414-94e8aad1
dispatch_id: dispatch-case-20260414-94e8aad1-20260414T175223Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-94e8aad1 | market-implied
question: Will the price of Bitcoin be above $70,000 on April 16?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page for Bitcoin above ___ on April 16?
source_type: market page / contract rules / live pricing
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-pricing, bitcoin]
---

# Summary

Polymarket's event page directly states the contract mechanics and shows the live market price for the $70,000 threshold leg. On fetch at roughly 2026-04-14 17:53Z, the page showed the April 16 market and listed the $70,000 outcome around 96% / Buy Yes 96.2¢, consistent with the assignment's `current_price` of 0.9595.

## Key facts extracted

- The market resolves "Yes" if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final Close price above $70,000.
- The resolution source is Binance, specifically BTC/USDT with `1m` candles selected.
- The event page displayed Apr 16, 2026 as the target date.
- The $70,000 threshold leg was trading around 96.2¢ on the fetched page.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."

## What is uncertain

- The event page is a market surface, not the ultimate settlement source.
- Web extraction is imperfect for dynamic pages, so quoted live price should be treated as a contemporaneous snapshot rather than a canonical time-series export.

## Why this source may matter

This is the direct source for both the market-implied probability and the contract wording that governs what evidence counts.

## Possible impact on the question

It makes the question mostly a short-horizon spot-price-and-timing problem rather than a broad interpretive Bitcoin thesis. Because the market is already pricing ~96%, any non-market view would need strong evidence that BTC could fall below $70,000 by the exact Binance 12:00 ET close candle on April 16, or that the contract mechanics are being misunderstood.

## Reliability notes

Good for contract wording and current market state, but not independent from the market itself. Needs at least one direct Binance check and ideally one external price-context cross-check for auditability.