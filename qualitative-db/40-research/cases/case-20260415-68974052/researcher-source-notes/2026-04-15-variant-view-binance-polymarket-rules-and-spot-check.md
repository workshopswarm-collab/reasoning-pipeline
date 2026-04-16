---
type: source_note
case_key: case-20260415-68974052
dispatch_id: dispatch-case-20260415-68974052-20260415T183011Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-68974052 | variant-view
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance BTCUSDT API spot check
source_type: primary + direct resolution-source verification
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-68974052/researcher-analyses/2026-04-15/dispatch-case-20260415-68974052-20260415T183011Z/personas/variant-view.md]
tags: [polymarket, binance, resolution-source, btc]
---

# Summary

The key direct evidence is the market’s own resolution language and a live verification of the named resolution venue. Polymarket states the contract resolves from the Binance BTC/USDT 1-minute candle at 12:00 ET on April 17, using the candle’s final Close price. A live Binance API spot check on April 15 around 14:32 ET showed BTC/USDT trading near 74.24k, i.e. materially above the 72k threshold with roughly 45.5 hours left until resolution.

## Key facts extracted

- Polymarket rule text says this market resolves to Yes if the Binance 1-minute candle for BTC/USDT at 12:00 ET on April 17 has a final Close above 72,000.
- The rule explicitly names Binance BTC/USDT rather than another exchange or pair.
- Price precision is determined by the source display/record.
- Binance public API spot check at 2026-04-15 ~18:32 UTC showed:
  - ticker price: 74242.30000000
  - recent 1m closes from 18:28 to 18:32 UTC: 74178.40, 74202.93, 74207.84, 74249.99, 74242.30
- CoinGecko simple price endpoint simultaneously showed bitcoin at 74224 USD, broadly confirming the same price region.
- Time-to-resolution check from America/New_York clock was ~45.47 hours from the observation time.

## Evidence directly stated by source

From Polymarket page/rules:
- market resolves on the Binance BTC/USDT 1-minute candle
- relevant candle is the 12:00 ET candle on April 17
- winning condition is final Close strictly higher than 72,000

From Binance API verification:
- BTC/USDT was trading above 72,000 at the time of verification
- recent 1-minute closes remained above 74,100 during the sampled window

## What is uncertain

- Current spot level does not guarantee the April 17 12:00 ET close remains above 72,000.
- API verification confirms the named venue and current price region, but not the exact future resolving candle.
- The direct webpage chart can be less easily machine-fetched than the API endpoints, though the rules explicitly point to Binance as source of truth.

## Why this source may matter

This source pair is the clearest way to verify both contract mechanics and current distance-from-threshold. The contract is narrow and date-sensitive, so confirming the exact source-of-truth venue and condition is more important than broad macro commentary.

## Possible impact on the question

The direct evidence supports a high Yes probability because BTC/USDT is currently ~3.1% above the threshold with less than two days remaining. The most plausible variant-to-consensus risk is not a rules surprise but a late volatility move that pushes the April 17 noon ET Binance close back under 72,000.

## Reliability notes

- Polymarket rules page is the governing contract source for what counts.
- Binance is the named resolution source; direct API outputs are highly relevant for venue verification and current state.
- CoinGecko is only a contextual cross-check, not the source of truth.
- Evidence independence is moderate: Binance and CoinGecko are separate surfaces but both reflect the same underlying market rather than independent causal evidence.