---
type: source_note
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: daily-close-thresholds
entity: sol
topic: Binance SOL/USDT direct price and contract mechanics check
question: Will the Binance SOL/USDT 1-minute candle at 12:00 ET on 2026-04-19 close above $80?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance public API + Polymarket market rules page
source_type: exchange_api_and_market_rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-15T20:16:23-04:00
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/variant-view.md
tags: [binance, polymarket, source-note, direct-evidence]
---

# Summary

Direct check of the governing price source family (Binance SOL/USDT) plus the Polymarket rules page. As of 2026-04-15 20:16 EDT, Binance public endpoints showed SOL/USDT around 84.74, already above the $80 threshold, but the contract resolves specifically from the SOL/USDT 1-minute candle with open time 12:00 ET (noon) on 2026-04-19 and its final Close value, not from the spot price at time of research.

## Key facts extracted

- Binance public price endpoint returned `{"symbol":"SOLUSDT","price":"84.74000000"}`.
- Binance 24h ticker returned `lastPrice: 84.74000000`, `highPrice: 85.83000000`, `lowPrice: 82.65000000`.
- Binance 1m kline endpoint returned a latest candle with open time `2026-04-16T00:16:00+00:00`, which maps to `2026-04-15T20:16:00-04:00` in EDT, confirming the exchange data can be aligned to ET for contract timing checks.
- Polymarket rules page states the market resolves Yes if the Binance SOL/USDT 1-minute candle for `12:00` in the ET timezone on the specified date has a final `Close` price higher than the listed threshold.
- Therefore all of the following must hold for Yes: (1) the relevant date is 2026-04-19, (2) the relevant candle is the 12:00 ET 1-minute candle, (3) the governing instrument is Binance SOL/USDT, (4) the final candle Close must be strictly greater than 80.00.

## Evidence directly stated by source

- Direct market price on Binance is above $80 at the time checked.
- The market is close-above on a specific minute close, not a touch/high market and not an end-of-day average.
- The governing source is Binance, not cross-exchange pricing.

## What is uncertain

- The contract does not resolve off the current price; it resolves off a future one-minute close on 2026-04-19 at noon ET.
- The Binance website UI is the named surface in the rules, while this note uses Binance public API endpoints to verify the same instrument and timing structure. That is strong contextual verification but not the final settlement observation.
- Short-dated crypto can move several percent in hours, so being above $80 now does not guarantee the noon ET close on Apr 19 remains above $80.

## Why this source may matter

This is the closest direct evidence available before resolution because it checks the named exchange/instrument rather than relying on third-party aggregators.

## Possible impact on the question

The direct Binance check supports a high Yes probability because SOL is already materially above $80 with roughly 3.7 days remaining, making a drop below $80 by the specific resolution minute possible but not the base case. The main variant-view angle is that the market may still be a bit overconfident because this is a single-minute close condition rather than a touch condition, so intraday weakness exactly at noon ET can still matter.

## Reliability notes

- Binance public endpoints are highly relevant because the contract explicitly names Binance SOL/USDT.
- Polymarket rules page is authoritative for contract interpretation.
- Evidence independence is moderate rather than high because both checks ultimately point back to the same governing source family and market operator wording.
- Strong source for mechanism and current state; not itself final settlement proof.