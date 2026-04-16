---
type: source_note
case_key: case-20260414-b6293fe0
dispatch_id: dispatch-case-20260414-b6293fe0-20260414T001837Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: spot-price-thresholds
entity: btc
topic: bitcoin-weekly-threshold
question: Will Bitcoin reach $74,000 April 13-19?
date_created: 2026-04-14
source_name: CoinGecko Bitcoin history API and Coinbase spot check
source_type: api_snapshot
source_url: https://api.coingecko.com/api/v3/coins/bitcoin/history?date=14-04-2026&localization=false
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [btc, threshold, provenance, verification]
---

# Summary
This source note preserves the direct external price checks used for the base-rate view. CoinGecko historical daily snapshots show BTC around $70.8k on Apr 13 and about $74.5k on Apr 14, while a live Coinbase spot check was around $74.37k during research.

## Key facts extracted
- CoinGecko Bitcoin history for 2026-04-13 returned `market_data.current_price.usd = 70756.75105500016`.
- CoinGecko Bitcoin history for 2026-04-14 returned `market_data.current_price.usd = 74514.63006655`.
- A live Coinbase BTC-USD spot endpoint check during research returned `74370.945` USD.
- These are not guaranteed Polymarket settlement sources, but they strongly indicate that BTC was already trading in the mid-$74k area during the market window.

## Evidence directly stated by source
- CoinGecko directly states the historical daily USD price snapshots for Bitcoin on the queried dates.
- Coinbase directly states a live BTC-USD spot price quote.

## What is uncertain
- CoinGecko historical daily values are daily snapshots, not an explicit intraday high series.
- Coinbase is not necessarily the exact governing source for Polymarket resolution here.
- The public Polymarket page fetched via readability did not expose the detailed rule text cleanly.

## Why this source may matter
If BTC is already around or above $74k on major reference venues at the start of the April 14 trading day, then the threshold has likely already been reached or is at least extremely close to being reached within the Apr 13-19 window. That makes a high base-rate probability reasonable unless Polymarket uses a narrow or unusual resolution source.

## Possible impact on the question
This source materially supports a high probability that the threshold gets hit during the weekly window and supports a view at or above the market-implied 89% baseline, while still leaving a small tail risk around source-of-truth mechanics.

## Reliability notes
- CoinGecko is a strong contextual price aggregator but not an official settlement source.
- Coinbase is a strong exchange spot reference but also not proven here to be the governing source of truth.
- Independence is moderate because the two price checks come from different services, but both depend on the same broad BTC spot market reality.