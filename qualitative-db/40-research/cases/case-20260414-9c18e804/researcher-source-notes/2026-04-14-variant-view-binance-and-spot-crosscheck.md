---
type: source_note
case_key: case-20260414-9c18e804
dispatch_id: dispatch-case-20260414-9c18e804-20260414T135145Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: will-bitcoin-reach-76k-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Binance BTCUSDT API and Coinbase/CoinGecko spot cross-check
source_type: exchange + market data APIs
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-9c18e804/researcher-analyses/2026-04-14/dispatch-case-20260414T135145Z/personas/variant-view.md]
tags: [binance, coinbase, coingecko, btc, threshold-proximity]
---

# Summary

This source note captures the direct settlement-relevant price context and a secondary spot cross-check.

## Key facts extracted

- Binance 24h ticker for BTCUSDT showed last price about `75,342.56`, 24h high about `75,397.00`, low about `71,333.08`, and +5.621% over 24h at observation time.
- Coinbase spot API showed BTC-USD around `75,426.805`.
- CoinGecko market data API showed BTC current price around `75,358`, high_24h around `75,216`, low_24h around `71,375`, and +5.579% over 24h with last_updated `2026-04-14T13:53:38Z`.
- The settlement-relevant gap from observed Binance high to the target was roughly $603.

## Evidence directly stated by source

- BTC had already rallied sharply into the mid-$75k range within the first part of the weekly window.
- The target is close in absolute terms: less than 1% above the observed Binance 24h high at capture time.

## What is uncertain

- The 24h ticker high is not the same thing as the maximum 1-minute high across the entire Apr 13-19 window; later moves could still invalidate the snapshot.
- Coinbase and CoinGecko are contextual cross-checks only; they are not the settlement source.

## Why this source may matter

This is the key direct evidence for whether the target is realistically within reach during the remaining window.

## Possible impact on the question

A market only needing one 1-minute print at $76,000 looks more plausible when BTC is already trading around $75.3k-$75.4k after a strong daily move. The variant angle is that the threshold is near enough that momentum plus ordinary intraday volatility may be sufficient even without a broader macro catalyst.

## Reliability notes

- Binance is the strongest direct source because it is also the contract’s stated settlement venue.
- Coinbase and CoinGecko are useful independent context checks that the move is not a single stale print artifact on one interface.