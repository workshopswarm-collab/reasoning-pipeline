---
type: source_note
case_key: case-20260414-76e5614f
dispatch_id: dispatch-case-20260414-76e5614f-20260414T182607Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page plus Binance BTCUSDT API
source_type: market rules plus exchange primary price source
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-76e5614f/researcher-analyses/2026-04-14/dispatch-case-20260414-76e5614f-20260414T182607Z/personas/base-rate.md]
tags: [source-note, polymarket, binance, settlement]
---

# Summary

This source pair established both the contract mechanics and the current reference price environment. The Polymarket market page states the contract resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 and specifically uses the final close price for that minute. Binance API checks confirmed BTCUSDT was trading around 74,573 on 2026-04-14, materially above the 72,000 threshold.

## Key facts extracted

- The contract resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final close strictly higher than 72,000.
- The market is explicitly about Binance BTC/USDT, not other exchanges or pairs.
- Binance BTCUSDT spot was approximately 74,573.11 at the time of checking on 2026-04-14.
- Binance exchange metadata for BTCUSDT shows a price tick size of 0.01, which makes the threshold comparison operationally precise to cents.

## Evidence directly stated by source

- Polymarket directly states the governing source of truth and the exact timing condition.
- Binance ticker and kline endpoints directly provide the current BTCUSDT price and the candle structure used for settlement.

## What is uncertain

- The checked live price is not the settlement price; BTC can move materially before April 17 noon ET.
- I did not independently inspect the Binance web UI candle at the exact future settlement time, only the API structure and live current prices.

## Why this source may matter

This is the governing contract evidence. It defines the exact condition that must hold and confirms the correct exchange/pair. It also anchors the current state of the market relative to the threshold.

## Possible impact on the question

Because the market settles on a specific Binance 1-minute close rather than a broader daily or cross-exchange price, modest intraday deviations or exchange-specific dislocations could matter at the margin. Still, with spot near 74.6k, BTC currently sits about 3.45% above the threshold, so the contract presently looks favored to resolve Yes absent a meaningful drawdown before the deadline.

## Reliability notes

- Polymarket is authoritative for the contract wording but not for the underlying price.
- Binance is authoritative for the underlying settlement price because the contract explicitly names Binance BTC/USDT as source of truth.
- Evidence independence is moderate because the rule source and price source are different surfaces, but the contract intentionally points back to Binance.