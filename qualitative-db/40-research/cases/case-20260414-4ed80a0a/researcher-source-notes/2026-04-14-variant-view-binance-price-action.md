---
type: source_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: protocols
entity: ethereum
topic: ethereum weekly threshold market
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-14
source_name: Binance ETHUSDT API snapshot and recent hourly candles
source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: variant-view
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/variant-view.md]
tags: [source-note, binance, price-action, threshold-market]
---

# Summary

Direct price evidence from Binance shows ETH already traded above the $2,400 threshold during the relevant 24h window, but this alone does not settle the Polymarket contract because the governing source of truth on the market page was not recoverable through the fetch tool.

## Key facts extracted

- Binance 24h ticker for ETHUSDT returned last price `2330.48`, 24h high `2415.50`, 24h low `2218.53`.
- The same query implies ETH did print materially above $2,400 on Binance during the recent lookback window.
- A second Binance endpoint for hourly candles returned recent 1h OHLC data, confirming active volatility in the low-$2200s into low-$2400s rather than a flat market.

## Evidence directly stated by source

- The exchange-reported high for the 24h period was `2415.50`.
- The exchange-reported last traded price at query time was `2330.48`.

## What is uncertain

- The exact venue and rule Polymarket will use to determine whether ETH "hit" $2,400 was not extractable from the market page via tool fetch.
- Binance high may not match the contract’s official reference venue or oracle.
- The 24h window in the Binance ticker is not perfectly aligned to the market’s April 13-19 wording.

## Why this source may matter

This is the strongest direct evidence that the threshold is plausibly already satisfied on at least one major venue, which explains why the market price is extreme.

## Possible impact on the question

If Polymarket resolves based on a broad or Binance-compatible interpretation of "hit," this evidence strongly favors YES / threshold reached. If the contract uses a narrower source or specific index, this source is only contextual rather than dispositive.

## Reliability notes

Binance API data is direct and recent, but it is venue-specific and therefore only partially authoritative for a contract with unresolved source-of-truth ambiguity.