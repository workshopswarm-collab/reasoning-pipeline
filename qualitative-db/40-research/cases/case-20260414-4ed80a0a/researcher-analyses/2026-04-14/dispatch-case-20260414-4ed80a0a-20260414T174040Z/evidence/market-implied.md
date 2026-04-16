---
type: evidence_map
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
research_run_id: 11f1ee38-19b5-4660-8255-0cc1fdcfb859
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2-400-april-13-19
question: "Will Ethereum reach $2,400 April 13-19?"
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-venue-specific-resolution-dependence"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/market-implied.md"]
tags: ["evidence-map", "source-of-truth", "verification"]
driver:
---

# Summary

The net evidence strongly supports the market's extreme Yes pricing because the governing venue-specific threshold appears already to have been hit on Binance inside the relevant window.

## Question being evaluated

Will Ethereum reach $2,400 during April 13-19 under this contract's specific settlement rules?

## Current lean

Strong Yes lean; near-settled in practical terms.

## Prior / starting view

Market prior was already very high at 91.6%, suggesting traders believed a qualifying print had likely already occurred or was overwhelmingly likely.

## Evidence supporting the claim

- Polymarket rules specify Binance ETH/USDT 1m candle highs as the governing source.
  - source: source note on Polymarket rules
  - why it matters causally: defines what counts
  - direct or indirect: direct
  - weight: very high

- Binance ETHUSDT 1h kline data shows a high of 2415.50 on 2026-04-14T14:00:00Z.
  - source: Binance klines source note
  - why it matters causally: if Binance recorded a high above 2400 during the contract window, the threshold condition is likely already met
  - direct or indirect: direct to venue, slightly indirect to exact 1m confirmation
  - weight: very high

- The threshold was exceeded by more than trivial noise (+15.5 above 2400), reducing concern that this was a tiny rounding edge.
  - source: Binance klines source note
  - why it matters causally: margin above threshold makes an accidental false positive less plausible
  - direct or indirect: direct
  - weight: high

## Evidence against the claim

- The verification pass here used Binance 1h candles rather than the exact 1m candle series named by the contract.
  - source: Binance klines source note
  - why it matters causally: a purist audit would prefer direct minute-level evidence
  - direct or indirect: direct limitation
  - weight: medium

- CoinGecko's 7-day contextual high was below 2400, showing that generic multi-venue price context can differ from the settlement venue.
  - source: Binance/CoinGecko source note
  - why it matters causally: reminds reviewer not to confuse contextual vendor data with venue-specific settlement data
  - direct or indirect: indirect/contextual
  - weight: low to medium

## Ambiguous or mixed evidence

- The market price at 91.6% rather than ~99% could reflect either residual resolution-process caution, liquidity frictions, or traders not fully trusting that the qualifying Binance print will cleanly map to settlement.

## Conflict between inputs

There is no major factual conflict once venue specificity is respected. The apparent tension is between contextual aggregator data and the named settlement venue, which is a source hierarchy issue rather than a true factual contradiction.

## Key assumptions

- Binance 1h high above 2400 implies at least one underlying 1m high above 2400 in that hour.
- The observed timestamp lies inside the contract's ET date window.

## Key uncertainties

- Exact minute-level candle audit was not captured in this artifact.
- Whether Polymarket could face any minor rule-interpretation dispute around data display versus API output.

## Disconfirming signals to watch

- Direct 1m Binance data contradicting the hourly print implication.
- Official dispute commentary suggesting the observed print is not eligible.
- Market repricing sharply down after broader participants inspect the rule-source mapping.

## What would increase confidence

- A saved Binance 1m candle extract for the relevant hour.
- A visible Polymarket/UMA settlement trail confirming the qualifying candle.

## Net update logic

Starting from a high market prior, the rules review explained why venue-specific intraperiod highs mattered more than headline ETH price context. The additional Binance verification then made the market's extreme confidence look justified and arguably still not fully maxed out.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- retrospective evaluation of source-of-truth handling in threshold crypto markets