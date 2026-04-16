---
type: evidence_map
case_key: case-20260415-3f432366
dispatch_id: dispatch-case-20260415-3f432366-20260415T074424Z
research_run_id: 5f867cbd-af6a-4df1-8ff3-be500d62cdb6
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?"
driver: reliability
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: medium
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-3f432366/researcher-analyses/2026-04-15/dispatch-case-20260415-3f432366-20260415T074424Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "market-implied"]
---

# Summary

The market’s ~74.5% Yes price looks directionally defensible because BTC is already above the strike on the governing exchange, but the contract’s single-minute noon-ET close creates enough path sensitivity that the market should not be treated as near-certain.

## Question being evaluated

Will Binance BTC/USDT close above 72,000 on the 12:00 ET 1-minute candle on April 17, 2026?

## Current lean

Lean Yes, but not by enough to call the market obviously cheap.

## Prior / starting view

Starting from the market prior, Yes around three-quarters looked plausible if spot was already above the strike and there was no hidden contract complication.

## Evidence supporting the claim

- Binance spot around 73,568.70 at retrieval time.
  - direct
  - from governing exchange ecosystem
  - high weight because it means the market is already in the money by roughly 2.2%
- Recent Binance 1-minute closes clustered around the same mid-73.5k zone.
  - direct
  - medium weight because it confirms the spot level was not a stale one-off print
- CoinGecko at roughly 73,613.
  - contextual
  - medium-low weight as an independence check that the broader market was also above the strike
- Contract wording requires only one specific minute close to be above 72,000, not a sustained multi-hour hold.
  - direct rules evidence
  - medium weight because once above the strike with cushion, the hurdle is straightforward

## Evidence against the claim

- The contract is timestamp-specific: one noon-ET 1-minute close on April 17.
  - direct rules evidence
  - high weight because this creates path dependence and timing risk
- BTC can move more than 2% over two days.
  - indirect/contextual
  - high weight because the current cushion is meaningful but not huge
- The market already prices Yes richly at roughly 74.5%, limiting obvious edge from merely observing current spot > strike.
  - direct market evidence
  - medium weight

## Ambiguous or mixed evidence

- CoinGecko confirmation helps on price context, but because settlement is Binance-specific it does not directly answer the contract.
- The Polymarket page snapshot showed ~75-76%; assignment metadata said 0.745. That difference is small enough not to change the core view.

## Conflict between inputs

No major factual conflict. The main issue is weighting: how much confidence current spot should give versus the risk embedded in a narrow future timestamp.

## Key assumptions

- No major downside catalyst hits BTC before the April 17 noon ET window.
- Binance pricing at settlement remains representative and operationally usable.

## Key uncertainties

- Short-horizon BTC volatility over the next ~48 hours.
- Whether macro or crypto-specific news emerges before the settlement minute.

## Disconfirming signals to watch

- BTC loses 72,000 decisively before April 17.
- Volatility rises sharply and price action becomes unstable around noon ET windows.
- Binance-specific operational or pricing anomalies emerge.

## What would increase confidence

- BTC holding above 72,000 through multiple subsequent sessions.
- Continued price stability on Binance into the April 17 morning.

## Net update logic

The market prior survives basic scrutiny. The most important evidence is that the governing exchange already shows BTC comfortably above the strike. The main reason not to simply match or exceed the market is that the contract is narrower than a generic daily-close market and BTC’s cushion is only modest relative to typical crypto volatility.

## Suggested downstream use

Use as orchestrator synthesis input and as a compact audit trail for why the market-implied persona stayed near consensus rather than taking a contrarian stand.
