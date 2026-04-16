---
type: source_note
case_key: case-20260414-9f18b170
dispatch_id: dispatch-case-20260414-9f18b170-20260414T142057Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-9f18b170 | risk-manager
question: Will Bitcoin reach $76,000 April 13-19?
driver: liquidity
date_created: 2026-04-14
source_name: Coinbase spot, Kraken ticker, CoinGecko market snapshot
source_type: market_data_context
source_url: https://api.coinbase.com/v2/prices/BTC-USD/spot
source_date: 2026-04-14
credibility: medium
recency: live
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [liquidity, macro]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-9f18b170/researcher-analyses/2026-04-14/dispatch-case-20260414-9f18b170-20260414T142057Z/personas/risk-manager.md]
tags: [coinbase, kraken, coingecko, price-context, verification]
---

# Summary

Independent live spot references showed BTC already trading around or modestly above the $76k threshold at research time, materially supporting a high Yes probability even though settlement depends specifically on Binance BTC/USDT 1-minute highs.

## Key facts extracted

- Coinbase spot API returned BTC-USD around 75,765.355.
- Kraken XBT/USD ticker returned last trade around 75,761.7 and day high around 75,761.7.
- CoinGecko market snapshot returned current_price around 75,670 with high_24h around 75,596 and 24h low around 71,547.
- These readings cluster just below or around 76k depending on venue and timestamp, implying the remaining distance to threshold is very small.

## Evidence directly stated by source

- Coinbase API: `{"data":{"amount":"75765.355","base":"BTC","currency":"USD"}}`
- Kraken API included last trade `c:["75761.70000", ...]` and high `h:["75761.70000", ...]`
- CoinGecko API showed `current_price":75670` and `high_24h":75596`

## What is uncertain

- These are not Binance BTC/USDT settlement values.
- Minor inter-venue basis means being above 76k on one venue does not guarantee a Binance 1-minute High at or above 76k at the same instant.
- CoinGecko is an aggregate/derived feed, not a direct settlement source.

## Why this source may matter

These checks provide the required extra verification pass and establish that the market is not pricing an implausible long-distance move. The contract is close enough to current spot that only modest continuation or brief exchange-specific overshoot is needed.

## Possible impact on the question

This source set supports a high Yes view, but it also sharpens the main risk-manager caveat: the residual risk is mostly microstructure / venue-specific path risk rather than broad directional BTC weakness.

## Reliability notes

Useful as independent contextual verification, but secondary to Binance-specific settlement mechanics. Evidence independence is medium because all references derive from the same global BTC market regime, though not from the same exact exchange feed.