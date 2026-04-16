---
type: evidence_map
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
research_run_id: a10e6d3e-9efd-4494-9641-024a999073f7
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: Will Ethereum reach $2,400 April 13-19?
driver: liquidity
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: [ethereum]
related_drivers: [liquidity, sentiment]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [evidence-map, weekly-price-target, crypto]
---

# Summary

The evidence leans toward ETH hitting $2,400 during the week, but the main risk-manager takeaway is that the market price looks somewhat too confident relative to the remaining path risk and partially opaque source-of-truth details.

## Question being evaluated

Will Ethereum reach $2,400 at any point during the April 13-19 window under the governing Polymarket contract rules?

## Current lean

Lean yes, with high probability but not as high as the market-implied 76%.

## Prior / starting view

Starting baseline was the market-implied probability from the assignment, 0.76.

## Evidence supporting the claim

- ETH spot context is already close to the threshold.
  - Source: spot-price source note.
  - Why it matters: only ~1.6%-2.2% additional upside is needed.
  - Direct vs indirect: indirect/contextual for settlement, direct for live market state.
  - Weight: high.

- Cross-venue consistency reduces chance that current proximity is a one-off bad print.
  - Source: CoinGecko, Binance, Kraken checks.
  - Why it matters: the target is near across multiple market-data views.
  - Direct vs indirect: indirect/contextual.
  - Weight: medium.

- The market itself is pricing the `↑ 2,400` outcome richly at 0.76.
  - Source: Polymarket assignment + event surface.
  - Why it matters: informed traders also see the barrier as reachable.
  - Direct vs indirect: direct for crowd baseline, indirect for truth.
  - Weight: medium.

## Evidence against the claim

- ETH had not yet reached $2,400 in the sampled spot checks.
  - Source: spot-price source note.
  - Why it matters: the remaining move, while small, is still real.
  - Direct vs indirect: indirect/contextual.
  - Weight: medium.

- The exact Polymarket rules / source-of-truth text was not fully exposed by the fetch output.
  - Source: Polymarket source note.
  - Why it matters: contract mechanics may differ from generic exchange spot prints.
  - Direct vs indirect: direct contract-surface limitation.
  - Weight: high.

- Multi-outcome hit-price structures can create confidence illusions when traders read a single outcome price as a simple binary probability.
  - Source: Polymarket event structure.
  - Why it matters: 0.76 may overstate the cleanliness of the inference `touch probability = 76%`.
  - Direct vs indirect: direct structural caution.
  - Weight: medium.

## Ambiguous or mixed evidence

- High crypto volatility helps the touch thesis if direction is favorable, but hurts it if risk sentiment flips negative.
- Cross-source agreement is good for current price context but does not fully solve contract-resolution ambiguity.

## Conflict between inputs

There is no sharp factual conflict. The disagreement is weighting-based: whether being within ~2% of the target over a week justifies a price as high as 0.76.

## Key assumptions

- Normal weekly ETH volatility remains large enough to make a $2,400 touch likely.
- The eventual settlement source behaves broadly like the major spot references checked.
- No hidden contract nuance meaningfully changes what counts as `reach`.

## Key uncertainties

- Exact authoritative settlement source and wording.
- Near-term crypto market regime over the rest of the week.
- Whether the multi-outcome market price embeds structural distortions versus a binary framing.

## Disconfirming signals to watch

- ETH falling materially away from the target early in the week.
- Evidence that the rules use a source that stays below $2,400 despite major spot venues nearing or briefly exceeding it.
- A failed attempt at/near $2,400 followed by broad risk-off reversal.

## What would increase confidence

- Direct confirmation of the official Polymarket rules / resolution source.
- Sustained spot trade above recent highs with multiple venues converging near or above $2,400.
- Evidence that prior weekly ETH path realized volatility remains normal rather than compressed.

## Net update logic

The strongest fact is simple: ETH is already close enough that a touch is plausible on ordinary weekly movement. That keeps the probability high. The main reason not to fully endorse the 0.76 market price is risk discipline: the move has not happened yet, the contract surface is not fully transparent from current fetches, and multi-outcome market pricing can look cleaner than it really is.

## Suggested downstream use

Use this as orchestrator synthesis input and as a compact audit trail for why the risk-manager view is `roughly agree, but slightly less confident than market`.