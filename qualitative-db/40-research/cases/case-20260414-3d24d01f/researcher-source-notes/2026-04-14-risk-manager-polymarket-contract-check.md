---
type: source_note
case_key: case-20260414-3d24d01f
dispatch_id: dispatch-case-20260414-3d24d01f-20260414T184328Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-3d24d01f | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 19?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market contract / primary rules source
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3d24d01f/researcher-analyses/2026-04-14/dispatch-case-20260414-3d24d01f-20260414T184328Z/personas/risk-manager.md]
tags: [polymarket, contract, resolution, timestamp-risk]
---

# Summary

The Polymarket rules make this a narrow-resolution market: Yes requires the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 19 to have a final close strictly higher than 70,000. This is not a generic "BTC trades above 70k sometime that day" question.

## Key facts extracted

- Resolution is based on the Binance BTC/USDT 1-minute candle.
- The relevant candle is specifically the 12:00 ET candle on April 19.
- The final close price of that candle must be higher than 70,000.
- Binance venue/pair matters; other exchanges and other pairs do not count.
- Price precision is determined by Binance's displayed precision.
- Current market price on the Polymarket runner was about 0.89 for the 70,000 line at fetch time.

## Evidence directly stated by source

- The page directly stated the rules and source of truth.
- The page directly showed the market-implied probability for the 70,000 threshold near 89%-90%.

## What is uncertain

- The phrase "12:00 in the ET timezone (noon)" could create minor user confusion about whether the relevant one-minute candle is labeled 12:00 or ends at 12:00:59, though operationally this usually maps cleanly to the 12:00 minute candle close.
- The fetched page is not an official Binance rulebook; it is the contract wrapper that points to Binance as governing source.

## Why this source may matter

This is the governing contract source, so it defines the exact thing being forecast and the exact timestamp/venue constraints.

## Possible impact on the question

It raises the importance of timing and venue-specific operational risk. Any analysis that only cites a broad BTC/USD spot price without checking Binance BTC/USDT and noon ET mechanics would be incomplete.

## Reliability notes

High reliability for contract interpretation because this is the market's own rules page. It does not answer the future price outcome; it only defines what counts.