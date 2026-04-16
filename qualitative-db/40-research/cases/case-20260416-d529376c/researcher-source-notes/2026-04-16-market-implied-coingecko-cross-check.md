---
type: source_note
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: tokens
entity: sol
topic: case-20260416-d529376c | market-implied
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close be above 80 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-16
source_name: CoinGecko Solana price cross-check
source_type: market_data_aggregator
source_url: https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: medium
novelty: low
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-d529376c/researcher-analyses/2026-04-16/dispatch-case-20260416-d529376c-20260416T030247Z/personas/market-implied.md]
tags: [source-note, crypto, coingecko, cross-check, sol]
---

# Summary

Secondary contextual source used for an extra verification pass. CoinGecko showed Solana at about 85.2 USD with positive 24-hour change, closely matching the direct Binance read.

## Key facts extracted

- CoinGecko simple price endpoint returned Solana at `85.2` USD.
- CoinGecko returned `usd_24h_change` of about `2.24%`.
- The level was very close to the Binance direct ticker read (~85.27), reducing concern that the Binance fetch was stale or anomalous.

## Evidence directly stated by source

- Solana was trading in the mid-85s in the broader market at fetch time.
- The 24-hour change was positive rather than sharply negative.

## What is uncertain

- CoinGecko is not the settlement source and may aggregate across venues.
- A broad-market spot cross-check does not answer the exact Binance noon-ET candle outcome on April 19.

## Why this source may matter

This is an independence and sanity-check source. It helps confirm that the direct Binance observation was not a one-off scrape artifact and that market context around the fetch time was consistent with SOL already being comfortably above the strike.

## Possible impact on the question

The cross-check modestly supports the market’s high-confidence stance by confirming that SOL is not merely barely above 80 on one venue; it appears broadly in the mid-80s.

## Reliability notes

- Useful as a verification source, not as the governing source of truth.
- Independence is partial rather than complete because crypto spot references co-move and may share exchange inputs.
- Best used as contextual confirmation rather than dispositive evidence.