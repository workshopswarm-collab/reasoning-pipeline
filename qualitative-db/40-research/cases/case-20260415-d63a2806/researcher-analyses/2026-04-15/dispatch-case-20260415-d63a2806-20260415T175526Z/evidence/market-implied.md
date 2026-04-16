---
type: evidence_map
case_key: case-20260415-d63a2806
dispatch_id: dispatch-case-20260415-d63a2806-20260415T175526Z
research_run_id: 9f219832-10ec-44a2-956e-72409b569e55
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "Whether 83.5% for BTC above 72k on Apr 17 noon ET is efficient"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 72000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["threshold-close mechanics"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-d63a2806/researcher-source-notes/2026-04-15-market-implied-binance-polymarket-resolution-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-d63a2806/researcher-analyses/2026-04-15/dispatch-case-20260415-d63a2806-20260415T175526Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "polymarket", "binance"]
---

# Summary

The market price around 83.5% appears mostly defensible because BTC is already trading above the threshold with a meaningful cushion and only needs one exact future minute-close to remain above that line. The main negative is not structural bearish evidence but timing-specific downside path risk over the next two days.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle on Apr 17 close above 72,000?

## Current lean

Lean Yes, with probability a bit below the market but still clearly above 75%.

## Prior / starting view

Start from the market prior of 83.5% because the contract is a short-dated, exchange-specific close-above question and the market ladder likely contains real distribution information.

## Evidence supporting the claim

- **Current Binance BTC/USDT level around 74.1k**  
  - source: source note / Binance API cross-check  
  - why it matters: gives roughly 2.1k cushion above strike  
  - direct vs indirect: direct contextual evidence  
  - weight: high

- **Recent hourly Binance candles mostly held 73.8k-74.5k area**  
  - source: Binance API 1h klines pulled during run  
  - why it matters: suggests BTC is not barely peeking above 72k; it is trading in a higher range  
  - direct vs indirect: direct contextual evidence  
  - weight: medium-high

- **Polymarket ladder is internally coherent across nearby strikes**  
  - source: Polymarket market page  
  - why it matters: 70k at ~96%, 72k at ~83%, 74k at ~51% implies a plausible short-horizon distribution centered near current spot  
  - direct vs indirect: direct market-implied evidence  
  - weight: medium-high

## Evidence against the claim

- **Resolution depends on one exact future minute close, not current spot**  
  - source: contract rules  
  - why it matters: even a generally bullish path can fail if BTC dips below 72k at the resolving minute  
  - direct vs indirect: direct mechanism evidence  
  - weight: high

- **Short-dated BTC can move >2k intraday without regime change**  
  - source: recent hourly ranges from Binance data and general BTC microstructure context  
  - why it matters: the present cushion is meaningful but not invulnerable  
  - direct vs indirect: mixed direct/contextual  
  - weight: medium

## Ambiguous or mixed evidence

- CoinDesk/CME contextual surfaces confirm active institutional BTC market context but did not add much case-specific edge versus the contract plus Binance direct data.

## Conflict between inputs

There was little factual conflict. The real tension is weighting-based: how much to discount an already-above-threshold spot state because the market resolves on one exact future closing minute.

## Key assumptions

- BTC remains in roughly its current trading regime into Apr 17 noon ET.
- Binance BTC/USDT remains representative enough that exchange-specific distortion is not the dominant risk.

## Key uncertainties

- Whether macro/crypto news hits before the resolving minute.
- Whether the final hour before noon ET on Apr 17 sees unusually sharp downside volatility.

## Disconfirming signals to watch

- BTC spending sustained time below 73k before Apr 17.
- Sharp widening of downside volatility on Binance.
- Any exchange-specific operational issue affecting Binance prints or candle confidence.

## What would increase confidence

- Continued trading above ~73.5k into late Apr 16 / early Apr 17.
- Additional corroboration from derivatives/implied-vol context showing limited downside expected into the timestamp.

## Net update logic

Starting from the market, the evidence supports most of the high Yes probability because BTC already sits above the strike and nearby-strike market prices are distributionally sensible. I still shade slightly below market because this is a one-minute close-above contract, so the relevant failure mode is a timing-specific downtick rather than a broad bearish thesis.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review
