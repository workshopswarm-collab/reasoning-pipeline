---
type: source_note
case_key: case-20260415-d63a2806
dispatch_id: dispatch-case-20260415-d63a2806-20260415T175526Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Binance noon ET close-above threshold for BTC/USDT on Apr 17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page + Binance API spot/klines cross-check
source_type: primary_contract_and_governing_source_context
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: supports_yes
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-d63a2806/researcher-analyses/2026-04-15/dispatch-case-20260415-d63a2806-20260415T175526Z/personas/market-implied.md
tags: [source-note, polymarket, binance, btc, threshold-market]
---

# Summary

This source note combines the market contract text from Polymarket with a direct Binance API cross-check for current BTC/USDT pricing context. It is the main source for the governing mechanism and for the fact that BTC/USDT was already trading materially above 72,000 at research time.

## Key facts extracted

- Polymarket states the contract resolves **Yes** if the **Binance BTC/USDT 1-minute candle at 12:00 ET on Apr 17** has a final **Close** price **higher than 72,000**.
- The governing source is explicitly **Binance BTC/USDT**, not another exchange or another pair.
- The relevant condition is **close-above**, not touch-above and not day-high-above.
- Binance API spot check during research showed BTC/USDT around **74,130**.
- Recent Binance 1-minute candles and CoinGecko spot context were broadly consistent with BTC trading around **74.1k** at the time of review.

## Evidence directly stated by source

- The contract wording on Polymarket directly states the settlement mechanism and source of truth.
- Binance API directly states recent BTC/USDT spot and 1-minute candle values.

## What is uncertain

- This source does not establish where BTC/USDT will be at the exact resolving minute on Apr 17.
- A current price above 72,000 does not guarantee the Apr 17 noon ET close will stay above 72,000.
- Web fetch of Binance frontend itself was not cleanly extractable in this environment, so the governing-source context is taken from the contract wording plus Binance public API rather than a saved frontend screenshot.

## Why this source may matter

- It cleanly resolves the mechanism-sensitive question that matters most: what has to happen, on which venue, at what timestamp, and using which field.
- It also shows the market is pricing a contract where the asset is already above the threshold by roughly 2k+, which helps explain why the market is at an elevated probability.

## Possible impact on the question

- This source supports a **Yes-leaning** view because BTC/USDT is already above the strike with roughly two days remaining.
- It also limits overconfidence because the market requires a **specific one-minute close** at a future timestamp, so path risk and closing-minute volatility still matter.

## Reliability notes

- Contract text is the highest-value source for mechanism/rules.
- Binance public API is a strong direct contextual source for current price but is not by itself proof of the final resolving candle.
- Independence is only moderate because both pieces revolve around the same core surface; a broader contextual source is still useful for market-environment cross-checking.
