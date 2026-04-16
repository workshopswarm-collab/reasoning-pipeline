---
type: evidence_map
case_key: case-20260415-8b112bd4
dispatch_id: dispatch-case-20260415-8b112bd4-20260415T153012Z
research_run_id: 8c3a4918-75e4-4fff-ad2b-1b19b9d93499
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-16
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 70000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: "low factual conflict / moderate weighting conflict"
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-8b112bd4/researcher-analyses/2026-04-15/dispatch-case-20260415-8b112bd4-20260415T153012Z/personas/variant-view.md"]
tags: ["evidence-map", "bitcoin", "binance", "settlement-risk"]
---

# Summary

The evidence strongly supports Yes, but the variant case is that the market may be underpricing timing-specific downside and exchange-specific settlement risk by treating a ~5% buffer as virtually settled.

## Question being evaluated

Whether the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-16 will have a final close above 70,000.

## Current lean

Lean Yes, but less confidently than the market.

## Prior / starting view

Starting baseline was the market-implied ~98.5% Yes from Polymarket.

## Evidence supporting the claim

- Binance primary price checks show BTC around 73.7k, about 5.3% above the threshold. Direct; high weight.
- Sampled Binance 1-minute candles stayed well above 70k, even after a notable sharp drop. Direct; high weight.
- Contract wording uses Binance BTC/USDT close specifically, and the exchange/API data needed for that check is available and straightforward to map into ET. Direct on mechanics; medium-high weight.

## Evidence against the claim

- Crypto can move more than 5% in under a day, and the contract settles on one exact minute rather than a daily average or end-of-day close. Contextual/contract-interpretive; medium weight.
- Sampled candles included a fast drop from ~74.0k to ~73.7k within minutes, which is a reminder that intraday path risk is real. Direct on volatility, indirect on final outcome; medium weight.
- The market references Binance UI candle output specifically, leaving a small implementation/operational edge relative to API-based verification. Indirect; low-medium weight.

## Ambiguous or mixed evidence

- The strong spot cushion argues for Yes, but the same narrow settlement design means current spot can create false comfort if traders mentally substitute "currently above" for "above at the exact resolving minute."

## Conflict between inputs

There is little factual conflict. The disagreement is mostly weighting-based: whether a roughly 5% cushion with <25 hours left should imply near-certainty or merely high confidence.

## Key assumptions

- No major adverse BTC-specific or macro shock before settlement.
- Binance spot and UI close logic remain operationally consistent.
- A 5% cushion is meaningful but not equivalent to a settled outcome.

## Key uncertainties

- BTC path over the next day.
- Whether any late volatility cluster occurs near noon ET Apr 16.
- Whether exchange-specific display or settlement quirks matter at all in practice.

## Disconfirming signals to watch

- BTC/USDT falling toward 71k or below before the settlement window.
- Elevated liquidation-driven downside volatility.
- Any sign of Binance UI/data irregularity around candle timestamps.

## What would increase confidence

- Additional Binance checks closer to settlement still showing BTC several thousand dollars above 70k.
- Absence of notable macro or crypto event risk into Apr 16 noon ET.

## Net update logic

The evidence does not overturn the consensus Yes case. It mostly trims confidence from extreme-market levels because the contract is exact-minute and exchange-specific, while crypto downside moves of the required size are uncommon but very possible.

## Suggested downstream use

Use as synthesis input to avoid rounding this case to certainty merely because current spot is comfortably above the strike.