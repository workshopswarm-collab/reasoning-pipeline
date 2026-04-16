---
type: source_note
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: daily-threshold-close
entity: sol
topic: Binance SOL/USDT noon-ET close-above-$80 resolution surface and current spot context
question: Will the Binance SOL/USDT 1-minute candle at 12:00 ET on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance public API plus Polymarket market rules page
source_type: primary_market_rule_and_authoritative_resolution_surface
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/catalyst-hunter.md
tags: [binance, polymarket, resolution-surface, sol]
---

# Summary

Primary note for this case’s governing source and contract mechanics. The market resolves from the Binance SOL/USDT 1-minute candle at 12:00 ET on Apr 19, 2026, using the final **close** price, not intraday high, not another exchange, and not another pair. A direct Binance API spot check on Apr 15/16 UTC showed SOL/USDT around 84.67, which is above the $80 threshold today but does **not** itself settle the contract because the relevant observed value is only the Apr 19 12:00 ET close.

## Key facts extracted

- Polymarket rules state: resolve Yes if the Binance SOL/USDT 1-minute candle for 12:00 in ET timezone on the specified date has a final close price higher than the listed threshold.
- The market is specifically about Binance SOL/USDT, not other exchanges or pairs.
- Price precision is determined by the source.
- Current Polymarket market page showed the Apr 19 $80 leg trading around 89% at capture time.
- Direct Binance public API check returned `{"symbol":"SOLUSDT","price":"84.67000000"}`.
- Direct Binance 1-minute klines API check returned recent closes in the 84.67-84.74 area, confirming the pair was trading above $80 at the time of verification.
- The relevant decision timestamp is Sunday, Apr 19, 2026 at 12:00 ET = 16:00 UTC.

## Evidence directly stated by source

From Polymarket rules page:
- Yes if Binance SOL/USDT 1 minute candle for 12:00 ET on the date in title has a final close price higher than $80.
- Resolution source is Binance with 1m Candles selected.
- This is not based on other exchanges or trading pairs.

From direct Binance API calls:
- Current spot and last few 1-minute candles were above $80 during the Apr 16 verification pass.

## What is uncertain

- Current spot above $80 does not prove the Apr 19 noon-ET candle will also close above $80.
- The Binance website candle UI, rather than the API, is named in the rules text; while the API is strong contextual verification for the same market, final settlement still depends on the Binance resolution surface as interpreted by Polymarket.
- Short-dated crypto volatility could still move SOL below $80 by the relevant minute close.

## Why this source may matter

This is the core source-of-truth note. It pins down the exact event, exact exchange, exact pair, exact timing, and exact field that matters. It also shows that the current market price is not detached from spot reality: SOL is presently above the threshold by about $4.67, or roughly 5.8%.

## Possible impact on the question

The source strongly supports a high Yes probability because the asset is already trading comfortably above the threshold with roughly three days remaining. It also narrows the risk to the actual mechanism that matters: whether SOL/USDT is still above $80 at the precise Binance 12:00 ET one-minute close on Apr 19.

## Reliability notes

- Polymarket rules page is the primary contract-mechanics source and therefore high credibility.
- Binance public API is a strong direct contextual verification surface for current price and current 1-minute candles, but it is not by itself the final settlement observation for Apr 19 noon ET.
- Evidence independence is medium: both sources are linked by the same underlying venue mechanics, but they serve different roles (contract wording vs current market state).
- Source-of-truth ambiguity is low-to-medium: the governing source is clear, but the rules refer to Binance’s trade interface candle display rather than explicitly to the API endpoint.