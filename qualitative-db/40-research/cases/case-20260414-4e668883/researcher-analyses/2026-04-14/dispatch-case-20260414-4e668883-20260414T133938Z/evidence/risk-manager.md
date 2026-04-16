---
type: evidence_map
case_key: case-20260414-4e668883
dispatch_id: dispatch-case-20260414-4e668883-20260414T133938Z
research_run_id: 2f051581-1b36-4b8c-bd55-908c914853d8
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2-400-april-13-19
question: "Will Ethereum reach $2,400 April 13-19?"
driver:
date_created: 2026-04-14
agent: risk-manager
status: draft
confidence: medium
conflict_status: low-direct-conflict-high-confidence-gap
action_relevance: high
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["short-horizon-crypto-price-path-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4e668883/researcher-analyses/2026-04-14/dispatch-case-20260414-4e668883-20260414T133938Z/personas/risk-manager.md"]
tags: ["evidence-map", "risk-manager", "timing-risk", "path-risk"]
---

# Summary

The evidence leans toward a likely $2,400 touch, but not as confidently as the market implies. The core issue is path risk inside a short window, not long-run ETH direction.

## Question being evaluated

Will Ethereum trade high enough to count as having reached $2,400 during April 13-19 under the market's governing rules?

## Current lean

Likely yes, but with enough timing and source-of-truth risk to keep the estimate below the market's 92.35%.

## Prior / starting view

Starting view was that a near-threshold crypto level should usually be favored, but an extreme market price requires checking whether the threshold has already been hit and whether rule/source ambiguity exists.

## Evidence supporting the claim

- ETH is already trading very near the target; CoinGecko latest around 2392.57. Direct contextual evidence; high weight.
- Binance hourly sample shows max high around 2396.03, confirming proximity across a second source class. Direct contextual evidence; medium-high weight.
- Polymarket market pricing itself at 92.35% indicates consensus that only a small move is needed. Indirect evidence; medium weight.

## Evidence against the claim

- Independent checks did not show a verified print at or above 2400 yet. Direct contextual evidence; high weight.
- The event is a path-dependent touch within a limited calendar window, so small reversal risk matters more than in an open-ended bullish ETH thesis. Interpretive but important; high weight.
- Public extract did not provide full resolution-source text, so exact settlement-source handling of brief wicks was not fully confirmed in-note. Rule/source ambiguity; medium weight.

## Ambiguous or mixed evidence

- Being a few dollars below threshold is both bullish and fragile: it takes very little upside to win, but repeated failure just below a round number can happen.

## Conflict between inputs

There is no strong factual conflict. The main conflict is weighting-based: the market appears to treat proximity as almost enough by itself, while the risk-manager discounts for time-bounded path risk and incomplete public rule verification.

## Key assumptions

- A qualifying touch does not require a weekly close.
- A qualifying print is likely to occur on the governing source if spot remains in the high-$2390s.
- No sharp crypto-wide reversal interrupts the attempt window.

## Key uncertainties

- Exact settlement-source details from the full market rules text.
- Whether a fleeting wick above $2,400 appears during the remaining window.

## Disconfirming signals to watch

- A rejection from the 2390s followed by multi-session drift lower.
- Verified rule text implying a stricter source/methodology than assumed.
- ETH underperforming BTC while broader crypto weakens.

## What would increase confidence

- Full explicit verification of the market's governing source and trigger logic.
- A confirmed trade print above $2,400 on the governing source.

## Net update logic

The evidence kept the lean positive because ETH is already extremely close to the threshold. But the additional verification pass showed the threshold had not yet been crossed in the checked independent sources, which is enough to keep the estimate meaningfully below the market's near-certainty.

## Suggested downstream use

Use as synthesis input and for retrospective evaluation of whether extreme short-window market prices systematically underprice path/timing risk near round-number thresholds.