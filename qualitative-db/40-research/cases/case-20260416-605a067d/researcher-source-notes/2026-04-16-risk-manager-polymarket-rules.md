---
type: source_note
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: daily-threshold-close
entity: ethereum
topic: Binance noon ET close-above threshold mechanics for ETH/USDT
question: Will the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 close above 2200?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market rules page
source_type: market rules / primary contract source
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/risk-manager.md
tags: [source-note, polymarket, binance, resolution-rules, noon-close]
---

# Summary

Primary contract source confirms this is a narrow, source-sensitive close-above market. It resolves from the Binance ETH/USDT 1-minute candle for **12:00 ET on April 17** using the final **Close** price, not intraday highs, not other exchanges, and not other pairs.

## Key facts extracted

- The market resolves **Yes** only if the Binance ETH/USDT 1-minute candle for **12:00 ET (noon)** on the specified date has a final **Close** price higher than **2200**.
- The governing source is Binance, specifically the ETH/USDT chart with **1m** candles selected.
- The rule explicitly says this is **not** about other exchanges or other trading pairs.
- Price precision is determined by the source.
- The visible market snapshot showed the 2200 line trading around **91.5¢ Yes / 9.9¢ No**, consistent with the assignment's current price of **0.871** as a high market-implied Yes probability.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for ETH/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the ETH/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/ETH_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance ETH/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The rules page does not itself provide the future April 17 noon candle result.
- The fetched HTML is a webpage rendering, not an independently archived proof object for later settlement review.
- The page shows current market prices, but those prices are not themselves governing evidence.

## Why this source may matter

This is the primary contract-definition source. It determines the exact mechanism, timing, timezone, and exchange specificity. It materially lowers interpretation ambiguity versus a generic "ETH above 2200" framing.

## Possible impact on the question

The rule framing makes the question easier than a full-day close but narrower than an intraday touch market. A trader only needs ETH/USDT on Binance to be above 2200 on the specific **12:00 ET one-minute close**, so the key risks are timing/path dependence around noon, exchange-specific deviations, and last-hour reversal risk.

## Reliability notes

- High reliability for contract wording and governing-source identification.
- Lower value for directional pricing by itself, since it does not supply the actual future noon close.
- Because the market is date-sensitive and source-sensitive, this source should be paired with a direct Binance data check and an explicit timezone check before finalizing.