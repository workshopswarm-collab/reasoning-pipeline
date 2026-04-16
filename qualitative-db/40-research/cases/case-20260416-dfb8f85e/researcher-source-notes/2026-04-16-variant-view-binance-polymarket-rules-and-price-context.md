---
type: source_note
case_key: case-20260416-dfb8f85e
dispatch_id: dispatch-case-20260416-dfb8f85e-20260416T140232Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and Binance BTCUSDT daily/market data
source_type: primary_plus_direct_market_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, resolution, btc]
---

# Summary

This source note captures the contract mechanics and immediate market context for the April 21 BTC > $72,000 question. The most important direct facts are that resolution depends on the Binance BTC/USDT 1-minute candle close at 12:00 ET on April 21, and the market-implied probability for the $72,000 threshold was about 79-80% on April 16. Separate direct Binance market data showed BTC daily closes recently moving from the high-$60ks into the mid-$70ks, including closes above $72,000 on April 13-16.

## Key facts extracted

- Polymarket rules specify a "Yes" resolution only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21 has a final close strictly higher than 72,000.
- The governing source of truth is Binance BTC/USDT, not other exchanges or BTC pairs.
- The market page showed the April 21 $72,000 contract around 79-80% Yes on April 16.
- Binance daily candles for 2026-04-13 through 2026-04-16 closed at approximately 74,417.99, 74,131.55, 74,809.99, and 73,705.05 respectively.
- Binance daily candles also show the market has recently traded materially below 72,000 intraday; for example 2026-04-12 had a low near 70,505.88 despite opening above 73,000.

## Evidence directly stated by source

- From Polymarket rules: resolution is based on the Binance BTC/USDT 1-minute candle close at 12:00 ET on April 21.
- From Polymarket market display: the $72,000 line was priced around 79-80% Yes.
- From Binance market data: BTC/USDT daily candles over the last several days have mostly closed above 72,000, but with nontrivial realized volatility.

## What is uncertain

- Daily candles do not directly settle the exact noon ET 1-minute close on April 21.
- The Binance webpage itself was not fetchable in readable text form, so direct exchange data was obtained through Binance API market data rather than the web page UI.
- There remains event risk over the next five days that could move BTC several percent.

## Why this source may matter

This is the core resolution and baseline-context source. It defines the exact contract conditions and anchors whether the market is likely over- or underestimating the probability that BTC stays above the threshold at the exact settlement minute.

## Possible impact on the question

The direct source supports a moderately bullish baseline because spot BTC is already above $72,000 by a comfortable but not overwhelming margin. However, because the contract is settled on one exact minute from one exchange, realized volatility and timestamp/exchange specificity make the contract more fragile than a simple "BTC around $74k today" narrative suggests.

## Reliability notes

- Contract mechanics from Polymarket are authoritative for how the market resolves.
- Binance API market data is highly relevant direct price evidence, though the specific authoritative settlement reference remains the Binance interface / underlying Binance BTCUSDT data at the specified minute.
- Independence is limited because both the contract and the price source revolve around Binance; this is acceptable here because Binance is explicitly the source of truth.