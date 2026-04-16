---
type: evidence_map
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
research_run_id: 15023e2f-188e-41f3-af65-e46f04fd7220
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: markets
entity: sol
topic: will-the-binance-sol-usdt-12-00-et-one-minute-candle-on-2026-04-19-close-above-80
question: "Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?"
driver: operational-risk
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-d529376c/researcher-analyses/2026-04-16/dispatch-case-20260416-d529376c-20260416T030247Z/personas/risk-manager.md"]
tags: ["evidence-map", "fragility", "timing-risk"]
---

# Summary

The net points to Yes being more likely than No, but the market price looks somewhat overconfident because the contract is narrow and timing-sensitive.

## Question being evaluated

Will Binance SOL/USDT print a final close above 80 on the one-minute candle corresponding to Apr 19, 2026 at 12:00 ET?

## Current lean

Lean Yes, but less strongly than the market.

## Prior / starting view

Starting view was that a spot price already in the mid-80s would make Yes likely, but an 89% market price seemed high enough to require stress-testing for timing and venue-specific fragility.

## Evidence supporting the claim

- Binance direct spot/ticker data showed SOL around 85.3 at review time.
  - Direct evidence
  - Matters because the asset is already meaningfully above the 80 threshold
  - Weight: high
- Binance daily candles for the last 10 days all closed above 80.
  - Direct evidence from the governing venue
  - Matters because it shows recent persistence above the strike, not just a one-off spike
  - Weight: medium-high
- Binance hourly closes over the last 72 hours ranged roughly 81.7 to 87.3.
  - Direct evidence from the governing venue
  - Matters because recent realized path stayed above the strike with some but not huge cushion
  - Weight: medium
- Coinbase spot around 85.335 broadly matched Binance.
  - Contextual/verification evidence
  - Matters because it reduces concern that Binance alone is showing an outlier print at review time
  - Weight: low-medium

## Evidence against the claim

- The contract settles on one exact minute, not on trend, average, daily close, or broader market strength.
  - Direct contract-mechanics risk
  - Matters because a brief dip below 80 at the wrong minute is enough to lose
  - Weight: high
- Recent hourly band shows the cushion over 80 is only a few dollars, not overwhelming for SOL.
  - Direct evidence
  - Matters because a 6%+ drawdown into noon ET is very plausible in crypto over several days
  - Weight: medium-high
- Market price near 89% may underprice path risk and operational edge cases because traders may anchor on current spot rather than exact settlement mechanics.
  - Interpretive evidence
  - Matters because this persona is explicitly testing for overconfidence
  - Weight: medium

## Ambiguous or mixed evidence

- Binance being the formal source of truth is both good and risky: good because it is specific, risky because UI/API implementation details are not exhaustively specified in the contract text.
- Crypto momentum could lift SOL further above 80, but the same high-beta character makes reversal risk nontrivial.

## Conflict between inputs

No major factual conflict across sources. The main tension is weighting-based: whether current price cushion deserves something like high-80s confidence or a more conservative low-80s probability once single-minute path risk is fully priced.

## Key assumptions

- Current cushion above 80 remains durable into Apr 19 noon ET.
- Binance venue-specific behavior remains normal.
- No major crypto-wide drawdown hits before the settlement minute.

## Key uncertainties

- Weekend macro/crypto sentiment before Apr 19 noon ET.
- How much weight to assign to recent persistence above 80 versus crypto’s short-horizon volatility.
- Any Binance display/API edge-case at settlement time.

## Disconfirming signals to watch

- SOL losing 82 and then retesting 80 before resolution.
- Broad crypto selloff that compresses alt-beta.
- Binance-specific pricing anomaly or outage.

## What would increase confidence

- Another 24-48 hours of Binance closes staying comfortably above 82-83.
- Continued cross-exchange consistency with no Binance-specific dislocation.
- A rising or stable broader crypto tape into the weekend.

## Net update logic

Current spot and recent Binance history support Yes, but the contract wording forces a discount for exact-minute settlement risk. That leaves me above 50% and still clearly pro-Yes, yet below the market’s 89% confidence.

## Suggested downstream use

Use as a cautionary synthesis input: likely Yes, but watch for overconfidence and keep contract-mechanics risk explicit in final weighting.