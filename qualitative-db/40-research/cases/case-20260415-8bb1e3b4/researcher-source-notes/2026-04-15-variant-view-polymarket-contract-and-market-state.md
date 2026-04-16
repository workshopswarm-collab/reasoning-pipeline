---
type: source_note
case_key: case-20260415-8bb1e3b4
dispatch_id: dispatch-case-20260415-8bb1e3b4-20260415T150551Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20 contract mechanics and market baseline
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 ET on 2026-04-20 be above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page for Bitcoin above ___ on April 20
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [variant-view.md, variant-view.sidecar.json, evidence/variant-view.md, assumptions/variant-view.md]
tags: [polymarket, contract-rules, market-baseline, resolution-source]
---

# Summary

This source establishes both the market-implied baseline and the formal resolution mechanics. It is the governing contextual source for what counts, especially because the contract is date-specific and keyed to a single Binance 1-minute candle in ET rather than a daily close or cross-exchange average.

## Key facts extracted

- The relevant threshold market is `70,000`, trading around `88¢` Yes on the fetched page, implying roughly `88%` market probability.
- The market resolves `Yes` if the Binance `BTC/USDT` `1 minute candle` for `12:00` in `ET` on `April 20, 2026` has a final `Close` price strictly higher than `70,000`.
- The market resolves `No` otherwise.
- Resolution source is Binance BTC/USDT with `1m` and `Candles` selected.
- The contract is explicitly about Binance BTC/USDT, not other exchanges or other BTC pairs.
- Price precision is determined by the source.

## Evidence directly stated by source

- Market probability baseline for the 70k threshold is very high.
- Settlement depends on one exact timestamped 1-minute close, not intraday highs, not daily close, and not non-Binance reference prices.

## What is uncertain

- The page is not itself the executable settlement record; final settlement still depends on what Binance shows for the specified candle at the specified time.
- The market page does not itself explain edge handling if Binance UI/API presentation changes, though it is still the clearest stated governing source-of-truth surface.

## Why this source may matter

This source is essential because a variant case here is less about broad Bitcoin direction and more about whether the market is overconfident relative to the exact settlement mechanics. A single 1-minute candle introduces path dependence and timing risk that can matter even if Bitcoin remains broadly bullish.

## Possible impact on the question

It supports a modestly more cautious view than a naïve spot-price reading would imply: Bitcoin can be above 70k now and still miss a single noon ET 1-minute close five days later.

## Reliability notes

- Strong for contract wording and market baseline because it is the host market page.
- Not sufficient alone for final price-direction assessment because it is not independent of the market and not the settlement datapoint itself.
