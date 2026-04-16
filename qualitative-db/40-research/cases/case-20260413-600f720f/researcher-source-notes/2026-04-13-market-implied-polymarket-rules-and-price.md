---
type: source_note
case_key: case-20260413-600f720f
dispatch_id: dispatch-case-20260413-600f720f-20260413T233138Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: prices
entity: btc
topic: will-bitcoin-reach-76k-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-13
source_name: Polymarket event API payload for Bitcoin hit-price weekly market
source_type: primary market source
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-600f720f/researcher-analyses/2026-04-13/dispatch-case-20260413-600f720f-20260413T233138Z/personas/market-implied.md]
tags: [polymarket, rules, resolution, market-implied, binance]
---

# Summary

Primary source for both current market-implied probability and contract interpretation. The event payload shows the exact submarket for $76k with outcome prices around 0.73/0.27 and gives the operative resolution text.

## Key facts extracted

- Target submarket: `Will Bitcoin reach $76,000 April 13-19?`
- Outcome prices at capture: `Yes 0.73`, `No 0.27`; best bid/ask around `0.72 / 0.74`; last trade `0.74`.
- Event-level volume at capture: about `$205.5k`; submarket volume about `$33.6k`.
- Rule text: resolves `Yes` if **any Binance 1-minute BTC/USDT candle** during the stated ET date range has a final **High** `>= 76,000`; otherwise `No`.
- Resolution source is explicitly Binance BTC/USDT 1-minute high prices, not other exchanges or pairs.

## Evidence directly stated by source

- Exact contract description:
  - "This market will immediately resolve to 'Yes' if any Binance 1-minute candle for BTC/USDT during the date range specified in the title (from 12:00 AM ET on the first date to 11:59 PM ET on the last) has a final 'High' price equal to or greater than the price specified in the title. Otherwise, this market will resolve to 'No'."
- Exact source-of-truth language:
  - "The resolution source for this market is Binance, specifically the BTC/USDT 'High' prices... with the chart settings on '1m' candles selected..."
- Market price snapshot is directly embedded in the payload as `outcomePrices: ["0.73", "0.27"]` with contemporaneous bid/ask and last trade.

## What is uncertain

- The source note captures a point-in-time probability snapshot only; the market can move materially before the week ends.
- Polymarket does not by itself tell whether 76k is well-calibrated; it only shows what traders are pricing and the rule mechanics.

## Why this source may matter

This is the governing source for contract wording and the cleanest source for the market-implied prior. For a hit-price market, the exact mechanics matter because hitting 76k even briefly on Binance is enough.

## Possible impact on the question

The rule structure is favorable to higher hit probabilities versus a close-based question, because only one qualifying 1-minute spike is needed over a full week. That makes a 70s probability more plausible than it would be for a weekly close-above contract.

## Reliability notes

High reliability for contract mechanics and market price because it is the venue's own event payload. Lower reliability for any generic FAQ text on the page, which appears templated and should not substitute for the specific market description.