---
type: evidence_map
case_key: case-20260415-c0464347
dispatch_id: dispatch-case-20260415-c0464347-20260415T011958Z
research_run_id: 8d532d1f-400f-4bf0-9042-47fa51bb248e
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: operational-risk
date_created: 2026-04-15
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["macro event timing"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-c0464347/researcher-analyses/2026-04-15/dispatch-case-20260415-c0464347-20260415T011958Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "timing", "catalyst"]
---

# Summary

The evidence nets to a high-probability Yes view because current Binance BTC/USDT spot is well above 70k, the contract settles on a single exchange-specific 1-minute close, and the most obvious scheduled macro catalyst (CPI) is already behind the market. The main remaining risk is an unscheduled risk-off or exchange-specific shock that drags BTC below 70k at exactly the settlement minute.

## Question being evaluated

Will Binance BTC/USDT close above 70,000 on the 12:00 ET 1-minute candle on April 20, 2026?

## Current lean

Lean Yes, high probability but not near certainty.

## Prior / starting view

Starting view was that market 88% Yes might be directionally right but could still be overstating safety if a major catalyst remained ahead or if contract mechanics made the threshold more fragile than spot suggested.

## Evidence supporting the claim

- Binance direct-source spot and 1m klines show BTC around 74.6k now, comfortably above 70k. Direct, high weight.
- Polymarket rules specify one exchange, one pair, one minute, and strict greater-than threshold, reducing ambiguity about what needs to happen. Direct/contractual, high weight.
- BLS CPI release calendar shows major scheduled inflation data already passed on Apr. 10, reducing remaining scheduled event risk. Direct/official calendar, medium weight.
- Cointelegraph market coverage shows BTC recently trading in the 72k-76k zone, consistent with current spot being above threshold by a meaningful margin. Contextual, low-medium weight.

## Evidence against the claim

- Cointelegraph and other crypto commentary still frame the 70k-75k area as a contested zone, so a 5-6% downdraft in five days is not implausible. Contextual, medium weight.
- The contract is fragile to a single-minute print on one venue; even if BTC is generally above 70k, a noon ET wick or Binance-specific divergence could still resolve No. Direct mechanics-based, high weight.
- Weekend or geopolitically driven crypto volatility could produce a sharp risk-off move without warning. Indirect, medium weight.

## Ambiguous or mixed evidence

- CME FedWatch confirms rate-watch relevance but does not by itself show a discrete April 15-20 catalyst likely to dominate BTC pricing.
- Media coverage highlighting both bullish 90k targets and bull-trap warnings is useful context but low-authority for this narrow contract.

## Conflict between inputs

There is little factual conflict. The real disagreement is weighting-based: whether the current 74.6k spot cushion dominates, or whether one-minute settlement fragility and crypto volatility deserve more discount.

## Key assumptions

- No large scheduled catalyst remains inside the window that is likely to move BTC below 70k by itself.
- Binance remains a usable and representative source at settlement.
- BTC does not suffer a fresh broad risk-off shock large enough to erase the current cushion.

## Key uncertainties

- Path of macro/geopolitical risk through the weekend.
- ETF flow or large-holder behavior between now and settlement.
- Single-minute settlement noise on Binance.

## Disconfirming signals to watch

- BTC breaks and holds below 72k before the weekend ends.
- Sharp cross-asset risk-off move with rising yields / falling equities.
- Binance-specific outage, spread dislocation, or weird candle behavior.

## What would increase confidence

- BTC holding above 73k into the final 24-48 hours.
- Absence of new macro/geopolitical shocks.
- Continued orderly Binance spot trading close to other major venues.

## Net update logic

The main update is from possible caution about extreme market pricing toward accepting that 88% Yes is broadly reasonable. Direct source verification plus the absence of a still-pending major scheduled macro catalyst keeps the threshold looking fairly safe, though not immune to one-minute exchange-specific fragility.

## Suggested downstream use

- Orchestrator synthesis input
- forecast update
- decision-maker review