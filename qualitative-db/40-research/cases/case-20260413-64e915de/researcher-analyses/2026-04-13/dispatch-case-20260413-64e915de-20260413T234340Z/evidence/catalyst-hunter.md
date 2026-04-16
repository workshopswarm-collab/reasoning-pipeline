---
type: evidence_map
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
research_run_id: 843133e1-9716-41f9-8bf5-84be28b858f9
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: protocols
entity: ethereum
topic: "competing catalyst paths for ETH to touch $2,400 during Apr 13-19"
question: "Will Ethereum reach $2,400 April 13-19?"
driver: liquidity
date_created: 2026-04-13
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: ["liquidity", "macro", "capital-markets"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-64e915de/researcher-analyses/2026-04-13/dispatch-case-20260413-64e915de-20260413T234340Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "ethereum", "catalyst-analysis", "threshold-market"]
---

# Summary

The evidence leans toward a hit, but mostly because ETH already nearly touched the threshold and because the remaining catalyst set is dominated by flow and momentum rather than by a missing binary event. The case is not "certain" because round-number resistance and the absence of a fresh scheduled upside catalyst can still prevent the final ~$25 move.

## Question being evaluated

Will ETH trade at or above $2,400 at any point during the Apr 13-19 resolution window?

## Current lean

Moderate lean yes.

## Prior / starting view

Starting from the market price alone, the assignment implied a very high baseline near 90.5%, which looked aggressive for a one-week threshold market unless spot was already close to target.

## Evidence supporting the claim

- Coinbase spot data had ETH around $2,374 late on Apr 13 and the same-day high at $2,395.
  - direct evidence
  - high weight
  - matters because the market only needs a marginal additional move, not a full trend reversal.
- Hourly Coinbase candles showed strong late-session acceleration from the low $2,230s to the mid $2,370s.
  - direct evidence
  - medium-high weight
  - matters because threshold-touch markets are path dependent and momentum can generate wick overshoots.
- Official calendars show no FOMC meeting inside Apr 13-19; the major CPI release already happened on Apr 10.
  - contextual evidence
  - medium weight
  - matters because there is no obvious scheduled macro headwind inside the actual window.
- CME documentation shows established weekly Ether derivatives for short-term event risk.
  - contextual evidence
  - medium weight
  - matters because short-dated derivatives can amplify threshold-seeking price action.

## Evidence against the claim

- The strongest disconfirming point is that ETH already failed to print $2,400 despite reaching $2,395 on day one.
  - direct evidence
  - high weight
  - matters because nearby resistance may be real, and threshold markets can get trapped just below round numbers.
- The biggest scheduled macro catalyst already passed before the window began.
  - contextual evidence
  - medium weight
  - matters because fresh upside information may be limited during the rest of the week.
- COT release on Apr 17 is lagged and may not provide enough new information to drive a decisive repricing.
  - contextual evidence
  - low-medium weight
  - matters because one visible calendar item inside the window may be low-information.

## Ambiguous or mixed evidence

- Polymarket page fetch gave headline probabilities but did not expose full rules text cleanly in the fetched extract, so source-of-truth wording needs to be treated carefully.
- CME weekly options existence cuts both ways: they can support upside extension or facilitate hedging and pinning just below strike-like round numbers.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: whether already reaching $2,395 makes a touch almost inevitable or only somewhat more likely than not.

## Key assumptions

- The relevant resolution source will count a qualifying print if ETH reaches $2,400 on the market's governing benchmark.
- Near-threshold momentum is more important than the absence of a new scheduled protocol catalyst.
- No adverse macro or crypto headline interrupts the move.

## Key uncertainties

- Exact resolution source mechanics on Polymarket if exchange prints diverge.
- Whether the current move is a one-day overshoot rather than the start of sustained follow-through.
- How much round-number resistance matters near $2,400.

## Disconfirming signals to watch

- ETH fails to retest $2,370-$2,395 over the next 24-48 hours.
- Spot reverses below roughly $2,330 with risk appetite fading.
- Clarified market rules show a more restrictive reference source than expected.

## What would increase confidence

- Confirmation from the Polymarket rules/source-of-truth text naming a broad or easily reachable pricing reference.
- A confirmed trade above $2,380-$2,390 on multiple major venues after the initial spike.
- Sustained strength in broader crypto/risk markets through midweek.

## Net update logic

The biggest update was from actual path proximity: ETH was not merely trending upward, it had already reached $2,395. That moved the case from "extreme market price may be too rich" toward "yes is favored, but not quite as much as the market says." Macro calendar work mainly served as a negative screen, showing no obvious new catalyst was missing and no immediate FOMC event sat inside the week.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, with emphasis on path dependence and the distinction between "favored" and "90%+ near certainty."