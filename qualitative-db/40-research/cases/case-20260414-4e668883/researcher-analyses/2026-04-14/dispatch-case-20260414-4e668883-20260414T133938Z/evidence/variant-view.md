---
type: evidence_map
case_key: case-20260414-4e668883
dispatch_id: dispatch-case-20260414-4e668883-20260414T133938Z
research_run_id: 047a346a-4787-42a7-9ab2-4be7aa9aea84
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: protocols
entity: ethereum
topic: eth-2400-april-13-19
question: "Will Ethereum reach $2,400 April 13-19?"
driver:
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["short-window-threshold-touch-dynamics"]
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "ethereum", "threshold-market"]
---

# Summary

The market is probably right directionally, but it may be modestly too confident. The neglected issue is not whether ETH can approach $2,400; it is whether a short-dated touch through a round-number resistance should really be priced near nine-in-ten before the threshold is actually printed on the governing source.

## Question being evaluated

Will Ethereum reach $2,400 at any point during the April 13-19 market window?

## Current lean

Lean yes, but less strongly than the market: about 80% rather than 89%.

## Prior / starting view

Starting view was that a threshold only a few percent above spot in a crypto market over nearly a week would usually deserve a high probability, but an 89% price required checking whether the market was collapsing "very likely" into "almost inevitable."

## Evidence supporting the claim

- Polymarket market page: the relevant outcome was priced around 89%, showing strong crowd confidence and suggesting the threshold is viewed as quite reachable. Weight: medium. Direct for market baseline, indirect for truth.
- TradingView ETHUSD page: ETH was described above roughly $2,350 with a spike near $2,395, leaving only a very small remaining move to touch $2,400. Weight: high. Contextual but highly relevant to distance-to-threshold.
- TradingView resistance stack: resistance levels were listed at $2,380 and $2,400, implying the threshold sits inside the active short-term range rather than far outside it. Weight: medium. Contextual.

## Evidence against the claim

- The same TradingView snapshot explicitly frames $2,400 as resistance, so the threshold is near enough to matter but also near enough to reject price repeatedly. Weight: high.
- The Polymarket fetched text did not expose the exact governing rules, so there remains some ambiguity around what precise print/source counts. Weight: low to medium.
- Short-dated path dependence matters: being close is not the same as touching, especially around psychologically salient round numbers. Weight: medium.

## Ambiguous or mixed evidence

- Bullish short-term momentum indicators help the yes case, but over very short horizons they can also be a late-stage reflection of a move that is already partially exhausted.
- Market consensus itself is informative, but it may also reflect crowd herding once price gets near a visible threshold.

## Conflict between inputs

There is little factual conflict. The disagreement is mostly weighting-based: how much to trust a high crowd probability versus the residual miss risk created by resistance and short-window timing.

## Key assumptions

- The market resolves on any qualifying intraperiod touch rather than a weekly close.
- The accessible contextual price snapshot is directionally representative of true current conditions.
- Round-number resistance can preserve a meaningful miss probability even when spot is close.

## Key uncertainties

- Exact governing source and print methodology for settlement.
- Whether the near-$2,395 move is still current enough to matter by the time of decision use.
- Whether a broader crypto catalyst emerges during the remaining window.

## Disconfirming signals to watch

- Verified print above $2,400 on the governing market source.
- Decisive breakout through $2,380 followed by continuation.
- Fresh positive regulatory, ETF, or macro-beta catalyst that broadens crypto upside.

## What would increase confidence

- Full readable access to the market's rules section and governing source.
- An independent price source confirming the same near-threshold setup.
- Intraday tape showing repeated failures versus successful acceptance above nearby resistance.

## Net update logic

The evidence supports a yes lean because the threshold is very close to spot and the available contextual source shows ETH already nearly reached it. The only genuinely variant contribution is that the market price seems to compress the remaining execution risk too aggressively for a short-dated, round-number threshold market. So the final lean remains yes, but with a moderate haircut from market confidence.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit trail for why the variant persona did not force a hard contrarian call despite identifying a credible overconfidence mechanism.