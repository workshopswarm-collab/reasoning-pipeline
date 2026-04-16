---
type: source_note
case_key: case-20260415-3f432366
dispatch_id: dispatch-case-20260415-3f432366-20260415T074424Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market rules / market-implied odds
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [variant-view-finding]
tags: [polymarket, market-rules, market-implied-probability, resolution-source]
---

# Summary

Polymarket's event page provides both the tradable market-implied probability for the $72,000 threshold and the governing resolution mechanics. For this case, the page showed the $72,000 line trading around 75-76% Yes on 2026-04-15, and it specifies a narrow source-of-truth condition: the final close of the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 17.

## Key facts extracted

- The April 17 "$72,000" contract was trading about 75-76% Yes on the event page at fetch time.
- The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 PM ET on April 17 has a final close price strictly higher than 72,000.
- The governing source is Binance BTC/USDT with 1m candles, not another exchange or another pair.
- Price precision follows Binance's displayed source precision.
- The event page also displayed neighboring thresholds around the focal contract: 70k around 93% Yes and 74k around 45% Yes, which implies the market sees 72k as near the middle of the plausible range rather than an extreme tail.

## Evidence directly stated by source

- Resolution source: Binance BTC/USDT 1-minute candle close.
- Timing convention: 12:00 PM ET on the specified date.
- Threshold condition: close price must be higher than 72,000, not equal.
- Market-implied odds snapshot: roughly 75-76% Yes for the 72k line.

## What is uncertain

- The fetched page is a live market surface, so probabilities can move after fetch time.
- The page does not by itself provide a statistical model for expected BTC movement; it only gives consensus pricing and contract wording.
- The page wording references the candle "currently available" on Binance, leaving some residual operational ambiguity if Binance UI presentation changes, although the intended source-of-truth is still clear.

## Why this source may matter

This is the primary source for both the consensus baseline and the exact contract mechanics. Because the contract is narrow, date-sensitive, and source-specific, rule interpretation is material rather than boilerplate.

## Possible impact on the question

This source anchors the entire analysis. It confirms that the relevant question is not whether BTC is broadly bullish, but whether Binance BTC/USDT remains above 72,000 at one exact minute-close on April 17 noon ET. That makes timing, threshold distance, and exchange-specific operational considerations more important than a generic directional BTC view.

## Reliability notes

Useful and necessary as the governing market and contract source. Credibility is medium-high for rules and current market pricing, but not independent evidence on where BTC will actually trade; it must be paired with external price/context data.